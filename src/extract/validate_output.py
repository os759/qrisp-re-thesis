"""Validate the structured model output against the requirement schema.

Two independent checks are applied to every record:

1. Schema check. The record is matched against config/requirement_schema_v1.json
   using JSON Schema. This catches missing fields, wrong value sets and any
   field the model invented on its own.
2. Excerpt check. Every source_excerpt has to occur literally in the prepared
   dataset, in the record named by the source field. This catches invented
   quotations, which the schema alone cannot detect.

Work package E, bachelor thesis. Research questions FF1 and FF2.

Run from the project root:

    python src/extract/validate_output.py \
      --input data/processed/extraction_<date>.jsonl \
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterator

from jsonschema import Draft202012Validator

DEFAULT_SCHEMA = Path("config/requirement_schema_v1.json")

# A patch line carries a leading marker: '+' added, '-' removed, ' ' context.
# An excerpt quoted from a diff never contains these markers, so they are
# removed before the comparison. Removed lines are dropped: they are no longer
# part of the code after the change.
DIFF_KEEP_PREFIXES = ("+", " ")
DIFF_FILE_HEADERS = ("+++", "---")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate model output against the requirement schema.")
    parser.add_argument("--input", required=True,
                        help="JSONL file with one model output object per line.")
    parser.add_argument("--dataset", default=None,
                        help="Prepared dataset. Enables the excerpt check.")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA),
                        help="Schema file. Default: config/requirement_schema_v1.json")
    parser.add_argument("--quiet", action="store_true",
                        help="Print the summary only.")
    return parser.parse_args()


def read_jsonl(path: Path) -> Iterator[tuple[int, dict[str, Any]]]:
    """Yield (line number, object) for every non-empty line."""
    with path.open(encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, start=1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                yield line_number, json.loads(raw)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"{path}, line {line_number}: not valid JSON: {error}") from error


def strip_diff_markers(patch: str) -> str:
    """Return the patch text without the leading diff markers.

    Added and context lines are kept without their first character. Removed
    lines, hunk headers and file headers are dropped.
    """
    kept: list[str] = []
    for line in patch.split("\n"):
        if line.startswith(DIFF_FILE_HEADERS):
            continue
        if line.startswith(DIFF_KEEP_PREFIXES):
            kept.append(line[1:])
    return "\n".join(kept)


def schema_errors(record: dict[str, Any],
                  validator: Draft202012Validator) -> list[str]:
    """Return one readable message per schema violation."""
    messages = []
    for error in sorted(validator.iter_errors(record), key=lambda e: list(e.path)):
        where = "/".join(str(part) for part in error.path) or "<root>"
        messages.append(f"schema: {where}: {error.message}")
    return messages


def haystacks_for(source: dict[str, Any],
                  pull: dict[str, Any]) -> list[str]:
    """Return the texts an excerpt may legitimately come from."""
    location = source.get("location")
    locator = source.get("locator")

    if location == "title":
        return [pull.get("title") or ""]
    if location == "body":
        return [pull.get("body") or ""]
    if location == "issue_comment":
        return [c.get("body") or "" for c in pull.get("issue_comments", [])
                if locator in (None, str(c.get("id")))]
    if location == "review_comment":
        return [(c.get("body") or "") + "\n" + (c.get("diff_hunk") or "")
                for c in pull.get("review_comments", [])
                if locator in (None, str(c.get("id")))]
    if location == "diff":
        return [strip_diff_markers(f.get("patch") or "")
                for f in pull.get("files", [])
                if locator in (None, f.get("filename"))]
    return []


def excerpt_errors(record: dict[str, Any],
                   dataset: dict[int, dict[str, Any]]) -> list[str]:
    """Check that every excerpt occurs literally in its named source."""
    messages = []
    for requirement in record.get("requirements", []):
        identifier = requirement.get("id", "<no id>")
        source = requirement.get("source") or {}
        excerpt = requirement.get("source_excerpt") or ""

        pull_number = source.get("pull_number")
        if pull_number != record.get("pull_number"):
            messages.append(
                f"excerpt: {identifier}: source points to pull {pull_number}, "
                f"record is pull {record.get('pull_number')}")
            continue

        pull = dataset.get(pull_number)
        if pull is None:
            messages.append(
                f"excerpt: {identifier}: pull {pull_number} not in the dataset")
            continue

        candidates = haystacks_for(source, pull)
        if not candidates:
            messages.append(
                f"excerpt: {identifier}: no text found for location "
                f"{source.get('location')} and locator {source.get('locator')}")
            continue

        if not any(excerpt in text for text in candidates):
            messages.append(
                f"excerpt: {identifier}: excerpt does not occur literally in "
                f"{source.get('location')} {source.get('locator')}")
    return messages


def load_dataset(path: Path) -> dict[int, dict[str, Any]]:
    return {record["number"]: record for _, record in read_jsonl(path)}


def main() -> int:
    arguments = parse_arguments()

    schema = json.loads(Path(arguments.schema).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    dataset = load_dataset(Path(arguments.dataset)) if arguments.dataset else None
    if dataset is None:
        print("Note: no --dataset given, the excerpt check is skipped.")

    records = 0
    rejected = 0
    requirements = 0

    for line_number, record in read_jsonl(Path(arguments.input)):
        records += 1
        problems = schema_errors(record, validator)
        if not problems and dataset is not None:
            problems = excerpt_errors(record, dataset)

        if problems:
            rejected += 1
            if not arguments.quiet:
                print(f"line {line_number}, pull {record.get('pull_number')}:")
                for problem in problems:
                    print(f"  {problem}")
        else:
            requirements += len(record.get("requirements", []))

    print(f"\nRecords read: {records}")
    print(f"Records rejected: {rejected}")
    print(f"Requirements in accepted records: {requirements}")
    return 1 if rejected else 0


if __name__ == "__main__":
    sys.exit(main())
