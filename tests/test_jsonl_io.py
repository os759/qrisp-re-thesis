"""Test the JSON Lines helpers that every collection script relies on.

Work package D, RQ1, decision D4. A fault here corrupts data without
raising an error: a lost record, a mangled umlaut or a silently
skipped line would never show up in a program that keeps running.
"""

from __future__ import annotations

import json

import pytest

from github_api import append_jsonl, read_jsonl


def test_written_records_are_read_back_unchanged(tmp_path):
    """A record survives a write and read cycle without change."""
    path = tmp_path / "data.jsonl"
    records = [
        {"number": 5, "title": "first", "body": None},
        {"number": 797, "title": "second", "nested": {"ref": "main"}},
    ]
    for record in records:
        append_jsonl(record, path)

    assert read_jsonl(path) == records


def test_each_record_occupies_exactly_one_line(tmp_path):
    """Two records must produce two lines, whatever they contain.

    A pull request body holds newlines. If they were written raw, one
    record would spread over several lines and the file would no longer
    be resumable line by line.
    """
    path = tmp_path / "data.jsonl"
    append_jsonl({"number": 1, "body": "line one\nline two\nline three"}, path)
    append_jsonl({"number": 2, "body": "single"}, path)

    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["body"] == "line one\nline two\nline three"


def test_non_ascii_characters_are_kept_readable(tmp_path):
    """Umlauts and other characters stay themselves, not escape codes."""
    path = tmp_path / "data.jsonl"
    append_jsonl({"body": "Größe der Änderung, 中文, emoji ok"}, path)

    raw = path.read_text(encoding="utf-8")
    assert "Größe der Änderung" in raw
    assert "\\u" not in raw
    assert read_jsonl(path)[0]["body"] == "Größe der Änderung, 中文, emoji ok"


def test_blank_lines_are_skipped(tmp_path):
    """Empty lines are ignored instead of raising or counting as records."""
    path = tmp_path / "data.jsonl"
    path.write_text('{"number": 1}\n\n   \n{"number": 2}\n', encoding="utf-8")

    assert read_jsonl(path) == [{"number": 1}, {"number": 2}]


def test_missing_file_yields_an_empty_list(tmp_path):
    """A run that has not written anything yet starts from nothing.

    The resume logic calls read_jsonl before the output file exists.
    It has to return an empty list rather than fail.
    """
    assert read_jsonl(tmp_path / "not_there.jsonl") == []


def test_a_broken_line_is_reported_with_its_number(tmp_path):
    """A truncated file must fail loudly, and name the line."""
    path = tmp_path / "data.jsonl"
    path.write_text('{"number": 1}\n{"number": 2\n', encoding="utf-8")

    with pytest.raises(ValueError) as error:
        read_jsonl(path)
    assert "line 2" in str(error.value)
