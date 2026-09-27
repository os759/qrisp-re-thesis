"""Validate the structured model output against the requirement schema.

Three independent checks are applied to every record, in this order:

1. Schema check. The record is matched against config/requirement_schema_v2.json
   using JSON Schema. This catches missing fields, wrong value sets and any
   field the model invented on its own.
2. Consistency check. evidence_strength is recomputed from the covered
   parts and from source_form by the rules of decision E6. A value the
   model set freely is rejected if it does not follow those rules.
3. Excerpt check. Every excerpt in the evidence list has to occur literally
   in the prepared dataset, in the place the entry names. This catches
   invented quotations, which the schema alone cannot detect. The check
   follows the excerpt rules of the prompt: no removed line, no hunk
   header, no joining across either, and for a review comment only the
   comment text. Tightened on 2026-09-24, addendum to E10, point 5.
   Loosened on 2026-09-27, addendum to E10 of that day, part 1, point 3:
   whitespace at the start and end of an excerpt is tolerated, because
   the prompt demands exact spaces only inside. Not tolerated is a kept
   leading space of a context line (context_marker_kept), and the rest
   must still have the prompt's minimum length of 10 characters.
   The model saw the prose with mentions replaced, decision E9. The same
   replacement is therefore applied to the dataset before the comparison.
   Pass --mentions-map for a run whose input was built that way.

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

from pseudonymise import load_mapping, mask

DEFAULT_SCHEMA = Path("config/requirement_schema_v2.json")

# A patch line carries a leading marker: '+' added, '-' removed, ' ' context.
# An excerpt quoted from a diff never contains these markers, so they are
# removed before the comparison. Removed lines and hunk headers (@@) must
# not be quoted, and an excerpt must not join lines across them (prompt
# version 1). They are therefore replaced by BARRIER, a character no
# excerpt contains.
DIFF_KEEP_PREFIXES = ("+", " ")
DIFF_FILE_HEADERS = ("+++", "---")
BARRIER = "\x00"

# Lower bound for the length of an excerpt in the prompt (field excerpt).
# It also applies to the rest left after removing edge whitespace.
MIN_EXCERPT_LENGTH = 10


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate model output against the requirement schema.")
    parser.add_argument("--input", required=True,
                        help="JSONL file with one model output object per line.")
    parser.add_argument("--dataset", default=None,
                        help="Prepared dataset. Enables the excerpt check.")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA),
                        help="Schema file. Default: config/requirement_schema_v2.json")
    parser.add_argument("--mentions-map", default=None,
                        help="Mapping written by build_prompt_input.py. Applies "
                             "the same replacement to the dataset, decision E9.")
    parser.add_argument("--allowlist", default="",
                        help="Comma separated names left unchanged, as in "
                             "config/model_input.toml.")
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

    Added and context lines are kept without their first character.
    Between two kept lines, a removed line or a hunk header becomes one
    BARRIER line, so no excerpt can span it. File headers (--- and +++)
    are only recognised before the first hunk header; after it, a line
    starting with +++ is an added line whose text starts with ++. Any
    other line, such as a truncation mark, is dropped.
    """
    kept: list[str] = []
    in_hunk = False
    barrier_pending = False
    for line in patch.split("\n"):
        if not in_hunk and line.startswith(DIFF_FILE_HEADERS):
            continue
        if line.startswith("@@") or (in_hunk and line.startswith("-")):
            in_hunk = True
            barrier_pending = True
        elif in_hunk and line.startswith(DIFF_KEEP_PREFIXES):
            if barrier_pending and kept:
                kept.append(BARRIER)
            barrier_pending = False
            kept.append(line[1:])
        elif not in_hunk and line.startswith(DIFF_KEEP_PREFIXES):
            kept.append(line[1:])  # a patch without a hunk header
    return "\n".join(kept)


def schema_errors(record: dict[str, Any],
                  validator: Draft202012Validator) -> list[str]:
    """Return one readable message per schema violation."""
    messages = []
    for error in sorted(validator.iter_errors(record), key=lambda e: list(e.path)):
        where = "/".join(str(part) for part in error.path) or "<root>"
        messages.append(f"schema: {where}: {error.message}")
    return messages


def haystacks_for(item: dict[str, Any],
                  pull: dict[str, Any],
                  mapping: dict[str, str] | None = None,
                  allowlist: set[str] | None = None) -> list[str]:
    """Return the texts an excerpt may legitimately come from.

    With a mapping, prose is masked exactly as it was for the model. The
    diff and the diff context of a review comment stay untouched, because
    they were never masked either.
    """
    location = item.get("location")
    locator = item.get("locator")

    def prose(text: str) -> str:
        if mapping is None:
            return text or ""
        return mask(text or "", mapping, allowlist or set())

    if location == "title":
        return [prose(pull.get("title"))]
    if location == "body":
        return [prose(pull.get("body"))]
    if location == "issue_comment":
        return [prose(c.get("body")) for c in pull.get("issue_comments", [])
                if locator in (None, str(c.get("id")))]
    if location == "review_comment":
        # Only the comment text; the prompt forbids quoting the code context.
        return [prose(c.get("body")) for c in pull.get("review_comments", [])
                if locator in (None, str(c.get("id")))]
    if location == "diff":
        return [strip_diff_markers(f.get("patch") or "")
                for f in pull.get("files", [])
                if locator in (None, f.get("filename"))]
    return []


def context_marker_kept(item: dict[str, Any], pull: dict[str, Any]) -> bool:
    """Rule of the addendum to E10 of 2026-09-27, part 1, conditions a to c.

    a) The excerpt comes from a diff.
    b) Its first line, without trailing whitespace, starts with a space.
       A first line of whitespace only becomes empty here and fails b.
    c) In the named file, after a hunk header, a line starts with exactly
       this first line. Because the first line starts with a space, such a
       line is always a context line with its marker still in place.
    """
    if item.get("location") != "diff":
        return False
    first = (item.get("excerpt") or "").split("\n", 1)[0].rstrip()
    if not first.startswith(" "):
        return False
    locator = item.get("locator")
    for file in pull.get("files", []):
        if locator not in (None, file.get("filename")):
            continue
        in_hunk = False
        for line in (file.get("patch") or "").split("\n"):
            if line.startswith("@@"):
                in_hunk = True
            elif in_hunk and line.startswith(first):
                return True
    return False


def excerpt_found(item: dict[str, Any], pull: dict[str, Any],
                  candidates: list[str]) -> bool:
    """Whether an excerpt counts as found in one of its candidate texts.

    Literal occurrence, or since 2026-09-27 occurrence without edge
    whitespace (addendum to E10 of that day, part 1, point 3).
    """
    excerpt = item.get("excerpt") or ""
    if any(excerpt in text for text in candidates):
        return True
    core = excerpt.strip()
    return (len(core) >= MIN_EXCERPT_LENGTH
            and any(core in text for text in candidates)
            and not context_marker_kept(item, pull))


def excerpt_errors(record: dict[str, Any],
                   dataset: dict[int, dict[str, Any]],
                   mapping: dict[str, str] | None = None,
                   allowlist: set[str] | None = None) -> list[str]:
    """Check that every excerpt occurs literally in its named source."""
    messages = []
    pull_number = record.get("pull_number")
    pull = dataset.get(pull_number)
    if pull is None:
        return [f"excerpt: pull {pull_number} not in the dataset"]

    for requirement in record.get("requirements", []):
        identifier = requirement.get("id", "<no id>")
        for position, item in enumerate(requirement.get("evidence", []), start=1):
            candidates = haystacks_for(item, pull, mapping, allowlist)
            if not candidates:
                messages.append(
                    f"excerpt: {identifier} evidence {position}: no text found for "
                    f"location {item.get('location')} and locator {item.get('locator')}")
                continue
            if not excerpt_found(item, pull, candidates):
                messages.append(
                    f"excerpt: {identifier} evidence {position}: excerpt does not "
                    f"occur literally in {item.get('location')} {item.get('locator')}")
    return messages


def required_parts(ears_pattern: str) -> set[str]:
    """Which parts the chosen EARS pattern has to have covered.

    System name and system response are mandatory for every pattern; see
    the rules on mandatory parts in the formulation probe of package C.
    The conditional patterns add the part their keyword introduces.
    """
    parts = {"system_name", "system_response"}
    if ears_pattern in ("state_driven", "optional_feature"):
        parts.add("precondition")
    elif ears_pattern in ("event_driven", "unwanted_behaviour"):
        parts.add("trigger")
    elif ears_pattern == "complex":
        parts.update({"precondition", "trigger"})
    return parts


def derive_evidence_strength(requirement: dict[str, Any]) -> str:
    """Recompute the evidence strength by the rules of decision E6."""
    covered: set[str] = set()
    for item in requirement.get("evidence", []):
        covered.update(item.get("supports", []))
    if not required_parts(requirement.get("ears_pattern", "")) <= covered:
        return "insufficient"
    return ("direct" if requirement.get("source_form") == "prescriptive"
            else "indirect")


def consistency_errors(record: dict[str, Any]) -> list[str]:
    """Reject an evidence strength that does not follow from the evidence."""
    messages = []
    for requirement in record.get("requirements", []):
        identifier = requirement.get("id", "<no id>")
        expected = derive_evidence_strength(requirement)
        stated = requirement.get("evidence_strength")
        if stated != expected:
            covered = sorted({part for item in requirement.get("evidence", [])
                              for part in item.get("supports", [])})
            missing = sorted(required_parts(requirement.get("ears_pattern", ""))
                             - set(covered))
            messages.append(
                f"consistency: {identifier}: evidence_strength is {stated}, "
                f"the rules of E6 give {expected} "
                f"(covered: {covered or 'none'}; missing: {missing or 'none'}; "
                f"source_form: {requirement.get('source_form')})")
    return messages


def check_record(record: dict[str, Any],
                 validator: Draft202012Validator,
                 dataset: dict[int, dict[str, Any]] | None,
                 mapping: dict[str, str] | None = None,
                 allowlist: set[str] | None = None) -> list[str]:
    """Run all checks on one record and stop at the first that reports."""
    problems = schema_errors(record, validator)
    if problems:
        return problems
    problems = consistency_errors(record)
    if problems:
        return problems
    if dataset is None:
        return []
    return excerpt_errors(record, dataset, mapping, allowlist)


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

    mapping = load_mapping(Path(arguments.mentions_map)) if arguments.mentions_map else None
    allowlist = {name.strip().lower()
                 for name in arguments.allowlist.split(",") if name.strip()}
    if dataset is not None and mapping is None:
        print("Note: no --mentions-map given, the dataset is compared unmasked.")

    records = 0
    rejected = 0
    requirements = 0

    for line_number, record in read_jsonl(Path(arguments.input)):
        records += 1
        problems = check_record(record, validator, dataset, mapping, allowlist)

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
