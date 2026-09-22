"""Draw a stratified sample of pull requests.

First written for the manual formulation probe of package C. Since
decision E10 it also draws the pilot sample of step A8 and, later, the
evaluation sample of decision E2.

The script only draws. It does not evaluate anything and it does not
produce requirements.

Two switches were added by decision E10. Without them the script
behaves exactly as before, so the draw of 2026-08-25 can be repeated:

* --sizes sets the number of records per stratum, for example
  S6=1,S5=4,S4=3,S3=3,S2=4,S1=5. All six strata must be named.
* --exclude names pull request numbers that must not be drawn, for
  example the twelve records of the formulation probe. Every number has
  to belong to the eligible population; an unknown number stops the
  script, because a typing error would otherwise go unnoticed.

Run from the project root:
    python src/analyze/draw_sample.py \
        --input data/interim/pulls_prepared_2026-08-19.jsonl
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

Record = dict[str, Any]
Predicate = Callable[[Record], bool]

DEFAULT_SEED = 20260823
DEFAULT_OUTPUT = Path("docs/sample_formulation_probe.md")


def comment_count(record: Record) -> int:
    """Number of comments actually present in the prepared record."""
    issue = record.get("issue_comments") or []
    review = record.get("review_comments") or []
    return len(issue) + len(review)


def stage3_dropped(record: Record) -> int:
    truncation = record.get("truncation") or {}
    value = truncation.get("stage3_dropped", 0)
    return int(value or 0)


# Stratum definitions, processed from the rarest to the most common one.
# Each entry: key, human readable label, predicate, target size.
STRATA: list[tuple[str, str, Predicate, int]] = [
    (
        "S6",
        "no code changes",
        lambda r: r.get("has_code_changes") is False,
        1,
    ),
    (
        "S5",
        "large diff, truncated by the per pull request budget",
        lambda r: stage3_dropped(r) > 0,
        2,
    ),
    (
        "S4",
        "no description text",
        lambda r: r.get("has_body") is False,
        2,
    ),
    (
        "S3",
        "closed without merge",
        lambda r: r.get("outcome") == "closed_unmerged",
        2,
    ),
    (
        "S2",
        "merged, no comments",
        lambda r: r.get("outcome") == "merged" and comment_count(r) == 0,
        2,
    ),
    (
        "S1",
        "merged, with comments",
        lambda r: r.get("outcome") == "merged" and comment_count(r) > 0,
        3,
    ),
]

FALLBACK_STRATUM = "S1"
DEFAULT_SIZES: dict[str, int] = {key: size for key, _, _, size in STRATA}
DEFAULT_TITLE = "Sample for the manual formulation probe (FF2)"


def parse_sizes(text: str) -> dict[str, int]:
    """Read 'S6=1,S5=4,...' into a dict. All strata must be named once."""
    sizes: dict[str, int] = {}
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        key, separator, value = part.partition("=")
        key = key.strip()
        if not separator:
            raise ValueError(f"--sizes: '{part}' has no '='")
        if key not in DEFAULT_SIZES:
            raise ValueError(f"--sizes: unknown stratum '{key}'")
        if key in sizes:
            raise ValueError(f"--sizes: stratum '{key}' named twice")
        try:
            number = int(value)
        except ValueError as error:
            raise ValueError(
                f"--sizes: '{value}' for {key} is not a whole number"
            ) from error
        if number < 0:
            raise ValueError(f"--sizes: {key} must not be negative")
        sizes[key] = number
    missing = sorted(set(DEFAULT_SIZES) - set(sizes))
    if missing:
        raise ValueError(f"--sizes: strata missing: {', '.join(missing)}")
    return sizes


def parse_exclude(text: str) -> set[int]:
    """Read '48,75,191' into a set of pull request numbers."""
    numbers: set[int] = set()
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            numbers.add(int(part))
        except ValueError as error:
            raise ValueError(
                f"--exclude: '{part}' is not a pull request number"
            ) from error
    return numbers


def apply_exclusion(
    eligible: list[Record], excluded: set[int]
) -> list[Record]:
    """Remove the excluded records. Stop if a number is not eligible."""
    known = {record.get("number") for record in eligible}
    unknown = sorted(excluded - known)
    if unknown:
        raise ValueError(
            "--exclude: not in the eligible population: "
            + ", ".join(str(n) for n in unknown)
        )
    return [r for r in eligible if r.get("number") not in excluded]


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def current_commit() -> str:
    """Short git commit of the working tree, or a marker if unavailable."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return result.stdout.strip() or "unknown"


def read_jsonl(path: Path) -> list[Record]:
    records: list[Record] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise SystemExit(
                    f"line {line_number} of {path} is not valid JSON: {error}"
                ) from error
    return records


def assign_strata(
    records: list[Record],
) -> tuple[dict[str, list[Record]], list[Record]]:
    """Assign every record to at most one stratum, rarest stratum first."""
    pools: dict[str, list[Record]] = {key: [] for key, _, _, _ in STRATA}
    assigned: set[int] = set()
    for key, _label, predicate, _size in STRATA:
        for record in records:
            number = record.get("number")
            if number in assigned:
                continue
            if predicate(record):
                pools[key].append(record)
                assigned.add(number)
    unassigned = [r for r in records if r.get("number") not in assigned]
    return pools, unassigned


def draw(
    pools: dict[str, list[Record]],
    unassigned: list[Record],
    seed: int,
    sizes: dict[str, int] | None = None,
) -> tuple[list[tuple[str, Record]], list[str]]:
    """Draw from every stratum. Returns the sample and a list of notes.

    Without sizes the targets of STRATA are used, as before decision E10.
    """
    sizes = DEFAULT_SIZES if sizes is None else sizes
    rng = random.Random(seed)
    notes: list[str] = []
    drawn: list[tuple[str, Record]] = []
    shortfall = 0

    for key, label, _predicate, _default in STRATA:
        size = sizes[key]
        pool = sorted(pools[key], key=lambda r: r.get("number", 0))
        if len(pool) < size:
            missing = size - len(pool)
            shortfall += missing
            notes.append(
                f"Stratum {key} ({label}) holds only {len(pool)} of "
                f"{size} required records. {missing} moved to "
                f"{FALLBACK_STRATUM}."
            )
            take = len(pool)
        else:
            take = size
        for record in rng.sample(pool, take):
            drawn.append((key, record))
            pools[key].remove(record)

    if shortfall:
        spare = sorted(
            pools[FALLBACK_STRATUM], key=lambda r: r.get("number", 0)
        )
        if len(spare) < shortfall:
            notes.append(
                f"Fallback stratum {FALLBACK_STRATUM} cannot absorb the "
                f"shortfall of {shortfall}; {len(spare)} records available."
            )
            shortfall = len(spare)
        for record in rng.sample(spare, shortfall):
            drawn.append((FALLBACK_STRATUM, record))
            pools[FALLBACK_STRATUM].remove(record)

    if unassigned:
        notes.append(
            f"{len(unassigned)} records matched no stratum and were not "
            f"eligible for the draw."
        )

    drawn.sort(key=lambda item: item[1].get("number", 0))
    return drawn, notes


def render(
    drawn: list[tuple[str, Record]],
    pools_before: dict[str, int],
    notes: list[str],
    input_path: Path,
    checksum: str,
    seed: int,
    total: int,
    bots: int,
    open_records: int,
    sizes: dict[str, int] | None = None,
    excluded: set[int] | None = None,
    title: str = DEFAULT_TITLE,
) -> str:
    sizes = DEFAULT_SIZES if sizes is None else sizes
    excluded = excluded or set()
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(
        "Generated by src/analyze/draw_sample.py. This file lists the "
        "drawn pull requests only. It contains no evaluation and no "
        "author identifiers."
    )
    lines.append("")
    lines.append("## Provenance")
    lines.append("")
    lines.append(f"- Drawn at: {timestamp}")
    lines.append(f"- Input file: {input_path}")
    lines.append(f"- Input SHA-256: {checksum}")
    lines.append(f"- Random seed: {seed}")
    lines.append(f"- Code commit: {current_commit()}")
    lines.append(f"- Records in input: {total}")
    lines.append(f"- Excluded bot records: {bots}")
    lines.append(f"- Excluded records still open: {open_records}")
    lines.append(f"- Eligible population: {total - bots - open_records}")
    if sizes != DEFAULT_SIZES:
        lines.append(
            "- Sizes per stratum (--sizes): "
            + ",".join(f"{key}={sizes[key]}" for key, _, _, _ in STRATA)
        )
    if excluded:
        lines.append(
            f"- Excluded before the draw (--exclude), {len(excluded)}: "
            + ", ".join(str(n) for n in sorted(excluded))
        )
    lines.append("")
    lines.append("## Stratum sizes in the eligible population")
    lines.append("")
    lines.append("| Stratum | Definition | Available | Drawn |")
    lines.append("|---|---|---|---|")
    for key, label, _predicate, _default in STRATA:
        taken = sum(1 for k, _ in drawn if k == key)
        lines.append(
            f"| {key} | {label} | {pools_before[key]} | {taken} "
            f"(target {sizes[key]}) |"
        )
    lines.append("")
    lines.append("## Drawn pull requests")
    lines.append("")
    lines.append(
        "| PR | Stratum | Outcome | Description | Comments | "
        "Files dropped by budget | URL |"
    )
    lines.append("|---|---|---|---|---|---|---|")
    for key, record in drawn:
        number = record.get("number")
        outcome = record.get("outcome", "")
        has_body = "yes" if record.get("has_body") else "no"
        comments = comment_count(record)
        dropped = stage3_dropped(record)
        url = record.get("html_url", "")
        lines.append(
            f"| {number} | {key} | {outcome} | {has_body} | {comments} | "
            f"{dropped} | {url} |"
        )
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    if notes:
        for note in notes:
            lines.append(f"- {note}")
    else:
        lines.append("- Every stratum was filled as planned.")
    lines.append("")
    lines.append(
        "Reproduction: rerun the command with the same input file and "
        "the same seed. The draw is deterministic."
    )
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Draw a stratified sample of pull requests for the manual "
            "formulation probe."
        )
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="prepared JSONL data set, one record per pull request",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"target file (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help=f"random seed (default: {DEFAULT_SEED})",
    )
    parser.add_argument(
        "--sizes",
        default=None,
        help="records per stratum, e.g. S6=1,S5=4,S4=3,S3=3,S2=4,S1=5 "
        "(default: the targets of the formulation probe)",
    )
    parser.add_argument(
        "--exclude",
        default=None,
        help="comma separated pull request numbers that must not be drawn",
    )
    parser.add_argument(
        "--title",
        default=DEFAULT_TITLE,
        help=f"heading of the output file (default: {DEFAULT_TITLE})",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="allow writing over an existing output file",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if not args.input.is_file():
        print(f"input file not found: {args.input}", file=sys.stderr)
        return 1
    if args.output.exists() and not args.overwrite:
        print(
            f"output file already exists: {args.output}\n"
            f"pass --overwrite to replace it",
            file=sys.stderr,
        )
        return 1

    try:
        sizes = parse_sizes(args.sizes) if args.sizes else None
        excluded = parse_exclude(args.exclude) if args.exclude else set()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    records = read_jsonl(args.input)
    total = len(records)
    non_bot = [r for r in records if not r.get("author_is_bot")]
    bots = total - len(non_bot)
    eligible = [r for r in non_bot if r.get("outcome") != "open"]
    open_records = len(non_bot) - len(eligible)
    try:
        eligible = apply_exclusion(eligible, excluded)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    pools, unassigned = assign_strata(eligible)
    pools_before = {key: len(pool) for key, pool in pools.items()}
    drawn, notes = draw(pools, unassigned, args.seed, sizes)

    checksum = sha256_of(args.input)
    text = render(
        drawn,
        pools_before,
        notes,
        args.input,
        checksum,
        args.seed,
        total,
        bots,
        open_records,
        sizes,
        excluded,
        args.title,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")

    print(f"records read:        {total}")
    print(f"bot records excluded:{bots:>4}")
    print(f"open records excluded:{open_records:>3}")
    if excluded:
        print(f"excluded by --exclude:{len(excluded):>3}")
    print(f"eligible population: {len(eligible)}")
    shown = DEFAULT_SIZES if sizes is None else sizes
    for key, label, _predicate, _default in STRATA:
        taken = sum(1 for k, _ in drawn if k == key)
        print(
            f"  {key} {label:<48} available {pools_before[key]:>4}  "
            f"drawn {taken} (target {shown[key]})"
        )
    print(f"drawn in total:      {len(drawn)}")
    for note in notes:
        print(f"note: {note}")
    print(f"written to:          {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

