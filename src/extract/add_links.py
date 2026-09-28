"""Write one link per evidence entry into a new file, sub-step 10 of A8.

The model writes html_url as null, because the source block holds no
links (decision E7). This script adds the links afterwards, without
touching the model output: it writes a separate JSONL file with one
line per evidence entry, joined by pull number, requirement id and
position of the entry.

Variant B of the decision of 2026-09-28:
* title, body, diff: the html_url of the pull request, from the
  prepared dataset;
* issue_comment, review_comment: the html_url that GitHub delivered
  for this comment, from the raw files of package D. No link is built
  by the script itself.

A link is only written if the comment belongs to the same pull request
and the URL starts with the address of the Qrisp repository; otherwise
the line gets url null and a kind that names the reason. The file holds
no text of a pull request, only numbers, identifiers and links.

Work package E, step A8, sub-step 10. Traceability, criterion B9.

Run from the project root:

    python src/extract/add_links.py \\
      --input data/processed/extraction_2026-09-25_full_v2.jsonl \\
      --dataset data/interim/pulls_prepared_2026-08-19.jsonl \\
      --issue-comments data/raw/issue_comments_2026-08-19.jsonl \\
      --review-comments data/raw/review_comments_2026-08-19.jsonl \\
      --output data/processed/extraction_2026-09-25_full_v2.links.jsonl
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from validate_output import load_dataset, read_jsonl

REPO_PREFIX = "https://github.com/eclipse-qrisp/Qrisp/"
PULL_LOCATIONS = ("title", "body", "diff")
COMMENT_LOCATIONS = ("issue_comment", "review_comment")


def load_comment_urls(path: Path) -> dict[str, tuple[int, str]]:
    """Comment id -> (pull number, html_url). A repeated id must repeat its values."""
    urls: dict[str, tuple[int, str]] = {}
    for line_number, record in read_jsonl(path):
        key = str(record["id"])
        value = (record["collected_pull_number"], record["html_url"])
        if key in urls and urls[key] != value:
            raise ValueError(f"{path}, line {line_number}: comment {key} appears "
                             "twice with different values")
        urls[key] = value
    return urls


def link_for(item: Any, pull_number: int, pull_url: str | None,
             comments: dict[str, dict[str, tuple[int, str]]]) -> tuple[str | None, str]:
    """(url, kind) for one evidence entry."""
    if not isinstance(item, dict):
        return None, "entry_not_an_object"
    location = item.get("location")
    if location in PULL_LOCATIONS:
        if pull_url is None:
            return None, "pull_not_in_dataset"
        if not pull_url.startswith(REPO_PREFIX):
            return None, "unexpected_url"
        return pull_url, "pull"
    if location in COMMENT_LOCATIONS:
        found = comments[location].get(str(item.get("locator")))
        if found is None:
            return None, "comment_not_found"
        comment_pull, url = found
        if comment_pull != pull_number:
            return None, "comment_of_other_pull"
        if not (url or "").startswith(REPO_PREFIX):
            return None, "unexpected_url"
        return url, "comment"
    return None, "unknown_location"


def build(records: list[dict[str, Any]], dataset: dict[int, dict[str, Any]],
          comments: dict[str, dict[str, tuple[int, str]]]) -> list[dict[str, Any]]:
    rows = []
    for record in records:
        number = record.get("pull_number")
        pull = dataset.get(number)
        pull_url = pull.get("html_url") if pull else None
        requirements = record.get("requirements")
        for requirement in requirements if isinstance(requirements, list) else []:
            if not isinstance(requirement, dict):
                continue
            evidence = requirement.get("evidence")
            for position, item in enumerate(evidence if isinstance(evidence, list) else [],
                                            start=1):
                url, kind = link_for(item, number, pull_url, comments)
                rows.append({
                    "pull_number": number,
                    "requirement_id": requirement.get("id"),
                    "evidence_position": position,
                    "location": item.get("location") if isinstance(item, dict) else None,
                    "html_url": url,
                    "link_kind": kind,
                })
    return rows


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Links for every evidence entry.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--issue-comments", required=True)
    parser.add_argument("--review-comments", required=True)
    parser.add_argument("--output", required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    output = Path(arguments.output)
    if output.exists():
        print(f"Refused: {output} exists and is not overwritten.")
        return 2
    records = [record for _, record in read_jsonl(Path(arguments.input))]
    dataset = load_dataset(Path(arguments.dataset))
    comments = {"issue_comment": load_comment_urls(Path(arguments.issue_comments)),
                "review_comment": load_comment_urls(Path(arguments.review_comments))}
    rows = build(records, dataset, comments)
    text = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    output.write_text(text, encoding="utf-8")

    print(f"Records read: {len(records)}")
    print(f"Evidence entries: {len(rows)}")
    by_kind = Counter(row["link_kind"] for row in rows)
    print("By kind: " + ", ".join(f"{k} {v}" for k, v in sorted(by_kind.items())))
    by_location = Counter((row["location"], row["link_kind"]) for row in rows)
    print("By location and kind: " + ", ".join(
        f"{loc} {kind} {n}" for (loc, kind), n in sorted(by_location.items(), key=str)))
    print(f"Written: {output}")
    print(f"SHA-256: {hashlib.sha256(text.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
