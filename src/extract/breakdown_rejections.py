"""Break the rejected records of a run down by the check that rejects them.

validate_output.py applies three checks in a fixed order and stops at
the first that reports: schema, consistency with the rules of decision
E6, excerpts. It prints how many records it rejects, but not which
check rejected them. This script counts exactly that, with the same
functions, and says for every record rejected by the schema or by E6
whether its excerpts would also have failed.

Nothing of a requirement, an excerpt or a source text is printed:
schema problems appear as the field path and the name of the violated
schema keyword, E6 problems as the pair "stated -> derived".

With --pull N the script shows one record: which checks fail, and the
identifier and position of every excerpt that is not found.

Work package E, step A8, sub-step 11. Research questions FF1, FF2, FF3.

Run from the project root:

    python src/extract/breakdown_rejections.py \\
      --input data/processed/extraction_2026-09-25_full_v2.jsonl \\
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \\
      --mentions-map data/interim/mention_map.json \\
      --allowlist "jaspify,jax,pytest,rus"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from pseudonymise import load_mapping
from validate_output import (DEFAULT_SCHEMA, check_record,
                             derive_evidence_strength, excerpt_found,
                             haystacks_for, load_dataset, read_jsonl)

CHECKS = ("schema", "e6", "excerpt")
INDEX = re.compile(r"/\d+(?=/|$)")


def schema_problems(record: Any, validator: Draft202012Validator) -> list[str]:
    """Path and keyword of every schema violation, list positions as *."""
    problems = []
    for error in validator.iter_errors(record):
        path = "/" + "/".join(str(part) for part in error.absolute_path)
        problems.append(f"{INDEX.sub('/*', path)} {error.validator}")
    return sorted(problems)


def failing_excerpts(record: dict[str, Any], dataset: dict[int, dict[str, Any]],
                     mapping: dict[str, str] | None,
                     allowlist: set[str]) -> list[tuple[str, int, Any]] | None:
    """(id, position, location) of every excerpt not found; None if not checkable."""
    pull = dataset.get(record.get("pull_number"))
    if pull is None:
        return None
    failing = []
    try:
        for requirement in record.get("requirements", []):
            for position, item in enumerate(requirement.get("evidence", []), start=1):
                candidates = haystacks_for(item, pull, mapping, allowlist)
                if not candidates or not excerpt_found(item, pull, candidates):
                    failing.append((requirement.get("id", "<no id>"), position,
                                    item.get("location")))
    except (AttributeError, TypeError):
        return None  # a record whose structure breaks the schema
    return failing


def e6_pairs(record: dict[str, Any]) -> list[str]:
    pairs = []
    for requirement in record.get("requirements", []):
        derived = derive_evidence_strength(requirement)
        stated = requirement.get("evidence_strength")
        if stated != derived:
            pairs.append(f"{stated} -> {derived}")
    return pairs


def analyse(record: dict[str, Any], validator: Draft202012Validator,
            dataset: dict[int, dict[str, Any]], mapping: dict[str, str] | None,
            allowlist: set[str]) -> dict[str, Any]:
    """First failing check as in validate_output.py, plus the later checks."""
    schema = schema_problems(record, validator)
    try:
        e6: list[str] | None = e6_pairs(record)
    except (AttributeError, TypeError):
        e6 = None  # only possible for a record that breaks the schema
    excerpts = failing_excerpts(record, dataset, mapping, allowlist)
    if schema:
        first = "schema"
    elif e6:
        first = "e6"
    elif excerpts is None or excerpts:
        first = "excerpt"
    else:
        first = None
    return {"pull": record.get("pull_number"), "first": first, "schema": schema,
            "e6": e6, "excerpts": excerpts,
            "requirements": len(record.get("requirements") or [])
            if isinstance(record.get("requirements"), list) else 0}


def summarise(results: list[dict[str, Any]]) -> dict[str, Any]:
    rejected = [r for r in results if r["first"]]
    first = Counter(r["first"] for r in rejected)
    also_excerpt = Counter()
    for r in rejected:
        if r["first"] in ("schema", "e6"):
            if r["excerpts"] is None:
                also_excerpt[f"{r['first']}: excerpts not checkable"] += 1
            elif r["excerpts"]:
                also_excerpt[f"{r['first']}: excerpts also fail"] += 1
            else:
                also_excerpt[f"{r['first']}: excerpts pass"] += 1
    schema_kinds = Counter(p for r in rejected for p in set(r["schema"]))
    e6_kinds = Counter(p for r in rejected if r["first"] == "e6" for p in r["e6"] or [])
    return {
        "records": len(results),
        "rejected": len(rejected),
        "first": {check: first[check] for check in CHECKS},
        "requirements_in_rejected": {check: sum(r["requirements"] for r in rejected
                                                if r["first"] == check) for check in CHECKS},
        "also_excerpt": dict(sorted(also_excerpt.items())),
        "schema_kinds": dict(sorted(schema_kinds.items())),
        "e6_kinds": dict(sorted(e6_kinds.items())),
        "e6_requirements": sum(e6_kinds.values()),
        "records_with_failing_excerpt": sum(1 for r in results if r["excerpts"]),
        "failing_excerpts": sum(len(r["excerpts"]) for r in results if r["excerpts"]),
    }


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count rejected records by the check that rejects them.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    parser.add_argument("--mentions-map", default=None)
    parser.add_argument("--allowlist", default="")
    parser.add_argument("--pull", type=int, default=None,
                        help="Show the checks for this one pull request.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    schema = json.loads(Path(arguments.schema).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    dataset = load_dataset(Path(arguments.dataset))
    mapping = load_mapping(Path(arguments.mentions_map)) if arguments.mentions_map else None
    allowlist = {n.strip().lower() for n in arguments.allowlist.split(",") if n.strip()}
    if mapping is None:
        print("Note: no --mentions-map given, the dataset is compared unmasked.")
    records = [record for _, record in read_jsonl(Path(arguments.input))]
    results = [analyse(r, validator, dataset, mapping, allowlist) for r in records]

    # Guard: the count must equal what validate_output.py rejects.
    rejected_by_checker = sum(1 for r in records
                              if check_record(r, validator, dataset, mapping, allowlist))
    summary = summarise(results)
    if summary["rejected"] != rejected_by_checker:
        print(f"ERROR: {summary['rejected']} rejected here, "
              f"{rejected_by_checker} by validate_output.py. Stop.")
        return 2

    if arguments.pull is not None:
        chosen = [r for r in results if r["pull"] == arguments.pull]
        if not chosen:
            print(f"pull {arguments.pull} not in the input")
            return 2
        for r in chosen:
            print(f"pull {r['pull']}: rejected by {r['first'] or 'nothing (accepted)'}")
            print(f"  schema problems: {len(r['schema'])}"
                  + "".join(f"\n    {p}" for p in r["schema"]))
            print("  E6 problems: " + ("not checkable" if r["e6"] is None
                                         else str(len(r["e6"]))))
            excerpts = r["excerpts"]
            print("  excerpts not found: " + ("not checkable" if excerpts is None
                                                else str(len(excerpts))))
            for ident, position, location in excerpts or []:
                print(f"    {ident}  evidence {position}  location {location}")
        return 0

    print(f"Records read: {summary['records']}")
    print(f"Records rejected: {summary['rejected']} "
          f"(validate_output.py: {rejected_by_checker})")
    print("Rejected by first failing check: "
          + ", ".join(f"{c} {n}" for c, n in summary["first"].items()))
    print("Requirements in rejected records, by check: "
          + ", ".join(f"{c} {n}" for c, n in summary["requirements_in_rejected"].items()))
    print("Records rejected by schema or E6, excerpt check: "
          + (", ".join(f"{k} {v}" for k, v in summary["also_excerpt"].items()) or "none"))
    print("Schema problems (path keyword: records): "
          + (", ".join(f"{k}: {v}" for k, v in summary["schema_kinds"].items()) or "none"))
    print(f"E6 problems in records rejected by E6: {summary['e6_requirements']} requirements "
          + (", ".join(f"{k}: {v}" for k, v in summary["e6_kinds"].items()) or ""))
    print(f"Records with at least one excerpt not found: "
          f"{summary['records_with_failing_excerpt']}")
    print(f"Excerpts not found, all records: {summary['failing_excerpts']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
