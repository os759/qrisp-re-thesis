"""Count the measures of decision F3 that were left for work package H.

Work package H. Research questions FF1 and FF3.

Every rule is fixed in docs/entscheidungen.md before counting:

* M1 part b (F3): share of the answers of the pilot run
  2026-09-24_pilot_v2 that pass the schema check of validate_output.py.
* M3 (F3): consistency over repetitions. The 20 pull requests of the
  pilot sample (docs/sample_pilot_a8.md) in two passes, the pilot run
  2026-09-24_pilot_v2 and the same pull requests in the full run
  2026-09-25_full_v2. A source place is the pair of location and
  locator of one evidence entry. Per pull request and pass: the set of
  source places of all evidence entries of all requirements. Jaccard
  agreement: places in both sets divided by places in at least one;
  1 if both sets are empty. Measure: mean over the 20 pull requests;
  also the smallest value and the number of requirements per pass. All
  evidence entries count, also rejected ones.
* Statement (i) of M2 (F3; addendum to F3 of 2026-10-01, point 4): of
  the unsupported requirements, how many the model itself marked
  insufficient and how many it gave a higher strength, and among the
  latter how many differ from the strength derived from all evidence
  (the rejections after E6).

Readings fixed with this program, before counting (chat of 09.10.2026):

* M3 counts the records of both passes whether or not they pass the
  schema check, because M3 measures the behaviour of the model (F3).
  An entry counts as a source place if it is an object with a text
  location; a locator that is not null is compared as text. As a second
  figure, the mean over the pull requests whose records pass the schema
  check in both passes is reported.
* (i) uses the base set and the rules of M2 exactly as
  count_requirements.py does; the program stops if its total of
  unsupported requirements differs from the committed counts file.

The program imports the checks from validate_output.py,
diagnose_excerpts.py and count_requirements.py and has no check rule
of its own. It prints and writes only counts, pull request numbers,
value names, checksums and the commit.

Run from the project root:

    python src/analyze/count_ff3_measures.py \\
      --full data/processed/extraction_2026-09-25_full_v2.jsonl \\
      --pilot data/processed/extraction_2026-09-24_pilot_v2.jsonl \\
      --pilot-sample docs/sample_pilot_a8.md \\
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \\
      --model-input data/processed/model_input_2026-09-19.jsonl \\
      --mentions-map data/interim/mention_map.json \\
      --allowlist "jaspify,jax,pytest,rus" \\
      --counts experiments/requirement_counts_2026-09-25_full_v2.json \\
      --output experiments/ff3_measures_2026-10-09.json
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

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
for _sub in ("extract", "prepare", "classify", "analyze"):
    if str(SRC / _sub) not in sys.path:
        sys.path.insert(0, str(SRC / _sub))

from jsonschema import Draft202012Validator  # noqa: E402

from check_classification import read_sample  # noqa: E402
from count_requirements import assess_requirement, evidence_status  # noqa: E402
from diagnose_excerpts import files_in_block, load_blocks  # noqa: E402
from pseudonymise import load_mapping  # noqa: E402
from validate_output import load_dataset  # noqa: E402

DEFAULT_SCHEMA = ROOT / "config" / "requirement_schema_v2.json"


class MeasureError(Exception):
    """A violated precondition. The message never holds content."""


# --- reading ------------------------------------------------------------


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as error:
                raise MeasureError(f"line {line_number} of {path} is not valid JSON") from error
            if not isinstance(value, dict):
                raise MeasureError(f"line {line_number} of {path} is not a JSON object")
            rows.append(value)
    return rows


def by_pull(records: list[dict[str, Any]], name: str) -> dict[int, dict[str, Any]]:
    result: dict[int, dict[str, Any]] = {}
    for record in records:
        number = record.get("pull_number")
        if number in result:
            raise MeasureError(f"{name}: pull request {number} has more than one record")
        result[number] = record
    return result


def is_valid(record: dict[str, Any], validator: Draft202012Validator) -> bool:
    return not any(True for _ in validator.iter_errors(record))


def _dicts(value: Any) -> list[dict[str, Any]]:
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


# --- M1 part b ----------------------------------------------------------


def m1_part_b(records: list[dict[str, Any]], validator: Draft202012Validator) -> dict[str, int]:
    valid = sum(1 for record in records if is_valid(record, validator))
    return {"records": len(records), "schema_valid": valid,
            "schema_invalid": len(records) - valid}


# --- M3 -----------------------------------------------------------------


def source_places(record: dict[str, Any] | None) -> set[tuple[str, str | None]]:
    """Pairs of location and locator of all evidence entries of all requirements."""
    places: set[tuple[str, str | None]] = set()
    if record is None:
        return places
    for requirement in _dicts(record.get("requirements")):
        for item in _dicts(requirement.get("evidence")):
            location = item.get("location")
            if not isinstance(location, str):
                continue
            locator = item.get("locator")
            places.add((location, None if locator is None else str(locator)))
    return places


def jaccard(first: set, second: set) -> float:
    union = first | second
    return 1.0 if not union else len(first & second) / len(union)


def requirement_count(record: dict[str, Any]) -> int:
    return len(_dicts(record.get("requirements")))


def m3(pulls: list[int], pilot: dict[int, dict[str, Any]], full: dict[int, dict[str, Any]],
       validator: Draft202012Validator) -> dict[str, Any]:
    missing = [p for p in pulls if p not in pilot or p not in full]
    if missing:
        raise MeasureError(f"pull requests of the pilot sample without a record in a pass: "
                           f"{', '.join(map(str, missing))}")
    per_pull = []
    for pull in pulls:
        valid_pilot = is_valid(pilot[pull], validator)
        valid_full = is_valid(full[pull], validator)
        per_pull.append({"pull": pull,
                         "jaccard": round(jaccard(source_places(pilot[pull]),
                                                  source_places(full[pull])), 4),
                         "places_pilot": len(source_places(pilot[pull])),
                         "places_full": len(source_places(full[pull])),
                         "requirements_pilot": requirement_count(pilot[pull]),
                         "requirements_full": requirement_count(full[pull]),
                         "schema_valid_pilot": valid_pilot, "schema_valid_full": valid_full})
    values = [jaccard(source_places(pilot[p]), source_places(full[p])) for p in pulls]
    both_valid = [value for value, row in zip(values, per_pull)
                  if row["schema_valid_pilot"] and row["schema_valid_full"]]
    return {
        "pull_requests": len(pulls),
        "mean": round(sum(values) / len(values), 4),
        "min": round(min(values), 4),
        "requirements_pilot": sum(row["requirements_pilot"] for row in per_pull),
        "requirements_full": sum(row["requirements_full"] for row in per_pull),
        "schema_invalid_records_pilot": sum(not row["schema_valid_pilot"] for row in per_pull),
        "schema_invalid_records_full": sum(not row["schema_valid_full"] for row in per_pull),
        "second_figure_both_schema_valid": {
            "pull_requests": len(both_valid),
            "mean": round(sum(both_valid) / len(both_valid), 4) if both_valid else None},
        "per_pull_request": per_pull,
    }


# --- statement (i) of M2 ------------------------------------------------


def statement_i(records: list[dict[str, Any]], validator: Draft202012Validator,
                dataset: dict[int, dict[str, Any]], blocks: dict[int, str],
                mapping: dict[str, str] | None, allowlist: set[str]) -> dict[str, Any]:
    """Assess the base set exactly as count_requirements.count_run does."""
    assessed = []
    for record in records:
        if not is_valid(record, validator):
            continue
        number = record.get("pull_number")
        pull = dataset.get(number)
        shown = files_in_block(blocks.get(number, ""))
        for requirement in _dicts(record.get("requirements")):
            flags = [evidence_status(item, pull, shown, mapping, allowlist)[0]
                     for item in _dicts(requirement.get("evidence"))]
            assessed.append(assess_requirement(requirement, flags))
    unsupported = [row for row in assessed if row["m2_unsupported"]]
    higher = [row for row in unsupported if row["strength_stated"] != "insufficient"]
    return {
        "base_set": len(assessed),
        "unsupported": len(unsupported),
        "stated_insufficient": len(unsupported) - len(higher),
        "stated_higher": len(higher),
        "stated_higher_by_value": dict(sorted(Counter(row["strength_stated"]
                                                      for row in higher).items())),
        "stated_higher_and_differs_from_all_evidence": sum(
            1 for row in higher if row["strength_stated"] != row["strength_all"]),
        "stated_differs_from_all_evidence_in_base_set": sum(
            1 for row in assessed if row["strength_stated"] != row["strength_all"]),
    }


def check_against_counts(result: dict[str, Any], counts_path: Path) -> None:
    counts = json.loads(counts_path.read_text(encoding="utf-8"))["counts"]["requirements"]
    pairs = (("base_set", counts["total"]), ("unsupported", counts["m2"]["unsupported"]),
             ("stated_differs_from_all_evidence_in_base_set",
              counts["stated_differs_from_all_evidence"]))
    for name, expected in pairs:
        if result[name] != expected:
            raise MeasureError(f"{name} is {result[name]}, the committed counts file "
                               f"has {expected}")


# --- command line -------------------------------------------------------


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], check=True,
                              capture_output=True, text=True, cwd=ROOT).stdout.strip() or "unknown"
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def print_counts(value: Any, prefix: str = "") -> None:
    for key, item in value.items():
        if isinstance(item, dict):
            print(f"{prefix}{key}:")
            print_counts(item, prefix + "  ")
        elif isinstance(item, list):
            print(f"{prefix}{key}:")
            for row in item:
                print(f"{prefix}  " + ", ".join(f"{k} {v}" for k, v in row.items()))
        else:
            print(f"{prefix}{key}: {item}")


INPUT_NAMES = ("full", "pilot", "pilot_sample", "dataset", "model_input", "mentions_map",
               "schema", "counts")


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="M1 part b, M3 and statement (i) of M2 "
                                     "(F3). Prints numbers only.")
    parser.add_argument("--full", required=True, help="Full run, JSONL.")
    parser.add_argument("--pilot", required=True, help="Pilot run with prompt v2, JSONL.")
    parser.add_argument("--pilot-sample", required=True, help="docs/sample_pilot_a8.md")
    parser.add_argument("--dataset", required=True, help="Prepared dataset, JSONL.")
    parser.add_argument("--model-input", required=True,
                        help="Model input the runs used, JSONL with source_block.")
    parser.add_argument("--mentions-map", default=None)
    parser.add_argument("--allowlist", default="")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    parser.add_argument("--counts", required=True,
                        help="Committed counts of count_requirements.py for the full run.")
    parser.add_argument("--output", required=True, help="Result JSON, never overwritten.")
    return parser.parse_args(argv)


def run(arguments: argparse.Namespace) -> int:
    output = Path(arguments.output)
    if output.exists():
        raise MeasureError(f"refusing to overwrite: {output}")
    schema = json.loads(Path(arguments.schema).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    full_records = read_jsonl(Path(arguments.full))
    pilot_records = read_jsonl(Path(arguments.pilot))
    full = by_pull(full_records, "full run")
    pilot = by_pull(pilot_records, "pilot run")
    sample = read_sample(Path(arguments.pilot_sample))
    if sorted(pilot) != sorted(sample):
        raise MeasureError("the pilot run does not hold exactly the pull requests of the "
                           "pilot sample")
    mapping = load_mapping(Path(arguments.mentions_map)) if arguments.mentions_map else None
    allowlist = {n.strip().lower() for n in arguments.allowlist.split(",") if n.strip()}
    if mapping is None:
        print("Note: no --mentions-map given, prose is compared unmasked.")
    m2_i = statement_i(full_records, validator, load_dataset(Path(arguments.dataset)),
                       load_blocks(Path(arguments.model_input)), mapping, allowlist)
    check_against_counts(m2_i, Path(arguments.counts))
    counts = {"m1_part_b_pilot": m1_part_b(pilot_records, validator),
              "m3": m3(sorted(sample), pilot, full, validator),
              "m2_statement_i": m2_i}
    result = {
        "rules": "docs/entscheidungen.md: F3 and the addendum to F3 of 2026-10-01; readings "
                 "in the docstring of src/analyze/count_ff3_measures.py",
        "code_commit": git_commit(),
        "inputs": {name: ({"path": getattr(arguments, name),
                           "sha256": sha256_of(Path(getattr(arguments, name)))}
                          if getattr(arguments, name) else None) for name in INPUT_NAMES},
        "allowlist": sorted(allowlist),
        "counts": counts,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Code commit: {result['code_commit']}")
    print_counts(counts)
    print(f"written: {output}")
    return 0


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    try:
        return run(arguments)
    except MeasureError as error:
        print(f"Stopped: {error}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
