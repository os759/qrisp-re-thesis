"""Replace GitHub mentions in prose by stable placeholders.

Decision E9. A login carries nothing that a requirement needs, so it is
replaced before the text is handed to an external model. The replacement
is stable: the same login always becomes the same placeholder, and a run
repeated on the same data gives the same result.

Where the replacement applies:

* prose only, that is the title, the description and the body of a
  comment or a review comment;
* never in a code change and never in the diff context of a review
  comment;
* inside a fenced or indented code block or an inline code span only for
  a login that is already known from prose. A Python decorator such as
  @property never enters the mapping, so it stays untouched, while
  `@alice` in backticks is still replaced.

Two safeguards keep code symbols out of the mapping:

* the context rules above;
* an allowlist in the configuration, for names that appear in prose but
  denote a decorator. In the data of 2026-09-15 these are jaspify, jax
  and pytest.

The mapping is written next to the prepared dataset, not into the
repository, because it can undo the replacement.

Work package E, bachelor thesis. Research question FF3, data control.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

# A mention starts at a word boundary. The character before must not be a
# word character (this keeps e-mail addresses out), a dot or a hyphen. A
# backtick is allowed, because `@alice` in code is handled by mask itself. GitHub logins are at most 39 characters long and contain no
# underscore; a token followed by one is therefore not a login. That also
# keeps the placeholders themselves out, so masking twice changes nothing.
MENTION = re.compile(
    r"(?<![\w.@-])@([A-Za-z0-9][A-Za-z0-9-]{0,38})(?![A-Za-z0-9\-_])")

FENCES = ("```", "~~~")
INLINE_CODE = re.compile(r"`[^`]*`")
# An indented line is normally a code block. A nested list item is not,
# although it carries the same indentation: "    - [ ] @alice and the
# students" is prose. The marker is checked before the indentation.
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)]|>)\s")


def _prose_spans(text: str) -> list[tuple[int, int]]:
    """Return the character ranges of text that is prose, not code."""
    spans: list[tuple[int, int]] = []
    offset = 0
    in_fence = False
    for line in text.split("\n"):
        end = offset + len(line)
        stripped = line.lstrip()
        if stripped.startswith(FENCES):
            in_fence = not in_fence
        elif in_fence:
            pass
        elif line.startswith(("    ", "\t")) and not LIST_ITEM.match(line):
            pass
        else:
            start = offset
            for match in INLINE_CODE.finditer(line):
                spans.append((start, offset + match.start()))
                start = offset + match.end()
            spans.append((start, end))
        offset = end + 1  # the newline
    return [(a, b) for a, b in spans if b > a]


def find_mentions(text: str, allowlist: set[str]) -> list[str]:
    """Return the logins mentioned in the prose of one text, in order."""
    found = []
    for start, end in _prose_spans(text or ""):
        for match in MENTION.finditer(text, start, end):
            login = match.group(1)
            if login.lower() not in allowlist:
                found.append(login)
    return found


def build_mapping(logins: set[str], prefix: str = "person") -> dict[str, str]:
    """Assign a placeholder to every login, sorted so a rerun is identical."""
    ordered = sorted({login.lower() for login in logins})
    width = max(2, len(str(len(ordered))))
    return {login: f"{prefix}_{number:0{width}d}"
            for number, login in enumerate(ordered, start=1)}


def mask(text: str, mapping: dict[str, str], allowlist: set[str]) -> str:
    """Replace the mentions of one text.

    In prose, every mention is replaced; a login that is not in the mapping
    becomes a placeholder for an unknown person, so nothing slips through.
    In code, only a login that the mapping already knows is replaced.
    """
    if not text:
        return text
    spans = _prose_spans(text)
    pieces = []
    last = 0
    for match in MENTION.finditer(text):
        login = match.group(1).lower()
        if login in allowlist:
            continue
        in_prose = any(start <= match.start() < end for start, end in spans)
        if in_prose:
            placeholder = mapping.get(login, "person_unknown")
        elif login in mapping:
            placeholder = mapping[login]
        else:
            continue  # a code symbol, left as it is
        pieces.append(text[last:match.start()])
        pieces.append("@" + placeholder)
        last = match.end()
    pieces.append(text[last:])
    return "".join(pieces)


def save_mapping(mapping: dict[str, str], path: Path) -> None:
    path.write_text(
        json.dumps(mapping, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")


def load_mapping(path: Path) -> dict[str, str]:
    return json.loads(path.read_text(encoding="utf-8"))
