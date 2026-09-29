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

## 6. Messwerte der Pilotlaeufe und Hochrechnung

Stand 24.09.2026, Paket E, Schritt A8, Teilschritt 11. Token und
Obergrenzen stammen aus den Manifesten unter data/processed/, die
Abrechnung aus dem OpenAI-Konto, abgelesen vom Verfasser. Die
Abschnitte 1 bis 5 bleiben als Stand vom 19.09.2026 stehen, damit die
Abweichung zwischen Schaetzung und Messung sichtbar bleibt.

### 6.1 Messwerte

| Groesse | 2026-09-22_pilot (Prompt v1) | 2026-09-24_pilot_v2 (Prompt v2) |
|---|---|---|
| Vorgaenge | 20 | 20 |
| Eingabe-Token | 209 263 | 211 023 |
| davon aus dem Zwischenspeicher gelesen | 68 526 | 74 005 |
| davon in den Zwischenspeicher geschrieben | 140 677 | 136 958 |
| Ausgabe-Token | 73 137 | 66 970 |
| davon Denk-Token | 45 702 | 38 818 |
| Ausgabe-Token je Vorgang, Mittel | 3 657 | 3 348 |
| Kostenobergrenze laut Programm | 1,3665 $ | 1,2942 $ |
| Abrechnung im Konto | 1,24 $ | 1,16 $ |

Die Abrechnung fuer v2 ist die Differenz der Kontosumme von 2,40 $ und
der Summe fuer v1. Berichtigt am 24.09.2026: Die erste Fassung nannte
eine Kontosumme von 2,37 $ und fuer v2 1,13 $. Der Verfasser hat 2,40 $
als richtige Kontosumme abgelesen. Der Probeaufruf zu PR 64 vom
22.09.2026 ist einer der 20 Vorgaenge des ersten Laufs und kein
zusaetzlicher Aufruf. In beiden Laeufen lag die Abrechnung bei 90 bis
91 Prozent der Obergrenze.

Zeichen je Token, gemessen am Lauf v2: 3,81 (211 023 Token auf 803 897
Zeichen laut Probelauf ohne Senden). Der Rechenwert in Abschnitt 1 war
3,5; die Annahme lag auf der sicheren Seite. Die Ausgabe je Vorgang lag
in beiden Laeufen innerhalb der angenommenen 2 000 bis 4 000 Token.

### 6.2 Hochrechnung fuer den Volllauf mit Prompt v2 im Stapelbetrieb

Rechenweg:

- Eingabe: 8 533 169 Zeichen der Quellbloecke plus 395 mal (16 363
  Zeichen Systemanweisung v2 und 183 Zeichen Nutzervorlage), zusammen
  15 068 839 Zeichen. Mit 3,81 Zeichen je Token sind das rund 3,96 Mio
  Eingabe-Token.
- Ausgabe: Mittel je Schicht aus dem Lauf v2, gewichtet mit der Groesse
  der Schicht in der Grundgesamtheit (docs/sample_pilot_a8.md); fuer die
  12 vor der Ziehung ausgeschlossenen Vorgaenge das Gesamtmittel. Das
  ergibt rund 1,33 Mio Ausgabe-Token. Die Gewichtung ist noetig, weil
  die Pilotstichprobe grosse Diffs (S5) ueberproportional enthaelt.
- Preise vom 21.09.2026 laut config/api_run.toml: 2,00 US-Dollar je
  Mio Eingabe-Token, 12,00 je Mio Ausgabe-Token. Der Stapelbetrieb
  halbiert beide Preise (Recherche vom 19.09.2026, Abschnitt 2). Vor dem
  Volllauf erneut zu pruefen.

| Rechnung | Betrag |
|---|---|
| Normalbetrieb, ohne Zwischenspeicher | 23,88 $ |
| Stapelbetrieb, ohne Zwischenspeicher | 11,94 $ |
| Stapelbetrieb, Obergrenze mit Aufschlag 1,25 auf die ganze Eingabe | 12,93 $ |
| dieselbe Obergrenze mit 19 % Umsatzsteuer | 15,39 $ |

Die Hochrechnung liegt innerhalb der Schaetzung aus Abschnitt 3 (9,07
bis 13,87 $ im Stapelbetrieb, ohne Steuer). Das Budget aus E3 von 150
Euro bleibt weit unterschritten.

Grenzen der Hochrechnung:

- Ob der Zwischenspeicher im Stapelbetrieb wirkt und ob dort der
  Aufschlag fuer das Schreiben anfaellt, ist nicht recherchiert. Die
  Obergrenze rechnet den Aufschlag auf die ganze Eingabe und liegt damit
  auf der sicheren Seite.
- Die Ausgabe schwankt zwischen Laeufen (Mittel 3 657 gegen 3 348 Token).
  Zwei Laeufe ergeben keine belastbare Streuung.
- Die Gewichtung nach Schichten beruht auf 1 bis 5 Vorgaengen je Schicht.
- Der Stapelbetrieb ist im Aufrufprogramm noch nicht umgesetzt.

### 6.3 Messwerte des Volllaufs 2026-09-25_full_v2

Stand 28.09.2026, Paket E. Token, Laufzeit und Kostenobergrenze stammen
aus data/processed/extraction_2026-09-25_full_v2.manifest.json,
berechnet von src/extract/cost_report.py. Die Abrechnung hat der
Verfasser am 26.09.2026 im OpenAI-Konto abgelesen (STATUS.md,
Abschnitt Aktuell). Preise laut Manifest vom 21.09.2026.

Der Volllauf lief im Normalbetrieb, nicht im Stapelbetrieb (Nachtrag
zu E8 vom 24.09.2026). Verglichen wird deshalb mit der Zeile
"Normalbetrieb, ohne Zwischenspeicher" aus 6.2, nicht mit den
Stapelpreisen. Gesendet wurden 395 Vorgaenge, 5 am 25.09.2026 und 390 am 26.09.2026.

| Groesse | Hochrechnung 6.2 | gemessen |
|---|---|---|
| Vorgaenge | 395 | 395, davon 395 vollstaendig |
| Eingabe-Token | rund 3,96 Mio | 3 906 903 |
| davon aus dem Zwischenspeicher gelesen | nicht eingerechnet | 1 530 735 (39,2 %) |
| davon in den Zwischenspeicher geschrieben | nicht eingerechnet | 2 374 983 |
| Ausgabe-Token | rund 1,33 Mio | 1 262 525 |
| davon Denk-Token | nicht geschaetzt | 727 673 (57,6 %) |
| Ausgabe-Token je Vorgang, Mittel / Median / Hoechstwert | - | 3 196 / 3 336 / 7 654 |
| Normalpreis ohne Zwischenspeicher, rechnerisch | 23,88 $ | 22,96 $ |
| Kostenobergrenze laut Programm | - | 24,1516 $ |
| Abrechnung im Konto | - | 21,40 $ (23,80 $ minus 2,40 $ vor dem Volllauf) |
| Laufzeit, Summe duration_seconds | 4,8 h (Nachtrag zu E8) | 3,82 h (13 759 s) |
| Laufzeit je Vorgang, Mittel / Hoechstwert | - | 34,8 s / 85,5 s |

Die Eingabe lag 1,3 Prozent unter der Hochrechnung, die Ausgabe
5,1 Prozent unter ihr. Die Abrechnung lag bei 88,6 Prozent
der Obergrenze, in den Pilotlaeufen bei 90 bis 91 Prozent (6.1). Der
Gesamtverbrauch des Kontos von 23,80 US-Dollar unterschreitet das Budget
aus E3 von 150 Euro weit.

Grenzen der Messwerte:

- Die Abrechnung ist die Differenz zweier Ablesungen des Kontos. Sie
  gilt fuer den Volllauf nur, wenn zwischen beiden Ablesungen kein
  anderer Aufruf lief. Ob sie Umsatzsteuer enthaelt, ist nicht geprueft.
- Die Laufzeit ist die Summe der Antwortzeiten. Pausen zwischen den
  Aufrufen und die Zeit zwischen beiden Sendetagen sind nicht enthalten.
- Die Zeichen je Token sind fuer den Volllauf nicht neu gemessen.
- Ein einzelner Volllauf ergibt keine Streuung zwischen Laeufen.
