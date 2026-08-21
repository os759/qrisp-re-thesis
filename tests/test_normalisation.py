"""Test the text cleaning applied during preparation.

Work package D, RQ1, decision D4. Two faults would be silent here.
Cleaning could eat real text, so a requirement would be reconstructed
from an incomplete description. Or it could be applied to patch text,
which would alter the source code the model reads. The measured basis
is the collection of 2026-08-19: CRLF line endings in 259 of 420
descriptions, template comments in 124.
"""

from __future__ import annotations

from build_interim import normalise_line_endings, normalise_prose


def test_windows_line_endings_become_unix_line_endings():
    """CRLF and a lone CR both collapse to a single newline."""
    assert normalise_line_endings("a\r\nb\rc") == "a\nb\nc"


def test_absent_patch_text_stays_absent():
    """GitHub omits the patch for 331 files; None must survive as None.

    Turning a missing patch into an empty string would hide the
    difference between "no change text delivered" and "changed to
    nothing".
    """
    assert normalise_line_endings(None) is None


def test_patch_text_keeps_its_comment_markers():
    """Source code is never stripped of comment markers.

    A changed HTML or Markdown file may legitimately contain the same
    marker the pull request template uses. Removing it would alter the
    code under study.
    """
    patch = "@@ -1 +1 @@\r\n-<!-- old note -->\r\n+<!-- new note -->"

    result = normalise_line_endings(patch)

    assert "<!-- old note -->" in result
    assert "<!-- new note -->" in result
    assert "\r" not in result


def test_a_complete_template_comment_is_removed():
    """The invisible template text carries no author statement."""
    result = normalise_prose("Fixes the parser\r\n<!-- describe here -->")

    assert result["text"] == "Fixes the parser"
    assert result["had_crlf"] is True
    assert result["had_template"] is True
    assert result["template_unterminated"] is False


def test_an_unterminated_marker_never_swallows_the_text():
    """Without a closing marker nothing is removed, only flagged.

    Cutting to the end of the text would destroy the description of
    every pull request whose author left a marker open.
    """
    result = normalise_prose("Real content <!-- forgot to close")

    assert result["text"] == "Real content <!-- forgot to close"
    assert result["template_unterminated"] is True


def test_text_after_a_template_comment_is_kept():
    """Removing a block must not remove what follows it."""
    result = normalise_prose("before\n<!-- hint -->\nafter")

    assert "before" in result["text"]
    assert "after" in result["text"]
    assert "hint" not in result["text"]


def test_a_missing_description_becomes_an_empty_string():
    """56 pull requests have no description at all."""
    for value in (None, "", "   \n\n  "):
        result = normalise_prose(value)
        assert result["text"] == ""
        assert result["had_template"] is False


def test_clean_text_is_returned_unchanged():
    """Text without CRLF and without a template must not be touched."""
    result = normalise_prose("First line\n\nSecond line")

    assert result["text"] == "First line\n\nSecond line"
    assert result["had_crlf"] is False
    assert result["had_template"] is False


def test_gaps_left_by_a_removed_block_are_closed():
    """Removing a block leaves blank lines; at most one is kept."""
    result = normalise_prose("a\n<!-- x -->\n\n\n\nb")

    assert result["text"] == "a\n\nb"
