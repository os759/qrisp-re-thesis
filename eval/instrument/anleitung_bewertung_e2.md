# Anleitung: Bewertung nach E2, Kriterienliste v1

Stand: 08.10.2026. Diese Anleitung enthaelt keine neue Notenregel. Sie
bringt eval/instrument/kriterien_v1.md in eine Form zum Arbeiten. Bei
einem Widerspruch gilt kriterien_v1.md. Teil 6 nennt, wie das Programm
die maschinellen Pruefregeln liest, wo der Wortlaut von v1 eine Frage
offenlaesst.

Ablage: eval/instrument/anleitung_bewertung_e2.md
Programm: src/analyze/evaluate_requirements.py

## Teil 1: Ablauf

Alle Befehle aus dem Repository-Stamm, mit aktivierter Umgebung
(source .venv/bin/activate). Arbeitsordner:
eval/responses/evaluation_e2_2026-10-08/ (von git ignoriert).

1. Bogen erzeugen (einmal), Befehl sheet. Ergebnis: sheet.md (der
   Bogen), answers.txt (deine Antworten), sheet_manifest.json
   (Reihenfolge und Pruefsummen). Diese drei Dateien nie von Hand
   loeschen.
2. sheet.md, answers.txt und kriterien_v1.md nebeneinander oeffnen.
   Eintrag 1 im Bogen gehoert zur ersten R-Zeile in answers.txt. Nach
   den Anforderungen eines Pull Requests folgt im Bogen sein Block
   "Ebene 2" und in answers.txt seine P-Zeile.
3. Je Anforderung B1 bis B7 in dieser Reihenfolge (A4), je Pull
   Request B11a und B11b. Zwischendurch speichern. Pausen sind
   jederzeit moeglich.
4. Zwischenpruefung, beliebig oft: Befehl compare. Solange etwas fehlt,
   nennt er nur Zeilennummern mit Problemen und schreibt nichts.
5. Sind alle Zeilen fertig, laeuft compare durch und sperrt
   answers.txt (A7). Ab jetzt answers.txt NICHT mehr aendern, auch
   nicht die Notizen.
6. Erst jetzt: Befehl n2-sheet. Er schreibt n2_sheet.md und
   n2_answers.txt fuer den Nebenteil (Teil 5).
7. Befehl result. Er schreibt
   experiments/evaluation_e2_2026-10-08.json mit Zahlen und Kennungen.

In den Chat gehen nur Zahlen, Kennungen wie QR-0064-01 und
Pull-Request-Nummern. Kein Satz, keine Notiz, kein Zitat.

## Teil 2: Zeilen in answers.txt

Anforderung:

    R | 7 | QR-0123-02 | 2 | 1 | 2 | 1 | 2 | 2 | 1 | Notiz

Felder: R | Nummer | Kennung | B1 | B2 | B3 | B4 | B5 | B6 | B7 | Notiz

Pull Request:

    P | 123 | 2 | 1 | Notiz

Felder: P | PR | B11a | B11b | Notiz

- R, Nummer, Kennung, P und PR stehen schon da. Nicht aendern.
- Werte: 2, 1, 0 oder ?. Kein anderes Zeichen.
- ? heisst nicht beurteilbar. Dann ist die Notiz Pflicht: warum.
- B11a mit - hat das Programm gesetzt, weil der Pull Request genau eine
  Anforderung hat. Nicht aendern.
- Notiz: freier Text ohne das Zeichen |.

## Teil 3: Allgemeine Regeln (kriterien_v1.md, Abschnitt 3)

- A1 Grundlage ist nur der Bogen. Den Link oeffnest du nur, um ein
  Zitat zu verstehen.
- A2 shall ist eine Konvention der Arbeit, kein Mangel und kein Beleg.
- A3 Jedes Kriterium nur nach seiner eigenen Frage.
- A4 Reihenfolge B1 bis B7, B7 zuletzt.
- A5 Namen von Teilen von Qrisp gelten als bestimmt.
- A6 Im Zweifel die niedrigere Note; im Zweifel, ob beurteilbar, ?.
- A7 Nach compare keine Aenderung mehr.

## Teil 4: Die Fragen je Kriterium

Die Noten 2, 1 und 0 mit ihren Beispielen stehen in kriterien_v1.md,
Abschnitte 5 und 7. Hier nur die Fragen zum schnellen Nachschlagen:

| Kriterium | Frage | Grundlage |
|---|---|---|
| B1 Eindeutigkeit | Laesst der Satz nur eine Lesart zu? | Satz |
| B2 Vollstaendigkeit | Versteht man den Satz ohne weitere Angaben? | Satz |
| B3 Einzelbezogenheit | Enthaelt der Satz genau eine Faehigkeit, Eigenschaft oder Einschraenkung? | Satz |
| B4 Nachweisbarkeit | Laesst sich pruefen, ob Qrisp den Satz erfuellt? | Satz |
| B5 Quellentreue | Behauptet der Satz etwas, das die gezeigten Zitate nicht tragen? | Satz und Zitate |
| B6 Relevanz | Dauerhafte Faehigkeit oder Eigenschaft statt einmaliger Arbeitsschritt? | Satz |
| B7 Praktische Nutzbarkeit | Ohne Umformulierung in eine Anforderungsdokumentation uebernehmbar? | Satz |
| B11a Widerspruchsfreiheit | Widersprechen oder ueberschneiden sich die Anforderungen, oder benennen sie dieselbe Sache verschieden? | alle Saetze des Pull Requests |
| B11b Verstaendlichkeit | Geht klar hervor, was erwartet wird und welchen Teil von Qrisp es betrifft? | alle Saetze des Pull Requests |

Achtung bei B5: Die Note 2 heisst "von den Zitaten getragen", also
gerade kein Mangel. Die Frage ist verneinend gestellt.

B8, B9 und B10 bewertest du nicht. Das Programm prueft sie und zeigt
sie erst im Ergebnis.

## Teil 5: Nebenteil N2 (nach der Sperre)

n2_sheet.md zeigt je Zeile der Datei fundstellen_paket_c.csv deine
Fundstelle aus der Formulierungsprobe und alle gefundenen Belege der
Pipeline in diesem Pull Request, die denselben Bestandteil tragen.

Frage: Gibt mindestens einer dieser Belege die Stelle wieder, die die
Formulierungsprobe nennt? Antwort in n2_answers.txt: ja, nein oder ?.

    3 | 191 | system_name | ja | Notiz

N2 ist nicht verblindet; du kennst deine eigenen Fundstellen. Das ist
in kriterien_v1.md, Abschnitt 8, so vorgesehen.

## Teil 6: Wie das Programm die maschinellen Regeln liest

Diese Lesarten stehen im Programm und in seinen Tests. Sie sind vor der
ersten Bewertung committet. Sie aendern keine Regel aus v1, sondern
legen fest, was v1 nicht ausdruecklich sagt.

1. Erstes Wort (B8.2): die erste Folge von Buchstaben im Satz.
2. Teil vor shall (B8.2, B8.3): der Text vor dem ersten Wort shall,
   ohne Beachtung der Gross- und Kleinschreibung. Hat der Satz kein
   Wort shall, gibt es keinen Teil vor shall; B8.3 und die Muster
   unwanted_behaviour und complex in B8.2 bestehen dann nicht. B8.4
   besteht in diesem Fall ohnehin nicht, das Gesamturteil B8 aendert
   sich also nicht.
3. B8.3: system_name muss als Zeichenfolge im Teil vor shall stehen,
   nicht als ganzes Wort.
4. Wortgrenzen (B8, B10): Ein Wort ist abgegrenzt, wenn davor und
   danach kein Buchstabe und keine Ziffer steht. Ein Unterstrich, ein
   Apostroph und ein Bindestrich sind daher Grenzen: all_items und
   it's sind Treffer.
5. B9 vergleicht die angegebene Belegstaerke mit der aus allen Belegen
   berechneten, auch den nicht gefundenen (derive_evidence_strength wie
   bei M2).
6. N1: Ortsart comment umfasst issue_comment und review_comment, wie in
   v1 Abschnitt 8.
7. N2: Auch ohne passenden Beleg setzt das Programm keine Antwort; du
   traegst sie selbst ein.
8. Explorativ: and zaehlt als ganzes Wort im Text nach dem ersten
   shall; shall not und shall be able to als ganze Wendungen, ohne
   Beachtung der Gross- und Kleinschreibung.
9. Anteile werden auf vier Nachkommastellen gerundet.
