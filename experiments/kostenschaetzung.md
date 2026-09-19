# Kostenschaetzung fuer die API-Laeufe

Erstellt am 19.09.2026. Paket E, Schritt A7. Grundlage der Entscheidung E8.
Pflicht aus E3: Die Schaetzung liegt vor dem ersten kostenpflichtigen Lauf
vor. Alle Preise sind am 19.09.2026 recherchiert und veralten schnell.

## 1. Umfang der Eingabe

Gemessen an data/processed/model_input_2026-09-19.jsonl, Manifest im selben
Ordner.

| Groesse | Wert |
|---|---|
| Quellbloecke | 395 |
| Zeichen in den Bloecken | 8 533 169 |
| laengster Block | 79 841 Zeichen |
| Systemanweisung, je Aufruf erneut | 16 042 Zeichen |
| Nutzervorlage, je Aufruf | 183 Zeichen |
| Zeichen gesamt, ein vollstaendiger Lauf | 14 942 044 |

Umrechnung in Token: Ein Token ist die Abrechnungseinheit des Anbieters.
Die Umrechnung ist eine Schaetzung, kein Messwert. Das Zaehlwerkzeug des
Anbieters wurde nicht verwendet.

| Annahme | Eingabe-Token |
|---|---|
| 3,0 Zeichen je Token | 4,98 Mio |
| 3,5 Zeichen je Token (Rechenwert) | 4,27 Mio |
| 4,0 Zeichen je Token | 3,74 Mio |

Davon entfallen 1,83 Mio Token auf die Systemanweisung, weil sie bei jedem
der 395 Aufrufe erneut gesendet wird. Das sind 43 Prozent der Eingabe.

Ausgabe: angenommen 2 000 bis 4 000 Token je Vorgang, also 0,8 bis 1,6 Mio
insgesamt. Denk-Token ("reasoning tokens") zaehlen als Ausgabe und sind in
dieser Spanne enthalten, aber nicht gemessen. Der Pilotlauf nach A8 ersetzt
die Annahme durch einen Messwert.

## 2. Preise am 19.09.2026

US-Dollar je 1 Mio Token, Eingabe / Ausgabe.

| Modell | Eingabe | Ausgabe |
|---|---|---|
| gpt-5.6-sol | 4,00 | 20,00 |
| gpt-5.6-terra | 2,00 | 12,00 |
| gpt-5.6-luna | 0,20 | 1,20 |
| claude-sonnet-5 | 2,00 | 10,00 |
| claude-haiku-4.5 | 1,00 | 5,00 |

Quelle: Modellseite von OpenAI, abgerufen am 19.09.2026, und die
Preisuebersicht von Anthropic, ebenfalls am 19.09.2026. Die genauen
Fundstellen stehen in docs/entscheidungen.md, E8.

Vorbehalt zu gpt-5.6-sol, berichtigt am 19.09.2026: Der Preis von 4,00 /
20,00 ist ein Aktionspreis. Die Preisseite von OpenAI nennt ihn als
mindestens bis zum 21.11.2026 gueltig, ohne Enddatum und ohne einen Preis
fuer die Zeit danach. Mehrere Uebersichten fuehren weiterhin 5,00 / 30,00;
diese Angabe ist veraltet. Der erste Entwurf dieser Schaetzung enthielt
denselben Fehler. Folgenlos fuer die Wahl, weil Sol nicht genommen wird,
aber ein Beleg dafuer, dass jede Preisangabe in der Arbeit ein Abrufdatum
braucht.

Zwei weitere Angaben der Preisseite, hier ohne Wirkung: Ab etwa 272 000
Eingabe-Token je Anfrage gilt ein hoeherer Preis fuer die ganze Anfrage.
Der laengste Quellblock liegt bei rund 23 000 Token, also weit darunter.
Zwischengespeicherte Eingabe wird mit einem Bruchteil berechnet.

Rabatte, bei beiden Anbietern verfuegbar:
- Stapelverarbeitung halbiert Eingabe- und Ausgabepreis. Die Antwort kommt
  verzoegert, was hier nicht stoert.
- Ein Zwischenspeicher fuer wiederholte Anfangsteile senkt den Preis der
  Systemanweisung deutlich. Hier nicht eingerechnet, wirkt also zugunsten
  des Budgets.

## 3. Kosten eines vollstaendigen Laufs

Ein Lauf heisst: alle 395 Vorgaenge einmal. Gerechnet mit 4,27 Mio
Eingabe-Token und 0,8 bis 1,6 Mio Ausgabe-Token, ohne Zwischenspeicher.

| Modell | Normalpreis | Stapel | Stapel mit 19 % Umsatzsteuer |
|---|---|---|---|
| gpt-5.6-terra | 18,14 – 27,74 $ | 9,07 – 13,87 $ | 10,79 – 16,51 $ |
| gpt-5.6-luna | 1,81 – 2,77 $ | 0,91 – 1,39 $ | 1,08 – 1,65 $ |
| gpt-5.6-sol | 33,08 – 49,08 $ | 16,54 – 24,54 $ | 19,68 – 29,20 $ |

Der Steuersatz ist nicht recherchiert; 19 Prozent sind ein vorsichtiger
Aufschlag. Der Wechselkurs ist ebenfalls nicht recherchiert. Die Rechnung
setzt 1 Euro gleich 1 US-Dollar. Das liegt auf der sicheren Seite, solange
der Euro nicht unter Parikurs faellt.

## 4. Geplanter Verbrauch bis zum Abschluss von Paket E und F

| Posten | Umfang | Modell | Schaetzung |
|---|---|---|---|
| Pilot A8 | 20 Vorgaenge, normal | terra | ca. 1,40 $ |
| Prompt-Ueberarbeitung | dreimal 20 Vorgaenge | terra | ca. 4,20 $ |
| Volllauf | 395 Vorgaenge, Stapel | terra | 9 – 14 $ |
| Wiederholungen fuer die Konsistenz | dreimal 40 Vorgaenge, Stapel | terra | ca. 4,20 $ |
| Reserve fuer Fehllaeufe | ein halber Volllauf | terra | ca. 7 $ |
| Summe, ohne Steuer | | | 26 – 31 $ |
| Summe, mit 19 % | | | 31 – 37 $ |

Das Budget aus E3 betraegt 150 Euro. Die Planung schoepft davon rund ein
Viertel aus. Geld ist damit nicht der begrenzende Faktor; die Wahl des
Modells richtet sich nach der Ergebnisqualitaet.

## 5. Was diese Schaetzung nicht leistet

- Die Token-Umrechnung ist geschaetzt. Abweichung bis etwa 17 Prozent nach
  oben moeglich.
- Der Umfang der Denk-Token ist unbekannt. Er kann die Ausgabe und damit
  den teureren Teil der Rechnung vergroessern.
- Fehlgeschlagene Aufrufe, Zeitueberschreitungen und Wiederholungen sind
  nur pauschal als Reserve enthalten.
- Preise, Steuer und Wechselkurs koennen sich aendern. Der Aktionspreis
  fuer gpt-5.6-sol laeuft fruehestens am 21.11.2026 aus.

Nach dem Pilotlauf A8 wird dieser Abschnitt durch Messwerte ersetzt:
tatsaechliche Eingabe- und Ausgabe-Token je Vorgang, tatsaechliche Kosten
laut Abrechnung, und daraus eine neue Hochrechnung fuer den Volllauf.
