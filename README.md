# LLM-gestützte Rekonstruktion von Softwareanforderungen aus der Entwicklungshistorie

Bachelorarbeit im Studiengang Angewandte Informatik, Hochschule RheinMain.
Fallstudie: Eclipse Qrisp (Repository `eclipse-qrisp/Qrisp`).

## Status

In Bearbeitung. Abgabetermin: 01.11.2026.

## Forschungsfragen

- **FF1** Inwieweit lassen sich aus der Pull-Request-Historie eines Open-Source-Projekts mithilfe von Large Language Models brauchbare, formal formulierte Softwareanforderungen rekonstruieren?
- **FF2** Welches Anforderungsformat eignet sich für die automatisierte Extraktion, und anhand welcher Kriterien ist diese Wahl zu begründen?
- **FF3** Welche Unterschiede zeigen sich zwischen API-basierten und lokal betriebenen Open-Source-Modellen hinsichtlich Qualität, Kosten und Datenkontrolle?
- **FF4** Welche von einer BSI- bzw. Common-Criteria-orientierten Prüfung erwarteten Sicherheitsanforderungen lassen sich aus der Entwicklungshistorie rekonstruieren, und wo bestehen Dokumentationslücken?

## Ausführungsumgebung

Stand der Erhebung: 31.07.2026

- Hardware: MacBook Pro, Apple M3 Pro, 36 GB Unified Memory
- Betriebssystem: macOS 26.5.2 (Build 25F84)
- Python 3.14.6
- Git 2.50.1 (Apple Git-155)

## Hinweise

Rohdaten, Zugangsdaten, Modellgewichte und Evaluationsrückmeldungen sind
bewusst nicht versioniert. Die Ausschlussregeln stehen in `.gitignore`.

Der Datensatz wird mit Erhebungszeitpunkt und Umfang in `data/MANIFEST.md`
dokumentiert.
