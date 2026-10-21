"""Tests for src/analyze/compare_runs.py with invented data (decision E12 j).

The checks are the ones of breakdown_rejections.analyse; these tests
make sure that the program restricts every run to the sample, counts
rejections and requirements exactly like validate_output.py, takes
tokens, cost and time from the manifest, refuses mismatched files and
never prints or writes model text.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src" / "analyze"))
sys.path.insert(0, str(ROOT / "src" / "extract"))

import compare_runs as c  # noqa: E402
from validate_output import check_record  # noqa: E402

from test_breakdown_rejections import (ACCEPTED, E6_BAD, EXCERPT_BAD, PULL,  # noqa: E402
                                       SCHEMA, SECRET, rec, requirement)

VALIDATOR = Draft202012Validator(SCHEMA)


def pull(number):
    return {**PULL, "number": number}


def record_for(number, template):
    return {**template, "pull_number": number}


def row(number, status="completed", valid=True, tokens=(100, 50), cost=0.01,
        duration=2.0, model="model-invented"):
    return {"pull_number": number, "status": status, "valid_json_object": valid,
            "input_tokens": tokens[0], "output_tokens": tokens[1],
            "cost_upper_bound_usd": cost, "duration_seconds": duration,
            "model_returned": model}


def write_run(directory, run_id, records, rows, provider=None):
    lines = [json.dumps(r) for r in records]
    (directory / f"extraction_{run_id}.jsonl").write_text(
        "\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    request = {"model_requested": "model-invented",
               "parameters_sent": {"model": "model-invented"}}
    if provider:
        request["provider"] = provider
    manifest = {"request": request, "prompt": {"version": "v2", "sha256": {"x": "y"}},
                "model_input": {"sha256": "m"}, "code_commit": "abc",
                "prices_usd_per_million": {}, "per_pull": rows}
    (directory / f"extraction_{run_id}.manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8")


@pytest.fixture
def project(tmp_path, monkeypatch):
    processed = tmp_path / "data" / "processed"
    processed.mkdir(parents=True)
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "sample.md").write_text(
        "| PR | Stratum |\n|---|---|\n| 3 | S1 | x |\n| 4 | S2 | x |\n| 5 | S3 | x |\n",
        encoding="utf-8")
    dataset = [pull(n) for n in (3, 4, 5, 6)]
    (tmp_path / "dataset.jsonl").write_text(
        "\n".join(json.dumps(p) for p in dataset) + "\n", encoding="utf-8")
    (tmp_path / "schema.json").write_text(json.dumps(SCHEMA), encoding="utf-8")
    # Run A: 3 accepted (1 requirement), 4 rejected by E6, 5 rejected by
    # excerpt (2 requirements), 6 outside the sample.
    write_run(processed, "run_a",
              [record_for(3, ACCEPTED), record_for(4, E6_BAD), record_for(5, EXCERPT_BAD),
               record_for(6, ACCEPTED)],
              [row(3), row(4, tokens=(200, 60), cost=0.02, duration=4.0), row(5), row(6)])
    # Run B: 3 accepted with two requirements, 4 no valid JSON, 5 accepted
    # and empty.
    write_run(processed, "run_b",
              [record_for(3, rec(requirement(), requirement("QR-0003-02"))),
               record_for(5, rec())],
              [row(3), row(4, status="incomplete", valid=False), row(5)],
              provider="anthropic")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(c, "git_state",
                        lambda: {"code_commit": "test", "src_and_config_committed": True})
    return tmp_path


ARGS = ["--sample", "docs/sample.md", "--run", "run_a", "--run", "run_b",
        "--dataset", "dataset.jsonl", "--schema", "schema.json"]


def load_output(project):
    return json.loads((project / "out.json").read_text(encoding="utf-8"))


def test_counts_of_both_runs(project):
    assert c.main(ARGS + ["--output", "out.json"]) == 0
    a, b = (run["counts"] for run in load_output(project)["runs"])
    assert a["pull_requests"] == 3 and a["answered"] == 3
    assert a["records_rejected"] == 2 and a["records_accepted"] == 1
    assert a["rejected_by_first_check"] == {"schema": 0, "e6": 1, "excerpt": 1}
    assert a["requirements"] == 4
    assert a["requirements_in_accepted_records"] == 1
    assert a["failing_excerpts"] == 1
    assert a["input_tokens"] == 400 and a["output_tokens"] == 160
    assert a["cost_upper_bound_usd"] == pytest.approx(0.04)
    assert a["duration_seconds_sum"] == 8.0 and a["duration_seconds_max"] == 4.0
    assert b["answered"] == 3 and b["completed"] == 2 and b["valid_json_object"] == 2
    assert b["records_rejected"] == 0 and b["records_accepted"] == 2
    assert b["requirements"] == 2 and b["requirements_in_accepted_records"] == 2
    assert b["pull_requests_with_requirements"] == 1


def test_rejections_match_validate_output(project):
    c.main(ARGS + ["--output", "out.json"])
    a = load_output(project)["runs"][0]["counts"]
    dataset = {p["number"]: p for p in (pull(n) for n in (3, 4, 5))}
    expected = sum(1 for record in (record_for(3, ACCEPTED), record_for(4, E6_BAD),
                                    record_for(5, EXCERPT_BAD))
                   if check_record(record, VALIDATOR, dataset, None, set()))
    assert a["records_rejected"] == expected


def test_pull_outside_the_sample_is_ignored(project):
    c.main(ARGS + ["--output", "out.json"])
    a = load_output(project)["runs"][0]["counts"]
    assert [p["pull"] for p in a["per_pull"]] == [3, 4, 5]


def test_source_records_provider_and_checksums(project):
    c.main(ARGS + ["--output", "out.json"])
    first, second = (run["source"] for run in load_output(project)["runs"])
    assert first["provider"] == "openai" and second["provider"] == "anthropic"
    assert len(first["extraction_sha256"]) == 64


def test_no_model_text_is_printed_or_written(project, capsys):
    c.main(ARGS + ["--output", "out.json"])
    assert SECRET not in capsys.readouterr().out
    assert SECRET not in (project / "out.json").read_text(encoding="utf-8")
    assert "cache gates" not in (project / "out.json").read_text(encoding="utf-8")


def test_existing_output_is_not_overwritten(project):
    (project / "out.json").write_text("{}", encoding="utf-8")
    assert c.main(ARGS + ["--output", "out.json"]) == 2
    assert (project / "out.json").read_text(encoding="utf-8") == "{}"


def test_needs_two_different_runs(project):
    assert c.main(["--sample", "docs/sample.md", "--run", "run_a", "--run", "run_a",
                   "--dataset", "dataset.jsonl", "--schema", "schema.json"]) == 2


def test_manifest_and_extraction_must_agree(project):
    processed = project / "data" / "processed"
    write_run(processed, "run_b", [record_for(3, ACCEPTED)],
              [row(3, valid=False), row(4), row(5)])
    with pytest.raises(ValueError, match="disagree"):
        c.main(ARGS)


def test_pull_twice_in_extraction_stops(project):
    processed = project / "data" / "processed"
    write_run(processed, "run_b", [record_for(3, ACCEPTED), record_for(3, ACCEPTED)],
              [row(3), row(4), row(5)])
    with pytest.raises(ValueError, match="twice"):
        c.main(ARGS)


def test_unanswered_pull_counts_as_not_answered(project):
    processed = project / "data" / "processed"
    write_run(processed, "run_b", [record_for(3, ACCEPTED)], [row(3)])
    c.main(ARGS + ["--output", "out.json"])
    b = load_output(project)["runs"][1]["counts"]
    assert b["answered"] == 1 and b["valid_json_object"] == 1


@pytest.mark.parametrize("run_id", ["../x", "a b", ""])
def test_run_id_is_checked(run_id):
    with pytest.raises(ValueError):
        c.run_paths(run_id)


def test_sample_numbers_in_order_and_unique(tmp_path):
    path = tmp_path / "s.md"
    path.write_text("| 9 | S1 |\n| 2 | S6 |\n", encoding="utf-8")
    assert c.read_sample_numbers(path) == [9, 2]
    path.write_text("| 9 | S1 |\n| 9 | S1 |\n", encoding="utf-8")
    with pytest.raises(ValueError):
        c.read_sample_numbers(path)


def test_complete_answer_without_json_object_is_counted_apart(project):
    """A complete answer can still miss the format, as qwen did in work package F."""
    processed = project / "data" / "processed"
    write_run(processed, "run_b", [record_for(3, ACCEPTED), record_for(5, rec())],
              [row(3), row(4, status="completed", valid=False), row(5)])
    c.main(ARGS + ["--output", "out.json"])
    b = load_output(project)["runs"][1]["counts"]
    assert b["completed"] == 3 and b["valid_json_object"] == 2
