"""Tests for the assembly of the model input.

Work package E, RQ1. Three things could silently distort the results:
a pull request that is dropped although it should be kept, a source
block that quietly exceeds its budget, and a cut that leaves no trace
in the text. All three are checked here.

The tests build their own small records and never read the prepared
dataset, which is not part of the repository.

Run from the project root: python -m pytest tests/ -v
"""

from __future__ import annotations

from typing import Any

import pytest

from build_prompt_input import (
    NOTE_ALLOWANCE,
    build_block,
    cap,
    selection_reason,
)

SETTINGS: dict[str, Any] = {
    "exclude_bots": True,
    "exclude_open": True,
    "include_drafts": True,
    "max_diff_hunk_chars": 500,
    "max_input_chars_per_pull": 80000,
    "truncation_marker": "\n[... truncated ...]\n",
}


@pytest.fixture
def settings() -> dict[str, Any]:
    return dict(SETTINGS)


@pytest.fixture
def pull() -> dict[str, Any]:
    return {
        "number": 42,
        "title": "Validate user input",
        "body": "At the moment inputs are not checked.",
        "outcome": "merged",
        "draft": False,
        "author": "somebody",
        "author_is_bot": False,
        "issue_comments": [
            {"id": 111, "author": "alice", "author_association": "CONTRIBUTOR",
             "created_at": "2025-01-02T00:00:00Z", "body": "Please add a check."}
        ],
        "review_comments": [
            {"id": 222, "author": "bob", "author_association": "COLLABORATOR",
             "created_at": "2025-01-01T00:00:00Z", "body": "Unreachable branch.",
             "path": "src/x.py", "line": 7, "diff_hunk": "@@ -1 +1 @@"}
        ],
        "files": [
            {"filename": "src/x.py", "status": "modified", "additions": 2,
             "deletions": 1, "patch": "@@ -1 +1 @@\n+checked = True",
             "patch_drop_reason": None}
        ],
    }


# --- selection, decision E4 -------------------------------------------


def test_a_normal_pull_request_is_kept(pull, settings):
    assert selection_reason(pull, settings) is None


def test_a_bot_contribution_is_left_out(pull, settings):
    pull["author_is_bot"] = True
    assert selection_reason(pull, settings) == "bot"


def test_an_open_pull_request_is_left_out(pull, settings):
    pull["outcome"] = "open"
    assert selection_reason(pull, settings) == "open"


def test_a_draft_is_kept_by_default(pull, settings):
    """Being marked as a draft says nothing about the content, see E4."""
    pull["draft"] = True
    assert selection_reason(pull, settings) is None


def test_a_draft_can_be_excluded_by_configuration(pull, settings):
    pull["draft"] = True
    settings["include_drafts"] = False
    assert selection_reason(pull, settings) == "draft"


def test_a_missing_description_does_not_exclude(pull, settings):
    """Title and diff are still a source, see E4."""
    pull["body"] = None
    assert selection_reason(pull, settings) is None


def test_a_pull_request_without_files_does_not_exclude(pull, settings):
    pull["files"] = []
    assert selection_reason(pull, settings) is None


# --- capping ----------------------------------------------------------


def test_short_text_is_returned_unchanged():
    text, was_cut = cap("abc", 10, "...")
    assert (text, was_cut) == ("abc", False)


def test_long_text_is_cut_and_marked():
    text, was_cut = cap("abcdefghij", 4, "<<cut>>")
    assert was_cut is True
    assert text.startswith("abcd")
    assert text.endswith("<<cut>>")


# --- block assembly, decision E5 --------------------------------------


def test_every_part_appears_in_the_block(pull, settings):
    block = build_block(pull, settings)["source_block"]
    for fragment in ("PULL REQUEST 42", "Validate user input",
                     "inputs are not checked", "Please add a check.",
                     "Unreachable branch.", "src/x.py", "checked = True"):
        assert fragment in block, fragment


def test_author_logins_never_reach_the_block(pull, settings):
    """Only the association is passed on, not the login."""
    block = build_block(pull, settings)["source_block"]
    for login in ("somebody", "alice", "bob"):
        assert login not in block, login
    assert "COLLABORATOR" in block


def test_comments_are_ordered_by_time(pull, settings):
    block = build_block(pull, settings)["source_block"]
    assert block.index("Unreachable branch.") < block.index("Please add a check.")


def test_a_long_review_context_is_capped(pull, settings):
    pull["review_comments"][0]["diff_hunk"] = "x" * 5000
    result = build_block(pull, settings)
    assert result["omitted"]["review_contexts_capped"] == 1
    assert result["truncated"] is True
    assert "x" * 600 not in result["source_block"]


def test_a_short_review_context_is_kept_whole(pull, settings):
    result = build_block(pull, settings)
    assert result["omitted"]["review_contexts_capped"] == 0
    assert "@@ -1 +1 @@" in result["source_block"]


def test_the_budget_is_never_exceeded(pull, settings):
    pull["files"] = [
        {"filename": f"src/f{i}.py", "status": "modified", "additions": 1,
         "deletions": 0, "patch": "y" * 20000, "patch_drop_reason": None}
        for i in range(20)
    ]
    result = build_block(pull, settings)
    assert result["chars"] <= settings["max_input_chars_per_pull"]


def test_prose_survives_when_the_diff_is_too_large(pull, settings):
    """A requirement is normally stated in words, so prose is kept first."""
    pull["files"] = [
        {"filename": "src/big.py", "status": "modified", "additions": 1,
         "deletions": 0, "patch": "y" * 200000, "patch_drop_reason": None}
    ]
    result = build_block(pull, settings)
    assert "inputs are not checked" in result["source_block"]
    assert result["omitted"]["file_sections"] == 1
    assert result["omitted"]["comment_sections"] == 0


def test_a_cut_leaves_a_visible_note(pull, settings):
    pull["files"] = [
        {"filename": "src/big.py", "status": "modified", "additions": 1,
         "deletions": 0, "patch": "y" * 200000, "patch_drop_reason": None}
    ]
    block = build_block(pull, settings)["source_block"]
    assert "[BUDGET NOTE]" in block


def test_the_note_allowance_leaves_room_for_the_note(pull, settings):
    pull["files"] = [
        {"filename": "src/big.py", "status": "modified", "additions": 1,
         "deletions": 0, "patch": "y" * 200000, "patch_drop_reason": None}
    ]
    result = build_block(pull, settings)
    assert result["chars"] <= settings["max_input_chars_per_pull"]
    assert NOTE_ALLOWANCE > len("[BUDGET NOTE] 99 comment sections and 99 file "
                                "sections were left out because the character "
                                "budget of 999999 was reached.")


def test_a_missing_description_is_stated_explicitly(pull, settings):
    pull["body"] = None
    block = build_block(pull, settings)["source_block"]
    assert "no description" in block


def test_a_file_without_patch_text_states_the_reason(pull, settings):
    pull["files"][0]["patch"] = ""
    pull["files"][0]["patch_drop_reason"] = "excluded file type"
    block = build_block(pull, settings)["source_block"]
    assert "excluded file type" in block


def test_an_untouched_pull_request_is_not_marked_as_cut(pull, settings):
    result = build_block(pull, settings)
    assert result["truncated"] is False
    assert "[BUDGET NOTE]" not in result["source_block"]
