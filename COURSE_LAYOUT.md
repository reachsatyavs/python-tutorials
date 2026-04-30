# Course directory layout (planned + current)

This document is the **map** for reorganising `python-tutorials`. Numbers keep folders sortable in the file explorer.

**Note:** College algorithm chapters are **11 / 7 / 9 contact hours** respectively (not “11 topics”).

---

## Current layout (after reorganisation)

```text
python-tutorials/
├── README.md                 # Course index (setup guide → module 01)
├── COURSE_LAYOUT.md          # This file — full roadmap
│
├── 01-python-intro/          # ✅ Why Python + install / venv / JupyterLab (full guide)
├── 02-data-types/            # ✅ Was: dataTypes/
├── 03-operators/             # ✅ Was: Operators/
├── 04-control-flows/         # ✅ Was: ControlFlows/
├── 05-functions/             # ✅ Was: Functions/
│
├── Hashing/                  # Supplementary (dict/hash internals) — not renumbered yet
├── AI_ML_Ecosystem.md
├── LLM.md
└── DevOps.md
```

---

## Planned modules (create when you have content)

| Dir | Topic | Status |
|-----|--------|--------|
| `06-comprehensions/` | List/dict/set comprehensions; generators (optional teaser) | Planned |
| `07-file-handling/` | Paths, open/read/write, context managers | Planned |
| `08-modules-pip/` | `import`, packages, `pip`, venv recap | Planned |
| `09-exception-handling/` | try/except/finally, raising, custom exceptions | Planned |
| `10-string-handling/` | Formatting, parsing patterns (can overlap 02; here = “string as text processing”) | Planned |
| `11-oop-basic/` | Classes, `__init__`, methods, attributes only | Planned |
| `12-regex-optional/` | `re` module | Planned |
| `13-bridge-ds-dataframes/` | From core Python to structures / pandas intro | Planned |

---

## Planned algorithm track (college chapters)

Place after core Python (e.g. after `13-…` or parallel term). Folder names can be adjusted to match official chapter titles.

| Dir (suggested) | Chapter | Hours |
|-----------------|---------|------:|
| `14-algorithms-data-structures/` | Algorithm 1 — Data structures | 11 |
| `15-algorithms-sorting/` | Algorithm 2 — Sorting | 7 |
| `16-algorithms-problem-solving/` | Algorithm 3 — Problem-solving with algorithms | 9 |

---

## Migration log (existing → numbered)

| Old path | New path |
|----------|----------|
| *(none)* | `01-python-intro/` |
| `dataTypes/` | `02-data-types/` |
| `Operators/` | `03-operators/` |
| `ControlFlows/` | `04-control-flows/` |
| `Functions/` | `05-functions/` |

Internal file links **inside** each module were relative to that folder only, so they still work after the rename.
