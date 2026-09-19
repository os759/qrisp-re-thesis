"""Tests for the replacement of mentions, decision E9.

Two failures would be invisible without these tests: a login that is not
replaced and therefore leaves the machine, and a code symbol that is
replaced and therefore corrupts the source text the model reads.

Work package E, research question FF3.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from pseudonymise import (build_mapping, find_mentions, load_mapping, mask,
                          save_mapping)

ALLOWLIST = {"pytest", "jax", "jaspify"}


@pytest.fixture
def mapping() -> dict[str, str]:
    return build_mapping({"alice", "bob-dev", "Carol"})


# --- what counts as a mention -----------------------------------------


def test_a_plain_mention_is_found():
    assert find_mentions("thanks @alice for the fix", ALLOWLIST) == ["alice"]


def test_several_mentions_keep_their_order():
    text = "@bob-dev and @alice agreed"
    assert find_mentions(text, ALLOWLIST) == ["bob-dev", "alice"]


def test_an_allowlisted_name_is_not_a_mention():
    assert find_mentions("use @pytest.mark here", ALLOWLIST) == []


def test_an_email_address_is_not_a_mention():
    assert find_mentions("write to alice@example.com", ALLOWLIST) == []


@pytest.mark.parametrize("text", [
    "```\n@alice\n```",
    "    @alice",
    "\t@alice",
    "see `@alice` in the code",
])
def test_code_contexts_hold_no_mentions(text):
    assert find_mentions(text, ALLOWLIST) == []


@pytest.mark.parametrize("text", [
    "    - @alice and the students",
    "        - [ ] @alice and the students",
    "    * @alice",
    "    1. @alice",
    "    > @alice wrote",
])
def test_an_indented_list_item_is_prose(text):
    """A nested list carries the indentation of a code block but is not one."""
    assert find_mentions(text, ALLOWLIST) == ["alice"]


def test_an_indented_list_inside_a_fence_stays_code():
    assert find_mentions("```\n    - @alice\n```", ALLOWLIST) == []


def test_prose_after_a_closed_fence_is_read_again():
    text = "```\n@property\n```\nthanks @alice"
    assert find_mentions(text, ALLOWLIST) == ["alice"]


# --- the mapping -------------------------------------------------------


def test_every_login_gets_its_own_placeholder(mapping):
    assert len(set(mapping.values())) == len(mapping)


def test_the_mapping_is_lower_case_and_stable(mapping):
    again = build_mapping({"Carol", "ALICE", "bob-dev"})
    assert mapping == again
    assert "carol" in mapping
    # Pinned to alphabetical order, so a rerun on another day and on
    # another machine numbers the logins in exactly the same way.
    assert mapping == {"alice": "person_01", "bob-dev": "person_02",
                       "carol": "person_03"}


def test_the_placeholder_carries_no_login(mapping):
    for login, placeholder in mapping.items():
        assert login not in placeholder
        assert placeholder.startswith("person_")


def test_the_mapping_survives_a_round_trip(tmp_path, mapping):
    path = tmp_path / "mention_map.json"
    save_mapping(mapping, path)
    assert load_mapping(path) == mapping
    assert json.loads(path.read_text(encoding="utf-8")) == mapping


# --- masking -----------------------------------------------------------


def test_a_mention_is_replaced(mapping):
    result = mask("thanks @alice", mapping, ALLOWLIST)
    assert "@alice" not in result
    assert "@" + mapping["alice"] in result


def test_the_same_login_always_gives_the_same_placeholder(mapping):
    first = mask("@alice writes", mapping, ALLOWLIST)
    second = mask("later @Alice writes again", mapping, ALLOWLIST)
    assert mapping["alice"] in first and mapping["alice"] in second


def test_two_logins_stay_distinguishable(mapping):
    result = mask("@alice and @bob-dev", mapping, ALLOWLIST)
    assert mapping["alice"] in result and mapping["bob-dev"] in result
    assert mapping["alice"] != mapping["bob-dev"]


def test_an_unknown_login_does_not_slip_through(mapping):
    result = mask("thanks @dave", mapping, ALLOWLIST)
    assert "@dave" not in result
    assert "person_unknown" in result


def test_a_known_login_in_code_is_replaced_too(mapping):
    """A login in backticks is a person, not a code symbol."""
    result = mask("see `@alice` in the code", mapping, ALLOWLIST)
    assert "@alice" not in result
    assert mapping["alice"] in result


def test_an_unknown_name_in_code_stays(mapping):
    """Nothing known about it, so it is treated as a code symbol."""
    text = "call `@custom_control` before this"
    assert mask(text, mapping, ALLOWLIST) == text


def test_a_decorator_in_code_is_left_alone(mapping):
    text = "run this:\n\n    @property\n    def value(self): ..."
    assert mask(text, mapping, ALLOWLIST) == text


def test_an_allowlisted_name_in_prose_is_left_alone(mapping):
    text = "mark it with @pytest and ask @alice"
    result = mask(text, mapping, ALLOWLIST)
    assert "@pytest" in result
    assert "@alice" not in result


def test_text_without_a_mention_is_unchanged(mapping):
    text = "This changes the simulator and adds a test."
    assert mask(text, mapping, ALLOWLIST) == text


def test_the_rest_of_the_sentence_survives(mapping):
    result = mask("@alice please check line 12 of core.py", mapping, ALLOWLIST)
    assert result.endswith("please check line 12 of core.py")


def test_masking_twice_changes_nothing_more(mapping):
    once = mask("thanks @alice", mapping, ALLOWLIST)
    assert mask(once, mapping, ALLOWLIST) == once


def test_a_placeholder_is_not_a_mention(mapping):
    assert find_mentions("thanks @person_01", ALLOWLIST) == []


def test_an_empty_text_is_returned_as_is(mapping):
    assert mask("", mapping, ALLOWLIST) == ""


# --- the two programs together ----------------------------------------


def test_no_login_reaches_the_built_block():
    """The block the model sees must carry no login and no code change."""
    from build_prompt_input import build_block, prose_fields

    pull = {
        "number": 7,
        "title": "Fix @alice's report",
        "body": "see `@alice` and:\n\n    @property\n    def x(self): ...",
        "issue_comments": [{"id": 1, "author_association": "NONE",
                            "created_at": "2026-01-01T00:00:00Z",
                            "body": "ping @bob-dev"}],
        "review_comments": [],
        "files": [{"filename": "a.py", "status": "modified", "additions": 1,
                   "deletions": 0, "patch": "@@ -1 +1 @@\n+@jaspify\n"}],
    }
    logins = set()
    for text in prose_fields(pull):
        logins.update(find_mentions(text, ALLOWLIST))
    mapping = build_mapping(logins)
    settings = {"max_input_chars_per_pull": 80000, "truncation_marker": "[cut]",
                "max_diff_hunk_chars": 500}

    block = build_block(pull, settings, mapping, ALLOWLIST)["source_block"]
    assert "@alice" not in block and "@bob-dev" not in block
    assert "@property" in block and "@jaspify" in block
    assert mapping["alice"] in block and mapping["bob-dev"] in block


def test_the_excerpt_check_follows_the_replacement():
    """A quotation from masked prose has to be found in the dataset again."""
    from validate_output import haystacks_for

    mapping = build_mapping({"alice"})
    pull = {"number": 7, "body": "@alice found a bug", "issue_comments": [],
            "review_comments": [], "files": []}
    item = {"location": "body", "locator": None}

    masked = haystacks_for(item, pull, mapping, ALLOWLIST)[0]
    assert masked == "@" + mapping["alice"] + " found a bug"
    assert haystacks_for(item, pull)[0] == "@alice found a bug"
