"""Tests for src/analyze/gap_analysis.py (work package G, step 8, decision G6).

All data are invented. The tests pin G6: candidates and cap (section 2),
the blind sheet (section 4), the categories (section 5), the
counter-check that only lowers (section 6), and that nothing but counts
and identifiers leaves the script.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
for sub in ("analyze", "classify", "extract", "prepare"):
    if str(ROOT / "src" / sub) not in sys.path:
        sys.path.insert(0, str(ROOT / "src" / sub))
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from jsonschema import Draft202012Validator  # noqa: E402

import count_requirements as cr  # noqa: E402
import gap_analysis as ga  # noqa: E402
from check_classification import CheckError  # noqa: E402
from test_count_requirements import BLOCKS, PULLS, SCHEMA, records  # noqa: E402


def req(key, *, kind="functional_performance", security=False, text="Qrisp shall do x.",
        rationale="Because of y here.", excerpt="plain words here"):
    return {"key": key, "pull": int(key[3:7]),
            "req": {"id": key, "type": kind, "security_relevant": security, "text": text,
                    "rationale": rationale,
                    "evidence": [{"location": "body", "locator": None, "excerpt": excerpt,
                                  "supports": ["system_name", "system_response"]}]},
            "found": [True], "strength": "direct"}


# --- grid and keywords -------------------------------------------------


def test_grid_has_the_27_relevant_entries():
    assert len(ga.GRID) == 27
    assert not set(ga.NOT_RELEVANT) & set(ga.GRID)
    assert set(ga.KEYWORDS_BY_ENTRY) == set(ga.GRID) - {"SR07", "SR08"}


def test_keyword_list_is_the_closed_list_of_g6():
    assert len(ga.KEYWORDS) == 129
    for word in ("signature", "signed", "hash", "sign", "key", "log"):
        assert word not in ga.KEYWORDS


def test_keyword_hits_prose_and_excerpts_case_insensitive():
    row = req("QR-0001-01", text="Qrisp shall emit a DEPRECATION warning.",
              excerpt="run PyTest in CI")
    prose, excerpts = ga.keyword_hits(row["req"])
    assert "deprecat" in prose and "pytest" in excerpts and "pytest" not in prose


# --- candidates and cap (G6 section 2) -----------------------------------


def test_three_subsets():
    rows = [req("QR-0001-01", text="Qrisp shall publish a changelog."),
            req("QR-0002-01", excerpt="uses pytest fixtures"),
            req("QR-0003-01", kind="process"),
            req("QR-0004-01", security=True),
            req("QR-0005-01"),
            req("QR-0006-01")]
    cands = ga.build_candidates(rows, {"QR-0005-01"})
    assert cands["prose"] == {"QR-0001-01"}
    assert cands["excerpt_only"] == {"QR-0002-01"}
    assert cands["process"] == {"QR-0003-01"}
    assert cands["security"] == {"QR-0004-01", "QR-0005-01"}
    assert sorted(cands["order"]) == ["QR-0001-01", "QR-0002-01", "QR-0003-01",
                                      "QR-0004-01", "QR-0005-01"]
    assert cands["cap_stage"] == 0


def test_g5_key_outside_base_set_stops():
    with pytest.raises(CheckError):
        ga.build_candidates([req("QR-0001-01")], {"QR-9999-01"})


def many(prefix, count, **kw):
    return [req(f"QR-{prefix}{i:03d}-01", **kw) for i in range(count)]


def test_cap_stage_1_draws_50_excerpt_only():
    rows = (many("1", 100, kind="process") + many("2", 40, text="shall release x")
            + many("3", 120, excerpt="a pytest run"))
    cands = ga.build_candidates(rows, set())
    chosen = set(cands["order"])
    assert cands["cap_stage"] == 1 and len(chosen) == 190
    assert cands["process"] <= chosen and cands["prose"] <= chosen
    assert len(chosen & cands["excerpt_only"]) == 50


def test_cap_stage_2_keeps_protected_and_fills_to_200():
    rows = (many("1", 150, kind="process") + many("2", 5, security=True)
            + many("3", 120, text="shall release x") + many("4", 80, excerpt="a pytest run"))
    cands = ga.build_candidates(rows, set())
    chosen = set(cands["order"])
    assert cands["cap_stage"] == 2 and len(chosen) == ga.CAP
    assert cands["process"] | cands["security"] <= chosen


def test_cap_is_reproducible():
    rows = many("1", 100, kind="process") + many("3", 160, excerpt="a pytest run")
    assert ga.build_candidates(rows, set())["order"] == \
        ga.build_candidates(rows, set())["order"]


def test_read_g5_security_takes_only_ja():
    text = "# header\n1 | QR-0001-01 | F | ja | 1 |  | \n2 | QR-0002-01 | F | nein |  |  | \n" \
           "3 | QR-0003-01 | P | unklar |  |  | \n"
    assert ga.read_g5_security(text) == {"QR-0001-01"}


# --- sheet and answers (G6 section 4) ------------------------------------


def test_sheet_is_blind():
    row = req("QR-0001-01", kind="process", security=True)
    row["req"].update({"evidence_strength": "direct", "source_form": "prescriptive",
                       "uncertainties": "MODEL-REMARK"})
    sheet = ga.render_sheet(["QR-0001-01"], {"QR-0001-01": row})
    for word in ("process", "prescriptive", "evidence_strength", "security_relevant",
                 "MODEL-REMARK", "insufficient", "found", "pytest"):
        assert word not in sheet.lower()
    assert "Qrisp shall do x." in sheet and "SR17" in sheet


@pytest.mark.parametrize("field, expected", [
    ("keine", {}),
    ("SR17:ja", {"SR17": "ja"}),
    ("sr17 : JA, SR19:teilweise, SR10:unklar",
     {"SR17": "ja", "SR19": "teilweise", "SR10": "unklar"}),
])
def test_parse_entries_valid(field, expected):
    assert ga.parse_entries(field) == (expected, None)


@pytest.mark.parametrize("field", ["", "SR07:ja", "SR30:ja", "SR17:vielleicht", "SR17",
                                   "SR17:ja, SR17:teilweise"])
def test_parse_entries_invalid(field):
    parsed, problem = ga.parse_entries(field)
    assert parsed is None and problem


def test_parse_answers_needs_every_line():
    order = ["QR-0001-01", "QR-0002-01"]
    answers, problems = ga.parse_answers("1 | QR-0001-01 | SR17:ja | \n", order)
    assert answers == {"QR-0001-01": {"SR17": "ja"}} and problems
    _, problems = ga.parse_answers("1 | QR-0002-01 | keine | \n2 | QR-0001-01 | keine | \n",
                                   order)
    assert problems


# --- categories (G6 section 5) -------------------------------------------


@pytest.mark.parametrize("answer, strength, category", [
    ("ja", "direct", 1), ("ja", "indirect", 2), ("ja", "insufficient", 3),
    ("teilweise", "direct", 2), ("teilweise", "indirect", 2),
    ("teilweise", "insufficient", 3), ("unklar", "direct", 3),
])
def test_contribution(answer, strength, category):
    assert ga.contribution(answer, strength) == category


def test_category_is_best_match_and_3_without_match():
    matches = ga.matches_by_entry(
        {"A": {"SR17": "ja"}, "B": {"SR17": "teilweise", "SR19": "ja"}, "C": {"SR19": "unklar"}},
        {"A": "indirect", "B": "direct", "C": "direct"})
    assessed = ga.assess_entries(matches, {})
    assert assessed["SR17"]["category"] == 2
    assert assessed["SR19"]["category"] == 1
    assert assessed["SR01"]["category"] == 3 and assessed["SR01"]["pending"] == []


# --- counter-check (G6 section 6) ----------------------------------------


@pytest.mark.parametrize("strength, check, expected", [
    ("direct", None, "direct"),
    ("direct", {"carries": "nein", "form": ""}, "insufficient"),
    ("indirect", {"carries": "nein", "form": ""}, "insufficient"),
    ("direct", {"carries": "ja", "form": "berichtend"}, "indirect"),
    ("indirect", {"carries": "ja", "form": "fordernd"}, "indirect"),
    ("insufficient", {"carries": "ja", "form": "fordernd"}, "insufficient"),
])
def test_counter_check_only_lowers(strength, check, expected):
    assert ga.lowered(strength, check) == expected


def test_pending_order_and_limit_of_three():
    answers = {k: {"SR17": "ja"} for k in ("QR-0005-01", "QR-0002-01", "QR-0009-01",
                                           "QR-0001-01")}
    answers["QR-0003-01"] = {"SR17": "teilweise"}
    strengths = {"QR-0005-01": "direct", "QR-0002-01": "direct", "QR-0009-01": "direct",
                 "QR-0001-01": "indirect", "QR-0003-01": "direct"}
    assessed = ga.assess_entries(ga.matches_by_entry(answers, strengths), {})
    assert assessed["SR17"]["pending"] == ["QR-0002-01", "QR-0005-01", "QR-0009-01"]


def test_limit_is_three_per_round():
    answers = {f"A{i}": {"SR17": "ja"} for i in range(1, 6)}
    assessed = ga.assess_entries(ga.matches_by_entry(answers, {k: "direct" for k in answers}),
                                 {})
    assert assessed["SR17"]["pending"] == ["A1", "A2", "A3"]


def test_ja_before_teilweise_within_category_2():
    answers = {"A1": {"SR17": "teilweise"}, "B1": {"SR17": "ja"}}
    assessed = ga.assess_entries(
        ga.matches_by_entry(answers, {"A1": "direct", "B1": "indirect"}), {})
    assert assessed["SR17"]["category"] == 2
    assert assessed["SR17"]["pending"] == ["B1", "A1"]


def test_failed_checks_lead_to_next_three_and_category_falls():
    answers = {k: {"SR17": "ja"} for k in ("A1", "A2", "A3", "A4")}
    answers["B1"] = {"SR17": "teilweise"}
    strengths = {"A1": "direct", "A2": "direct", "A3": "direct", "A4": "direct",
                 "B1": "indirect"}
    matches = ga.matches_by_entry(answers, strengths)
    no = {"carries": "nein", "form": ""}
    round_1 = {k: no for k in ("A1", "A2", "A3")}
    assessed = ga.assess_entries(matches, round_1)
    assert assessed["SR17"]["category"] == 1 and assessed["SR17"]["pending"] == ["A4"]
    reported = {"carries": "ja", "form": "berichtend"}
    assessed = ga.assess_entries(matches, {**round_1, "A4": reported})
    assert assessed["SR17"]["category"] == 2
    assert assessed["SR17"]["verified"] == ["A4"] and assessed["SR17"]["pending"] == []
    assessed = ga.assess_entries(matches, {**round_1, "A4": no})
    assert assessed["SR17"]["category"] == 2 and assessed["SR17"]["pending"] == ["B1"]
    assessed = ga.assess_entries(matches, {**round_1, "A4": no, "B1": no})
    assert assessed["SR17"]["category"] == 3


def test_verified_match_settles_entry():
    matches = ga.matches_by_entry({"A1": {"SR22": "ja"}, "A2": {"SR22": "ja"}},
                                  {"A1": "direct", "A2": "direct"})
    assessed = ga.assess_entries(matches, {"A1": {"carries": "ja", "form": "fordernd"}})
    assert assessed["SR22"] == {**assessed["SR22"], "category": 1, "verified": ["A1"],
                                "pending": []}


@pytest.mark.parametrize("line, ok", [
    ("1 | A1 | ja | fordernd", True), ("1 | A1 | nein | ", True),
    ("1 | A1 | ja | ", False), ("1 | A1 | nein | berichtend", False),
    ("1 | A1 | vielleicht | fordernd", False), ("1 | A2 | ja | fordernd", False),
])
def test_parse_counter(line, ok):
    _, problems = ga.parse_counter(line + "\n", ["A1"])
    assert (not problems) is ok


def test_counter_sheet_shows_only_found_excerpts():
    row = req("QR-0001-01", excerpt="FOUND-EXCERPT")
    row["req"]["evidence"].append({"location": "title", "locator": None,
                                   "excerpt": "MISSING-EXCERPT", "supports": ["trigger"]})
    row["found"] = [True, False]
    sheet, answers = ga.render_counter(["QR-0001-01"], {"QR-0001-01": row}, 1)
    assert "FOUND-EXCERPT" in sheet and "MISSING-EXCERPT" not in sheet
    assert "Because of y" not in sheet and "1 | QR-0001-01 |" in answers


# --- tally (G6 section 8) ------------------------------------------------


def test_tally_categories_and_details():
    answers = {"A1": {"SR17": "ja"}, "A2": {"SR01": "teilweise"}, "A3": {"SR02": "ja"},
               "A4": {"SR03": "unklar"}, "A5": {}}
    strengths = {"A1": "direct", "A2": "indirect", "A3": "insufficient", "A4": "direct",
                 "A5": "direct"}
    matches = ga.matches_by_entry(answers, strengths)
    checks = {"A1": {"carries": "ja", "form": "fordernd"},
              "A2": {"carries": "ja", "form": "berichtend"}}
    counts = ga.tally(ga.assess_entries(matches, checks), matches, checks, {"A5", "A1"},
                      answers)
    entries = counts["entries"]
    assert entries["SR17"]["category"] == 1 and entries["SR17"]["deciding"] == ["A1"]
    assert entries["SR01"]["category"] == 2
    assert entries["SR02"]["category_3_detail"] == "only_insufficient"
    assert entries["SR03"]["category_3_detail"] == "no_match" and entries["SR03"]["unklar"] == 1
    assert entries["SR07"] == {"category": 4} and entries["SR08"] == {"category": 4}
    assert counts["categories"]["product_SR01_SR09"] == {"1": 0, "2": 1, "3": 6, "4": 2}
    assert counts["categories"]["process_SR10_SR29"] == {"1": 1, "2": 0, "3": 19, "4": 0}
    assert counts["explorative"]["g5_security_ja_without_grid_entry"] == 1


def test_tally_counts_lowered_matches():
    answers = {"A1": {"SR17": "ja"}}
    matches = ga.matches_by_entry(answers, {"A1": "direct"})
    checks = {"A1": {"carries": "ja", "form": "berichtend"}}
    entry = ga.tally(ga.assess_entries(matches, checks), matches, checks, set(),
                     answers)["entries"]["SR17"]
    assert entry["lowered_by_counter_check"] == 1
    assert entry["matches_after_counter_check"]["ja_indirect"] == 1
    assert entry["category"] == 2


# --- agreement with count_requirements.py (G1) ---------------------------


def test_strengths_agree_with_count_requirements():
    """Same base set and same FF4 strength as G1, whatever the check rules are."""
    validator = Draft202012Validator(SCHEMA)
    rows = ga.requirement_rows(records(), validator, PULLS, BLOCKS, None, set())
    summary = cr.count_run(records(), validator, PULLS, BLOCKS)
    assert len(rows) == summary["requirements"]["total"]
    counted = {}
    for row in rows:
        counted[row["strength"]] = counted.get(row["strength"], 0) + 1
    assert counted == summary["requirements"]["ff4"]["strength_from_found_evidence"]


# --- command line --------------------------------------------------------


def fake_rows():
    rows = [req("QR-0101-01", kind="process", text="Qrisp shall run MARKER-ONE in CI."),
            req("QR-0102-01", text="Qrisp shall emit a deprecation MARKER-TWO."),
            req("QR-0103-01", security=True, rationale="MARKER-THREE rationale text"),
            req("QR-0104-01", text="Unrelated MARKER-FOUR sentence.")]
    rows[1]["strength"] = "indirect"
    return rows


@pytest.fixture
def run(tmp_path, monkeypatch):
    monkeypatch.setattr(ga, "load_rows", lambda arguments: fake_rows())
    files = {}
    for name in ("input", "dataset", "model_input", "schema"):
        files[name] = tmp_path / f"{name}.txt"
        files[name].write_text(name, encoding="utf-8")
    g5_answers = tmp_path / "g5_answers.txt"
    g5_answers.write_text("1 | QR-0103-01 | F | ja | 1 |  | \n", encoding="utf-8")
    g5_result = tmp_path / "g5_result.json"
    g5_result.write_text(json.dumps({"files": {"answers": ga.sha256_of(g5_answers)}}),
                         encoding="utf-8")
    out = tmp_path / "work"
    base = ["--input", str(files["input"]), "--dataset", str(files["dataset"]),
            "--model-input", str(files["model_input"]), "--schema", str(files["schema"]),
            "--g5-answers", str(g5_answers), "--g5-result", str(g5_result),
            "--out-dir", str(out)]

    def call(command, *extra):
        return ga.main([command, *base, *extra])
    return call, out, tmp_path, g5_answers


def fill(path, mapping):
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            lines.append(line)
            continue
        number, key = (f.strip() for f in line.split("|")[:2])
        lines.append(f"{number} | {key} | {mapping[key]} | ")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_full_run_writes_counts_and_no_content(run, capsys):
    call, out, tmp_path, _ = run
    assert call("sheet") == 0
    manifest = json.loads((out / "sheet_manifest.json").read_text(encoding="utf-8"))
    assert sorted(manifest["order"]) == ["QR-0101-01", "QR-0102-01", "QR-0103-01"]
    fill(out / "answers.txt", {"QR-0101-01": "SR17:ja", "QR-0102-01": "SR28:ja",
                               "QR-0103-01": "keine"})
    assert call("compare") == 0
    fill(out / "counter_1.txt", {"QR-0101-01": "ja | fordernd", "QR-0102-01": "ja | berichtend"})
    assert call("result", "--output", str(tmp_path / "r.json")) == 2  # round still open
    assert call("next") == 0
    output = tmp_path / "result.json"
    assert call("result", "--output", str(output)) == 0
    written = output.read_text(encoding="utf-8")
    printed = capsys.readouterr().out
    entries = json.loads(written)["counts"]["entries"]
    assert entries["SR17"]["category"] == 1 and entries["SR28"]["category"] == 2
    assert json.loads(written)["counts"]["explorative"]["g5_security_ja_without_grid_entry"] == 1
    for text in ("MARKER-ONE", "MARKER-TWO", "MARKER-THREE", "MARKER-FOUR", "shall"):
        assert text not in written and text not in printed


def test_changed_answers_after_compare_stop(run):
    call, out, tmp_path, _ = run
    call("sheet")
    fill(out / "answers.txt", {"QR-0101-01": "SR17:ja", "QR-0102-01": "keine",
                               "QR-0103-01": "keine"})
    call("compare")
    fill(out / "answers.txt", {"QR-0101-01": "SR17:teilweise", "QR-0102-01": "keine",
                               "QR-0103-01": "keine"})
    assert call("next") == 2
    assert call("result", "--output", str(tmp_path / "r.json")) == 2


def test_changed_answers_without_counter_round_stop_result(run):
    call, out, tmp_path, _ = run
    call("sheet")
    fill(out / "answers.txt", {k: "keine" for k in ("QR-0101-01", "QR-0102-01", "QR-0103-01")})
    assert call("compare") == 0
    # unklar changes no category and opens no check: only the lock can stop it
    fill(out / "answers.txt", {"QR-0101-01": "SR17:unklar", "QR-0102-01": "keine",
                               "QR-0103-01": "keine"})
    assert call("result", "--output", str(tmp_path / "r.json")) == 2
    assert not (tmp_path / "r.json").exists()


def test_changed_counter_round_after_lock_stops(run):
    call, out, tmp_path, _ = run
    call("sheet")
    fill(out / "answers.txt", {"QR-0101-01": "SR17:ja", "QR-0102-01": "keine",
                               "QR-0103-01": "keine"})
    call("compare")
    fill(out / "counter_1.txt", {"QR-0101-01": "ja | fordernd"})
    call("next")
    fill(out / "counter_1.txt", {"QR-0101-01": "nein | "})
    assert call("result", "--output", str(tmp_path / "r.json")) == 2


def test_incomplete_answers_write_nothing(run):
    call, out, _, _ = run
    call("sheet")
    assert call("compare") == 1
    assert not (out / "lock.json").exists()


def test_g5_answers_checked_by_checksum(run):
    call, out, _, g5_answers = run
    g5_answers.write_text("1 | QR-0101-01 | F | ja | 1 |  | \n", encoding="utf-8")
    assert call("sheet") == 2 and not (out / "sheet.md").exists()


def test_sheet_refuses_to_overwrite(run):
    call, out, _, _ = run
    assert call("sheet") == 0
    assert call("sheet") == 2
