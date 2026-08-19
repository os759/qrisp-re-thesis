"""Fetch the comments of every pull request in a collected dataset.

Work package D, RQ1. Two kinds of comment exist on a pull request:
general conversation comments, served by the issues endpoint, and
review comments attached to a line of code, served by the pulls
endpoint. This script fetches one kind per run and writes one raw file
per kind.

For every pull request a progress record is written, including those
without any comment. An interrupted run resumes from that progress
file. The detail dataset supplies the expected number of comments per
pull request; every deviation is reported and stored in the manifest.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from github_api import (
    PROJECT_ROOT,
    append_jsonl,
    build_headers,
    current_commit,
    fetch_paginated,
    load_config,
    load_token,
    read_jsonl,
    sha256_of,
)

RAW_DIR = PROJECT_ROOT / "data" / "raw"
MANIFEST_DIR = PROJECT_ROOT / "data" / "manifests"
PROGRESS_EVERY = 25

KINDS = {
    "issue": {
        "path": "issues/{number}/comments",
        "expected_field": "comments",
        "file_stem": "issue_comments",
    },
    "review": {
        "path": "pulls/{number}/comments",
        "expected_field": "review_comments",
        "file_stem": "review_comments",
    },
}


def parse_arguments() -> argparse.Namespace:
    """Read the command line arguments."""
    parser = argparse.ArgumentParser(
        description="Fetch pull request comments of one kind."
    )
    parser.add_argument(
        "--kind",
        required=True,
        choices=sorted(KINDS),
        help="issue for conversation comments, review for code comments.",
    )
    parser.add_argument(
        "--source",
        required=True,
        help="JSONL file holding the pull request detail objects.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Handle at most this many pull requests (trial run).",
    )
    parser.add_argument(
        "--day",
        default=None,
        help="Date stamp of the output files (YYYY-MM-DD).",
    )
    return parser.parse_args()


def resolve_path(raw_path: str) -> Path:
    """Interpret a relative path as relative to the project root."""
    path = Path(raw_path)
    return path if path.is_absolute() else PROJECT_ROOT / path


def expected_counts(records: list[dict[str, Any]],
                    field: str) -> dict[int, int]:
    """Map every pull request number to its documented comment count."""
    return {int(record["number"]): int(record.get(field) or 0)
            for record in records}


def handled_numbers(path: Path) -> set[int]:
    """Return the pull request numbers already handled, from progress."""
    return {int(record["number"]) for record in read_jsonl(path)}


def main() -> int:
    arguments = parse_arguments()
    kind = KINDS[arguments.kind]
    config = load_config()
    headers = build_headers(load_token(), config["api"]["version"])
    timeout = config["fetch"]["timeout_seconds"]
    pause = config["fetch"]["pause_seconds"]
    max_retries = config["fetch"]["max_retries"]
    per_page = config["api"]["per_page"]

    source_path = resolve_path(arguments.source)
    if not source_path.is_file():
        print(f"Source file not found: {source_path}")
        return 1

    collected_at = datetime.now(timezone.utc)
    day = arguments.day or collected_at.strftime("%Y-%m-%d")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    stem = kind["file_stem"]
    output_path = RAW_DIR / f"{stem}_{day}.jsonl"
    progress_path = RAW_DIR / f"{stem}_{day}.progress.jsonl"

    details = read_jsonl(source_path)
    if not details:
        print(f"No records found in {source_path}")
        return 1
    expected = expected_counts(details, kind["expected_field"])
    done = handled_numbers(progress_path)
    todo = [number for number in sorted(expected) if number not in done]
    if arguments.limit is not None:
        todo = todo[: arguments.limit]

    print(f"Kind:             {arguments.kind} "
          f"({kind['expected_field']})")
    print(f"Source detail:    {source_path.name} ({len(expected)} numbers)")
    print(f"Output file:      {output_path.name}")
    print(f"Progress file:    {progress_path.name}")
    print(f"Already handled:  {len(done)}")
    print(f"Handling now:     {len(todo)}")
    print(f"Expected total:   {sum(expected.values())} comments")
    print()

    base_url = (f"{config['api']['base_url']}"
                f"/repos/{config['source']['owner']}"
                f"/{config['source']['repo']}")
    failures: list[dict[str, Any]] = []

    for position, number in enumerate(todo, start=1):
        path = kind["path"].format(number=number)
        records, status = fetch_paginated(
            f"{base_url}/{path}", headers, timeout, max_retries,
            per_page=per_page, pause=pause,
        )
        if status != 200:
            print(f"  #{number}: HTTP {status} - skipped")
            failures.append({"number": number, "status_code": status})
            continue
        for record in records:
            record["collected_pull_number"] = number
            append_jsonl(record, output_path)
        append_jsonl(
            {
                "number": number,
                "fetched": len(records),
                "expected": expected[number],
                "handled_at_utc": datetime.now(timezone.utc).isoformat(),
            },
            progress_path,
        )
        if position % PROGRESS_EVERY == 0 or position == len(todo):
            print(f"  {position}/{len(todo)} handled, last #{number}")
        time.sleep(pause)

    progress = read_jsonl(progress_path)
    if not progress:
        print("Nothing handled, no manifest created.")
        return 1

    fetched_total = sum(int(entry["fetched"]) for entry in progress)
    deviations = [
        {"number": int(entry["number"]),
         "expected": int(entry["expected"]),
         "fetched": int(entry["fetched"])}
        for entry in progress
        if int(entry["fetched"]) != int(entry["expected"])
    ]
    handled = {int(entry["number"]) for entry in progress}

    manifest = {
        "collected_at_utc": collected_at.isoformat(),
        "repository": config["source"]["repo_id"],
        "repository_full_name": (f"{config['source']['owner']}"
                                 f"/{config['source']['repo']}"),
        "endpoint": f"{arguments.kind}_comments",
        "api_version": config["api"]["version"],
        "parameters": {
            "per_page": per_page,
            "pause_seconds": pause,
            "max_retries": max_retries,
            "timeout_seconds": timeout,
        },
        "source_dataset": {
            "file": source_path.name,
            "sha256": sha256_of(source_path),
            "record_count": len(expected),
        },
        "added_fields": ["collected_pull_number"],
        "pull_requests_handled": len(handled),
        "pull_requests_missing": [n for n in sorted(expected)
                                  if n not in handled],
        "record_count": fetched_total,
        "expected_count": sum(expected.values()),
        "deviations": deviations,
        "failures": failures,
        "output_file": output_path.name,
        "sha256": sha256_of(output_path) if output_path.is_file() else None,
        "progress_file": progress_path.name,
        "progress_sha256": sha256_of(progress_path),
        "collector_commit": current_commit(),
    }
    manifest_path = MANIFEST_DIR / f"manifest_{stem}_{day}.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print()
    print(f"Pull requests:    {len(handled)} of {len(expected)}")
    print(f"Comments stored:  {fetched_total}")
    print(f"Comments expected:{manifest['expected_count']}")
    print(f"Deviations:       {len(deviations)}")
    print(f"Failed requests:  {len(failures)}")
    print(f"Data file:        {output_path}")
    print(f"Manifest:         {manifest_path}")
    print(f"SHA-256:          {manifest['sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())