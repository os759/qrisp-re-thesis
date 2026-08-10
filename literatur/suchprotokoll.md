# Suchprotokoll

Zweck: Die Literaturrecherche muss im Methodenteil reproduzierbar sein.
Jede durchgefuehrte Suche wird hier mit einer Zeile dokumentiert.

## Ein- und Ausschlusskriterien

Eingeschlossen: 2019-2026 bei LLM-Themen, ohne Zeitgrenze bei
RE-Grundlagen und Standards; englisch oder deutsch; Volltext
zugaenglich; begutachtet oder methodisch nachvollziehbarer Preprint.

Ausgeschlossen: Anbieter- und Werbebeitraege; Arbeiten zu Training oder
Fine-Tuning ohne Prompting-Bezug (durch Abgrenzung ausgeschlossen);
Quantencomputing-Fachbeitraege ohne Software-Engineering-Bezug;
Arbeiten ohne beschriebene Methodik.

## Verfuegbare Zugaenge (geprueft am 05.08.2026)

- ACM Digital Library Premium (HLB-Lizenz)
- IEEE/IET Electronic Library IEL (HLB-Lizenz)
- Springer Nature Link (HLB-Lizenz)
- arXiv (frei)
- Common Criteria Portal (frei)
- RFC Editor (frei)

## Phase 1: Vorabpruefung der im Exposé genannten Quellen

Zweck dieser Phase war nicht die systematische Suche, sondern die
Pruefung, ob die im Exposé genannten Quellen tatsaechlich existieren
und korrekt angegeben sind. Durchgefuehrt als gezielte Titelsuche im
offenen Web, nicht als Datenbankrecherche. Die systematische Suche in
ACM, IEEE und Springer steht noch aus (Phase 2).

| Datum | Portal | Suchstring | Filter | Treffer | gescreent | aufgenommen | Bemerkung |
|---|---|---|---|----|----|---|---|
| 05.08.2026 | IEEE Xplore | 29148 | - | -  | -  | 1 | ISO/IEC/IEEE 29148:2018 als Volltext bezogen (L07) |
| 05.08.2026 | Web, gezielt | Arora Grundy Abdelrazek generative AI requirements engineering | - | -  | -  | 1 | arXiv:2310.13976 bestaetigt; zusaetzlich begutachtete Fassung als Springer-Buchkapitel gefunden (L02) |
| 05.08.2026 | Web, gezielt | Qrisp compilable high-level programming gate-based quantum computers | - | -  | -  | 1 | arXiv:2406.14792 bestaetigt (L04). Nebenbefund: Betreuer ist Mitautor |
| 05.08.2026 | Web, gezielt | Vogelsang Fischbach large language models NLP requirements engineering | - | -  | -  | 1 | arXiv:2402.13823 bestaetigt; erschienen im Handbook on NLP for RE, Springer 2025 (L03) |
| 05.08.2026 | Web, gezielt | large language models requirements engineering systematic literature review | - | -  | -  | 3 | Zadenoori et al. SLR arXiv:2509.11446 (L01); zusaetzlich zwei Arbeiten zu Open-Source-Modellen im RE, relevant fuer FF3 (L12, L13) |
| 05.08.2026 | Web, gezielt | OWASP Top 10 for LLM Applications aktuelle Version | - | -  | -  | 0 | Sekundaerquellen widersprechen sich zur Versionsbezeichnung. Primaerquelle noch zu pruefen (L10) |
| 05.08.2026 | Web, gezielt | Common Criteria CC:2022 ISO/IEC 15408:2022 | - | -  | -  | 1 | CC:2022 Rev. 1 frei ueber CC-Portal; ISO-Fassung kostenpflichtig (L08) |
| 06.08.2026 | RFC Editor | RFC 2119 | - | -  | -  | 1 | Volltext gelesen (L06) |
| 06.08.2026 | RFC Editor | RFC 8174 | - | -  | -  | 1 | Aktualisiert RFC 2119. Beide bilden BCP 14 (L11) |
| 06.08.2026 | IEEE Xplore (HLB) | 10.1109/RE.2009.9 | keine, DOI-Direktzugriff | 1 | 1  | 1 | Direktbeschaffung der EARS-Primaerquelle ueber DOI-Resolver (L05). |
| 06.08.2026 | IEEE Xplore (HLB) | "Easy Approach to Requirements Syntax" | Feld: Document Title | <Trefferzahl> | -  | 2 | Vorwaertssuche nach Folgearbeiten. Aufgenommen: Wilkinson/Mavin 2018 (L15) und Mavin/Wilkinson 2010 (L14). Titelabweichung bei L14: Xplore fuehrt "Requirements Engineering", das Papier selbst "Requirements Syntax". |
| 10.08.2026 | Springer Nature Link | 10.1007/s00766-016-0250-x | keine, DOI-Direktzugriff | 1 | 1 | 1 | Beschaffung der Primaerquelle zu User Stories und deren Qualitaetskriterien (FF2, Ebene Darstellungsperspektive). Open Access, CC BY 4.0 - PDF darf ins Repository (L16). |

## Phase 2: Systematische Suche (noch nicht begonnen)

Geplante Suchstraenge:

- S1 LLM im RE: "large language model" AND "requirements engineering"
- S2 Retrospektives RE und Mining: mining software repositories
  requirements, pull request analysis requirements
- S3 Anforderungsformate: EARS requirements syntax, requirements
  quality criteria, user story quality
- S4 Sicherheitsanforderungen: security requirements engineering,
  Common Criteria security functional requirements

Hinweis: Die EARS-Primaerquellen (L05, L14, L15) wurden bereits am
06.08.2026 gezielt beschafft. S3 beschraenkt sich daher auf
Anwendungsarbeiten Dritter sowie auf User Stories und
Qualitaetskriterien.

Portale in dieser Reihenfolge: ACM Digital Library, IEEE Xplore,
SpringerLink, ergaenzend arXiv.
