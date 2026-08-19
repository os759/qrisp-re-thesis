"""Describe a collected pull request detail dataset.

Work package D, RQ1. Reads a JSON Lines file of pull request detail
objects and reports field coverage, author and bot shares, diff sizes,
outcome distribution, comment counts and description properties. The
script sends no API requests. Its output is the empirical basis for the
large diff threshold, the bot handling rule and the corpus description
in the implementation chapter.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from github_api import PROJECT_ROOT, read_jsonl, sha256_of

DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "findings_pull_details.md"
SIZE_THRESHOLDS = [200, 500, 1000, 2000, 5000, 10000]
TEMPLATE_MARKER = "<!--"


def parse_arguments() -> argparse.Namespace:
    """Read the command line arguments."""
    parser = argparse.ArgumentParser(
        description="Describe a pull request detail dataset."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="JSONL file holding the pull request detail objects.",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Markdown file the report is written to.",
    )
    return parser.parse_args()


def resolve_path(raw_path: str) -> Path:
    """Interpret a relative path as relative to the project root."""
    path = Path(raw_path)
    return path if path.is_absolute() else PROJECT_ROOT / path


def is_empty(value: Any) -> bool:
    """Treat None and empty containers or strings as unpopulated."""
    return value is None or (isinstance(value, (list, dict, str))
                             and len(value) == 0)


def percentile(sorted_values: list[int], share: float) -> float:
    """Return the value at the given share of a sorted list."""
    if not sorted_values:
        return 0.0
    position = (len(sorted_values) - 1) * share
    lower = int(position)
    upper = min(lower + 1, len(sorted_values) - 1)
    weight = position - lower
    return sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight


def outcome_of(record: dict[str, Any]) -> str:
    """Derive the outcome of a pull request from its state fields."""
    if record.get("merged_at"):
        return "merged"
    if record.get("state") == "closed":
        return "closed_unmerged"
    return "open"


def author_of(record: dict[str, Any]) -> tuple[str, str]:
    """Return login and account type of the pull request author."""
    user = record.get("user") or {}
    return user.get("login", "unknown"), user.get("type", "unknown")


def looks_like_bot(login: str, account_type: str) -> bool:
    """Apply the documented bot detection rule."""
    return account_type == "Bot" or login.endswith("[bot]")


def field_coverage(records: list[dict[str, Any]]) -> list[str]:
    """Report how often each top level field carries a value."""
    keys: list[str] = []
    for record in records:
        for key in record:
            if key not in keys:
                keys.append(key)

    lines = ["| Field | Populated | Share | Value types |",
             "|---|---|---|---|"]
    for key in sorted(keys):
        populated = 0
        kinds: Counter[str] = Counter()
        for record in records:
            value = record.get(key)
            kinds[type(value).__name__] += 1
            if not is_empty(value):
                populated += 1
        share = 100 * populated / len(records)
        kind_text = ", ".join(f"{name} {count}"
                              for name, count in kinds.most_common())
        lines.append(f"| `{key}` | {populated} | {share:.1f} % | {kind_text} |")
    return lines


def number_row(title: str, values: list[int]) -> str:
    """Format one distribution row of a markdown table."""
    ordered = sorted(values)
    if not ordered:
        return f"| {title} | - | - | - | - | - | - | - | - |"
    return (
        f"| {title} | {min(ordered)} | "
        f"{percentile(ordered, 0.5):.0f} | "
        f"{percentile(ordered, 0.75):.0f} | "
        f"{percentile(ordered, 0.90):.0f} | "
        f"{percentile(ordered, 0.95):.0f} | "
        f"{percentile(ordered, 0.99):.0f} | "
        f"{max(ordered)} | {sum(ordered)} |"
    )


def build_report(
    records: list[dict[str, Any]],
    source_path: Path,
    checksum: str,
) -> str:
    """Assemble the full markdown report."""
    total = len(records)
    lines: list[str] = []
    add = lines.append
    header = ("| Measure | min | median | p75 | p90 | p95 | p99 | max "
              "| total |")
    ruler = "|---|---|---|---|---|---|---|---|---|"

    add("# Findings: pull request details")
    add("")
    add(f"Created: {datetime.now(timezone.utc).isoformat()}")
    add(f"Source: `{source_path.name}`")
    add(f"SHA-256 of source: `{checksum}`")
    add(f"Records: {total}")
    add("")
    add("Produced by `src/collect/analyze_pull_details.py`. "
        "No API requests.")
    add("")

    add("## 1 Field coverage")
    add("")
    add("Unpopulated means null, empty list, empty object or empty string.")
    add("")
    lines.extend(field_coverage(records))
    add("")

    add("## 2 Authors and bots")
    add("")
    authors = [author_of(record) for record in records]
    logins = Counter(login for login, _ in authors)
    types = Counter(account_type for _, account_type in authors)
    bot_logins = Counter(
        login for login, account_type in authors
        if looks_like_bot(login, account_type)
    )
    add(f"Distinct authors: {len(logins)}")
    add(f"Detected as bot: {sum(bot_logins.values())} of {total} "
        f"pull requests, {len(bot_logins)} distinct accounts")
    add("")
    add("| Account type | Pull requests |")
    add("|---|---|")
    for account_type, count in types.most_common():
        add(f"| `{account_type}` | {count} |")
    add("")
    if bot_logins:
        add("| Bot account | Pull requests |")
        add("|---|---|")
        for login, count in bot_logins.most_common():
            add(f"| `{login}` | {count} |")
    else:
        add("No account matches the bot rule.")
    add("")
    add("Distribution without account names, data minimisation per "
        "`docs/entscheidungen.md`.")
    add("")
    add("| Rank | Pull requests |")
    add("|---|---|")
    for rank, (_, count) in enumerate(logins.most_common(), start=1):
        add(f"| {rank} | {count} |")
    add("")

    add("## 3 Outcome of the pull requests")
    add("")
    outcomes = Counter(outcome_of(record) for record in records)
    add("| outcome | Count | Share |")
    add("|---|---|---|")
    for name, count in outcomes.most_common():
        add(f"| `{name}` | {count} | {100 * count / total:.1f} % |")
    add("")

    add("## 4 Size of the changes")
    add("")
    additions = [int(r.get("additions") or 0) for r in records]
    deletions = [int(r.get("deletions") or 0) for r in records]
    changed = [int(r.get("changed_files") or 0) for r in records]
    touched = [a + d for a, d in zip(additions, deletions)]
    add(header)
    add(ruler)
    add(number_row("additions", additions))
    add(number_row("deletions", deletions))
    add(number_row("additions + deletions", touched))
    add(number_row("changed_files", changed))
    add("")
    add("### Effect of candidate thresholds")
    add("")
    add("Lines means `additions + deletions`.")
    add("")
    add("| Threshold | PRs above | Share of PRs | Share of all lines |")
    add("|---|---|---|---|")
    total_lines = sum(touched) or 1
    for threshold in SIZE_THRESHOLDS:
        above = [value for value in touched if value > threshold]
        add(f"| > {threshold} lines | {len(above)} | "
            f"{100 * len(above) / total:.1f} % | "
            f"{100 * sum(above) / total_lines:.1f} % |")
    add("")

    add("## 5 Comments")
    add("")
    issue_comments = [int(r.get("comments") or 0) for r in records]
    review_comments = [int(r.get("review_comments") or 0) for r in records]
    commits = [int(r.get("commits") or 0) for r in records]
    add(header)
    add(ruler)
    add(number_row("comments", issue_comments))
    add(number_row("review_comments", review_comments))
    add(number_row("commits", commits))
    add("")
    silent = sum(1 for a, b in zip(issue_comments, review_comments)
                 if a + b == 0)
    add(f"Pull requests without any comment: {silent}")
    add(f"Pull requests with review comments: "
        f"{sum(1 for value in review_comments if value > 0)}")
    add("")

    add("## 6 Description texts")
    add("")
    bodies = [record.get("body") for record in records]
    missing = sum(1 for body in bodies if body is None)
    blank = sum(1 for body in bodies if body is not None and not body.strip())
    with_template = sum(1 for body in bodies
                        if body and TEMPLATE_MARKER in body)
    with_crlf = sum(1 for body in bodies if body and "\r\n" in body)
    add(f"Without description (null): {missing}")
    add(f"Description is whitespace only: {blank}")
    add(f"Contains template text (`{TEMPLATE_MARKER}`): {with_template}")
    add(f"Contains CRLF line endings: {with_crlf}")
    add("")
    body_lengths = [len(body) for body in bodies if body]
    add(header)
    add(ruler)
    add(number_row("characters per description", body_lengths))
    add("")

    return "\n".join(lines) + "\n"


def main() -> int:
    arguments = parse_arguments()
    source_path = resolve_path(arguments.source)
    if not source_path.is_file():
        print(f"Source file not found: {source_path}")
        return 1

    records = read_jsonl(source_path)
    if not records:
        print(f"No records found in {source_path}")
        return 1

    report = build_report(records, source_path, sha256_of(source_path))

    output_path = resolve_path(arguments.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"Report written to: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())