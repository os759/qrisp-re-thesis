"""Gap analysis of the security grid, decision G6.

Work package G, step 8. Research question FF4.

All rules are fixed in docs/entscheidungen.md before the analysis:

* G2: the grid SR01 to SR29; SR07 and SR08 are category 4.
* G1: base set and evidence strength for FF4 (found evidence only). The
  strength comes from count_requirements.py, which holds no check rule
  of its own; this script adds none either.
* G6: candidates (keyword, process, security), cap 200, blind matching
  sheet, categories 1 to 3, counter-check that only lowers.

Nothing of a requirement text, rationale, excerpt, title or comment is
printed or written to the result file. Only counts, grid entries and
requirement identifiers. Sheets and answers contain pull request content
and belong under eval/responses/, which git ignores.

Sub-commands, in this order:

    sheet    count the candidates, write the matching sheet and answer file
    compare  check and lock the answers, write round 1 of the counter-check
    next     check a completed counter-check round, write the next if needed
    result   write the counts of G6 section 8 as JSON

Run from the project root, for example:

    python src/analyze/gap_analysis.py sheet \\
      --input data/processed/extraction_2026-09-25_full_v2.jsonl \\
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \\
      --model-input data/processed/model_input_2026-09-19.jsonl \\
      --mentions-map data/interim/mention_map.json \\
      --allowlist "jaspify,jax,pytest,rus" \\
      --g5-answers eval/responses/classification_check_2026-10-06/answers.txt \\
      --g5-result experiments/classification_check_2026-10-06.json \\
      --out-dir eval/responses/gap_analysis_2026-10-06
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
for _path in (HERE, HERE.parent / "classify"):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from jsonschema import Draft202012Validator  # noqa: E402

import count_requirements as cr  # noqa: E402
from check_classification import (CheckError, fence, git_commit,  # noqa: E402
                                  load_requirements, print_counts,
                                  refuse_existing, sha256_of, write_json)

PULL_URL = "https://github.com/eclipse-qrisp/Qrisp/pull/{number}"
SEED = 20261005           # G6 sections 2 and 4
CAP = 200                 # G6 section 2
EXCERPT_ONLY_SAMPLE = 50  # G6 section 2, stage 1
CHECKS_PER_ROUND = 3      # G6 section 6

# G2, relevant entries: number -> (source, short form, level). Own words.
GRID: dict[str, tuple[str, str, str]] = {
    "SR01": ("29148 9.6.18 c 1", "bestimmte kryptografische Verfahren einsetzen", "Beispiel"),
    "SR02": ("29148 9.6.18 c 2", "bestimmte Protokoll- oder Verlaufsdaten fuehren", "Beispiel"),
    "SR03": ("29148 9.6.18 c 3", "bestimmte Funktionen verschiedenen Modulen zuweisen",
             "Beispiel"),
    "SR04": ("29148 9.6.18 c 4", "Kommunikation zwischen Programmteilen begrenzen", "Beispiel"),
    "SR05": ("29148 9.6.18 c 5", "Integritaet kritischer Variablen pruefen", "Beispiel"),
    "SR06": ("29148 9.6.18 c 6", "Datenschutz sicherstellen", "Beispiel"),
    "SR09": ("29148 9.6.17 d", "Verarbeitungsschritte nachverfolgbar machen",
             "Inhaltsvorgabe"),
    "SR10": ("TR GV.01", "Beitragsregeln dokumentieren; erwartete Qualitaet angeben",
             "MUST; Zusatz SHOULD"),
    "SR11": ("TR GV.02", "Repository, Webseiten und sensible Daten vor unbefugten "
             "Handlungen schuetzen", "MUST"),
    "SR12": ("TR LE.01", "Lizenz fuer alle Inhalte angeben, auch fuer die Dokumentation",
             "MUST"),
    "SR13": ("TR LE.02", "Lizenztexte oder Verweise darauf bereitstellen", "MUST"),
    "SR14": ("TR QA.01", "Liste der Fremdkomponenten bereitstellen", "MUST"),
    "SR15": ("TR QA.02", "gesamten Quelltext oeffentlich lesbar machen", "MUST"),
    "SR16": ("TR QA.03", "beschreiben, wie Fehler gemeldet werden", "MUST"),
    "SR17": ("TR QA.04", "Testverfahren einrichten und nutzen", "MUST"),
    "SR18": ("TR QA.05", "Speichersicherheitsfehler vermeiden oder verringern", "SHOULD"),
    "SR19": ("TR QA.06", "alle Aenderungen am Quelltext begutachten lassen", "SHOULD"),
    "SR20": ("TR BR.01", "Bauanleitung fuer alle Bestandteile oeffentlich machen", "MUST"),
    "SR21": ("TR BR.02", "eindeutige, stetig steigende Versionskennungen vergeben", "MUST"),
    "SR22": ("TR BR.03", "bei der Verteilung Integritaet wahren oder pruefbar machen; "
             "Echtheit", "MUST; Zusatz MAY"),
    "SR23": ("TR BR.04", "je Veroeffentlichung Aenderungen an Funktion und Sicherheit "
             "protokollieren", "MUST"),
    "SR24": ("TR BR.05", "Quellpakete enthalten nur Inhalte aus dem Repository",
             "MUST NOT"),
    "SR25": ("TR BR.06", "Builds reproduzierbar machen", "SHOULD"),
    "SR26": ("TR VM.01", "Sicherheitskontakt dokumentieren; vertrauliches Melden "
             "ermoeglichen", "MUST; Zusatz SHOULD"),
    "SR27": ("TR VM.02", "entdeckte Schwachstellen in angemessener Frist veroeffentlichen",
             "MUST"),
    "SR28": ("TR DE.01", "Einstellung des Projekts oder von Teilen mitteilen", "SHOULD"),
    "SR29": ("TR DE.02", "Migrationswege aufzeigen", "MAY"),
}
NOT_RELEVANT = ("SR07", "SR08")  # G2 rule 3, category 4
PRODUCT = tuple(f"SR{n:02d}" for n in range(1, 10))

# G6 section 3, closed list. Searched all at once.
KEYWORDS_BY_ENTRY: dict[str, tuple[str, ...]] = {
    "SR01": ("cryptograph", "encrypt", "decrypt", "cipher", "tls", "hashlib", "sha256"),
    "SR02": ("audit", "logging", "logger", "log file"),
    "SR03": ("separation of", "privilege", "sandbox", "isolat"),
    "SR04": ("sandbox", "isolat", "information flow", "restrict access"),
    "SR05": ("integrity", "checksum", "tamper", "corrupt"),
    "SR06": ("privacy", "personal data", "gdpr", "anonymi", "pseudonym", "confidential"),
    "SR09": ("traceab", "provenance", "audit trail"),
    "SR10": ("contribut", "code of conduct", "guideline", "style guide", "coding standard",
             "pre-commit", "lint"),
    "SR11": ("branch protection", "permission", "access control", "secret", "credential",
             "token", "password", "two-factor", "2fa", "authenti", "authoriz"),
    "SR12": ("licen", "spdx", "copyright"),
    "SR13": ("licen", "spdx", "copyright"),
    "SR14": ("requirements.txt", "pyproject", "setup.py", "setup.cfg", "third-party",
             "third party", "sbom"),
    "SR15": ("open source", "open-source", "publicly"),
    "SR16": ("bug report", "issue template", "report a bug", "report bugs", "issue tracker"),
    "SR17": ("pytest", "unit test", "test suite", "continuous integration", "github action",
             "workflow"),
    "SR18": ("memory safe", "memory leak", "buffer overflow", "out of bounds", "out-of-bounds",
             "segfault", "segmentation fault", "use after free", "use-after-free"),
    "SR19": ("review", "approv"),
    "SR20": ("installation", "pip install", "build instruction", "sdist", "wheel"),
    "SR21": ("versioning", "version number", "__version__", "semantic version", "semver",
             "release"),
    "SR22": ("pypi", "publish", "gpg", "sigstore", "code signing", "checksum", "sha256"),
    "SR23": ("changelog", "change log", "release note"),
    "SR24": ("sdist", "manifest.in", "package_data", "package data"),
    "SR25": ("reproducib", "lock file", "lockfile", "pinned"),
    "SR26": ("security.md", "security policy", "security contact", "responsible disclosure",
             "vulnerab"),
    "SR27": ("vulnerab", "advisory", "cve-", "ghsa-", "security fix"),
    "SR28": ("deprecat", "discontinu", "end of life", "end-of-life", "unmaintained",
             "no longer supported"),
    "SR29": ("migrat", "breaking change", "backward compat", "backwards compat",
             "upgrade guide"),
}
KEYWORDS: tuple[str, ...] = tuple(sorted({w for ws in KEYWORDS_BY_ENTRY.values() for w in ws}))

MATCH_ANSWERS = ("ja", "teilweise", "unklar")
STRENGTHS = ("direct", "indirect", "insufficient")


# --- rows and candidates (G6 sections 1 and 2) ---------------------------


def requirement_rows(records: list[dict[str, Any]], validator: Draft202012Validator,
                     dataset: dict[int, dict[str, Any]], blocks: dict[int, str],
                     mapping: dict[str, str] | None, allowlist: set[str]
                     ) -> list[dict[str, Any]]:
    """Base set of G1 point 1 with the strength for FF4 (G1 point 3).

    Keys as in check_classification.py, so the G5 answers can be joined.
    """
    rows = load_requirements(records, validator)
    for row in rows:
        pull = dataset.get(row["pull"])
        shown = cr.files_in_block(blocks.get(row["pull"], ""))
        flags = [cr.evidence_status(item, pull, shown, mapping, allowlist)[0]
                 for item in row["req"]["evidence"]]
        row["found"] = flags
        row["strength"] = cr.assess_requirement(row["req"], flags)["strength_ff4"]
    return rows


def keyword_hits(requirement: dict[str, Any]) -> tuple[set[str], set[str]]:
    """Keywords in sentence or rationale, and in the excerpts."""
    prose = f"{requirement.get('text', '')}\n{requirement.get('rationale', '')}".lower()
    excerpts = "\n".join(item.get("excerpt", "")
                         for item in requirement.get("evidence", [])).lower()
    return ({w for w in KEYWORDS if w in prose}, {w for w in KEYWORDS if w in excerpts})


def read_g5_security(text: str) -> set[str]:
    """Keys the author judged security relevant (ja) in the G5 answer file."""
    keys = set()
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split("|")]
        if len(fields) >= 4 and fields[3].lower() == "ja":
            keys.add(fields[1])
    return keys


def build_candidates(rows: list[dict[str, Any]], g5_ja: set[str]) -> dict[str, Any]:
    """The three subsets, the cap of G6 section 2 and the sheet order."""
    keys = {row["key"] for row in rows}
    unknown = g5_ja - keys
    if unknown:
        raise CheckError(f"G5 answers name {len(unknown)} key(s) outside the base set")
    prose: set[str] = set()
    excerpt: set[str] = set()
    for row in rows:
        in_prose, in_excerpts = keyword_hits(row["req"])
        if in_prose:
            prose.add(row["key"])
        elif in_excerpts:
            excerpt.add(row["key"])
    process = {row["key"] for row in rows if row["req"]["type"] == "process"}
    security = {row["key"] for row in rows if row["req"]["security_relevant"]} | g5_ja
    protected = process | security
    union = prose | excerpt | protected
    chosen, stage = set(union), 0
    if len(protected) > CAP:
        raise CheckError("process and security candidates alone exceed the cap")
    if len(chosen) > CAP:
        stage = 1
        free = sorted(excerpt - protected)
        drawn = set(random.Random(SEED).sample(free, min(EXCERPT_ONLY_SAMPLE, len(free))))
        chosen = protected | (prose - protected) | drawn
        if len(chosen) > CAP:
            stage = 2
            pool = sorted(chosen - protected)
            chosen = protected | set(random.Random(SEED).sample(pool, CAP - len(protected)))
    order = sorted(chosen)
    random.Random(SEED).shuffle(order)
    return {"prose": prose, "excerpt_only": excerpt, "process": process,
            "security": security, "union": union, "order": order, "cap_stage": stage}


def candidate_counts(cands: dict[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "requirements_in_base_set": len(rows),
        "strength_ff4_base_set": dict(sorted(Counter(r["strength"] for r in rows).items())),
        "keyword_in_sentence_or_rationale": len(cands["prose"]),
        "keyword_only_in_excerpts": len(cands["excerpt_only"]),
        "process": len(cands["process"]),
        "security": len(cands["security"]),
        "union": len(cands["union"]),
        "cap_stage": cands["cap_stage"],
        "sheet_rows": len(cands["order"]),
    }


# --- matching sheet and answers (G6 section 4) ---------------------------


def render_grid() -> list[str]:
    lines = ["## Raster (G2), relevante Eintraege", "",
             "| Nr. | Quelle | Kurzform | Stufe |", "|---|---|---|---|"]
    lines += [f"| {n} | {s} | {k} | {lvl} |" for n, (s, k, lvl) in GRID.items()]
    return lines + ["", "Kern: bei TR-Eintraegen der Teil vor \"Zusatz\", bei 29148 die "
                        "ganze Kurzform (G6 Punkt 4).", ""]


def render_requirement(number: int, row: dict[str, Any], found_only: bool) -> list[str]:
    req = row["req"]
    lines = [f"## {number}. {row['key']} (PR {row['pull']})", "",
             f"Link: {PULL_URL.format(number=row['pull'])}", "",
             "Requirement:", "", f"{fence(req['text'])}text", req["text"], fence(req["text"]),
             ""]
    if not found_only:
        lines += ["Rationale:", "", f"{fence(req['rationale'])}text", req["rationale"],
                  fence(req["rationale"]), ""]
    lines += ["Evidence:", ""]
    for index, (item, found) in enumerate(zip(req["evidence"], row["found"]), start=1):
        if found_only and not found:
            continue
        where = item["location"] + (f", {item['locator']}" if item.get("locator") else "")
        mark = fence(item["excerpt"])
        lines += [f"Excerpt {index} ({where}):", "", f"{mark}text", item["excerpt"], mark, ""]
    return lines


def render_sheet(order: list[str], by_key: dict[str, dict[str, Any]]) -> str:
    """Blind: no model label, no strength, no found flag, no subset, no keyword."""
    lines = ["# Gap analysis matching sheet (G6)", "",
             "Local file, contains pull request content. Do not paste into a chat.",
             "Fill in the answer file, not this sheet.", ""] + render_grid()
    for number, key in enumerate(order, start=1):
        lines += render_requirement(number, by_key[key], found_only=False)
    return "\n".join(lines) + "\n"


ANSWER_HEADER = """# Answers for the gap analysis (G6 section 4). One line per sheet entry.
# Fields: number | id | entries | note
# entries: keine, or a comma separated list like  SR17:ja, SR19:teilweise, SR10:unklar
#          entries are SR01 to SR29 without SR07 and SR08; each at most once
# note:    free text without the character |
"""


def render_answers(order: list[str]) -> str:
    return ANSWER_HEADER + "".join(f"{n} | {key} |  | \n" for n, key in enumerate(order, 1))


def parse_entries(field: str) -> tuple[dict[str, str] | None, str | None]:
    if field.lower() == "keine":
        return {}, None
    if not field:
        return None, "entries empty (write keine if nothing fits)"
    result: dict[str, str] = {}
    for token in (t.strip() for t in field.split(",")):
        entry, _, answer = (part.strip() for part in token.partition(":"))
        entry, answer = entry.upper(), answer.lower()
        if entry not in GRID:
            return None, "unknown or not relevant grid entry"
        if answer not in MATCH_ANSWERS:
            return None, "answer must be ja, teilweise or unklar"
        if entry in result:
            return None, "grid entry named twice"
        result[entry] = answer
    return result, None


def parse_answers(text: str, order: list[str]) -> tuple[dict[str, dict[str, str]], list[str]]:
    answers: dict[str, dict[str, str]] = {}
    problems: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split("|")]
        if len(fields) < 4:
            problems.append(f"line {line_number}: fewer than 4 fields")
            continue
        number, key, entries = fields[:3]
        if not number.isdigit() or not 1 <= int(number) <= len(order) \
                or order[int(number) - 1] != key:
            problems.append(f"line {line_number}: number and id do not match the sheet")
            continue
        if key in answers:
            problems.append(f"line {line_number}: entry {number} appears twice")
            continue
        parsed, problem = parse_entries(entries)
        if problem:
            problems.append(f"line {line_number}: {problem}")
            continue
        answers[key] = parsed
    missing = [n for n, key in enumerate(order, start=1) if key not in answers]
    if missing:
        problems.append(f"entries without a valid line: {len(missing)} (first: {missing[0]})")
    return answers, problems


# --- categories and counter-check (G6 sections 5 and 6) ------------------


def lowered(strength: str, check: dict[str, str] | None) -> str:
    """G6 section 6: lowers only, never raises."""
    if check is None:
        return strength
    if check["carries"] == "nein":
        return "insufficient"
    if check["form"] == "berichtend" and strength == "direct":
        return "indirect"
    return strength


def contribution(answer: str, strength: str) -> int:
    """Category a single match supports (G6 section 5)."""
    if answer == "ja" and strength == "direct":
        return 1
    if (answer == "ja" and strength == "indirect") or \
            (answer == "teilweise" and strength in ("direct", "indirect")):
        return 2
    return 3


def matches_by_entry(answers: dict[str, dict[str, str]],
                     strengths: dict[str, str]) -> dict[str, list[tuple[str, str, str]]]:
    """entry -> [(key, answer, strength)], unklar included."""
    result: dict[str, list[tuple[str, str, str]]] = {entry: [] for entry in GRID}
    for key, entries in answers.items():
        for entry, answer in entries.items():
            result[entry].append((key, answer, strengths[key]))
    return result


def priority(match: tuple[str, str, str]) -> tuple[int, int, str]:
    key, answer, strength = match
    return (0 if answer == "ja" else 1, 0 if strength == "direct" else 1, key)


def assess_entries(matches: dict[str, list[tuple[str, str, str]]],
                   checks: dict[str, dict[str, str]]) -> dict[str, dict[str, Any]]:
    """Category per entry after the counter-check, and pending checks."""
    result = {}
    for entry, items in matches.items():
        effective = [(key, answer, lowered(strength, checks.get(key)))
                     for key, answer, strength in items]
        category = min((contribution(a, s) for _, a, s in effective), default=3)
        verified = [key for key, a, s in effective
                    if key in checks and contribution(a, s) == category]
        pending: list[str] = []
        if category < 3 and not verified:
            open_items = sorted((m for m in effective
                                 if m[0] not in checks and contribution(m[1], m[2]) == category),
                                key=priority)
            pending = [key for key, _, _ in open_items[:CHECKS_PER_ROUND]]
        result[entry] = {"category": category, "verified": sorted(verified),
                         "pending": pending, "effective": effective}
    return result


def all_pending(assessed: dict[str, dict[str, Any]]) -> list[str]:
    return sorted({key for value in assessed.values() for key in value["pending"]})


COUNTER_HEADER = """# Counter-check round {round} (G6 section 6). One line per sheet entry.
# Fields: number | id | carries | form
# carries: ja if a shown excerpt carries the system response of the sentence, else nein
# form:    fordernd or berichtend for that excerpt; leave empty when carries is nein
"""


def render_counter(keys: list[str], by_key: dict[str, dict[str, Any]], round_no: int
                   ) -> tuple[str, str]:
    lines = [f"# Gap analysis counter-check sheet, round {round_no} (G6)", "",
             "Local file, contains pull request content. Do not paste into a chat.",
             "Only excerpts found in the pull request are shown.", ""]
    for number, key in enumerate(keys, start=1):
        lines += render_requirement(number, by_key[key], found_only=True)
    answers = COUNTER_HEADER.format(round=round_no) + "".join(
        f"{n} | {key} |  | \n" for n, key in enumerate(keys, start=1))
    return "\n".join(lines) + "\n", answers


def parse_counter(text: str, keys: list[str]) -> tuple[dict[str, dict[str, str]], list[str]]:
    checks: dict[str, dict[str, str]] = {}
    problems: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split("|")]
        if len(fields) < 4 or not fields[0].isdigit() \
                or not 1 <= int(fields[0]) <= len(keys) or keys[int(fields[0]) - 1] != fields[1]:
            problems.append(f"line {line_number}: number and id do not match the sheet")
            continue
        key, carries, form = fields[1], fields[2].lower(), fields[3].lower()
        if key in checks:
            problems.append(f"line {line_number}: entry appears twice")
            continue
        if carries not in ("ja", "nein"):
            problems.append(f"line {line_number}: carries must be ja or nein")
        elif carries == "ja" and form not in ("fordernd", "berichtend"):
            problems.append(f"line {line_number}: form must be fordernd or berichtend")
        elif carries == "nein" and form:
            problems.append(f"line {line_number}: form only with carries ja")
        checks[key] = {"carries": carries, "form": form}
    if len(checks) != len(keys):
        problems.append(f"entries without a line: {len(keys) - len(checks)}")
    return checks, problems


# --- result (G6 section 8) ------------------------------------------------


def tally(assessed: dict[str, dict[str, Any]], matches: dict[str, list[tuple[str, str, str]]],
          checks: dict[str, dict[str, str]], g5_ja: set[str],
          answers: dict[str, dict[str, str]]) -> dict[str, Any]:
    entries: dict[str, Any] = {}
    for entry, value in assessed.items():
        original = matches[entry]
        cell = {f"{a}_{s}": 0 for a in ("ja", "teilweise") for s in STRENGTHS}
        for _, answer, strength in value["effective"]:
            if answer != "unklar":
                cell[f"{answer}_{strength}"] += 1
        lowered_count = sum(1 for (k, a, s), (_, _, e) in zip(original, value["effective"])
                            if s != e)
        real = [m for m in value["effective"] if m[1] != "unklar"]
        if value["category"] < 3:
            detail = None
        elif not real:
            detail = "no_match"
        else:
            detail = "only_insufficient"
        entries[entry] = {"category": value["category"], "category_3_detail": detail,
                          "matches_after_counter_check": cell,
                          "unklar": sum(1 for m in original if m[1] == "unklar"),
                          "lowered_by_counter_check": lowered_count,
                          "deciding": value["verified"]}
    for entry in NOT_RELEVANT:
        entries[entry] = {"category": 4}
    entries = dict(sorted(entries.items()))

    def sums(names: list[str]) -> dict[str, int]:
        counts = Counter(entries[n]["category"] for n in names)
        return {str(c): counts.get(c, 0) for c in (1, 2, 3, 4)}

    product = [n for n in entries if n in PRODUCT]
    process = [n for n in entries if n not in PRODUCT]
    matched = {key for key, value in answers.items()
               if any(a in ("ja", "teilweise") for a in value.values())}
    return {
        "entries": entries,
        "categories": {"product_SR01_SR09": sums(product),
                       "process_SR10_SR29": sums(process), "all": sums(list(entries))},
        "counter_check": {"checked": len(checks),
                          "carries_nein": sum(1 for c in checks.values() if c["carries"] == "nein"),
                          "berichtend": sum(1 for c in checks.values() if c["form"] == "berichtend")},
        "explorative": {"g5_security_ja": len(g5_ja),
                        "g5_security_ja_without_grid_entry": len(g5_ja - matched),
                        "g5_security_ja_not_on_sheet": len(g5_ja - set(answers))},
    }


# --- command line ---------------------------------------------------------


def paths_in(directory: Path) -> dict[str, Path]:
    return {"sheet": directory / "sheet.md", "answers": directory / "answers.txt",
            "manifest": directory / "sheet_manifest.json", "lock": directory / "lock.json"}


def counter_paths(directory: Path, round_no: int) -> tuple[Path, Path]:
    return (directory / f"counter_{round_no}.md", directory / f"counter_{round_no}.txt")


def input_hashes(arguments: argparse.Namespace) -> dict[str, str]:
    names = ("input", "dataset", "model_input", "schema", "g5_answers", "g5_result")
    hashes = {name: sha256_of(Path(getattr(arguments, name))) for name in names}
    if arguments.mentions_map:
        hashes["mentions_map"] = sha256_of(Path(arguments.mentions_map))
    return hashes


def load_rows(arguments: argparse.Namespace) -> list[dict[str, Any]]:
    schema = json.loads(Path(arguments.schema).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    mapping = cr.load_mapping(Path(arguments.mentions_map)) if arguments.mentions_map else None
    allowlist = {n.strip().lower() for n in arguments.allowlist.split(",") if n.strip()}
    records = [record for _, record in cr.read_jsonl(Path(arguments.input))]
    return requirement_rows(records, Draft202012Validator(schema),
                            cr.load_dataset(Path(arguments.dataset)),
                            cr.load_blocks(Path(arguments.model_input)), mapping, allowlist)


def load_g5(arguments: argparse.Namespace) -> set[str]:
    """G5 answers, accepted only with the checksum of the G5 result file."""
    result = json.loads(Path(arguments.g5_result).read_text(encoding="utf-8"))
    if result["files"]["answers"] != sha256_of(Path(arguments.g5_answers)):
        raise CheckError("G5 answer file differs from the checksum in the G5 result")
    return read_g5_security(Path(arguments.g5_answers).read_text(encoding="utf-8"))


def prepare(arguments: argparse.Namespace):
    rows = load_rows(arguments)
    g5_ja = load_g5(arguments)
    return rows, g5_ja, build_candidates(rows, g5_ja)


def command_sheet(arguments: argparse.Namespace) -> int:
    directory = Path(arguments.out_dir)
    paths = paths_in(directory)
    refuse_existing(paths["sheet"], paths["answers"], paths["manifest"])
    rows, _g5, cands = prepare(arguments)
    by_key = {row["key"]: row for row in rows}
    directory.mkdir(parents=True, exist_ok=True)
    paths["sheet"].write_text(render_sheet(cands["order"], by_key), encoding="utf-8")
    paths["answers"].write_text(render_answers(cands["order"]), encoding="utf-8")
    write_json(paths["manifest"], {"order": cands["order"], "inputs": input_hashes(arguments),
                                   "code_commit": git_commit(), "seed": SEED})
    print_counts(candidate_counts(cands, rows))
    return 0


def load_state(arguments: argparse.Namespace):
    directory = Path(arguments.out_dir)
    paths = paths_in(directory)
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    if manifest["inputs"] != input_hashes(arguments):
        raise CheckError("inputs differ from those of the sheet (checksums)")
    rows, g5_ja, cands = prepare(arguments)
    if cands["order"] != manifest["order"]:
        raise CheckError("sheet order cannot be reproduced")
    answers, problems = parse_answers(paths["answers"].read_text(encoding="utf-8"),
                                      cands["order"])
    by_key = {row["key"]: row for row in rows}
    strengths = {row["key"]: row["strength"] for row in rows}
    return directory, paths, rows, g5_ja, cands, by_key, strengths, answers, problems


def completed_rounds(directory: Path, lock: dict[str, Any]
                     ) -> tuple[dict[str, dict[str, str]], int]:
    """Read all locked counter rounds; return checks and the number of rounds."""
    checks: dict[str, dict[str, str]] = {}
    for round_no, info in enumerate(lock["rounds"], start=1):
        _sheet, answer_file = counter_paths(directory, round_no)
        if info.get("answers_sha256") and info["answers_sha256"] != sha256_of(answer_file):
            raise CheckError(f"counter-check round {round_no} changed after it was locked")
        if not info.get("answers_sha256"):
            break
        parsed, problems = parse_counter(answer_file.read_text(encoding="utf-8"), info["keys"])
        if problems:
            raise CheckError(f"counter-check round {round_no} not complete")
        checks.update(parsed)
    return checks, len(lock["rounds"])


def command_compare(arguments: argparse.Namespace) -> int:
    directory, paths, _rows, _g5, cands, by_key, strengths, answers, problems = \
        load_state(arguments)
    refuse_existing(paths["lock"])
    if problems:
        for problem in problems:
            print(problem)
        print(f"answers not complete: {len(problems)} problem(s). Nothing written.")
        return 1
    matches = matches_by_entry(answers, strengths)
    pending = all_pending(assess_entries(matches, {}))
    lock = {"answers_sha256": sha256_of(paths["answers"]), "rounds": []}
    print(f"answers complete: {len(answers)}")
    if pending:
        sheet, answer_text = render_counter(pending, by_key, 1)
        sheet_path, answer_path = counter_paths(directory, 1)
        refuse_existing(sheet_path, answer_path)
        sheet_path.write_text(sheet, encoding="utf-8")
        answer_path.write_text(answer_text, encoding="utf-8")
        lock["rounds"].append({"keys": pending})
    write_json(paths["lock"], lock)
    print(f"counter-check round 1 entries: {len(pending)}")
    return 0


def command_next(arguments: argparse.Namespace) -> int:
    directory, paths, _rows, _g5, _cands, by_key, strengths, answers, problems = \
        load_state(arguments)
    lock = json.loads(paths["lock"].read_text(encoding="utf-8"))
    if problems or lock["answers_sha256"] != sha256_of(paths["answers"]):
        raise CheckError("answer file changed after the compare step")
    if not lock["rounds"] or lock["rounds"][-1].get("answers_sha256"):
        print("no open counter-check round")
        return 0
    round_no = len(lock["rounds"])
    current = lock["rounds"][-1]
    _sheet, answer_file = counter_paths(directory, round_no)
    parsed, round_problems = parse_counter(answer_file.read_text(encoding="utf-8"),
                                           current["keys"])
    if round_problems:
        for problem in round_problems:
            print(problem)
        print(f"round {round_no} not complete. Nothing written.")
        return 1
    current["answers_sha256"] = sha256_of(answer_file)
    checks, _ = completed_rounds(directory, lock)
    pending = all_pending(assess_entries(matches_by_entry(answers, strengths), checks))
    if pending:
        sheet, answer_text = render_counter(pending, by_key, round_no + 1)
        sheet_path, answer_path = counter_paths(directory, round_no + 1)
        refuse_existing(sheet_path, answer_path)
        sheet_path.write_text(sheet, encoding="utf-8")
        answer_path.write_text(answer_text, encoding="utf-8")
        lock["rounds"].append({"keys": pending})
    write_json(paths["lock"], lock)
    print(f"round {round_no} locked: {len(parsed)} entries")
    print(f"counter-check round {round_no + 1} entries: {len(pending)}")
    return 0


def command_result(arguments: argparse.Namespace) -> int:
    output = Path(arguments.output)
    refuse_existing(output)
    directory, paths, rows, g5_ja, cands, by_key, strengths, answers, problems = \
        load_state(arguments)
    lock = json.loads(paths["lock"].read_text(encoding="utf-8"))
    if problems or lock["answers_sha256"] != sha256_of(paths["answers"]):
        raise CheckError("answer file changed after the compare step")
    if lock["rounds"] and not lock["rounds"][-1].get("answers_sha256"):
        raise CheckError("a counter-check round is still open (run next)")
    checks, rounds = completed_rounds(directory, lock)
    matches = matches_by_entry(answers, strengths)
    assessed = assess_entries(matches, checks)
    if all_pending(assessed):
        raise CheckError("counter-checks still pending")
    files = {"sheet": sha256_of(paths["sheet"]), "answers": sha256_of(paths["answers"])}
    for round_no in range(1, rounds + 1):
        for path in counter_paths(directory, round_no):
            files[path.name] = sha256_of(path)
    result = {
        "rules": "docs/entscheidungen.md: G1, G2 and G6",
        "code_commit": git_commit(),
        "inputs": {name: {"path": str(getattr(arguments, name, "")) or None, "sha256": value}
                   for name, value in input_hashes(arguments).items()},
        "files": files,
        "candidates": candidate_counts(cands, rows),
        "counts": tally(assessed, matches, checks, g5_ja, answers),
    }
    write_json(output, result)
    print_counts(result["counts"]["categories"])
    print(f"written: {output}")
    return 0


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Gap analysis of the security grid (G6). "
                                     "Prints numbers and identifiers only.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("sheet", "compare", "next", "result"):
        command = sub.add_parser(name)
        command.add_argument("--input", required=True, help="Extraction output, JSONL.")
        command.add_argument("--dataset", required=True, help="Prepared dataset, JSONL.")
        command.add_argument("--model-input", required=True, help="Model input, JSONL.")
        command.add_argument("--mentions-map", default=None)
        command.add_argument("--allowlist", default="")
        command.add_argument("--schema", default=str(cr.DEFAULT_SCHEMA))
        command.add_argument("--g5-answers", required=True, help="G5 answer file.")
        command.add_argument("--g5-result", required=True, help="G5 result JSON.")
        command.add_argument("--out-dir", required=True, help="Directory under eval/responses/.")
        if name == "result":
            command.add_argument("--output", required=True, help="Result JSON, never overwritten.")
    return parser.parse_args(argv)


COMMANDS = {"sheet": command_sheet, "compare": command_compare, "next": command_next,
            "result": command_result}


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    try:
        return COMMANDS[arguments.command](arguments)
    except CheckError as error:
        print(f"Stopped: {error}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
