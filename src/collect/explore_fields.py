"""Explore the field structure of a pull request object.

Work package D, RQ1. Basis for the reasoned field selection and data
minimisation: fetches a single pull request and lists the available
fields with type and a shortened preview. Nothing is stored.
"""

from __future__ import annotations

import sys
from typing import Any

import requests

from github_api import build_headers, load_config, load_token

PREVIEW_LENGTH = 60


def preview(value: Any) -> str:
    """Return a short single-line preview of a field value."""
    if value is None:
        return "None"
    if isinstance(value, (list, dict)):
        return f"{len(value)} entries"
    text = " ".join(str(value).split())
    if len(text) > PREVIEW_LENGTH:
        return f"{text[:PREVIEW_LENGTH]} ... ({len(text)} characters)"
    return text


def main() -> int:
    config = load_config()
    headers = build_headers(load_token(), config["api"]["version"])

    url = (f"{config['api']['base_url']}/repos/{config['source']['owner']}"
           f"/{config['source']['repo']}/pulls")

    response = requests.get(
        url,
        headers=headers,
        params={"state": config["api"]["state"], "per_page": 1, "page": 1},
        timeout=config["fetch"]["timeout_seconds"],
    )
    response.raise_for_status()

    page = response.json()
    if not page:
        print("The API returned no pull request.")
        return 1

    pull_request = page[0]
    print(f"Pull request #{pull_request.get('number')}")
    print(f"Top-level fields: {len(pull_request)}")
    print("-" * 76)
    for name in sorted(pull_request):
        type_name = type(pull_request[name]).__name__
        print(f"{name:26} {type_name:6} {preview(pull_request[name])}")

    print("-" * 76)
    for nested in ("user", "head", "base"):
        content = pull_request.get(nested)
        if isinstance(content, dict):
            print(f"{nested}: {', '.join(sorted(content))}")
            print()

    print("-" * 76)
    print(f"Rate limit remaining: "
          f"{response.headers.get('x-ratelimit-remaining')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
