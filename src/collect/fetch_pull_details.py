"""Fetch the detail object for every pull request in a collected list.

Work package D, RQ1. The list endpoint returns 36 fields per pull
request, the detail endpoint 48. This script reads the pull request
numbers from a previously collected list file, requests the detail
endpoint once per number and appends each raw response to a JSON Lines
file. An interrupted run can be resumed: numbers already present in the
output file are skipped. A manifest records the collection time, the
parameters, the source dataset with its checksum and a checksum of the
output file.
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
    load_config,
    load_token,
    read_jsonl,
    request_with_retry,
    sha256_of,
)

RAW_DIR = PROJECT_ROOT / "data" / "raw"
MANIFEST_DIR = PROJECT_ROOT / "data" / "manifests"
PROGRESS_EVERY = 25


def parse_arguments() -> argparse.Namespace:
    """Read the command line arguments."""
    parser = argparse.ArgumentParser(
        description="Fetch pull request details for a collected list."
    )
    parser.add_argument(
        "--source",
        required=True,
        help="JSONL file holding the collected pull request list.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Fetch at most this many pull requests (trial run).",
    )
    parser.add_argument(
        "--day",
        default=None,
        help="Date stamp of the output file (YYYY-MM-DD). Pass the "
             "original date to resume a run started on an earlier day.",
    )
    return parser.parse_args()


def resolve_path(raw_path: str) -> Path:
    """Interpret a relative path as relative to the project root."""
    path = Path(raw_path)
    return path if path.is_absolute() else PROJECT_ROOT / path


def pull_numbers_from(path: Path) -> list[int]:
    """Return the sorted, distinct pull request numbers of a list file."""
    records = read_jsonl(path)
    if not records:
        raise ValueError(f"No records found in {path}")
    numbers = sorted({int(record["number"]) for record in records})
    if len(numbers) != len(records):
        print(f"NOTE: {len(records)} records hold {len(numbers)} "
              f"distinct numbers.")
    return numbers


def numbers_in_output(path: Path) -> set[int]:
    """Return the pull request numbers already present in the output."""
    return {int(record["number"]) for record in read_jsonl(path)}


def build_manifest(
    config: dict[str, Any],
    collected_at: datetime,
    source_path: Path,
    output_path: Path,
    wanted: list[int],
    stored: set[int],
    failures: list[dict[str, Any]],
) -> dict[str, Any]:
    """Assemble the manifest describing this collection run."""
    return {
        "collected_at_utc": collected_at.isoformat(),
        "repository": config["source"]["repo_id"],
        "repository_full_name": (f"{config['source']['owner']}"
                                 f"/{config['source']['repo']}"),
        "endpoint": "pulls_detail",
        "api_version": config["api"]["version"],
        "parameters": {
            "pause_seconds": config["fetch"]["pause_seconds"],
            "max_retries": config["fetch"]["max_retries"],
            "timeout_seconds": config["fetch"]["timeout_seconds"],
        },
        "source_dataset": {
            "file": source_path.name,
            "sha256": sha256_of(source_path),
            "record_count": len(wanted),
        },
        "record_count": len(stored),
        "number_min": min(stored) if stored else None,
        "number_max": max(stored) if stored else None,
        "missing_numbers": [n for n in wanted if n not in stored],
        "failures": failures,
        "output_file": output_path.name,
        "sha256": sha256_of(output_path),
        "collector_commit": current_commit(),
    }


def main() -> int:
    arguments = parse_arguments()
    config = load_config()
    headers = build_headers(load_token(), config["api"]["version"])
    timeout = config["fetch"]["timeout_seconds"]
    pause = config["fetch"]["pause_seconds"]
    max_retries = config["fetch"]["max_retries"]

    source_path = resolve_path(arguments.source)
    if not source_path.is_file():
        print(f"Source file not found: {source_path}")
        return 1

    collected_at = datetime.now(timezone.utc)
    day = arguments.day or collected_at.strftime("%Y-%m-%d")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RAW_DIR / f"pull_details_{day}.jsonl"

    wanted = pull_numbers_from(source_path)
    stored = numbers_in_output(output_path)
    missing = [number for number in wanted if number not in stored]
    if arguments.limit is not None:
        missing = missing[: arguments.limit]

    print(f"Source list:      {source_path.name} ({len(wanted)} numbers)")
    print(f"Output file:      {output_path.name}")
    print(f"Already present:  {len(stored)}")
    print(f"Fetching now:     {len(missing)}")
    print()

    base_url = (f"{config['api']['base_url']}"
                f"/repos/{config['source']['owner']}"
                f"/{config['source']['repo']}/pulls")
    failures: list[dict[str, Any]] = []

    for position, number in enumerate(missing, start=1):
        response = request_with_retry(
            f"{base_url}/{number}", headers, timeout, max_retries
        )
        if response.status_code != 200:
            print(f"  #{number}: HTTP {response.status_code} - skipped")
            failures.append({
                "number": number,
                "status_code": response.status_code,
            })
            continue
        append_jsonl(response.json(), output_path)
        if position % PROGRESS_EVERY == 0 or position == len(missing):
            print(f"  {position}/{len(missing)} fetched, last #{number}, "
                  f"rate limit left "
                  f"{response.headers.get('x-ratelimit-remaining')}")
        time.sleep(pause)

    if not output_path.is_file():
        print("No records written, no manifest created.")
        return 1

    stored = numbers_in_output(output_path)
    manifest = build_manifest(
        config, collected_at, source_path, output_path,
        wanted, stored, failures,
    )
    manifest_path = MANIFEST_DIR / f"manifest_pull_details_{day}.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print()
    print(f"Records in file:  {manifest['record_count']} of {len(wanted)}")
    print(f"Still missing:    {len(manifest['missing_numbers'])}")
    print(f"Failed requests:  {len(failures)}")
    print(f"Data file:        {output_path}")
    print(f"Manifest:         {manifest_path}")
    print(f"SHA-256:          {manifest['sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())