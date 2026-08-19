"""Describe a collected pull request file dataset.

Work package D, RQ1. Reads a JSON Lines file of changed file records
and reports change status, file extensions, directories, patch sizes
and the composition of the largest pull requests. The file is read line
by line, because the patch texts together are far larger than the other
raw datasets. The script sends no API requests.

Its output decides the open part of decision D1: whether the truncation
rule stays a line threshold per pull request or becomes a rule by file
type.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Iterator

from github_api import PROJECT_ROOT, sha256_of

DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "findings_pull_files.md"
TOP_EXTENSIONS = 20
TOP_PULLS = 15
CHAR_THRESHOLDS = [10_000, 50_000, 100_000, 250_000, 500_000, 1_000_000]


def parse_arguments() -> argparse.Namespace:
    """Read the command line arguments."""
    parser = argparse.ArgumentParser(
        description="Describe a pull request file dataset."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="JSONL file holding the changed file records.",
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


def stream_records(path: Path) -> Iterator[dict[str, Any]]:
    """Yield one record per line without holding the whole file."""
    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"{path} line {line_number} is not valid JSON: {error}"
                ) from error


def extension_of(filename: str) -> str:
    """Return the lower case file extension, or a placeholder."""
    suffix = PurePosixPath(filename).suffix.lower()
    return suffix if suffix else "(no extension)"


def top_directory_of(filename: str) -> str:
    """Return the first path component, or a placeholder."""
    parts = PurePosixPath(filename).parts
    return parts[0] if len(parts) > 1 else "(repository root)"


def percentile(sorted_values: list[int], share: float) -> float:
    """Return the value at the given share of a sorted list."""
    if not sorted_values:
        return 0.0
    position = (len(sorted_values) - 1) * share
    lower = int(position)
    upper = min(lower + 1, len(sorted_values) - 1)
    weight = position - lower
    return sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight


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


class Tally:
    """Collect every figure the report needs in a single pass."""

    def __init__(self) -> None:
        self.records = 0
        self.status = Counter()
        self.files_per_extension = Counter()
        self.chars_per_extension = Counter()
        self.files_per_directory = Counter()
        self.chars_per_directory = Counter()
        self.patch_lengths: list[int] = []
        self.missing_patch_extensions = Counter()
        self.missing_patch_count = 0
        self.files_per_pull = Counter()
        self.chars_per_pull = Counter()
        self.extension_chars_per_pull: dict[int, Counter] = defaultdict(
            Counter
        )

    def add(self, record: dict[str, Any]) -> None:
        """Fold one file record into the running totals."""
        self.records += 1
        filename = record.get("filename", "")
        extension = extension_of(filename)
        directory = top_directory_of(filename)
        number = int(record.get("collected_pull_number", -1))
        patch = record.get("patch")
        length = len(patch) if patch is not None else 0

        self.status[record.get("status", "unknown")] += 1
        self.files_per_extension[extension] += 1
        self.chars_per_extension[extension] += length
        self.files_per_directory[directory] += 1
        self.chars_per_directory[directory] += length
        self.files_per_pull[number] += 1
        self.chars_per_pull[number] += length
        self.extension_chars_per_pull[number][extension] += length

        if patch is None:
            self.missing_patch_count += 1
            self.missing_patch_extensions[extension] += 1
        else:
            self.patch_lengths.append(length)


def build_report(tally: Tally, source_path: Path, checksum: str) -> str:
    """Assemble the full markdown report."""
    lines: list[str] = []
    add = lines.append
    total_chars = sum(tally.chars_per_pull.values()) or 1
    header = ("| Measure | min | median | p75 | p90 | p95 | p99 | max "
              "| total |")
    ruler = "|---|---|---|---|---|---|---|---|---|"

    add("# Findings: changed files and diffs")
    add("")
    add(f"Created: {datetime.now(timezone.utc).isoformat()}")
    add(f"Source: `{source_path.name}`")
    add(f"SHA-256 of source: `{checksum}`")
    add(f"File records: {tally.records}")
    add(f"Pull requests with at least one file: "
        f"{len(tally.files_per_pull)}")
    add(f"Characters of patch text: {total_chars}")
    add("")
    add("Produced by `src/collect/analyze_pull_files.py`. No API requests.")
    add("")

    add("## 1 Kind of change")
    add("")
    add("| status | Files | Share |")
    add("|---|---|---|")
    for name, count in tally.status.most_common():
        add(f"| `{name}` | {count} | "
            f"{100 * count / tally.records:.1f} % |")
    add("")

    add("## 2 File extensions")
    add("")
    add(f"The {TOP_EXTENSIONS} extensions holding the most patch text.")
    add("")
    add("| Extension | Files | Characters | Share of characters |")
    add("|---|---|---|---|")
    for extension, chars in tally.chars_per_extension.most_common(
            TOP_EXTENSIONS):
        add(f"| `{extension}` | {tally.files_per_extension[extension]} | "
            f"{chars} | {100 * chars / total_chars:.1f} % |")
    add("")

    add("## 3 Top level directories")
    add("")
    add("| Directory | Files | Characters | Share of characters |")
    add("|---|---|---|---|")
    for directory, chars in tally.chars_per_directory.most_common(
            TOP_EXTENSIONS):
        add(f"| `{directory}` | {tally.files_per_directory[directory]} | "
            f"{chars} | {100 * chars / total_chars:.1f} % |")
    add("")

    add("## 4 Files delivered without a patch")
    add("")
    add(f"GitHub omits the `patch` field for "
        f"{tally.missing_patch_count} of {tally.records} files "
        f"({100 * tally.missing_patch_count / tally.records:.1f} %).")
    add("")
    add("| Extension | Files without patch |")
    add("|---|---|")
    for extension, count in tally.missing_patch_extensions.most_common(
            TOP_EXTENSIONS):
        add(f"| `{extension}` | {count} |")
    add("")

    add("## 5 Size of the patch text")
    add("")
    add(header)
    add(ruler)
    add(number_row("characters per file", tally.patch_lengths))
    add(number_row("characters per pull request",
                   list(tally.chars_per_pull.values())))
    add(number_row("files per pull request",
                   list(tally.files_per_pull.values())))
    add("")
    add("### Effect of candidate thresholds per pull request")
    add("")
    add("| Threshold | PRs above | Share of PRs | Share of all characters |")
    add("|---|---|---|---|")
    pull_count = len(tally.chars_per_pull) or 1
    for threshold in CHAR_THRESHOLDS:
        above = [value for value in tally.chars_per_pull.values()
                 if value > threshold]
        add(f"| > {threshold} characters | {len(above)} | "
            f"{100 * len(above) / pull_count:.1f} % | "
            f"{100 * sum(above) / total_chars:.1f} % |")
    add("")

    add("## 6 The largest pull requests")
    add("")
    add(f"The {TOP_PULLS} pull requests holding the most patch text, each "
        f"with its three strongest extensions.")
    add("")
    add("| PR | Files | Characters | Share | Strongest extensions |")
    add("|---|---|---|---|---|")
    for number, chars in tally.chars_per_pull.most_common(TOP_PULLS):
        top = tally.extension_chars_per_pull[number].most_common(3)
        detail = ", ".join(
            f"{extension} {100 * value / (chars or 1):.0f} %"
            for extension, value in top
        )
        add(f"| #{number} | {tally.files_per_pull[number]} | {chars} | "
            f"{100 * chars / total_chars:.1f} % | {detail} |")
    add("")

    return "\n".join(lines) + "\n"


def main() -> int:
    arguments = parse_arguments()
    source_path = resolve_path(arguments.source)
    if not source_path.is_file():
        print(f"Source file not found: {source_path}")
        return 1

    tally = Tally()
    for record in stream_records(source_path):
        tally.add(record)
    if tally.records == 0:
        print(f"No records found in {source_path}")
        return 1

    report = build_report(tally, source_path, sha256_of(source_path))

    output_path = resolve_path(arguments.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"Report written to: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())