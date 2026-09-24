"""Assign every rejected excerpt to one cause, without printing its content.

Rule: docs/entscheidungen.md, addendum to E10 of 2026-09-24. The yardstick
is prompt version 1 (prompts/extraction_system_v1.md, field excerpt):

* rule 1: the excerpt follows the prompt, yet validate_output.py rejects
  it. The checker is at fault.
* rule 2: the excerpt breaks a rule of the prompt. A finding about the
  model.
* rule 3: no defined cause fits. The author inspects the place locally.

Causes are tested in the fixed order of CAUSES below; the first that
fits is reported. An excerpt that breaks two rules gets only the first.

Point 5 of the rule: for accepted excerpts the script also counts where
validate_output.py is more lenient than the prompt.

Nothing of an excerpt, a diff or a comment is printed: only the pull
number, the requirement id, the position of the evidence entry and the
cause.

Work package E, step A8, sub-step 9. Research questions FF1 and FF2.

Run from the project root:

    python src/extract/diagnose_excerpts.py \
      --input data/processed/extraction_2026-09-22_pilot.jsonl \
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \
      --model-input data/processed/model_input_2026-09-19.jsonl \
      --mentions-map data/interim/mention_map.json \
      --allowlist "jaspify,jax,pytest,rus"
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from pseudonymise import load_mapping, mask
from validate_output import haystacks_for, load_dataset, read_jsonl, strip_diff_markers

# Cause -> (rule of the addendum to E10, short description). The order
# of this dictionary is the order in which the causes are tested.
CAUSES: dict[str, tuple[int, str]] = {
    "locator_not_found": (2, "no file or comment with the named locator"),
    "edge_whitespace": (1, "only whitespace at the start or end differs"),
    "plus_plus_line_dropped": (1, "an added line starting with ++ is dropped by the checker"),
    "removed_line": (2, "contains text of a removed line (-)"),
    "hunk_header": (2, "contains text of a hunk header line (@@)"),
    "diff_markers_kept": (2, "the leading +, - or space was not left out"),
    "inner_whitespace": (2, "spaces, tabs or line breaks inside differ"),
    "ellipsis": (2, "shortened with ... or the ellipsis character"),
    "other_file": (2, "occurs in the diff of another file"),
    "review_context": (2, "occurs in the code context of a review comment"),
    "other_location": (2, "occurs in another part of the pull request"),
    "file_not_in_block": (2, "the named file was not shown to the model"),
    "likely_rephrased": (3, "most words occur in the source, the wording does not"),
    "no_match": (3, "no defined cause fits"),
}

# Share of the words of an excerpt that must occur in the named source
# for likely_rephrased. A heuristic, therefore rule 3 and not rule 2.
REPHRASE_WORD_SHARE = 0.8

# A character no excerpt contains. It stands in for a line the prompt
# forbids to cross, so a multi-line excerpt across it cannot match.
BARRIER = "\x00"

FILE_HEADER = re.compile(r"^\[FILE (?P<name>.+?) status=\S* \+\S* -\S*\]$")
NOT_INCLUDED = "(diff not included:"
ELLIPSIS = re.compile(r"\.\.\.|\u2026")
WORD = re.compile(r"\w{3,}")


# --- views of a patch -------------------------------------------------


def _view(patch: str, *, keep_plus_plus: bool = False, removed: str = "skip",
          header: str = "skip") -> str:
    """Rebuild a patch without markers under the given line policy.

    removed / header: "skip" drops the line, "strip" keeps its text,
    "barrier" puts BARRIER in its place.
    """
    kept: list[str] = []
    for line in patch.split("\n"):
        if line.startswith("@@"):
            if header == "strip":
                kept.append(line)
            elif header == "barrier":
                kept.append(BARRIER)
        elif line.startswith("+++") and not keep_plus_plus:
            continue  # as validate_output.py does
        elif line.startswith("-"):
            if removed == "strip":
                kept.append(line[1:])
            elif removed == "barrier":
                kept.append(BARRIER)
        elif line.startswith(("+", " ")):
            kept.append(line[1:])
    return "\n".join(kept)


def collapse(text: str) -> str:
    """Every run of whitespace becomes one space; no-break space counts."""
    return re.sub(r"\s+", " ", text.replace("\u00a0", " ")).strip()


def occurs(excerpt: str, texts: list[str]) -> bool:
    """True if the excerpt, or the excerpt without edge whitespace, occurs."""
    trimmed = excerpt.strip()
    return any(excerpt in text or (trimmed and trimmed in text) for text in texts)


def words_covered(excerpt: str, texts: list[str]) -> float:
    words = [w.lower() for w in WORD.findall(excerpt)]
    if not words:
        return 0.0
    pool = {w.lower() for text in texts for w in WORD.findall(text)}
    return sum(w in pool for w in words) / len(words)


# --- what the model saw -----------------------------------------------


def files_in_block(block: str) -> set[str]:
    """File paths whose diff text was part of the source block."""
    lines = block.split("\n")
    shown = set()
    for position, line in enumerate(lines):
        match = FILE_HEADER.match(line)
        if not match:
            continue
        following = lines[position + 1] if position + 1 < len(lines) else ""
        if not following.startswith(NOT_INCLUDED):
            shown.add(match.group("name"))
    return shown


def load_blocks(path: Path) -> dict[int, str]:
    return {record["pull_number"]: record["source_block"]
            for _, record in read_jsonl(path)}


# --- classification ---------------------------------------------------


def prose_texts(pull: dict[str, Any], mapping: dict[str, str] | None,
                allowlist: set[str]) -> list[str]:
    def clean(text: str | None) -> str:
        return mask(text or "", mapping, allowlist) if mapping else (text or "")
    texts = [clean(pull.get("title")), clean(pull.get("body"))]
    for key in ("issue_comments", "review_comments"):
        texts.extend(clean(c.get("body")) for c in pull.get(key, []))
    return texts


def classify(item: dict[str, Any], pull: dict[str, Any], shown: set[str],
             mapping: dict[str, str] | None = None,
             allowlist: set[str] | None = None) -> str:
    """Return the first cause from CAUSES that fits a rejected excerpt."""
    allowlist = allowlist or set()
    excerpt = item.get("excerpt") or ""
    candidates = haystacks_for(item, pull, mapping, allowlist)
    if not candidates:
        return "locator_not_found"

    # The prompt demands exact inner spaces only, so edge whitespace is
    # tested first and counts against the checker.
    if excerpt.strip() and any(excerpt.strip() in c for c in candidates):
        return "edge_whitespace"

    if item.get("location") == "diff":
        locator = item.get("locator")
        targets = [f.get("patch") or "" for f in pull.get("files", [])
                   if locator in (None, f.get("filename"))]
        others = [f.get("patch") or "" for f in pull.get("files", [])
                  if locator is not None and f.get("filename") != locator]
        if occurs(excerpt, [_view(p, keep_plus_plus=True) for p in targets]):
            return "plus_plus_line_dropped"
        if occurs(excerpt, [_view(p, removed="strip") for p in targets]):
            return "removed_line"
        if occurs(excerpt, [_view(p, header="strip") for p in targets]):
            return "hunk_header"
        if occurs(excerpt, targets):
            return "diff_markers_kept"

    if any(collapse(excerpt) and collapse(excerpt) in collapse(c) for c in candidates):
        return "inner_whitespace"
    fragments = [collapse(f) for f in ELLIPSIS.split(excerpt) if collapse(f)]
    if ELLIPSIS.search(excerpt) and fragments and all(
            any(f in collapse(c) for c in candidates) for f in fragments):
        return "ellipsis"

    if item.get("location") == "diff":
        if occurs(excerpt, [strip_diff_markers(p) for p in others]):
            return "other_file"
        hunks = [c.get("diff_hunk") or "" for c in pull.get("review_comments", [])]
        if occurs(excerpt, hunks + [strip_diff_markers(h) for h in hunks]):
            return "review_context"
        if occurs(excerpt, prose_texts(pull, mapping, allowlist)):
            return "other_location"
        if item.get("locator") not in shown:
            return "file_not_in_block"
    else:
        elsewhere = prose_texts(pull, mapping, allowlist) + [
            strip_diff_markers(f.get("patch") or "") for f in pull.get("files", [])]
        if occurs(excerpt, [t for t in elsewhere if t not in candidates]):
            return "other_location"

    if words_covered(excerpt, candidates) >= REPHRASE_WORD_SHARE:
        return "likely_rephrased"
    return "no_match"


def lenient_findings(item: dict[str, Any], pull: dict[str, Any], shown: set[str],
                     mapping: dict[str, str] | None = None,
                     allowlist: set[str] | None = None) -> list[str]:
    """Point 5: why an accepted excerpt would fail a check as strict as the prompt."""
    excerpt = item.get("excerpt") or ""
    location = item.get("location")
    locator = item.get("locator")
    found: list[str] = []
    if location == "diff":
        targets = [f.get("patch") or "" for f in pull.get("files", [])
                   if locator in (None, f.get("filename"))]
        if not any(excerpt in _view(p, removed="barrier") for p in targets):
            found.append("spans_removed_line")
        if not any(excerpt in _view(p, header="barrier") for p in targets):
            found.append("spans_hunk_header")
        if locator not in shown:
            found.append("file_not_in_block")
    elif location == "review_comment":
        bodies = [mask(c.get("body") or "", mapping, allowlist or set()) if mapping
                  else (c.get("body") or "")
                  for c in pull.get("review_comments", [])
                  if locator in (None, str(c.get("id")))]
        if not any(excerpt in body for body in bodies):
            found.append("from_review_context")
    return found


# --- run --------------------------------------------------------------


def diagnose(records, dataset, blocks, mapping=None, allowlist=None) -> dict[str, Any]:
    """Classify every excerpt that validate_output.py rejects."""
    rejected: list[dict[str, Any]] = []
    lenient: Counter = Counter()
    accepted_by_location: Counter = Counter()
    for record in records:
        number = record.get("pull_number")
        pull = dataset.get(number)
        if pull is None:
            rejected.append({"pull": number, "id": "<no pull>", "position": 0,
                             "location": None, "cause": "locator_not_found"})
            continue
        shown = files_in_block(blocks.get(number, ""))
        for requirement in record.get("requirements", []):
            for position, item in enumerate(requirement.get("evidence", []), start=1):
                excerpt = item.get("excerpt") or ""
                candidates = haystacks_for(item, pull, mapping, allowlist or set())
                if candidates and any(excerpt in text for text in candidates):
                    accepted_by_location[item.get("location")] += 1
                    lenient.update(lenient_findings(item, pull, shown, mapping, allowlist))
                    continue
                rejected.append({"pull": number, "id": requirement.get("id", "<no id>"),
                                 "position": position, "location": item.get("location"),
                                 "cause": classify(item, pull, shown, mapping, allowlist)})
    return {"rejected": rejected, "lenient": lenient,
            "accepted_by_location": accepted_by_location}


def rule_four(rejected: list[dict[str, Any]]) -> dict[str, int]:
    """Causes under rule 2 with the number of distinct pull requests."""
    pulls: dict[str, set] = defaultdict(set)
    for entry in rejected:
        if CAUSES[entry["cause"]][0] == 2:
            pulls[entry["cause"]].add(entry["pull"])
    return {cause: len(numbers) for cause, numbers in pulls.items()}


def code_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], check=True,
                              capture_output=True, text=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assign rejected excerpts to causes, without printing content.")
    parser.add_argument("--input", required=True, help="Extraction output, JSONL.")
    parser.add_argument("--dataset", required=True, help="Prepared dataset, JSONL.")
    parser.add_argument("--model-input", required=True,
                        help="Model input the run used, JSONL with source_block.")
    parser.add_argument("--mentions-map", default=None)
    parser.add_argument("--allowlist", default="")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    dataset = load_dataset(Path(arguments.dataset))
    blocks = load_blocks(Path(arguments.model_input))
    mapping = load_mapping(Path(arguments.mentions_map)) if arguments.mentions_map else None
    allowlist = {n.strip().lower() for n in arguments.allowlist.split(",") if n.strip()}
    if mapping is None:
        print("Note: no --mentions-map given, prose is compared unmasked.")
    records = [record for _, record in read_jsonl(Path(arguments.input))]

    result = diagnose(records, dataset, blocks, mapping, allowlist)
    print(f"Code commit: {code_commit()}")
    print(f"Records read: {len(records)}")
    print(f"Rejected excerpts: {len(result['rejected'])}\n")
    for entry in result["rejected"]:
        rule = CAUSES[entry["cause"]][0]
        print(f"pull {entry['pull']}  {entry['id']}  evidence {entry['position']}  "
              f"location {entry['location']}  cause {entry['cause']}  rule {rule}")

    print("\nCauses:")
    counts = Counter(entry["cause"] for entry in result["rejected"])
    for cause, (rule, text) in CAUSES.items():
        if counts[cause]:
            print(f"  {cause}: {counts[cause]}  (rule {rule}; {text})")

    repeated = {c: n for c, n in rule_four(result["rejected"]).items() if n >= 2}
    print("\nRule 4, same cause under rule 2 in at least two pull requests: "
          + (", ".join(f"{c} in {n}" for c, n in sorted(repeated.items()))
             if repeated else "not met"))

    print("\nPoint 5, accepted excerpts by location: "
          + (", ".join(f"{k} {v}" for k, v in sorted(result["accepted_by_location"].items()))
             or "none"))
    print("Point 5, accepted but more lenient than the prompt: "
          + (", ".join(f"{k} {v}" for k, v in sorted(result["lenient"].items()))
             or "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
