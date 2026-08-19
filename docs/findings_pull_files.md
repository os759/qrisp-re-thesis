# Findings: changed files and diffs

Created: 2026-08-19T11:28:25.527236+00:00
Source: `pull_files_2026-08-19.jsonl`
SHA-256 of source: `7315f5254a914278618c85c23422d7f2a04d1460ee8d8c6c6733f4e91533bbdc`
File records: 8424
Pull requests with at least one file: 471
Characters of patch text: 32557763

Produced by `src/collect/analyze_pull_files.py`. No API requests.

## 1 Kind of change

| status | Files | Share |
|---|---|---|
| `modified` | 6320 | 75.0 % |
| `added` | 1618 | 19.2 % |
| `removed` | 302 | 3.6 % |
| `renamed` | 184 | 2.2 % |

## 2 File extensions

The 20 extensions holding the most patch text.

| Extension | Files | Characters | Share of characters |
|---|---|---|---|
| `.py` | 6596 | 26378164 | 81.0 % |
| `.ipynb` | 134 | 2332725 | 7.2 % |
| `.rst` | 1219 | 2287404 | 7.0 % |
| `.drawio` | 11 | 493599 | 1.5 % |
| `.bkp` | 11 | 435362 | 1.3 % |
| `.svg` | 14 | 277368 | 0.9 % |
| `.html` | 18 | 85881 | 0.3 % |
| `.yml` | 75 | 79576 | 0.2 % |
| `.md` | 37 | 57256 | 0.2 % |
| `.css` | 16 | 38010 | 0.1 % |
| `.toml` | 53 | 36719 | 0.1 % |
| `.txt` | 14 | 12630 | 0.0 % |
| `.js` | 4 | 11375 | 0.0 % |
| `.td` | 6 | 9828 | 0.0 % |
| `.dtmp` | 1 | 8184 | 0.0 % |
| `(no extension)` | 33 | 6955 | 0.0 % |
| `.cfg` | 15 | 5344 | 0.0 % |
| `.yaml` | 1 | 531 | 0.0 % |
| `.bat` | 1 | 456 | 0.0 % |
| `.in` | 3 | 396 | 0.0 % |

## 3 Top level directories

| Directory | Files | Characters | Share of characters |
|---|---|---|---|
| `src` | 4409 | 17619598 | 54.1 % |
| `tests` | 2108 | 8665985 | 26.6 % |
| `documentation` | 1665 | 6044668 | 18.6 % |
| `(repository root)` | 150 | 114190 | 0.4 % |
| `.github` | 77 | 81894 | 0.3 % |
| `.ipynb_checkpoints` | 1 | 11396 | 0.0 % |
| `requirements` | 6 | 10435 | 0.0 % |
| `tools` | 3 | 9597 | 0.0 % |
| `logo` | 4 | 0 | 0.0 % |
| `scripts` | 1 | 0 | 0.0 % |

## 4 Files delivered without a patch

GitHub omits the `patch` field for 331 of 8424 files (3.9 %).

| Extension | Files without patch |
|---|---|
| `.png` | 151 |
| `.py` | 128 |
| `.rst` | 19 |
| `(no extension)` | 8 |
| `.html` | 8 |
| `.jpg` | 7 |
| `.ipynb` | 4 |
| `.docx` | 2 |
| `.pptx` | 1 |
| `.css` | 1 |
| `.js` | 1 |
| `.typed` | 1 |

## 5 Size of the patch text

| Measure | min | median | p75 | p90 | p95 | p99 | max | total |
|---|---|---|---|---|---|---|---|---|
| characters per file | 45 | 1397 | 4013 | 9534 | 16612 | 40147 | 99478 | 32557763 |
| characters per pull request | 0 | 9627 | 35472 | 112459 | 288050 | 1182055 | 2761999 | 32557763 |
| files per pull request | 1 | 4 | 10 | 31 | 53 | 417 | 575 | 8424 |

### Effect of candidate thresholds per pull request

| Threshold | PRs above | Share of PRs | Share of all characters |
|---|---|---|---|
| > 10000 characters | 231 | 49.0 % | 97.9 % |
| > 50000 characters | 94 | 20.0 % | 87.8 % |
| > 100000 characters | 54 | 11.5 % | 78.9 % |
| > 250000 characters | 27 | 5.7 % | 66.6 % |
| > 500000 characters | 13 | 2.8 % | 52.0 % |
| > 1000000 characters | 7 | 1.5 % | 38.2 % |

## 6 The largest pull requests

The 15 pull requests holding the most patch text, each with its three strongest extensions.

| PR | Files | Characters | Share | Strongest extensions |
|---|---|---|---|---|
| #674 | 574 | 2761999 | 8.5 % | .py 100 %, .toml 0 %, .yml 0 % |
| #676 | 575 | 2758805 | 8.5 % | .py 100 %, .toml 0 %, .yml 0 % |
| #197 | 429 | 1827787 | 5.6 % | .py 100 %, .rst 0 % |
| #670 | 475 | 1587059 | 4.9 % | .py 99 %, .toml 0 %, .yml 0 % |
| #488 | 412 | 1387796 | 4.3 % | .py 96 %, .ipynb 4 %, .toml 0 % |
| #675 | 380 | 1093880 | 3.4 % | .py 100 %, .rst 0 %, (no extension) 0 % |
| #532 | 52 | 1018406 | 3.1 % | .drawio 48 %, .bkp 43 %, .html 8 % |
| #248 | 87 | 890026 | 2.7 % | .ipynb 63 %, .rst 35 %, .py 2 % |
| #246 | 40 | 870793 | 2.7 % | .ipynb 68 %, .rst 32 %, .html 0 % |
| #446 | 475 | 776637 | 2.4 % | .py 100 %, .toml 0 %, (no extension) 0 % |
| #134 | 193 | 774927 | 2.4 % | .py 85 %, .rst 8 %, .ipynb 6 % |
| #300 | 381 | 634815 | 1.9 % | .py 100 % |
| #331 | 132 | 559741 | 1.7 % | .py 90 %, .rst 9 %, .ipynb 0 % |
| #361 | 106 | 479001 | 1.5 % | .py 94 %, .rst 4 %, .ipynb 1 % |
| #413 | 97 | 459391 | 1.4 % | .py 95 %, .rst 3 %, .ipynb 1 % |

