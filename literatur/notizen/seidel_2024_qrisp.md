# Lesenotiz: Seidel et al. 2024, Qrisp

Quelle: Seidel, R.; Bock, S.; Zander, R.; Petric, M.; Steinmann, N.;
Tcholtchev, N.; Hauswirth, M.: Qrisp: A Framework for Compilable
High-Level Programming of Gate-Based Quantum Computers. Preprint,
arXiv:2406.14792v1, 20.06.2024. https://arxiv.org/abs/2406.14792
BibTeX: seidel2024qrisp (thesis.bib). Literaturmatrix: L04.
Gelesen: Volltext v1 am 12.10.2026 von Claude; vom Verfasser noch nicht.

## Inhalt, soweit fuer die Arbeit relevant

- Qrisp ist eine in Python eingebettete Sprache (eDSL) fuer gatterbasierte
  Quantencomputer. Programme werden bis auf Schaltkreisebene uebersetzt
  und laufen damit auf den meisten physischen Backends und Simulatoren
  (Zusammenfassung, Abschn. 1).
- Motivation aus der Softwaretechnik: Programmieren von Quantenrechnern
  gleiche heute dem Programmieren in Assembler; wachsende Komplexitaet
  fuehre zu mehr Fehlern, schlechterer Wartbarkeit und hoeheren Kosten
  (Abschn. 1).
- Drei Entwurfsziele: Schnittstelle ueber mehrere Abstraktionsebenen,
  Compiler fuer hardwarespezifische Uebersetzung hardwareneutralen Codes,
  Lehrwerkzeug (Abschn. 1).
- Fazit der Autoren: Qrisp-Code laesst sich modularisieren; Teilmodule
  lassen sich austauschen, isoliert testen und benchmarken, Fehler
  systematisch beheben und Dokumentation nutzerfreundlich gestalten
  (Abschn. 7).
- Quelltext offen auf GitHub (eclipse-qrisp/Qrisp), Tutorials auf
  qrisp.eu (Abschnitt Code availability).
- Autoren bei Fraunhofer FOKUS, Berlin; Hauswirth zusaetzlich TU Berlin.
  Gefoerdert vom BMWK (Acknowledgement).

## Nicht relevant

Abschn. 2 bis 6 (QuantumVariable, Uncomputation, Kompilierung,
Beispiele wie Shor-Algorithmus, Ausblick zu Jax) betreffen
Quantencomputing und liegen nach der Abgrenzung ausserhalb der Arbeit.

## Einordnung (eigene)

- Die Quelle beschreibt den Untersuchungsgegenstand, nicht seinen
  Entwicklungsprozess. Ueber Anforderungsdokumentation sagt sie nichts.
  Die Aussage, Qrisp sei ohne formale Anforderungen gewachsen, stammt
  deshalb aus dem Expose (Angaben aus dem Projekt), nicht aus dieser
  Quelle.
- Die softwaretechnische Begruendung der Autoren (Wartbarkeit,
  Modularitaet, Testbarkeit) stuetzt die Motivation, Anforderungen
  nachvollziehbar zu dokumentieren; das ist eine eigene Verbindung.
- Preprint, nicht begutachtet.
- Der Betreuer der Arbeit (Nikolay Tcholtchev) ist Mitautor. Fuer
  Abschn. 7.4 der Arbeit ausgewiesen.
