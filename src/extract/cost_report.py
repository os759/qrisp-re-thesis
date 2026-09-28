"""Write section 6.3 of experiments/kostenschaetzung.md from the run manifest.

Every measured value comes from the manifest of the full run. The
projection of section 6.2, the billing read by the author and the
runtime estimate of the addendum to E8 are not typed anew: the script
holds them as constants and stops unless each one stands, in exactly
this wording, in its source file. So a value in section 6.3 can only
differ from its source if the source itself changes.

Without --write the section is printed for reading. With --write it is
appended to the cost estimate, but only if section 6.2 is the last
section and no section 6.3 exists yet. Nothing else in the file changes.

Work package E, step A8, sub-step 11, full run. Research question FF3
(cost and effort).

Run from the project root:

    python src/extract/cost_report.py \\
      --manifest data/processed/extraction_2026-09-25_full_v2.manifest.json \\
      --estimate experiments/kostenschaetzung.md \\
      --status STATUS.md --decisions docs/entscheidungen.md [--write]
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path
from typing import Any

# Reference values with the wording that must occur in their source.
# (value, file key, wording after whitespace is collapsed)
REFERENCES: dict[str, tuple[float, str, str]] = {
    "input_projected_million": (3.96, "estimate", "rund 3,96 Mio Eingabe-Token"),
    "output_projected_million": (1.33, "estimate", "rund 1,33 Mio Ausgabe-Token"),
    "normal_projected_usd": (23.88, "estimate", "| Normalbetrieb, ohne Zwischenspeicher | 23,88 $ |"),
    # wording only; the text of 6.3 repeats it, no number is computed from it
    "pilot_billing_share": (0.0, "estimate", "lag die Abrechnung bei 90 bis 91 Prozent der Obergrenze"),
    "billed_total_usd": (23.80, "status", "Gesamtverbrauch 23,80 US-Dollar"),
    "billed_before_usd": (2.40, "status", "davon vor dem Volllauf 2,40"),
    "runtime_estimate_hours": (4.8, "decisions", "Geschaetzte Laufzeit 4,8 Stunden"),
}
SECTION_62 = "### 6.2 Hochrechnung"
SECTION_63 = "### 6.3"
TOKEN_FIELDS = ("input_tokens", "cached_tokens", "cache_write_tokens",
                "output_tokens", "reasoning_tokens")


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check_references(texts: dict[str, str]) -> list[str]:
    """Wording of every reference value that is missing from its source."""
    return [f"{name}: '{wording}' not found in {key}"
            for name, (_, key, wording) in REFERENCES.items()
            if wording not in collapse(texts[key])]


def measure(manifest: dict[str, Any]) -> dict[str, Any]:
    """Totals and spreads from the manifest; totals are checked against per_pull."""
    per_pull = manifest["per_pull"]
    for field in TOKEN_FIELDS:
        total = sum(p[field] for p in per_pull)
        if total != manifest["tokens"][field]:
            raise ValueError(f"{field}: per_pull sums to {total}, "
                             f"tokens says {manifest['tokens'][field]}")
    bound = sum(p["cost_upper_bound_usd"] for p in per_pull)
    if abs(bound - manifest["cost_upper_bound_usd"]) > 0.0001:
        raise ValueError(f"cost upper bound: per_pull sums to {bound:.4f}, "
                         f"manifest says {manifest['cost_upper_bound_usd']}")
    outputs = [p["output_tokens"] for p in per_pull]
    durations = [p["duration_seconds"] for p in per_pull]
    prices = manifest["prices_usd_per_million"]
    tokens = manifest["tokens"]
    days: dict[str, int] = {}
    for p in per_pull:
        days[p["started_at"][:10]] = days.get(p["started_at"][:10], 0) + 1
    return {
        "run_id": manifest["run_id"],
        "pulls": len(per_pull),
        "completed": manifest["counts"]["completed"],
        **tokens,
        "output_mean": statistics.mean(outputs),
        "output_median": statistics.median(outputs),
        "output_max": max(outputs),
        "normal_usd": (tokens["input_tokens"] * prices["input_per_million"]
                       + tokens["output_tokens"] * prices["output_per_million"]) / 1e6,
        "bound_usd": manifest["cost_upper_bound_usd"],
        "prices_retrieved": prices["retrieved"],
        "duration_seconds": sum(durations),
        "duration_mean": statistics.mean(durations),
        "duration_max": max(durations),
        "days": dict(sorted(days.items())),
    }


def de(value: float, digits: int = 0) -> str:
    """German number format: 1 234 567 or 3,82."""
    text = f"{value:,.{digits}f}".replace(",", " ").replace(".", ",")
    return text


def share(part: float, whole: float) -> str:
    return de(100 * part / whole, 1) + " %"


def section(m: dict[str, Any], today: str) -> str:
    ref = {name: value for name, (value, _, _) in REFERENCES.items()}
    billed = ref["billed_total_usd"] - ref["billed_before_usd"]
    hours = m["duration_seconds"] / 3600
    input_dev = 100 * (m["input_tokens"] / 1e6 - ref["input_projected_million"]) \
        / ref["input_projected_million"]
    output_dev = 100 * (m["output_tokens"] / 1e6 - ref["output_projected_million"]) \
        / ref["output_projected_million"]
    days = " und ".join(f"{n} am {d[8:10]}.{d[5:7]}.{d[:4]}" for d, n in m["days"].items())
    rows = [
        ("Vorgaenge", "395", f"{m['pulls']}, davon {m['completed']} vollstaendig"),
        ("Eingabe-Token", "rund 3,96 Mio", de(m["input_tokens"])),
        ("davon aus dem Zwischenspeicher gelesen", "nicht eingerechnet",
         f"{de(m['cached_tokens'])} ({share(m['cached_tokens'], m['input_tokens'])})"),
        ("davon in den Zwischenspeicher geschrieben", "nicht eingerechnet",
         de(m["cache_write_tokens"])),
        ("Ausgabe-Token", "rund 1,33 Mio", de(m["output_tokens"])),
        ("davon Denk-Token", "nicht geschaetzt",
         f"{de(m['reasoning_tokens'])} ({share(m['reasoning_tokens'], m['output_tokens'])})"),
        ("Ausgabe-Token je Vorgang, Mittel / Median / Hoechstwert", "-",
         f"{de(m['output_mean'])} / {de(m['output_median'])} / {de(m['output_max'])}"),
        ("Normalpreis ohne Zwischenspeicher, rechnerisch",
         de(ref["normal_projected_usd"], 2) + " $", de(m["normal_usd"], 2) + " $"),
        ("Kostenobergrenze laut Programm", "-", de(m["bound_usd"], 4) + " $"),
        ("Abrechnung im Konto", "-",
         f"{de(billed, 2)} $ ({de(ref['billed_total_usd'], 2)} $ minus "
         f"{de(ref['billed_before_usd'], 2)} $ vor dem Volllauf)"),
        ("Laufzeit, Summe duration_seconds", "4,8 h (Nachtrag zu E8)",
         f"{de(hours, 2)} h ({de(m['duration_seconds'])} s)"),
        ("Laufzeit je Vorgang, Mittel / Hoechstwert", "-",
         f"{de(m['duration_mean'], 1)} s / {de(m['duration_max'], 1)} s"),
    ]
    table = ["| Groesse | Hochrechnung 6.2 | gemessen |", "|---|---|---|"]
    table += [f"| {a} | {b} | {c} |" for a, b, c in rows]
    return "\n".join([
        "",
        f"### 6.3 Messwerte des Volllaufs {m['run_id']}",
        "",
        f"Stand {today}, Paket E. Token, Laufzeit und Kostenobergrenze stammen",
        f"aus data/processed/extraction_{m['run_id']}.manifest.json,",
        "berechnet von src/extract/cost_report.py. Die Abrechnung hat der",
        "Verfasser am 26.09.2026 im OpenAI-Konto abgelesen (STATUS.md,",
        "Abschnitt Aktuell). Preise laut Manifest vom "
        f"{m['prices_retrieved'][8:10]}.{m['prices_retrieved'][5:7]}.{m['prices_retrieved'][:4]}.",
        "",
        "Der Volllauf lief im Normalbetrieb, nicht im Stapelbetrieb (Nachtrag",
        "zu E8 vom 24.09.2026). Verglichen wird deshalb mit der Zeile",
        "\"Normalbetrieb, ohne Zwischenspeicher\" aus 6.2, nicht mit den",
        f"Stapelpreisen. Gesendet wurden {m['pulls']} Vorgaenge, {days}.",
        "",
        *table,
        "",
        f"Die Eingabe lag {de(abs(input_dev), 1)} Prozent "
        f"{'unter' if input_dev < 0 else 'ueber'} der Hochrechnung, die Ausgabe",
        f"{de(abs(output_dev), 1)} Prozent {'unter' if output_dev < 0 else 'ueber'} ihr. "
        f"Die Abrechnung lag bei {de(100 * billed / m['bound_usd'], 1)} Prozent",
        "der Obergrenze, in den Pilotlaeufen bei 90 bis 91 Prozent (6.1). Der",
        f"Gesamtverbrauch des Kontos von {de(ref['billed_total_usd'], 2)} US-Dollar "
        "unterschreitet das Budget",
        "aus E3 von 150 Euro weit.",
        "",
        "Grenzen der Messwerte:",
        "",
        "- Die Abrechnung ist die Differenz zweier Ablesungen des Kontos. Sie",
        "  gilt fuer den Volllauf nur, wenn zwischen beiden Ablesungen kein",
        "  anderer Aufruf lief. Ob sie Umsatzsteuer enthaelt, ist nicht geprueft.",
        "- Die Laufzeit ist die Summe der Antwortzeiten. Pausen zwischen den",
        "  Aufrufen und die Zeit zwischen beiden Sendetagen sind nicht enthalten.",
        "- Die Zeichen je Token sind fuer den Volllauf nicht neu gemessen.",
        "- Ein einzelner Volllauf ergibt keine Streuung zwischen Laeufen.",
        "",
    ])


def append_section(path: Path, text: str) -> None:
    content = path.read_text(encoding="utf-8")
    if SECTION_63 in content:
        raise ValueError(f"{path} already has a section 6.3; nothing written.")
    if content.count(SECTION_62) != 1:
        raise ValueError(f"{path}: section 6.2 not found exactly once; nothing written.")
    if "\n### " in content[content.index(SECTION_62) + len(SECTION_62):] \
            or "\n## " in content[content.index(SECTION_62):]:
        raise ValueError(f"{path}: section 6.2 is not the last section; nothing written.")
    if not content.endswith("\n"):
        raise ValueError(f"{path} does not end with a line break; nothing written.")
    path.write_text(content + text, encoding="utf-8")


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Section 6.3 from the run manifest.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--estimate", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--decisions", required=True)
    parser.add_argument("--today", default="28.09.2026")
    parser.add_argument("--write", action="store_true",
                        help="Append the section to --estimate.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    texts = {"estimate": Path(arguments.estimate).read_text(encoding="utf-8"),
             "status": Path(arguments.status).read_text(encoding="utf-8"),
             "decisions": Path(arguments.decisions).read_text(encoding="utf-8")}
    missing = check_references(texts)
    if missing:
        for problem in missing:
            print(f"ERROR {problem}")
        return 2
    manifest = json.loads(Path(arguments.manifest).read_text(encoding="utf-8"))
    text = section(measure(manifest), arguments.today)
    if not arguments.write:
        print(text)
        return 0
    append_section(Path(arguments.estimate), text)
    print(f"Section 6.3 appended to {arguments.estimate}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
