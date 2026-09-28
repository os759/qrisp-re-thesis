"""Show the rejected excerpts of rule 3 in the author's terminal only.

Rule: docs/entscheidungen.md, addendum to E10 of 2026-09-28, rule 3 in
the full run, part 3. The author inspects every excerpt that the search
program src/extract/diagnose_excerpts.py puts under rule 3 and assigns
it to rule 1 (checker at fault) or rule 2 (model at fault).

This script selects exactly those excerpts, with the same checks as
diagnose_excerpts.py, and shows for each one:

* the excerpt as the model wrote it, plain and as a Python literal, so
  invisible characters become visible;
* the closest passage in the named source, as validate_output.py sees
  it (a diff without its line markers; a barrier line stands for a
  removed line or a hunk header);
* the differences between both, marked as [-only in source-] and
  {+only in excerpt+};
* hint H1: whether the excerpt, without edge whitespace, occurs in the
  source block the model saw, and in which section of it.

The hints are aids. The assignment is made by the author.

Content of pull requests is printed. Therefore the script refuses to
write to anything but a terminal, unless --allow-pipe is given. Never
paste the output into a chat. The only files it writes are the
assignment table (--template), which holds identifiers and no content.

Work package E, step A8, rule 3. Research questions FF1 and FF2.

Run from the project root, one excerpt at a time:

    python src/extract/inspect_excerpts.py \\
      --input data/processed/extraction_2026-09-25_full_v2.jsonl \\
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \\
      --model-input data/processed/model_input_2026-09-19.jsonl \\
      --mentions-map data/interim/mention_map.json \\
      --allowlist "jaspify,jax,pytest,rus" --only 1
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from diagnose_excerpts import CAUSES, classify, files_in_block, load_blocks
from pseudonymise import load_mapping
from validate_output import (BARRIER, excerpt_found, haystacks_for,
                             load_dataset, read_jsonl)

RULE_THREE_CAUSES = {cause for cause, (rule, _) in CAUSES.items() if rule == 3}

# Kind of deviation -> rule it belongs to. Fixed in the addendum of
# 2026-09-28 before the inspection; the author tests them in this
# order and takes the first that fits.
SUBTYPES: dict[str, int] = {
    "pruefprogramm": 1,
    "zusammengesetzt": 2,
    "umformuliert": 2,
    "zeichen": 2,
    "ohne_gegenstueck": 2,
}
YES_NO = ("ja", "nein")

TABLE_COLUMNS = ["Nr", "Pull", "Anforderung", "Beleg", "Ursache", "Regel",
                 "Unterart", "Andere Stelle", "Zweifel"]
BARRIER_SHOWN = "<SPERRE: entfernte Zeile oder @@-Zeile>"
CONTEXT_CHARS = 40
HEADER_PREFIXES = ("[", "===")


# --- selection --------------------------------------------------------


def select(records: list[dict[str, Any]], dataset: dict[int, dict[str, Any]],
           blocks: dict[int, str], mapping: dict[str, str] | None,
           allowlist: set[str]) -> list[dict[str, Any]]:
    """Rejected excerpts under rule 3, in the order diagnose_excerpts.py prints them.

    The loop repeats diagnose(): same records, same order, same check
    for acceptance, same classify(). A test compares both.
    """
    selected: list[dict[str, Any]] = []
    for record in records:
        number = record.get("pull_number")
        pull = dataset.get(number)
        if pull is None:
            continue
        shown = files_in_block(blocks.get(number, ""))
        for requirement in record.get("requirements", []):
            for position, item in enumerate(requirement.get("evidence", []), start=1):
                candidates = haystacks_for(item, pull, mapping, allowlist)
                if candidates and excerpt_found(item, pull, candidates):
                    continue
                cause = classify(item, pull, shown, mapping, allowlist)
                if cause not in RULE_THREE_CAUSES:
                    continue
                selected.append({
                    "nr": len(selected) + 1, "pull": number,
                    "id": requirement.get("id", "<no id>"), "position": position,
                    "location": item.get("location"), "locator": item.get("locator"),
                    "cause": cause, "item": item, "candidates": candidates,
                    "block": blocks.get(number, ""),
                })
    return selected


# --- hints ------------------------------------------------------------


def markerless_lines(block: str) -> list[str]:
    """The block line by line, diff markers left out, one line per line.

    A line starting with @@ or with a single - becomes BARRIER; a line
    starting with + or a space loses its first character; any other
    line stays. A prose line that starts with - (a list item) also
    becomes BARRIER; that is why block_hint searches the raw block too.
    The line count is kept, so a line number fits both views.
    """
    lines = []
    for line in block.split("\n"):
        if line.startswith("@@") or line.startswith("-"):
            lines.append(BARRIER)
        elif line.startswith(("+", " ")):
            lines.append(line[1:])
        else:
            lines.append(line)
    return lines


def block_hint(excerpt: str, block: str) -> tuple[bool, int | None, str | None]:
    """Hint H1: occurs the excerpt without edge whitespace in the model's block?

    Returns (found, line number counted from 1, nearest header line
    above it). Searched in the raw block and in the markerless view.
    """
    core = excerpt.strip()
    if not core or not block:
        return False, None, None
    raw_lines = block.split("\n")
    for view in (block, "\n".join(markerless_lines(block))):
        offset = view.find(core)
        if offset >= 0:
            line_number = view.count("\n", 0, offset) + 1
            header = next((raw_lines[i] for i in range(line_number - 1, -1, -1)
                           if raw_lines[i].startswith(HEADER_PREFIXES)), None)
            return True, line_number, header
    return False, None, None


def closest_passage(excerpt: str, texts: list[str]) -> tuple[str, float]:
    """The window of a source text that fits the excerpt best, and its similarity.

    Anchored at the longest common run of characters, widened by
    CONTEXT_CHARS on both sides. Similarity is the ratio of difflib
    between 0 and 1, taken between the excerpt and the part of the
    window from its first to its last matching character, so the added
    context does not lower it. A heuristic for reading, not a
    measurement.
    """
    best_window, best_ratio = "", -1.0
    for text in texts:
        if not text:
            continue
        match = SequenceMatcher(None, text, excerpt, autojunk=False).find_longest_match(
            0, len(text), 0, len(excerpt))
        start = max(0, match.a - match.b - CONTEXT_CHARS)
        end = min(len(text), match.a - match.b + len(excerpt) + CONTEXT_CHARS)
        window = text[start:end]
        ratio = SequenceMatcher(None, matched_core(window, excerpt), excerpt,
                                autojunk=False).ratio()
        if ratio > best_ratio:
            best_window, best_ratio = window, ratio
    return best_window, max(best_ratio, 0.0)


def matched_core(source: str, excerpt: str) -> str:
    """The part of source from its first to its last character shared with the excerpt."""
    blocks = [b for b in SequenceMatcher(None, source, excerpt, autojunk=False)
              .get_matching_blocks() if b.size]
    return source[blocks[0].a:blocks[-1].a + blocks[-1].size] if blocks else ""


def mark_differences(source: str, excerpt: str) -> str:
    """Excerpt with its differences to the matched core of source marked.

    Source text before the first and after the last shared character is
    context and not marked; the full window is printed separately.
    """
    core = matched_core(source, excerpt)
    parts = []
    for tag, i1, i2, j1, j2 in SequenceMatcher(None, core, excerpt,
                                               autojunk=False).get_opcodes():
        if tag == "equal":
            parts.append(excerpt[j1:j2])
            continue
        if i2 > i1:
            parts.append("[-" + core[i1:i2] + "-]")
        if j2 > j1:
            parts.append("{+" + excerpt[j1:j2] + "+}")
    return "".join(parts)


def visible(text: str) -> str:
    return text.replace(BARRIER, BARRIER_SHOWN)


# --- output -----------------------------------------------------------


def render(entry: dict[str, Any], total: int) -> str:
    excerpt = entry["item"].get("excerpt") or ""
    window, ratio = closest_passage(excerpt, entry["candidates"])
    found, line_number, header = block_hint(excerpt, entry["block"])
    hint = (f"ja, Zeile {line_number} des Quellblocks, Abschnitt: {header}"
            if found else "nein")
    rule = "=" * 72
    return "\n".join([
        rule,
        f"Zitat {entry['nr']} von {total}   pull {entry['pull']}   {entry['id']}   "
        f"Beleg {entry['position']}",
        f"Stelle: {entry['location']} {entry['locator']}   Ursache: {entry['cause']}",
        f"H1, im Quellblock des Modells: {hint}",
        f"Aehnlichkeit mit der naechsten Stelle: {ratio:.2f}",
        "",
        "--- Zitat des Modells ---",
        visible(excerpt),
        "--- dasselbe als Python-Literal (macht unsichtbare Zeichen sichtbar) ---",
        repr(excerpt),
        "--- naechste Stelle in der genannten Quelle (Sicht des Pruefprogramms) ---",
        visible(window),
        "--- Unterschiede: [-nur in der Quelle-] {+nur im Zitat+} ---",
        visible(mark_differences(window, excerpt)),
        "",
    ])


def write_template(selected: list[dict[str, Any]], path: Path) -> None:
    """Assignment table with identifiers only. Never overwrites."""
    if path.exists():
        raise FileExistsError(f"{path} exists; not overwritten.")
    lines = [
        "# Zuordnung der Zitate nach Regel 3, Volllauf 2026-09-25_full_v2",
        "",
        "Regel: docs/entscheidungen.md, Nachtrag zu E10 vom 28.09.2026,",
        "Regel 3 im Volllauf, Teil 3. Die Tabelle enthaelt nur Kennungen,",
        "keine Inhalte. Erzeugt von src/extract/inspect_excerpts.py,",
        "ausgefuellt vom Verfasser.",
        "",
        "Regel: 1 oder 2. Unterart: " + ", ".join(SUBTYPES) + ".",
        "Andere Stelle und Zweifel: ja oder nein.",
        "",
        "| " + " | ".join(TABLE_COLUMNS) + " |",
        "|" + "---|" * len(TABLE_COLUMNS),
    ]
    for e in selected:
        lines.append(f"| {e['nr']} | {e['pull']} | {e['id']} | {e['position']} | "
                     f"{e['cause']} |  |  |  |  |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_table(path: Path) -> list[list[str]]:
    rows = []
    for line in path.read_text(encoding="utf-8").split("\n"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("|") and cells and cells[0].isdigit():
            rows.append(cells)
    return rows


def tally(selected: list[dict[str, Any]], path: Path) -> tuple[list[str], dict[str, Counter]]:
    """Check the filled table against the selection and count it."""
    problems: list[str] = []
    counts: dict[str, Counter] = {k: Counter() for k in
                                  ("rule", "subtype", "cause_rule", "other_place",
                                   "doubt", "pulls_rule")}
    rows = read_table(path)
    if len(rows) != len(selected):
        problems.append(f"table has {len(rows)} rows, selection has {len(selected)}")
    pulls: dict[str, set] = {"1": set(), "2": set()}
    for row, entry in zip(rows, selected):
        if len(row) != len(TABLE_COLUMNS):
            problems.append(f"row {row[0]}: {len(row)} cells instead of {len(TABLE_COLUMNS)}")
            continue
        nr, pull, ident, position, cause, rule, subtype, other, doubt = row
        expected = [str(entry["nr"]), str(entry["pull"]), entry["id"],
                    str(entry["position"]), entry["cause"]]
        if [nr, pull, ident, position, cause] != expected:
            problems.append(f"row {nr}: identifiers differ from the selection")
            continue
        if rule not in ("1", "2"):
            problems.append(f"row {nr}: rule must be 1 or 2")
        if subtype not in SUBTYPES:
            problems.append(f"row {nr}: unknown subtype")
        elif rule in ("1", "2") and SUBTYPES[subtype] != int(rule):
            problems.append(f"row {nr}: subtype {subtype} belongs to rule {SUBTYPES[subtype]}")
        if other not in YES_NO or doubt not in YES_NO:
            problems.append(f"row {nr}: other place and doubt must be ja or nein")
        elif subtype == "pruefprogramm" and other == "ja":
            problems.append(f"row {nr}: pruefprogramm needs the named place, not another")
        if problems and problems[-1].startswith(f"row {nr}:"):
            continue
        counts["rule"][rule] += 1
        counts["subtype"][subtype] += 1
        counts["cause_rule"][f"{cause} -> rule {rule}"] += 1
        counts["other_place"][other] += 1
        counts["doubt"][doubt] += 1
        pulls[rule].add(pull)
    for rule, numbers in pulls.items():
        counts["pulls_rule"][rule] = len(numbers)
    return problems, counts


# --- run --------------------------------------------------------------


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Show rule 3 excerpts in the terminal; count the assignment.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--model-input", required=True)
    parser.add_argument("--mentions-map", default=None)
    parser.add_argument("--allowlist", default="")
    parser.add_argument("--only", type=int, default=None,
                        help="Show only excerpt number N (counted from 1).")
    parser.add_argument("--list", action="store_true",
                        help="List identifiers only, no content.")
    parser.add_argument("--template", default=None,
                        help="Write the empty assignment table here (identifiers only).")
    parser.add_argument("--tally", default=None,
                        help="Check and count a filled assignment table.")
    parser.add_argument("--allow-pipe", action="store_true",
                        help="Print content also when the output is no terminal.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    dataset = load_dataset(Path(arguments.dataset))
    blocks = load_blocks(Path(arguments.model_input))
    mapping = load_mapping(Path(arguments.mentions_map)) if arguments.mentions_map else None
    allowlist = {n.strip().lower() for n in arguments.allowlist.split(",") if n.strip()}
    records = [record for _, record in read_jsonl(Path(arguments.input))]
    selected = select(records, dataset, blocks, mapping, allowlist)
    by_cause = Counter(e["cause"] for e in selected)
    print(f"Rule 3 excerpts: {len(selected)}  ("
          + ", ".join(f"{c} {n}" for c, n in sorted(by_cause.items())) + ")")

    if arguments.template:
        write_template(selected, Path(arguments.template))
        print(f"Template written: {arguments.template}")
        return 0
    if arguments.tally:
        problems, counts = tally(selected, Path(arguments.tally))
        for problem in problems:
            print(f"PROBLEM {problem}")
        for name, counter in counts.items():
            print(f"{name}: " + (", ".join(f"{k} {v}" for k, v in sorted(counter.items()))
                                 or "none"))
        return 1 if problems else 0
    if arguments.list:
        for e in selected:
            print(f"{e['nr']}  pull {e['pull']}  {e['id']}  evidence {e['position']}  "
                  f"location {e['location']}  cause {e['cause']}")
        return 0

    if not sys.stdout.isatty() and not arguments.allow_pipe:
        print("Refused: the output is no terminal and would hold content. "
              "Use --list, or --allow-pipe if you know where it goes.")
        return 2
    chosen = selected
    if arguments.only is not None:
        if not 1 <= arguments.only <= len(selected):
            print(f"--only must lie between 1 and {len(selected)}.")
            return 2
        chosen = [selected[arguments.only - 1]]
    print("WARNING: content of pull requests follows. Do not paste it into a chat.\n")
    for entry in chosen:
        print(render(entry, len(selected)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
