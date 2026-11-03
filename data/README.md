# Daten

- `raw/` unveraenderte API-Antworten. NICHT versioniert.
- `interim/` Zwischenstaende der Aufbereitung. NICHT versioniert.
- `processed/` aufbereiteter Korpus, Modelleingaben und Extraktionen.
  Versioniert sind nur die Manifeste (`*.manifest.json`), siehe
  `.gitignore`.
- `manifests/` je Erhebungsschritt eine Manifestdatei mit
  Erhebungszeitpunkt, Umfang und Pruefsumme. Versioniert.
