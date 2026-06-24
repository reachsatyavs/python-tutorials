# Module 09 — Modules & pip

A **module** is any `.py` file. A **package** is a folder of modules. Together they are how Python code is organised, reused, and shared across the world. `pip` is the command-line tool that installs packages from the Python Package Index (PyPI).

**Prerequisites:** `[08-file-handling/](../08-file-handling/README.md)` — you will see modules that read/write files. A basic comfort with the terminal is helpful for `pip` and `venv` commands.

---

## Contents

| File | Type | What it covers |
| ---- | ---- | -------------- |
| `[Modules.md](Modules.md)` | Notes | Full write-up — what modules are, `import` patterns, standard library overview, creating your own module, `__name__`, packages, `pip`, virtual environments, `requirements.txt`, cheat sheet |
| `[modules_examples.py](modules_examples.py)` | Script | 12 runnable examples — standard library modules, creating and importing a local module, JSON/CSV round-trips, `__name__` guard, datetime, collections, itertools |
| `[myutils.py](myutils.py)` | Helper | A small sample module imported by `modules_examples.py` |

---

## Learning order

1. Read `[Modules.md](Modules.md)` sections 1–4 — what a module is, `import` forms, and the standard library.
2. Run `python3 modules_examples.py` from this folder to see standard-library modules in action.
3. Read sections 5–6 — creating your own module and the `__name__` guard.
4. Read sections 7–9 — `pip`, virtual environments, and `requirements.txt`. Follow along in your terminal.

---

## Quick mental model

| Concept | One line |
| ------- | -------- |
| Module | Any `.py` file — `math`, `os`, `myutils` |
| Package | A folder with `__init__.py` inside |
| `import math` | Loads the module; access via `math.sqrt()` |
| `from math import sqrt` | Brings `sqrt` into local scope |
| `import math as m` | Alias — access via `m.sqrt()` |
| `if __name__ == "__main__":` | Code that only runs when the file is the entry point |
| `pip install requests` | Downloads and installs a third-party package |
| `venv` | Isolated Python environment — one per project |
| `requirements.txt` | Snapshot of all package versions your project needs |

---

## Next module

**10 — Exception Handling** (planned): `try / except / else / finally`, raising exceptions, custom exception classes, and best practices.
