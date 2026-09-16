"""Tests for the validation of the structured model output.

Work package E, RQ1. Two things can silently corrupt the results:
a model output that does not match the agreed schema, and a source
excerpt that was never in the data. Both are checked here.

The tests build their own small records. They never read the prepared
dataset, which is not part of the repository.

Run from the project root: python -m pytest tests/ -v
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import pytest
from jsonschema import Draft202012Validator

from validate_output import (
    check_record,
    consistency_errors,
    derive_evidence_strength,
    excerpt_errors,
    haystacks_for,
    required_parts,
    schema_errors,
    strip_diff_markers,
)

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "config" / "requirement_schema_v2.json"


@pytest.fixture(scope="module")
def validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


@pytest.fixture
def record() -> dict[str, Any]:
    """A minimal record that has to pass every check."""
    return {
        "schema_version": 2,
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
                "source_form": "prescriptive",
                "evidence": [
                    {
                        "location": "body",
                        "locator": None,
                        "html_url": None,
                        "excerpt": "inputs are not checked before they are used",
                        "supports": ["system_name", "system_response"],
                    }
                ],
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
    "security_relevant", "rationale", "evidence", "source_form",
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
    record["requirements"][0]["evidence"][0]["excerpt"] = "inputs are validated on every call"
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_excerpt_from_diff_passes_without_markers(record, pull):
    item = record["requirements"][0]["evidence"][0]
    item["location"] = "diff"
    item["locator"] = "src/qrisp/core/input.py"
    item["excerpt"] = "the value shall be checked"
    assert excerpt_errors(record, dataset_of(pull)) == []


def test_excerpt_from_a_removed_line_is_rejected(record, pull):
    """Removed lines are no longer part of the code after the change."""
    item = record["requirements"][0]["evidence"][0]
    item["location"] = "diff"
    item["locator"] = "src/qrisp/core/input.py"
    item["excerpt"] = "old line that was removed"
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_wrong_file_as_source_is_rejected(record, pull):
    item = record["requirements"][0]["evidence"][0]
    item["location"] = "diff"
    item["locator"] = "src/qrisp/core/other.py"
    item["excerpt"] = "the value shall be checked"
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_a_pull_outside_the_dataset_is_reported(record, pull):
    record["pull_number"] = 43
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_pull_missing_from_dataset_is_reported(record):
    assert excerpt_errors(record, {}) != []


def test_comment_locator_selects_the_named_comment(record, pull):
    item = record["requirements"][0]["evidence"][0]
    item["location"] = "issue_comment"
    item["locator"] = "111"
    item["excerpt"] = "add a check for negative values"
    assert excerpt_errors(record, dataset_of(pull)) == []

    item["locator"] = "999"
    assert excerpt_errors(record, dataset_of(pull)) != []


def test_haystacks_cover_every_location(pull):
    for location in ("title", "body", "issue_comment", "review_comment", "diff"):
        item = {"location": location, "locator": None}
        assert haystacks_for(item, pull), location


def test_review_comment_includes_its_diff_hunk(record, pull):
    item = record["requirements"][0]["evidence"][0]
    item["location"] = "review_comment"
    item["locator"] = "222"
    item["excerpt"] = "@@ -1 +1 @@"
    assert excerpt_errors(record, dataset_of(pull)) == []


# --- evidence and strength, decision E6 -------------------------------


@pytest.mark.parametrize("pattern,extra", [
    ("ubiquitous", set()),
    ("state_driven", {"precondition"}),
    ("optional_feature", {"precondition"}),
    ("event_driven", {"trigger"}),
    ("unwanted_behaviour", {"trigger"}),
    ("complex", {"precondition", "trigger"}),
])
def test_each_pattern_demands_its_own_parts(pattern, extra):
    assert required_parts(pattern) == {"system_name", "system_response"} | extra


def test_a_demanding_source_with_full_coverage_is_direct(record):
    assert derive_evidence_strength(record["requirements"][0]) == "direct"
    assert consistency_errors(record) == []


def test_a_reporting_source_with_full_coverage_is_indirect(record):
    requirement = record["requirements"][0]
    requirement["source_form"] = "descriptive"
    requirement["evidence_strength"] = "indirect"
    assert consistency_errors(record) == []


def test_a_missing_part_makes_it_insufficient(record):
    requirement = record["requirements"][0]
    requirement["evidence"][0]["supports"] = ["system_response"]
    requirement["evidence_strength"] = "insufficient"
    assert consistency_errors(record) == []


def test_a_missing_part_outranks_a_demanding_source(record):
    """Coverage decides first, see decision E6."""
    requirement = record["requirements"][0]
    requirement["evidence"][0]["supports"] = ["system_response"]
    assert derive_evidence_strength(requirement) == "insufficient"


def test_a_conditional_pattern_without_its_trigger_is_insufficient(record):
    requirement = record["requirements"][0]
    requirement["text"] = "When input arrives, the library shall check it."
    requirement["ears_pattern"] = "event_driven"
    assert derive_evidence_strength(requirement) == "insufficient"


def test_two_excerpts_can_cover_the_parts_together(record):
    requirement = record["requirements"][0]
    requirement["evidence"][0]["supports"] = ["system_name"]
    requirement["evidence"].append({
        "location": "issue_comment",
        "locator": "111",
        "html_url": None,
        "excerpt": "Please add a check for negative values.",
        "supports": ["system_response"],
    })
    assert derive_evidence_strength(requirement) == "direct"
    assert consistency_errors(record) == []


def test_a_freely_claimed_strength_is_rejected(record):
    """The model must not call a weak reconstruction well evidenced."""
    requirement = record["requirements"][0]
    requirement["source_form"] = "descriptive"
    requirement["evidence_strength"] = "direct"
    assert consistency_errors(record) != []


def test_the_report_names_the_missing_part(record):
    requirement = record["requirements"][0]
    requirement["evidence"][0]["supports"] = ["system_response"]
    assert "system_name" in consistency_errors(record)[0]


def test_evidence_must_not_be_empty(validator, record):
    record["requirements"][0]["evidence"] = []
    assert schema_errors(record, validator) != []


def test_at_most_three_sources_are_allowed(validator, record):
    item = record["requirements"][0]["evidence"][0]
    record["requirements"][0]["evidence"] = [dict(item) for _ in range(4)]
    assert schema_errors(record, validator) != []


def test_an_unknown_supported_part_is_rejected(validator, record):
    record["requirements"][0]["evidence"][0]["supports"] = ["system_owner"]
    assert schema_errors(record, validator) != []


def test_an_unknown_source_form_is_rejected(validator, record):
    record["requirements"][0]["source_form"] = "normative"
    assert schema_errors(record, validator) != []


def test_a_duplicated_part_in_one_excerpt_is_rejected(validator, record):
    record["requirements"][0]["evidence"][0]["supports"] = [
        "system_name", "system_name"]
    assert schema_errors(record, validator) != []


# --- all checks together ----------------------------------------------


def test_every_check_is_actually_run(validator, record, pull):
    """Guards against a check that exists but is never called."""
    good = check_record(record, validator, dataset_of(pull))
    assert good == []

    broken_schema = copy.deepcopy(record)
    broken_schema["requirements"][0]["confidence"] = 0.9
    assert check_record(broken_schema, validator, dataset_of(pull)) != []

    broken_rule = copy.deepcopy(record)
    broken_rule["requirements"][0]["source_form"] = "descriptive"
    assert check_record(broken_rule, validator, dataset_of(pull)) != []

    broken_excerpt = copy.deepcopy(record)
    broken_excerpt["requirements"][0]["evidence"][0]["excerpt"] = "never written here"
    assert check_record(broken_excerpt, validator, dataset_of(pull)) != []
