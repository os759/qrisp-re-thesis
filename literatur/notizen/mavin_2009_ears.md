# Mavin et al. 2009: EARS (Easy Approach to Requirements Syntax)

BibTeX-Key: mavin2009ears
Quellentyp: Konferenzbeitrag (RE'09, IEEE)
Gelesen am: 06.08.2026
Status: gelesen
Bezug zu: FF2 (primaer), FF1 (sekundaer)
Volltext liegt: literatur/volltexte/ (lizenzpflichtig, nicht im Repo)

## 1 Was die Quelle sagt

- Kontext: Regelungssysteme fuer Flugzeugtriebwerke bei Rolls-Royce;
  sicherheitskritisch, hohe Zuliefererzahl (Abschn. 1)
- Acht Probleme unstrukturierter NL-Anforderungen: Mehrdeutigkeit,
  Vagheit, Komplexitaet, Auslassung, Duplikation, Wortreichtum,
  unangemessene Implementierungsvorgabe, Nicht-Testbarkeit (Abschn. 2)
- Ausgeklammert: widerspruechliche Anforderungen, fehlende
  Rueckverfolgbarkeit (Abschn. 2)
- Ablehnung formaler und grafischer Notationen wegen
  Uebersetzungsfehlern, Sprachbarriere, Schulungsaufwand (Abschn. 2)
- Generische Syntax: optionale Vorbedingungen, optionaler Ausloeser,
  Systemname, shall, Systemreaktion; Klauselreihenfolge folgt
  zeitlicher Logik (Abschn. 4.1)
- Fuenf Muster: Ubiquitous, Event-driven (WHEN), Unwanted behaviour
  (IF-THEN), State-driven (WHILE/During), Optional feature (WHERE)
  (Abschn. 4.2-4.6); Kombination zu komplexen Mustern (Abschn. 4.7)
- Muster fuer unerwuenschtes Verhalten ist logisch aequivalent zum
  ereignisgetriebenen, erhaelt aber eigene Syntax zur
  Wiedererkennbarkeit; Verweis auf Misuse Cases (Abschn. 4.4, Fussnote)
- Fallstudie an EASA CS-E 50: 36 Rohanforderungen -> 47 EARS-
  Anforderungen; Wortzahl je Anforderung 36,9 -> 25,6 (Tabelle 2)
- Bei fuenf von acht Kriterien keine Probleme mehr; Mehrdeutigkeit,
  Vagheit, Wortreichtum reduziert, nicht beseitigt (Abschn. 5, 6)
- Autoren relativieren die Beseitigung von Auslassungen selbst
  (Abschn. 6)

## 2 Kernbegriffe und Definitionen

| Begriff | Definition laut Quelle | Fundstelle |
|---|---|---|
| Ubiquitous requirement | ohne Vorbedingung und Ausloeser, dauerhaft aktiv | 4.2 |
| Event-driven requirement | ausgeloest durch Ereignis an der Systemgrenze | 4.3 |
| Unwanted behaviour | alle unerwuenschten Situationen: Ausfaelle, Stoerungen, unerwartetes Verhalten interagierender Systeme | 4.4 |
| State-driven requirement | aktiv, solange ein definierter Zustand besteht | 4.5 |
| Optional feature requirement | nur gueltig, wenn ein Merkmal im System enthalten ist | 4.6 |

## 3 Woertliche Zitate

Keine. Der Inhalt ist vollstaendig paraphrasierbar.

## 4 Art der Evidenz

Einzelfallstudie in einem Unternehmen. Stichprobe: 36 Anforderungen
aus einem Abschnitt eines Zulassungsdokuments. Messverfahren:
Auszaehlen von Problemvorkommen vor und nach der Umformulierung,
Bewertung durch die Autoren selbst. Kein unabhaengiges Rating, keine
Reliabilitaetspruefung.

## 5 Meine Einordnung

- EARS belegt Ebene (b) des Vier-Ebenen-Modells: Satz- und
  Syntaxmuster, keine Qualitaetsmerkmale, keine Modalitaetsstufen
- EARS verwendet ausschliesslich shall und stuetzt damit 29148
  Abschn. 5.2.7 gegen die RFC-2119-Konvention
- Gehoert nach Abschnitt 2.2.2; Konsequenzen fuer die Pipeline in
  Kapitel 4
- Verhaeltnis zu 29148: komplementaer, nicht konkurrierend

## 6 Meine Schlussfolgerungen

- Die Schluesselwortverankerung erlaubt eine regelbasierte Pruefung
  der Formatkonformitaet und damit ein objektives Vergleichsmass
  fuer FF3
- Die Slotstruktur laesst sich auf ein JSON-Schema abbilden; das
  Modell fuellt Felder, der Satz wird programmatisch erzeugt
- Ernsthafte Einschraenkung: EARS ist fuer hochrangige Stakeholder-
  Anforderungen validiert, PR-Inhalte liegen auf Implementierungsebene

## 7 Einschraenkungen und Kritik

- Stichprobe 36 Anforderungen, nur hochrangig und sicherheitsbezogen
- Vagheitseinstufung nach Angabe der Autoren ermessensabhaengig
- Kein Anspruch auf universelle Anwendbarkeit
- Ein Unternehmen, eine Domaene; externe Validitaet begrenzt

## 8 Offene Punkte und zu pruefen

- [ ] Titelvariante klaeren: Papierkopf nennt "EARS (Easy Approach to
      Requirements Syntax)", die Datenbank "Easy Approach to
      Requirements Syntax (EARS)"
- [ ] Wie wird der Abstraktionsebenen-Unterschied in der
      Entscheidungsmatrix als Kriterium abgebildet?

## 9 Anschlussliteratur

Rueckwaerts: Sindre/Opdahl Misuse Cases (Ref. 21); Hooks "Writing Good
Requirements" (Ref. 12); Wiegers "Writing Good Requirements" (Ref. 13);
Attempto Controlled English (Ref. 17)
Vorwaerts: Mavin/Wilkinson 2010 (Big EARS); Wilkinson/Mavin 2018;
noch zu recherchieren: LLM-Arbeiten, die EARS erzeugen
