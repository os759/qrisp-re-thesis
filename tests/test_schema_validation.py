"""Tests for the validation of the structured model output.

Work package E, RQ1. Two things can silently corrupt the results:
a model output that does not match the agreed schema, and a source
excerpt that was never in the data. Both are checked here.

The tests build their own small records. They never read the prepared
dataset, which is not part of the repository.

Run from the project root: python -m pytest tests/ -v
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
from jsonschema import Draft202012Validator

from validate_output import (
    excerpt_errors,
    haystacks_for,
    schema_errors,
    strip_diff_markers,
)

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "config" / "requirement_schema_v1.json"


@pytest.fixture(scope="module")
def validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


@pytest.fixture
def record() -> dict[str, Any]:
    """A minimal record that has to pass every check."""
    return {
        "schema_version": 1,
        "pull_number": 42,
        "processing_status": "requirements_found",
        "status_reason": None,
        "requirements": [
            {
                "id": "QR-0042-01",
                "text": "The library shall check inputs for validity before processing them.",
                "ears_pattern": "ubiquitous",
                "system_name": "the library",
                "type": "functional_performance",
                "security_relevant": False,
                "rationale": "The review comment asks for input checking.",
                "beneficiary": None,
                "component": None,
                "verification": None,
                "source": {
                    "pull_number": 42,
                    "location": "body",
                    "locator": None,
                    "html_url": None,
                },
                "source_excerpt": "inputs are not checked before they are used",
                "evidence_strength": "direct",
                "uncertainties": None,
                "missing_information": None,
                "modality_set_by_convention": True,
            }
        ],
    }


@pytest.fixture
def pull() -> dict[str, Any]:
    """A pull request record in the shape produced by build_interim.py."""
    return {
        "number": 42,
        "title": "Validate user input",
        "body": "At the moment inputs are not checked before they are used.",
        "issue_comments": [
            {"id": 111, "body": "Please add a check for negative values."}
        ],
        "review_comments": [
            {"id": 222, "body": "This branch is unreachable.", "diff_hunk": "@@ -1 +1 @@"}
        ],
        "files": [
            {
                "filename": "src/qrisp/core/input.py",
                "patch": "@@ -1,2 +1,4 @@\n context line\n+the value shall be checked\n-old line that was removed\n",
            }
        ],
    }


# --- schema check -----------------------------------------------------


def test_valid_record_passes(validator, record):
    assert schema_errors(record, validator) == []


@pytest.mark.parametrize("field", [
    "id", "text", "ears_pattern", "system_name", "type",
    "security_relevant", "rationale", "source", "source_excerpt",
    "evidence_strength", "modality_set_by_convention",
])
def test_missing_mandatory_field_is_rejected(validator, record, field):
    record["requirements"][0].pop(field)
    assert schema_errors(record, validator) != []


def test_invented_field_is_rejected(validator, record):
    """A free numeric confidence must not slip through, see decision E1."""
    record["requirements"][0]["confidence"] = 0.87
    assert schema_errors(record, validator) != []


def test_sentence_without_shall_is_rejected(validator, record):
    record["requirements"][0]["text"] = "The library must check inputs for validity."
    assert schema_errors(record, validator) != []


def test_identifier_pattern_is_enforced(validator, record):
    record["requirements"][0]["id"] = "REQ-1"
    assert schema_errors(record, validator) != []


def test_unknown_ears_pattern_is_rejected(validator, record):
    record["requirements"][0]["ears_pattern"] = "when_driven"
    assert schema_errors(record, validator) != []


def test_unknown_requirement_type_is_rejected(validator, record):
    """The value set comes from 29148 clause 5.2.8.3 and is closed."""
    record["requirements"][0]["type"] = "security"
    assert schema_errors(record, validator) != []


def test_modality_marker_cannot_be_turned_off(validator, record):
    """The marker records that shall is set by convention, see C5 section 3."""
    record["requirements"][0]["modality_set_by_convention"] = False
    assert schema_errors(record, validator) != []


def test_empty_result_is_a_valid_record(validator, record):
    record["processing_status"] = "no_requirements_found"
    record["status_reason"] = "The pull request only fixes typos."
    record["requirements"] = []
    assert schema_errors(record, validator) == []


def test_empty_result_needs_a_reason(validator, record):
    record["processing_status"] = "no_requirements_found"
    record["status_reason"] = None
    record["requirements"] = []
    assert schema_errors(record, validator) != []


def test_empty_result_must_not_carry_requirements(validator, record):
    record["processing_status"] = "no_requirements_found"
    record["status_reason"] = "Nothing found."
    assert schema_errors(record, validator) != []


def test_found_status_needs_at_least_one_requirement(validator, record):
    record["requirements"] = []
    assert schema_errors(record, validator) != []


# --- diff markers -----------------------------------------------------


def test_added_and_context_lines_are_kept():
    patch = "@@ -1 +1 @@\n context\n+added\n-removed\n"
    assert strip_diff_markers(patch) == "context\nadded"


def test_file_headers_are_dropped():
    patch = "--- a/x.py\n+++ b/x.py\n+added\n"
    assert strip_diff_markers(patch) == "added"


# --- excerpt check ----------------------------------------------------


def dataset_of(pull: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {pull["number"]: pull}


def test_literal_excerpt_from_body_passes(record, pull):
    assert excerpt_errors(record, dataset_of(pull)) == []


def test_invented_excerpt_is_rejected(record, pull):
    record["requirements"][0]["source_excerpt"] = "inputs are validated on every call"
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_excerpt_from_diff_passes_without_markers(record, pull):
    requirement = record["requirements"][0]
    requirement["source"]["location"] = "diff"
    requirement["source"]["locator"] = "src/qrisp/core/input.py"
    requirement["source_excerpt"] = "the value shall be checked"
    assert excerpt_errors(record, dataset_of(pull)) == []


def test_excerpt_from_a_removed_line_is_rejected(record, pull):
    """Removed lines are no longer part of the code after the change."""
    requirement = record["requirements"][0]
    requirement["source"]["location"] = "diff"
    requirement["source"]["locator"] = "src/qrisp/core/input.py"
    requirement["source_excerpt"] = "old line that was removed"
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_wrong_file_as_source_is_rejected(record, pull):
    requirement = record["requirements"][0]
    requirement["source"]["location"] = "diff"
    requirement["source"]["locator"] = "src/qrisp/core/other.py"
    requirement["source_excerpt"] = "the value shall be checked"
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_source_pointing_to_another_pull_is_rejected(record, pull):
    record["requirements"][0]["source"]["pull_number"] = 43
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_pull_missing_from_dataset_is_reported(record):
    assert excerpt_errors(record, {}) != []


def test_comment_locator_selects_the_named_comment(record, pull):
    requirement = record["requirements"][0]
    requirement["source"]["location"] = "issue_comment"
    requirement["source"]["locator"] = "111"
    requirement["source_excerpt"] = "add a check for negative values"
    assert excerpt_errors(record, dataset_of(pull)) == []

    requirement["source"]["locator"] = "999"
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_haystacks_cover_every_location(pull):
    for location in ("title", "body", "issue_comment", "review_comment", "diff"):
        source = {"pull_number": 42, "location": location, "locator": None}
        assert haystacks_for(source, pull), location


def test_review_comment_includes_its_diff_hunk(record, pull):
    requirement = record["requirements"][0]
    requirement["source"]["location"] = "review_comment"
    requirement["source"]["locator"] = "222"
    requirement["source_excerpt"] = "@@ -1 +1 @@"
    assert excerpt_errors(record, dataset_of(pull)) == []
