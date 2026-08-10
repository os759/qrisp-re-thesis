# Lucassen et al. 2016: Improving agile requirements (QUS framework)

BibTeX-Key: lucassen2016qus
Quellentyp: Zeitschriftenartikel, begutachtet (Requirements Engineering)
Gelesen am: 10.08.2026
Status: gelesen
Bezug zu: FF2 (primaer), FF1, FF3, Evaluation
Volltext liegt: literatur/pdf/ (Open Access, CC BY 4.0 - darf ins Repo)

## 1 Was die Quelle sagt

- Verbreitete Schablone, auf Cohn zurueckgefuehrt: As a <type of user>,
  I want <goal>, [so that <some reason>] (Abschn. 1)
- Eine User Story besteht aus drei Bestandteilen: Text, Gespraeche
  zwischen Beteiligten, Akzeptanzkriterien (Abschn. 1)
- Ueber 80 syntaktische Varianten der Schablone existieren (Abschn. 2)
- Begriffsmodell: eine Rolle, ein Means, null oder mehr Ends, ein
  Format (Abschn. 2, Abb. 1)
- Means besteht aus Subjekt mit Absicht, Handlungsverb, direktem
  Objekt; optional indirektes Objekt und Adjektiv (Abschn. 2.3)
- Drei Varianten wohlgeformter Ends: Klaerung des Means, Abhaengigkeit
  von anderer Funktionalitaet, Qualitaetsanforderung (Abschn. 2.4)
- QUS: 13 Kriterien in Lindlands Kategorien syntaktisch, semantisch,
  pragmatisch; Zuordnung zu einzelner Story oder Menge (Abschn. 3,
  Tabelle 1)
- Fuer die Mengenkriterien werden formale Praedikate angegeben
  (Abschn. 3.2)
- AQUSA: Werkzeug in Python/Flask, nutzt Stanford CoreNLP und NLTK;
  zerlegt den Text an Signalwoertern (Abschn. 4, 4.2)
- Perfect Recall Condition nach Berry et al.: moeglichst alle Maengel
  finden, notfalls auf Kosten der Genauigkeit (Abschn. 4)
- Version 1 deckt nur syntaktische und einige pragmatische Kriterien
  ab; semantische bleiben ausgeklammert (Abschn. 4)
- Auswertung an 1023 User Stories aus 18 Datensaetzen (Abschn. 5)
- Gesamt: makro 92,1 % Trefferquote / 77,4 % Genauigkeit;
  mikro 93,8 % / 72,2 % (Tabelle 4)
- Je Kriterium (Tabelle 5): Well-formed 95,7/42,3; Atomic 82,9/51,2;
  Minimal 95,5/69,5; Uniform 95,4/87,1; Unique 100/100
- Im Mittel wies gut die Haelfte der Stories mindestens einen Mangel
  auf (Abschn. 5.1)
- Erwartung fuer Version 2: 97,9 % / 84,8 % (Abschn. 6.7)

## 2 Kernbegriffe und Definitionen

| Begriff | Definition laut Quelle | Fundstelle |
|---|---|---|
| Role | Stakeholder oder Persona, der den Bedarf aeussert | 2.2 |
| Means | das vom System Erwartete | 2.3 |
| End | Begruendung fuer das Means | 2.4 |
| Well-formed | enthaelt mindestens Rolle und Means | Tab. 1 |
| Atomic | genau ein Merkmal je Story | Tab. 1 |
| Minimal | nichts ausser Rolle, Means, Ends | Tab. 1 |
| Perfect Recall Condition | Werkzeug soll nahezu alle Maengel finden | 4 |

## 3 Woertliche Zitate

Keine.

## 4 Art der Evidenz

Mehrfallstudie. 1023 User Stories aus 18 Datensaetzen, ueberwiegend
unabhaengige Softwareanbieter mit Sitz in den Niederlanden. Bewertung
durch studentische Gruppen, nachgeprueft durch einen unabhaengigen
Assistenten nach festgelegtem Protokoll. Quantitative Auswertung von
Trefferquote und Genauigkeit je Kriterium.

## 5 Meine Einordnung

- Bestaetigt Ebene (a): User Story ist eine Perspektive, kein
  Satzmuster fuer beliebige Systemanforderungen
- Strukturelle Parallele zu 29148: Trennung Einzelanforderung /
  Anforderungsmenge, unabhaengig bestaetigt
- Die Quelle zitiert 29148 in der Ausgabe 2011, nicht 2018
- Gehoert nach 2.2.3; Konsequenzen nach Kapitel 4

## 6 Meine Schlussfolgerungen

- Schwerster Einwand fuer diese Arbeit: Well-formed verlangt zwingend
  eine Rolle. PR-Daten sind entwicklerzentriert und nennen den
  Nutznießer meist nicht. Die Rolle muesste erfunden werden, was der
  Belegstaerke-Systematik widerspricht.
- Aus PR-Daten ist nur ein Teil der drei Bestandteile gewinnbar;
  Akzeptanzkriterien im agilen Sinn fehlen.
- Die AQUSA-Werte sind ein publizierter Referenzmassstab fuer die
  Leistungsfaehigkeit automatischer Formatpruefung und damit fuer FF3
  verwertbar.
- Die Arbeitsteilung Werkzeug/Mensch ist mit dieser Quelle belegbar
  und nicht bloss praktisch begruendet.
- Die Grenze bei semantischen Kriterien wird auch fuer den eigenen
  Formatpruefer gelten und ist vorab zu benennen.

## 7 Einschraenkungen und Kritik

- Auswahlverzerrung: ueberwiegend niederlaendische Softwareanbieter
- Untersucherverzerrung durch Auslegungsspielraum der Kriterien
- Version 1 deckt die semantischen Kriterien nicht ab
- Genauigkeit bei Well-formed und Atomic unter 55 Prozent

## 8 Offene Punkte und zu pruefen

- [ ] INVEST wird hier als Independent-Negotiable-Valuable-
      Estimatable-Scalable-Testable aufgeloest. Nach meiner Kenntnis
      steht das S urspruenglich fuer Small. Gegen Wake 2003 pruefen,
      falls INVEST verwendet wird.
- [ ] Ausgabenunterschied 29148:2011 gegenueber 29148:2018 beim
      Verknuepfen beider Quellen beachten

## 9 Anschlussliteratur

Rueckwaerts: Wake 2003 (INVEST, frei im Web); Cohn 2004 (Buch);
Wautelet et al. 2014 (Vereinheitlichung von User-Story-Modellen);
Berry et al. 2012 (dumb tools); Femmer et al. 2014
(requirements smells gegen ISO 29148)
Vorwaerts: Lucassen et al. 2015 (RE'15, Vorlaeuferarbeit);
Dalpiaz et al. 2019 (terminologische Mehrdeutigkeit)