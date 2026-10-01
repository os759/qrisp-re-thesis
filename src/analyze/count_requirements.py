"""Count the requirements of one extraction run, without printing content.

Work package G, step 1. Research questions FF4 and FF1; also the measure
M2 (unsupported rate) of decision F3 for FF3.

Every rule used here is fixed in docs/entscheidungen.md before counting:

* Base set (F3, M2; G1 point 1): the requirements in all records that
  pass the schema check.
* Found evidence (F3, M2 condition 1; G1 point 2): validate_output.py
  accepts the excerpt (excerpt_found), or diagnose_excerpts.py assigns
  its rejection to a cause of rule 1 (classify). Causes of rule 2 or 3
  count as not found; the author assigned all rule 3 cases of the full
  run to rule 2 (addendum to E10 of 2026-09-28, part 4).
* M2 unsupported (F3): no evidence found, or the evidence strength
  derived from all evidence (derive_evidence_strength) is insufficient.
* Strength for FF4 (G1 point 3): derive_evidence_strength over the found
  evidence only.
* Supported for FF4 (G1 point 4): that strength is direct or indirect.

The script has no check rule of its own. It imports the checks from
validate_output.py and diagnose_excerpts.py and only counts. Excerpt
statistics cover all records, as in diagnose_excerpts.py; requirement
statistics cover records that pass the schema check.

Nothing of an excerpt, a requirement text, a diff or a comment is
printed or written: only counts, value names, checksums and the commit.

Run from the project root:

    python src/analyze/count_requirements.py \\
      --input data/processed/extraction_2026-09-25_full_v2.jsonl \\
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \\
      --model-input data/processed/model_input_2026-09-19.jsonl \\
      --mentions-map data/interim/mention_map.json \\
      --allowlist "jaspify,jax,pytest,rus" \\
      --output experiments/requirement_counts_2026-09-25_full_v2.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

SRC = Path(__file__).resolve().parents[1]
for _sub in ("extract", "prepare"):
    if str(SRC / _sub) not in sys.path:
        sys.path.insert(0, str(SRC / _sub))

from jsonschema import Draft202012Validator  # noqa: E402

from diagnose_excerpts import CAUSES, classify, files_in_block, load_blocks  # noqa: E402
from pseudonymise import load_mapping  # noqa: E402
from validate_output import (DEFAULT_SCHEMA, derive_evidence_strength,  # noqa: E402
                             excerpt_found, haystacks_for, load_dataset,
                             read_jsonl)

SUPPORTED = ("direct", "indirect")


def evidence_status(item: dict[str, Any], pull: dict[str, Any] | None,
                    shown: set[str], mapping: dict[str, str] | None,
                    allowlist: set[str]) -> tuple[bool, int | None]:
    """Return (found, rule) for one evidence entry.

    rule is None for an excerpt validate_output.py accepts, otherwise the
    rule of the cause diagnose_excerpts.py assigns. Found means accepted
    or rule 1 (F3, M2 condition 1; G1 point 2).
    """
    if pull is None:
        return False, CAUSES["locator_not_found"][0]
    candidates = haystacks_for(item, pull, mapping, allowlist)
    if candidates and excerpt_found(item, pull, candidates):
        return True, None
    rule = CAUSES[classify(item, pull, shown, mapping, allowlist)][0]
    return rule == 1, rule


def assess_requirement(requirement: dict[str, Any],
                       found_flags: list[bool]) -> dict[str, Any]:
    """Apply M2 (F3) and G1 to one requirement."""
    evidence = requirement.get("evidence", [])
    found_items = [item for item, found in zip(evidence, found_flags) if found]
    strength_all = derive_evidence_strength(requirement)
    strength_ff4 = derive_evidence_strength({**requirement, "evidence": found_items})
    no_evidence_found = not found_items
    insufficient_all = strength_all == "insufficient"
    return {
        "type": requirement.get("type"),
        "security_relevant": bool(requirement.get("security_relevant")),
        "strength_stated": requirement.get("evidence_strength"),
        "strength_all": strength_all,
        "strength_ff4": strength_ff4,
        "no_evidence_found": no_evidence_found,
        "insufficient_all": insufficient_all,
        "m2_unsupported": no_evidence_found or insufficient_all,
        "ff4_supported": strength_ff4 in SUPPORTED,
        "partly_found": bool(found_items) and len(found_items) < len(evidence),
    }


def _list_of_dicts(value: Any) -> list[dict[str, Any]]:
    return [entry for entry in value if isinstance(entry, dict)] \
        if isinstance(value, list) else []


def count_run(records: list[dict[str, Any]], validator: Draft202012Validator,
              dataset: dict[int, dict[str, Any]], blocks: dict[int, str],
              mapping: dict[str, str] | None = None,
              allowlist: set[str] | None = None) -> dict[str, Any]:
    """Count records, excerpts and requirements of one run."""
    allowlist = allowlist or set()
    status: Counter = Counter()
    excerpts: Counter = Counter()
    by_rule: Counter = Counter()
    assessed: list[dict[str, Any]] = []
    schema_valid = 0

    for record in records:
        valid = not any(True for _ in validator.iter_errors(record))
        if valid:
            schema_valid += 1
            status[record["processing_status"]] += 1
        number = record.get("pull_number")
        pull = dataset.get(number)
        shown = files_in_block(blocks.get(number, ""))
        for requirement in _list_of_dicts(record.get("requirements", [])):
            flags = []
            for item in _list_of_dicts(requirement.get("evidence", [])):
                found, rule = evidence_status(item, pull, shown, mapping, allowlist)
                flags.append(found)
                excerpts["total"] += 1
                if rule is None:
                    excerpts["accepted"] += 1
                else:
                    excerpts["rejected"] += 1
                    by_rule[str(rule)] += 1
            if valid:
                assessed.append(assess_requirement(requirement, flags))

    return summarise(len(records), schema_valid, status, excerpts, by_rule, assessed)


def summarise(read: int, schema_valid: int, status: Counter, excerpts: Counter,
              by_rule: Counter, assessed: list[dict[str, Any]]) -> dict[str, Any]:
    """Turn the assessed requirements into counts only."""
    def count(key: str, rows: list[dict[str, Any]]) -> dict[str, int]:
        return dict(sorted(Counter(str(row[key]) for row in rows).items()))

    def flag(key: str, rows: list[dict[str, Any]]) -> int:
        return sum(1 for row in rows if row[key])

    security = [row for row in assessed if row["security_relevant"]]
    type_by_security: dict[str, dict[str, int]] = {}
    for row in assessed:
        cell = type_by_security.setdefault(str(row["type"]), {"true": 0, "false": 0})
        cell["true" if row["security_relevant"] else "false"] += 1

    return {
        "records": {
            "read": read,
            "schema_valid": schema_valid,
            "schema_invalid": read - schema_valid,
            "processing_status_schema_valid": dict(sorted(status.items())),
        },
        "excerpts_all_records": {
            "total": excerpts["total"],
            "accepted": excerpts["accepted"],
            "rejected": excerpts["rejected"],
            "rejected_by_rule": dict(sorted(by_rule.items())),
        },
        "requirements": {
            "total": len(assessed),
            "by_type": {name: cell["true"] + cell["false"]
                        for name, cell in sorted(type_by_security.items())},
            "security_relevant": {"true": len(security),
                                  "false": len(assessed) - len(security)},
            "type_by_security_relevant": dict(sorted(type_by_security.items())),
            "strength_stated_by_model": count("strength_stated", assessed),
            "strength_from_all_evidence": count("strength_all", assessed),
            "stated_differs_from_all_evidence": sum(
                1 for row in assessed if row["strength_stated"] != row["strength_all"]),
            "partly_found": flag("partly_found", assessed),
            "m2": {
                "no_evidence_found": flag("no_evidence_found", assessed),
                "insufficient_from_all_evidence": flag("insufficient_all", assessed),
                "both": sum(1 for row in assessed
                            if row["no_evidence_found"] and row["insufficient_all"]),
                "unsupported": flag("m2_unsupported", assessed),
            },
            "ff4": {
                "strength_from_found_evidence": count("strength_ff4", assessed),
                "supported": flag("ff4_supported", assessed),
                "strength_changed_by_g1": sum(
                    1 for row in assessed if row["strength_ff4"] != row["strength_all"]),
                "m2_supported_but_not_ff4": sum(
                    1 for row in assessed
                    if not row["m2_unsupported"] and not row["ff4_supported"]),
                "ff4_supported_but_m2_unsupported": sum(
                    1 for row in assessed
                    if row["ff4_supported"] and row["m2_unsupported"]),
            },
            "security_relevant_only": {
                "total": len(security),
                "by_type": count("type", security),
                "strength_from_found_evidence": count("strength_ff4", security),
                "ff4_supported": flag("ff4_supported", security),
                "m2_unsupported": flag("m2_unsupported", security),
            },
        },
    }


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def git_state() -> dict[str, Any]:
    """Short commit and whether src/ and config/ are committed."""
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], check=True,
                                capture_output=True, text=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", "src", "config"],
                               check=True, capture_output=True, text=True).stdout.strip()
        return {"code_commit": commit, "src_and_config_committed": not dirty}
    except (OSError, subprocess.CalledProcessError):
        return {"code_commit": "unknown", "src_and_config_committed": False}


def print_summary(summary: dict[str, Any], prefix: str = "") -> None:
    for key, value in summary.items():
        if isinstance(value, dict):
            print(f"{prefix}{key}:")
            print_summary(value, prefix + "  ")
        else:
            print(f"{prefix}{key}: {value}")


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count requirements by type, security relevance and evidence "
                    "status (F3, G1). Prints numbers only.")
    parser.add_argument("--input", required=True, help="Extraction output, JSONL.")
    parser.add_argument("--dataset", required=True, help="Prepared dataset, JSONL.")
    parser.add_argument("--model-input", required=True,
                        help="Model input the run used, JSONL with source_block.")
    parser.add_argument("--mentions-map", default=None)
    parser.add_argument("--allowlist", default="")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    parser.add_argument("--output", default=None,
                        help="Optional JSON file for the counts. Never overwritten.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    output = Path(arguments.output) if arguments.output else None
    if output is not None and output.exists():
        print(f"Refusing to overwrite {output}.")
        return 2

    schema = json.loads(Path(arguments.schema).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    dataset = load_dataset(Path(arguments.dataset))
    blocks = load_blocks(Path(arguments.model_input))
    mapping = load_mapping(Path(arguments.mentions_map)) if arguments.mentions_map else None
    allowlist = {n.strip().lower() for n in arguments.allowlist.split(",") if n.strip()}
    if mapping is None:
        print("Note: no --mentions-map given, prose is compared unmasked.")

    records = [record for _, record in read_jsonl(Path(arguments.input))]
    summary = count_run(records, validator, dataset, blocks, mapping, allowlist)

    state = git_state()
    print(f"Code commit: {state['code_commit']}")
    if not state["src_and_config_committed"]:
        print("Warning: src/ or config/ has uncommitted changes.")
    print_summary(summary)

    if output is not None:
        result = {
            **state,
            "rules": "docs/entscheidungen.md: F3 (M2) and G1",
            "inputs": {
                "input": {"path": arguments.input, "sha256": sha256_of(Path(arguments.input))},
                "dataset": {"path": arguments.dataset,
                            "sha256": sha256_of(Path(arguments.dataset))},
                "model_input": {"path": arguments.model_input,
                                "sha256": sha256_of(Path(arguments.model_input))},
                "schema": {"path": arguments.schema,
                           "sha256": sha256_of(Path(arguments.schema))},
                "mentions_map_given": mapping is not None,
                "allowlist": sorted(allowlist),
            },
            "counts": summary,
        }
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
        print(f"\nWritten: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
