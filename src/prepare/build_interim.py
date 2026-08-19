"""Build the reduced, merged dataset from the raw collection files.

Work package D, RQ1. The collection step wrote one raw file per API
endpoint (decision D3). This script merges them into a single JSON
Lines file holding one record per pull request, with its comments and
changed files embedded (decision D5).

Three things happen here and nowhere else:

1. Field reduction. Only the fields named in the decision of
   2026-08-12 are carried over. Volatile, constant and empty fields are
   dropped, and of the author object only the login is kept.
2. Text normalisation. Line endings become LF, and HTML comment blocks
   left over from the pull request template are removed from prose
   fields. Patch text and diff hunks are never stripped of comments,
   because a comment marker can be part of the changed source.
3. Truncation of patch text in three stages, following decision D1.
   Nothing is deleted silently: every dropped or shortened patch is
   marked on the record it belongs to.

Bot contributions are kept and flagged, not removed (decision D7).
Pull requests without a description or without any code change are kept
and flagged as well (decision D6). Selecting a subset is the job of a
later step, where the choice can be justified against a research
question.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# github_api lives in the sibling package src/collect. Running a script
# only puts its own directory on the import path, so the sibling has to
# be added explicitly.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "collect"))

from github_api import (  # noqa: E402
    PROJECT_ROOT,
    append_jsonl,
    current_commit,
    load_config,
    read_jsonl,
    sha256_of,
)

INTERIM_DIR = PROJECT_ROOT / "data" / "interim"
MANIFEST_DIR = PROJECT_ROOT / "data" / "manifests"

HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
BLANK_LINES = re.compile(r"\n{3,}")


def parse_arguments() -> argparse.Namespace:
    """Read the command line arguments."""
    parser = argparse.ArgumentParser(
        description="Merge and reduce the raw files into data/interim."
    )
    parser.add_argument("--details", required=True,
                        help="JSONL file holding the pull request details.")
    parser.add_argument("--issue-comments", required=True,
                        help="JSONL file holding the conversation comments.")
    parser.add_argument("--review-comments", required=True,
                        help="JSONL file holding the review comments.")
    parser.add_argument("--files", required=True,
                        help="JSONL file holding the changed files.")
    parser.add_argument("--limit", type=int, default=None,
                        help="Handle at most this many pull requests.")
    parser.add_argument("--day", default=None,
                        help="Date stamp of the output file (YYYY-MM-DD).")
    parser.add_argument("--overwrite", action="store_true",
                        help="Delete an existing output file first.")
    return parser.parse_args()


def resolve_path(raw_path: str) -> Path:
    """Interpret a relative path as relative to the project root."""
    path = Path(raw_path)
    return path if path.is_absolute() else PROJECT_ROOT / path


def normalise_line_endings(text: str | None) -> str | None:
    """Turn CRLF and CR into LF, keeping None as None."""
    if text is None:
        return None
    return text.replace("\r\n", "\n").replace("\r", "\n")


def normalise_prose(text: str | None) -> dict[str, Any]:
    """Clean a prose field and report what had to be changed.

    Returns the cleaned text together with three markers: whether the
    original used CRLF line endings, whether it contained a template
    comment, and whether a comment was left unterminated. Only complete
    comment blocks are removed, so an unclosed marker cannot swallow
    the rest of the text.
    """
    if not text:
        return {"text": "", "had_crlf": False,
                "had_template": False, "template_unterminated": False}
    had_crlf = "\r" in text
    cleaned = normalise_line_endings(text) or ""
    had_template = "<!--" in cleaned
    cleaned = HTML_COMMENT.sub("", cleaned)
    unterminated = "<!--" in cleaned
    cleaned = BLANK_LINES.sub("\n\n", cleaned).strip()
    return {"text": cleaned, "had_crlf": had_crlf,
            "had_template": had_template,
            "template_unterminated": unterminated}


def author_of(user: dict[str, Any] | None) -> tuple[str | None, bool]:
    """Return the login and whether the account is a bot (decision D2)."""
    if not user:
        return None, False
    login = user.get("login")
    is_bot = user.get("type") == "Bot" or bool(
        login and login.endswith("[bot]")
    )
    return login, is_bot


def outcome_of(record: dict[str, Any]) -> str:
    """Classify a pull request as merged, closed_unmerged or open."""
    if record.get("merged_at"):
        return "merged"
    if record.get("state") == "open":
        return "open"
    return "closed_unmerged"


def reduce_comment(record: dict[str, Any], review: bool) -> dict[str, Any]:
    """Reduce one comment to the fields needed for reconstruction."""
    login, is_bot = author_of(record.get("user"))
    body = normalise_prose(record.get("body"))
    reduced: dict[str, Any] = {
        "id": record.get("id"),
        "author": login,
        "author_is_bot": is_bot,
        "author_association": record.get("author_association"),
        "created_at": record.get("created_at"),
        "updated_at": record.get("updated_at"),
        "html_url": record.get("html_url"),
        "body": body["text"],
        "body_had_crlf": body["had_crlf"],
        "body_had_template": body["had_template"],
        "body_template_unterminated": body["template_unterminated"],
    }
    if review:
        reduced.update({
            "path": record.get("path"),
            "line": record.get("line"),
            "side": record.get("side"),
            "commit_id": record.get("commit_id"),
            "review_id": record.get("pull_request_review_id"),
            "diff_hunk": normalise_line_endings(record.get("diff_hunk")),
        })
    return reduced


def prepare_files(records: list[dict[str, Any]],
                  settings: dict[str, Any]) -> tuple[list[dict[str, Any]],
                                                     dict[str, int]]:
    """Reduce the changed files and apply the three truncation stages.

    Stage 1 drops the patch text of excluded file types and of files the
    API delivered without one. Stage 2 caps the patch text of a single
    file. Stage 3 caps the patch text of the whole pull request; files
    are served in the order GitHub delivered them, and once the budget
    is spent the remaining files keep their name and line counts only.
    """
    skip = {suffix.lower() for suffix in settings["skip_patch_extensions"]}
    max_file = settings["max_patch_chars_per_file"]
    marker = settings["truncation_marker"]
    budget = settings["max_patch_chars_per_pull"]

    prepared: list[dict[str, Any]] = []
    counters = {"stage1_dropped": 0, "stage2_truncated": 0,
                "stage3_truncated": 0, "stage3_dropped": 0,
                "chars_original": 0, "chars_kept": 0}

    for record in records:
        filename = record.get("filename") or ""
        patch = normalise_line_endings(record.get("patch"))
        original = len(patch) if patch else 0
        counters["chars_original"] += original

        entry: dict[str, Any] = {
            "filename": filename,
            "status": record.get("status"),
            "additions": record.get("additions"),
            "deletions": record.get("deletions"),
            "changes": record.get("changes"),
            "patch": None,
            "patch_kept": False,
            "patch_drop_reason": None,
            "patch_truncated": False,
            "patch_chars_original": original,
            "patch_chars_kept": 0,
        }

        if patch is None:
            entry["patch_drop_reason"] = "no_patch_from_api"
            counters["stage1_dropped"] += 1
        elif Path(filename).suffix.lower() in skip:
            entry["patch_drop_reason"] = "excluded_file_type"
            counters["stage1_dropped"] += 1
        elif budget <= len(marker):
            entry["patch_drop_reason"] = "pull_budget_exhausted"
            counters["stage3_dropped"] += 1
        else:
            text = patch
            truncated = False
            if len(text) > max_file:
                text = text[:max_file] + marker
                truncated = True
                counters["stage2_truncated"] += 1
            if len(text) > budget:
                text = text[: budget - len(marker)] + marker
                truncated = True
                counters["stage3_truncated"] += 1
            entry["patch"] = text
            entry["patch_kept"] = True
            entry["patch_truncated"] = truncated
            entry["patch_chars_kept"] = len(text)
            budget -= len(text)
            counters["chars_kept"] += len(text)

        prepared.append(entry)

    return prepared, counters


def build_record(detail: dict[str, Any],
                 issue_comments: list[dict[str, Any]],
                 review_comments: list[dict[str, Any]],
                 files: list[dict[str, Any]],
                 settings: dict[str, Any]) -> dict[str, Any]:
    """Assemble one prepared record for a single pull request."""
    login, is_bot = author_of(detail.get("user"))
    title = normalise_prose(detail.get("title"))
    body = normalise_prose(detail.get("body"))
    base = detail.get("base") or {}
    head = detail.get("head") or {}

    prepared_files, truncation = prepare_files(files, settings)
    sorted_issue = sorted(issue_comments,
                          key=lambda item: (item.get("created_at") or "",
                                            item.get("id") or 0))
    sorted_review = sorted(review_comments,
                           key=lambda item: (item.get("created_at") or "",
                                             item.get("id") or 0))

    return {
        "number": int(detail["number"]),
        "title": title["text"],
        "body": body["text"],
        "has_body": bool(body["text"]),
        "body_had_crlf": body["had_crlf"],
        "body_had_template": body["had_template"],
        "body_template_unterminated": body["template_unterminated"],
        "state": detail.get("state"),
        "outcome": outcome_of(detail),
        "draft": detail.get("draft"),
        "author": login,
        "author_is_bot": is_bot,
        "author_association": detail.get("author_association"),
        "created_at": detail.get("created_at"),
        "updated_at": detail.get("updated_at"),
        "closed_at": detail.get("closed_at"),
        "merged_at": detail.get("merged_at"),
        "html_url": detail.get("html_url"),
        "labels": [label.get("name") for label in (detail.get("labels") or [])],
        "base_ref": base.get("ref"),
        "base_sha": base.get("sha"),
        "head_sha": head.get("sha"),
        "counts_api": {
            "additions": detail.get("additions"),
            "deletions": detail.get("deletions"),
            "changed_files": detail.get("changed_files"),
            "commits": detail.get("commits"),
            "comments": detail.get("comments"),
            "review_comments": detail.get("review_comments"),
        },
        "counts_dataset": {
            "files": len(prepared_files),
            "issue_comments": len(sorted_issue),
            "review_comments": len(sorted_review),
        },
        "has_code_changes": bool(prepared_files),
        "has_patch_text": any(item["patch_kept"] for item in prepared_files),
        "truncation": truncation,
        "issue_comments": [reduce_comment(item, review=False)
                           for item in sorted_issue],
        "review_comments": [reduce_comment(item, review=True)
                            for item in sorted_review],
        "files": prepared_files,
    }


def count_lines(path: Path) -> int:
    """Count the non-empty lines of a file without parsing them.

    Used for the manifest only. Reading the large file a second time
    just to count its records would waste time and memory.
    """
    with path.open("r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


def group_by_pull(path: Path) -> dict[int, list[dict[str, Any]]]:
    """Group the records of a raw file by their pull request number."""
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for record in read_jsonl(path):
        grouped[int(record["collected_pull_number"])].append(record)
    return grouped


def main() -> int:
    arguments = parse_arguments()
    config = load_config()
    settings = config["prepare"]

    sources = {
        "details": resolve_path(arguments.details),
        "issue_comments": resolve_path(arguments.issue_comments),
        "review_comments": resolve_path(arguments.review_comments),
        "files": resolve_path(arguments.files),
    }
    for role, path in sources.items():
        if not path.is_file():
            print(f"Source file not found ({role}): {path}")
            return 1

    built_at = datetime.now(timezone.utc)
    day = arguments.day or built_at.strftime("%Y-%m-%d")

    INTERIM_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    output_path = INTERIM_DIR / f"pulls_prepared_{day}.jsonl"

    if output_path.is_file():
        if not arguments.overwrite:
            print(f"Output file already exists: {output_path}")
            print("Pass --overwrite to rebuild it, or choose another --day.")
            return 1
        output_path.unlink()
        print(f"Removed existing output file: {output_path.name}")

    details = read_jsonl(sources["details"])
    if not details:
        print(f"No records found in {sources['details']}")
        return 1
    details.sort(key=lambda record: int(record["number"]))
    if arguments.limit is not None:
        details = details[: arguments.limit]

    issue_by_pull = group_by_pull(sources["issue_comments"])
    review_by_pull = group_by_pull(sources["review_comments"])
    files_by_pull = group_by_pull(sources["files"])

    print(f"Details:          {sources['details'].name} "
          f"({len(details)} handled)")
    print(f"Issue comments:   {sources['issue_comments'].name}")
    print(f"Review comments:  {sources['review_comments'].name}")
    print(f"Changed files:    {sources['files'].name}")
    print(f"Output file:      {output_path.name}")
    print()

    statistics = {
        "pull_requests": 0, "bot_pull_requests": 0,
        "without_body": 0, "body_emptied_by_cleaning": 0,
        "body_template_unterminated": 0,
        "normalised_crlf": 0, "removed_template": 0,
        "without_code_changes": 0, "without_patch_text": 0,
        "without_any_comment": 0,
        "issue_comments": 0, "review_comments": 0, "files": 0,
        "files_stage1_dropped": 0, "files_stage2_truncated": 0,
        "files_stage3_truncated": 0, "files_stage3_dropped": 0,
        "pulls_truncated": 0,
        "patch_chars_original": 0, "patch_chars_kept": 0,
    }
    deviations: list[dict[str, Any]] = []

    for detail in details:
        number = int(detail["number"])
        record = build_record(
            detail,
            issue_by_pull.get(number, []),
            review_by_pull.get(number, []),
            files_by_pull.get(number, []),
            settings,
        )
        append_jsonl(record, output_path)

        statistics["pull_requests"] += 1
        statistics["bot_pull_requests"] += int(record["author_is_bot"])
        statistics["normalised_crlf"] += int(record["body_had_crlf"])
        statistics["removed_template"] += int(record["body_had_template"])
        statistics["body_template_unterminated"] += int(
            record["body_template_unterminated"])
        if not record["has_body"]:
            statistics["without_body"] += 1
            if (detail.get("body") or "").strip():
                statistics["body_emptied_by_cleaning"] += 1
        if not record["has_code_changes"]:
            statistics["without_code_changes"] += 1
        if not record["has_patch_text"]:
            statistics["without_patch_text"] += 1

        counts = record["counts_dataset"]
        if counts["issue_comments"] == 0 and counts["review_comments"] == 0:
            statistics["without_any_comment"] += 1
        statistics["issue_comments"] += counts["issue_comments"]
        statistics["review_comments"] += counts["review_comments"]
        statistics["files"] += counts["files"]

        truncation = record["truncation"]
        statistics["files_stage1_dropped"] += truncation["stage1_dropped"]
        statistics["files_stage2_truncated"] += truncation["stage2_truncated"]
        statistics["files_stage3_truncated"] += truncation["stage3_truncated"]
        statistics["files_stage3_dropped"] += truncation["stage3_dropped"]
        statistics["patch_chars_original"] += truncation["chars_original"]
        statistics["patch_chars_kept"] += truncation["chars_kept"]
        if truncation["chars_kept"] < truncation["chars_original"]:
            statistics["pulls_truncated"] += 1

        api = record["counts_api"]
        for field, actual in (("changed_files", counts["files"]),
                              ("comments", counts["issue_comments"]),
                              ("review_comments", counts["review_comments"])):
            expected = api.get(field)
            if expected is not None and int(expected) != actual:
                deviations.append({"number": number, "field": field,
                                   "api": int(expected), "dataset": actual})

    manifest = {
        "built_at_utc": built_at.isoformat(),
        "repository": config["source"]["repo_id"],
        "repository_full_name": (f"{config['source']['owner']}"
                                 f"/{config['source']['repo']}"),
        "stage": "interim",
        "source_dataset": {
            role: {"file": path.name, "sha256": sha256_of(path),
                   "record_count": count_lines(path)}
            for role, path in sources.items()
        },
        "parameters": {
            "skip_patch_extensions": settings["skip_patch_extensions"],
            "max_patch_chars_per_file":
                settings["max_patch_chars_per_file"],
            "max_patch_chars_per_pull":
                settings["max_patch_chars_per_pull"],
            "file_order": "as delivered by the API",
            "limit": arguments.limit,
        },
        "derived_fields": [
            "outcome", "author_is_bot", "has_body", "has_code_changes",
            "has_patch_text", "body_had_crlf", "body_had_template",
            "body_template_unterminated", "counts_dataset", "truncation",
        ],
        "record_count": statistics["pull_requests"],
        "statistics": statistics,
        "deviations": deviations,
        "output_file": output_path.name,
        "sha256": sha256_of(output_path),
        "builder_commit": current_commit(),
    }
    manifest_path = MANIFEST_DIR / f"manifest_prepared_{day}.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Pull requests:    {statistics['pull_requests']}")
    print(f"  by bots:        {statistics['bot_pull_requests']}")
    print(f"  without body:   {statistics['without_body']} "
          f"(emptied by cleaning: "
          f"{statistics['body_emptied_by_cleaning']})")
    print(f"  no code change: {statistics['without_code_changes']}")
    print(f"  no patch text:  {statistics['without_patch_text']}")
    print(f"  no comment:     {statistics['without_any_comment']}")
    print(f"CRLF normalised:  {statistics['normalised_crlf']}")
    print(f"Template removed: {statistics['removed_template']} "
          f"(unterminated: "
          f"{statistics['body_template_unterminated']})")
    print(f"Comments:         {statistics['issue_comments']} issue, "
          f"{statistics['review_comments']} review")
    print(f"Files:            {statistics['files']}")
    print(f"  stage 1 dropped:{statistics['files_stage1_dropped']}")
    print(f"  stage 2 cut:    {statistics['files_stage2_truncated']}")
    print(f"  stage 3 cut:    {statistics['files_stage3_truncated']}")
    print(f"  stage 3 dropped:{statistics['files_stage3_dropped']}")
    print(f"Patch characters: {statistics['patch_chars_original']} -> "
          f"{statistics['patch_chars_kept']}")
    print(f"Pulls truncated:  {statistics['pulls_truncated']}")
    print(f"Deviations:       {len(deviations)}")
    print(f"Data file:        {output_path}")
    print(f"Manifest:         {manifest_path}")
    print(f"SHA-256:          {manifest['sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
