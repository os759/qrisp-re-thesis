# Konfiguration

- `collect.toml` Erhebung ueber die GitHub-API
- `model_input.toml` Aufbau der Modelleingabe
- `api_run.toml` Laeufe ueber die OpenAI-API
- `anthropic_run.toml` Lauf ueber die Anthropic-API (E12)
- `local_run.toml`, `local_run_qwen.toml` lokale Laeufe ueber Ollama
- `ollama/` Modelfiles der lokalen Modelle mit erweitertem Kontext
- `requirement_schema_v1.json`, `requirement_schema_v2.json` JSON-Schema
  der Modellausgabe

Die Dateien enthalten keine Zugangsdaten. Zugangstoken gehoeren
ausschliesslich in `.env` bzw. Umgebungsvariablen; `.env` und
`config/config.yaml` sind ueber `.gitignore` ausgeschlossen.
