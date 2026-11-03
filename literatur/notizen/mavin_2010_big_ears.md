# Mavin & Wilkinson 2010: BIG EARS

BibTeX-Key: mavin2010bigears
Quellentyp: Konferenzbeitrag (RE'10, IEEE)
Gelesen am: 06.08.2026
Status: gelesen
Bezug zu: FF2 (primaer), FF1 (Verfahren), Evaluation (Kriterien)
Volltext liegt: literatur/volltexte/ (lizenzpflichtig, nicht im Repo)

## 1 Was die Quelle sagt

- Ziel: die 2009 benannten Grenzen adressieren, breitere Erprobung
- Drei Dokumentmengen: gesamtes CS-E (166 Seiten, 78.187 Woerter,
  192 anforderungshaltige Abschnitte); GSSRD mit 267
  Anforderungssaetzen; 418 Sicherheitsanforderungen eines Programms
- Verfahren: Rohtext in Tabelle, Einstufung jeder Aussage als
  Anforderung / Ueberschrift / Information / nicht anwendbar,
  Umformulierung durch fachuebergreifende Gruppe, Auftrennung
  zusammengesetzter Anforderungen, Iteration, Validierung durch
  Zulassungsexperten, Nachschaerfung der Muster
- Operationalisierung der acht Probleme, u. a. Komplexitaet bei zwei
  oder mehr verbundenen Anforderungen, drei oder mehr Vorbedingungen
  oder zwei oder mehr Ausloesern; Mehrdeutigkeit nach lexikalisch,
  referenziell, syntaktisch
- Ergebnis: Beseitigung der aufgetretenen Probleme bei rund 99 Prozent
  der Anforderungen in den groesseren Fallstudien
- Verbleibend: Untestbarkeit durch unquantifizierte Woerter;
  Komplexitaet aus Matrizen und langen Bedingungslisten; Vagheit,
  wo die Rohfassung Rueckfragen erfordert haette
- Lessons Learned: Wahrheitstabellen; CRUD-Vollstaendigkeitspruefung
  an sichtbaren Funktionen; Abgrenzungsproblem ubiquitous gegen
  event-driven; passive und aktive Anforderungen; Paarbildung von
  Anforderungen; Identifikation von Akteuren; Rueckverfolgbarkeit
  ueber Vorbedingung, Ausloeser, Systemreaktion
- Future Work: kein Muster fuer unerwuenschte Zustaende; Kritik am
  IF-THEN-Muster; moegliche Erweiterung auf Softwareanforderungen

## 2 Kernbegriffe und Definitionen

| Begriff | Definition laut Quelle | Fundstelle |
|---|---|---|
| Passive requirement | System soll gegen eine Stoerung immun sein | Lessons Learned |
| Active requirement | System muss aktiv handeln, um sich zu schuetzen | Lessons Learned |
| Pairing | logisch zusammengehoerige Anforderungen, z. B. gewuenschtes und unerwuenschtes Verhalten | Lessons Learned |
| Evident function | fuer den Nutzer sichtbare Funktion, im Gegensatz zu verborgenen internen Funktionen | Lessons Learned, Fussnote 4 |

## 3 Woertliche Zitate

Keine.

## 4 Art der Evidenz

Drei Fallstudien in einem Unternehmen, deutlich groesserer Umfang als
2009. Auszaehlung von Problemvorkommen vor und nach Umformulierung.
Bewertung durch die Autoren; Schwellenwerte teilweise selbst und nach
eigener Angabe subjektiv festgelegt. Validierung der Umformulierungen
durch einen internen Experten, nicht der Bewertung.

## 5 Meine Einordnung

- Wichtigste Quelle fuer das Verfahren, nicht nur fuer das Format
- Der zweistufige Ablauf (erst einstufen, dann umformulieren) ist das
  Vorbild fuer das Prompt-Design in Kapitel 4
- Die operationalisierten acht Probleme sind Kandidaten fuer den
  Bewertungsbogen der Evaluation (Woche 8)
- Gehoert nach 2.2.2 (Abschnitt 3 und 4) sowie nach Kapitel 4

## 6 Meine Schlussfolgerungen

- Die von den Autoren genannte Erweiterungsrichtung auf
  Softwareanforderungen legitimiert die Anwendung auf PR-Daten als
  begruendeten Schritt, belegt sie aber nicht
- Die 99-Prozent-Angabe ist eine Selbstbewertung und darf nicht als
  Wirksamkeitsnachweis zitiert werden
- Passive/aktive Anforderungen und Paarbildung erklaeren, warum eine
  einzelne PR haeufig nur einen Teil einer Anforderung hergibt; das
  stuetzt die dreistufige Belegstaerke-Klassifikation

## 7 Einschraenkungen und Kritik

- Ein Unternehmen, eine Domaene
- Umformulierung durch eine fachuebergreifende Ingenieursgruppe (Abschnitt
  Method); die Komplexitaetsschwelle legten die Autoren fest (Fussnote 3).
  Berichtigt am 25.10.2026: Dass Bewertende und Umformulierende dieselbe
  Personengruppe sind, steht so nicht im Volltext.
- Schwellenwerte teilweise subjektiv
- Kein Muster fuer unerwuenschte Zustaende

## 8 Offene Punkte und zu pruefen

- [ ] Xplore fuehrt den Titel mit "Requirements Engineering",
      das Papier mit "Requirements Syntax" - im BibTeX vermerkt
- [ ] Welche der acht Probleme sind an PR-abgeleiteten Anforderungen
      ueberhaupt messbar?

## 9 Anschlussliteratur

Rueckwaerts: Firesmith "Are Your Requirements Complete?";
Gause/Weinberg "Exploring Requirements"
Vorwaerts: Wilkinson/Mavin 2018; EARS-Workshop 2018 insgesamt
