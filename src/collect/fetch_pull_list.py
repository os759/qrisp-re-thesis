"""Fetch the full pull request list of the configured repository.

Work package D, RQ1. Walks all pages of the list endpoint, stores the
raw responses as JSON Lines and writes a manifest documenting the
collection time, the parameters used and a checksum of the output file.
Raw data stays outside the repository; only the manifest is versioned.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

from github_api import (
    PROJECT_ROOT,
    build_headers,
    current_commit,
    load_config,
    load_token,
    sha256_of,
)

RAW_DIR = PROJECT_ROOT / "data" / "raw"
MANIFEST_DIR = PROJECT_ROOT / "data" / "manifests"


def fetch_all_pages(
    url: str,
    headers: dict[str, str],
    params: dict[str, Any],
    timeout: int,
) -> list[dict[str, Any]]:
    """Fetch every page of a paginated endpoint, following the link header."""
    records: list[dict[str, Any]] = []
    page = 1
    while True:
        response = requests.get(
            url, headers=headers, params={**params, "page": page},
            timeout=timeout,
        )
        response.raise_for_status()
        batch = response.json()
        if not batch:
            break
        records.extend(batch)
        print(f"  page {page}: {len(batch)} records "
              f"(total {len(records)}, rate limit left "
              f"{response.headers.get('x-ratelimit-remaining')})")
        if 'rel="next"' not in response.headers.get("link", ""):
            break
        page += 1
    return records


def write_jsonl(records: list[dict[str, Any]], path: Path) -> None:
    """Write one JSON object per line."""
    with path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> int:
    config = load_config()
    headers = build_headers(load_token(), config["api"]["version"])
    collected_at = datetime.now(timezone.utc)
    day = collected_at.strftime("%Y-%m-%d")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RAW_DIR / f"pulls_{day}.jsonl"

    if output_path.exists():
        print(f"File already exists: {output_path}")
        print("Delete or rename it before collecting again.")
        return 1

    params = {
        "state": config["api"]["state"],
        "per_page": config["api"]["per_page"],
    }
    url = (f"{config['api']['base_url']}/repos/{config['source']['owner']}"
           f"/{config['source']['repo']}/pulls")

    print(f"Fetching pull request list from {config['source']['owner']}"
          f"/{config['source']['repo']} ...")
    records = fetch_all_pages(
        url, headers, params, config["fetch"]["timeout_seconds"]
    )

    numbers = [record["number"] for record in records]
    if len(set(numbers)) != len(numbers):
        print("WARNING: duplicate pull request numbers in the result.")

    write_jsonl(records, output_path)

    manifest = {
        "collected_at_utc": collected_at.isoformat(),
        "repository": config["source"]["repo_id"],
        "repository_full_name": (f"{config['source']['owner']}"
                                 f"/{config['source']['repo']}"),
        "endpoint": "pulls_list",
        "api_version": config["api"]["version"],
        "parameters": params,
        "record_count": len(records),
        "number_min": min(numbers) if numbers else None,
        "number_max": max(numbers) if numbers else None,
        "output_file": output_path.name,
        "sha256": sha256_of(output_path),
        "collector_commit": current_commit(),
    }
    manifest_path = MANIFEST_DIR / f"manifest_pulls_{day}.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print()
    print(f"Records written:  {len(records)}")
    print(f"Number range:     #{manifest['number_min']} to "
          f"#{manifest['number_max']}")
    print(f"Data file:        {output_path}")
    print(f"Manifest:         {manifest_path}")
    print(f"SHA-256:          {manifest['sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
