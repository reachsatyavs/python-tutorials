# Module 08 — File Handling

Every real program reads or writes data — configs, logs, CSVs, JSON responses, reports. File handling is how Python talks to the file system. This module covers everything from opening a single text file to reading structured CSV and JSON data.

**Prerequisites:** `[05-functions/](../05-functions/README.md)` — functions, `with` context managers. `[07-decorators/](../07-decorators/README.md)` — optional but helpful for error-handling patterns.

---

## Contents

| File | Type | What it covers |
| ---- | ---- | -------------- |
| `[FileHandling.md](FileHandling.md)` | Notes | Full write-up — `open()`, modes, reading, writing, `with`, `pathlib`, CSV, JSON, directory ops, error handling, cheat sheet |
| `[file_handling.py](file_handling.py)` | Script | 15 runnable examples — creates sample files, reads them back, writes CSVs and JSON, navigates paths |

---

## Learning order

1. Read `[FileHandling.md](FileHandling.md)` sections 1–5 — `open()`, modes, reading, writing, `with`.
2. Run `python3 file_handling.py` — it creates temporary files in a `temp/` folder so you can see real output.
3. Continue with sections 6–9 — `pathlib`, CSV, JSON, directory operations.
4. Read section 10 (error handling) before writing any production file code.

---

## Quick mental model

| Task | How |
| ---- | --- |
| Open a file safely | `with open("file.txt", "r") as f:` |
| Read whole file | `f.read()` |
| Read line by line | `for line in f:` |
| Write to file | `with open("file.txt", "w") as f: f.write(...)` |
| Append without overwriting | mode `"a"` |
| Modern path handling | `from pathlib import Path` |
| Read CSV | `import csv` → `csv.DictReader(f)` |
| Read / write JSON | `import json` → `json.load(f)` / `json.dump(data, f)` |

---

## Next module

**[09 — Modules & pip](../09-modules-and-pip/README.md):** what modules and packages are, `import` patterns, the standard library, creating your own module, `pip`, virtual environments, `requirements.txt`.
