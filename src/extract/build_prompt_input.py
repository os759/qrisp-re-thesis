"""Build the source block that is handed to the model, one per pull request.

The prepared dataset is not changed. This step only derives a bounded,
readable text from it. Two rules govern the result:

* Selection, decision E4. Bot contributions and pull requests that are
  still open are left out. Drafts, missing descriptions and missing code
  changes are kept, because the remaining fields are still a source.
* Budget, decision E5. The context of a review comment (diff_hunk) is
  capped, and the whole block has an upper character limit. Prose is kept
  first, file diffs are cut first, and every cut is marked in the text.

Author logins are never written into the block. Only the association
(CONTRIBUTOR, COLLABORATOR, NONE) is passed on. It carries the part that
matters for a requirement and avoids sending personal data to a model.

Work package E, bachelor thesis. Research question FF1.

Run from the project root:

    python src/extract/build_prompt_input.py \
      --input data/interim/pulls_prepared_2026-08-19.jsonl \
      --output data/processed/model_input_2026-09-15.jsonl
"""

from __future__ import annotations

import argparse
import hashlib
import json
import tomllib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_CONFIG = Path("config/model_input.toml")

# Characters held back for the closing note about what was left out.
NOTE_ALLOWANCE = 300


# --- configuration ----------------------------------------------------


def load_settings(path: Path) -> dict[str, Any]:
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    settings = data["model_input"]
    for key in ("exclude_bots", "exclude_open", "include_drafts",
                "max_diff_hunk_chars", "max_input_chars_per_pull",
                "truncation_marker"):
        if key not in settings:
            raise KeyError(f"{path}: setting '{key}' is missing")
    return settings


# --- selection, decision E4 -------------------------------------------


def selection_reason(pull: dict[str, Any], settings: dict[str, Any]) -> str | None:
    """Return why the pull request is left out, or None if it is kept."""
    if settings["exclude_bots"] and pull.get("author_is_bot"):
        return "bot"
    if settings["exclude_open"] and pull.get("outcome") == "open":
        return "open"
    if not settings["include_drafts"] and pull.get("draft"):
        return "draft"
    return None


# --- block assembly ---------------------------------------------------


def cap(text: str, limit: int, marker: str) -> tuple[str, bool]:
    """Shorten text to limit characters and say whether it was cut."""
    if len(text) <= limit:
        return text, False
    return text[:limit] + marker, True


def prose_sections(pull: dict[str, Any],
                   settings: dict[str, Any]) -> tuple[list[str], int]:
    """Title, description and comments, in that order. Returns the
    sections and how many review contexts were capped."""
    marker = settings["truncation_marker"]
    hunk_limit = settings["max_diff_hunk_chars"]
    sections = [f"[TITLE]\n{pull.get('title') or ''}"]

    body = (pull.get("body") or "").strip()
    sections.append(f"[DESCRIPTION]\n{body}" if body
                    else "[DESCRIPTION]\n(the pull request has no description)")

    capped = 0
    entries: list[tuple[str, str]] = []

    for comment in pull.get("issue_comments", []):
        head = (f"[COMMENT id={comment.get('id')} "
                f"association={comment.get('author_association')} "
                f"at={comment.get('created_at')}]")
        entries.append((comment.get("created_at") or "",
                        f"{head}\n{(comment.get('body') or '').strip()}"))

    for comment in pull.get("review_comments", []):
        context, was_capped = cap(comment.get("diff_hunk") or "", hunk_limit, marker)
        capped += int(was_capped)
        head = (f"[REVIEW COMMENT id={comment.get('id')} "
                f"association={comment.get('author_association')} "
                f"at={comment.get('created_at')} "
                f"file={comment.get('path')} line={comment.get('line')}]")
        block = f"{head}\n[context]\n{context}\n[text]\n{(comment.get('body') or '').strip()}"
        entries.append((comment.get("created_at") or "", block))

    entries.sort(key=lambda item: item[0])
    sections.extend(block for _, block in entries)
    return sections, capped


def file_sections(pull: dict[str, Any]) -> list[str]:
    sections = []
    for entry in pull.get("files", []):
        head = (f"[FILE {entry.get('filename')} status={entry.get('status')} "
                f"+{entry.get('additions')} -{entry.get('deletions')}]")
        patch = entry.get("patch") or ""
        if not patch:
            reason = entry.get("patch_drop_reason") or "no patch text available"
            sections.append(f"{head}\n(diff not included: {reason})")
        else:
            sections.append(f"{head}\n{patch}")
    return sections


def build_block(pull: dict[str, Any],
                settings: dict[str, Any]) -> dict[str, Any]:
    """Assemble the source block and report what had to be left out."""
    budget = settings["max_input_chars_per_pull"]
    marker = settings["truncation_marker"]
    # Room is held back for the closing note, so the finished block never
    # exceeds the budget.
    limit = budget - NOTE_ALLOWANCE

    header = f"=== PULL REQUEST {pull.get('number')} ==="
    prose, hunks_capped = prose_sections(pull, settings)
    files = file_sections(pull)

    parts = [header]
    used = len(header)
    dropped_prose = 0
    dropped_files = 0

    # Prose first: a requirement is normally stated in words, not in code.
    for section in prose:
        if used + len(section) + 2 > limit:
            dropped_prose += 1
            continue
        parts.append(section)
        used += len(section) + 2

    for section in files:
        if used + len(section) + 2 > limit:
            dropped_files += 1
            continue
        parts.append(section)
        used += len(section) + 2

    if dropped_prose or dropped_files:
        note = (f"[BUDGET NOTE] {dropped_prose} comment sections and "
                f"{dropped_files} file sections were left out because the "
                f"character budget of {budget} was reached.{marker}")
        parts.append(note)

    block = "\n\n".join(parts)
    if len(block) > budget:  # must not happen, guards against a wrong allowance
        block = block[:budget - len(marker)] + marker
    return {
        "source_block": block,
        "chars": len(block),
        "truncated": bool(dropped_prose or dropped_files or hunks_capped),
        "omitted": {
            "comment_sections": dropped_prose,
            "file_sections": dropped_files,
            "review_contexts_capped": hunks_capped,
        },
    }


# --- input and output -------------------------------------------------


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the model input from the prepared dataset.")
    parser.add_argument("--input", required=True, help="Prepared dataset, JSONL.")
    parser.add_argument("--output", required=True, help="Target file, JSONL.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--overwrite", action="store_true",
                        help="Allow an existing output file to be replaced.")
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    settings = load_settings(Path(arguments.config))

    source = Path(arguments.input)
    target = Path(arguments.output)
    if target.exists() and not arguments.overwrite:
        print(f"{target} already exists. Use --overwrite to replace it.")
        return 1

    kept = 0
    left_out: dict[str, int] = {}
    truncated = 0
    total_chars = 0

    with source.open(encoding="utf-8") as handle, \
            target.open("w", encoding="utf-8") as out:
        for raw in handle:
            raw = raw.strip()
            if not raw:
                continue
            pull = json.loads(raw)
            reason = selection_reason(pull, settings)
            if reason is not None:
                left_out[reason] = left_out.get(reason, 0) + 1
                continue

            result = build_block(pull, settings)
            record = {
                "pull_number": pull["number"],
                "html_url": pull.get("html_url"),
                "outcome": pull.get("outcome"),
                "draft": pull.get("draft"),
                **result,
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            kept += 1
            truncated += int(result["truncated"])
            total_chars += result["chars"]

    manifest = {
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "input_file": str(source),
        "input_sha256": sha256_of(source),
        "output_file": str(target),
        "config_file": str(Path(arguments.config)),
        "settings": settings,
        "pulls_kept": kept,
        "pulls_left_out": left_out,
        "pulls_with_a_cut": truncated,
        "characters_total": total_chars,
    }
    manifest_path = target.with_suffix(".manifest.json")
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Pulls kept: {kept}")
    print(f"Pulls left out: {left_out}")
    print(f"Pulls with a cut: {truncated}")
    print(f"Characters total: {total_chars}")
    print(f"Manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
