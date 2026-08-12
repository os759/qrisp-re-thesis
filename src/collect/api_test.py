"""Connectivity check against the GitHub REST API.

Work package D, RQ1. Verifies that configuration and credentials load
correctly and that the API responds with the expected rate limit.
The token itself is never printed, only its length.
"""

from __future__ import annotations

import sys

import requests

from github_api import CONFIG_PATH, build_headers, load_config, load_token


def main() -> int:
    config = load_config()
    token = load_token()
    api_version = config["api"]["version"]

    response = requests.get(
        f"{config['api']['base_url']}/rate_limit",
        headers=build_headers(token, api_version),
        timeout=config["fetch"]["timeout_seconds"],
    )
    response.raise_for_status()
    core = response.json()["resources"]["core"]

    print(f"Configuration loaded:  {CONFIG_PATH}")
    print(f"Token loaded:          {len(token)} characters")
    print(f"API version requested: {api_version}")
    print(f"API version accepted:  "
          f"{response.headers.get('x-github-api-version-selected')}")
    print(f"Status code:           {response.status_code}")
    print(f"Rate limit:            {core['remaining']} of {core['limit']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
