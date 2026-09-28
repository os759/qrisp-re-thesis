"""Tests for src/extract/breakdown_rejections.py with invented data.

The schema here is a small stand-in, so the tests do not depend on
config/requirement_schema_v2.json. What matters: the first failing
check is the one validate_output.py stops at, the counts add up to its
number of rejections, and no model text is printed.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "extract"))

import breakdown_rejections as b  # noqa: E402
from validate_output import check_record, excerpt_errors  # noqa: E402

SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object", "additionalProperties": False,
    "required": ["pull_number", "requirements"],
    "properties": {
        "pull_number": {"type": "integer"},
        "requirements": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["id", "ears_pattern", "source_form", "evidence_strength", "evidence"],
            "properties": {
                "id": {"type": "string"},
                "ears_pattern": {"enum": ["ubiquitous", "event_driven"]},
                "source_form": {"enum": ["prescriptive", "descriptive"]},
                "evidence_strength": {"enum": ["direct", "indirect", "insufficient"]},
                "evidence": {"type": "array", "items": {
                    "type": "object", "additionalProperties": False,
                    "required": ["location", "locator", "excerpt", "supports"],
                    "properties": {
                        "location": {"enum": ["title", "body", "diff"]},
                        "locator": {"type": ["string", "null"]},
                        "excerpt": {"type": "string"},
                        "supports": {"type": "array", "minItems": 1,
                                     "items": {"enum": ["system_name", "system_response",
                                                        "trigger"]}}}}}}}}},
}
VALIDATOR = Draft202012Validator(SCHEMA)

PULL = {"number": 3, "title": "Add the gate", "body": "The compiler shall cache gates.",
        "issue_comments": [], "review_comments": [],
        "files": [{"filename": "a.py", "patch": "@@ -1 +1 @@\n+cache = {}"}]}
DATASET = {3: PULL}
SECRET = "SECRET_MODEL_WORDING"


def requirement(ident="QR-0003-01", excerpt="The compiler shall cache gates.",
                strength="direct", **changes):
    req = {"id": ident, "ears_pattern": "ubiquitous", "source_form": "prescriptive",
           "evidence_strength": strength,
           "evidence": [{"location": "body", "locator": None, "excerpt": excerpt,
                         "supports": ["system_name", "system_response"]}]}
    req.update(changes)
    return req


def rec(*requirements):
    return {"pull_number": 3, "requirements": list(requirements)}


ACCEPTED = rec(requirement())
SCHEMA_BAD = rec(requirement(ears_pattern=SECRET))
SCHEMA_MISSING = {"pull_number": 3}
E6_BAD = rec(requirement(strength="indirect"))
EXCERPT_BAD = rec(requirement(), requirement("QR-0003-02", excerpt=SECRET))
SCHEMA_AND_EXCERPT = rec(requirement(excerpt=SECRET, ears_pattern="x"))
RECORDS = [ACCEPTED, SCHEMA_BAD, SCHEMA_MISSING, E6_BAD, EXCERPT_BAD, SCHEMA_AND_EXCERPT]


def analyse(record):
    return b.analyse(record, VALIDATOR, DATASET, None, set())


@pytest.mark.parametrize("record, first", [
    (ACCEPTED, None), (SCHEMA_BAD, "schema"), (SCHEMA_MISSING, "schema"),
    (E6_BAD, "e6"), (EXCERPT_BAD, "excerpt"), (SCHEMA_AND_EXCERPT, "schema"),
])
def test_first_check_is_the_one_the_checker_stops_at(record, first):
    assert analyse(record)["first"] == first
    assert bool(check_record(record, VALIDATOR, DATASET, None, set())) == (first is not None)


def test_counts_add_up_to_the_rejections_of_the_checker():
    summary = b.summarise([analyse(r) for r in RECORDS])
    rejected = sum(1 for r in RECORDS if check_record(r, VALIDATOR, DATASET, None, set()))
    assert summary["rejected"] == rejected == 5
    assert summary["first"] == {"schema": 3, "e6": 1, "excerpt": 1}
    assert sum(summary["first"].values()) == summary["rejected"]


def test_later_checks_are_reported_for_schema_rejections():
    summary = b.summarise([analyse(r) for r in RECORDS])
    assert summary["also_excerpt"] == {"e6: excerpts pass": 1,
                                       "schema: excerpts also fail": 1,
                                       "schema: excerpts pass": 2}


def test_failing_excerpts_match_the_checker():
    for record in RECORDS[:2] + RECORDS[3:]:
        failing = b.failing_excerpts(record, DATASET, None, set())
        assert len(failing) == len(excerpt_errors(record, DATASET, None, set()))
    assert b.failing_excerpts(EXCERPT_BAD, DATASET, None, set()) == [("QR-0003-02", 1, "body")]


def test_an_unknown_locator_counts_as_failing_excerpt():
    item = {"location": "diff", "locator": "missing.py", "excerpt": "cache = {}",
            "supports": ["system_name", "system_response"]}
    record = rec(requirement(evidence=[item]))
    assert b.failing_excerpts(record, DATASET, None, set()) == [("QR-0003-01", 1, "diff")]
    assert len(excerpt_errors(record, DATASET, None, set())) == 1
    assert analyse(record)["first"] == "excerpt"


def test_a_pull_missing_from_the_dataset_counts_as_excerpt_rejection():
    record = {"pull_number": 99, "requirements": [requirement()]}
    result = b.analyse(record, VALIDATOR, DATASET, None, set())
    assert result["first"] == "excerpt" and result["excerpts"] is None
    assert check_record(record, VALIDATOR, DATASET, None, set())


def test_schema_problems_carry_path_and_keyword_only():
    problems = analyse(SCHEMA_BAD)["schema"]
    assert problems == ["/requirements/*/ears_pattern enum"]
    assert analyse(SCHEMA_MISSING)["schema"] == ["/ required"]


def test_schema_kinds_count_records_not_occurrences():
    twice = rec(requirement(ears_pattern="x"), requirement("QR-0003-02", ears_pattern="y"))
    summary = b.summarise([analyse(twice)])
    assert summary["schema_kinds"] == {"/requirements/*/ears_pattern enum": 1}


def test_e6_pairs_name_stated_and_derived():
    summary = b.summarise([analyse(E6_BAD)])
    assert summary["e6_kinds"] == {"indirect -> direct": 1}
    assert summary["e6_requirements"] == 1


def write(tmp_path: Path, records) -> list[str]:
    (tmp_path / "in.jsonl").write_text("\n".join(json.dumps(r) for r in records) + "\n",
                                       encoding="utf-8")
    (tmp_path / "ds.jsonl").write_text(json.dumps(PULL) + "\n", encoding="utf-8")
    (tmp_path / "schema.json").write_text(json.dumps(SCHEMA), encoding="utf-8")
    return ["--input", str(tmp_path / "in.jsonl"), "--dataset", str(tmp_path / "ds.jsonl"),
            "--schema", str(tmp_path / "schema.json")]


def test_main_prints_counts_and_no_model_text(tmp_path, capsys):
    assert b.main(write(tmp_path, RECORDS)) == 0
    printed = capsys.readouterr().out
    assert "Records rejected: 5 (validate_output.py: 5)" in printed
    assert "Rejected by first failing check: schema 3, e6 1, excerpt 1" in printed
    assert SECRET not in printed


def test_main_shows_one_pull(tmp_path, capsys):
    assert b.main(write(tmp_path, [EXCERPT_BAD]) + ["--pull", "3"]) == 0
    printed = capsys.readouterr().out
    assert "pull 3: rejected by excerpt" in printed
    assert "excerpts not found: 1" in printed and "QR-0003-02  evidence 1  location body" in printed
    assert SECRET not in printed


def test_main_stops_when_counts_disagree(tmp_path, capsys, monkeypatch):
    monkeypatch.setattr(b, "check_record", lambda *args: [])
    assert b.main(write(tmp_path, RECORDS)) == 2
    assert "ERROR" in capsys.readouterr().out
