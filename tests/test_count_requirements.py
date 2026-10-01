"""Tests for src/analyze/count_requirements.py (work package G, step 1).

All data are invented. The tests pin the rules of F3 (M2) and G1 in
docs/entscheidungen.md: which evidence counts as found, how M2 and the
strength for FF4 follow, and that nothing but counts leaves the script.
"""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
for sub in ("analyze", "extract", "prepare"):
    if str(ROOT / "src" / sub) not in sys.path:
        sys.path.insert(0, str(ROOT / "src" / sub))

from jsonschema import Draft202012Validator  # noqa: E402

import count_requirements as cr  # noqa: E402

SCHEMA = json.loads((ROOT / "config" / "requirement_schema_v2.json").read_text(encoding="utf-8"))

PULLS = {
    101: {
        "number": 101,
        "title": "Add input validation to the parser",
        "body": "The parser must reject malformed input values before compilation. "
                "this is short text",
        "issue_comments": [{"id": 9001, "body": "Please also log rejected inputs."}],
        "review_comments": [],
        "files": [{"filename": "src/qrisp/parser.py",
                   "patch": "@@ -1,2 +1,3 @@\n def parse(x):\n+    validate_input(x)\n     return x"}],
    },
    102: {
        "number": 102,
        "title": "Document the transpiler options",
        "body": "", "issue_comments": [], "review_comments": [], "files": [],
    },
    103: {
        "number": 103,
        "title": "Fix typo", "body": "", "issue_comments": [], "review_comments": [],
        "files": [],
    },
}

BLOCKS = {101: "[FILE src/qrisp/parser.py status=modified +1 -0]\n@@ -1,2 +1,3 @@\n"}


def evidence(location, excerpt, supports, locator=None):
    return {"location": location, "locator": locator, "html_url": None,
            "excerpt": excerpt, "supports": supports}


def requirement(number, index, *, pattern="ubiquitous", kind="functional_performance",
                security=False, stated="direct", form="prescriptive", items=()):
    return {
        "id": f"QR-{number:04d}-{index:02d}",
        "text": "The parser shall reject malformed input.",
        "ears_pattern": pattern, "system_name": "parser", "type": kind,
        "security_relevant": security, "rationale": "Invented rationale.",
        "evidence_strength": stated, "modality_set_by_convention": True,
        "evidence": list(items), "source_form": form,
    }


BOTH = ["system_name", "system_response"]


def records():
    req_101 = [
        # A: found, prescriptive -> direct everywhere.
        requirement(101, 1, items=[evidence(
            "body", "The parser must reject malformed input values", BOTH)]),
        # B: second evidence not found (rule 3, likely_rephrased) carries the response.
        requirement(101, 2, kind="interface", items=[
            evidence("title", "Add input validation to the parser", ["system_name"]),
            evidence("body", "The parser shall reject malformed input", ["system_response"])]),
        # C: diff excerpt found, descriptive -> indirect, security relevant.
        requirement(101, 3, pattern="event_driven", kind="quality_non_functional",
                    security=True, stated="indirect", form="descriptive", items=[evidence(
                        "diff", "    validate_input(x)", BOTH + ["trigger"],
                        locator="src/qrisp/parser.py")]),
        # D: edge whitespace with a rest under 10 characters -> rule 1 -> found.
        requirement(101, 4, items=[evidence("body", "  short   ", BOTH)]),
        # E: quoted from a comment but named as body -> rule 2; stated value differs.
        requirement(101, 5, kind="process", security=True, stated="insufficient",
                    items=[evidence("body", "Please also log rejected inputs.", BOTH)]),
        # G: found, but the trigger of event_driven is not covered -> insufficient.
        requirement(101, 6, pattern="event_driven", stated="insufficient",
                    form="descriptive", items=[evidence(
                        "title", "Add input validation to the parser", BOTH)]),
    ]
    req_999 = [
        # F: pull missing from the dataset -> not found.
        requirement(999, 1, kind="usability_quality_in_use",
                    items=[evidence("body", "Anything at all here", BOTH)]),
        # H: not found and trigger missing -> both conditions of M2.
        requirement(999, 2, pattern="event_driven", kind="human_factors",
                    stated="insufficient", items=[evidence("body", "Anything else here", BOTH)]),
    ]
    return [
        {"schema_version": 2, "pull_number": 101, "processing_status": "requirements_found",
         "status_reason": None, "requirements": req_101},
        # Schema error (invented field): excerpts counted, requirements not.
        {"schema_version": 2, "pull_number": 102, "processing_status": "requirements_found",
         "status_reason": None, "confidence": 0.9, "requirements": [requirement(
             102, 1, items=[evidence("title", "Document the transpiler options", BOTH)])]},
        {"schema_version": 2, "pull_number": 103, "processing_status": "no_requirements_found",
         "status_reason": "Only a typo fix.", "requirements": []},
        {"schema_version": 2, "pull_number": 999, "processing_status": "requirements_found",
         "status_reason": None, "requirements": req_999},
    ]


@pytest.fixture
def summary():
    return cr.count_run(records(), Draft202012Validator(SCHEMA), PULLS, BLOCKS)


# --- records and excerpts ----------------------------------------------


def test_records_and_schema(summary):
    assert summary["records"] == {
        "read": 4, "schema_valid": 3, "schema_invalid": 1,
        "processing_status_schema_valid": {"no_requirements_found": 1,
                                           "requirements_found": 2}}


def test_excerpts_cover_all_records_including_schema_errors(summary):
    assert summary["excerpts_all_records"] == {
        "total": 10, "accepted": 5, "rejected": 5,
        "rejected_by_rule": {"1": 1, "2": 3, "3": 1}}


@pytest.mark.parametrize("item, pull, found, rule", [
    (evidence("body", "The parser must reject malformed input values", BOTH), 101, True, None),
    (evidence("body", "  short   ", BOTH), 101, True, 1),
    (evidence("body", "Please also log rejected inputs.", BOTH), 101, False, 2),
    (evidence("body", "The parser shall reject malformed input", BOTH), 101, False, 3),
    (evidence("body", "Anything at all here", BOTH), 999, False, 2),
])
def test_evidence_status(item, pull, found, rule):
    shown = cr.files_in_block(BLOCKS.get(pull, ""))
    assert cr.evidence_status(item, PULLS.get(pull), shown, None, set()) == (found, rule)


# --- requirements ------------------------------------------------------


def test_requirement_counts(summary):
    req = summary["requirements"]
    assert req["total"] == 8
    assert req["by_type"] == {"functional_performance": 3, "human_factors": 1, "interface": 1,
                              "process": 1, "quality_non_functional": 1,
                              "usability_quality_in_use": 1}
    assert req["security_relevant"] == {"true": 2, "false": 6}
    assert req["type_by_security_relevant"]["process"] == {"true": 1, "false": 0}
    assert req["strength_from_all_evidence"] == {"direct": 5, "indirect": 1, "insufficient": 2}
    assert req["stated_differs_from_all_evidence"] == 1
    assert req["partly_found"] == 1


def test_m2(summary):
    assert summary["requirements"]["m2"] == {
        "no_evidence_found": 3, "insufficient_from_all_evidence": 2,
        "both": 1, "unsupported": 4}


def test_ff4(summary):
    assert summary["requirements"]["ff4"] == {
        "strength_from_found_evidence": {"direct": 2, "indirect": 1, "insufficient": 5},
        "supported": 3, "strength_changed_by_g1": 3,
        "m2_supported_but_not_ff4": 1, "ff4_supported_but_m2_unsupported": 0}


def test_security_relevant_only(summary):
    assert summary["requirements"]["security_relevant_only"] == {
        "total": 2, "by_type": {"process": 1, "quality_non_functional": 1},
        "strength_from_found_evidence": {"indirect": 1, "insufficient": 1},
        "ff4_supported": 1, "m2_unsupported": 1}


def test_g1_strength_uses_found_evidence_only():
    req = requirement(1, 1, items=[
        evidence("title", "x" * 10, ["system_name"]),
        evidence("body", "y" * 10, ["system_response"])])
    row = cr.assess_requirement(req, [True, False])
    assert (row["strength_all"], row["strength_ff4"]) == ("direct", "insufficient")
    assert not row["m2_unsupported"] and not row["ff4_supported"]


@pytest.mark.parametrize("pattern", ["ubiquitous", "event_driven", "state_driven", "complex"])
@pytest.mark.parametrize("form", ["prescriptive", "descriptive"])
def test_ff4_supported_is_never_m2_unsupported(pattern, form):
    """G1, consequence: supported for FF4 implies supported for M2."""
    parts = ["system_name", "system_response", "precondition", "trigger"]
    supports = [list(c) for n in (1, 2) for c in itertools.combinations(parts, n)]
    for chosen in itertools.combinations(supports, 2):
        items = [evidence("body", "z" * 10, s) for s in chosen]
        for flags in itertools.product([True, False], repeat=2):
            row = cr.assess_requirement(
                requirement(1, 1, pattern=pattern, form=form, items=items), list(flags))
            assert not (row["ff4_supported"] and row["m2_unsupported"])
            if not any(flags):
                assert row["m2_unsupported"] and row["strength_ff4"] == "insufficient"


# --- command line ------------------------------------------------------


def write_inputs(tmp_path):
    def jsonl(name, rows):
        path = tmp_path / name
        path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
        return path
    return (jsonl("extraction.jsonl", records()),
            jsonl("dataset.jsonl", PULLS.values()),
            jsonl("model_input.jsonl", [{"pull_number": n, "source_block": b}
                                        for n, b in BLOCKS.items()]))


def test_main_writes_counts_and_no_content(tmp_path, capsys):
    extraction, dataset, model_input = write_inputs(tmp_path)
    output = tmp_path / "out" / "counts.json"
    code = cr.main(["--input", str(extraction), "--dataset", str(dataset),
                    "--model-input", str(model_input),
                    "--schema", str(ROOT / "config" / "requirement_schema_v2.json"),
                    "--output", str(output)])
    assert code == 0
    printed = capsys.readouterr().out
    written = output.read_text(encoding="utf-8")
    result = json.loads(written)
    assert result["counts"]["requirements"]["ff4"]["supported"] == 3
    assert result["inputs"]["input"]["sha256"] == cr.sha256_of(extraction)
    for text in ("malformed", "validate_input", "short text", "rejected inputs",
                 "transpiler", "Invented rationale", "shall reject"):
        assert text not in printed and text not in written


def test_main_refuses_to_overwrite(tmp_path):
    extraction, dataset, model_input = write_inputs(tmp_path)
    output = tmp_path / "counts.json"
    output.write_text("keep", encoding="utf-8")
    code = cr.main(["--input", str(extraction), "--dataset", str(dataset),
                    "--model-input", str(model_input), "--output", str(output),
                    "--schema", str(ROOT / "config" / "requirement_schema_v2.json")])
    assert code == 2 and output.read_text(encoding="utf-8") == "keep"
