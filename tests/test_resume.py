"""Test how an interrupted collection run finds out what is done.

Work package D, RQ1, decision D4. Every fetch script reads its own
earlier output to decide which pull requests still need handling. If
that reading is wrong, a resumed run either fetches pull requests
twice or skips them, and neither shows up as an error.

Note on scope: the one-line filter that turns "wanted" and "done" into
a to-do list sits inside main() and is not a separate function. What is
tested here are the functions that read the state from disk, which is
where a fault would be silent.
"""

from __future__ import annotations

import json

from fetch_pull_comments import handled_numbers
from fetch_pull_details import numbers_in_output, pull_numbers_from


def write_jsonl(path, records):
    """Write records as one JSON object per line."""
    with path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record) + "\n")
    return path


def test_numbers_already_fetched_are_recognised(tmp_path):
    """Numbers present in the output file count as done."""
    path = write_jsonl(tmp_path / "details.jsonl",
                       [{"number": 5}, {"number": 12}, {"number": 797}])

    assert numbers_in_output(path) == {5, 12, 797}


def test_an_absent_output_file_means_nothing_is_done(tmp_path):
    """The first run of a script starts with an empty set."""
    assert numbers_in_output(tmp_path / "details.jsonl") == set()


def test_a_resumed_run_skips_exactly_what_is_present(tmp_path):
    """Combining the wanted list with the done set leaves the remainder.

    This mirrors an interrupted run: three of five pull requests were
    written before the abort, so two are left.
    """
    source = write_jsonl(tmp_path / "list.jsonl",
                         [{"number": number} for number in (5, 12, 40, 97, 797)])
    output = write_jsonl(tmp_path / "details.jsonl",
                         [{"number": number} for number in (5, 12, 40)])

    wanted = pull_numbers_from(source)
    done = numbers_in_output(output)

    assert [number for number in wanted if number not in done] == [97, 797]


def test_number_order_does_not_depend_on_the_file_order(tmp_path):
    """Pull request numbers come back sorted and without duplicates.

    The numbers in the Qrisp repository have gaps, because issues and
    pull requests share one counter. Any processing has to read them
    from the file rather than count upwards.
    """
    path = write_jsonl(tmp_path / "list.jsonl",
                       [{"number": 797}, {"number": 5},
                        {"number": 40}, {"number": 5}])

    assert pull_numbers_from(path) == [5, 40, 797]


def test_progress_records_are_read_even_without_results(tmp_path):
    """A pull request with zero comments still counts as handled.

    222 pull requests carry no comment at all. Without a progress
    record they would be requested again on every resumed run.
    """
    path = write_jsonl(
        tmp_path / "comments.progress.jsonl",
        [{"number": 5, "fetched": 0, "expected": 0},
         {"number": 12, "fetched": 3, "expected": 3}],
    )

    assert handled_numbers(path) == {5, 12}
