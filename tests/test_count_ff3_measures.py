"""Tests for src/analyze/count_ff3_measures.py (F3: M1 part b, M3, statement (i)).

All data are invented. The file sets its import path itself.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
for _sub in ("extract", "prepare", "classify", "analyze"):
    if str(ROOT / "src" / _sub) not in sys.path:
        sys.path.insert(0, str(ROOT / "src" / _sub))

import count_ff3_measures as ff3  # noqa: E402

SCHEMA = ROOT / "config" / "requirement_schema_v2.json"
VALIDATOR = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))


def evidence(location, excerpt, supports, locator=None):
    return {"location": location, "locator": locator, "excerpt": excerpt,
            "supports": list(supports)}


def requirement(rid, items, strength, pattern="ubiquitous", source_form="descriptive"):
    return {"id": rid, "text": "The Widget shall do something useful.", "ears_pattern": pattern,
            "system_name": "Widget", "type": "functional_performance",
            "security_relevant": False, "rationale": "SECRET-RATIONALE for testing.",
            "evidence_strength": strength, "modality_set_by_convention": True,
            "evidence": items, "source_form": source_form}


def record(number, requirements, valid=True):
    rec = {"schema_version": 2, "pull_number": number,
           "processing_status": "requirements_found" if requirements else "no_requirements_found",
           "status_reason": None if requirements else "Nothing to extract here.",
           "requirements": requirements}
    if not valid:
        rec["schema_version"] = 1
    return rec


BOTH = ["system_name", "system_response"]
DATASET = {
    1: {"number": 1, "title": "Widget title here", "body": "The Widget must do something.",
        "issue_comments": [{"id": 7, "body": "Comment about the Widget behaviour."}],
        "review_comments": [], "files": []},
    2: {"number": 2, "title": "Second pull title", "body": "Body of the second pull.",
        "issue_comments": [], "review_comments": [], "files": []},
}


# --- M3 -----------------------------------------------------------------

def test_source_places_pairs_and_robustness():
    rec = {"requirements": [
        {"evidence": [evidence("body", "x" * 10, BOTH), evidence("issue_comment", "y" * 10,
                                                                 BOTH, 7)]},
        {"evidence": [evidence("body", "z" * 10, BOTH), "not an object", {"location": 5}]},
        "not a requirement"]}
    assert ff3.source_places(rec) == {("body", None), ("issue_comment", "7")}
    assert ff3.source_places(None) == set()
    assert ff3.source_places({"requirements": "broken"}) == set()


def test_locator_int_and_text_are_the_same_place():
    first = {"requirements": [{"evidence": [evidence("issue_comment", "a" * 10, BOTH, 7)]}]}
    second = {"requirements": [{"evidence": [evidence("issue_comment", "a" * 10, BOTH, "7")]}]}
    assert ff3.source_places(first) == ff3.source_places(second)


def test_jaccard():
    assert ff3.jaccard(set(), set()) == 1.0
    assert ff3.jaccard({1, 2}, {2, 3}) == pytest.approx(1 / 3)
    assert ff3.jaccard({1}, set()) == 0.0
    assert ff3.jaccard({1, 2}, {1, 2}) == 1.0


def test_m3_counts_invalid_records_and_reports_second_figure():
    pilot = {
        1: record(1, [requirement("QR-0001-01", [evidence("body", "b" * 10, BOTH)], "indirect")]),
        2: record(2, [requirement("QR-0002-01", [evidence("title", "t" * 10, BOTH)], "indirect")],
                  valid=False),
        3: record(3, []),
    }
    full = {
        1: record(1, [requirement("QR-0001-01", [evidence("body", "b" * 10, BOTH),
                                                 evidence("title", "t" * 10, BOTH)], "indirect")]),
        2: record(2, [requirement("QR-0002-01", [evidence("title", "t" * 10, BOTH)], "indirect")]),
        3: record(3, []),
    }
    result = ff3.m3([1, 2, 3], pilot, full, VALIDATOR)
    assert result["mean"] == round((0.5 + 1.0 + 1.0) / 3, 4)
    assert result["min"] == 0.5
    assert result["requirements_pilot"] == 2
    assert result["requirements_full"] == 2
    assert result["schema_invalid_records_pilot"] == 1
    assert result["schema_invalid_records_full"] == 0
    assert result["second_figure_both_schema_valid"] == {"pull_requests": 2, "mean": 0.75}
    row = result["per_pull_request"][0]
    assert row == {"pull": 1, "jaccard": 0.5, "places_pilot": 1, "places_full": 2,
                   "requirements_pilot": 1, "requirements_full": 1,
                   "schema_valid_pilot": True, "schema_valid_full": True}


def test_m3_missing_record_stops():
    with pytest.raises(ff3.MeasureError):
        ff3.m3([1, 2], {1: record(1, []), 2: record(2, [])}, {1: record(1, [])}, VALIDATOR)


def test_m3_counts_rejected_evidence_too():
    # The excerpt is not in the dataset, yet it is a source place (F3).
    rec = record(1, [requirement("QR-0001-01", [evidence("body", "invented text here", BOTH)],
                                 "indirect")])
    assert ff3.source_places(rec) == {("body", None)}


# --- M1 part b ----------------------------------------------------------

def test_m1_part_b():
    records = [record(1, []), record(2, [], valid=False), record(3, [])]
    assert ff3.m1_part_b(records, VALIDATOR) == {"records": 3, "schema_valid": 2,
                                                 "schema_invalid": 1}


# --- statement (i) ------------------------------------------------------

def records_for_i():
    found = evidence("body", "The Widget must do something.", BOTH)
    found_name_only = evidence("body", "The Widget must do something.", ["system_name"])
    missing = evidence("body", "This is not in the body at all.", BOTH)
    return [
        record(1, [
            requirement("QR-0001-01", [found], "indirect"),                 # supported
            requirement("QR-0001-02", [found_name_only], "insufficient"),   # unsupported, says so
            requirement("QR-0001-03", [missing], "direct",
                        source_form="prescriptive"),                       # unsupported, higher
            requirement("QR-0001-04", [found_name_only], "direct"),         # higher and differs
        ]),
        record(2, [requirement("QR-0002-01", [missing], "indirect")], valid=False),  # not in base
    ]


def test_statement_i():
    result = ff3.statement_i(records_for_i(), VALIDATOR, DATASET, {}, None, set())
    assert result == {"base_set": 4, "unsupported": 3, "stated_insufficient": 1,
                      "stated_higher": 2, "stated_higher_by_value": {"direct": 2},
                      "stated_higher_and_differs_from_all_evidence": 1,
                      "stated_differs_from_all_evidence_in_base_set": 1}


def counts_file(tmp_path, total=4, unsupported=3, differs=1):
    path = tmp_path / "counts.json"
    path.write_text(json.dumps({"counts": {"requirements": {
        "total": total, "m2": {"unsupported": unsupported},
        "stated_differs_from_all_evidence": differs}}}), encoding="utf-8")
    return path


def test_check_against_counts(tmp_path):
    result = ff3.statement_i(records_for_i(), VALIDATOR, DATASET, {}, None, set())
    ff3.check_against_counts(result, counts_file(tmp_path))
    for change in ({"total": 5}, {"unsupported": 2}, {"differs": 0}):
        with pytest.raises(ff3.MeasureError):
            ff3.check_against_counts(result, counts_file(tmp_path, **change))


# --- whole run ----------------------------------------------------------

SAMPLE = """# Pilot sample

## Drawn pull requests

| PR | Stratum |
|---|---|
| 1 | S1 |
| 2 | S2 |
"""


def write_jsonl(path, rows):
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


@pytest.fixture
def files(tmp_path):
    paths = {name: tmp_path / name for name in ("full.jsonl", "pilot.jsonl", "sample.md",
                                                "dataset.jsonl", "model_input.jsonl")}
    write_jsonl(paths["full.jsonl"], records_for_i())
    write_jsonl(paths["pilot.jsonl"], [record(1, []), record(2, [], valid=False)])
    paths["sample.md"].write_text(SAMPLE, encoding="utf-8")
    write_jsonl(paths["dataset.jsonl"], list(DATASET.values()))
    write_jsonl(paths["model_input.jsonl"], [{"pull_number": 1, "source_block": ""},
                                             {"pull_number": 2, "source_block": ""}])
    paths["counts"] = counts_file(tmp_path)
    paths["output"] = tmp_path / "out" / "ff3.json"
    return paths


def argv(files):
    return ["--full", str(files["full.jsonl"]), "--pilot", str(files["pilot.jsonl"]),
            "--pilot-sample", str(files["sample.md"]), "--dataset", str(files["dataset.jsonl"]),
            "--model-input", str(files["model_input.jsonl"]), "--schema", str(SCHEMA),
            "--counts", str(files["counts"]), "--output", str(files["output"])]


def test_run_writes_counts_without_content(files, capsys):
    assert ff3.main(argv(files)) == 0
    result = json.loads(files["output"].read_text(encoding="utf-8"))
    assert result["counts"]["m1_part_b_pilot"] == {"records": 2, "schema_valid": 1,
                                                   "schema_invalid": 1}
    assert result["counts"]["m3"]["pull_requests"] == 2
    assert result["counts"]["m2_statement_i"]["unsupported"] == 3
    text = files["output"].read_text(encoding="utf-8") + capsys.readouterr().out
    for fragment in ("Widget", "SECRET-RATIONALE", "must do"):
        assert fragment not in text


def test_run_refuses_overwrite(files):
    assert ff3.main(argv(files)) == 0
    assert ff3.main(argv(files)) == 2


def test_run_stops_when_pilot_differs_from_sample(files):
    write_jsonl(files["pilot.jsonl"], [record(1, [])])
    assert ff3.main(argv(files)) == 2
    assert not files["output"].exists()


def test_run_stops_on_count_mismatch(files, tmp_path):
    files["counts"] = counts_file(tmp_path, unsupported=99)
    assert ff3.main(argv(files)) == 2
    assert not files["output"].exists()


def test_duplicate_records_stop(files):
    write_jsonl(files["pilot.jsonl"], [record(1, []), record(2, []), record(2, [])])
    assert ff3.main(argv(files)) == 2


def test_run_stops_when_pilot_has_an_extra_pull_request(files):
    write_jsonl(files["pilot.jsonl"], [record(1, []), record(2, []), record(3, [])])
    assert ff3.main(argv(files)) == 2
    assert not files["output"].exists()
