# Findings: pull request details

Created: 2026-08-19T11:28:08.290631+00:00
Source: `pull_details_2026-08-14.jsonl`
SHA-256 of source: `19bc97ad11d3e097e873eb72cc84df283d20c9fffb61d8a1f7013151dfa03bd9`
Records: 476

Produced by `src/collect/analyze_pull_details.py`. No API requests.

## 1 Field coverage

Unpopulated means null, empty list, empty object or empty string.

| Field | Populated | Share | Value types |
|---|---|---|---|
| `_links` | 476 | 100.0 % | dict 476 |
| `active_lock_reason` | 0 | 0.0 % | NoneType 476 |
| `additions` | 476 | 100.0 % | int 476 |
| `assignee` | 44 | 9.2 % | NoneType 432, dict 44 |
| `assignees` | 47 | 9.9 % | list 476 |
| `author_association` | 476 | 100.0 % | str 476 |
| `auto_merge` | 0 | 0.0 % | NoneType 476 |
| `base` | 476 | 100.0 % | dict 476 |
| `body` | 420 | 88.2 % | str 420, NoneType 56 |
| `changed_files` | 476 | 100.0 % | int 476 |
| `closed_at` | 423 | 88.9 % | str 423, NoneType 53 |
| `comments` | 476 | 100.0 % | int 476 |
| `comments_url` | 476 | 100.0 % | str 476 |
| `commits` | 476 | 100.0 % | int 476 |
| `commits_url` | 476 | 100.0 % | str 476 |
| `created_at` | 476 | 100.0 % | str 476 |
| `deletions` | 476 | 100.0 % | int 476 |
| `diff_url` | 476 | 100.0 % | str 476 |
| `draft` | 476 | 100.0 % | bool 476 |
| `head` | 476 | 100.0 % | dict 476 |
| `html_url` | 476 | 100.0 % | str 476 |
| `id` | 476 | 100.0 % | int 476 |
| `issue_url` | 476 | 100.0 % | str 476 |
| `labels` | 36 | 7.6 % | list 476 |
| `locked` | 476 | 100.0 % | bool 476 |
| `maintainer_can_modify` | 476 | 100.0 % | bool 476 |
| `merge_commit_sha` | 434 | 91.2 % | str 434, NoneType 42 |
| `mergeable` | 136 | 28.6 % | NoneType 340, bool 136 |
| `mergeable_state` | 476 | 100.0 % | str 476 |
| `merged` | 476 | 100.0 % | bool 476 |
| `merged_at` | 314 | 66.0 % | str 314, NoneType 162 |
| `merged_by` | 314 | 66.0 % | dict 314, NoneType 162 |
| `milestone` | 66 | 13.9 % | NoneType 410, dict 66 |
| `node_id` | 476 | 100.0 % | str 476 |
| `number` | 476 | 100.0 % | int 476 |
| `patch_url` | 476 | 100.0 % | str 476 |
| `rebaseable` | 136 | 28.6 % | NoneType 340, bool 136 |
| `requested_reviewers` | 63 | 13.2 % | list 476 |
| `requested_teams` | 0 | 0.0 % | list 476 |
| `review_comment_url` | 476 | 100.0 % | str 476 |
| `review_comments` | 476 | 100.0 % | int 476 |
| `review_comments_url` | 476 | 100.0 % | str 476 |
| `state` | 476 | 100.0 % | str 476 |
| `statuses_url` | 476 | 100.0 % | str 476 |
| `title` | 476 | 100.0 % | str 476 |
| `updated_at` | 476 | 100.0 % | str 476 |
| `url` | 476 | 100.0 % | str 476 |
| `user` | 476 | 100.0 % | dict 476 |

## 2 Authors and bots

Distinct authors: 61
Detected as bot: 31 of 476 pull requests, 2 distinct accounts

| Account type | Pull requests |
|---|---|
| `User` | 445 |
| `Bot` | 31 |

| Bot account | Pull requests |
|---|---|
| `dependabot[bot]` | 28 |
| `Copilot` | 3 |

Distribution without account names, data minimisation per `docs/entscheidungen.md`.

| Rank | Pull requests |
|---|---|
| 1 | 95 |
| 2 | 74 |
| 3 | 67 |
| 4 | 35 |
| 5 | 28 |
| 6 | 23 |
| 7 | 16 |
| 8 | 13 |
| 9 | 13 |
| 10 | 12 |
| 11 | 7 |
| 12 | 6 |
| 13 | 5 |
| 14 | 5 |
| 15 | 4 |
| 16 | 4 |
| 17 | 4 |
| 18 | 4 |
| 19 | 3 |
| 20 | 3 |
| 21 | 3 |
| 22 | 3 |
| 23 | 3 |
| 24 | 2 |
| 25 | 2 |
| 26 | 2 |
| 27 | 2 |
| 28 | 2 |
| 29 | 2 |
| 30 | 2 |
| 31 | 2 |
| 32 | 1 |
| 33 | 1 |
| 34 | 1 |
| 35 | 1 |
| 36 | 1 |
| 37 | 1 |
| 38 | 1 |
| 39 | 1 |
| 40 | 1 |
| 41 | 1 |
| 42 | 1 |
| 43 | 1 |
| 44 | 1 |
| 45 | 1 |
| 46 | 1 |
| 47 | 1 |
| 48 | 1 |
| 49 | 1 |
| 50 | 1 |
| 51 | 1 |
| 52 | 1 |
| 53 | 1 |
| 54 | 1 |
| 55 | 1 |
| 56 | 1 |
| 57 | 1 |
| 58 | 1 |
| 59 | 1 |
| 60 | 1 |
| 61 | 1 |

## 3 Outcome of the pull requests

| outcome | Count | Share |
|---|---|---|
| `merged` | 314 | 66.0 % |
| `closed_unmerged` | 109 | 22.9 % |
| `open` | 53 | 11.1 % |

## 4 Size of the changes

| Measure | min | median | p75 | p90 | p95 | p99 | max | total |
|---|---|---|---|---|---|---|---|---|
| additions | 0 | 101 | 529 | 1978 | 5837 | 11467 | 19297 | 429717 |
| deletions | 0 | 12 | 93 | 420 | 846 | 7582 | 17650 | 154104 |
| additions + deletions | 0 | 162 | 766 | 2424 | 6880 | 18474 | 30166 | 583821 |
| changed_files | 0 | 3 | 10 | 30 | 53 | 416 | 575 | 8417 |

### Effect of candidate thresholds

Lines means `additions + deletions`.

| Threshold | PRs above | Share of PRs | Share of all lines |
|---|---|---|---|
| > 200 lines | 222 | 46.6 % | 98.0 % |
| > 500 lines | 151 | 31.7 % | 93.9 % |
| > 1000 lines | 100 | 21.0 % | 87.6 % |
| > 2000 lines | 55 | 11.6 % | 76.6 % |
| > 5000 lines | 28 | 5.9 % | 61.9 % |
| > 10000 lines | 15 | 3.2 % | 45.0 % |

## 5 Comments

| Measure | min | median | p75 | p90 | p95 | p99 | max | total |
|---|---|---|---|---|---|---|---|---|
| comments | 0 | 0 | 2 | 4 | 6 | 12 | 21 | 636 |
| review_comments | 0 | 0 | 0 | 9 | 20 | 63 | 158 | 1716 |
| commits | 0 | 3 | 11 | 28 | 55 | 168 | 430 | 6673 |

Pull requests without any comment: 222
Pull requests with review comments: 113

## 6 Description texts

Without description (null): 56
Description is whitespace only: 0
Contains template text (`<!--`): 124
Contains CRLF line endings: 259

| Measure | min | median | p75 | p90 | p95 | p99 | max | total |
|---|---|---|---|---|---|---|---|---|
| characters per description | 9 | 874 | 1876 | 3951 | 6043 | 11122 | 19512 | 679145 |

