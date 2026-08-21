"""Test the derived field that separates merged from discarded work.

Work package D, RQ1, decision D4. GitHub only knows open and closed.
A discarded pull request and a merged one are both closed, so the
state field alone cannot say whether a change ever reached the code
base. A fault here would turn rejected proposals into evidence for
implemented requirements.
"""

from __future__ import annotations

from build_interim import outcome_of


def test_a_merged_pull_request_is_merged():
    """A merge timestamp is the only proof that work was integrated."""
    record = {"state": "closed", "merged_at": "2024-05-01T10:00:00Z"}

    assert outcome_of(record) == "merged"


def test_a_closed_pull_request_without_merge_is_discarded():
    """Closed and never merged means the proposal was dropped."""
    record = {"state": "closed", "merged_at": None}

    assert outcome_of(record) == "closed_unmerged"


def test_an_open_pull_request_stays_open():
    """Still under discussion, so neither accepted nor rejected."""
    record = {"state": "open", "merged_at": None}

    assert outcome_of(record) == "open"


def test_the_merge_timestamp_outranks_the_state_field():
    """A merge timestamp decides, whatever state says."""
    record = {"state": "open", "merged_at": "2024-05-01T10:00:00Z"}

    assert outcome_of(record) == "merged"


def test_an_empty_merge_timestamp_does_not_count_as_merged():
    """An empty string must not be mistaken for a timestamp."""
    record = {"state": "closed", "merged_at": ""}

    assert outcome_of(record) == "closed_unmerged"


def test_every_record_receives_one_of_three_values():
    """No input may fall through without a classification."""
    inputs = [
        {"state": "closed", "merged_at": "2024-05-01T10:00:00Z"},
        {"state": "closed", "merged_at": None},
        {"state": "open", "merged_at": None},
        {},
    ]

    results = {outcome_of(record) for record in inputs}
    assert results <= {"merged", "closed_unmerged", "open"}
    assert len(results) == 3
