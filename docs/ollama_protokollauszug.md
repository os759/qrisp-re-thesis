# Auszug aus dem Serverprotokoll von Ollama, 30.09.2026

Zweck: Belege fuer Abschnitt 6.1 der Arbeit (sec:eval-pilot-lokal)
und fuer die Messgroesse M6 (Speicherbedarf) aus F3 in
docs/entscheidungen.md. Das vollstaendige Protokoll bleibt ausserhalb
des Repositorys. Erzeugt mit einem Hilfsskript, das die Zeilen aus
der Datei liest; jede Zeile ist auf 220 Zeichen gekuerzt.

Quelle: ~/qrisp-ollama-logs/serve_2026-09-30.log
SHA-256 der Protokolldatei: d1ca597e8303e7c3bf714b550e60ec05ac723162f6687a1ea274055b6c126b6a
Zeilen in der Protokolldatei: 1479

Inhalte von Pull Requests stehen in keiner der ausgewaehlten Zeilen.
Nicht aufgenommen ist Zeile 2 (Serverkonfiguration), weil sie
Umgebungsvariablen und lokale Pfade enthaelt.

## Ausgewaehlte Zeilen

Zeile 3: Cloud-Funktionen abgeschaltet (F2, Tabelle tab:pilot-bedingungen)

```
    3: time=2026-09-30T00:45:04.287+02:00 level=INFO source=routes.go:2007 msg="Ollama cloud disabled: true"
```

Zeile 10: Voreingestelltes Kontextfenster 32 768 Token, bemessen am Grafikspeicher, vor dem Laden eines Modells

```
   10: time=2026-09-30T00:45:04.379+02:00 level=INFO source=routes.go:2115 msg="vram-based default context" total_vram="28.1 GiB" default_num_ctx=32768
```

Zeile 29: Nutzbarer Grafikspeicher 28 753 MiB

```
   29: cmn  common_param:   - MTL0    : Apple M3 Pro (28753 MiB, 28753 MiB free)
```

Zeile 47: M6, gpt-oss-20b-ctx64k: eingeplanter Grafikspeicher

```
   47: common_params_fit_impl: projected to use 13838 MiB of device memory vs. 28753 MiB of free device memory
```

Zeile 107: gpt-oss-20b-ctx64k: Dateigroesse der Gewichte

```
  107: print_info: file size   = 12.83 GiB (5.27 BPW) 
```

Zeile 335: Erster Versuch: keine Kuerzung, 8 071 Token im Kontext am Ende der Anfrage

```
  335: slot      release: id  0 | task 0 | stop processing: n_tokens = 8071, truncated = 0
```

Zeile 383: qwen3.6-27b-ctx64k: geschaetzter Hoechstbedarf des Bildteils

```
  383: srv    load_model: [mtmd] estimated worst-case memory usage of mmproj is 1188.39 MiB (took 99.42 ms)
```

Zeile 395: M6, qwen3.6-27b-ctx64k: eingeplanter Grafikspeicher, ohne Bildteil

```
  395: common_params_fit_impl: projected to use 21155 MiB of device memory vs. 28154 MiB of free device memory
```

Zeile 439: qwen3.6-27b-ctx64k: Dateigroesse der Gewichte

```
  439: print_info: file size   = 15.67 GiB (4.93 BPW) 
```

Zeile 655: qwen3.6-27b-ctx64k: Groesse des Bildteils

```
  655: load_hparams: model size:         887.99 MiB
```

Zeile 659: qwen3.6-27b-ctx64k: Rechenpuffer des Bildteils

```
  659: reserve_compute_meta:       MTL0 compute buffer size =   275.48 MiB
```

Zeile 1475: Zweiter Versuch: keine Kuerzung, 13 889 Token im Kontext am Ende der Anfrage

```
 1475: slot      release: id  0 | task 0 | stop processing: n_tokens = 13889, truncated = 0
```

## Adresse des Servers

```
    6: time=2026-09-30T00:45:04.290+02:00 level=INFO source=routes.go:2065 msg="Listening on 127.0.0.1:11434 (version 0.34.4)"
```

## Zugriffsliste des Servers

Alle Zeilen mit [GIN]: Uhrzeit, Ergebnis, Dauer, Adresse des
Aufrufers und Endpunkt.
Anfragen an /v1/responses: 2.

```
   11: [GIN] 2026/09/30 - 08:04:33 | 200 |      45.875µs |       127.0.0.1 | GET      "/api/version"
   12: [GIN] 2026/09/30 - 08:04:33 | 200 |      13.583µs |       127.0.0.1 | HEAD     "/"
   13: [GIN] 2026/09/30 - 08:04:33 | 200 |      3.1095ms |       127.0.0.1 | GET      "/api/tags"
   14: [GIN] 2026/09/30 - 08:13:05 | 200 |      30.125µs |       127.0.0.1 | GET      "/api/version"
   15: [GIN] 2026/09/30 - 08:13:05 | 200 |   35.750292ms |       127.0.0.1 | POST     "/api/show"
   16: [GIN] 2026/09/30 - 08:13:05 | 200 |    1.473583ms |       127.0.0.1 | GET      "/api/tags"
  337: [GIN] 2026/09/30 - 08:14:43 | 200 |         1m38s |       127.0.0.1 | POST     "/v1/responses"
  338: [GIN] 2026/09/30 - 08:53:12 | 200 |      15.042µs |       127.0.0.1 | HEAD     "/"
  340: [GIN] 2026/09/30 - 09:01:23 | 200 |       16.75µs |       127.0.0.1 | HEAD     "/"
  345: [GIN] 2026/09/30 - 09:03:42 | 200 |        10m29s |       127.0.0.1 | POST     "/api/pull"
  346: [GIN] 2026/09/30 - 09:03:42 | 200 |       8.292µs |       127.0.0.1 | HEAD     "/"
  347: [GIN] 2026/09/30 - 09:03:42 | 200 |         2m18s |       127.0.0.1 | POST     "/api/create"
  348: [GIN] 2026/09/30 - 09:03:42 | 200 |      11.125µs |       127.0.0.1 | HEAD     "/"
  349: [GIN] 2026/09/30 - 09:03:42 | 200 |   63.596625ms |       127.0.0.1 | POST     "/api/show"
  350: [GIN] 2026/09/30 - 09:03:42 | 200 |   60.927292ms |       127.0.0.1 | POST     "/api/show"
  351: [GIN] 2026/09/30 - 09:03:42 | 200 |      11.667µs |       127.0.0.1 | HEAD     "/"
  352: [GIN] 2026/09/30 - 09:03:42 | 200 |     712.667µs |       127.0.0.1 | POST     "/api/show"
  702: [GIN] 2026/09/30 - 09:03:52 | 200 |  9.461238833s |       127.0.0.1 | POST     "/api/generate"
  703: [GIN] 2026/09/30 - 09:03:52 | 200 |    1.230791ms |       127.0.0.1 | HEAD     "/"
  704: [GIN] 2026/09/30 - 09:03:52 | 200 |    1.357583ms |       127.0.0.1 | GET      "/api/ps"
  705: [GIN] 2026/09/30 - 09:05:21 | 200 |      17.042µs |       127.0.0.1 | HEAD     "/"
  706: [GIN] 2026/09/30 - 09:05:21 | 200 |    31.82875ms |       127.0.0.1 | POST     "/api/create"
  707: [GIN] 2026/09/30 - 09:05:21 | 200 |      13.041µs |       127.0.0.1 | HEAD     "/"
  708: [GIN] 2026/09/30 - 09:05:21 | 200 |     852.041µs |       127.0.0.1 | POST     "/api/show"
  709: [GIN] 2026/09/30 - 09:05:21 | 200 |      12.042µs |       127.0.0.1 | HEAD     "/"
  710: [GIN] 2026/09/30 - 09:05:21 | 200 |     698.041µs |       127.0.0.1 | POST     "/api/show"
  711: [GIN] 2026/09/30 - 09:05:21 | 200 |    1.751583ms |       127.0.0.1 | POST     "/api/generate"
  712: [GIN] 2026/09/30 - 09:05:21 | 200 |      11.292µs |       127.0.0.1 | HEAD     "/"
  713: [GIN] 2026/09/30 - 09:05:21 | 200 |      15.333µs |       127.0.0.1 | GET      "/api/ps"
  714: [GIN] 2026/09/30 - 09:16:40 | 200 |      60.583µs |       127.0.0.1 | GET      "/api/version"
  715: [GIN] 2026/09/30 - 09:16:40 | 200 |    1.265458ms |       127.0.0.1 | POST     "/api/show"
  716: [GIN] 2026/09/30 - 09:16:41 | 200 |    4.041083ms |       127.0.0.1 | GET      "/api/tags"
 1477: [GIN] 2026/09/30 - 09:37:47 | 200 |         21m6s |       127.0.0.1 | POST     "/v1/responses"
 1479: [GIN] 2026/09/30 - 15:02:49 | 200 |     203.791µs |       127.0.0.1 | GET      "/api/version"
```

