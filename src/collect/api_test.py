"""Verbindungstest zur GitHub-API.

Arbeitspaket D, FF1. Prueft, ob Konfiguration und Token korrekt geladen
werden und ob die API mit dem erwarteten Kontingent antwortet.
Der Token wird nie ausgegeben, nur seine Laenge.
"""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path
from typing import Any

import requests

PROJEKT_WURZEL = Path(__file__).resolve().parents[2]
KONFIG_PFAD = PROJEKT_WURZEL / "config" / "collect.toml"
ENV_PFAD = PROJEKT_WURZEL / ".env"


def lade_konfiguration(pfad: Path) -> dict[str, Any]:
    """Liest die TOML-Konfiguration ein."""
    if not pfad.is_file():
        raise FileNotFoundError(f"Konfigurationsdatei fehlt: {pfad}")
    with pfad.open("rb") as datei:
        return tomllib.load(datei)


def lade_token(pfad: Path, schluessel: str = "GITHUB_TOKEN") -> str:
    """Liest einen Wert aus der .env-Datei."""
    if not pfad.is_file():
        raise FileNotFoundError(f"Datei mit Zugangsdaten fehlt: {pfad}")
    for zeile in pfad.read_text(encoding="utf-8").splitlines():
        zeile = zeile.strip()
        if not zeile or zeile.startswith("#") or "=" not in zeile:
            continue
        name, _, wert = zeile.partition("=")
        if name.strip() == schluessel:
            wert = wert.strip()
            if not wert:
                raise ValueError(f"{schluessel} in {pfad} ist leer.")
            return wert
    raise KeyError(f"{schluessel} nicht in {pfad} gefunden.")


def baue_kopfzeilen(token: str, api_version: str) -> dict[str, str]:
    """Erzeugt die HTTP-Kopfzeilen fuer jede Anfrage an die GitHub-API."""
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": api_version,
    }


def main() -> int:
    konfig = lade_konfiguration(KONFIG_PFAD)
    token = lade_token(ENV_PFAD)
    api_version = konfig["api"]["version"]
    kopfzeilen = baue_kopfzeilen(token, api_version)

    url = f"{konfig['api']['base_url']}/rate_limit"
    antwort = requests.get(
        url,
        headers=kopfzeilen,
        timeout=konfig["abruf"]["timeout_sekunden"],
    )
    antwort.raise_for_status()

    kern = antwort.json()["resources"]["core"]

    print(f"Konfiguration gelesen:   {KONFIG_PFAD}")
    print(f"Token geladen:           {len(token)} Zeichen")
    print(f"API-Version angefordert: {api_version}")
    print(f"API-Version angenommen:  "
          f"{antwort.headers.get('x-github-api-version-selected')}")
    print(f"Statuscode:              {antwort.status_code}")
    print(f"Kontingent:              {kern['remaining']} von {kern['limit']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
