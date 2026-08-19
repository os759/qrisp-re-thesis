"""Fetch the changed files and diffs of every pull request.

Work package D, RQ1. For every pull request the files endpoint returns
one record per changed file, holding the path, the change status, the
line counts and, unless the file is too large or binary, the patch text
itself. Nothing is shortened here: decision D1 places truncation in the
preparation step, not in the collection step.

For every pull request a progress record is written, including those
without any changed file. An interrupted run resumes from that progress
file. The detail dataset supplies the expected number of changed files;
every deviation is reported and stored in the manifest. The progress
record also counts files delivered without a patch, because the API
omits the patch for very large or binary files.
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
FILE_STEM = "pull_files"


def parse_arguments() -> argparse.Namespace:
    """Read the command line arguments."""
    parser = argparse.ArgumentParser(
        description="Fetch changed files and diffs per pull request."
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


def expected_counts(records: list[dict[str, Any]]) -> dict[int, int]:
    """Map every pull request number to its documented file count."""
    return {int(record["number"]): int(record.get("changed_files") or 0)
            for record in records}


def handled_numbers(path: Path) -> set[int]:
    """Return the pull request numbers already handled, from progress."""
    return {int(record["number"]) for record in read_jsonl(path)}


def main() -> int:
    arguments = parse_arguments()
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
    output_path = RAW_DIR / f"{FILE_STEM}_{day}.jsonl"
    progress_path = RAW_DIR / f"{FILE_STEM}_{day}.progress.jsonl"

    details = read_jsonl(source_path)
    if not details:
        print(f"No records found in {source_path}")
        return 1
    expected = expected_counts(details)
    done = handled_numbers(progress_path)
    todo = [number for number in sorted(expected) if number not in done]
    if arguments.limit is not None:
        todo = todo[: arguments.limit]

    print(f"Source detail:    {source_path.name} ({len(expected)} numbers)")
    print(f"Output file:      {output_path.name}")
    print(f"Progress file:    {progress_path.name}")
    print(f"Already handled:  {len(done)}")
    print(f"Handling now:     {len(todo)}")
    print(f"Expected total:   {sum(expected.values())} changed files")
    print()

    base_url = (f"{config['api']['base_url']}"
                f"/repos/{config['source']['owner']}"
                f"/{config['source']['repo']}")
    failures: list[dict[str, Any]] = []

    for position, number in enumerate(todo, start=1):
        records, status = fetch_paginated(
            f"{base_url}/pulls/{number}/files", headers, timeout,
            max_retries, per_page=per_page, pause=pause,
        )
        if status != 200:
            print(f"  #{number}: HTTP {status} - skipped")
            failures.append({"number": number, "status_code": status})
            continue
        without_patch = 0
        patch_characters = 0
        for record in records:
            record["collected_pull_number"] = number
            patch = record.get("patch")
            if patch is None:
                without_patch += 1
            else:
                patch_characters += len(patch)
            append_jsonl(record, output_path)
        append_jsonl(
            {
                "number": number,
                "fetched": len(records),
                "expected": expected[number],
                "files_without_patch": without_patch,
                "patch_characters": patch_characters,
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
    without_patch_total = sum(int(entry["files_without_patch"])
                              for entry in progress)
    patch_characters_total = sum(int(entry["patch_characters"])
                                 for entry in progress)
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
        "endpoint": "pull_files",
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
        "files_without_patch": without_patch_total,
        "patch_characters": patch_characters_total,
        "deviations": deviations,
        "failures": failures,
        "output_file": output_path.name,
        "sha256": sha256_of(output_path) if output_path.is_file() else None,
        "progress_file": progress_path.name,
        "progress_sha256": sha256_of(progress_path),
        "collector_commit": current_commit(),
    }
    manifest_path = MANIFEST_DIR / f"manifest_{FILE_STEM}_{day}.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print()
    print(f"Pull requests:    {len(handled)} of {len(expected)}")
    print(f"Files stored:     {fetched_total}")
    print(f"Files expected:   {manifest['expected_count']}")
    print(f"Without patch:    {without_patch_total}")
    print(f"Patch characters: {patch_characters_total}")
    print(f"Deviations:       {len(deviations)}")
    print(f"Failed requests:  {len(failures)}")
    print(f"Data file:        {output_path}")
    print(f"Manifest:         {manifest_path}")
    print(f"SHA-256:          {manifest['sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())