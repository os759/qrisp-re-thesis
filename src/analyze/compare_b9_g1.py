"""Compare the requirements that satisfy B9 with those supported after G1.

Work package H, part 3. Research question FF1; the set after G1 is the
one the gap analysis uses for FF4.

Both counts are already committed and equal: B9 (criterion of
eval/instrument/kriterien_v1.md, section 6.2) in
experiments/evaluation_e2_2026-10-08.json, and "supported" after G1
(docs/entscheidungen.md, G1 point 4) in
experiments/requirement_counts_2026-09-25_full_v2.json. Equal counts do
not show equal sets. This program checks per requirement whether both
rules pick the same requirements.

* B9 per requirement: machine_values of evaluate_requirements.py, that
  is all evidence found and the stated strength equal to the strength
  derived from all evidence.
* G1 per requirement: assess_requirement of count_requirements.py,
  field ff4_supported, that is the strength derived from the found
  evidence only is direct or indirect.
* Base set: the requirements of the schema-valid records of the full
  run, read with load_requirements as in evaluate_requirements.py.

The program has no check rule of its own. It stops before writing if
its totals or the checksums of its inputs differ from the two committed
result files, because then it would not compare the same sets.

It prints and writes only counts, value names, requirement identifiers,
checksums and the commit; no requirement text, no excerpt. The result
also holds the checksum of this program, because the program may be
committed in the same commit as its result.

Run from the project root:

    python src/analyze/compare_b9_g1.py \\
      --input data/processed/extraction_2026-09-25_full_v2.jsonl \\
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \\
      --model-input data/processed/model_input_2026-09-19.jsonl \\
      --mentions-map data/interim/mention_map.json \\
      --allowlist "jaspify,jax,pytest,rus" \\
      --evaluation experiments/evaluation_e2_2026-10-08.json \\
      --counts experiments/requirement_counts_2026-09-25_full_v2.json \\
      --output experiments/b9_g1_comparison_2026-10-10.json
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

from check_classification import load_requirements  # noqa: E402
from count_requirements import assess_requirement  # noqa: E402
from diagnose_excerpts import load_blocks  # noqa: E402
from evaluate_requirements import Context, machine_values  # noqa: E402
from pseudonymise import load_mapping  # noqa: E402
from validate_output import load_dataset  # noqa: E402

DEFAULT_SCHEMA = ROOT / "config" / "requirement_schema_v2.json"
G1_REASONS = ("not_all_found", "strength_differs", "both")


class CompareError(Exception):
    """A violated precondition. The message never holds content."""


# --- comparison ---------------------------------------------------------


def judge(row: dict[str, Any], context: Context) -> dict[str, Any]:
    """B9 and G1 for one requirement, with the parts that decide them."""
    values = machine_values(row, context)
    flags = context.found_flags(row["pull"], row["req"])
    assessed = assess_requirement(row["req"], flags)
    return {"key": row["key"], "B9": bool(values["B9"]),
            "G1": bool(assessed["ff4_supported"]),
            "all_found": bool(values["all_evidence_found"]),
            "strength_matches": bool(values["strength_matches"]),
            "stated": assessed["strength_stated"],
            "strength_all": assessed["strength_all"],
            "strength_found": assessed["strength_ff4"]}


def g1_reason(judged: dict[str, Any]) -> str:
    """Why a requirement supported after G1 fails B9."""
    if not judged["all_found"] and not judged["strength_matches"]:
        return "both"
    return "not_all_found" if not judged["all_found"] else "strength_differs"


def compare(rows: list[dict[str, Any]], context: Context) -> dict[str, Any]:
    judged = [judge(row, context) for row in rows]
    b9_only = [j for j in judged if j["B9"] and not j["G1"]]
    g1_only = [j for j in judged if j["G1"] and not j["B9"]]
    reasons = Counter(g1_reason(j) for j in g1_only)
    return {
        "base_set": len(judged),
        "b9_satisfied": sum(j["B9"] for j in judged),
        "g1_supported": sum(j["G1"] for j in judged),
        "cross": {"b9_and_g1": sum(j["B9"] and j["G1"] for j in judged),
                  "b9_only": len(b9_only),
                  "g1_only": len(g1_only),
                  "neither": sum(not j["B9"] and not j["G1"] for j in judged)},
        "identical_sets": not b9_only and not g1_only,
        "b9_only_by_stated_strength": dict(sorted(Counter(j["stated"]
                                                          for j in b9_only).items())),
        "g1_only_by_reason": {reason: reasons[reason] for reason in G1_REASONS},
        "g1_only_by_strength_from_found_evidence": dict(sorted(
            Counter(j["strength_found"] for j in g1_only).items())),
        "ids": {"b9_only": sorted(j["key"] for j in b9_only),
                "g1_only": sorted(j["key"] for j in g1_only)},
    }


def check_against_committed(result: dict[str, Any], evaluation: dict[str, Any],
                            counts: dict[str, Any]) -> None:
    """Stop if the totals differ from the two committed result files."""
    base = evaluation["counts"]["machine"]["base_set"]
    requirements = counts["counts"]["requirements"]
    pairs = (("base_set", base["n"], "evaluation file"),
             ("base_set", requirements["total"], "counts file"),
             ("b9_satisfied", base["B9"]["satisfied"], "evaluation file"),
             ("g1_supported", requirements["ff4"]["supported"], "counts file"))
    for name, expected, where in pairs:
        if result[name] != expected:
            raise CompareError(f"{name} is {result[name]}, the committed {where} has "
                               f"{expected}")


def check_inputs(hashes: dict[str, str | None], evaluation: dict[str, Any],
                 counts: dict[str, Any]) -> None:
    """Stop if an input is not the file the committed results were made from."""
    for name in ("input", "dataset", "model_input"):
        for where, recorded in (("evaluation file", evaluation["inputs"][name]["sha256"]),
                                ("counts file", counts["inputs"][name]["sha256"])):
            if hashes[name] != recorded:
                raise CompareError(f"--{name.replace('_', '-')} differs from the file "
                                   f"in the committed {where} (checksum)")
    recorded_map = (evaluation["inputs"].get("mentions_map") or {}).get("sha256")
    if hashes["mentions_map"] != recorded_map:
        raise CompareError("--mentions-map differs from the file in the committed "
                           "evaluation file (checksum)")


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


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise CompareError(f"line {line_number} of {path} is not valid JSON") from error
    return rows


INPUT_NAMES = ("input", "dataset", "model_input", "mentions_map", "schema", "evaluation",
               "counts")


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare B9 (criteria list v1) with "
                                     "'supported' after G1. Prints numbers and ids only.")
    parser.add_argument("--input", required=True, help="Full run, JSONL.")
    parser.add_argument("--dataset", required=True, help="Prepared dataset, JSONL.")
    parser.add_argument("--model-input", required=True,
                        help="Model input the run used, JSONL with source_block.")
    parser.add_argument("--mentions-map", default=None)
    parser.add_argument("--allowlist", default="")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    parser.add_argument("--evaluation", required=True,
                        help="Committed result of evaluate_requirements.py.")
    parser.add_argument("--counts", required=True,
                        help="Committed result of count_requirements.py.")
    parser.add_argument("--output", required=True, help="Result JSON, never overwritten.")
    return parser.parse_args(argv)


def print_counts(value: dict[str, Any], prefix: str = "") -> None:
    for key, item in value.items():
        if isinstance(item, dict):
            print(f"{prefix}{key}:")
            print_counts(item, prefix + "  ")
        elif isinstance(item, list):
            print(f"{prefix}{key}: {len(item)} (identifiers in the JSON file)")
        else:
            print(f"{prefix}{key}: {item}")


def run(arguments: argparse.Namespace) -> int:
    output = Path(arguments.output)
    if output.exists():
        raise CompareError(f"refusing to overwrite: {output}")
    hashes = {name: (sha256_of(Path(getattr(arguments, name)))
                     if getattr(arguments, name) else None) for name in INPUT_NAMES}
    evaluation = json.loads(Path(arguments.evaluation).read_text(encoding="utf-8"))
    counts = json.loads(Path(arguments.counts).read_text(encoding="utf-8"))
    check_inputs(hashes, evaluation, counts)

    schema = json.loads(Path(arguments.schema).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    rows = load_requirements(read_jsonl(Path(arguments.input)), validator)
    allowlist = {n.strip().lower() for n in arguments.allowlist.split(",") if n.strip()}
    mapping = load_mapping(Path(arguments.mentions_map)) if arguments.mentions_map else None
    if mapping is None:
        print("Note: no --mentions-map given, prose is compared unmasked.")
    context = Context(load_dataset(Path(arguments.dataset)),
                      load_blocks(Path(arguments.model_input)), mapping, allowlist)

    result = compare(rows, context)
    check_against_committed(result, evaluation, counts)
    document = {
        "rules": "eval/instrument/kriterien_v1.md, section 6.2 (B9); docs/entscheidungen.md, "
                 "G1 point 4; functions of evaluate_requirements.py and count_requirements.py",
        "code_commit": git_commit(),
        # The program may be committed together with this file, after the run;
        # its checksum pins the code that produced the counts.
        "program_sha256": sha256_of(Path(__file__)),
        "inputs": {name: ({"path": getattr(arguments, name), "sha256": hashes[name]}
                          if hashes[name] else None) for name in INPUT_NAMES},
        "allowlist": sorted(allowlist),
        "counts": result,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")
    print(f"Code commit: {document['code_commit']}")
    print_counts(result)
    print(f"written: {output}")
    return 0


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    try:
        return run(arguments)
    except CompareError as error:
        print(f"Stopped: {error}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
