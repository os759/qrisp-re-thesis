"""Shared building blocks for accessing the GitHub REST API.

Work package D, RQ1. Loads configuration and credentials and builds the
HTTP headers, so that every collection script uses the same documented
basis.
"""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

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
