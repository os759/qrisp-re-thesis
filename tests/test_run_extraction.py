"""Tests for run_extraction.py. No network: every answer is invented.

The tests cover the places where an error would silently cost money or
falsify the run record (criterion from D4): resume, stop on the spend
limit, strict parsing, token and cost figures, and the key never
reaching a file.

Work package E, step A8. Research questions FF1 and FF3. Since work
package F also the local model (decision F2): no key, endpoint on this
computer only, context window checked before the first call.
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
        "store": False,
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
cache_write_multiplier = 1.25
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


def factory_from(responses: dict[int, list], expected_key: str | None = FAKE_KEY):
    """A sender that answers per pull number from a list of responses."""
    calls: list[int] = []

    def factory(config, key):
        assert key == expected_key

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


PRICES = {"input_per_million": 2.0, "output_per_million": 12.0,
          "cache_write_multiplier": 1.25}


def test_usage_and_cost():
    usage = run.usage_of(answer(5))
    assert usage == {"input_tokens": 1000, "cached_tokens": 200,
                     "cache_write_tokens": 0,
                     "output_tokens": 300, "reasoning_tokens": 100}
    assert run.cost_upper_bound(usage, PRICES) == pytest.approx(0.0056)


def test_cost_of_the_real_first_call_matches_the_invoice():
    """Token figures of pull 64 from step 7; the invoice showed 0.07 dollars."""
    usage = {"input_tokens": 5402, "cached_tokens": 0, "cache_write_tokens": 5399,
             "output_tokens": 4608, "reasoning_tokens": 2850}
    cost = run.cost_upper_bound(usage, PRICES)
    assert cost == pytest.approx(0.0687995)
    assert round(cost, 2) == 0.07


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
    assert manifest["per_pull"][0]["store_applied"] is False
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


# --- local model, decision F2 ------------------------------------------


LOCAL_CONFIG = (CONFIG
                .replace('endpoint = "https://example.invalid/v1/responses"',
                         'endpoint = "http://127.0.0.1:11434/v1/responses"\n'
                         'api_key_name = ""')
                .replace('model = "gpt-5.6-terra"', 'model = "local-invented"')
                + '[runtime]\nkind = "ollama"\nbase_url = "http://127.0.0.1:11434"\n'
                  'expected_num_ctx = 65536\n')

SNAPSHOT = {"kind": "ollama", "version": "0.0.0-invented", "model": "local-invented",
            "model_digest": "d" * 64, "weights_blob_sha256": "b" * 64,
            "details": {"family": "invented"}, "parameters": "num_ctx 65536",
            "num_ctx": 65536}


@pytest.fixture
def local_project(project, monkeypatch):
    """The invented project with the local configuration and runtime."""
    (project / "config" / "local_run.toml").write_text(LOCAL_CONFIG, encoding="utf-8")

    def no_key(key):
        raise AssertionError("a local run must not read a key")
    monkeypatch.setattr(run, "load_token", no_key)
    monkeypatch.setattr(run, "describe_runtime", lambda config: dict(SNAPSHOT))
    return project


LOCAL_ARGS = ARGS + ["--config", "config/local_run.toml"]


def test_local_config_is_accepted(local_project):
    config = run.load_config(Path("config/local_run.toml"))
    assert run.key_name(config) == ""
    assert config["runtime"]["expected_num_ctx"] == 65536


def test_config_without_key_needs_a_local_endpoint(tmp_path):
    path = tmp_path / "c.toml"
    path.write_text(LOCAL_CONFIG.replace("http://127.0.0.1:11434/v1/responses",
                                         "https://example.invalid/v1/responses"),
                    encoding="utf-8")
    with pytest.raises(ValueError, match="on this computer, decision F2"):
        run.load_config(path)


def test_key_is_only_sent_over_https(tmp_path):
    path = tmp_path / "c.toml"
    path.write_text(CONFIG.replace("https://example.invalid", "http://127.0.0.1:11434"),
                    encoding="utf-8")
    with pytest.raises(ValueError, match="only sent over https"):
        run.load_config(path)


def test_runtime_must_be_local(tmp_path):
    path = tmp_path / "c.toml"
    path.write_text(LOCAL_CONFIG.replace('base_url = "http://127.0.0.1:11434"',
                                         'base_url = "http://192.168.1.5:11434"'),
                    encoding="utf-8")
    with pytest.raises(ValueError, match="base_url must be on this computer"):
        run.load_config(path)


def test_sender_without_key_sends_no_authorization(monkeypatch):
    seen = {}

    def fake_post(url, headers, json, timeout):
        seen.update(headers)
        return FakeResponse(200, {})
    monkeypatch.setattr(run.requests, "post", fake_post)
    config = {"request": {"endpoint": "http://127.0.0.1:1/v1/responses"},
              "transport": {"timeout_seconds": 1}}
    run.make_sender(config, None)({})
    assert "Authorization" not in seen
    run.make_sender(config, FAKE_KEY)({})
    assert seen["Authorization"] == f"Bearer {FAKE_KEY}"


@pytest.mark.parametrize("text, value", [
    ("num_ctx                        65536\ntemperature                    1", 65536),
    ("temperature 1\nnum_ctx 32768", 32768),
    ("temperature 1", None),
    ("num_ctx_extra 5", None),
])
def test_parse_num_ctx(text, value):
    assert run.parse_num_ctx(text) == value


def test_describe_runtime_keeps_checksums_but_not_paths():
    config = {"runtime": {"kind": "ollama", "base_url": "http://127.0.0.1:11434/"},
              "request": {"model": "local-invented"}}
    blob = "e" * 64
    urls = []

    def get(url, timeout):
        urls.append(url)
        if url.endswith("/api/version"):
            return FakeResponse(200, {"version": "0.34.4"})
        return FakeResponse(200, {"models": [
            {"name": "other:latest", "digest": "0" * 64},
            {"name": "local-invented:latest", "digest": "d" * 64}]})

    def post(url, json, timeout):
        urls.append(url)
        assert json == {"model": "local-invented"}
        return FakeResponse(200, {
            "modelfile": f"# comment\nFROM /Users/someone/.ollama/models/blobs/sha256-{blob}\n",
            "parameters": "num_ctx                        65536\ntemperature 1",
            "details": {"family": "gptoss", "quantization_level": "MXFP4"}})
    snapshot = run.describe_runtime(config, get=get, post=post)
    assert snapshot["version"] == "0.34.4"
    assert snapshot["model_digest"] == "d" * 64
    assert snapshot["weights_blob_sha256"] == blob
    assert snapshot["num_ctx"] == 65536
    assert "/Users/" not in json.dumps(snapshot)
    assert urls[0] == "http://127.0.0.1:11434/api/version"


def test_describe_runtime_stops_on_http_error():
    config = {"runtime": {"kind": "ollama", "base_url": "http://127.0.0.1:11434"},
              "request": {"model": "missing"}}
    with pytest.raises(requests.HTTPError):
        run.describe_runtime(config,
                             get=lambda url, timeout: FakeResponse(200, {"version": "x"}),
                             post=lambda url, json, timeout: FakeResponse(404, {}))


def test_local_run_sends_no_key_and_records_the_runtime(local_project):
    factory, calls = factory_from({n: [FakeResponse(200, answer(n))] for n in (5, 7, 9)},
                                  expected_key=None)
    assert run.main(LOCAL_ARGS, sender_factory=factory, sleep=lambda _s: None) == 0
    assert calls == [5, 7, 9]
    out = local_project / "data" / "processed"
    manifest = json.loads((out / "extraction_test_run.manifest.json").read_text())
    assert manifest["runtime"]["snapshots"] == [SNAPSHOT]
    assert manifest["runtime"]["consistent"] is True
    assert manifest["runtime"]["reasoning_tokens_reported"] is True
    assert manifest["counts"]["reached_context_limit"] == []
    assert manifest["per_pull"][0]["reached_context_limit"] is False
    raw = [json.loads(line) for line in
           (out / "extraction_test_run.raw.jsonl").read_text().splitlines()]
    assert all(entry["runtime"] == SNAPSHOT for entry in raw)


def test_api_manifest_has_no_runtime_section(project):
    factory, _calls = factory_from({n: [FakeResponse(200, answer(n))] for n in (5, 7, 9)})
    run.main(ARGS, sender_factory=factory, sleep=lambda _s: None)
    manifest = json.loads((project / "data" / "processed" /
                           "extraction_test_run.manifest.json").read_text())
    assert "runtime" not in manifest
    assert "reached_context_limit" not in manifest["counts"]
    assert "reached_context_limit" not in manifest["per_pull"][0]


def test_wrong_context_window_stops_before_sending(local_project, monkeypatch, capsys):
    monkeypatch.setattr(run, "describe_runtime",
                        lambda config: {**SNAPSHOT, "num_ctx": 32768})
    factory, calls = factory_from({}, expected_key=None)
    assert run.main(LOCAL_ARGS, sender_factory=factory) == 1
    assert calls == []
    assert list((local_project / "data" / "processed").glob("extraction_*")) == []
    assert "expected 65536" in capsys.readouterr().err


def test_unreachable_runtime_stops_before_sending(local_project, monkeypatch):
    def down(config):
        raise requests.ConnectionError("invented")
    monkeypatch.setattr(run, "describe_runtime", down)
    factory, calls = factory_from({}, expected_key=None)
    assert run.main(LOCAL_ARGS, sender_factory=factory) == 1
    assert calls == []


def test_dry_run_does_not_ask_the_runtime(local_project, monkeypatch):
    def forbidden(config):
        raise AssertionError("dry run must not ask the runtime")
    monkeypatch.setattr(run, "describe_runtime", forbidden)
    factory, calls = factory_from({}, expected_key=None)
    assert run.main(LOCAL_ARGS + ["--dry-run"], sender_factory=factory) == 0


def test_full_context_window_is_flagged(local_project):
    big = answer(5)
    big["usage"] = {"input_tokens": 60000, "output_tokens": 5536,
                    "output_tokens_details": {"reasoning_tokens": 0}}
    small = answer(7)
    small["usage"] = {"input_tokens": 100, "output_tokens": 10,
                      "output_tokens_details": {"reasoning_tokens": 0}}
    factory, _calls = factory_from({5: [FakeResponse(200, big)],
                                    7: [FakeResponse(200, small)],
                                    9: [FakeResponse(200, small)]}, expected_key=None)
    run.main(LOCAL_ARGS, sender_factory=factory, sleep=lambda _s: None)
    manifest = json.loads((local_project / "data" / "processed" /
                           "extraction_test_run.manifest.json").read_text())
    assert manifest["counts"]["reached_context_limit"] == [5]
    assert manifest["runtime"]["reasoning_tokens_reported"] is False


def test_runtime_change_during_a_run_is_visible(local_project, monkeypatch):
    factory, _calls = factory_from({5: [FakeResponse(200, answer(5))]}, expected_key=None)
    run.main(LOCAL_ARGS + ["--limit", "1"], sender_factory=factory, sleep=lambda _s: None)
    monkeypatch.setattr(run, "describe_runtime",
                        lambda config: {**SNAPSHOT, "version": "0.0.1-invented"})
    factory, _calls = factory_from({7: [FakeResponse(200, answer(7))],
                                    9: [FakeResponse(200, answer(9))]}, expected_key=None)
    run.main(LOCAL_ARGS, sender_factory=factory, sleep=lambda _s: None)
    manifest = json.loads((local_project / "data" / "processed" /
                           "extraction_test_run.manifest.json").read_text())
    assert manifest["runtime"]["consistent"] is False
    assert [s["version"] for s in manifest["runtime"]["snapshots"]] == [
        "0.0.0-invented", "0.0.1-invented"]


def test_rebuild_with_limit_0_does_not_ask_the_runtime(local_project, monkeypatch):
    factory, _calls = factory_from({n: [FakeResponse(200, answer(n))] for n in (5, 7, 9)},
                                   expected_key=None)
    run.main(LOCAL_ARGS, sender_factory=factory, sleep=lambda _s: None)

    def down(config):
        raise requests.ConnectionError("runtime is off, nothing to send")
    monkeypatch.setattr(run, "describe_runtime", down)
    factory, calls = factory_from({}, expected_key=None)
    assert run.main(LOCAL_ARGS + ["--limit", "0"], sender_factory=factory) == 0
    assert calls == []
