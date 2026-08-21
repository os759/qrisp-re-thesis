"""Test the three truncation stages applied to patch text.

Work package D, RQ1, decisions D1 and D4. This is where the dataset
changes most: in the run of 2026-08-19, 4580 of 8424 files lost their
patch text and 32555716 characters were reduced to 7396580. A fault
here would silently remove source code that a requirement was meant to
be reconstructed from, or silently exceed the budget a model can read.

The stages are: 1) no patch text for excluded file types and for files
the API delivered without one, 2) an upper limit per single file,
3) a character budget for the whole pull request, spent in the order
the API delivered the files.
"""

from __future__ import annotations

import pytest

from build_interim import prepare_files

MARKER = "\n[... truncated ...]\n"


@pytest.fixture
def settings():
    """The truncation settings, matching config/collect.toml."""
    return {
        "skip_patch_extensions": [".ipynb", ".drawio", ".bkp", ".svg"],
        "max_patch_chars_per_file": 100,
        "max_patch_chars_per_pull": 300,
        "truncation_marker": MARKER,
    }


def raw_file(filename, patch, additions=3, deletions=1):
    """Build one changed file record as the files endpoint returns it."""
    return {"filename": filename, "status": "modified",
            "additions": additions, "deletions": deletions,
            "changes": additions + deletions, "patch": patch,
            "sha": "s" * 40, "blob_url": "b", "raw_url": "r"}


def test_stage_one_drops_excluded_file_types(settings):
    """A notebook carries no readable diff, so its patch text goes."""
    prepared, counters = prepare_files(
        [raw_file("examples/demo.ipynb", "x" * 50)], settings)

    assert prepared[0]["patch"] is None
    assert prepared[0]["patch_drop_reason"] == "excluded_file_type"
    assert counters["stage1_dropped"] == 1


def test_stage_one_keeps_name_and_line_counts(settings):
    """Decision D1 keeps the file itself, only the patch text goes.

    Without the name and the line counts, the record would no longer
    show that the file was touched at all.
    """
    prepared, _ = prepare_files(
        [raw_file("docs/plan.drawio", "x" * 50, additions=7, deletions=2)],
        settings)

    assert prepared[0]["filename"] == "docs/plan.drawio"
    assert prepared[0]["additions"] == 7
    assert prepared[0]["deletions"] == 2


def test_stage_one_handles_a_file_the_api_sent_without_a_patch(settings):
    """GitHub omits the patch for binary and very large files."""
    prepared, counters = prepare_files(
        [raw_file("img/logo.png", None)], settings)

    assert prepared[0]["patch_drop_reason"] == "no_patch_from_api"
    assert prepared[0]["patch_chars_original"] == 0
    assert counters["stage1_dropped"] == 1


def test_the_file_type_check_ignores_capitalisation(settings):
    """An upper case extension must be excluded just the same."""
    prepared, _ = prepare_files(
        [raw_file("examples/Demo.IPYNB", "x" * 50)], settings)

    assert prepared[0]["patch_drop_reason"] == "excluded_file_type"


def test_a_short_patch_passes_through_unchanged(settings):
    """Below every limit, the text must arrive exactly as it was."""
    patch = "@@ -1 +1 @@\n-old line\n+new line"
    prepared, counters = prepare_files([raw_file("src/a.py", patch)],
                                       settings)

    assert prepared[0]["patch"] == patch
    assert prepared[0]["patch_kept"] is True
    assert prepared[0]["patch_truncated"] is False
    assert counters["stage2_truncated"] == 0
    assert counters["stage3_truncated"] == 0


def test_stage_two_caps_a_single_large_file(settings):
    """One oversized file is cut to the per file limit, and marked."""
    prepared, counters = prepare_files([raw_file("src/big.py", "z" * 500)],
                                       settings)

    assert prepared[0]["patch"].endswith(MARKER)
    assert prepared[0]["patch_truncated"] is True
    assert prepared[0]["patch_chars_original"] == 500
    assert prepared[0]["patch_chars_kept"] == 100 + len(MARKER)
    assert counters["stage2_truncated"] == 1


def test_a_cut_keeps_the_beginning_of_the_diff(settings):
    """Truncation removes the end, never the start.

    A diff header names the file and the line range. Losing it would
    make the remaining text impossible to place.
    """
    patch = "@@ -1,5 +1,5 @@ header\n" + "z" * 500
    prepared, _ = prepare_files([raw_file("src/big.py", patch)], settings)

    assert prepared[0]["patch"].startswith("@@ -1,5 +1,5 @@ header")


def test_stage_three_stops_once_the_budget_is_spent(settings):
    """Files are served in order until the pull request budget is gone."""
    records = [raw_file(f"src/m{index}.py", "q" * 90) for index in range(6)]

    prepared, counters = prepare_files(records, settings)

    kept = [item["patch_kept"] for item in prepared]
    assert kept[:3] == [True, True, True]
    assert kept[4:] == [False, False]
    assert counters["stage3_dropped"] >= 1
    assert prepared[5]["patch_drop_reason"] == "pull_budget_exhausted"


def test_the_pull_request_budget_is_never_exceeded(settings):
    """The kept characters stay within the configured budget."""
    records = [raw_file(f"src/m{index}.py", "q" * 90) for index in range(20)]

    _, counters = prepare_files(records, settings)

    assert counters["chars_kept"] <= settings["max_patch_chars_per_pull"]


def test_no_file_disappears_from_the_record(settings):
    """Every changed file stays listed, whatever happens to its patch.

    Dropping the file itself would understate how many files a pull
    request touched, and the count would no longer match the API.
    """
    records = [raw_file("examples/demo.ipynb", "x" * 50),
               raw_file("img/logo.png", None),
               raw_file("src/a.py", "@@ -1 +1 @@\n-a\n+b")]
    records += [raw_file(f"src/m{index}.py", "q" * 90) for index in range(10)]

    prepared, _ = prepare_files(records, settings)

    assert len(prepared) == len(records)
    assert [item["filename"] for item in prepared] == \
           [item["filename"] for item in records]


def test_the_original_size_is_recorded_even_when_the_patch_is_dropped(
        settings):
    """chars_original counts what arrived, chars_kept what remains.

    Both numbers are needed to state how much of the change text the
    preparation removed.
    """
    records = [raw_file("examples/demo.ipynb", "x" * 400),
               raw_file("src/a.py", "y" * 50)]

    _, counters = prepare_files(records, settings)

    assert counters["chars_original"] == 450
    assert counters["chars_kept"] == 50


def test_an_empty_pull_request_produces_no_files_and_no_counts(settings):
    """Five pull requests changed no file at all (decision D6)."""
    prepared, counters = prepare_files([], settings)

    assert prepared == []
    assert counters["chars_original"] == 0
    assert counters["chars_kept"] == 0
    assert counters["stage1_dropped"] == 0
