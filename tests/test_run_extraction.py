"""Tests for run_extraction.py. No network: every answer is invented.

The tests cover the places where an error would silently cost money or
falsify the run record (criterion from D4): resume, stop on the spend
limit, strict parsing, token and cost figures, and the key never
reaching a file.

Work package E, step A8. Research questions FF1 and FF3.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src" / "extract"))
sys.path.insert(0, str(ROOT / "src" / "collect"))

import run_extraction as run  # noqa: E402

FAKE_KEY = "sk-test-0123456789-not-a-real-key"


# --- helpers ----------------------------------------------------------


class FakeResponse(requests.Response):
    def __init__(self, status: int, body: dict, headers: dict | None = None):
        super().__init__()
        self.status_code = status
        self._content = json.dumps(body).encode("utf-8")
        self.headers.update(headers or {})


def answer(pull: int, text: str | None = None, status: str = "completed",
           model: str = "gpt-5.6-terra-invented") -> dict:
    if text is None:
        text = json.dumps({"schema_version": 2, "pull_number": pull,
                           "processing_status": "no_requirements_found",
                           "status_reason": "invented", "requirements": []})
    return {
        "id": f"resp_{pull}", "model": model, "status": status,
        "incomplete_details": {"reason": "max_output_tokens"}
        if status == "incomplete" else None,
        "reasoning": {"effort": "medium"},
        "output": [
            {"type": "reasoning", "summary": []},
            {"type": "message", "content": [{"type": "output_text", "text": text}]},
        ],
        "usage": {"input_tokens": 1000, "input_tokens_details": {"cached_tokens": 200},
                  "output_tokens": 300, "output_tokens_details": {"reasoning_tokens": 100}},
    }


CONFIG = """
[request]
endpoint = "https://example.invalid/v1/responses"
model = "gpt-5.6-terra"
reasoning_effort = "medium"
max_output_tokens = 25000
store = false
[transport]
timeout_seconds = 5
max_retries = 3
pause_seconds = 0
[prices]
retrieved = "2026-09-21"
input_per_million = 2.00
output_per_million = 12.00
[files]
prompt_version = "v1"
model_input = "data/processed/model_input_test.jsonl"
output_directory = "data/processed"
"""


@pytest.fixture
def project(tmp_path, monkeypatch):
    """An invented project root with prompts, config, input and sample."""
    (tmp_path / "prompts").mkdir()
    (tmp_path / "prompts" / "extraction_system_v1.md").write_text(
        "invented system prompt", encoding="utf-8")
    (tmp_path / "prompts" / "extraction_user_v1.md").write_text(
        "PR $pull_number\n<<<SOURCE_BLOCK_START>>>\n$source_block\n"
        "<<<SOURCE_BLOCK_END>>>\n", encoding="utf-8")
    (tmp_path / "config").mkdir()
    (tmp_path / "config" / "api_run.toml").write_text(CONFIG, encoding="utf-8")
    (tmp_path / "data" / "processed").mkdir(parents=True)
    lines = [json.dumps({"pull_number": n,
                         "source_block": f"=== PULL REQUEST {n} ===\n[TITLE]\nx"})
             for n in (5, 7, 9, 11)]
    (tmp_path / "data" / "processed" / "model_input_test.jsonl").write_text(
        "\n".join(lines) + "\n", encoding="utf-8")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "sample.md").write_text(
        "| PR | Stratum |\n|---|---|\n| 5 | S2 | merged |\n| 7 | S5 | merged |\n"
        "| 9 | S1 | merged |\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(run, "load_token", lambda key: FAKE_KEY)
    monkeypatch.setattr(run, "uncommitted_source_changes", lambda: [])
    return tmp_path


def factory_from(responses: dict[int, list]):
    """A sender that answers per pull number from a list of responses."""
    calls: list[int] = []

    def factory(config, key):
        assert key == FAKE_KEY

        def send(body):
            number = int(body["input"][0]["content"].split()[1])
            calls.append(number)
            item = responses[number].pop(0)
            if isinstance(item, Exception):
                raise item
            return item
        return send
    return factory, calls


ARGS = ["--sample", "docs/sample.md", "--run-id", "test_run"]


# --- request body -----------------------------------------------------


def test_request_body_sends_store_false_and_effort(project):
    config = run.load_config(Path("config/api_run.toml"))
    body = run.build_request_body(config, "SYS", "USER")
    assert body == {"model": "gpt-5.6-terra", "instructions": "SYS",
                    "input": [{"role": "user", "content": "USER"}],
                    "reasoning": {"effort": "medium"},
                    "max_output_tokens": 25000, "store": False}


def test_config_with_store_true_is_rejected(tmp_path):
    path = tmp_path / "api_run.toml"
    path.write_text(CONFIG.replace("store = false", "store = true"), encoding="utf-8")
    with pytest.raises(ValueError, match="store must be false"):
        run.load_config(path)


# --- answer parsing ---------------------------------------------------


def test_output_text_skips_reasoning_items():
    assert run.output_text(answer(5, text='{"a": 1}')) == '{"a": 1}'


@pytest.mark.parametrize("text, problem", [
    ("", "empty answer"),
    ('```json\n{"a": 1}\n```', "not valid JSON"),
    ('Here it is: {"a": 1}', "not valid JSON"),
    ('[1, 2]', "not an object"),
])
def test_parsing_is_strict(text, problem):
    parsed, reason = run.parse_model_output(text)
    assert parsed is None and problem in reason


def test_usage_and_cost():
    usage = run.usage_of(answer(5))
    assert usage == {"input_tokens": 1000, "cached_tokens": 200,
                     "output_tokens": 300, "reasoning_tokens": 100}
    cost = run.cost_upper_bound(usage, {"input_per_million": 2.0,
                                        "output_per_million": 12.0})
    assert cost == pytest.approx(0.0056)


# --- transport --------------------------------------------------------


def test_server_error_is_retried():
    replies = [FakeResponse(500, {}), FakeResponse(200, answer(5))]
    waits = []
    result = run.send_with_retry(lambda body: replies.pop(0), {}, 3,
                                 sleep=waits.append, log=lambda _t: None)
    assert result.status_code == 200 and len(waits) == 1


def test_rate_limit_is_retried_with_retry_after():
    replies = [FakeResponse(429, {"error": {"code": "rate_limit_exceeded"}},
                            {"retry-after": "7"}),
               FakeResponse(200, answer(5))]
    waits = []
    run.send_with_retry(lambda body: replies.pop(0), {}, 3,
                        sleep=waits.append, log=lambda _t: None)
    assert waits == [7.0]


@pytest.mark.parametrize("status, body", [
    (429, {"error": {"code": "insufficient_quota"}}),
    (429, {"error": {"type": "billing_limit"}}),
    (429, {}),
    (401, {"error": {"code": "invalid_api_key"}}),
    (404, {"error": {"code": "model_not_found"}}),
])
def test_other_errors_stop_at_once(status, body):
    calls = []

    def send(_body):
        calls.append(1)
        return FakeResponse(status, body)
    with pytest.raises(run.RunStopped):
        run.send_with_retry(send, {}, 5, sleep=lambda _s: None, log=lambda _t: None)
    assert len(calls) == 1


def test_network_errors_give_up_after_max_retries():
    def send(_body):
        raise requests.ConnectionError("invented")
    with pytest.raises(run.RunStopped, match="after 3 attempts"):
        run.send_with_retry(send, {}, 3, sleep=lambda _s: None, log=lambda _t: None)


# --- input ------------------------------------------------------------


def test_sample_numbers_are_read_in_order(project):
    assert run.read_sample_numbers(Path("docs/sample.md")) == [5, 7, 9]


def test_sample_with_duplicate_is_rejected(tmp_path):
    path = tmp_path / "s.md"
    path.write_text("| 5 | S2 |\n| 5 | S2 |\n", encoding="utf-8")
    with pytest.raises(ValueError, match="listed twice"):
        run.read_sample_numbers(path)


def test_missing_block_stops(project):
    with pytest.raises(ValueError, match=r"no source block for \[99\]"):
        run.select_blocks(Path("data/processed/model_input_test.jsonl"), [5, 99])


# --- whole run --------------------------------------------------------


def test_dry_run_sends_nothing_and_writes_nothing(project, capsys):
    factory, calls = factory_from({})
    assert run.main(ARGS + ["--dry-run"], sender_factory=factory) == 0
    assert calls == []
    assert list((project / "data" / "processed").glob("extraction_*")) == []
    assert "nothing was sent" in capsys.readouterr().out


def test_full_run_writes_three_files_and_counts(project):
    factory, calls = factory_from({
        5: [FakeResponse(200, answer(5))],
        7: [FakeResponse(200, answer(7, text="not json"))],
        9: [FakeResponse(200, answer(9, status="incomplete", text=""))],
    })
    assert run.main(ARGS, sender_factory=factory, sleep=lambda _s: None) == 0
    assert calls == [5, 7, 9]
    out = project / "data" / "processed"
    manifest = json.loads((out / "extraction_test_run.manifest.json").read_text())
    assert manifest["outcome"] == "finished"
    assert manifest["counts"]["answered"] == 3
    assert manifest["counts"]["incomplete"] == 1
    assert manifest["counts"]["valid_json_object"] == 1
    assert manifest["tokens"]["reasoning_tokens"] == 300
    assert manifest["request"]["parameters_sent"]["store"] is False
    assert manifest["request"]["models_returned"] == ["gpt-5.6-terra-invented"]
    lines = (out / "extraction_test_run.jsonl").read_text().splitlines()
    assert [json.loads(line)["pull_number"] for line in lines] == [5]


def test_resume_never_sends_an_answered_pull_again(project):
    factory, calls = factory_from({5: [FakeResponse(200, answer(5))]})
    assert run.main(ARGS + ["--limit", "1"], sender_factory=factory,
                    sleep=lambda _s: None) == 0
    assert calls == [5]
    factory, calls = factory_from({7: [FakeResponse(200, answer(7))],
                                   9: [FakeResponse(200, answer(9))]})
    assert run.main(ARGS, sender_factory=factory, sleep=lambda _s: None) == 0
    assert calls == [7, 9]
    manifest = json.loads((project / "data" / "processed" /
                           "extraction_test_run.manifest.json").read_text())
    assert manifest["counts"]["answered"] == 3


def test_spend_limit_stops_the_run_and_keeps_what_was_paid(project):
    factory, calls = factory_from({
        5: [FakeResponse(200, answer(5))],
        7: [FakeResponse(429, {"error": {"code": "insufficient_quota"}})],
        9: [FakeResponse(200, answer(9))],
    })
    assert run.main(ARGS, sender_factory=factory, sleep=lambda _s: None) == 2
    assert calls == [5, 7]
    manifest = json.loads((project / "data" / "processed" /
                           "extraction_test_run.manifest.json").read_text())
    assert manifest["outcome"] == "stopped"
    assert manifest["counts"]["not_answered"] == [7, 9]


def test_key_never_reaches_a_file(project):
    factory, _calls = factory_from({n: [FakeResponse(200, answer(n))] for n in (5, 7, 9)})
    run.main(ARGS, sender_factory=factory, sleep=lambda _s: None)
    for path in (project / "data" / "processed").glob("extraction_*"):
        assert FAKE_KEY not in path.read_text(encoding="utf-8")


def test_uncommitted_source_changes_block_a_real_run(project, monkeypatch):
    monkeypatch.setattr(run, "uncommitted_source_changes", lambda: [" M src/x.py"])
    factory, calls = factory_from({})
    assert run.main(ARGS, sender_factory=factory) == 1
    assert calls == []
