# Bewertungskriterien, Fassung v0

Festgelegt am: 21.09.2026, vor dem ersten kostenpflichtigen Lauf
Grundlage: E2 und Nachtrag zu E2 vom 21.09.2026 in docs/entscheidungen.md.

Diese Fassung legt nur fest, WAS bewertet wird: Name, Definition in
einem Satz, Grundlage und Ebene. Skala, Entscheidungsregeln,
Beispiele und die endgueltige Art der Erhebung folgen vor der ersten
Bewertung (Fassung v1). Sie wurde vor dem ersten kostenpflichtigen Lauf
festgelegt, also bevor der Verfasser Ausgaben des Modells gesehen hat.
Kriterien werden danach nicht mehr ergaenzt oder gestrichen; aendern
duerfen sich nur Skala, Regeln und Beispiele.

Die Kennungen B1 bis B11 sind neu. Sie haben nichts mit den Kriterien
K1 bis K10 der Formatauswahl zu tun.

## Ebene 1: jede einzelne Anforderung

| Nr. | Kriterium | Definition in einem Satz | Grundlage | Erhebung (vorgesehen) |
|---|---|---|---|---|
| B1 | Eindeutigkeit | Der Satz laesst nur eine Lesart zu. | 29148 Abschn. 5.2.5, Unambiguous | von Hand |
| B2 | Vollstaendigkeit des Satzes | Der Satz beschreibt die Faehigkeit oder Eigenschaft so, dass man ihn ohne weitere Angaben versteht. | 29148 Abschn. 5.2.5, Complete | von Hand |
| B3 | Einzelbezogenheit | Der Satz enthaelt genau eine Faehigkeit, Eigenschaft oder Einschraenkung. | 29148 Abschn. 5.2.5, Singular | von Hand |
| B4 | Nachweisbarkeit | Der Satz ist so gefasst, dass sich pruefen laesst, ob Qrisp ihn erfuellt. | 29148 Abschn. 5.2.5, Verifiable | von Hand |
| B5 | Quellentreue | Der Satz behauptet nichts, was die zitierten Stellen des Pull Requests nicht tragen. | Setzung des Verfassers, siehe Anmerkung 1 | von Hand |
| B6 | Relevanz | Der Satz beschreibt eine dauerhafte Faehigkeit oder Eigenschaft von Qrisp und keinen einmaligen Arbeitsschritt. | Setzung des Verfassers | von Hand |
| B7 | Praktische Nutzbarkeit | Der Satz koennte ohne Umformulierung in eine Anforderungsdokumentation von Qrisp uebernommen werden. | Setzung des Verfassers, siehe Anmerkung 3 | von Hand |
| B8 | Formatkonformitaet | Die Ausgabe erfuellt das Schema v2, und der Satz folgt dem angegebenen EARS-Muster. | 29148 Abschn. 5.2.5, Conforming; Zielformat C5 | Schema maschinell, EARS-Muster von Hand |
| B9 | Quellennachvollziehbarkeit | Jede zitierte Stelle steht woertlich im Pull Request, und die Belegstaerke folgt den Regeln von E6. | E6; Pruefung durch validate_output.py | maschinell |
| B10 | Sprachliche Kriterien | Der Satz enthaelt keine der unbestimmten Ausdrucksklassen aus 29148 Abschn. 5.2.7. | 29148 Abschn. 5.2.7 | maschinell, Regeln in v1 |

## Ebene 2: alle Anforderungen eines Pull Requests zusammen

| Nr. | Kriterium | Definition in einem Satz | Grundlage | Erhebung (vorgesehen) |
|---|---|---|---|---|
| B11a | Widerspruchsfreiheit | Die Anforderungen eines Pull Requests widersprechen sich nicht, ueberschneiden sich nicht und verwenden fuer dieselbe Sache dasselbe Wort. | 29148 Abschn. 5.2.6, Consistent | von Hand |
| B11b | Verstaendlichkeit | Aus den Anforderungen eines Pull Requests geht klar hervor, was erwartet wird und welchen Teil von Qrisp es betrifft. | 29148 Abschn. 5.2.6, Comprehensible | von Hand |

## Nicht aufgenommen

| Merkmal | Begruendung |
|---|---|
| Correct, Abschn. 5.2.5 | Verlangt den Bedarf, aus dem die Anforderung hervorging. Er ist nicht dokumentiert (wie in C5). Ersetzt durch B5. |
| Necessary, Feasible, Appropriate, Abschn. 5.2.5 | Wie in C5 begruendet. |
| Complete, Abschn. 5.2.6 | Ein einzelner Pull Request ist keine vollstaendige Spezifikation. Das Merkmal waere immer verfehlt. |
| Feasible und Able to be validated, Abschn. 5.2.6 | Setzen Kosten, Termine und den tatsaechlichen Bedarf voraus. |
| Abdeckung (findet die Pipeline alle Anforderungen eines Pull Requests?) | Braucht eine von Hand erstellte Referenz. Sie liegt nur fuer die zwoelf Faelle aus Paket C vor und wird im Nebenteil von E2 geprueft. |

## Anmerkungen

1. B5 statt "Korrektheit". Die Norm versteht unter Correct die
   zutreffende Wiedergabe des Bedarfs; dieses Merkmal ist nach C5 nicht
   pruefbar. B5 prueft nur die Treue zur zitierten Quelle. B5 und B9
   ergaenzen sich: B9 prueft maschinell, ob die Zitate existieren, B5
   von Hand, ob der Satz ueber sie hinausgeht.
2. Verstaendlichkeit steht auf Ebene 2, weil die Norm sie als Merkmal
   der Menge fuehrt. Auf Ebene 1 ist sie in B1 enthalten; die Norm
   verbindet Unambiguous mit einfacher, leicht verstaendlicher
   Formulierung.
3. B7 ist das schwaechste Kriterium: Der Verfasser bewertet stellvertretend
   fuer das Qrisp-Team. Das gehoert nach Kapitel 7.
4. Art der Erhebung. Die Spalte nennt den Stand vom 21.09.2026 und
   ist vorlaeufig. Der Verfasser moechte die Bewertung von Hand so
   weit wie moeglich durch maschinelle Pruefung ersetzen. Das weicht
   von E2 ab, wonach der Hauptteil eine Selbstbewertung durch den
   Verfasser ist. Ob und wie weit das geschieht, wird vor der ersten
   Bewertung in einer eigenen Entscheidung festgelegt. Fest bleibt
   unabhaengig davon die Liste der Kriterien.
5. Die Zuordnung der Normmerkmale zu den Ebenen und zur Art der Erhebung
   ist eine Einordnung des Verfassers und steht so nicht in der Norm.
