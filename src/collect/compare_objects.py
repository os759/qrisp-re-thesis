"""Compare the pull request object from the list and detail endpoints.

Work package D, RQ1. Establishes empirically whether the list endpoint
returns a reduced object and therefore whether an additional detail
request per pull request is required. Nothing is stored.
"""

from __future__ import annotations

import sys

import requests

from github_api import build_headers, load_config, load_token


def main() -> int:
    config = load_config()
    headers = build_headers(load_token(), config["api"]["version"])
    timeout = config["fetch"]["timeout_seconds"]
    base_url = (f"{config['api']['base_url']}/repos"
                f"/{config['source']['owner']}/{config['source']['repo']}/pulls")

    list_response = requests.get(
        base_url,
        headers=headers,
        params={"state": config["api"]["state"], "per_page": 1, "page": 1},
        timeout=timeout,
    )
    list_response.raise_for_status()
    from_list = list_response.json()[0]
    number = from_list["number"]

    detail_response = requests.get(
        f"{base_url}/{number}", headers=headers, timeout=timeout
    )
    detail_response.raise_for_status()
    from_detail = detail_response.json()

    list_fields = set(from_list)
    detail_fields = set(from_detail)

    print(f"Compared pull request: #{number}")
    print(f"Fields in list object:   {len(list_fields)}")
    print(f"Fields in detail object: {len(detail_fields)}")
    print()

    detail_only = sorted(detail_fields - list_fields)
    print(f"Detail endpoint only ({len(detail_only)}):")
    for name in detail_only:
        print(f"  {name:22} = {from_detail[name]!r:.60}")
    print()

    list_only = sorted(list_fields - detail_fields)
    print(f"List endpoint only ({len(list_only)}):")
    for name in list_only:
        print(f"  {name}")
    print()

    print(f"Rate limit remaining: "
          f"{detail_response.headers.get('x-ratelimit-remaining')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
