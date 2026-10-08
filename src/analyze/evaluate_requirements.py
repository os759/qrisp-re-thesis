"""Evaluation of the extracted requirements, decision E2.

Work package H. Research questions FF1 and FF2.

All rules are fixed before the first rating in
eval/instrument/kriterien_v1.md (criteria list v1, commit 938d338) and
in the addendum to E2 of 2026-10-08 in docs/entscheidungen.md:

* Scope: all requirements of the schema-valid records of the full run
  for the pull requests in docs/sample_eval_e2.md (the sample of G5).
* Hand criteria B1 to B7 per requirement, B11a and B11b per pull
  request, on the scale 2, 1, 0 and ? (not assessable). B11a gets - (not
  applicable) for a pull request with exactly one requirement; the
  program sets it.
* Machine criteria B8, B9 and B10 (sections 6.1 to 6.3 of the list),
  on the sample and on the whole base set.
* Side part of E2 (section 8): N1 by machine, N2 by hand after the lock.
* Counts of section 9, including the rule for "usable" in the sense of
  FF1.

The program holds no rule beyond the list. For B9 it calls the existing
functions of validate_output.py, diagnose_excerpts.py and
count_requirements.py. It never prints a requirement text, an excerpt,
a note or other pull request content; on screen appear only counts,
requirement identifiers and pull request numbers. Sheets and answer
files contain pull request content and belong under eval/responses/,
which git ignores.

Sub-commands, in this order:

    sheet      write the blind rating sheet and the answer file
    compare    check the answers; when complete, lock the answer file (A7)
    n2-sheet   after the lock: write the sheet and answer file for N2
    result     write all counts as JSON

Run from the project root, for example:

    python src/analyze/evaluate_requirements.py sheet \\
      --input data/processed/extraction_2026-09-25_full_v2.jsonl \\
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \\
      --model-input data/processed/model_input_2026-09-19.jsonl \\
      --mentions-map data/interim/mention_map.json \\
      --allowlist "jaspify,jax,pytest,rus" \\
      --sample docs/sample_eval_e2.md \\
      --out-dir eval/responses/evaluation_e2_2026-10-08
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import random
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
for _sub in ("extract", "prepare", "classify", "analyze"):
    if str(SRC / _sub) not in sys.path:
        sys.path.insert(0, str(SRC / _sub))

from jsonschema import Draft202012Validator  # noqa: E402

from check_classification import fence, load_requirements, read_sample  # noqa: E402
from count_requirements import evidence_status  # noqa: E402
from diagnose_excerpts import files_in_block, load_blocks  # noqa: E402
from pseudonymise import load_mapping  # noqa: E402
from validate_output import derive_evidence_strength, load_dataset  # noqa: E402

DEFAULT_SCHEMA = ROOT / "config" / "requirement_schema_v2.json"
DEFAULT_FUNDSTELLEN = ROOT / "eval" / "instrument" / "fundstellen_paket_c.csv"
DEFAULT_CRITERIA = ROOT / "eval" / "instrument" / "kriterien_v1.md"
PULL_URL = "https://github.com/eclipse-qrisp/Qrisp/pull/{number}"

ORDER_SEED = 20261008          # list v1, section 4
HAND_REQUIREMENT = ("B1", "B2", "B3", "B4", "B5", "B6", "B7")
HAND_PULL = ("B11a", "B11b")
GRADES = ("2", "1", "0", "?")  # list v1, section 2
NOT_APPLICABLE = "-"           # B11a with exactly one requirement
N2_ANSWERS = ("ja", "nein", "?")
PARTS = ("system_name", "system_response")
LOCATION_KIND = {"title": "title", "body": "body", "issue_comment": "comment",
                 "review_comment": "comment", "diff": "diff"}  # list v1, section 8
EXPLORATORY_PULLS = (75, 413, 692)  # list v1, section 8, last paragraph

# B8.2: the five keywords of the conditional EARS patterns (list v1, 6.1).
CONDITION_WORDS = ("while", "during", "when", "if", "where")
STATE_WORDS = ("while", "during", "where")
EVENT_WORDS = ("when", "if")
OTHER_MODALS = ("must", "should", "will", "may")  # B8.5

# B10: exactly the examples of 29148 clause 5.2.7 (list v1, 6.3), in the
# order of the table. K9 is not checked by machine.
WORD_LIST: tuple[tuple[str, str], ...] = (
    ("K1", "best"), ("K1", "most"),
    ("K2", "user friendly"), ("K2", "easy to use"), ("K2", "cost effective"),
    ("K3", "it"), ("K3", "this"), ("K3", "that"),
    ("K4", "almost always"), ("K4", "significant"), ("K4", "minimal"),
    ("K4", "or"), ("K4", "and/or"),
    ("K5", "provide support"), ("K5", "but not limited to"), ("K5", "as a minimum"),
    ("K6", "better than"), ("K6", "higher quality"),
    ("K7", "if possible"), ("K7", "as appropriate"), ("K7", "as applicable"),
    ("K8", "all"), ("K8", "always"), ("K8", "never"), ("K8", "every"),
)
CLASSES = tuple(sorted({cls for cls, _ in WORD_LIST}))

# Exploratory counts of list v1, section 9 (no criterion).
FORMS = ("shall not", "shall be able to")


class EvaluationError(Exception):
    """A violated precondition. The message never holds content."""


# --- word search (list v1, 6.3, search rules; also used by B8) ----------

LETTER_OR_DIGIT = r"[^\W_]"


def word_pattern(expression: str) -> re.Pattern[str]:
    """Whole words, any case, a space inside also matches a hyphen."""
    body = r"[ \-]".join(re.escape(part) for part in expression.split(" "))
    return re.compile(rf"(?<!{LETTER_OR_DIGIT}){body}(?!{LETTER_OR_DIGIT})",
                      re.IGNORECASE)


# Longest expression first; and/or (6 characters) therefore before or.
SEARCH_ORDER = sorted(((cls, expr, word_pattern(expr)) for cls, expr in WORD_LIST),
                      key=lambda entry: -len(entry[1]))
SHALL = word_pattern("shall")


def has_word(text: str, word: str) -> bool:
    return word_pattern(word).search(text) is not None


def b10_hits(text: str) -> list[tuple[str, str]]:
    """(class, expression) per hit. A character counts for one hit only."""
    taken = [False] * len(text)
    hits: list[tuple[str, str]] = []
    for cls, expression, pattern in SEARCH_ORDER:
        for match in pattern.finditer(text):
            if any(taken[match.start():match.end()]):
                continue
            for position in range(match.start(), match.end()):
                taken[position] = True
            hits.append((cls, expression))
    return hits


# --- B8 format conformity (list v1, 6.1) --------------------------------


def first_word(text: str) -> str:
    match = re.search(r"[^\W\d_]+", text)
    return match.group(0).lower() if match else ""


def part_before_shall(text: str) -> str | None:
    """Text before the first word shall, any case; None without such a word."""
    match = SHALL.search(text)
    return text[:match.start()] if match else None


def part_after_shall(text: str) -> str:
    match = SHALL.search(text)
    return text[match.end():] if match else ""


def b8_pattern(requirement: dict[str, Any]) -> bool:
    """B8.2: the first word fits ears_pattern."""
    text = requirement.get("text", "")
    first = first_word(text)
    before = part_before_shall(text)
    pattern = requirement.get("ears_pattern")
    if pattern == "ubiquitous":
        return first not in CONDITION_WORDS
    if pattern == "state_driven":
        return first in ("while", "during")
    if pattern == "event_driven":
        return first == "when"
    if pattern == "unwanted_behaviour":
        return first == "if" and before is not None and has_word(before, "then")
    if pattern == "optional_feature":
        return first == "where"
    if pattern == "complex":
        return (first in CONDITION_WORDS and before is not None
                and any(has_word(before, word) for word in STATE_WORDS)
                and any(has_word(before, word) for word in EVENT_WORDS))
    return False


def b8_order(requirement: dict[str, Any]) -> bool:
    """B8.3: system_name, any case, in the part before shall."""
    before = part_before_shall(requirement.get("text", ""))
    name = (requirement.get("system_name") or "").casefold()
    return before is not None and bool(name) and name in before.casefold()


def b8_shall(requirement: dict[str, Any]) -> bool:
    """B8.4: shall occurs as a word exactly once, in lower case."""
    found = SHALL.findall(requirement.get("text", ""))
    return len(found) == 1 and found[0] == "shall"


def b8_no_other_modal(requirement: dict[str, Any]) -> bool:
    """B8.5: none of must, should, will, may as a word, any case."""
    text = requirement.get("text", "")
    return not any(has_word(text, word) for word in OTHER_MODALS)


B8_CHECKS = (("B8.2_pattern", b8_pattern), ("B8.3_order", b8_order),
             ("B8.4_shall", b8_shall), ("B8.5_no_other_modal", b8_no_other_modal))


# --- machine criteria per requirement -----------------------------------


class Context:
    """Dataset, model input and mention map, needed for B9 and N1."""

    def __init__(self, dataset: dict[int, dict[str, Any]], blocks: dict[int, str],
                 mapping: dict[str, str] | None, allowlist: set[str]) -> None:
        self.dataset = dataset
        self.blocks = blocks
        self.mapping = mapping
        self.allowlist = allowlist

    def found_flags(self, pull_number: int, requirement: dict[str, Any]) -> list[bool]:
        pull = self.dataset.get(pull_number)
        shown = files_in_block(self.blocks.get(pull_number, ""))
        return [evidence_status(item, pull, shown, self.mapping, self.allowlist)[0]
                for item in requirement.get("evidence", [])]


def machine_values(row: dict[str, Any], context: Context) -> dict[str, Any]:
    """B8, B9 and B10 for one requirement, without its text."""
    requirement = row["req"]
    values: dict[str, Any] = {name: check(requirement) for name, check in B8_CHECKS}
    values["B8"] = all(values[name] for name, _ in B8_CHECKS)
    flags = context.found_flags(row["pull"], requirement)
    values["all_evidence_found"] = bool(flags) and all(flags)
    values["partly_found"] = any(flags) and not all(flags)
    values["strength_matches"] = (requirement.get("evidence_strength")
                                  == derive_evidence_strength(requirement))
    values["B9"] = values["all_evidence_found"] and values["strength_matches"]
    hits = b10_hits(requirement.get("text", ""))
    values["B10_hits"] = hits
    values["B10"] = not hits
    return values


def machine_block(rows: list[dict[str, Any]], values: dict[str, dict[str, Any]]) -> dict[str, Any]:
    keys = [row["key"] for row in rows]

    def count(name: str) -> int:
        return sum(1 for key in keys if values[key][name])

    by_class_requirements = Counter()
    hits_by_class = Counter()
    hits_by_expression = Counter()
    for key in keys:
        hits = values[key]["B10_hits"]
        for cls in {cls for cls, _ in hits}:
            by_class_requirements[cls] += 1
        for cls, expression in hits:
            hits_by_class[cls] += 1
            hits_by_expression[expression] += 1
    return {
        "n": len(keys),
        "B8": {"satisfied": count("B8"),
               **{name: count(name) for name, _ in B8_CHECKS}},
        "B9": {"satisfied": count("B9"), "all_evidence_found": count("all_evidence_found"),
               "strength_matches": count("strength_matches"),
               "partly_found": count("partly_found")},
        "B10": {"satisfied": count("B10"), "requirements_with_hit": len(keys) - count("B10"),
                "hits_total": sum(hits_by_class.values()),
                "requirements_by_class": {cls: by_class_requirements[cls] for cls in CLASSES},
                "hits_by_class": {cls: hits_by_class[cls] for cls in CLASSES},
                "hits_by_expression": {expr: hits_by_expression[expr]
                                       for _, expr in WORD_LIST}},
    }


# --- reading the inputs -------------------------------------------------


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise EvaluationError(f"line {line_number} of {path} is not valid JSON") from error
    return rows


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], check=True,
                              capture_output=True, text=True, cwd=ROOT).stdout.strip() or "unknown"
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def read_fundstellen(path: Path) -> list[dict[str, Any]]:
    """Rows of the copy from the formulation probe (list v1, section 8)."""
    text = path.read_text(encoding="utf-8")
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames != ["pr", "part", "locations", "fundstelle"]:
        raise EvaluationError(f"{path}: header must be pr,part,locations,fundstelle")
    rows = []
    seen = set()
    for line_number, row in enumerate(reader, start=2):
        locations = row["locations"].split("+") if row["locations"] else []
        if not (row["pr"] or "").isdigit() or row["part"] not in PARTS or not locations \
                or any(kind not in set(LOCATION_KIND.values()) for kind in locations):
            raise EvaluationError(f"{path}, line {line_number}: invalid row")
        if (int(row["pr"]), row["part"]) in seen:
            raise EvaluationError(f"{path}, line {line_number}: row appears twice")
        seen.add((int(row["pr"]), row["part"]))
        rows.append({"pr": int(row["pr"]), "part": row["part"],
                     "locations": locations, "fundstelle": row["fundstelle"]})
    if not rows:
        raise EvaluationError(f"{path}: no rows")
    return rows


class State:
    """Everything derived from the inputs; identical on every call."""

    def __init__(self, arguments: argparse.Namespace) -> None:
        schema = json.loads(Path(arguments.schema).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        self.records = read_jsonl(Path(arguments.input))
        self.record_by_pull: dict[int, dict[str, Any]] = {}
        self.valid_pulls: set[int] = set()
        for record in self.records:
            number = record.get("pull_number")
            if number in self.record_by_pull:
                raise EvaluationError(f"pull request {number} has more than one record")
            self.record_by_pull[number] = record
            if not any(True for _ in validator.iter_errors(record)):
                self.valid_pulls.add(number)
        self.rows = load_requirements(self.records, validator)
        self.by_key = {row["key"]: row for row in self.rows}
        self.sample_pulls = read_sample(Path(arguments.sample))
        sample_set = set(self.sample_pulls)
        self.sample_rows = [row for row in self.rows if row["pull"] in sample_set]
        self.keys_by_pull: dict[int, list[str]] = {}
        for row in self.sample_rows:
            self.keys_by_pull.setdefault(row["pull"], []).append(row["key"])
        for keys in self.keys_by_pull.values():
            keys.sort()
        self.entries = build_entries(self.keys_by_pull)
        self.fundstellen = read_fundstellen(Path(arguments.fundstellen))
        self.arguments = arguments
        self._context: Context | None = None

    @property
    def context(self) -> Context:
        if self._context is None:
            arguments = self.arguments
            mapping = (load_mapping(Path(arguments.mentions_map))
                       if arguments.mentions_map else None)
            self._context = Context(load_dataset(Path(arguments.dataset)),
                                    load_blocks(Path(arguments.model_input)),
                                    mapping, allowlist_of(arguments))
        return self._context

    def single(self, pull: int) -> bool:
        return len(self.keys_by_pull[pull]) == 1


def build_entries(keys_by_pull: dict[int, list[str]]) -> list[list[Any]]:
    """Sheet order (list v1, section 4): pull requests shuffled with the
    seed, requirements by identifier, then the block for level 2."""
    pulls = sorted(keys_by_pull)
    random.Random(ORDER_SEED).shuffle(pulls)
    entries: list[list[Any]] = []
    number = 0
    for pull in pulls:
        for key in keys_by_pull[pull]:
            number += 1
            entries.append(["R", number, key, pull])
        entries.append(["P", pull])
    return entries


def allowlist_of(arguments: argparse.Namespace) -> set[str]:
    return {name.strip().lower() for name in arguments.allowlist.split(",") if name.strip()}


INPUT_NAMES = ("input", "dataset", "model_input", "mentions_map", "sample", "schema",
               "fundstellen", "criteria")


def input_hashes(arguments: argparse.Namespace) -> dict[str, str | None]:
    hashes: dict[str, str | None] = {}
    for name in INPUT_NAMES:
        value = getattr(arguments, name)
        hashes[name] = sha256_of(Path(value)) if value else None
    return hashes


# --- sheet and answers --------------------------------------------------


def text_block(text: str) -> list[str]:
    mark = fence(text)
    return [f"{mark}text", text, mark, ""]


def render_sheet(state: State) -> str:
    """Blind sheet: sentence and excerpts only (list v1, section 4)."""
    lines = ["# Bewertungsbogen nach E2, Kriterienliste v1", "",
             "Lokale Datei mit Inhalten aus Pull Requests. Nicht in einen Chat kopieren.",
             "Antworten in answers.txt, nicht hier. Notenregeln:",
             "eval/instrument/kriterien_v1.md, Abschnitte 3, 5 und 7.", ""]
    for entry in state.entries:
        if entry[0] == "R":
            _, number, key, pull = entry
            requirement = state.by_key[key]["req"]
            lines += [f"## {number}. {key} (PR {pull})", "",
                      f"Link: {PULL_URL.format(number=pull)}", "", "Anforderung:", ""]
            lines += text_block(requirement["text"])
            for index, item in enumerate(requirement["evidence"], start=1):
                where = item["location"] + (f", {item['locator']}" if item.get("locator") else "")
                lines += [f"Beleg {index} ({where}):", ""]
                lines += text_block(item["excerpt"])
        else:
            pull = entry[1]
            keys = state.keys_by_pull[pull]
            lines += [f"## PR {pull}, Ebene 2 (B11a, B11b)", "",
                      f"Link: {PULL_URL.format(number=pull)}", "",
                      f"Alle Anforderungen dieses Pull Requests: {len(keys)}", ""]
            for key in keys:
                lines += [f"{key}:", ""]
                lines += text_block(state.by_key[key]["req"]["text"])
            if state.single(pull):
                lines += ["B11a ist vom Programm auf - gesetzt (genau eine Anforderung).", ""]
    return "\n".join(lines) + "\n"


ANSWER_HEADER = """# Antworten zur Bewertung nach E2, Kriterienliste v1. Eine Zeile je Eintrag im Bogen.
# Zeile R (Anforderung): R | Nummer | Kennung | B1 | B2 | B3 | B4 | B5 | B6 | B7 | Notiz
# Zeile P (Pull Request): P | PR | B11a | B11b | Notiz
# Werte: 2, 1, 0 oder ? (nicht beurteilbar). Bei ? gehoert der Grund in die Notiz.
# B11a mit - hat das Programm gesetzt (genau eine Anforderung). Nicht aendern.
# Notiz: freier Text ohne das Zeichen |. Kann leer bleiben, ausser bei ?.
"""


def render_answers(state: State) -> str:
    lines = []
    for entry in state.entries:
        if entry[0] == "R":
            lines.append(f"R | {entry[1]} | {entry[2]} |" + "  |" * len(HAND_REQUIREMENT) + " ")
        else:
            first = f" {NOT_APPLICABLE} " if state.single(entry[1]) else "  "
            lines.append(f"P | {entry[1]} |{first}|  | ")
    return ANSWER_HEADER + "\n".join(lines) + "\n"


def parse_answers(text: str, state: State) -> tuple[dict[str, Any], list[str]]:
    """Answers by requirement key and by pull request, and a list of
    problems that name line numbers only."""
    expected_r = {entry[2]: entry[1] for entry in state.entries if entry[0] == "R"}
    expected_p = {entry[1] for entry in state.entries if entry[0] == "P"}
    requirements: dict[str, dict[str, str]] = {}
    pulls: dict[int, dict[str, str]] = {}
    problems: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split("|")]
        kind = fields[0].upper()
        if kind == "R":
            if len(fields) != 3 + len(HAND_REQUIREMENT) + 1:
                problems.append(f"line {line_number}: an R line needs 11 fields "
                                "(| in the note?)")
                continue
            number, key = fields[1], fields[2]
            if key not in expected_r or number != str(expected_r[key]):
                problems.append(f"line {line_number}: number and id do not match the sheet")
                continue
            if key in requirements:
                problems.append(f"line {line_number}: entry {number} appears twice")
                continue
            grades = dict(zip(HAND_REQUIREMENT, fields[3:3 + len(HAND_REQUIREMENT)]))
            note = fields[-1]
            for name, value in grades.items():
                if value not in GRADES:
                    problems.append(f"line {line_number}: {name} must be 2, 1, 0 or ?")
            if "?" in grades.values() and not note:
                problems.append(f"line {line_number}: ? needs a reason in the note")
            requirements[key] = {**grades, "note": note}
        elif kind == "P":
            if len(fields) != 5:
                problems.append(f"line {line_number}: a P line needs 5 fields (| in the note?)")
                continue
            if not fields[1].isdigit() or int(fields[1]) not in expected_p:
                problems.append(f"line {line_number}: not a pull request of the sheet")
                continue
            pull = int(fields[1])
            if pull in pulls:
                problems.append(f"line {line_number}: pull request {pull} appears twice")
                continue
            b11a, b11b, note = fields[2], fields[3], fields[4]
            if state.single(pull):
                if b11a != NOT_APPLICABLE:
                    problems.append(f"line {line_number}: B11a must stay - "
                                    "(exactly one requirement)")
            elif b11a not in GRADES:
                problems.append(f"line {line_number}: B11a must be 2, 1, 0 or ?")
            if b11b not in GRADES:
                problems.append(f"line {line_number}: B11b must be 2, 1, 0 or ?")
            if "?" in (b11a, b11b) and not note:
                problems.append(f"line {line_number}: ? needs a reason in the note")
            pulls[pull] = {"B11a": b11a, "B11b": b11b, "note": note}
        else:
            problems.append(f"line {line_number}: line must start with R or P")
    missing_r = [number for key, number in expected_r.items() if key not in requirements]
    missing_p = sorted(expected_p - set(pulls))
    if missing_r:
        problems.append(f"requirements without an answer line: {len(missing_r)} "
                        f"(first: {min(missing_r)})")
    if missing_p:
        problems.append(f"pull requests without an answer line: {len(missing_p)} "
                        f"(first: PR {missing_p[0]})")
    return {"requirements": requirements, "pulls": pulls}, problems


# --- side part N1 and N2 (list v1, section 8) ----------------------------


def record_state(state: State, pull: int) -> str:
    record = state.record_by_pull.get(pull)
    if record is None:
        return "missing"
    if pull not in state.valid_pulls:
        return "schema_invalid"
    return "valid" if record.get("requirements") else "no_requirements"


def carrying_evidence(state: State, pull: int, part: str) -> list[tuple[str, dict[str, Any]]]:
    """Found evidence of the valid record that carries the part, any location."""
    if record_state(state, pull) != "valid":
        return []
    result = []
    for row in state.rows:
        if row["pull"] != pull:
            continue
        flags = state.context.found_flags(pull, row["req"])
        for item, found in zip(row["req"].get("evidence", []), flags):
            if found and part in item.get("supports", []):
                result.append((row["key"], item))
    return result


def n1_found(state: State, fund: dict[str, Any]) -> bool:
    return any(LOCATION_KIND.get(item.get("location")) in fund["locations"]
               for _, item in carrying_evidence(state, fund["pr"], fund["part"]))


def render_n2_sheet(state: State) -> str:
    lines = ["# Bogen N2, Nebenteil von E2 (Kriterienliste v1, Abschnitt 8)", "",
             "Lokale Datei mit Inhalten aus Pull Requests. Nicht in einen Chat kopieren.",
             "Frage: Gibt mindestens einer der gezeigten Belege die Stelle wieder,",
             "die die Formulierungsprobe nennt? Antwort ja, nein oder ? in n2_answers.txt.", ""]
    for number, fund in enumerate(state.fundstellen, start=1):
        lines += [f"## {number}. PR {fund['pr']}, {fund['part']}", "",
                  f"Link: {PULL_URL.format(number=fund['pr'])}", "",
                  f"Fundstelle der Formulierungsprobe ({'+'.join(fund['locations'])}):", ""]
        lines += text_block(fund["fundstelle"])
        status = record_state(state, fund["pr"])
        evidence = carrying_evidence(state, fund["pr"], fund["part"])
        if status != "valid":
            lines += [f"Datensatz des Volllaufs: {status}. Keine Belege.", ""]
        elif not evidence:
            lines += ["Kein gefundener Beleg der Pipeline traegt diesen Bestandteil.", ""]
        for index, (key, item) in enumerate(evidence, start=1):
            where = item["location"] + (f", {item['locator']}" if item.get("locator") else "")
            lines += [f"Beleg {index} von {key} ({where}):", ""]
            lines += text_block(item["excerpt"])
    return "\n".join(lines) + "\n"


N2_HEADER = """# Antworten N2. Felder: Nummer | PR | Bestandteil | Antwort | Notiz
# Antwort: ja, nein oder ?. Notiz: freier Text ohne das Zeichen |.
"""


def render_n2_answers(state: State) -> str:
    return N2_HEADER + "".join(f"{n} | {fund['pr']} | {fund['part']} |  | \n"
                               for n, fund in enumerate(state.fundstellen, start=1))


def parse_n2(text: str, state: State) -> tuple[dict[int, str], list[str]]:
    answers: dict[int, str] = {}
    problems: list[str] = []
    rows = state.fundstellen
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split("|")]
        if len(fields) != 5 or not fields[0].isdigit() \
                or not 1 <= int(fields[0]) <= len(rows) \
                or fields[1] != str(rows[int(fields[0]) - 1]["pr"]) \
                or fields[2] != rows[int(fields[0]) - 1]["part"]:
            problems.append(f"line {line_number}: does not match a row of the N2 sheet")
            continue
        number = int(fields[0])
        if number in answers:
            problems.append(f"line {line_number}: row {number} appears twice")
            continue
        if fields[3].lower() not in N2_ANSWERS:
            problems.append(f"line {line_number}: answer must be ja, nein or ?")
        answers[number] = fields[3].lower()
    if len(answers) != len(rows):
        problems.append(f"N2 rows without an answer line: {len(rows) - len(answers)}")
    return answers, problems


# --- counts (list v1, section 9) ----------------------------------------


def grade_block(values: list[str], with_not_applicable: bool = False) -> dict[str, Any]:
    counts = Counter(values)
    rated = sum(counts[g] for g in ("2", "1", "0"))
    block: dict[str, Any] = {g: counts[g] for g in GRADES}
    if with_not_applicable:
        block[NOT_APPLICABLE] = counts[NOT_APPLICABLE]
    block["rated"] = rated
    block["share_2_of_rated"] = round(counts["2"] / rated, 4) if rated else None
    return block


def usable(grades: dict[str, str], machine: dict[str, Any]) -> str:
    """Rule for "usable" in the sense of FF1 (list v1, section 9)."""
    if any(grades[name] == "?" for name in HAND_REQUIREMENT):
        return "?"
    ok = (all(int(grades[name]) >= 1 for name in ("B1", "B2", "B3", "B4"))
          and grades["B5"] == "2" and grades["B6"] == "2" and int(grades["B7"]) >= 1
          and machine["B8"] and machine["B9"])
    return "ja" if ok else "nein"


def cross(rows_keys: list[str], has: dict[str, bool], grades: dict[str, dict[str, str]],
          criterion: str) -> dict[str, dict[str, int]]:
    result = {"with": Counter(), "without": Counter()}
    for key in rows_keys:
        result["with" if has[key] else "without"][grades[key][criterion]] += 1
    return {side: {g: counts[g] for g in GRADES} for side, counts in result.items()}


def tally(state: State, answers: dict[str, Any], n2: dict[int, str]) -> dict[str, Any]:
    context = state.context
    values = {row["key"]: machine_values(row, context) for row in state.rows}
    sample_keys = [row["key"] for row in state.sample_rows]
    grades = answers["requirements"]
    pull_grades = answers["pulls"]

    hand: dict[str, Any] = {}
    for name in HAND_REQUIREMENT:
        block = grade_block([grades[key][name] for key in sample_keys])
        block["pull_requests_with_a_0"] = len({state.by_key[key]["pull"] for key in sample_keys
                                               if grades[key][name] == "0"})
        hand[name] = block
    for name in HAND_PULL:
        block = grade_block([pull_grades[p][name] for p in state.keys_by_pull],
                            with_not_applicable=True)
        block["pull_requests_with_a_0"] = sum(1 for p in state.keys_by_pull
                                              if pull_grades[p][name] == "0")
        hand[name] = block

    usable_values = {key: usable(grades[key], values[key]) for key in sample_keys}
    usable_counts = Counter(usable_values.values())

    record_count = len(state.records)
    machine = {
        "B8.1_schema_full_run": {"records": record_count,
                                  "schema_valid": len(state.valid_pulls),
                                  "schema_invalid": record_count - len(state.valid_pulls)},
        "sample": machine_block(state.sample_rows, values),
        "base_set": machine_block(state.rows, values),
    }

    per_row = []
    n1_counts = {part: Counter() for part in PARTS}
    n2_counts = {part: Counter() for part in PARTS}
    not_valid = 0
    for number, fund in enumerate(state.fundstellen, start=1):
        status = record_state(state, fund["pr"])
        found = n1_found(state, fund)
        not_valid += status != "valid"
        n1_counts[fund["part"]]["found" if found else "not_found"] += 1
        n2_counts[fund["part"]][n2[number]] += 1
        per_row.append({"row": number, "pr": fund["pr"], "part": fund["part"],
                        "record": status, "N1": found, "N2": n2[number]})
    side = {
        "rows": len(state.fundstellen),
        "pull_requests": len({fund["pr"] for fund in state.fundstellen}),
        "rows_without_valid_record_with_requirements": not_valid,
        "N1": {part: {"found": n1_counts[part]["found"],
                      "of": sum(n1_counts[part].values())} for part in PARTS},
        "N2": {part: {answer: n2_counts[part][answer] for answer in N2_ANSWERS}
               for part in PARTS},
        "per_row": per_row,
        "exploratory_requirements_in_pulls": {
            str(pull): (len(state.record_by_pull[pull]["requirements"])
                        if record_state(state, pull) in ("valid", "no_requirements")
                        else record_state(state, pull))
            for pull in EXPLORATORY_PULLS},
    }
    side["N1"]["total"] = {"found": sum(side["N1"][p]["found"] for p in PARTS),
                           "of": len(state.fundstellen)}
    side["N2"]["total"] = {answer: sum(side["N2"][p][answer] for p in PARTS)
                           for answer in N2_ANSWERS}

    def form_count(rows: list[dict[str, Any]], form: str) -> int:
        pattern = word_pattern(form)
        return sum(1 for row in rows if pattern.search(row["req"].get("text", "")))

    exploratory = {
        "note": "exploratory, no criterion (list v1, section 9)",
        "B10_hit_vs_B1": cross(sample_keys, {k: not values[k]["B10"] for k in sample_keys},
                               grades, "B1"),
        "and_after_shall_vs_B3": cross(
            sample_keys,
            {k: has_word(part_after_shall(state.by_key[k]["req"].get("text", "")), "and")
             for k in sample_keys}, grades, "B3"),
        "forms": {form: {"sample": form_count(state.sample_rows, form),
                         "base_set": form_count(state.rows, form)} for form in FORMS},
    }

    per_requirement = [{
        "key": key, "pull": state.by_key[key]["pull"],
        **{name: grades[key][name] for name in HAND_REQUIREMENT},
        **{name: values[key][name] for name, _ in B8_CHECKS},
        "B8": values[key]["B8"], "B9": values[key]["B9"],
        "B9_all_evidence_found": values[key]["all_evidence_found"],
        "B9_strength_matches": values[key]["strength_matches"],
        "B10": values[key]["B10"],
        "B10_classes": sorted({cls for cls, _ in values[key]["B10_hits"]}),
        "usable": usable_values[key],
    } for key in sample_keys]
    per_pull = [{"pull": pull, "requirements": len(keys), "B11a": pull_grades[pull]["B11a"],
                 "B11b": pull_grades[pull]["B11b"]}
                for pull, keys in sorted(state.keys_by_pull.items())]

    return {
        "scope": scope_counts(state),
        "hand": hand,
        "notes_filled": sum(1 for key in sample_keys if grades[key]["note"])
        + sum(1 for p in state.keys_by_pull if pull_grades[p]["note"]),
        "usable_ff1": {"ja": usable_counts["ja"], "nein": usable_counts["nein"],
                       "not_assessable": usable_counts["?"], "n": len(sample_keys)},
        "machine": machine,
        "side_part": side,
        "exploratory": exploratory,
        "per_requirement": per_requirement,
        "per_pull_request": per_pull,
    }


# --- command line -------------------------------------------------------


def print_counts(value: Any, prefix: str = "", skip: tuple[str, ...] = ()) -> None:
    for key, item in value.items():
        if key in skip:
            continue
        if isinstance(item, dict):
            print(f"{prefix}{key}:")
            print_counts(item, prefix + "  ", skip)
        elif isinstance(item, list):
            print(f"{prefix}{key}: {len(item)} entries (see the JSON file)")
        else:
            print(f"{prefix}{key}: {item}")


def refuse_existing(*paths: Path) -> None:
    existing = [str(path) for path in paths if path.exists()]
    if existing:
        raise EvaluationError("refusing to overwrite: " + ", ".join(existing))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def paths_in(directory: Path) -> dict[str, Path]:
    return {"sheet": directory / "sheet.md", "answers": directory / "answers.txt",
            "manifest": directory / "sheet_manifest.json",
            "lock": directory / "answers_lock.json",
            "n2_sheet": directory / "n2_sheet.md", "n2_answers": directory / "n2_answers.txt"}


def scope_counts(state: State) -> dict[str, int]:
    return {"requirements_in_base_set": len(state.rows),
            "sample_pull_requests": len(state.sample_pulls),
            "sample_pull_requests_with_requirements": len(state.keys_by_pull),
            "sample_requirements": len(state.sample_rows),
            "pull_requests_with_one_requirement": sum(
                1 for p in state.keys_by_pull if state.single(p)),
            "fundstellen_rows": len(state.fundstellen)}


def command_sheet(arguments: argparse.Namespace) -> int:
    paths = paths_in(Path(arguments.out_dir))
    refuse_existing(paths["sheet"], paths["answers"], paths["manifest"])
    state = State(arguments)
    if not state.sample_rows:
        raise EvaluationError("no requirement of the sample in a schema-valid record")
    Path(arguments.out_dir).mkdir(parents=True, exist_ok=True)
    paths["sheet"].write_text(render_sheet(state), encoding="utf-8")
    paths["answers"].write_text(render_answers(state), encoding="utf-8")
    write_json(paths["manifest"], {"entries": state.entries, "inputs": input_hashes(arguments),
                                   "allowlist": sorted(allowlist_of(arguments)),
                                   "code_commit": git_commit(), "seed": ORDER_SEED})
    print_counts(scope_counts(state))
    print(f"sheet entries written: {len(state.entries)}")
    return 0


def load_checked_state(arguments: argparse.Namespace) -> tuple[dict[str, Path], State]:
    paths = paths_in(Path(arguments.out_dir))
    if not paths["manifest"].exists():
        raise EvaluationError("no sheet yet; run the sheet command first")
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    if manifest["inputs"] != input_hashes(arguments):
        raise EvaluationError("inputs differ from those of the sheet (checksums)")
    if manifest["allowlist"] != sorted(allowlist_of(arguments)):
        raise EvaluationError("allowlist differs from that of the sheet")
    state = State(arguments)
    if state.entries != manifest["entries"]:
        raise EvaluationError("sheet order cannot be reproduced")
    return paths, state


def checked_lock(paths: dict[str, Path]) -> None:
    if not paths["lock"].exists():
        raise EvaluationError("answers are not locked yet; run compare first")
    lock = json.loads(paths["lock"].read_text(encoding="utf-8"))
    if lock["answers_sha256"] != sha256_of(paths["answers"]):
        raise EvaluationError("answer file changed after the compare step")


def command_compare(arguments: argparse.Namespace) -> int:
    paths, state = load_checked_state(arguments)
    refuse_existing(paths["lock"])
    answers, problems = parse_answers(paths["answers"].read_text(encoding="utf-8"), state)
    if problems:
        for problem in problems:
            print(problem)
        print(f"answers not complete: {len(problems)} problem(s). Nothing written.")
        return 1
    write_json(paths["lock"], {"answers_sha256": sha256_of(paths["answers"])})
    print(f"requirements rated: {len(answers['requirements'])}")
    print(f"pull requests rated: {len(answers['pulls'])}")
    print("answer file locked (A7). Do not change answers.txt from now on.")
    return 0


def command_n2_sheet(arguments: argparse.Namespace) -> int:
    paths, state = load_checked_state(arguments)
    checked_lock(paths)
    refuse_existing(paths["n2_sheet"], paths["n2_answers"])
    paths["n2_sheet"].write_text(render_n2_sheet(state), encoding="utf-8")
    paths["n2_answers"].write_text(render_n2_answers(state), encoding="utf-8")
    statuses = Counter(record_state(state, fund["pr"]) for fund in state.fundstellen)
    print(f"N2 rows written: {len(state.fundstellen)}")
    print("records of these rows: " + ", ".join(f"{k} {v}" for k, v in sorted(statuses.items())))
    return 0


def command_result(arguments: argparse.Namespace) -> int:
    output = Path(arguments.output)
    refuse_existing(output)
    paths, state = load_checked_state(arguments)
    checked_lock(paths)
    answers, problems = parse_answers(paths["answers"].read_text(encoding="utf-8"), state)
    if problems:
        raise EvaluationError(f"answers not complete: {len(problems)} problem(s)")
    if not paths["n2_answers"].exists():
        raise EvaluationError("no N2 answer file yet; run n2-sheet first")
    n2, problems = parse_n2(paths["n2_answers"].read_text(encoding="utf-8"), state)
    if problems:
        for problem in problems:
            print(problem)
        raise EvaluationError(f"N2 answers not complete: {len(problems)} problem(s)")
    counts = tally(state, answers, n2)
    result = {
        "rules": "eval/instrument/kriterien_v1.md; docs/entscheidungen.md: E2 and its addenda",
        "code_commit": git_commit(),
        "inputs": {name: {"path": getattr(arguments, name), "sha256": value}
                   for name, value in input_hashes(arguments).items()},
        "allowlist": sorted(allowlist_of(arguments)),
        "files": {name: sha256_of(paths[name])
                  for name in ("sheet", "answers", "n2_sheet", "n2_answers")},
        "counts": counts,
    }
    write_json(output, result)
    print_counts(counts, skip=("hits_by_expression",))
    print(f"written: {output}")
    return 0


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluation after E2 and criteria list v1. "
                                     "Prints numbers and identifiers only.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("sheet", "compare", "n2-sheet", "result"):
        command = sub.add_parser(name)
        command.add_argument("--input", required=True, help="Extraction output, JSONL.")
        command.add_argument("--dataset", required=True, help="Prepared dataset, JSONL.")
        command.add_argument("--model-input", required=True,
                             help="Model input the run used, JSONL with source_block.")
        command.add_argument("--mentions-map", default=None)
        command.add_argument("--allowlist", default="")
        command.add_argument("--sample", required=True, help="Sample file of draw_sample.py.")
        command.add_argument("--schema", default=str(DEFAULT_SCHEMA))
        command.add_argument("--fundstellen", default=str(DEFAULT_FUNDSTELLEN))
        command.add_argument("--criteria", default=str(DEFAULT_CRITERIA))
        command.add_argument("--out-dir", required=True, help="Directory under eval/responses/.")
        if name == "result":
            command.add_argument("--output", required=True,
                                 help="Result JSON, never overwritten.")
    return parser.parse_args(argv)


COMMANDS = {"sheet": command_sheet, "compare": command_compare,
            "n2-sheet": command_n2_sheet, "result": command_result}


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    try:
        return COMMANDS[arguments.command](arguments)
    except EvaluationError as error:
        print(f"Stopped: {error}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
