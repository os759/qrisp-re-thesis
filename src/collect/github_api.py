"""Shared building blocks for accessing the GitHub REST API.

Work package D, RQ1. Loads configuration and credentials and builds the
HTTP headers, so that every collection script uses the same documented
basis.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
import tomllib
from pathlib import Path
from typing import Any

import requests

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "config" / "collect.toml"
ENV_PATH = PROJECT_ROOT / ".env"


def load_config(path: Path = CONFIG_PATH) -> dict[str, Any]:
    """Read the TOML configuration file."""
    if not path.is_file():
        raise FileNotFoundError(f"Configuration file missing: {path}")
    with path.open("rb") as file:
        return tomllib.load(file)


def load_token(path: Path = ENV_PATH, key: str = "GITHUB_TOKEN") -> str:
    """Read a single value from the .env file."""
    if not path.is_file():
        raise FileNotFoundError(f"Credentials file missing: {path}")
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, _, value = line.partition("=")
        if name.strip() == key:
            value = value.strip()
            if not value:
                raise ValueError(f"{key} in {path} is empty.")
            return value
    raise KeyError(f"{key} not found in {path}.")


def build_headers(token: str, api_version: str) -> dict[str, str]:
    """Build the HTTP headers sent with every GitHub API request."""
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": api_version,
    }

def sha256_of(path: Path) -> str:
    """Return the SHA-256 checksum of a file."""
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def current_commit() -> str:
    """Return the current Git commit hash, or 'unknown' if unavailable."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """Read a JSON Lines file into a list, skipping blank lines."""
    if not path.is_file():
        return []
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"{path} line {line_number} is not valid JSON: {error}"
                ) from error
    return records


def append_jsonl(record: dict[str, Any], path: Path) -> None:
    """Append a single JSON object as one line to a JSON Lines file."""
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def retry_delay_seconds(response: requests.Response, fallback: int) -> int:
    """Derive the wait time from GitHub's rate limit response headers."""
    retry_after = response.headers.get("retry-after")
    if retry_after and retry_after.isdigit():
        return int(retry_after)
    if response.headers.get("x-ratelimit-remaining") == "0":
        reset = response.headers.get("x-ratelimit-reset")
        if reset and reset.isdigit():
            return max(int(reset) - int(time.time()) + 5, 1)
    return fallback


def request_with_retry(
    url: str,
    headers: dict[str, str],
    timeout: int,
    max_retries: int,
    params: dict[str, Any] | None = None,
) -> requests.Response:
    """Send a GET request, retrying on rate limits and server errors.

    Returns the response for every status the caller has to handle
    itself, including 404. Raises RuntimeError if all attempts fail.
    """
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(
                url, headers=headers, params=params, timeout=timeout
            )
        except requests.RequestException as error:
            wait = 2 ** attempt
            print(f"    network error ({error}); retry in {wait}s "
                  f"[{attempt}/{max_retries}]")
            time.sleep(wait)
            continue

        if response.status_code in (403, 429):
            wait = retry_delay_seconds(response, fallback=2 ** attempt)
            print(f"    rate limited (HTTP {response.status_code}); "
                  f"waiting {wait}s [{attempt}/{max_retries}]")
            time.sleep(wait)
            continue

        if 500 <= response.status_code < 600:
            wait = 2 ** attempt
            print(f"    server error (HTTP {response.status_code}); "
                  f"retry in {wait}s [{attempt}/{max_retries}]")
            time.sleep(wait)
            continue

        return response

    raise RuntimeError(f"Giving up after {max_retries} attempts: {url}")