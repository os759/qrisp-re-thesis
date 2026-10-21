"""Compare two or more extraction runs on the pull requests of one sample.

After the submission, decision E12 point j: for the sample of E2
(docs/sample_eval_e2.md) the runs of gpt-5.6-terra (full run
2026-09-25_full_v2) and claude-sonnet-5-5 (2026-10-21_claude_eval_v2)
are counted with the same rules. Counted are exactly the measures named
in E12 j: answered requests, complete answers, valid JSON objects,
records rejected by validate_output.py (by the first failing check),
requirements, tokens, cost upper bound and run time.

The program has no check rule of its own. The checks come from
breakdown_rejections.analyse, which calls the same functions as
validate_output.py in the same order. Figures per request come from the
manifest of each run, which run_extraction.py wrote.

It prints and writes only counts, pull request numbers, model names,
checksums and the commit; no requirement text, no excerpt and no source
text.

Run from the project root:

    python src/analyze/compare_runs.py \\
      --sample docs/sample_eval_e2.md \\
      --run 2026-09-25_full_v2 --run 2026-10-21_claude_eval_v2 \\
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \\
      --mentions-map data/interim/mention_map.json \\
      --allowlist "jaspify,jax,pytest,rus" \\
      --output experiments/model_comparison_eval_e2_2026-10-21.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

SRC = Path(__file__).resolve().parents[1]
for _sub in ("extract", "prepare"):
    if str(SRC / _sub) not in sys.path:
        sys.path.insert(0, str(SRC / _sub))

from jsonschema import Draft202012Validator  # noqa: E402

from breakdown_rejections import CHECKS, analyse  # noqa: E402
from pseudonymise import load_mapping  # noqa: E402
from validate_output import DEFAULT_SCHEMA, load_dataset, read_jsonl  # noqa: E402

PROCESSED = Path("data/processed")
# Same table rows as run_extraction.read_sample_numbers: "| 64 | S2 | ...".
SAMPLE_ROW = re.compile(r"^\| (\d+) \| S\d+ \|")
RUN_ID = re.compile(r"[0-9A-Za-z_.-]+")


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


def read_sample_numbers(path: Path) -> list[int]:
    numbers = [int(m.group(1)) for line in path.read_text(encoding="utf-8").splitlines()
               if (m := SAMPLE_ROW.match(line))]
    if not numbers:
        raise ValueError(f"{path}: no pull request rows found")
    if len(set(numbers)) != len(numbers):
        raise ValueError(f"{path}: a pull request is listed twice")
    return numbers


def run_paths(run_id: str, directory: Path = PROCESSED) -> dict[str, Path]:
    if not RUN_ID.fullmatch(run_id):
        raise ValueError(f"invalid run id: {run_id}")
    return {"extraction": directory / f"extraction_{run_id}.jsonl",
            "manifest": directory / f"extraction_{run_id}.manifest.json"}


def records_by_pull(path: Path, wanted: set[int]) -> dict[int, dict[str, Any]]:
    """Parsed model outputs of the wanted pull requests. A repeat stops the program."""
    found: dict[int, dict[str, Any]] = {}
    for line_number, record in read_jsonl(path):
        number = record.get("pull_number") if isinstance(record, dict) else None
        if number in wanted:
            if number in found:
                raise ValueError(f"{path}, line {line_number}: pull {number} twice")
            found[number] = record
    return found


def count_run(numbers: list[int], manifest: dict[str, Any],
              records: dict[int, dict[str, Any]], validator: Draft202012Validator,
              dataset: dict[int, dict[str, Any]], mapping: dict[str, str] | None,
              allowlist: set[str]) -> dict[str, Any]:
    """Counts of one run, restricted to the sample numbers."""
    rows = {row["pull_number"]: row for row in manifest.get("per_pull", [])}
    per_pull = []
    for number in numbers:
        row = rows.get(number)
        record = records.get(number)
        result = (analyse(record, validator, dataset, mapping, allowlist)
                  if record is not None else None)
        failing = result["excerpts"] if result is not None else None
        per_pull.append({
            "pull": number,
            "answered": row is not None,
            "status": row.get("status") if row else None,
            "valid_json_object": bool(row and row.get("valid_json_object")),
            "record_present": record is not None,
            "first_failing_check": result["first"] if result else None,
            "requirements": result["requirements"] if result else 0,
            "failing_excerpts": len(failing) if failing else 0,
            "input_tokens": row.get("input_tokens", 0) if row else 0,
            "output_tokens": row.get("output_tokens", 0) if row else 0,
            "cost_upper_bound_usd": row.get("cost_upper_bound_usd", 0.0) if row else 0.0,
            "duration_seconds": row.get("duration_seconds") if row else None,
            "model_returned": row.get("model_returned") if row else None,
        })
    # A record without a manifest row, or the reverse, means the two files
    # do not belong together; counting on would mix runs.
    for item in per_pull:
        if item["valid_json_object"] != item["record_present"]:
            raise ValueError(f"pull {item['pull']}: manifest and extraction file "
                             "disagree about a valid JSON object")
    accepted = [p for p in per_pull if p["record_present"] and p["first_failing_check"] is None]
    durations = [p["duration_seconds"] for p in per_pull if p["duration_seconds"] is not None]
    return {
        "models_returned": sorted({str(p["model_returned"]) for p in per_pull
                                   if p["answered"]}),
        "pull_requests": len(numbers),
        "answered": sum(p["answered"] for p in per_pull),
        "completed": sum(p["status"] == "completed" for p in per_pull),
        "valid_json_object": sum(p["valid_json_object"] for p in per_pull),
        "records_rejected": sum(p["record_present"] and p["first_failing_check"] is not None
                                for p in per_pull),
        "rejected_by_first_check": {check: sum(p["first_failing_check"] == check
                                               for p in per_pull) for check in CHECKS},
        "records_accepted": len(accepted),
        "pull_requests_with_requirements": sum(p["requirements"] > 0 for p in per_pull),
        "requirements": sum(p["requirements"] for p in per_pull),
        "requirements_in_accepted_records": sum(p["requirements"] for p in accepted),
        "failing_excerpts": sum(p["failing_excerpts"] for p in per_pull),
        "input_tokens": sum(p["input_tokens"] for p in per_pull),
        "output_tokens": sum(p["output_tokens"] for p in per_pull),
        "cost_upper_bound_usd": round(sum(p["cost_upper_bound_usd"] for p in per_pull), 4),
        "duration_seconds_sum": round(sum(durations), 2),
        "duration_seconds_mean": round(sum(durations) / len(durations), 2) if durations else None,
        "duration_seconds_max": max(durations) if durations else None,
        "per_pull": per_pull,
    }


def run_record(run_id: str, manifest: dict[str, Any], paths: dict[str, Path]) -> dict[str, Any]:
    """Where a run comes from: settings and checksums, no content."""
    request = manifest.get("request", {})
    return {
        "run_id": run_id,
        "model_requested": request.get("model_requested"),
        "provider": request.get("provider", "openai"),
        "parameters_sent": request.get("parameters_sent"),
        "prompt_version": manifest.get("prompt", {}).get("version"),
        "prompt_sha256": manifest.get("prompt", {}).get("sha256"),
        "model_input_sha256": manifest.get("model_input", {}).get("sha256"),
        "run_code_commit": manifest.get("code_commit"),
        "prices_usd_per_million": manifest.get("prices_usd_per_million"),
        "extraction_sha256": sha256_of(paths["extraction"]),
        "manifest_sha256": sha256_of(paths["manifest"]),
    }


SUMMARY_KEYS = ("answered", "completed", "valid_json_object", "records_rejected",
                "records_accepted", "pull_requests_with_requirements", "requirements",
                "requirements_in_accepted_records", "failing_excerpts", "input_tokens",
                "output_tokens", "cost_upper_bound_usd", "duration_seconds_sum",
                "duration_seconds_mean", "duration_seconds_max")


def print_table(runs: list[dict[str, Any]]) -> None:
    names = [run["source"]["run_id"] for run in runs]
    width = max(len(name) for name in names) + 2
    print("measure".ljust(36) + "".join(name.rjust(width) for name in names))
    for key in SUMMARY_KEYS:
        print(key.ljust(36) + "".join(str(run["counts"][key]).rjust(width) for run in runs))
    for check in CHECKS:
        print(f"rejected first by {check}".ljust(36)
              + "".join(str(run["counts"]["rejected_by_first_check"][check]).rjust(width)
                        for run in runs))
    print("models returned: " + " | ".join(", ".join(run["counts"]["models_returned"])
                                           for run in runs))


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare runs on one sample (E12 j).")
    parser.add_argument("--sample", required=True)
    parser.add_argument("--run", action="append", required=True,
                        help="run id, e.g. 2026-09-25_full_v2; give it once per run")
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--mentions-map", default=None)
    parser.add_argument("--allowlist", default="")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    parser.add_argument("--processed", default=str(PROCESSED))
    parser.add_argument("--output", default=None)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    if len(arguments.run) < 2 or len(set(arguments.run)) != len(arguments.run):
        print("Give at least two different runs.")
        return 2
    output = Path(arguments.output) if arguments.output else None
    if output is not None and output.exists():
        print(f"Refusing to overwrite {output}.")
        return 2

    sample = Path(arguments.sample)
    numbers = read_sample_numbers(sample)
    schema = json.loads(Path(arguments.schema).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    dataset = load_dataset(Path(arguments.dataset))
    mapping = load_mapping(Path(arguments.mentions_map)) if arguments.mentions_map else None
    allowlist = {n.strip().lower() for n in arguments.allowlist.split(",") if n.strip()}
    if mapping is None:
        print("Note: no --mentions-map given, prose is compared unmasked.")

    runs = []
    for run_id in arguments.run:
        paths = run_paths(run_id, Path(arguments.processed))
        manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
        records = records_by_pull(paths["extraction"], set(numbers))
        counts = count_run(numbers, manifest, records, validator, dataset, mapping, allowlist)
        runs.append({"source": run_record(run_id, manifest, paths), "counts": counts})

    state = git_state()
    print(f"Code commit: {state['code_commit']}")
    if not state["src_and_config_committed"]:
        print("Warning: src/ or config/ has uncommitted changes.")
    print(f"Sample: {sample} ({len(numbers)} pull requests)\n")
    print_table(runs)

    if output is not None:
        result = {
            **state,
            "rules": "docs/entscheidungen.md: E12 point j; checks of validate_output.py "
                     "through breakdown_rejections.analyse",
            "notes": [
                "cost_upper_bound_usd is computed by run_extraction.py from the "
                "tokens and the prices in each manifest; the invoice is binding.",
                "output_tokens include the thinking of both models. OpenAI reports "
                "it separately, Anthropic does not.",
                "Effort settings are not calibrated between providers: medium for "
                "gpt-5.6-terra (E11 a), high for claude-sonnet-5-5 (E12 c).",
            ],
            "inputs": {
                "sample": {"path": str(sample), "sha256": sha256_of(sample),
                           "pull_numbers": numbers},
                "dataset": {"path": arguments.dataset,
                            "sha256": sha256_of(Path(arguments.dataset))},
                "schema": {"path": arguments.schema,
                           "sha256": sha256_of(Path(arguments.schema))},
                "mentions_map_given": mapping is not None,
                "allowlist": sorted(allowlist),
            },
            "runs": runs,
        }
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
        print(f"\nWritten: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
