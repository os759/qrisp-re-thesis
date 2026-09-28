"""Tests for src/extract/inspect_excerpts.py with invented data.

The script must select exactly the excerpts that diagnose_excerpts.py
puts under rule 3, show the right hints, refuse to print content into
a pipe, and write no content into the assignment table. The table
check must catch every wrong or missing value.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "extract"))

import diagnose_excerpts as d  # noqa: E402
import inspect_excerpts as ie  # noqa: E402
from validate_output import BARRIER  # noqa: E402

PATCH = "\n".join([
    "@@ -1,3 +1,3 @@",
    " def rotate(qubit, angle):",
    "-    return old_rotation(qubit)",
    "+    return apply_rotation(qubit, angle)",
    " # end of rotate",
])

PULL = {
    "number": 9,
    "title": "Add rotation gate",
    "body": "The simulator shall apply the rotation angle to the qubit.",
    "issue_comments": [], "review_comments": [],
    "files": [{"filename": "src/gate.py", "patch": PATCH}],
}

BLOCK = "\n\n".join([
    "=== PULL REQUEST 9 ===",
    "[TITLE]\nAdd rotation gate",
    "[BODY]\nThe simulator shall apply the rotation angle to the qubit.",
    "[FILE src/gate.py status=modified +1 -1]\n" + PATCH,
])

SECRET = "the rotation angle shall apply the simulator to the qubit"


def diff(excerpt: str) -> dict:
    return {"location": "diff", "locator": "src/gate.py", "excerpt": excerpt}


def body(excerpt: str) -> dict:
    return {"location": "body", "locator": None, "excerpt": excerpt}


ITEMS = [
    body("The simulator shall apply the rotation angle to the qubit."),  # accepted
    body(SECRET),                                                        # likely_rephrased
    body("completely unrelated wording xyz"),                            # no_match
    diff("+    return apply_rotation(qubit, angle)"),                     # diff_markers_kept
    diff("return apply_rotation(qubit,angle)"),                           # likely_rephrased
]


def record(items: list[dict]) -> dict:
    return {"pull_number": 9, "requirements": [
        {"id": f"QR-0009-{n:02d}", "evidence": [item]}
        for n, item in enumerate(items, start=1)]}


RECORDS = [record(ITEMS)]


def selection():
    return ie.select(RECORDS, {9: PULL}, {9: BLOCK}, None, set())


# --- selection ----------------------------------------------------------


def test_selection_equals_rule_three_of_the_search_program():
    result = d.diagnose(RECORDS, {9: PULL}, {9: BLOCK}, None, set())
    expected = [(e["pull"], e["id"], e["position"], e["cause"])
                for e in result["rejected"] if d.CAUSES[e["cause"]][0] == 3]
    got = [(e["pull"], e["id"], e["position"], e["cause"]) for e in selection()]
    assert got == expected
    assert [c for *_, c in got] == ["likely_rephrased", "no_match", "likely_rephrased"]


def test_an_accepted_excerpt_is_never_selected():
    """Acceptance comes from excerpt_found over all candidates, not from one text.

    A whitespace-only excerpt found in the second comment is accepted by
    the checker, although classify alone would call it no_match.
    """
    pull = dict(PULL, issue_comments=[{"id": 1, "body": "first"},
                                      {"id": 2, "body": "a            b"}])
    item = {"location": "issue_comment", "locator": None, "excerpt": "          "}
    assert d.classify(item, pull, set()) == "no_match"
    assert ie.select([record([item])], {9: pull}, {9: BLOCK}, None, set()) == []


def test_selection_is_numbered_from_one():
    assert [e["nr"] for e in selection()] == [1, 2, 3]


def test_rule_three_causes_come_from_the_search_program():
    assert ie.RULE_THREE_CAUSES == {"likely_rephrased", "no_match"}


def test_subtypes_follow_the_addendum_of_2026_09_28():
    assert list(ie.SUBTYPES.items()) == [
        ("pruefprogramm", 1), ("zusammengesetzt", 2), ("umformuliert", 2),
        ("zeichen", 2), ("ohne_gegenstueck", 2)]


def test_a_pull_missing_from_the_dataset_is_skipped():
    assert ie.select(RECORDS, {}, {}, None, set()) == []


# --- hints --------------------------------------------------------------


def test_markerless_view_keeps_line_count_and_sets_barriers():
    lines = ie.markerless_lines(PATCH)
    assert len(lines) == len(PATCH.split("\n"))
    assert lines[0] == BARRIER and lines[2] == BARRIER
    assert lines[1] == "def rotate(qubit, angle):"
    assert lines[3] == "    return apply_rotation(qubit, angle)"


def test_hint_finds_a_diff_excerpt_without_markers():
    found, line, header = ie.block_hint("def rotate(qubit, angle):", BLOCK)
    assert found and header.startswith("[FILE src/gate.py")
    assert BLOCK.split("\n")[line - 1] == " def rotate(qubit, angle):"


def test_hint_finds_prose_in_the_raw_block():
    found, _, header = ie.block_hint("  shall apply the rotation angle ", BLOCK)
    assert found and header == "[BODY]"


def test_hint_does_not_join_across_a_removed_line():
    excerpt = "def rotate(qubit, angle):\n    return apply_rotation(qubit, angle)"
    assert ie.block_hint(excerpt, BLOCK)[0] is False


@pytest.mark.parametrize("excerpt", [SECRET, "", "   "])
def test_hint_is_no_for_rephrased_or_empty(excerpt):
    assert ie.block_hint(excerpt, BLOCK) == (False, None, None)


def test_closest_passage_finds_the_changed_line():
    window, ratio = ie.closest_passage("return apply_rotaton(qubit, angle)",
                                       ["unrelated text", "x" * 50 + "return apply_rotation(qubit, angle)"])
    assert "apply_rotation" in window and ratio > 0.8


def test_differences_mark_one_missing_character_only():
    marked = ie.mark_differences("xx return apply_rotation(q) yy", "return apply_rotaton(q)")
    assert marked == "return apply_rotat[-i-]on(q)"


def test_differences_show_added_text():
    assert ie.mark_differences("a b", "a x b") == "a {+x +}b"


def test_differences_show_a_backslash_change():
    assert ie.mark_differences(r"a \\ket b", r"a \ket b") == r"a [-\-]\ket b"


def test_barrier_is_shown_readably():
    assert ie.visible("a" + BARRIER + "b") == "a" + ie.BARRIER_SHOWN + "b"


# --- template and tally -------------------------------------------------


def filled(tmp_path: Path, values: list[tuple[str, str, str, str]]) -> Path:
    path = tmp_path / "table.md"
    ie.write_template(selection(), path)
    lines = path.read_text(encoding="utf-8").split("\n")
    out, index = [], 0
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("|") and cells[0].isdigit():
            rule, subtype, other, doubt = values[index]
            line = "| " + " | ".join(cells[:5] + [rule, subtype, other, doubt]) + " |"
            index += 1
        out.append(line)
    path.write_text("\n".join(out), encoding="utf-8")
    return path


def test_template_holds_identifiers_and_no_content(tmp_path):
    path = tmp_path / "table.md"
    ie.write_template(selection(), path)
    text = path.read_text(encoding="utf-8")
    assert "QR-0009-02" in text and "likely_rephrased" in text
    assert SECRET not in text and "unrelated" not in text and "qubit,angle" not in text
    assert len(ie.read_table(path)) == 3


def test_template_never_overwrites(tmp_path):
    path = tmp_path / "table.md"
    path.write_text("kept", encoding="utf-8")
    with pytest.raises(FileExistsError):
        ie.write_template(selection(), path)
    assert path.read_text(encoding="utf-8") == "kept"


def test_tally_counts_a_valid_table(tmp_path):
    path = filled(tmp_path, [("2", "umformuliert", "nein", "nein"),
                             ("2", "ohne_gegenstueck", "nein", "ja"),
                             ("1", "pruefprogramm", "nein", "nein")])
    problems, counts = ie.tally(selection(), path)
    assert problems == []
    assert counts["rule"] == {"2": 2, "1": 1}
    assert counts["subtype"]["ohne_gegenstueck"] == 1
    assert counts["doubt"] == {"nein": 2, "ja": 1}
    assert counts["cause_rule"]["likely_rephrased -> rule 2"] == 1
    assert counts["pulls_rule"] == {"1": 1, "2": 1}


@pytest.mark.parametrize("values, fragment", [
    ([("3", "zeichen", "nein", "nein")] + [("2", "zeichen", "nein", "nein")] * 2, "rule must be"),
    ([("2", "pruefprogramm", "nein", "nein")] + [("2", "zeichen", "nein", "nein")] * 2,
     "belongs to rule 1"),
    ([("1", "zeichen", "nein", "nein")] + [("2", "zeichen", "nein", "nein")] * 2,
     "belongs to rule 2"),
    ([("2", "tippfehler", "nein", "nein")] + [("2", "zeichen", "nein", "nein")] * 2,
     "unknown subtype"),
    ([("2", "zeichen", "", "nein")] + [("2", "zeichen", "nein", "nein")] * 2, "ja or nein"),
    ([("2", "zeichen", "nein", "vielleicht")] + [("2", "zeichen", "nein", "nein")] * 2,
     "ja or nein"),
    ([("1", "pruefprogramm", "ja", "nein")] + [("2", "zeichen", "nein", "nein")] * 2,
     "needs the named place"),
])
def test_tally_rejects_wrong_values(tmp_path, values, fragment):
    problems, counts = ie.tally(selection(), filled(tmp_path, values))
    assert any(fragment in p for p in problems)
    assert sum(counts["rule"].values()) == 2


def test_tally_rejects_a_missing_row(tmp_path):
    path = filled(tmp_path, [("2", "zeichen", "nein", "nein")] * 3)
    lines = [l for l in path.read_text(encoding="utf-8").split("\n") if not l.startswith("| 3 ")]
    path.write_text("\n".join(lines), encoding="utf-8")
    problems, _ = ie.tally(selection(), path)
    assert any("2 rows" in p for p in problems)


def test_tally_rejects_changed_identifiers(tmp_path):
    path = filled(tmp_path, [("2", "zeichen", "nein", "nein")] * 3)
    path.write_text(path.read_text(encoding="utf-8").replace("QR-0009-03", "QR-0009-09"),
                    encoding="utf-8")
    problems, _ = ie.tally(selection(), path)
    assert any("identifiers differ" in p for p in problems)


# --- main ---------------------------------------------------------------


def write_inputs(tmp_path: Path) -> list[str]:
    (tmp_path / "input.jsonl").write_text(json.dumps(RECORDS[0]) + "\n", encoding="utf-8")
    (tmp_path / "dataset.jsonl").write_text(json.dumps(PULL) + "\n", encoding="utf-8")
    (tmp_path / "model_input.jsonl").write_text(
        json.dumps({"pull_number": 9, "source_block": BLOCK}) + "\n", encoding="utf-8")
    return ["--input", str(tmp_path / "input.jsonl"),
            "--dataset", str(tmp_path / "dataset.jsonl"),
            "--model-input", str(tmp_path / "model_input.jsonl")]


def test_main_refuses_content_into_a_pipe(tmp_path, capsys):
    assert ie.main(write_inputs(tmp_path)) == 2
    printed = capsys.readouterr().out
    assert "Refused" in printed and SECRET not in printed


def test_main_list_prints_no_content(tmp_path, capsys):
    assert ie.main(write_inputs(tmp_path) + ["--list"]) == 0
    printed = capsys.readouterr().out
    assert "Rule 3 excerpts: 3  (likely_rephrased 2, no_match 1)" in printed
    assert SECRET not in printed and "unrelated" not in printed


def test_main_shows_one_excerpt_on_request(tmp_path, capsys):
    assert ie.main(write_inputs(tmp_path) + ["--allow-pipe", "--only", "3"]) == 0
    printed = capsys.readouterr().out
    assert "Zitat 3 von 3" in printed and "(qubit,[- -]angle)" in printed
    assert "H1, im Quellblock des Modells: nein" in printed
    assert SECRET not in printed


def test_main_rejects_a_number_out_of_range(tmp_path, capsys):
    assert ie.main(write_inputs(tmp_path) + ["--allow-pipe", "--only", "4"]) == 2


def test_main_tally_returns_one_on_problems(tmp_path, capsys):
    path = tmp_path / "table.md"
    assert ie.main(write_inputs(tmp_path) + ["--template", str(path)]) == 0
    assert ie.main(write_inputs(tmp_path) + ["--tally", str(path)]) == 1
    assert "PROBLEM" in capsys.readouterr().out
