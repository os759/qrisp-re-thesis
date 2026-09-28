"""Tests for src/extract/add_links.py with invented data.

Every evidence entry must get exactly one line, the right link or a
named reason for none, and the model output must stay untouched.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "extract"))

import add_links as a  # noqa: E402

PREFIX = "https://github.com/eclipse-qrisp/Qrisp/"
PULL_URL = PREFIX + "pull/7"
DATASET = {7: {"number": 7, "html_url": PULL_URL}}
COMMENTS = {
    "issue_comment": {"11": (7, PULL_URL + "#issuecomment-11"),
                      "12": (8, PREFIX + "pull/8#issuecomment-12"),
                      "13": (7, "https://example.org/x")},
    "review_comment": {"21": (7, PULL_URL + "#discussion_r21")},
}


def ev(location, locator=None):
    return {"location": location, "locator": locator, "excerpt": "SECRET TEXT"}


@pytest.mark.parametrize("item, expected", [
    (ev("title"), (PULL_URL, "pull")),
    (ev("body"), (PULL_URL, "pull")),
    (ev("diff", "src/a.py"), (PULL_URL, "pull")),
    (ev("issue_comment", "11"), (PULL_URL + "#issuecomment-11", "comment")),
    (ev("review_comment", "21"), (PULL_URL + "#discussion_r21", "comment")),
    (ev("review_comment", "11"), (None, "comment_not_found")),
    (ev("issue_comment", "99"), (None, "comment_not_found")),
    (ev("issue_comment", None), (None, "comment_not_found")),
    (ev("issue_comment", "12"), (None, "comment_of_other_pull")),
    (ev("issue_comment", "13"), (None, "unexpected_url")),
    (ev("elsewhere"), (None, "unknown_location")),
    ("not a dict", (None, "entry_not_an_object")),
])
def test_link_for_every_case(item, expected):
    assert a.link_for(item, 7, PULL_URL, COMMENTS) == expected


def test_a_pull_missing_from_the_dataset_gets_no_link():
    assert a.link_for(ev("body"), 9, None, COMMENTS) == (None, "pull_not_in_dataset")


def test_a_foreign_pull_url_is_refused():
    assert a.link_for(ev("body"), 7, "https://example.org/pull/7", COMMENTS) == \
        (None, "unexpected_url")


def test_one_line_per_evidence_entry_in_order():
    records = [{"pull_number": 7, "requirements": [
        {"id": "QR-0007-01", "evidence": [ev("body"), ev("issue_comment", "11")]},
        {"id": "QR-0007-02", "evidence": [ev("review_comment", "21")]}]},
        {"pull_number": 8},
        {"pull_number": 7, "requirements": "broken"}]
    rows = a.build(records, DATASET, COMMENTS)
    assert [(r["requirement_id"], r["evidence_position"], r["link_kind"]) for r in rows] == [
        ("QR-0007-01", 1, "pull"), ("QR-0007-01", 2, "comment"), ("QR-0007-02", 1, "comment")]
    assert all("excerpt" not in r for r in rows)


def test_comment_ids_are_read_as_strings_and_repeats_must_agree(tmp_path):
    path = tmp_path / "c.jsonl"
    same = {"id": 11, "collected_pull_number": 7, "html_url": PULL_URL + "#c11"}
    path.write_text(json.dumps(same) + "\n" + json.dumps(same) + "\n", encoding="utf-8")
    assert a.load_comment_urls(path) == {"11": (7, PULL_URL + "#c11")}
    other = dict(same, html_url=PULL_URL + "#other")
    path.write_text(json.dumps(same) + "\n" + json.dumps(other) + "\n", encoding="utf-8")
    with pytest.raises(ValueError):
        a.load_comment_urls(path)


def files(tmp_path):
    record = {"pull_number": 7, "requirements": [
        {"id": "QR-0007-01", "evidence": [ev("body"), ev("issue_comment", "11")]}]}
    (tmp_path / "in.jsonl").write_text(json.dumps(record) + "\n", encoding="utf-8")
    (tmp_path / "ds.jsonl").write_text(json.dumps(DATASET[7]) + "\n", encoding="utf-8")
    (tmp_path / "ic.jsonl").write_text(json.dumps(
        {"id": 11, "collected_pull_number": 7, "html_url": PULL_URL + "#issuecomment-11"})
        + "\n", encoding="utf-8")
    (tmp_path / "rc.jsonl").write_text("", encoding="utf-8")
    return ["--input", str(tmp_path / "in.jsonl"), "--dataset", str(tmp_path / "ds.jsonl"),
            "--issue-comments", str(tmp_path / "ic.jsonl"),
            "--review-comments", str(tmp_path / "rc.jsonl"),
            "--output", str(tmp_path / "out.jsonl")]


def test_main_writes_links_and_leaves_the_input_alone(tmp_path, capsys):
    args = files(tmp_path)
    before = (tmp_path / "in.jsonl").read_bytes()
    assert a.main(args) == 0
    rows = [json.loads(l) for l in (tmp_path / "out.jsonl").read_text().splitlines()]
    assert [r["html_url"] for r in rows] == [PULL_URL, PULL_URL + "#issuecomment-11"]
    assert (tmp_path / "in.jsonl").read_bytes() == before
    printed = capsys.readouterr().out
    assert "Evidence entries: 2" in printed and "SECRET" not in printed
    assert "SECRET" not in (tmp_path / "out.jsonl").read_text()


def test_main_never_overwrites(tmp_path, capsys):
    args = files(tmp_path)
    (tmp_path / "out.jsonl").write_text("kept", encoding="utf-8")
    assert a.main(args) == 2
    assert (tmp_path / "out.jsonl").read_text() == "kept"
