"""Tests for src/extract/cost_report.py with an invented manifest.

The section must take every measured value from the manifest, refuse
to run when a reference wording is missing from its source, and append
to the cost estimate only at the end of section 6.2, never twice.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "extract"))

import cost_report as c  # noqa: E402

ESTIMATE = """# Kosten

## 6. Messwerte

### 6.1 Messwerte

In beiden Laeufen lag die Abrechnung bei 90 bis
91 Prozent der Obergrenze.

### 6.2 Hochrechnung fuer den Volllauf

  Zeichen. Mit 3,81 Zeichen je Token sind das rund 3,96 Mio
  Eingabe-Token.
- Ausgabe: ergibt rund 1,33 Mio Ausgabe-Token.

| Normalbetrieb, ohne Zwischenspeicher | 23,88 $ |

- Der Stapelbetrieb ist noch nicht umgesetzt.
"""
STATUS = "Abrechnung: Gesamtverbrauch\n23,80 US-Dollar, davon vor dem Volllauf 2,40."
DECISIONS = "Geschaetzte Laufzeit 4,8 Stunden, weil"


def per_pull(number, day, inp, out, dur, bound):
    return {"pull_number": number, "started_at": f"2026-09-{day}T10:00:00+00:00",
            "input_tokens": inp, "cached_tokens": inp // 2, "cache_write_tokens": inp // 4,
            "output_tokens": out, "reasoning_tokens": out // 2,
            "duration_seconds": dur, "cost_upper_bound_usd": bound}


def manifest():
    pulls = [per_pull(1, 25, 1000, 300, 10.0, 0.01), per_pull(2, 26, 3000, 500, 30.0, 0.02),
             per_pull(3, 26, 2000, 1000, 20.0, 0.03)]
    tokens = {f: sum(p[f] for p in pulls) for f in c.TOKEN_FIELDS}
    return {"run_id": "2026-09-25_full_v2", "counts": {"completed": 3}, "per_pull": pulls,
            "tokens": tokens, "cost_upper_bound_usd": 0.06,
            "prices_usd_per_million": {"retrieved": "2026-09-21",
                                       "input_per_million": 2.0, "output_per_million": 12.0}}


TEXTS = {"estimate": ESTIMATE, "status": STATUS, "decisions": DECISIONS}


def test_all_references_are_found_across_line_breaks():
    assert c.check_references(TEXTS) == []


@pytest.mark.parametrize("key, old, new", [
    ("estimate", "rund 3,96 Mio", "rund 3,97 Mio"),
    ("estimate", "23,88 $", "23,89 $"),
    ("status", "23,80", "23,90"),
    ("status", "2,40", "2,50"),
    ("decisions", "4,8", "4,9"),
])
def test_a_changed_reference_stops_the_script(key, old, new):
    texts = dict(TEXTS, **{key: TEXTS[key].replace(old, new)})
    assert len(c.check_references(texts)) == 1


def test_measure_takes_totals_and_spreads_from_the_manifest():
    m = c.measure(manifest())
    assert m["input_tokens"] == 6000 and m["output_tokens"] == 1800
    assert m["output_median"] == 500 and m["output_max"] == 1000
    assert m["output_mean"] == 600
    assert m["duration_seconds"] == 60.0 and m["duration_max"] == 30.0
    assert m["normal_usd"] == pytest.approx((6000 * 2 + 1800 * 12) / 1e6)
    assert m["days"] == {"2026-09-25": 1, "2026-09-26": 2}


@pytest.mark.parametrize("field", ["input_tokens", "output_tokens", "cached_tokens"])
def test_measure_stops_when_totals_disagree(field):
    data = manifest()
    data["tokens"][field] += 1
    with pytest.raises(ValueError):
        c.measure(data)


def test_measure_stops_when_the_cost_bound_disagrees():
    data = manifest()
    data["cost_upper_bound_usd"] = 0.07
    with pytest.raises(ValueError):
        c.measure(data)


def test_german_number_format():
    assert c.de(3906903) == "3 906 903"
    assert c.de(3.8221, 2) == "3,82"
    assert c.share(1, 4) == "25,0 %"


def test_section_shows_measured_and_derived_values():
    text = c.section(c.measure(manifest()), "28.09.2026")
    assert "### 6.3 Messwerte des Volllaufs 2026-09-25_full_v2" in text
    assert "| Eingabe-Token | rund 3,96 Mio | 6 000 |" in text
    assert "21,40 $ (23,80 $ minus 2,40 $ vor dem Volllauf)" in text
    assert "1 am 25.09.2026 und 2 am 26.09.2026" in text
    assert "0,0600 $" in text and "unter der Hochrechnung" in text


def test_append_only_at_the_end_and_only_once(tmp_path):
    path = tmp_path / "k.md"
    path.write_text(ESTIMATE, encoding="utf-8")
    c.append_section(path, "\n### 6.3 X\n")
    assert path.read_text(encoding="utf-8") == ESTIMATE + "\n### 6.3 X\n"
    with pytest.raises(ValueError):
        c.append_section(path, "\n### 6.3 X\n")


def test_append_refuses_when_6_2_is_not_last(tmp_path):
    path = tmp_path / "k.md"
    path.write_text(ESTIMATE + "\n## 7. Anderes\n", encoding="utf-8")
    with pytest.raises(ValueError):
        c.append_section(path, "\n### 6.3 X\n")
    assert path.read_text(encoding="utf-8").endswith("## 7. Anderes\n")


def write_files(tmp_path):
    for name, text in [("k.md", ESTIMATE), ("s.md", STATUS), ("d.md", DECISIONS)]:
        (tmp_path / name).write_text(text, encoding="utf-8")
    (tmp_path / "m.json").write_text(json.dumps(manifest()), encoding="utf-8")
    return ["--manifest", str(tmp_path / "m.json"), "--estimate", str(tmp_path / "k.md"),
            "--status", str(tmp_path / "s.md"), "--decisions", str(tmp_path / "d.md")]


def test_main_without_write_changes_nothing(tmp_path, capsys):
    assert c.main(write_files(tmp_path)) == 0
    assert "### 6.3" in capsys.readouterr().out
    assert (tmp_path / "k.md").read_text(encoding="utf-8") == ESTIMATE


def test_main_with_write_appends(tmp_path):
    assert c.main(write_files(tmp_path) + ["--write"]) == 0
    assert (tmp_path / "k.md").read_text(encoding="utf-8").startswith(ESTIMATE + "\n### 6.3")


def test_main_stops_on_a_missing_reference(tmp_path, capsys):
    args = write_files(tmp_path)
    (tmp_path / "s.md").write_text("nothing", encoding="utf-8")
    assert c.main(args + ["--write"]) == 2
    assert (tmp_path / "k.md").read_text(encoding="utf-8") == ESTIMATE
