"""Tests for src/analyze/evaluate_requirements.py (E2, criteria list v1).

All data are invented. The file sets its import path itself.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
for _sub in ("extract", "prepare", "classify", "analyze"):
    if str(ROOT / "src" / _sub) not in sys.path:
        sys.path.insert(0, str(ROOT / "src" / _sub))

import evaluate_requirements as ev  # noqa: E402

SCHEMA = ROOT / "config" / "requirement_schema_v2.json"


# --- invented data ------------------------------------------------------

def pull(number, title="", body="", issue_comments=(), review_comments=(), files=()):
    return {"number": number, "title": title, "body": body,
            "issue_comments": list(issue_comments), "review_comments": list(review_comments),
            "files": list(files)}


DATASET = [
    pull(10, title="Add widget export", body="The Exporter must write files in UTF-8 format.",
         issue_comments=[{"id": 501, "body": "Exporter should also handle empty input gracefully."}],
         review_comments=[{"id": 601, "body": "Please make the Exporter validate paths first.",
                           "diff_hunk": "@@ -1 +1 @@\n+x = 1"}],
         files=[{"filename": "src/export.py",
                 "patch": "@@ -1,2 +1,3 @@\n context line\n+def export_utf8(data):\n-old line"}]),
    pull(20, title="Fix parser crash", body="Parser crashes when the input is empty.",
         files=[{"filename": "src/parse.py",
                 "patch": "@@ -1 +1,2 @@\n+def parse(text):\n+    return []"}]),
    pull(30, title="Docs tutorials", body="Rework the docs page for tutorials."),
    pull(40, title="Invalid record pull", body="Something else entirely here."),
    pull(50, title="Outside the sample", body="The Backend must log every call."),
]

BLOCKS = [
    {"pull_number": 10, "source_block": "[FILE src/export.py status=modified +1 -1]\n@@ x"},
    {"pull_number": 20, "source_block": "[FILE src/parse.py status=modified +2 -0]\n@@ x"},
    {"pull_number": 30, "source_block": ""},
    {"pull_number": 40, "source_block": ""},
    {"pull_number": 50, "source_block": ""},
]


def evidence(location, excerpt, supports, locator=None):
    return {"location": location, "locator": locator, "excerpt": excerpt,
            "supports": list(supports)}


def requirement(rid, text, pattern, name, items, strength, source_form="descriptive"):
    return {"id": rid, "text": text, "ears_pattern": pattern, "system_name": name,
            "type": "functional_performance", "security_relevant": False,
            "rationale": "SECRET-RATIONALE-TEXT for testing.",
            "evidence_strength": strength, "modality_set_by_convention": True,
            "evidence": items, "source_form": source_form,
            "beneficiary": None, "component": None, "verification": "VERIFY-TEXT",
            "uncertainties": None, "missing_information": None}


def record(number, requirements):
    return {"schema_version": 2, "pull_number": number,
            "processing_status": "requirements_found", "status_reason": None,
            "requirements": requirements}


R10_1 = requirement("QR-0010-01", "The Exporter shall write files in UTF-8 format.",
                    "ubiquitous", "Exporter",
                    [evidence("body", "The Exporter must write files in UTF-8 format.",
                              ["system_name", "system_response"])],
                    "direct", "prescriptive")
R10_2 = requirement("QR-0010-02",
                    "When the input is empty, the Exporter shall handle it without an error.",
                    "event_driven", "Exporter",
                    [evidence("issue_comment", "Exporter should also handle empty input gracefully.",
                              ["system_name", "system_response"], "501")],
                    "insufficient")
R20_1 = requirement("QR-0020-01",
                    "If the input is empty, then the Parser shall return an empty result.",
                    "unwanted_behaviour", "Parser",
                    [evidence("body", "Parser crashes when the input is empty.",
                              ["system_name", "trigger"]),
                     evidence("diff", "def parse(text):", ["system_response"], "src/parse.py")],
                    "indirect")
R20_2 = requirement("QR-0020-02", "The Parser shall not crash on all inputs.",
                    "ubiquitous", "Parser",
                    [evidence("title", "Fix parser crash", ["system_name", "system_response"])],
                    "direct")  # the rules of E6 give indirect
R30_1 = requirement("QR-0030-01", "The Docs page shall list every tutorial.",
                    "ubiquitous", "Docs page",
                    [evidence("body", "Completely invented sentence not in source.",
                              ["system_name", "system_response"])],
                    "indirect")
R50_1 = requirement("QR-0050-01", "The Backend shall log each call.", "ubiquitous", "Backend",
                    [evidence("body", "The Backend must log every call.",
                              ["system_name", "system_response"])],
                    "direct", "prescriptive")

RECORDS = [record(10, [R10_1, R10_2]), record(20, [R20_1, R20_2]), record(30, [R30_1]),
           {**record(40, []), "schema_version": 1}, record(50, [R50_1])]

SAMPLE = """# Sample

## Drawn pull requests

| PR | Stratum | URL |
|---|---|---|
| 10 | S1 | x |
| 20 | S2 | x |
| 30 | S3 | x |
| 40 | S4 | x |

## Notes
"""

FUNDSTELLEN = """pr,part,locations,fundstelle
10,system_name,body,"Beschreibung: Exporter"
10,system_response,comment,"Kommentar: leere Eingabe"
20,system_response,title,"Titel: parser crash"
20,system_name,diff,"Diff: Parser"
30,system_name,body,"Beschreibung: Docs page"
40,system_name,title+body,"Titel: etwas"
"""


def write_jsonl(path, rows):
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


@pytest.fixture
def files(tmp_path):
    paths = {name: tmp_path / name for name in
             ("input.jsonl", "dataset.jsonl", "model_input.jsonl", "sample.md",
              "fundstellen.csv", "criteria.md")}
    write_jsonl(paths["input.jsonl"], RECORDS)
    write_jsonl(paths["dataset.jsonl"], DATASET)
    write_jsonl(paths["model_input.jsonl"], BLOCKS)
    paths["sample.md"].write_text(SAMPLE, encoding="utf-8")
    paths["fundstellen.csv"].write_text(FUNDSTELLEN, encoding="utf-8")
    paths["criteria.md"].write_text("criteria v1\n", encoding="utf-8")
    paths["out"] = tmp_path / "responses"
    paths["output"] = tmp_path / "experiments" / "evaluation.json"
    return paths


def argv(files, command):
    args = [command, "--input", str(files["input.jsonl"]), "--dataset",
            str(files["dataset.jsonl"]), "--model-input", str(files["model_input.jsonl"]),
            "--sample", str(files["sample.md"]), "--schema", str(SCHEMA),
            "--fundstellen", str(files["fundstellen.csv"]),
            "--criteria", str(files["criteria.md"]), "--out-dir", str(files["out"])]
    if command == "result":
        args += ["--output", str(files["output"])]
    return args


def state_of(files):
    return ev.State(ev.parse_arguments(argv(files, "sheet")))


GOOD = {"QR-0010-01": "2 | 2 | 2 | 2 | 2 | 2 | 2 | ",
        "QR-0010-02": "1 | 1 | 1 | 1 | 2 | 2 | 1 | ",
        "QR-0020-01": "2 | 2 | 2 | 2 | 2 | 2 | 2 | ",
        "QR-0020-02": "0 | 2 | 2 | 2 | 2 | 2 | 2 | ",
        "QR-0030-01": "2 | ? | 2 | 2 | 2 | 0 | 2 | Quantenwissen noetig"}
GOOD_PULLS = {10: "2 | 1 | ", 20: "0 | 2 | ", 30: "- | 2 | "}


def fill_answers(files, requirements=None, pulls=None):
    requirements = {**GOOD, **(requirements or {})}
    pulls = {**GOOD_PULLS, **(pulls or {})}
    path = files["out"] / "answers.txt"
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        fields = [f.strip() for f in line.split("|")]
        if line.startswith("R |"):
            lines.append(f"R | {fields[1]} | {fields[2]} | {requirements[fields[2]]}")
        elif line.startswith("P |"):
            lines.append(f"P | {fields[1]} | {pulls[int(fields[1])]}")
        else:
            lines.append(line)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def fill_n2(files, answers=("ja", "nein", "ja", "?", "nein", "nein")):
    path = files["out"] / "n2_answers.txt"
    lines = []
    index = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            lines.append(line)
            continue
        fields = [f.strip() for f in line.split("|")]
        lines.append(f"{fields[0]} | {fields[1]} | {fields[2]} | {answers[index]} | ")
        index += 1
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_all(files, capsys=None):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files)
    assert ev.main(argv(files, "compare")) == 0
    assert ev.main(argv(files, "n2-sheet")) == 0
    fill_n2(files)
    assert ev.main(argv(files, "result")) == 0
    return json.loads(files["output"].read_text(encoding="utf-8"))


# --- B10 word list and search rules -------------------------------------

def test_b10_space_matches_hyphen():
    assert ev.b10_hits("The API shall be user-friendly.") == [("K2", "user friendly")]


@pytest.mark.parametrize("text", ["its value", "everything works", "everyone agrees",
                                  "the item2 list", "a mostly fine idea"])
def test_b10_no_inflected_or_derived_forms(text):
    assert ev.b10_hits(text) == []


def test_b10_longest_expression_wins():
    assert ev.b10_hits("It shall almost always work.") == [("K4", "almost always"),
                                                           ("K3", "it")]


def test_b10_and_or_before_or():
    assert ev.b10_hits("x and/or y") == [("K4", "and/or")]


def test_b10_hyphen_is_a_word_boundary():
    assert ev.b10_hits("the most-used gate") == [("K1", "most")]


def test_b10_case_and_repeats():
    hits = ev.b10_hits("ALL gates and all qubits")
    assert hits == [("K8", "all"), ("K8", "all")]


def test_b10_apostrophe_and_underscore_are_boundaries():
    assert ev.b10_hits("it's") == [("K3", "it")]
    assert ev.b10_hits("all_items") == [("K8", "all")]


def test_b10_word_list_is_exactly_the_29148_examples():
    assert len(ev.WORD_LIST) == 25
    assert ev.CLASSES == ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8")
    assert {expr for _, expr in ev.WORD_LIST} >= {"but not limited to", "as applicable",
                                                  "higher quality", "cost effective"}


# --- B8 format conformity -----------------------------------------------

def req(text, pattern="ubiquitous", name="Qrisp"):
    return {"text": text, "ears_pattern": pattern, "system_name": name}


@pytest.mark.parametrize("text,pattern,expected", [
    ("The Qrisp shall do x.", "ubiquitous", True),
    ("When x, the Qrisp shall do y.", "ubiquitous", False),
    ("While x, Qrisp shall do y.", "state_driven", True),
    ("During x, Qrisp shall do y.", "state_driven", True),
    ("When x, Qrisp shall do y.", "state_driven", False),
    ("when x, Qrisp shall do y.", "event_driven", True),
    ("If x, Qrisp shall do y.", "event_driven", False),
    ("If x, then Qrisp shall do y.", "unwanted_behaviour", True),
    ("If x, Qrisp shall do y.", "unwanted_behaviour", False),
    ("If x, Qrisp shall do y then z.", "unwanted_behaviour", False),
    ("Where x, Qrisp shall do y.", "optional_feature", True),
    ("While x, when y, Qrisp shall do z.", "complex", True),
    ("Where x, if y, Qrisp shall do z.", "complex", True),
    ("While x, during y, Qrisp shall do z.", "complex", False),
    ("The Qrisp, while x and when y, shall do z.", "complex", False),
    ("When x, Qrisp shall do y while z.", "complex", False),
])
def test_b8_pattern(text, pattern, expected):
    assert ev.b8_pattern(req(text, pattern)) is expected


def test_b8_pattern_unknown_value_fails():
    assert ev.b8_pattern(req("The Qrisp shall do x.", "other")) is False


def test_b8_order():
    assert ev.b8_order(req("The QRISP compiler shall do x.", name="Qrisp")) is True
    assert ev.b8_order(req("The compiler shall do x for Qrisp.", name="Qrisp")) is False
    assert ev.b8_order(req("The Qrisp compiler does x.", name="Qrisp")) is False


def test_b8_shall():
    assert ev.b8_shall(req("Qrisp shall do x.")) is True
    assert ev.b8_shall(req("Qrisp Shall do x.")) is False
    assert ev.b8_shall(req("Qrisp shall do x and shall do y.")) is False
    assert ev.b8_shall(req("Marshall shall do x.")) is True


@pytest.mark.parametrize("text,expected", [
    ("Qrisp shall do x.", True), ("Qrisp shall do x as the mayor said.", True),
    ("Qrisp shall do x; users may skip it.", False), ("Qrisp shall do x. Will it?", False),
    ("Qrisp shall do what it MUST.", False), ("Qrisp shall do x and should y.", False),
])
def test_b8_no_other_modal(text, expected):
    assert ev.b8_no_other_modal(req(text)) is expected


# --- inputs, order, sheet -----------------------------------------------

def test_scope_and_order(files):
    state = state_of(files)
    assert len(state.rows) == 6
    assert sorted(state.keys_by_pull) == [10, 20, 30]
    assert [e for e in state.entries if e[0] == "R"][0][1] == 1
    numbers = [e[1] for e in state.entries if e[0] == "R"]
    assert numbers == list(range(1, 6))
    # each P block follows the requirements of its pull request
    for index, entry in enumerate(state.entries):
        if entry[0] == "P":
            before = [e for e in state.entries[:index] if e[0] == "R" and e[3] == entry[1]]
            assert len(before) == len(state.keys_by_pull[entry[1]])
    assert state.entries == state_of(files).entries
    assert ev.build_entries({1: ["a"], 2: ["b"], 3: ["c"], 4: ["d"]}) \
        == ev.build_entries({4: ["d"], 3: ["c"], 2: ["b"], 1: ["a"]})


def test_order_uses_the_seed():
    import random
    pulls = [1, 2, 3, 4, 5, 6, 7]
    expected = sorted(pulls)
    random.Random(20261008).shuffle(expected)
    entries = ev.build_entries({p: [f"k{p}"] for p in pulls})
    assert [e[1] for e in entries if e[0] == "P"] == expected


def test_requirements_sorted_within_pull(files):
    state = state_of(files)
    assert state.keys_by_pull[10] == ["QR-0010-01", "QR-0010-02"]


def test_duplicate_record_is_refused(files):
    write_jsonl(files["input.jsonl"], RECORDS + [record(10, [R10_1])])
    with pytest.raises(ev.EvaluationError):
        state_of(files)


def test_sheet_is_blind(files):
    assert ev.main(argv(files, "sheet")) == 0
    sheet = (files["out"] / "sheet.md").read_text(encoding="utf-8")
    assert "The Exporter must write files in UTF-8 format." in sheet
    assert "SECRET-RATIONALE-TEXT" not in sheet
    assert "VERIFY-TEXT" not in sheet
    for word in ("ears_pattern", "event_driven", "insufficient", "functional_performance",
                 "prescriptive", "system_response", "security"):
        assert word not in sheet
    assert sheet.count("## PR ") == 3
    assert "B11a ist vom Programm auf - gesetzt" in sheet


def test_answer_template_sets_dash_only_for_single(files):
    assert ev.main(argv(files, "sheet")) == 0
    lines = (files["out"] / "answers.txt").read_text(encoding="utf-8").splitlines()
    p_lines = {int(line.split("|")[1]): line for line in lines if line.startswith("P |")}
    assert p_lines[30].split("|")[2].strip() == "-"
    assert p_lines[10].split("|")[2].strip() == ""
    state = state_of(files)
    _, problems = ev.parse_answers("\n".join(lines), state)
    assert any("requirement" in p or "must be" in p for p in problems)


def test_sheet_refuses_overwrite(files):
    assert ev.main(argv(files, "sheet")) == 0
    assert ev.main(argv(files, "sheet")) == 2


# --- parsing the answers ------------------------------------------------

def parsed(files, requirements=None, pulls=None):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files, requirements, pulls)
    return ev.parse_answers((files["out"] / "answers.txt").read_text(encoding="utf-8"),
                            state_of(files))


def test_complete_answers_have_no_problems(files):
    answers, problems = parsed(files)
    assert problems == []
    assert answers["requirements"]["QR-0030-01"]["B2"] == "?"
    assert answers["pulls"][30]["B11a"] == "-"


@pytest.mark.parametrize("change", [
    {"requirements": {"QR-0010-01": "3 | 2 | 2 | 2 | 2 | 2 | 2 | "}},
    {"requirements": {"QR-0010-01": "- | 2 | 2 | 2 | 2 | 2 | 2 | "}},
    {"requirements": {"QR-0010-01": "2 | 2 | 2 | 2 | 2 | 2 | ? | "}},
    {"requirements": {"QR-0010-01": "2 | 2 | 2 | 2 | 2 | 2 | 2 | a | b"}},
    {"requirements": {"QR-0010-01": "2 | 2 | 2 | 2 | 2 | 2 | "}},
    {"pulls": {30: "2 | 2 | "}},
    {"pulls": {10: "- | 2 | "}},
    {"pulls": {10: "2 | - | "}},
    {"pulls": {10: "? | 2 | "}},
])
def test_invalid_answers_are_reported(files, change):
    _, problems = parsed(files, **change)
    assert problems


def test_wrong_number_duplicate_and_missing_lines(files):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files)
    path = files["out"] / "answers.txt"
    lines = path.read_text(encoding="utf-8").splitlines()
    first_r = next(i for i, line in enumerate(lines) if line.startswith("R |"))
    state = state_of(files)
    wrong = lines[first_r].replace("R | 1 |", "R | 2 |")
    _, problems = ev.parse_answers("\n".join(lines[:first_r] + [wrong] + lines[first_r + 1:]),
                                   state)
    assert any("do not match" in p for p in problems)
    _, problems = ev.parse_answers("\n".join(lines + [lines[first_r]]), state)
    assert any("twice" in p for p in problems)
    _, problems = ev.parse_answers("\n".join(lines[:first_r] + lines[first_r + 1:]), state)
    assert any("without an answer" in p for p in problems)
    p_line = next(line for line in lines if line.startswith("P |"))
    _, problems = ev.parse_answers("\n".join([l for l in lines if l != p_line]), state)
    assert any("pull requests without" in p for p in problems)
    _, problems = ev.parse_answers("\n".join(lines + ["X | 1"]), state)
    assert any("start with R or P" in p for p in problems)


# --- compare, lock, n2-sheet, result ------------------------------------

def test_compare_incomplete_writes_nothing(files):
    assert ev.main(argv(files, "sheet")) == 0
    assert ev.main(argv(files, "compare")) == 1
    assert not (files["out"] / "answers_lock.json").exists()


def test_compare_locks_and_refuses_second_run(files):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files)
    assert ev.main(argv(files, "compare")) == 0
    assert (files["out"] / "answers_lock.json").exists()
    assert ev.main(argv(files, "compare")) == 2


def test_compare_without_sheet_stops(files):
    assert ev.main(argv(files, "compare")) == 2


def test_n2_sheet_needs_the_lock(files):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files)
    assert ev.main(argv(files, "n2-sheet")) == 2
    assert not (files["out"] / "n2_sheet.md").exists()


def test_changed_answers_after_lock_stop_everything(files):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files)
    assert ev.main(argv(files, "compare")) == 0
    fill_answers(files, {"QR-0010-01": "1 | 2 | 2 | 2 | 2 | 2 | 2 | "})
    assert ev.main(argv(files, "n2-sheet")) == 2
    assert ev.main(argv(files, "result")) == 2


def test_changed_input_after_sheet_stops(files):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files)
    files["criteria.md"].write_text("criteria v2\n", encoding="utf-8")
    assert ev.main(argv(files, "compare")) == 2


def test_changed_allowlist_after_sheet_stops(files):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files)
    assert ev.main(argv(files, "compare") + ["--allowlist", "jax"]) == 2


def test_result_needs_complete_n2(files):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files)
    assert ev.main(argv(files, "compare")) == 0
    assert ev.main(argv(files, "result")) == 2
    assert ev.main(argv(files, "n2-sheet")) == 0
    assert ev.main(argv(files, "result")) == 2
    fill_n2(files, ("ja", "nein", "ja", "?", "nein", "vielleicht"))
    assert ev.main(argv(files, "result")) == 2
    assert not files["output"].exists()


def test_result_refuses_overwrite(files):
    run_all(files)
    assert ev.main(argv(files, "result")) == 2


def test_result_holds_no_content(files):
    run_all(files)
    text = files["output"].read_text(encoding="utf-8")
    for fragment in ("Exporter shall", "UTF-8", "SECRET-RATIONALE", "Quantenwissen",
                     "Beschreibung:", "parse(text)", "Parser crashes"):
        assert fragment not in text


def test_screen_output_holds_no_content(files, capsys):
    run_all(files)
    out = capsys.readouterr().out
    for fragment in ("Exporter shall", "UTF-8", "Quantenwissen", "Beschreibung:"):
        assert fragment not in out


def test_n2_sheet_content(files):
    assert ev.main(argv(files, "sheet")) == 0
    fill_answers(files)
    assert ev.main(argv(files, "compare")) == 0
    assert ev.main(argv(files, "n2-sheet")) == 0
    sheet = (files["out"] / "n2_sheet.md").read_text(encoding="utf-8")
    assert sheet.count("## ") == 6
    assert "Datensatz des Volllaufs: schema_invalid" in sheet
    assert "Kein gefundener Beleg" in sheet  # PR 30, excerpt not found


# --- counts -------------------------------------------------------------

def test_machine_values(files):
    state = state_of(files)
    values = {row["key"]: ev.machine_values(row, state.context) for row in state.rows}
    assert values["QR-0010-01"]["B9"] is True
    assert values["QR-0010-01"]["B8"] is True
    assert values["QR-0010-02"]["B9"] is True  # stated insufficient = derived
    assert values["QR-0010-02"]["B10"] is False  # "it"
    assert values["QR-0020-01"]["B9"] is True
    assert values["QR-0020-01"]["B8.2_pattern"] is True
    assert values["QR-0020-02"]["strength_matches"] is False
    assert values["QR-0020-02"]["B9"] is False
    assert values["QR-0030-01"]["all_evidence_found"] is False
    assert values["QR-0030-01"]["B10"] is False  # every


def test_partly_found(files):
    item_ok = evidence("body", "The Exporter must write files in UTF-8 format.",
                       ["system_name", "system_response"])
    item_bad = evidence("body", "This sentence is not in the body at all.", ["rationale"])
    row = {"key": "k", "pull": 10,
           "req": requirement("QR-0010-09", "The Exporter shall x.", "ubiquitous", "Exporter",
                              [item_ok, item_bad], "direct", "prescriptive")}
    values = ev.machine_values(row, state_of(files).context)
    assert values["partly_found"] is True
    assert values["all_evidence_found"] is False
    assert values["B9"] is False


def test_result_counts(files):
    counts = run_all(files)["counts"]
    assert counts["scope"]["requirements_in_base_set"] == 6
    assert counts["scope"]["sample_requirements"] == 5
    assert counts["scope"]["pull_requests_with_one_requirement"] == 1
    assert counts["hand"]["B1"] == {"2": 3, "1": 1, "0": 1, "?": 0, "rated": 5,
                                    "share_2_of_rated": 0.6, "pull_requests_with_a_0": 1}
    assert counts["hand"]["B2"]["?"] == 1
    assert counts["hand"]["B2"]["rated"] == 4
    assert counts["hand"]["B11a"]["-"] == 1
    assert counts["hand"]["B11a"]["0"] == 1
    assert counts["hand"]["B11a"]["pull_requests_with_a_0"] == 1
    # usable: 10-01 ja, 10-02 ja (all >= 1, B5=B6=2, B7=1, B8, B9),
    # 20-01 ja, 20-02 nein (B1 = 0), 30-01 not assessable (?)
    assert counts["usable_ff1"] == {"ja": 3, "nein": 1, "not_assessable": 1, "n": 5}
    machine = counts["machine"]
    assert machine["B8.1_schema_full_run"] == {"records": 5, "schema_valid": 4,
                                               "schema_invalid": 1}
    assert machine["sample"]["n"] == 5
    assert machine["base_set"]["n"] == 6
    assert machine["sample"]["B9"]["satisfied"] == 3
    assert machine["base_set"]["B9"]["satisfied"] == 4
    assert machine["sample"]["B10"]["requirements_by_class"]["K3"] == 1
    assert machine["sample"]["B10"]["requirements_by_class"]["K8"] == 2
    assert machine["sample"]["B10"]["hits_by_expression"]["every"] == 1
    assert machine["base_set"]["B10"]["requirements_with_hit"] == 3
    per = {row["key"]: row for row in counts["per_requirement"]}
    assert per["QR-0020-02"]["usable"] == "nein"
    assert per["QR-0030-01"]["B10_classes"] == ["K8"]
    assert counts["notes_filled"] == 1


def test_side_part_counts(files):
    side = run_all(files)["counts"]["side_part"]
    found = {(r["pr"], r["part"]): r["N1"] for r in side["per_row"]}
    assert found == {(10, "system_name"): True, (10, "system_response"): True,
                     (20, "system_response"): True, (20, "system_name"): False,
                     (30, "system_name"): False, (40, "system_name"): False}
    assert side["N1"]["total"] == {"found": 3, "of": 6}
    assert side["N1"]["system_name"] == {"found": 1, "of": 4}
    assert side["rows_without_valid_record_with_requirements"] == 1
    assert side["N2"]["total"] == {"ja": 2, "nein": 3, "?": 1}
    assert side["exploratory_requirements_in_pulls"] == {"75": "missing", "413": "missing",
                                                         "692": "missing"}


def test_exploratory_counts(files):
    exploratory = run_all(files)["counts"]["exploratory"]
    assert exploratory["forms"]["shall not"] == {"sample": 1, "base_set": 1}
    assert exploratory["B10_hit_vs_B1"]["with"]["0"] == 1
    assert exploratory["B10_hit_vs_B1"]["without"]["2"] == 2


@pytest.mark.parametrize("grades,b8,b9,expected", [
    ({"B1": "1", "B2": "1", "B3": "1", "B4": "1", "B5": "2", "B6": "2", "B7": "1"},
     True, True, "ja"),
    ({"B1": "0", "B2": "2", "B3": "2", "B4": "2", "B5": "2", "B6": "2", "B7": "2"},
     True, True, "nein"),
    ({"B1": "2", "B2": "2", "B3": "2", "B4": "0", "B5": "2", "B6": "2", "B7": "2"},
     True, True, "nein"),
    ({"B1": "2", "B2": "2", "B3": "2", "B4": "2", "B5": "1", "B6": "2", "B7": "2"},
     True, True, "nein"),
    ({"B1": "2", "B2": "2", "B3": "2", "B4": "2", "B5": "2", "B6": "1", "B7": "2"},
     True, True, "nein"),
    ({"B1": "2", "B2": "2", "B3": "2", "B4": "2", "B5": "2", "B6": "2", "B7": "0"},
     True, True, "nein"),
    ({"B1": "2", "B2": "2", "B3": "2", "B4": "2", "B5": "2", "B6": "2", "B7": "2"},
     False, True, "nein"),
    ({"B1": "2", "B2": "2", "B3": "2", "B4": "2", "B5": "2", "B6": "2", "B7": "2"},
     True, False, "nein"),
    ({"B1": "0", "B2": "2", "B3": "2", "B4": "2", "B5": "2", "B6": "2", "B7": "?"},
     True, True, "?"),
    ({"B1": "2", "B2": "2", "B3": "?", "B4": "2", "B5": "2", "B6": "2", "B7": "2"},
     True, True, "?"),
])
def test_usable_rule(grades, b8, b9, expected):
    assert ev.usable(grades, {"B8": b8, "B9": b9}) == expected


def test_grade_block_ignores_question_marks_in_share():
    block = ev.grade_block(["2", "2", "1", "?"])
    assert block["rated"] == 3
    assert block["share_2_of_rated"] == round(2 / 3, 4)
    assert ev.grade_block(["?"])["share_2_of_rated"] is None


# --- copy of the formulation probe -------------------------------------

@pytest.mark.parametrize("content", [
    "pr,part,where,fundstelle\n10,system_name,body,x\n",
    "pr,part,locations,fundstelle\n10,trigger,body,x\n",
    "pr,part,locations,fundstelle\n10,system_name,issue_comment,x\n",
    "pr,part,locations,fundstelle\nzehn,system_name,body,x\n",
    "pr,part,locations,fundstelle\n10,system_name,body,x\n10,system_name,diff,y\n",
    "pr,part,locations,fundstelle\n",
])
def test_invalid_fundstellen_are_refused(tmp_path, content):
    path = tmp_path / "f.csv"
    path.write_text(content, encoding="utf-8")
    with pytest.raises(ev.EvaluationError):
        ev.read_fundstellen(path)


def test_fundstellen_of_the_repository_are_valid():
    rows = ev.read_fundstellen(ev.DEFAULT_FUNDSTELLEN)
    assert len(rows) == 20
    assert len({row["pr"] for row in rows}) == 11


def test_strength_is_derived_from_all_evidence(files):
    """B9 compares with the strength from all evidence, not only the found."""
    item_ok = evidence("body", "The Exporter must write files in UTF-8 format.", ["system_name"])
    item_bad = evidence("body", "This sentence is not in the body at all.", ["system_response"])
    row = {"key": "k", "pull": 10,
           "req": requirement("QR-0010-09", "The Exporter shall x.", "ubiquitous", "Exporter",
                              [item_ok, item_bad], "direct", "prescriptive")}
    values = ev.machine_values(row, state_of(files).context)
    assert values["strength_matches"] is True
    assert values["B9"] is False


def test_n1_review_comment_counts_as_comment(files):
    changed = requirement(
        "QR-0010-02", "When the input is empty, the Exporter shall handle it without an error.",
        "event_driven", "Exporter",
        [evidence("review_comment", "Please make the Exporter validate paths first.",
                  ["system_name", "system_response"], "601")], "insufficient")
    write_jsonl(files["input.jsonl"], [record(10, [R10_1, changed])] + RECORDS[1:])
    state = state_of(files)
    fund = {"pr": 10, "part": "system_response", "locations": ["comment"], "fundstelle": "x"}
    assert ev.n1_found(state, fund) is True
    fund_diff = {**fund, "locations": ["diff"]}
    assert ev.n1_found(state, fund_diff) is False
