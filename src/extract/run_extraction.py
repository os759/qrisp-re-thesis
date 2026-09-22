"""Send the source blocks of a sample to the OpenAI API and record the run.

Work package E, step A8, decisions E8 and E10. Research questions FF1,
FF2 and FF3 (cost, run time, data control).

What the script does, in this order:

1. Read the pull request numbers from a sample file, for example
   docs/sample_pilot_a8.md.
2. Take the matching source blocks from the model input. A missing block
   stops the script.
3. Build every message with prompt_files.py. That module also rejects a
   block that could break the separation of instruction and material.
4. Dry run (--dry-run): show what would be sent and estimate the cost.
   Nothing is sent and no key is needed.
5. Real run: send one block after the other. Every answer is appended to
   the raw file at once, so an interrupted run continues where it
   stopped and never pays twice for an answer it already has.
6. Derive the extraction file for validate_output.py and the manifest
   from the raw file.

Files, decision E10 c (all in data/processed/):
    extraction_<run id>.raw.jsonl       every answer in full, stays local
    extraction_<run id>.jsonl           parsed model output, stays local
    extraction_<run id>.manifest.json   the run record, is versioned

Error handling:
* network error, HTTP 5xx, HTTP 429 with code rate_limit_exceeded:
  wait and try again;
* any other HTTP 429, for example the spend limit: stop at once, because
  waiting does not help and trying again could cost money;
* any other error status (400, 401, 403, 404): stop at once.

The key is read from .env and is never written to any file.

Run from the project root:

    python src/extract/run_extraction.py --sample docs/sample_pilot_a8.md \\
        --run-id 2026-09-22_pilot --dry-run
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import subprocess
import sys
import time
import tomllib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "collect"))

from github_api import load_token  # noqa: E402
from prompt_files import (  # noqa: E402
    load_prompt,
    prompt_paths,
    prompt_sha256,
    render_user_message,
)

DEFAULT_CONFIG = Path("config/api_run.toml")
KEY_NAME = "OPENAI_API_KEY"
# Rough conversion for the dry run only, as in experiments/kostenschaetzung.md.
CHARS_PER_TOKEN = 3.5
# Sample files list the drawn pull requests as table rows "| 64 | S2 | ...".
SAMPLE_ROW = re.compile(r"^\| (\d+) \| S\d+ \|")
# Folders whose uncommitted changes would make the manifest's commit wrong.
SOURCE_PATHS = ("src", "config", "prompts")


class RunStopped(RuntimeError):
    """The run must stop, and trying again would not help."""


# --- configuration and input -----------------------------------------


def load_config(path: Path) -> dict[str, Any]:
    with path.open("rb") as handle:
        config = tomllib.load(handle)
    for section, keys in {
        "request": ("endpoint", "model", "reasoning_effort",
                    "max_output_tokens", "store"),
        "transport": ("timeout_seconds", "max_retries", "pause_seconds"),
        "prices": ("retrieved", "input_per_million", "output_per_million",
                   "cache_write_multiplier"),
        "files": ("prompt_version", "model_input", "output_directory"),
    }.items():
        for key in keys:
            if key not in config.get(section, {}):
                raise KeyError(f"{path}: [{section}] {key} is missing")
    if config["request"]["store"] is not False:
        raise ValueError(f"{path}: store must be false, decision E10")
    return config


def read_sample_numbers(path: Path) -> list[int]:
    """Pull request numbers from the table of a sample file, in order."""
    numbers = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = SAMPLE_ROW.match(line)
        if match:
            numbers.append(int(match.group(1)))
    if not numbers:
        raise ValueError(f"{path}: no pull request rows found")
    duplicates = sorted({n for n in numbers if numbers.count(n) > 1})
    if duplicates:
        raise ValueError(f"{path}: numbers listed twice: {duplicates}")
    return numbers


def select_blocks(path: Path, numbers: list[int]) -> dict[int, dict[str, Any]]:
    """The model input records for the given numbers. Stops if one is missing."""
    wanted = set(numbers)
    found: dict[int, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as handle:
        for raw in handle:
            raw = raw.strip()
            if not raw:
                continue
            record = json.loads(raw)
            if record.get("pull_number") in wanted:
                found[record["pull_number"]] = record
    missing = sorted(wanted - set(found))
    if missing:
        raise ValueError(f"{path}: no source block for {missing}")
    return found


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_output(*arguments: str) -> str:
    try:
        result = subprocess.run(["git", *arguments], capture_output=True,
                                text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return ""
    return result.stdout.strip()


def uncommitted_source_changes() -> list[str]:
    """Changed or new files below src/, config/ and prompts/."""
    listing = git_output("status", "--porcelain", "--", *SOURCE_PATHS)
    return [line for line in listing.splitlines() if line.strip()]


# --- request and answer ----------------------------------------------


def build_request_body(config: dict[str, Any], system_prompt: str,
                       user_message: str) -> dict[str, Any]:
    """The JSON body of one call. Only settings named in the config are sent."""
    request = config["request"]
    return {
        "model": request["model"],
        "instructions": system_prompt,
        "input": [{"role": "user", "content": user_message}],
        "reasoning": {"effort": request["reasoning_effort"]},
        "max_output_tokens": request["max_output_tokens"],
        "store": request["store"],
    }


def output_text(response: dict[str, Any]) -> str:
    """The visible text of an answer. Reasoning items carry no text here."""
    pieces = []
    for item in response.get("output") or []:
        if item.get("type") != "message":
            continue
        for part in item.get("content") or []:
            if part.get("type") == "output_text":
                pieces.append(part.get("text") or "")
    return "".join(pieces)


def parse_model_output(text: str) -> tuple[dict[str, Any] | None, str | None]:
    """Parse the answer strictly. Returns (object, None) or (None, reason).

    Nothing is repaired: text around the object or a code fence counts as
    a format error, because the prompt asks for the bare object. That rate
    is a measurement for FF2, decision E10 e.
    """
    stripped = text.strip()
    if not stripped:
        return None, "empty answer"
    try:
        value = json.loads(stripped)
    except json.JSONDecodeError as error:
        return None, f"not valid JSON: {error.msg} at position {error.pos}"
    if not isinstance(value, dict):
        return None, f"JSON is a {type(value).__name__}, not an object"
    return value, None


def usage_of(response: dict[str, Any]) -> dict[str, int]:
    usage = response.get("usage") or {}
    return {
        "input_tokens": int(usage.get("input_tokens") or 0),
        "cached_tokens": int((usage.get("input_tokens_details") or {})
                             .get("cached_tokens") or 0),
        "cache_write_tokens": int((usage.get("input_tokens_details") or {})
                                  .get("cache_write_tokens") or 0),
        "output_tokens": int(usage.get("output_tokens") or 0),
        "reasoning_tokens": int((usage.get("output_tokens_details") or {})
                                .get("reasoning_tokens") or 0),
    }


def cost_upper_bound(usage: dict[str, int], prices: dict[str, Any]) -> float:
    """US dollars. Writing to the cache costs a surcharge; reading from it
    is charged at the full input price here, so the result stays an upper
    bound. Found in step 7: the first call wrote 5 399 of 5 402 input
    tokens to the cache."""
    written = min(usage["cache_write_tokens"], usage["input_tokens"])
    other_input = usage["input_tokens"] - written
    return (other_input * prices["input_per_million"]
            + written * prices["input_per_million"]
            * prices["cache_write_multiplier"]
            + usage["output_tokens"] * prices["output_per_million"]) / 1_000_000


# --- transport -------------------------------------------------------


def error_code(response: requests.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return ""
    error = body.get("error") if isinstance(body, dict) else None
    if not isinstance(error, dict):
        return ""
    return str(error.get("code") or error.get("type") or "")


def wait_seconds(response: requests.Response | None, attempt: int) -> float:
    if response is not None:
        value = response.headers.get("retry-after")
        if value:
            try:
                return max(float(value), 1.0)
            except ValueError:
                pass
    return float(2 ** attempt)


Sender = Callable[[dict[str, Any]], requests.Response]


def make_sender(config: dict[str, Any], key: str) -> Sender:
    headers = {"Authorization": f"Bearer {key}",
               "Content-Type": "application/json"}
    endpoint = config["request"]["endpoint"]
    timeout = config["transport"]["timeout_seconds"]

    def send(body: dict[str, Any]) -> requests.Response:
        return requests.post(endpoint, headers=headers, json=body,
                             timeout=timeout)
    return send


def send_with_retry(send: Sender, body: dict[str, Any], max_retries: int,
                    sleep: Callable[[float], None] = time.sleep,
                    log: Callable[[str], None] = print) -> requests.Response:
    """Send one body. Returns a 200 response or raises RunStopped."""
    for attempt in range(1, max_retries + 1):
        try:
            response = send(body)
        except requests.RequestException as error:
            wait = wait_seconds(None, attempt)
            log(f"    network error ({type(error).__name__}); "
                f"retry in {wait:.0f}s [{attempt}/{max_retries}]")
            sleep(wait)
            continue
        status = response.status_code
        if status == 200:
            return response
        code = error_code(response)
        if status == 429 and code == "rate_limit_exceeded":
            wait = wait_seconds(response, attempt)
            log(f"    rate limited; waiting {wait:.0f}s [{attempt}/{max_retries}]")
            sleep(wait)
            continue
        if 500 <= status < 600:
            wait = wait_seconds(response, attempt)
            log(f"    server error HTTP {status}; retry in {wait:.0f}s "
                f"[{attempt}/{max_retries}]")
            sleep(wait)
            continue
        raise RunStopped(f"HTTP {status}, code '{code}': {response.text[:300]}")
    raise RunStopped(f"no answer after {max_retries} attempts")


# --- raw file and resume ----------------------------------------------


def read_raw(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    entries = []
    with path.open(encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, start=1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                entries.append(json.loads(raw))
            except json.JSONDecodeError as error:
                raise ValueError(f"{path}, line {line_number}: {error}") from error
    return entries


def answered_pulls(entries: list[dict[str, Any]]) -> set[int]:
    """Pull requests with a paid answer. They are never sent again."""
    return {entry["pull_number"] for entry in entries
            if entry.get("response") is not None}


def append_raw(path: Path, entry: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
        handle.flush()


# --- derived files ----------------------------------------------------


def summarise_entry(entry: dict[str, Any], prices: dict[str, Any]) -> dict[str, Any]:
    """One row of the manifest for one answer."""
    response = entry["response"]
    usage = usage_of(response)
    parsed, reason = parse_model_output(output_text(response))
    row = {
        "pull_number": entry["pull_number"],
        "response_id": response.get("id"),
        "model_returned": response.get("model"),
        "status": response.get("status"),
        "incomplete_reason": (response.get("incomplete_details") or {}).get("reason"),
        "reasoning": response.get("reasoning"),
        # Echoed by the API: evidence of the settings actually applied.
        "store_applied": response.get("store"),
        "temperature_applied": response.get("temperature"),
        "top_p_applied": response.get("top_p"),
        "service_tier": response.get("service_tier"),
        "started_at": entry.get("started_at"),
        "duration_seconds": entry.get("duration_seconds"),
        "attempts_logged": entry.get("attempts_logged", 0),
        **usage,
        "cost_upper_bound_usd": round(cost_upper_bound(usage, prices), 6),
        "valid_json_object": parsed is not None,
        "parse_problem": reason,
        "pull_number_in_output": parsed.get("pull_number") if parsed else None,
    }
    return row


def write_extraction(path: Path, entries: list[dict[str, Any]]) -> int:
    """Write every parsed answer, one per line. Returns the count."""
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for entry in entries:
            parsed, _reason = parse_model_output(output_text(entry["response"]))
            if parsed is not None:
                handle.write(json.dumps(parsed, ensure_ascii=False) + "\n")
                count += 1
    return count


def build_manifest(*, run_id: str, config: dict[str, Any], config_path: Path,
                   sample_path: Path, numbers: list[int], input_path: Path,
                   entries: list[dict[str, Any]], outcome: str,
                   stop_reason: str | None, started_at: str,
                   body_example: dict[str, Any], files: dict[str, str]) -> dict[str, Any]:
    prices = config["prices"]
    rows = [summarise_entry(entry, prices) for entry in entries]
    answered = {row["pull_number"] for row in rows}
    totals = {key: sum(row[key] for row in rows)
              for key in ("input_tokens", "cached_tokens",
                          "cache_write_tokens", "output_tokens",
                          "reasoning_tokens")}
    version = config["files"]["prompt_version"]
    return {
        "run_id": run_id,
        "outcome": outcome,
        "stop_reason": stop_reason,
        "started_at": started_at,
        "finished_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "code_commit": git_output("rev-parse", "HEAD") or "unknown",
        "request": {
            "endpoint": config["request"]["endpoint"],
            "model_requested": config["request"]["model"],
            "models_returned": sorted({str(row["model_returned"]) for row in rows}),
            "parameters_sent": {key: value for key, value in body_example.items()
                                if key not in ("instructions", "input")},
            "not_sent": ["temperature", "reasoning mode", "response format"],
        },
        "prompt": {
            "version": version,
            "files": [str(p) for p in prompt_paths(version)],
            "sha256": prompt_sha256(version),
        },
        "config": {"file": str(config_path), "sha256": sha256_of(config_path)},
        "sample": {"file": str(sample_path), "sha256": sha256_of(sample_path),
                   "pull_numbers": numbers},
        "model_input": {"file": str(input_path), "sha256": sha256_of(input_path)},
        "files": files,
        "prices_usd_per_million": prices,
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "requests": requests.__version__,
        },
        "counts": {
            "planned": len(numbers),
            "answered": len(answered),
            "not_answered": sorted(set(numbers) - answered),
            "completed": sum(1 for r in rows if r["status"] == "completed"),
            "incomplete": sum(1 for r in rows if r["status"] == "incomplete"),
            "valid_json_object": sum(1 for r in rows if r["valid_json_object"]),
            "pull_number_mismatch": sorted(
                r["pull_number"] for r in rows
                if r["valid_json_object"]
                and r["pull_number_in_output"] != r["pull_number"]),
        },
        "tokens": totals,
        "cost_upper_bound_usd": round(sum(r["cost_upper_bound_usd"] for r in rows), 4),
        "per_pull": rows,
    }


# --- main -------------------------------------------------------------


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the extraction on a sample.")
    parser.add_argument("--sample", required=True, type=Path,
                        help="sample file, e.g. docs/sample_pilot_a8.md")
    parser.add_argument("--run-id", required=True,
                        help="name of the run, e.g. 2026-09-22_pilot")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--limit", type=int, default=None,
                        help="send at most this many new blocks (step 7: 1)")
    parser.add_argument("--dry-run", action="store_true",
                        help="build everything, send nothing")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None,
         sender_factory: Callable[[dict[str, Any], str], Sender] = make_sender,
         sleep: Callable[[float], None] = time.sleep) -> int:
    arguments = parse_arguments(argv)
    if not re.fullmatch(r"[0-9A-Za-z_.-]+", arguments.run_id):
        print("--run-id may contain letters, digits, '.', '-' and '_' only",
              file=sys.stderr)
        return 1

    config = load_config(arguments.config)
    numbers = read_sample_numbers(arguments.sample)
    input_path = Path(config["files"]["model_input"])
    blocks = select_blocks(input_path, numbers)
    system_prompt, user_template = load_prompt(config["files"]["prompt_version"])

    bodies = {}
    for number in numbers:
        message = render_user_message(user_template, number,
                                      blocks[number]["source_block"])
        bodies[number] = build_request_body(config, system_prompt, message)

    out_dir = Path(config["files"]["output_directory"])
    raw_path = out_dir / f"extraction_{arguments.run_id}.raw.jsonl"
    extraction_path = out_dir / f"extraction_{arguments.run_id}.jsonl"
    manifest_path = out_dir / f"extraction_{arguments.run_id}.manifest.json"

    entries = read_raw(raw_path)
    done = answered_pulls(entries)
    unknown = sorted(done - set(numbers))
    if unknown:
        print(f"{raw_path} holds answers for pulls outside the sample: {unknown}",
              file=sys.stderr)
        return 1
    todo = [n for n in numbers if n not in done]
    if arguments.limit is not None:
        todo = todo[:arguments.limit]

    prices = config["prices"]
    print(f"sample: {len(numbers)} pulls, answered before: {len(done)}, "
          f"to send now: {len(todo)}")

    if arguments.dry_run:
        estimate_in = 0.0
        for number in todo:
            chars = len(bodies[number]["instructions"]) + len(
                bodies[number]["input"][0]["content"])
            tokens = chars / CHARS_PER_TOKEN
            estimate_in += tokens
            print(f"  pull {number:>4}: {chars:>7} characters, about "
                  f"{tokens:>7.0f} input tokens")
        low = (estimate_in * prices["input_per_million"]
               + len(todo) * 2000 * prices["output_per_million"]) / 1e6
        high = (estimate_in * prices["input_per_million"]
                + len(todo) * 4000 * prices["output_per_million"]) / 1e6
        print(f"estimate for these {len(todo)} calls: {low:.2f} to {high:.2f} US dollars "
              f"(2 000 to 4 000 output tokens each, prices of {prices['retrieved']})")
        print("dry run: nothing was sent, no file was written")
        return 0

    changes = uncommitted_source_changes()
    if changes:
        print("Uncommitted changes below src/, config/ or prompts/. Commit first, "
              "so that the manifest names the code that ran:", file=sys.stderr)
        for line in changes:
            print(f"  {line}", file=sys.stderr)
        return 1

    key = load_token(key=KEY_NAME)
    send = sender_factory(config, key)
    started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    outcome, stop_reason = "finished", None

    for position, number in enumerate(todo, start=1):
        print(f"[{position}/{len(todo)}] pull {number}")
        attempts: list[str] = []
        began = time.monotonic()
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        try:
            response = send_with_retry(
                send, bodies[number], config["transport"]["max_retries"],
                sleep=sleep, log=lambda text: (attempts.append(text), print(text)))
        except RunStopped as error:
            outcome, stop_reason = "stopped", f"pull {number}: {error}"
            print(f"  stopped: {error}", file=sys.stderr)
            break
        answer = response.json()
        entry = {
            "pull_number": number,
            "started_at": stamp,
            "duration_seconds": round(time.monotonic() - began, 2),
            "attempts_logged": len(attempts),
            "response": answer,
        }
        append_raw(raw_path, entry)
        entries.append(entry)
        row = summarise_entry(entry, prices)
        print(f"  {row['status']}, {row['input_tokens']} in / "
              f"{row['output_tokens']} out ({row['reasoning_tokens']} reasoning), "
              f"JSON object: {'yes' if row['valid_json_object'] else 'no'}")
        if position < len(todo):
            sleep(config["transport"]["pause_seconds"])

    if len({e["pull_number"] for e in entries}) < len(numbers) and outcome == "finished":
        outcome = "partial"
    written = write_extraction(extraction_path, entries)
    manifest = build_manifest(
        run_id=arguments.run_id, config=config, config_path=arguments.config,
        sample_path=arguments.sample, numbers=numbers, input_path=input_path,
        entries=entries, outcome=outcome, stop_reason=stop_reason,
        started_at=started_at, body_example=bodies[numbers[0]],
        files={"raw": str(raw_path), "extraction": str(extraction_path),
               "manifest": str(manifest_path)})
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")

    counts = manifest["counts"]
    print(f"\noutcome: {outcome}")
    print(f"answered: {counts['answered']} of {counts['planned']}, "
          f"incomplete: {counts['incomplete']}, "
          f"valid JSON objects: {counts['valid_json_object']}")
    print(f"tokens: {manifest['tokens']}")
    print(f"cost, upper bound: {manifest['cost_upper_bound_usd']:.4f} US dollars")
    print(f"extraction file: {extraction_path} ({written} records)")
    print(f"manifest: {manifest_path}")
    return 0 if outcome != "stopped" else 2


if __name__ == "__main__":
    raise SystemExit(main())
