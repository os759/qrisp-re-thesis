# Anleitung: Pruefung der Klassifikation von Hand (G4, G5)

Stand: 05.10.2026. Diese Anleitung enthaelt keine neue Regel. Sie
bringt G4 (Massstab) und G5 (Pruefplan) aus docs/entscheidungen.md in
eine Form zum Arbeiten. Bei einem Widerspruch gilt der Text von G4 und
G5.

Ablage: eval/instrument/anleitung_klassifikation_g5.md

## Teil 1: Ablauf

Alle Befehle aus dem Repository-Stamm, mit aktivierter Umgebung
(source .venv/bin/activate). Arbeitsordner:
eval/responses/classification_check_2026-10-06/ (von git ignoriert).

1. Bogen erzeugen (einmal). Ergebnis: sheet.md (der Bogen),
   answers.txt (deine Antworten), sheet_manifest.json (Reihenfolge und
   Pruefsummen). Diese drei Dateien nie von Hand loeschen.
2. sheet.md und answers.txt nebeneinander oeffnen. Eintrag 1 im Bogen
   gehoert zu Zeile 1 in answers.txt, und so weiter.
3. Je Eintrag: lesen, entscheiden, eine Zeile in answers.txt
   ausfuellen (Teil 2 bis 4). Zwischendurch speichern. Pausen sind
   jederzeit moeglich.
4. Zwischenpruefung, beliebig oft: der Befehl compare. Solange etwas
   fehlt, nennt er nur Zeilennummern mit Problemen und schreibt nichts.
5. Sind alle Zeilen fertig, laeuft compare durch. Ab jetzt answers.txt
   NICHT mehr aendern. compare hat ihre Pruefsumme gespeichert.
6. compare nennt die Abweichungen beim Sicherheitsbezug und schreibt
   follow_up.txt. Dort fuellst du nur die letzte Spalte aus (Teil 5).
7. Befehl result. Er schreibt
   experiments/classification_check_2026-10-06.json mit Zahlen.
8. Dependabot-Sichtung (Teil 6), unabhaengig von 1 bis 7.

In den Chat gehen nur Zahlen, Kennungen wie QR-0064-01 und
Pull-Request-Nummern. Kein Satz, keine Begruendung, kein Zitat.

## Teil 2: Eine Zeile in answers.txt

    7 | QR-0123-02 | I | nein |  | TY1 | Notiz

Felder: Nummer | Kennung | Typ | Sicherheit | Zweck | Regel | Notiz

- Nummer und Kennung: stehen schon da, nicht aendern.
- Typ: ein Buchstabe, siehe Teil 3.
- Sicherheit: ja, nein oder unklar, siehe Teil 4.
- Zweck: nur bei ja: 1, 2 oder 3. Bei nein und unklar leer lassen.
- Regel: leer, oder die Regel, die du angewandt hast, zum Beispiel GF1
  oder TY1. Mehrere mit Komma: GF4,TY2.
- Notiz: freier Text, ohne das Zeichen |. Kann leer bleiben.

Grundlage ist nur, was im Bogen steht: Anforderungssatz, Rationale,
Zitate (G4 Grenzfallregel 6). Den Link oeffnest du nur, um ein Zitat
zu verstehen. Du ergaenzt keinen Sicherheitszweck aus eigenem Wissen.

## Teil 3: Typ (G4 Teil 3)

Massstab ist der Wortlaut des Prompts (prompts/extraction_system_v2.md),
den auch das Modell bekommen hat:

| Code | Typwert | Wortlaut im Prompt |
|---|---|---|
| F | functional_performance | a function or task the software performs, including how well it performs it |
| I | interface | how the software interacts with external systems, or how its own parts interact with each other, including its programming interface |
| P | process | a requirement on how the software is developed, tested, documented or released, for example a contribution rule |
| Q | quality_non_functional | a quality property such as portability, reliability, maintainability or security |
| U | usability_quality_in_use | how well users can achieve their goals with the software, for example how efficiently or how satisfied |
| H | human_factors | required results of the interaction with human users beyond achieving their goals, for example how reliably people can use the software without mistakes, or effects on their health or well-being |

Typregeln fuer Grenzfaelle:

| Code | Wann | Entscheidung |
|---|---|---|
| TY1 | I oder F? | I, wenn der Satz festlegt, wie etwas aufgerufen, uebergeben oder verbunden wird (Name, Parameter, Rueckgabe, Datenformat, Zusammenspiel mit fremden Bibliotheken, Diensten oder Teilen von Qrisp). F, wenn er festlegt, was Qrisp berechnet oder bewirkt. Trifft beides zu: Was legt der shall-Teil fest, die Form des Zusammenspiels (I) oder das Ergebnis (F)? |
| TY2 | P? | P, wenn die Anforderung Entwicklung, Tests, Dokumentation oder Veroeffentlichung betrifft und nicht das Verhalten der ausgelieferten Software. |
| TY3 | Q oder F bei Leistung? | Die Leistung einer bestimmten Funktion ist F, nicht Q. |
| TY4 | U oder H? | Passen beide, U. |

## Teil 4: Sicherheit (G4 Teil 2)

Frage: Laesst der Bogen erkennen, dass die Anforderung einem dieser
Zwecke dient?

| Zweck | Inhalt |
|---|---|
| 1 | Schutz von Qrisp, seinem Repository, seinen ausgelieferten Paketen oder der von Qrisp verarbeiteten Daten vor zufaelligem oder boeswilligem Zugriff, Gebrauch, Veraenderung, Zerstoerung oder Offenlegung |
| 2 | Umgang mit nicht vertrauenswuerdigen Eingaben (Daten, die der aufrufende Code nicht selbst erzeugt: Dateien, Netzwerkantworten, Antworten fremder Dienste, serialisierte Objekte), soweit ein Schaden nach Zweck 1 abgewendet werden soll |
| 3 | Beheben, Melden oder Veroeffentlichen von Schwachstellen in Qrisp oder in seinen Abhaengigkeiten |

- ja: mindestens ein Zweck ist erkennbar. Trage den Zweck ein; bei
  mehreren den, der am deutlichsten erkennbar ist, und die anderen in
  die Notiz.
- nein: kein Zweck erkennbar.
- unklar: du kannst es aus dem Bogen nicht entscheiden. Kurz in die
  Notiz schreiben, warum.

Grenzfallregeln:

| Code | Fall | Urteil |
|---|---|---|
| GF1 | Pruefung von Aufrufparametern (Typ, Wertebereich, Form) | nein, ausser Zweck 2 |
| GF2 | Fehlerbehandlung, Absturzfreiheit, Wiederherstellung | nein, ausser der Ausfall laesst sich durch Eingaben nach Zweck 2 herbeifuehren |
| GF3 | Version einer Abhaengigkeit anheben oder festlegen | nur ja, wenn die Quelle eine Schwachstelle oder einen Sicherheitsgrund nennt |
| GF4 | allgemeine Entwicklungspraxis: Tests, Begutachtung, Lizenzen, Versionsnummern, Aenderungsprotokoll, Bauanleitung, Beitragsregeln | nein, ausser die Quelle nennt einen Sicherheitszweck |
| GF5 | Zugangsdaten fuer fremde Dienste (Schluessel, Token) | ja, Zweck 1 |
| GF6 | Sicherheitszweck nur aus eigenem Wissen erschlossen | nicht ergaenzen |
| GF7 | nicht entscheidbar | unklar |

Hinweis zum Wort token: Es kann ein Zugangstoken meinen (GF5) oder
etwas ganz anderes, etwa ein Element beim Zerlegen von Text. Entscheide
nach dem Bogen, nicht nach dem Wort.

Typ und Sicherheit sind unabhaengig: Eine Anforderung kann zum Beispiel
I und zugleich sicherheitsrelevant sein.

## Teil 5: follow_up.txt (nach compare)

Jetzt siehst du zum ersten Mal, was das Modell gesagt hat. Die Zeile
zeigt das Modell und dein Urteil. Du traegst nur ein, ob die
Abweichung an der neuen Definition liegt (G4, Abweichungen 1 bis 4):

| Wert | Bedeutung |
|---|---|
| 1 | Du hast ja gesagt, weil es um zufaellige Einwirkung oder um Offenlegung geht. Beides stand nicht in der Definition, die das Modell hatte. |
| 2 | Du hast ja gesagt, weil es um Repository oder ausgelieferte Pakete geht. |
| 3 | Das Modell hat ja gesagt, du nein, weil es nur um Ausfall ohne fremde Eingabe geht (GF2). |
| 4 | Die Abweichung liegt an der genaueren Fassung von nicht vertrauenswuerdigen Eingaben, etwa reine Parameterpruefung (GF1). |
| keine | Die Abweichung liegt an keinem dieser vier Punkte. |

Dein Urteil aus answers.txt aenderst du dabei nicht.

## Teil 6: Dependabot (G5 Punkt 7)

1. Befehl dependabot-sheet. Er nennt die Zahl der 25 Beitraege je
   Klasse: id (CVE- oder GHSA- im Text, zaehlt automatisch als
   Hinweis), word (nur secur oder vulnerab), none.
2. Nur die Klasse word steht im Bogen dependabot_sheet.md. Je Beitrag:
   Nennt der Text eine Schwachstelle, die diese Aktualisierung behebt?
   Antwort in dependabot_answers.txt: ja, nein oder unklar.
3. Befehl dependabot-result. Er schreibt
   experiments/dependabot_check_2026-10-06.json.
