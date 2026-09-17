"""Load the versioned prompt files and assemble the message for one pull request.

The system prompt is sent unchanged for every pull request. The user message
is built from a template with two placeholders, $pull_number and
$source_block. string.Template is used instead of str.format because the
prompt text contains curly braces from the JSON example.

Two guards protect the separation of instruction and material (decision E5,
chapter 5, prompt injection):

* A source block that contains one of the delimiter lines is rejected. It
  could otherwise close the material early and place text outside it.
* The number in the block header has to match the given pull request number.

Work package E, bachelor thesis. Research question FF1.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from string import Template

PROMPT_DIR = Path("prompts")
BLOCK_START = "<<<SOURCE_BLOCK_START>>>"
BLOCK_END = "<<<SOURCE_BLOCK_END>>>"


class PromptInputError(ValueError):
    """Raised when a source block must not be sent to the model."""


def prompt_paths(version: str, directory: Path = PROMPT_DIR) -> tuple[Path, Path]:
    """Return the system and user file for a prompt version such as 'v1'."""
    return (directory / f"extraction_system_{version}.md",
            directory / f"extraction_user_{version}.md")


def load_prompt(version: str, directory: Path = PROMPT_DIR) -> tuple[str, str]:
    """Read the system prompt and the user template of one version."""
    system_path, user_path = prompt_paths(version, directory)
    return (system_path.read_text(encoding="utf-8"),
            user_path.read_text(encoding="utf-8"))


def prompt_sha256(version: str, directory: Path = PROMPT_DIR) -> dict[str, str]:
    """Checksums of both files, for the run manifest."""
    result = {}
    for path in prompt_paths(version, directory):
        result[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def render_user_message(template: str, pull_number: int, source_block: str) -> str:
    """Insert one source block into the user template."""
    for delimiter in (BLOCK_START, BLOCK_END):
        if delimiter in source_block:
            raise PromptInputError(
                f"pull {pull_number}: source block contains the delimiter {delimiter}")
    expected_header = f"=== PULL REQUEST {pull_number} ==="
    if not source_block.startswith(expected_header):
        raise PromptInputError(
            f"pull {pull_number}: source block does not start with '{expected_header}'")
    return Template(template).substitute(
        pull_number=pull_number, source_block=source_block)
