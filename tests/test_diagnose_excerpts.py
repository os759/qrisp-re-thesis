"""Tests for src/extract/diagnose_excerpts.py with invented data.

One pull request, three files, one review comment. Every cause and every
count of point 5 has one case. The last tests check that the script
rejects exactly what validate_output.py rejects, and that it prints no
excerpt text. Adapted on 2026-09-24 to the tightened validate_output.py.
Extended on 2026-09-27 by the cause context_marker_kept (addendum to E10
of that day, part 1), and adapted the same day to point 3: edge
whitespace is accepted now, so edge_whitespace is left only for a rest
shorter than 10 characters.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "extract"))

import diagnose_excerpts as d  # noqa: E402
from validate_output import excerpt_errors, strip_diff_markers  # noqa: E402

PATCH_A = "\n".join([
    "@@ -1,4 +1,5 @@ def setup():",
    " context line one",
    "-removed line here",
    "+added line alpha",
    "+++plus plus content",
    " context two",
    "@@ -10,2 +11,2 @@",
    "+second hunk line",
    " context three",
])

PULL = {
    "number": 7,
    "title": "Title text about the feature",
    "body": "Body mentions @alice and describes the change in detail",
    "issue_comments": [],
    "review_comments": [{"id": 11, "body": "Please keep this check",
                         "diff_hunk": "@@ -1 +1 @@\n+hunk only context line"}],
    "files": [
        {"filename": "src/a.py", "patch": PATCH_A},
        {"filename": "src/b.py", "patch": "@@ -1 +1 @@\n+other file content here"},
        {"filename": "src/c.py", "patch": "@@ -1 +1 @@\n+hidden file content"},
    ],
}

BLOCK = "\n\n".join([
    "=== PULL REQUEST 7 ===",
    "[FILE src/a.py status=modified +4 -1]\n" + PATCH_A,
    "[FILE src/b.py status=added +1 -0]\n@@ -1 +1 @@\n+other file content here",
    "[FILE src/c.py status=added +1 -0]\n(diff not included: pull_budget_exhausted)",
])

MAPPING = {"alice": "person_01"}
SHOWN = d.files_in_block(BLOCK)


def diff(excerpt: str, locator: str = "src/a.py") -> dict:
    return {"location": "diff", "locator": locator, "excerpt": excerpt}


def cause(item: dict) -> str:
    return d.classify(item, PULL, SHOWN, MAPPING, set())


def test_block_parser_skips_files_not_included():
    assert SHOWN == {"src/a.py", "src/b.py"}


CAUSE_CASES = [
    (diff("x", locator="src/missing.py"), "locator_not_found"),
    (diff(" context line one"), "context_marker_kept"),
    (diff(" context three  "), "context_marker_kept"),
    (diff(" context line one\nadded line alpha"), "context_marker_kept"),
    (diff(" context line one", locator="src/b.py"), "other_file"),
    (diff("   alpha   "), "edge_whitespace"),
    (diff("removed line here"), "removed_line"),
    (diff("@@ -10,2 +11,2 @@\nsecond hunk line"), "hunk_header"),
    (diff("def setup():"), "hunk_header"),
    (diff("context line one\nadded line alpha"), "spans_removed_line"),
    (diff("context two\nsecond hunk line"), "spans_hunk_header"),
    (diff("def setup():\ncontext line one\nadded line alpha"), "hunk_header"),
    (diff("removed line here\nadded line alpha\n++plus plus content\n"
          "context two\nsecond hunk line"), "removed_line"),
    (diff("+added line alpha"), "diff_markers_kept"),
    (diff("added  line   alpha"), "inner_whitespace"),
    (diff("context line one ... context two"), "ellipsis"),
    (diff("context line one \u2026 context two"), "ellipsis"),
    (diff("other file content here"), "other_file"),
    (diff("hunk only context line"), "review_context"),
    ({"location": "review_comment", "locator": "11",
      "excerpt": "hunk only context line"}, "review_context"),
    (diff("describes the change in detail"), "other_location"),
    (diff("invented content that is nowhere", locator="src/c.py"), "file_not_in_block"),
    (diff("context line one and added alpha line"), "likely_rephrased"),
    (diff("completely unrelated wording xyz"), "no_match"),
    ({"location": "body", "locator": None,
      "excerpt": "describes  the change"}, "inner_whitespace"),
    ({"location": "title", "locator": None,
      "excerpt": "describes the change in detail"}, "other_location"),
]


@pytest.mark.parametrize("item, expected", CAUSE_CASES)
def test_every_cause(item, expected):
    assert cause(item) == expected


def test_every_cause_case_is_rejected_by_validate_output():
    """A cause is only meaningful for an excerpt the checker rejects."""
    cases = [case for case, _ in CAUSE_CASES]
    rejected = excerpt_errors(record(cases), {7: PULL}, MAPPING, set())
    assert len(rejected) == len(cases)


def test_marker_check_comes_before_edge_whitespace():
    order = list(d.CAUSES)
    assert order.index("context_marker_kept") < order.index("edge_whitespace")


@pytest.mark.parametrize("excerpt, patch, expected", [
    (" fake context", " fake context\n@@ -1 +1 @@\n+real line", False),
    (" \ncontext two", PATCH_A, False),
    (" context two", PATCH_A, True),
    ("context two", PATCH_A, False),
])
def test_marker_rule_conditions(excerpt, patch, expected):
    pull = {"files": [{"filename": "x.py", "patch": patch}]}
    item = {"location": "diff", "locator": "x.py", "excerpt": excerpt}
    assert d.context_marker_kept(item, pull) is expected


def test_marker_rule_needs_a_diff():
    item = {"location": "body", "locator": None, "excerpt": " context two"}
    assert d.context_marker_kept(item, PULL) is False


@pytest.mark.parametrize("item", [
    diff(" added line alpha"),
    diff("  added line alpha "),
    diff("second hunk line\n"),
    {"location": "body", "locator": None, "excerpt": " describes the change in detail "},
])
def test_edge_whitespace_is_accepted_now(item):
    rec = record([item])
    assert excerpt_errors(rec, {7: PULL}, MAPPING, set()) == []
    result = d.diagnose([rec], {7: PULL}, {7: BLOCK}, MAPPING, set())
    assert result["rejected"] == []


def test_rules_match_the_addendum_to_e10():
    """Rule 1 and rule 3 are closed lists; everything else is rule 2."""
    by_rule = {r: {c for c, (rule, _) in d.CAUSES.items() if rule == r} for r in (1, 2, 3)}
    assert by_rule[1] == {"edge_whitespace"}
    assert by_rule[3] == {"likely_rephrased", "no_match"}
    assert len(by_rule[2]) == len(d.CAUSES) - 3


@pytest.mark.parametrize("patch", [
    PATCH_A,
    "@@ -1,2 +1 @@\n-gone\n+kept\n-gone too\n",
    "--- a/x.py\n+++ b/x.py\n@@ -1 +1 @@\n+++counter",
])
def test_default_view_equals_the_checker(patch):
    assert d._view(patch) == strip_diff_markers(patch)


def test_masked_prose_is_found_as_other_location():
    assert cause(diff("Body mentions @person_01")) == "other_location"


@pytest.mark.parametrize("item, expected", [
    (diff("hidden file content", locator="src/c.py"), ["file_not_in_block"]),
    (diff("added line alpha"), []),
    ({"location": "review_comment", "locator": "11",
      "excerpt": "Please keep this check"}, []),
])
def test_lenient_findings(item, expected):
    assert d.lenient_findings(item, SHOWN) == expected


def record(excerpts: list[dict]) -> dict:
    return {"pull_number": 7, "requirements": [
        {"id": f"QR-0007-{n:02d}", "evidence": [item]}
        for n, item in enumerate(excerpts, start=1)]}


MIXED = [diff("added line alpha"), diff("+added line alpha"),
         diff("removed line here"), diff("context line one\nadded line alpha"),
         {"location": "body", "locator": None, "excerpt": "Body mentions @person_01"}]


def test_same_rejections_as_validate_output():
    rec = record(MIXED)
    result = d.diagnose([rec], {7: PULL}, {7: BLOCK}, MAPPING, set())
    assert len(result["rejected"]) == len(excerpt_errors(rec, {7: PULL}, MAPPING, set()))
    assert [e["cause"] for e in result["rejected"]] == [
        "diff_markers_kept", "removed_line", "spans_removed_line"]
    assert result["accepted_by_location"] == {"diff": 1, "body": 1}
    assert result["lenient"] == {}


def test_cause_before_is_reported_for_marker_cases():
    rec = record([diff(" context line one"), diff(" context line one\nadded line alpha"),
                  diff("+added line alpha")])
    result = d.diagnose([rec], {7: PULL}, {7: BLOCK}, MAPPING, set())
    assert [(e["cause"], e["before"]) for e in result["rejected"]] == [
        ("context_marker_kept", "edge_whitespace"),
        ("context_marker_kept", "spans_removed_line"),
        ("diff_markers_kept", None)]


def test_rule_four_counts_distinct_pulls():
    rejected = [{"pull": 1, "cause": "removed_line"}, {"pull": 1, "cause": "removed_line"},
                {"pull": 2, "cause": "ellipsis"}, {"pull": 3, "cause": "ellipsis"},
                {"pull": 4, "cause": "edge_whitespace"}]
    assert d.rule_four(rejected) == {"removed_line": 1, "ellipsis": 2}


def test_main_prints_no_excerpt_text(tmp_path, capsys):
    secret = "completely unrelated wording xyz"
    files = {"input.jsonl": record([diff(secret)]), "dataset.jsonl": PULL,
             "model_input.jsonl": {"pull_number": 7, "source_block": BLOCK}}
    for name, content in files.items():
        (tmp_path / name).write_text(json.dumps(content) + "\n", encoding="utf-8")
    (tmp_path / "map.json").write_text(json.dumps(MAPPING), encoding="utf-8")
    assert d.main(["--input", str(tmp_path / "input.jsonl"),
                   "--dataset", str(tmp_path / "dataset.jsonl"),
                   "--model-input", str(tmp_path / "model_input.jsonl"),
                   "--mentions-map", str(tmp_path / "map.json")]) == 0
    printed = capsys.readouterr().out
    assert "cause no_match  rule 3" in printed
    assert "context_marker_kept by cause before 2026-09-27: none" in printed
    assert secret not in printed and "unrelated" not in printed


def test_main_prints_the_cause_before(tmp_path, capsys):
    files = {"input.jsonl": record([diff(" context line one")]), "dataset.jsonl": PULL,
             "model_input.jsonl": {"pull_number": 7, "source_block": BLOCK}}
    for name, content in files.items():
        (tmp_path / name).write_text(json.dumps(content) + "\n", encoding="utf-8")
    assert d.main(["--input", str(tmp_path / "input.jsonl"),
                   "--dataset", str(tmp_path / "dataset.jsonl"),
                   "--model-input", str(tmp_path / "model_input.jsonl")]) == 0
    printed = capsys.readouterr().out
    assert "cause context_marker_kept  rule 2  before edge_whitespace" in printed
    assert "context_marker_kept by cause before 2026-09-27: edge_whitespace 1" in printed
    assert "context line one" not in printed
