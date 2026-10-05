"""Manual check of the classification labels, decisions G4 and G5.

Work package G, steps 6 and 7. Research questions FF1 and FF4.

The rules are fixed in docs/entscheidungen.md before the check:

* G4 is the yardstick: the six type values, the kinds derived from them
  and the final definition of security_relevant.
* G5 is the check plan: three sets (marked, search hits, sample), the
  keyword list, the cap of 150 search hits, the seed 20261005, a blind
  check sheet, and the Dependabot review of the 25 closed records.

The script draws and counts; it holds no rule beyond G4 and G5. It
never prints a requirement text, a rationale, an excerpt, a title or a
comment. Only counts, requirement identifiers and pull request numbers
appear on screen. Sheet and answer files contain pull request content
and therefore belong under eval/responses/, which git ignores.

Sub-commands, in this order:

    search             counts of the three sets, before the check
    sheet              write the blind check sheet and the answer file
    compare            check the answers, write the follow-up file for
                       disagreements on security relevance
    result             write the counts of G5 section 6 as JSON
    dependabot-sheet   step 7: list the Dependabot records to read
    dependabot-result  step 7: write the counts as JSON

Run from the project root, for example:

    python src/classify/check_classification.py search \\
      --input data/processed/extraction_2026-09-25_full_v2.jsonl \\
      --sample docs/sample_eval_e2.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SCHEMA = ROOT / "config" / "requirement_schema_v2.json"
PULL_URL = "https://github.com/eclipse-qrisp/Qrisp/pull/{number}"

# G5 section 3, closed list, in the order of the decision.
KEYWORDS: tuple[str, ...] = (
    "secur", "vulnerab", "cve-", "ghsa-", "advisory", "exploit", "attack",
    "malicious", "tamper", "integrity", "authenti", "authoriz", "permission",
    "access control", "credential", "secret", "password", "api key", "api_key",
    "apikey", "token", "encrypt", "decrypt", "cryptograph", "checksum", "sha256",
    "privacy", "personal data", "confidential", "disclos", "leak", "audit",
    "untrusted", "sanitiz", "sanitis", "injection", "pickle", "deserializ",
    "deserialis", "eval(", "exec(", "subprocess", "shell=true", "arbitrary code",
    "denial of service", "resource exhaustion", "dependabot",
)
SEED = 20261005          # G5 sections 3, 4 and 5
CAP = 150                # G5 section 3
EXCERPT_ONLY_SAMPLE = 50  # G5 section 3

# G4 part 1 (variant normnah) and part 3.
TYPE_CODES = {
    "F": "functional_performance",
    "I": "interface",
    "P": "process",
    "Q": "quality_non_functional",
    "U": "usability_quality_in_use",
    "H": "human_factors",
}
KIND_OF_TYPE = {
    "functional_performance": "functional",
    "quality_non_functional": "non_functional",
    "usability_quality_in_use": "non_functional",
    "human_factors": "non_functional",
    "interface": "interface",
    "process": "process",
}
SECURITY_ANSWERS = ("ja", "nein", "unklar")
PURPOSES = ("1", "2", "3")                   # G4 part 2, Zweck 1 to 3
RULE_CODE = re.compile(r"^(GF[1-7]|TY[1-4])$")  # Grenzfallregel 1-7, Typregel 1-4
DEFINITION_ANSWERS = ("1", "2", "3", "4", "keine")  # G4, Abweichungen 1-4

DEPENDABOT_LOGIN = "dependabot[bot]"
VULNERABILITY_ID = ("cve-", "ghsa-")   # G5 section 7 a
SECURITY_WORDS = ("secur", "vulnerab")  # G5 section 7 b


class CheckError(Exception):
    """A violated precondition. The message never holds content."""


# --- reading ------------------------------------------------------------


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise CheckError(f"line {line_number} of {path} is not valid JSON") from error
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
                              capture_output=True, text=True).stdout.strip() or "unknown"
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def load_requirements(records: list[dict[str, Any]],
                      validator: Draft202012Validator) -> list[dict[str, Any]]:
    """Requirements of the records that pass the schema check (G1 point 1).

    Each requirement gets a key: its id, with a suffix ~2, ~3 ... if the
    same id occurs more than once in the run.
    """
    rows: list[dict[str, Any]] = []
    seen: Counter = Counter()
    for record in records:
        if any(True for _ in validator.iter_errors(record)):
            continue
        for requirement in record["requirements"]:
            seen[requirement["id"]] += 1
            key = requirement["id"] if seen[requirement["id"]] == 1 \
                else f"{requirement['id']}~{seen[requirement['id']]}"
            rows.append({"key": key, "pull": record["pull_number"], "req": requirement})
    return rows


def read_sample(path: Path) -> list[int]:
    """Pull request numbers of the table 'Drawn pull requests' (draw_sample.py)."""
    numbers: list[int] = []
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_table = line.strip() == "## Drawn pull requests"
            continue
        match = re.match(r"^\|\s*(\d+)\s*\|", line)
        if in_table and match:
            numbers.append(int(match.group(1)))
    if not numbers:
        raise CheckError(f"no drawn pull requests found in {path}")
    return numbers


# --- the three sets of G5 section 2 -------------------------------------


def keyword_hits(requirement: dict[str, Any]) -> tuple[set[str], set[str]]:
    """Keywords found in sentence or rationale, and in the excerpts (G5 section 3)."""
    prose = f"{requirement.get('text', '')}\n{requirement.get('rationale', '')}".lower()
    excerpts = "\n".join(item.get("excerpt", "")
                         for item in requirement.get("evidence", [])).lower()
    return ({word for word in KEYWORDS if word in prose},
            {word for word in KEYWORDS if word in excerpts})


def build_sets(rows: list[dict[str, Any]], sample_pulls: list[int]) -> dict[str, Any]:
    """Marked, search hits (all and checked), sample, and the sheet rows."""
    marked = {row["key"] for row in rows if row["req"]["security_relevant"]}
    per_keyword: Counter = Counter()
    prose_hits: set[str] = set()
    excerpt_only: set[str] = set()
    for row in rows:
        in_prose, in_excerpts = keyword_hits(row["req"])
        if row["key"] in marked or not (in_prose or in_excerpts):
            continue
        for word in in_prose | in_excerpts:
            per_keyword[word] += 1
        (prose_hits if in_prose else excerpt_only).add(row["key"])
    hits = prose_hits | excerpt_only
    cap_applied = len(hits) > CAP
    if cap_applied:
        chosen = random.Random(SEED).sample(sorted(excerpt_only),
                                            min(EXCERPT_ONLY_SAMPLE, len(excerpt_only)))
        checked = prose_hits | set(chosen)
    else:
        checked = set(hits)
    pulls = set(sample_pulls)
    sample = {row["key"] for row in rows if row["pull"] in pulls}
    order = sorted(marked | checked | sample)
    random.Random(SEED).shuffle(order)
    return {"marked": marked, "hits": hits, "prose_hits": prose_hits,
            "excerpt_only": excerpt_only, "checked": checked, "cap_applied": cap_applied,
            "sample": sample, "sample_pulls": sorted(pulls), "order": order,
            "per_keyword": dict(sorted(per_keyword.items()))}


def set_counts(sets: dict[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    pulls_with_requirements = {row["pull"] for row in rows if row["key"] in sets["sample"]}
    return {
        "requirements_in_base_set": len(rows),
        "marked": len(sets["marked"]),
        "search_hits_outside_marked": len(sets["hits"]),
        "of_which_in_sentence_or_rationale": len(sets["prose_hits"]),
        "of_which_only_in_excerpts": len(sets["excerpt_only"]),
        "cap_applied": sets["cap_applied"],
        "search_hits_checked": len(sets["checked"]),
        "sample_pull_requests": len(sets["sample_pulls"]),
        "sample_pull_requests_with_requirements": len(pulls_with_requirements),
        "sample_requirements": len(sets["sample"]),
        "sheet_rows": len(sets["order"]),
        "requirements_per_keyword": sets["per_keyword"],
    }


# --- sheet and answers --------------------------------------------------


def fence(text: str) -> str:
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def render_sheet(sets: dict[str, Any], by_key: dict[str, dict[str, Any]]) -> str:
    """Blind sheet: no type, no security label, no set, no model remarks (G5 5.1)."""
    lines = ["# Classification check sheet (G4, G5)", "",
             "Local file, contains pull request content. Do not paste into a chat.",
             "Fill in the answer file, not this sheet. Codes: see the answer file.", ""]
    for number, key in enumerate(sets["order"], start=1):
        row = by_key[key]
        req = row["req"]
        lines += [f"## {number}. {key} (PR {row['pull']})", "",
                  f"Link: {PULL_URL.format(number=row['pull'])}", "",
                  "Requirement:", "", f"{fence(req['text'])}text", req["text"],
                  fence(req["text"]), "",
                  "Rationale:", "", f"{fence(req['rationale'])}text", req["rationale"],
                  fence(req["rationale"]), "", "Evidence:", ""]
        for index, item in enumerate(req["evidence"], start=1):
            where = item["location"] + (f", {item['locator']}" if item.get("locator") else "")
            mark = fence(item["excerpt"])
            lines += [f"Excerpt {index} ({where}):", "", f"{mark}text", item["excerpt"],
                      mark, ""]
    return "\n".join(lines) + "\n"


ANSWER_HEADER = """# Answers for the classification check (G4, G5). One line per sheet entry.
# Fields: number | id | type | security | purpose | rule | note
# type:     F functional_performance, I interface, P process,
#           Q quality_non_functional, U usability_quality_in_use, H human_factors
# security: ja, nein or unklar
# purpose:  1, 2 or 3 (G4 Zweck), only when security is ja, otherwise empty
# rule:     empty, or GF1 to GF7 (Grenzfallregel) and TY1 to TY4 (Typregel),
#           several separated by commas
# note:     free text without the character |
"""


def render_answers(order: list[str]) -> str:
    return ANSWER_HEADER + "".join(f"{n} | {key} |  |  |  |  | \n"
                                   for n, key in enumerate(order, start=1))


def parse_answers(text: str, order: list[str]) -> tuple[dict[str, dict[str, str]], list[str]]:
    """Return the answers by key and a list of problems (line numbers only)."""
    answers: dict[str, dict[str, str]] = {}
    problems: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split("|")]
        if len(fields) < 7:
            problems.append(f"line {line_number}: fewer than 7 fields")
            continue
        number, key, kind, security, purpose, rule = fields[:6]
        if not number.isdigit() or not 1 <= int(number) <= len(order) \
                or order[int(number) - 1] != key:
            problems.append(f"line {line_number}: number and id do not match the sheet")
            continue
        if key in answers:
            problems.append(f"line {line_number}: entry {number} appears twice")
            continue
        if kind.upper() not in TYPE_CODES:
            problems.append(f"line {line_number}: type must be one of F I P Q U H")
        if security.lower() not in SECURITY_ANSWERS:
            problems.append(f"line {line_number}: security must be ja, nein or unklar")
        elif security.lower() == "ja" and purpose not in PURPOSES:
            problems.append(f"line {line_number}: security ja needs purpose 1, 2 or 3")
        elif security.lower() != "ja" and purpose:
            problems.append(f"line {line_number}: purpose only with security ja")
        codes = [code.strip().upper() for code in rule.split(",") if code.strip()]
        if any(not RULE_CODE.match(code) for code in codes):
            problems.append(f"line {line_number}: rule must be GF1-GF7 or TY1-TY4")
        answers[key] = {"type": TYPE_CODES.get(kind.upper(), ""),
                        "security": security.lower(), "purpose": purpose,
                        "rules": ",".join(codes)}
    missing = [n for n, key in enumerate(order, start=1) if key not in answers]
    if missing:
        problems.append(f"entries without an answer line: {len(missing)} "
                        f"(first: {missing[0]})")
    return answers, problems


def security_disagreements(order: list[str], answers: dict[str, dict[str, str]],
                           by_key: dict[str, dict[str, Any]]) -> list[tuple[int, str, str, str]]:
    """(number, key, model, author) where model and author differ; unklar never differs."""
    result = []
    for number, key in enumerate(order, start=1):
        author = answers[key]["security"]
        model = "ja" if by_key[key]["req"]["security_relevant"] else "nein"
        if author != "unklar" and author != model:
            result.append((number, key, model, author))
    return result


FOLLOW_UP_HEADER = """# Follow-up for disagreements on security relevance (G5 section 5, step 4).
# Do not change the answer file. Fill in only the field definition:
#   1, 2, 3 or 4 if the disagreement follows from Abweichung 1 to 4 of G4,
#   keine otherwise.
# Fields: number | id | model | author | definition
"""


def render_follow_up(disagreements: list[tuple[int, str, str, str]]) -> str:
    return FOLLOW_UP_HEADER + "".join(f"{n} | {key} | {model} | {author} | \n"
                                      for n, key, model, author in disagreements)


def parse_follow_up(text: str, disagreements: list[tuple[int, str, str, str]]
                    ) -> tuple[dict[str, str], list[str]]:
    expected = {key: (n, model, author) for n, key, model, author in disagreements}
    values: dict[str, str] = {}
    problems: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split("|")]
        if len(fields) < 5 or fields[1] not in expected \
                or fields[0] != str(expected[fields[1]][0]):
            problems.append(f"line {line_number}: not a disagreement of the compare step")
            continue
        if fields[1] in values:
            problems.append(f"line {line_number}: entry appears twice")
            continue
        if fields[4].lower() not in DEFINITION_ANSWERS:
            problems.append(f"line {line_number}: definition must be 1, 2, 3, 4 or keine")
        values[fields[1]] = fields[4].lower()
    if len(values) != len(expected):
        problems.append(f"disagreements without a line: {len(expected) - len(values)}")
    return values, problems


def tally(order: list[str], answers: dict[str, dict[str, str]],
          follow_up: dict[str, str], sets: dict[str, Any],
          by_key: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Counts of G5 section 6. Shares are left to the text of the thesis."""
    def security_block(keys: set[str]) -> dict[str, int]:
        block = Counter({"n": len(keys)})
        for key in keys:
            author = answers[key]["security"]
            model = bool(by_key[key]["req"]["security_relevant"])
            block[f"author_{author}"] += 1
            if model:
                block["model_true"] += 1
            if model and author == "ja":
                block["confirmed"] += 1
            if model and author == "nein":
                block["rejected"] += 1
                block["rejected_by_definition" if follow_up[key] != "keine"
                      else "rejected_misjudged"] += 1
            if not model and author == "ja":
                block["missed"] += 1
                block["missed_by_definition" if follow_up[key] != "keine"
                      else "missed_misjudged"] += 1
        names = ("n", "model_true", "author_ja", "author_nein", "author_unklar",
                 "confirmed", "rejected", "rejected_by_definition", "rejected_misjudged",
                 "missed", "missed_by_definition", "missed_misjudged")
        return {name: block[name] for name in names}

    sample = sets["sample"]
    confusion: dict[str, dict[str, int]] = {model: {author: 0 for author in TYPE_CODES.values()}
                                            for model in TYPE_CODES.values()}
    agree = kind_agree = 0
    for key in sample:
        model = by_key[key]["req"]["type"]
        author = answers[key]["type"]
        confusion[model][author] += 1
        agree += model == author
        kind_agree += KIND_OF_TYPE[model] == KIND_OF_TYPE[author]
    rules = Counter(code for key in order for code in answers[key]["rules"].split(",") if code)
    return {
        "security": {"marked": security_block(sets["marked"]),
                     "search_hits_checked": security_block(sets["checked"]),
                     "sample": security_block(sample)},
        "type_sample": {"n": len(sample), "type_agree": agree, "kind_agree": kind_agree,
                        "confusion_model_rows_author_columns": confusion},
        "rules_used_all_rows": dict(sorted(rules.items())),
    }


# --- Dependabot (G5 section 7) -------------------------------------------


def author_login(record: dict[str, Any]) -> str:
    author = record.get("author")
    return (author.get("login") if isinstance(author, dict) else author) or ""


def dependabot_records(dataset: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted((r for r in dataset if author_login(r) == DEPENDABOT_LOGIN
                   and r.get("outcome") != "open"), key=lambda r: r["number"])


def dependabot_text(record: dict[str, Any]) -> str:
    parts = [record.get("title") or "", record.get("body") or ""]
    for name in ("issue_comments", "review_comments"):
        parts += [comment.get("body") or "" for comment in record.get(name) or []]
    return "\n".join(parts)


def dependabot_classes(records: list[dict[str, Any]]) -> dict[int, str]:
    """id (7 a), word (7 b) or none, per pull request number."""
    classes = {}
    for record in records:
        text = dependabot_text(record).lower()
        if any(mark in text for mark in VULNERABILITY_ID):
            classes[record["number"]] = "id"
        elif any(word in text for word in SECURITY_WORDS):
            classes[record["number"]] = "word"
        else:
            classes[record["number"]] = "none"
    return classes


def render_dependabot_sheet(records: list[dict[str, Any]], classes: dict[int, str]) -> str:
    lines = ["# Dependabot review sheet (G5 section 7 b)", "",
             "Local file, contains pull request content. Do not paste into a chat.",
             "Question: does the text name a vulnerability that the update fixes?", ""]
    for record in records:
        if classes[record["number"]] != "word":
            continue
        text = dependabot_text(record)
        mark = fence(text)
        lines += [f"## PR {record['number']} ({record.get('outcome')})", "",
                  f"Link: {PULL_URL.format(number=record['number'])}", "",
                  f"{mark}text", text, mark, ""]
    return "\n".join(lines) + "\n"


DEPENDABOT_HEADER = """# Answers for the Dependabot review (G5 section 7 b).
# Fields: PR | answer   with answer ja, nein or unklar
"""


def dependabot_counts(records: list[dict[str, Any]], classes: dict[int, str],
                      answers: dict[int, str] | None) -> dict[str, Any]:
    by_outcome: dict[str, Counter] = {}
    for record in records:
        cell = by_outcome.setdefault(record.get("outcome", "unknown"), Counter())
        cls = classes[record["number"]]
        cell["records"] += 1
        cell[f"class_{cls}"] += 1
        if answers is not None and cls == "word":
            cell[f"word_answer_{answers[record['number']]}"] += 1
        if cls == "id" or (answers is not None and cls == "word"
                           and answers[record["number"]] == "ja"):
            cell["hints"] += 1
    names = ["records", "class_id", "class_word", "class_none"]
    if answers is not None:
        names += ["word_answer_ja", "word_answer_nein", "word_answer_unklar", "hints"]
    rows = {outcome: {name: cell[name] for name in names}
            for outcome, cell in sorted(by_outcome.items())}
    rows["total"] = {name: sum(row[name] for row in rows.values()) for name in names}
    return rows


def parse_dependabot_answers(text: str, expected: set[int]) -> tuple[dict[int, str], list[str]]:
    answers: dict[int, str] = {}
    problems: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split("|")]
        if len(fields) < 2 or not fields[0].isdigit() or int(fields[0]) not in expected:
            problems.append(f"line {line_number}: not a pull request of the sheet")
            continue
        if int(fields[0]) in answers:
            problems.append(f"line {line_number}: pull request appears twice")
            continue
        if fields[1].lower() not in SECURITY_ANSWERS:
            problems.append(f"line {line_number}: answer must be ja, nein or unklar")
        answers[int(fields[0])] = fields[1].lower()
    if len(answers) != len(expected):
        problems.append(f"pull requests without an answer: {len(expected) - len(answers)}")
    return answers, problems


# --- command line -------------------------------------------------------


def print_counts(value: Any, prefix: str = "") -> None:
    for key, item in value.items():
        if isinstance(item, dict):
            print(f"{prefix}{key}:")
            print_counts(item, prefix + "  ")
        else:
            print(f"{prefix}{key}: {item}")


def refuse_existing(*paths: Path) -> None:
    existing = [str(path) for path in paths if path.exists()]
    if existing:
        raise CheckError("refusing to overwrite: " + ", ".join(existing))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def prepare(arguments: argparse.Namespace) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    schema = json.loads(Path(arguments.schema).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    rows = load_requirements(read_jsonl(Path(arguments.input)), Draft202012Validator(schema))
    return rows, build_sets(rows, read_sample(Path(arguments.sample)))


def input_hashes(arguments: argparse.Namespace) -> dict[str, str]:
    return {name: sha256_of(Path(getattr(arguments, name)))
            for name in ("input", "sample", "schema")}


def command_search(arguments: argparse.Namespace) -> int:
    rows, sets = prepare(arguments)
    print_counts(set_counts(sets, rows))
    return 0


def paths_in(directory: Path) -> dict[str, Path]:
    return {"sheet": directory / "sheet.md", "answers": directory / "answers.txt",
            "manifest": directory / "sheet_manifest.json",
            "lock": directory / "answers_lock.json", "follow_up": directory / "follow_up.txt"}


def command_sheet(arguments: argparse.Namespace) -> int:
    paths = paths_in(Path(arguments.out_dir))
    refuse_existing(paths["sheet"], paths["answers"], paths["manifest"])
    rows, sets = prepare(arguments)
    by_key = {row["key"]: row for row in rows}
    Path(arguments.out_dir).mkdir(parents=True, exist_ok=True)
    paths["sheet"].write_text(render_sheet(sets, by_key), encoding="utf-8")
    paths["answers"].write_text(render_answers(sets["order"]), encoding="utf-8")
    write_json(paths["manifest"], {"order": sets["order"], "inputs": input_hashes(arguments),
                                   "code_commit": git_commit(), "seed": SEED})
    print_counts(set_counts(sets, rows))
    print(f"sheet entries written: {len(sets['order'])}")
    return 0


def load_checked_state(arguments: argparse.Namespace):
    paths = paths_in(Path(arguments.out_dir))
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    if manifest["inputs"] != input_hashes(arguments):
        raise CheckError("inputs differ from those of the sheet (checksums)")
    rows, sets = prepare(arguments)
    if sets["order"] != manifest["order"]:
        raise CheckError("sheet order cannot be reproduced")
    by_key = {row["key"]: row for row in rows}
    answers, problems = parse_answers(paths["answers"].read_text(encoding="utf-8"),
                                      sets["order"])
    return paths, rows, sets, by_key, answers, problems


def command_compare(arguments: argparse.Namespace) -> int:
    paths = paths_in(Path(arguments.out_dir))
    refuse_existing(paths["lock"], paths["follow_up"])
    paths, _rows, sets, by_key, answers, problems = load_checked_state(arguments)
    if problems:
        for problem in problems:
            print(problem)
        print(f"answers not complete: {len(problems)} problem(s). Nothing written.")
        return 1
    disagreements = security_disagreements(sets["order"], answers, by_key)
    type_differs = sum(1 for key in sets["sample"]
                       if answers[key]["type"] != by_key[key]["req"]["type"])
    write_json(paths["lock"], {"answers_sha256": sha256_of(paths["answers"])})
    paths["follow_up"].write_text(render_follow_up(disagreements), encoding="utf-8")
    print(f"answers complete: {len(answers)}")
    print(f"security disagreements: {len(disagreements)}")
    for number, key, model, author in disagreements:
        print(f"  {number} {key} model={model} author={author}")
    print(f"type disagreements in the sample: {type_differs}")
    return 0


def command_result(arguments: argparse.Namespace) -> int:
    output = Path(arguments.output)
    refuse_existing(output)
    paths, rows, sets, by_key, answers, problems = load_checked_state(arguments)
    if problems:
        raise CheckError(f"answers not complete: {len(problems)} problem(s)")
    lock = json.loads(paths["lock"].read_text(encoding="utf-8"))
    if lock["answers_sha256"] != sha256_of(paths["answers"]):
        raise CheckError("answer file changed after the compare step")
    disagreements = security_disagreements(sets["order"], answers, by_key)
    follow_up, problems = parse_follow_up(paths["follow_up"].read_text(encoding="utf-8"),
                                          disagreements)
    if problems:
        for problem in problems:
            print(problem)
        raise CheckError(f"follow-up not complete: {len(problems)} problem(s)")
    result = {
        "rules": "docs/entscheidungen.md: G4 and G5",
        "code_commit": git_commit(),
        "inputs": {name: {"path": getattr(arguments, name), "sha256": value}
                   for name, value in input_hashes(arguments).items()},
        "files": {name: sha256_of(paths[name])
                  for name in ("sheet", "answers", "follow_up")},
        "sets": set_counts(sets, rows),
        "counts": tally(sets["order"], answers, follow_up, sets, by_key),
    }
    write_json(output, result)
    print_counts(result["counts"])
    print(f"written: {output}")
    return 0


def command_dependabot_sheet(arguments: argparse.Namespace) -> int:
    directory = Path(arguments.out_dir)
    sheet, answers = directory / "dependabot_sheet.md", directory / "dependabot_answers.txt"
    refuse_existing(sheet, answers)
    records = dependabot_records(read_jsonl(Path(arguments.dataset)))
    classes = dependabot_classes(records)
    directory.mkdir(parents=True, exist_ok=True)
    sheet.write_text(render_dependabot_sheet(records, classes), encoding="utf-8")
    answers.write_text(DEPENDABOT_HEADER + "".join(
        f"{r['number']} | \n" for r in records if classes[r["number"]] == "word"),
        encoding="utf-8")
    print_counts(dependabot_counts(records, classes, None))
    return 0


def command_dependabot_result(arguments: argparse.Namespace) -> int:
    output = Path(arguments.output)
    refuse_existing(output)
    directory = Path(arguments.out_dir)
    records = dependabot_records(read_jsonl(Path(arguments.dataset)))
    classes = dependabot_classes(records)
    expected = {number for number, cls in classes.items() if cls == "word"}
    answer_file = directory / "dependabot_answers.txt"
    answers, problems = parse_dependabot_answers(answer_file.read_text(encoding="utf-8"),
                                                 expected)
    if problems:
        for problem in problems:
            print(problem)
        raise CheckError(f"answers not complete: {len(problems)} problem(s)")
    counts = dependabot_counts(records, classes, answers)
    write_json(output, {"rules": "docs/entscheidungen.md: G5 section 7",
                        "code_commit": git_commit(),
                        "inputs": {"dataset": {"path": arguments.dataset,
                                               "sha256": sha256_of(Path(arguments.dataset))}},
                        "files": {"answers": sha256_of(answer_file),
                                  "sheet": sha256_of(directory / "dependabot_sheet.md")},
                        "counts": counts})
    print_counts(counts)
    print(f"written: {output}")
    return 0


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manual check of the classification "
                                     "(G4, G5). Prints numbers and identifiers only.")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_run(name: str, out_dir: bool, output: bool) -> None:
        command = sub.add_parser(name)
        command.add_argument("--input", required=True, help="Extraction output, JSONL.")
        command.add_argument("--sample", required=True, help="Sample file of draw_sample.py.")
        command.add_argument("--schema", default=str(DEFAULT_SCHEMA))
        if out_dir:
            command.add_argument("--out-dir", required=True,
                                 help="Directory under eval/responses/.")
        if output:
            command.add_argument("--output", required=True, help="Result JSON, never overwritten.")

    add_run("search", False, False)
    add_run("sheet", True, False)
    add_run("compare", True, False)
    add_run("result", True, True)
    for name, output in (("dependabot-sheet", False), ("dependabot-result", True)):
        command = sub.add_parser(name)
        command.add_argument("--dataset", required=True, help="Prepared dataset, JSONL.")
        command.add_argument("--out-dir", required=True, help="Directory under eval/responses/.")
        if output:
            command.add_argument("--output", required=True, help="Result JSON, never overwritten.")
    return parser.parse_args(argv)


COMMANDS = {"search": command_search, "sheet": command_sheet, "compare": command_compare,
            "result": command_result, "dependabot-sheet": command_dependabot_sheet,
            "dependabot-result": command_dependabot_result}


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    try:
        return COMMANDS[arguments.command](arguments)
    except CheckError as error:
        print(f"Stopped: {error}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
