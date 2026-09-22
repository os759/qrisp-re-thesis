"""Tests for the switches --sizes and --exclude of draw_sample.py.

Decision E10: only the two new switches are tested, because an
exclusion that silently fails would put already used records into a
new sample (criterion from D4). All data here are invented.

Work package E, step A8. Research question FF1.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "analyze"))

import draw_sample  # noqa: E402
from draw_sample import (  # noqa: E402
    DEFAULT_SIZES,
    apply_exclusion,
    assign_strata,
    draw,
    parse_exclude,
    parse_sizes,
)

PILOT_SIZES = "S6=1,S5=4,S4=3,S3=3,S2=4,S1=5"


def invented_records() -> list[dict]:
    """Twenty invented records for each of the six strata, 120 in total."""
    records = []
    number = 1
    kinds = [
        {"has_code_changes": False},                          # S6
        {"truncation": {"stage3_dropped": 2}},                 # S5
        {"has_body": False},                                   # S4
        {"outcome": "closed_unmerged"},                        # S3
        {"outcome": "merged"},                                 # S2
        {"outcome": "merged", "issue_comments": [{"id": 1}]},  # S1
    ]
    for kind in kinds:
        for _ in range(20):
            record = {
                "number": number,
                "author_is_bot": False,
                "outcome": "merged",
                "has_code_changes": True,
                "has_body": True,
                "truncation": {"stage3_dropped": 0},
                "issue_comments": [],
                "review_comments": [],
                "html_url": f"https://example.invalid/pull/{number}",
            }
            record.update(kind)
            records.append(record)
            number += 1
    return records


def drawn_numbers(records, seed, sizes=None, excluded=frozenset()):
    eligible = apply_exclusion(records, set(excluded))
    pools, unassigned = assign_strata(eligible)
    drawn, _notes = draw(pools, unassigned, seed, sizes)
    return [record["number"] for _key, record in drawn]


# --- parse_sizes ------------------------------------------------------


def test_parse_sizes_reads_all_six_strata():
    assert parse_sizes(PILOT_SIZES) == {
        "S6": 1, "S5": 4, "S4": 3, "S3": 3, "S2": 4, "S1": 5}


@pytest.mark.parametrize("text, message", [
    ("S6=1,S5=4,S4=3,S3=3,S2=4", "missing: S1"),
    ("S6=1,S5=4,S4=3,S3=3,S2=4,S1=5,S7=1", "unknown stratum 'S7'"),
    ("S6=1,S6=2,S5=4,S4=3,S3=3,S2=4,S1=5", "named twice"),
    ("S6=-1,S5=4,S4=3,S3=3,S2=4,S1=5", "must not be negative"),
    ("S6=eins,S5=4,S4=3,S3=3,S2=4,S1=5", "not a whole number"),
    ("S6 1,S5=4,S4=3,S3=3,S2=4,S1=5", "has no '='"),
])
def test_parse_sizes_rejects_faulty_input(text, message):
    with pytest.raises(ValueError, match=message):
        parse_sizes(text)


# --- parse_exclude and apply_exclusion --------------------------------


def test_parse_exclude_reads_numbers_and_ignores_spaces():
    assert parse_exclude(" 48, 75 ,191,") == {48, 75, 191}


def test_parse_exclude_rejects_text():
    with pytest.raises(ValueError, match="'#75' is not a pull request number"):
        parse_exclude("48,#75")


def test_exclusion_stops_on_unknown_number():
    records = invented_records()
    with pytest.raises(ValueError, match="not in the eligible population: 9999"):
        apply_exclusion(records, {5, 9999})


def test_excluded_records_are_never_drawn():
    """Exclude most records of every stratum and draw with many seeds."""
    records = invented_records()
    excluded = {r["number"] for r in records if r["number"] % 20 not in (0, 1, 2, 3, 4, 5, 6)}
    sizes = parse_sizes(PILOT_SIZES)
    for seed in range(50):
        numbers = drawn_numbers(records, seed, sizes, excluded)
        assert not set(numbers) & excluded


# --- sizes ------------------------------------------------------------


def test_sizes_give_twenty_records_in_the_right_strata():
    records = invented_records()
    eligible = apply_exclusion(records, set())
    pools, unassigned = assign_strata(eligible)
    drawn, notes = draw(pools, unassigned, 20260921, parse_sizes(PILOT_SIZES))
    per_stratum = {}
    for key, _record in drawn:
        per_stratum[key] = per_stratum.get(key, 0) + 1
    assert per_stratum == {"S6": 1, "S5": 4, "S4": 3, "S3": 3, "S2": 4, "S1": 5}
    assert notes == []


def test_without_switches_the_draw_is_unchanged():
    """No --sizes means exactly the targets of the formulation probe."""
    records = invented_records()
    for seed in (1, 20260823, 20260921):
        assert (drawn_numbers(records, seed)
                == drawn_numbers(records, seed, dict(DEFAULT_SIZES)))
    assert sum(DEFAULT_SIZES.values()) == 12


# --- whole script -----------------------------------------------------


def test_script_writes_sizes_and_exclusion_into_the_file(tmp_path, monkeypatch):
    source = tmp_path / "pulls.jsonl"
    source.write_text(
        "\n".join(json.dumps(r) for r in invented_records()) + "\n",
        encoding="utf-8")
    target = tmp_path / "sample.md"
    monkeypatch.setattr(draw_sample, "current_commit", lambda: "test")
    code = draw_sample.main([
        "--input", str(source), "--output", str(target),
        "--seed", "20260921", "--sizes", PILOT_SIZES,
        "--exclude", "3,7", "--title", "Pilot sample A8",
    ])
    text = target.read_text(encoding="utf-8")
    assert code == 0
    assert text.startswith("# Pilot sample A8")
    assert "- Sizes per stratum (--sizes): S6=1,S5=4,S4=3,S3=3,S2=4,S1=5" in text
    assert "- Excluded before the draw (--exclude), 2: 3, 7" in text
    rows = [line for line in text.splitlines() if line.startswith("| ")
            and line.split("|")[1].strip().isdigit()]
    assert len(rows) == 20
    assert not {line.split("|")[1].strip() for line in rows} & {"3", "7"}


def test_script_stops_on_unknown_excluded_number(tmp_path, capsys):
    source = tmp_path / "pulls.jsonl"
    source.write_text(
        "\n".join(json.dumps(r) for r in invented_records()) + "\n",
        encoding="utf-8")
    target = tmp_path / "sample.md"
    code = draw_sample.main([
        "--input", str(source), "--output", str(target), "--exclude", "5000"])
    assert code == 1
    assert not target.exists()
    assert "5000" in capsys.readouterr().err
