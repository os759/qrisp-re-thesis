"""Tests for src/analyze/compare_b9_g1.py (B9 against "supported" after G1).

All data are invented. The file sets its import path itself.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
for _sub in ("extract", "prepare", "classify", "analyze"):
    if str(ROOT / "src" / _sub) not in sys.path:
        sys.path.insert(0, str(ROOT / "src" / _sub))

import compare_b9_g1 as cmp  # noqa: E402
from check_classification import load_requirements  # noqa: E402
from evaluate_requirements import Context  # noqa: E402

SCHEMA = ROOT / "config" / "requirement_schema_v2.json"
VALIDATOR = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))

BOTH = ["system_name", "system_response"]
NAME = ["system_name"]
RESPONSE = ["system_response"]
FOUND = "The Widget must do something."
MISSING = "This is not in the body at all."
DATASET = {
    1: {"number": 1, "title": "Widget title here", "body": FOUND,
        "issue_comments": [{"id": 7, "body": "Comment about the Widget behaviour."}],
        "review_comments": [], "files": []},
}


def evidence(excerpt, supports, location="body", locator=None):
    return {"location": location, "locator": locator, "excerpt": excerpt,
            "supports": list(supports)}


def requirement(rid, items, strength, source_form="descriptive"):
    return {"id": rid, "text": "The Widget shall do something useful.",
            "ears_pattern": "ubiquitous", "system_name": "Widget",
            "type": "functional_performance", "security_relevant": False,
            "rationale": "SECRET-RATIONALE for testing.", "evidence_strength": strength,
            "modality_set_by_convention": True, "evidence": items,
            "source_form": source_form}


def record(number, requirements, valid=True):
    rec = {"schema_version": 2, "pull_number": number,
           "processing_status": "requirements_found" if requirements else "no_requirements_found",
           "status_reason": None if requirements else "Nothing to extract here.",
           "requirements": requirements}
    if not valid:
        rec["schema_version"] = 1
    return rec


def cases():
    """One requirement per cell and reason, in a fixed order."""
    return [
        # both: all found, stated equals derived (indirect)
        requirement("QR-0001-01", [evidence(FOUND, BOTH)], "indirect"),
        # B9 only: all found, response not covered, model says insufficient
        requirement("QR-0001-02", [evidence(FOUND, NAME)], "insufficient"),
        # G1 only, not all found: found part covers both, the second is missing
        requirement("QR-0001-03", [evidence(FOUND, BOTH), evidence(MISSING, RESPONSE)],
                    "indirect"),
        # G1 only, strength differs: all found, derived indirect, stated direct
        requirement("QR-0001-04", [evidence(FOUND, BOTH)], "direct"),
        # G1 only, both reasons
        requirement("QR-0001-05", [evidence(FOUND, BOTH), evidence(MISSING, NAME)],
                    "insufficient"),
        # neither: nothing found
        requirement("QR-0001-06", [evidence(MISSING, BOTH)], "indirect"),
        # neither: all found, insufficient, model says indirect
        requirement("QR-0001-07", [evidence(FOUND, RESPONSE)], "indirect"),
    ]


def context():
    return Context(DATASET, {}, None, set())


def rows_for(requirements, number=1):
    return load_requirements([record(number, requirements)], VALIDATOR)


# --- judge and compare --------------------------------------------------

def test_judge_uses_found_evidence_for_g1_and_all_evidence_for_b9():
    judged = cmp.judge(rows_for(cases())[2], context())
    assert judged["key"] == "QR-0001-03"
    assert judged["B9"] is False and judged["G1"] is True
    assert judged["all_found"] is False and judged["strength_matches"] is True


def test_compare_cross_table():
    result = cmp.compare(rows_for(cases()), context())
    assert result["base_set"] == 7
    assert result["cross"] == {"b9_and_g1": 1, "b9_only": 1, "g1_only": 3, "neither": 2}
    assert result["b9_satisfied"] == 2
    assert result["g1_supported"] == 4
    assert result["identical_sets"] is False


def test_compare_reasons_and_ids():
    result = cmp.compare(rows_for(cases()), context())
    assert result["g1_only_by_reason"] == {"not_all_found": 1, "strength_differs": 1,
                                           "both": 1}
    assert result["b9_only_by_stated_strength"] == {"insufficient": 1}
    assert result["g1_only_by_strength_from_found_evidence"] == {"indirect": 3}
    assert result["ids"] == {"b9_only": ["QR-0001-02"],
                             "g1_only": ["QR-0001-03", "QR-0001-04", "QR-0001-05"]}


def test_identical_sets():
    result = cmp.compare(rows_for([cases()[0], cases()[5]]), context())
    assert result["identical_sets"] is True
    assert result["cross"] == {"b9_and_g1": 1, "b9_only": 0, "g1_only": 0, "neither": 1}
    assert result["g1_only_by_reason"] == {"not_all_found": 0, "strength_differs": 0, "both": 0}
    assert result["ids"] == {"b9_only": [], "g1_only": []}


def test_equal_counts_are_not_identical_sets():
    # The case the comparison exists for: one requirement leaves, another enters.
    result = cmp.compare(rows_for([cases()[1], cases()[2]]), context())
    assert result["b9_satisfied"] == result["g1_supported"] == 1
    assert result["identical_sets"] is False
    assert result["cross"] == {"b9_and_g1": 0, "b9_only": 1, "g1_only": 1, "neither": 0}


def test_direct_counts_as_supported():
    req = requirement("QR-0001-01", [evidence(FOUND, BOTH)], "direct", "prescriptive")
    result = cmp.compare(rows_for([req]), context())
    assert result["cross"]["b9_and_g1"] == 1


def test_schema_invalid_records_are_not_in_the_base_set():
    records = [record(1, cases()[:2]), record(2, [cases()[3]], valid=False)]
    rows = load_requirements(records, VALIDATOR)
    assert cmp.compare(rows, context())["base_set"] == 2


def test_g1_reason():
    assert cmp.g1_reason({"all_found": False, "strength_matches": True}) == "not_all_found"
    assert cmp.g1_reason({"all_found": True, "strength_matches": False}) == "strength_differs"
    assert cmp.g1_reason({"all_found": False, "strength_matches": False}) == "both"


# --- checks against the committed files ---------------------------------

def committed(base=7, b9=2, g1=4, total=7, sha="x"):
    evaluation = {"counts": {"machine": {"base_set": {"n": base, "B9": {"satisfied": b9}}}},
                  "inputs": {name: {"sha256": sha}
                             for name in ("input", "dataset", "model_input", "mentions_map")}}
    counts = {"counts": {"requirements": {"total": total, "ff4": {"supported": g1}}},
              "inputs": {name: {"sha256": sha} for name in ("input", "dataset", "model_input")}}
    return evaluation, counts


def test_check_against_committed():
    result = cmp.compare(rows_for(cases()), context())
    cmp.check_against_committed(result, *committed())
    for change in ({"base": 8}, {"total": 6}, {"b9": 3}, {"g1": 5}):
        with pytest.raises(cmp.CompareError):
            cmp.check_against_committed(result, *committed(**change))


def test_check_inputs():
    hashes = {"input": "x", "dataset": "x", "model_input": "x", "mentions_map": "x"}
    cmp.check_inputs(hashes, *committed())
    for name in hashes:
        with pytest.raises(cmp.CompareError):
            cmp.check_inputs({**hashes, name: "y"}, *committed())
    evaluation, counts = committed()
    counts["inputs"]["dataset"]["sha256"] = "y"
    with pytest.raises(cmp.CompareError):
        cmp.check_inputs(hashes, evaluation, counts)


def test_check_inputs_without_mentions_map():
    evaluation, counts = committed()
    evaluation["inputs"]["mentions_map"] = None
    hashes = {"input": "x", "dataset": "x", "model_input": "x", "mentions_map": None}
    cmp.check_inputs(hashes, evaluation, counts)
    with pytest.raises(cmp.CompareError):
        cmp.check_inputs({**hashes, "mentions_map": "x"}, evaluation, counts)


# --- whole run ----------------------------------------------------------

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_jsonl(path, rows):
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


@pytest.fixture
def files(tmp_path):
    paths = {name: tmp_path / name for name in ("full.jsonl", "dataset.jsonl",
                                                "model_input.jsonl")}
    write_jsonl(paths["full.jsonl"], [record(1, cases()), record(2, cases()[:1], valid=False)])
    write_jsonl(paths["dataset.jsonl"], list(DATASET.values()))
    write_jsonl(paths["model_input.jsonl"], [{"pull_number": 1, "source_block": ""}])
    write_committed(paths, tmp_path)
    paths["output"] = tmp_path / "out" / "compare.json"
    return paths


def write_committed(paths, tmp_path, b9=2, g1=4):
    hashes = {"input": sha(paths["full.jsonl"]), "dataset": sha(paths["dataset.jsonl"]),
              "model_input": sha(paths["model_input.jsonl"])}
    evaluation = {"counts": {"machine": {"base_set": {"n": 7, "B9": {"satisfied": b9}}}},
                  "inputs": {**{k: {"sha256": v} for k, v in hashes.items()},
                             "mentions_map": None}}
    counts = {"counts": {"requirements": {"total": 7, "ff4": {"supported": g1}}},
              "inputs": {k: {"sha256": v} for k, v in hashes.items()}}
    paths["evaluation"] = tmp_path / "evaluation.json"
    paths["counts"] = tmp_path / "counts.json"
    paths["evaluation"].write_text(json.dumps(evaluation), encoding="utf-8")
    paths["counts"].write_text(json.dumps(counts), encoding="utf-8")


def argv(files):
    return ["--input", str(files["full.jsonl"]), "--dataset", str(files["dataset.jsonl"]),
            "--model-input", str(files["model_input.jsonl"]), "--schema", str(SCHEMA),
            "--evaluation", str(files["evaluation"]), "--counts", str(files["counts"]),
            "--output", str(files["output"])]


def test_run_writes_counts_without_content(files, capsys):
    assert cmp.main(argv(files)) == 0
    result = json.loads(files["output"].read_text(encoding="utf-8"))
    assert result["counts"]["cross"] == {"b9_and_g1": 1, "b9_only": 1, "g1_only": 3,
                                         "neither": 2}
    assert result["inputs"]["input"]["sha256"] == sha(files["full.jsonl"])
    assert result["inputs"]["mentions_map"] is None
    assert result["program_sha256"] == sha(Path(cmp.__file__))
    text = files["output"].read_text(encoding="utf-8") + capsys.readouterr().out
    for fragment in ("Widget", "SECRET-RATIONALE", "must do", "not in the body"):
        assert fragment not in text


def test_run_refuses_overwrite(files):
    assert cmp.main(argv(files)) == 0
    before = files["output"].read_text(encoding="utf-8")
    assert cmp.main(argv(files)) == 2
    assert files["output"].read_text(encoding="utf-8") == before


def test_run_stops_on_count_mismatch(files, tmp_path):
    write_committed(files, tmp_path, g1=3)
    assert cmp.main(argv(files)) == 2
    assert not files["output"].exists()


def test_run_stops_on_other_input(files):
    write_jsonl(files["dataset.jsonl"], list(DATASET.values()) * 2)
    assert cmp.main(argv(files)) == 2
    assert not files["output"].exists()
