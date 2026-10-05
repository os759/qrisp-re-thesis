"""Tests for src/classify/check_classification.py (work package G, steps 6 and 7).

All data are invented. The tests pin the rules of G4 and G5 in
docs/entscheidungen.md: the three sets, the keyword list and the cap,
the blind sheet, the answer and follow-up checks, the counts, the
Dependabot review, and that nothing but numbers and identifiers is
printed.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src" / "classify") not in sys.path:
    sys.path.insert(0, str(ROOT / "src" / "classify"))

from jsonschema import Draft202012Validator  # noqa: E402

import check_classification as cc  # noqa: E402

SCHEMA_PATH = ROOT / "config" / "requirement_schema_v2.json"
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
SECRET_WORDS = ("Invented", "invented", "Zebra", "zebra-excerpt", "PRIVATE-TITLE",
                "PRIVATE-BODY")


def item(excerpt="Zebra excerpt text here", location="body"):
    return {"location": location, "locator": None, "html_url": None,
            "excerpt": excerpt, "supports": ["system_name", "system_response"]}


def req(pull, index, *, kind="interface", security=False, text=None,
        rationale="Invented rationale for the test.", excerpt="Zebra excerpt text here"):
    return {"id": f"QR-{pull:04d}-{index:02d}",
            "text": text or "The Zebra module shall return an invented value.",
            "ears_pattern": "ubiquitous", "system_name": "Zebra", "type": kind,
            "security_relevant": security, "rationale": rationale,
            "evidence_strength": "indirect", "modality_set_by_convention": True,
            "evidence": [item(excerpt)], "source_form": "descriptive",
            "uncertainties": "Model doubt: chose interface over functional."}


def record(pull, requirements, **extra):
    return {"schema_version": 2, "pull_number": pull,
            "processing_status": "requirements_found", "status_reason": None,
            "requirements": requirements, **extra}


def records():
    return [
        record(10, [req(10, 1, security=True, kind="process"),            # marked
                    req(10, 2, text="The Zebra parser shall reject UNTRUSTED input."),  # prose hit
                    req(10, 3, excerpt="calls eval( on the invented string")]),  # excerpt hit
        record(20, [req(20, 1, kind="functional_performance"),            # sample only
                    req(20, 2, kind="quality_non_functional",
                        rationale="Invented: avoids a Leak of data.")]),  # sample and hit
        record(30, [req(30, 1, security=True)]),                          # marked
        record(40, [req(40, 1, excerpt="shell=True in the invented call")],  # hit, schema error
               confidence=0.5),
        record(50, [req(50, 1, kind="human_factors")]),                   # nothing
    ]


SAMPLE_MD = """# Evaluation sample

## Provenance

- Excluded before the draw (--exclude), 2: 48, 75

| 48 | an invented table with numbers that is not the drawn table |

## Stratum sizes in the eligible population

| Stratum | Definition | Available | Drawn |
|---|---|---|---|
| S6 | no code changes | 2 | 1 (target 1) |

## Drawn pull requests

| PR | Stratum | Outcome | Description | Comments | Files dropped by budget | URL |
|---|---|---|---|---|---|---|
| 20 | S2 | merged | yes | 0 | 0 | https://github.com/eclipse-qrisp/Qrisp/pull/20 |
| 60 | S1 | merged | yes | 3 | 0 | https://github.com/eclipse-qrisp/Qrisp/pull/60 |

## Notes
"""


@pytest.fixture
def rows():
    return cc.load_requirements(records(), Draft202012Validator(SCHEMA))


@pytest.fixture
def sets(rows):
    return cc.build_sets(rows, [20, 60])


# --- base set and sets --------------------------------------------------


def test_base_set_skips_schema_errors(rows):
    assert [row["key"] for row in rows] == [
        "QR-0010-01", "QR-0010-02", "QR-0010-03", "QR-0020-01", "QR-0020-02",
        "QR-0030-01", "QR-0050-01"]


def test_duplicate_ids_get_a_suffix():
    rows = cc.load_requirements([record(10, [req(10, 1)]), record(11, [req(10, 1)])],
                                Draft202012Validator(SCHEMA))
    assert [row["key"] for row in rows] == ["QR-0010-01", "QR-0010-01~2"]
    assert [row["pull"] for row in rows] == [10, 11]


def test_read_sample_takes_only_the_drawn_table(tmp_path):
    path = tmp_path / "sample.md"
    path.write_text(SAMPLE_MD, encoding="utf-8")
    assert cc.read_sample(path) == [20, 60]


def test_read_sample_refuses_an_empty_table(tmp_path):
    path = tmp_path / "sample.md"
    path.write_text("# nothing\n## Drawn pull requests\n", encoding="utf-8")
    with pytest.raises(cc.CheckError):
        cc.read_sample(path)


def test_keyword_hits_case_and_place():
    prose, excerpts = cc.keyword_hits(req(1, 1, text="X shall stop an Attack.",
                                          excerpt="run(cmd, shell=True)"))
    assert prose == {"attack"} and excerpts == {"shell=true"}


def test_keyword_list_is_the_list_of_g5():
    assert len(cc.KEYWORDS) == 47 and len(set(cc.KEYWORDS)) == 47
    for word in ("hash", "sign", "signature", "key", "log"):
        assert word not in cc.KEYWORDS


def test_sets(sets):
    assert sets["marked"] == {"QR-0010-01", "QR-0030-01"}
    assert sets["prose_hits"] == {"QR-0010-02", "QR-0020-02"}
    assert sets["excerpt_only"] == {"QR-0010-03"}
    assert sets["checked"] == sets["hits"] and not sets["cap_applied"]
    assert sets["sample"] == {"QR-0020-01", "QR-0020-02"}
    assert sorted(sets["order"]) == sorted({"QR-0010-01", "QR-0030-01", "QR-0010-02",
                                            "QR-0020-02", "QR-0010-03", "QR-0020-01"})
    assert sets["per_keyword"] == {"eval(": 1, "leak": 1, "untrusted": 1}


def test_marked_requirements_are_not_search_hits():
    rows = cc.load_requirements([record(1, [req(1, 1, security=True, text="X shall avoid a leak.")])],
                                Draft202012Validator(SCHEMA))
    sets = cc.build_sets(rows, [])
    assert sets["marked"] == {"QR-0001-01"} and not sets["hits"]


def test_order_is_reproducible(rows):
    assert cc.build_sets(rows, [20])["order"] == cc.build_sets(rows, [20])["order"]


def cap_rows(prose, excerpt_only):
    reqs = [req(1, i, text="X shall stop an attack.") for i in range(1, prose + 1)]
    reqs += [req(2, i, excerpt="an invented token here") for i in range(1, excerpt_only + 1)]
    return [{"key": r["id"], "pull": int(r["id"][3:7]), "req": r} for r in reqs]


def test_no_cap_at_exactly_150():
    sets = cc.build_sets(cap_rows(100, 50), [])
    assert not sets["cap_applied"] and len(sets["checked"]) == 150


def test_cap_above_150_keeps_prose_and_samples_50():
    sets = cc.build_sets(cap_rows(100, 80), [])
    assert sets["cap_applied"]
    assert sets["prose_hits"] <= sets["checked"]
    assert len(sets["checked"] - sets["prose_hits"]) == 50
    again = cc.build_sets(cap_rows(100, 80), [])
    assert again["checked"] == sets["checked"]


def test_cap_with_fewer_than_50_excerpt_only_takes_all():
    sets = cc.build_sets(cap_rows(160, 10), [])
    assert sets["cap_applied"] and len(sets["checked"]) == 170


# --- sheet --------------------------------------------------------------


def test_sheet_is_blind(rows, sets):
    by_key = {row["key"]: row for row in rows}
    sheet = cc.render_sheet(sets, by_key)
    for word in ("interface", "process", "functional_performance", "security_relevant",
                 "Model doubt", "marked", "sample", "indirect", "true", "false"):
        assert word not in sheet
    assert sheet.count("\n## ") == len(sets["order"])
    assert "https://github.com/eclipse-qrisp/Qrisp/pull/10" in sheet


def test_fence_survives_backticks():
    assert cc.fence("no ticks") == "```"
    assert cc.fence("has ``` inside") == "````"


# --- answers ------------------------------------------------------------


def answer_text(order, lines):
    return cc.ANSWER_HEADER + "".join(
        f"{n} | {key} | {lines.get(key, ('F', 'nein', '', '', ''))[0]} | "
        f"{lines.get(key, ('F', 'nein', '', '', ''))[1]} | "
        f"{lines.get(key, ('F', 'nein', '', '', ''))[2]} | "
        f"{lines.get(key, ('F', 'nein', '', '', ''))[3]} | "
        f"{lines.get(key, ('F', 'nein', '', '', ''))[4]}\n"
        for n, key in enumerate(order, start=1))


def test_empty_answer_file_is_incomplete(sets):
    _answers, problems = cc.parse_answers(cc.render_answers(sets["order"]), sets["order"])
    assert len(problems) >= len(sets["order"])


@pytest.mark.parametrize("line, message", [
    (("X", "nein", "", "", ""), "type must be"),
    (("F", "maybe", "", "", ""), "security must be"),
    (("F", "ja", "", "", ""), "needs purpose"),
    (("F", "nein", "2", "", ""), "purpose only"),
    (("F", "ja", "4", "", ""), "needs purpose"),
    (("F", "nein", "", "GF8", ""), "rule must be"),
    (("F", "nein", "", "G1", ""), "rule must be"),
])
def test_answer_problems(sets, line, message):
    key = sets["order"][0]
    _answers, problems = cc.parse_answers(answer_text(sets["order"], {key: line}), sets["order"])
    assert any(message in problem for problem in problems)


def test_valid_answers_with_rules_and_note(sets):
    key = sets["order"][0]
    text = answer_text(sets["order"], {key: ("i", "JA", "1", "gf2, ty1", "a note")})
    answers, problems = cc.parse_answers(text, sets["order"])
    assert not problems
    assert answers[key] == {"type": "interface", "security": "ja", "purpose": "1",
                            "rules": "GF2,TY1"}


def test_wrong_order_and_duplicates_are_problems(sets):
    order = sets["order"]
    text = answer_text(order, {})
    body = [line for line in text.splitlines() if not line.startswith("#")]
    wrong_id = text.replace(f"1 | {order[0]} |", f"1 | {order[1]} |")
    assert any("do not match" in p for p in cc.parse_answers(wrong_id, order)[1])
    doubled = text + body[0] + "\n"
    assert any("twice" in p for p in cc.parse_answers(doubled, order)[1])


def test_unklar_is_never_a_disagreement(rows, sets):
    by_key = {row["key"]: row for row in rows}
    answers = {key: {"type": "interface", "security": "unklar", "purpose": "", "rules": ""}
               for key in sets["order"]}
    assert cc.security_disagreements(sets["order"], answers, by_key) == []


def full_answers(sets, overrides):
    base = {key: ("I", "nein", "", "", "") for key in sets["order"]}
    base.update(overrides)
    return answer_text(sets["order"], base)


OVERRIDES = {
    "QR-0010-01": ("P", "ja", "1", "", ""),      # marked, confirmed
    "QR-0030-01": ("I", "nein", "", "GF4", ""),  # marked, rejected
    "QR-0010-02": ("I", "ja", "2", "GF1", ""),   # hit, missed
    "QR-0020-02": ("U", "unklar", "", "", ""),   # sample and hit, unclear, same kind
    "QR-0020-01": ("I", "ja", "1", "TY1", ""),   # sample, missed, type differs (model F)
}


def test_disagreements(rows, sets):
    by_key = {row["key"]: row for row in rows}
    answers, problems = cc.parse_answers(full_answers(sets, OVERRIDES), sets["order"])
    assert not problems
    found = {key: (model, author) for _n, key, model, author
             in cc.security_disagreements(sets["order"], answers, by_key)}
    assert found == {"QR-0030-01": ("ja", "nein"), "QR-0010-02": ("nein", "ja"),
                     "QR-0020-01": ("nein", "ja")}


def test_follow_up_checks(rows, sets):
    by_key = {row["key"]: row for row in rows}
    answers, _ = cc.parse_answers(full_answers(sets, OVERRIDES), sets["order"])
    disagreements = cc.security_disagreements(sets["order"], answers, by_key)
    empty = cc.render_follow_up(disagreements)
    assert cc.parse_follow_up(empty, disagreements)[1]
    filled = empty.replace(" | \n", " | 3\n")
    values, problems = cc.parse_follow_up(filled, disagreements)
    assert not problems and set(values.values()) == {"3"}
    assert any("must be" in p for p in
               cc.parse_follow_up(empty.replace(" | \n", " | 5\n"), disagreements)[1])
    shortened = "".join(filled.splitlines(keepends=True)[:-1])
    assert any("without a line" in p for p in
               cc.parse_follow_up(shortened, disagreements)[1])


def test_tally(rows, sets):
    by_key = {row["key"]: row for row in rows}
    answers, _ = cc.parse_answers(full_answers(sets, OVERRIDES), sets["order"])
    follow_up = {"QR-0030-01": "keine", "QR-0010-02": "4", "QR-0020-01": "keine"}
    counts = cc.tally(sets["order"], answers, follow_up, sets, by_key)
    marked = counts["security"]["marked"]
    assert (marked["n"], marked["confirmed"], marked["rejected"],
            marked["rejected_misjudged"], marked["rejected_by_definition"]) == (2, 1, 1, 1, 0)
    hits = counts["security"]["search_hits_checked"]
    assert (hits["n"], hits["missed"], hits["missed_by_definition"],
            hits["author_unklar"]) == (3, 1, 1, 1)
    sample = counts["security"]["sample"]
    assert (sample["n"], sample["missed"], sample["missed_misjudged"],
            sample["author_unklar"]) == (2, 1, 1, 1)
    types = counts["type_sample"]
    assert (types["n"], types["type_agree"], types["kind_agree"]) == (2, 0, 1)
    matrix = types["confusion_model_rows_author_columns"]
    assert matrix["functional_performance"]["interface"] == 1
    assert matrix["quality_non_functional"]["usability_quality_in_use"] == 1
    assert counts["rules_used_all_rows"] == {"GF1": 1, "GF4": 1, "TY1": 1}


def test_kind_agree_counts_non_functional_together():
    assert cc.KIND_OF_TYPE["usability_quality_in_use"] == cc.KIND_OF_TYPE["human_factors"] \
        == cc.KIND_OF_TYPE["quality_non_functional"] == "non_functional"
    assert len({cc.KIND_OF_TYPE[t] for t in cc.TYPE_CODES.values()}) == 4


# --- command line, end to end -------------------------------------------


def write_inputs(tmp_path):
    extraction = tmp_path / "extraction.jsonl"
    extraction.write_text("".join(json.dumps(r) + "\n" for r in records()), encoding="utf-8")
    sample = tmp_path / "sample.md"
    sample.write_text(SAMPLE_MD, encoding="utf-8")
    return ["--input", str(extraction), "--sample", str(sample), "--schema", str(SCHEMA_PATH)]


def test_full_run_prints_no_content(tmp_path, capsys):
    common = write_inputs(tmp_path)
    out_dir = tmp_path / "responses"
    assert cc.main(["search", *common]) == 0
    assert cc.main(["sheet", *common, "--out-dir", str(out_dir)]) == 0
    order = json.loads((out_dir / "sheet_manifest.json").read_text())["order"]
    sets = {"order": order}
    assert cc.main(["compare", *common, "--out-dir", str(out_dir)]) == 1  # empty answers
    assert not (out_dir / "answers_lock.json").exists()
    (out_dir / "answers.txt").write_text(full_answers(sets, OVERRIDES), encoding="utf-8")
    assert cc.main(["compare", *common, "--out-dir", str(out_dir)]) == 0
    assert cc.main(["compare", *common, "--out-dir", str(out_dir)]) == 2  # no second run
    output = tmp_path / "result.json"
    assert cc.main(["result", *common, "--out-dir", str(out_dir),
                    "--output", str(output)]) == 2  # follow-up empty
    follow = out_dir / "follow_up.txt"
    follow.write_text(follow.read_text().replace(" | \n", " | keine\n"), encoding="utf-8")
    assert cc.main(["result", *common, "--out-dir", str(out_dir), "--output", str(output)]) == 0
    result = json.loads(output.read_text())
    assert result["sets"]["sheet_rows"] == 6
    assert result["counts"]["security"]["marked"]["rejected_misjudged"] == 1
    assert result["files"]["answers"] == cc.sha256_of(out_dir / "answers.txt")
    assert cc.main(["result", *common, "--out-dir", str(out_dir), "--output", str(output)]) == 2
    printed = capsys.readouterr().out
    written = output.read_text()
    for word in SECRET_WORDS + ("UNTRUSTED", "Leak", "shell=True"):
        assert word not in printed and word not in written


def test_result_refuses_changed_answers(tmp_path):
    common = write_inputs(tmp_path)
    out_dir = tmp_path / "responses"
    cc.main(["sheet", *common, "--out-dir", str(out_dir)])
    order = json.loads((out_dir / "sheet_manifest.json").read_text())["order"]
    answers = out_dir / "answers.txt"
    answers.write_text(full_answers({"order": order}, OVERRIDES), encoding="utf-8")
    cc.main(["compare", *common, "--out-dir", str(out_dir)])
    follow = out_dir / "follow_up.txt"
    follow.write_text(follow.read_text().replace(" | \n", " | keine\n"), encoding="utf-8")
    changed = answers.read_text().replace("| QR-0010-03 | I |", "| QR-0010-03 | F |")
    assert changed != answers.read_text()
    answers.write_text(changed, encoding="utf-8")
    assert cc.main(["result", *common, "--out-dir", str(out_dir),
                    "--output", str(tmp_path / "r.json")]) == 2
    assert not (tmp_path / "r.json").exists()


def test_sheet_refuses_to_overwrite_and_inputs_must_match(tmp_path):
    common = write_inputs(tmp_path)
    out_dir = tmp_path / "responses"
    assert cc.main(["sheet", *common, "--out-dir", str(out_dir)]) == 0
    assert cc.main(["sheet", *common, "--out-dir", str(out_dir)]) == 2
    (tmp_path / "sample.md").write_text(SAMPLE_MD + "An extra note.\n", encoding="utf-8")
    assert cc.main(["compare", *common, "--out-dir", str(out_dir)]) == 2


# --- Dependabot ----------------------------------------------------------


def pull(number, author, outcome, title="Bump PRIVATE-TITLE", body="PRIVATE-BODY",
         comments=()):
    return {"number": number, "author": author, "outcome": outcome, "title": title,
            "body": body, "issue_comments": [{"body": c} for c in comments],
            "review_comments": []}


DATASET = [
    pull(1, "dependabot[bot]", "merged", body="Fixes CVE-2099-0001 PRIVATE-BODY"),
    pull(2, "dependabot[bot]", "closed_unmerged", body="PRIVATE-BODY Security release"),
    pull(3, "dependabot[bot]", "closed_unmerged", comments=["see GHSA-xxxx"]),
    pull(4, "dependabot[bot]", "merged"),
    pull(5, "dependabot[bot]", "open", body="CVE-2099-0002"),   # open: excluded
    pull(6, "person", "merged", body="security"),                # not Dependabot
    pull(7, {"login": "dependabot[bot]"}, "merged", body="vulnerability noted"),
]


def test_dependabot_selection_and_classes():
    records = cc.dependabot_records(DATASET)
    assert [r["number"] for r in records] == [1, 2, 3, 4, 7]
    assert cc.dependabot_classes(records) == {1: "id", 2: "word", 3: "id", 4: "none",
                                              7: "word"}


def test_dependabot_counts_with_answers():
    records = cc.dependabot_records(DATASET)
    classes = cc.dependabot_classes(records)
    counts = cc.dependabot_counts(records, classes, {2: "nein", 7: "ja"})
    assert counts["total"] == {"records": 5, "class_id": 2, "class_word": 2, "class_none": 1,
                               "word_answer_ja": 1, "word_answer_nein": 1,
                               "word_answer_unklar": 0, "hints": 3}
    assert counts["merged"]["hints"] == 2 and counts["closed_unmerged"]["hints"] == 1


def test_dependabot_answer_problems():
    _a, problems = cc.parse_dependabot_answers("2 | vielleicht\n9 | ja\n", {2, 7})
    assert any("must be" in p for p in problems)
    assert any("not a pull request" in p for p in problems)
    assert any("without an answer" in p for p in problems)


def test_dependabot_end_to_end_prints_no_content(tmp_path, capsys):
    dataset = tmp_path / "dataset.jsonl"
    dataset.write_text("".join(json.dumps(r) + "\n" for r in DATASET), encoding="utf-8")
    out_dir = tmp_path / "responses"
    assert cc.main(["dependabot-sheet", "--dataset", str(dataset),
                    "--out-dir", str(out_dir)]) == 0
    sheet = (out_dir / "dependabot_sheet.md").read_text()
    assert "## PR 2 " in sheet and "## PR 7 " in sheet and "## PR 1 " not in sheet
    (out_dir / "dependabot_answers.txt").write_text("2 | nein\n7 | ja\n", encoding="utf-8")
    output = tmp_path / "dep.json"
    assert cc.main(["dependabot-result", "--dataset", str(dataset), "--out-dir", str(out_dir),
                    "--output", str(output)]) == 0
    assert json.loads(output.read_text())["counts"]["total"]["hints"] == 3
    printed = capsys.readouterr().out
    for word in ("PRIVATE-TITLE", "PRIVATE-BODY", "Security release", "vulnerability noted"):
        assert word not in printed and word not in output.read_text()


def test_constants_of_g5():
    assert (cc.SEED, cc.CAP, cc.EXCERPT_ONLY_SAMPLE) == (20261005, 150, 50)
    assert cc.TYPE_CODES == {"F": "functional_performance", "I": "interface", "P": "process",
                             "Q": "quality_non_functional", "U": "usability_quality_in_use",
                             "H": "human_factors"}
