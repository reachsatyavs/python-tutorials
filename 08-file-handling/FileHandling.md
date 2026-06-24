# Python File Handling
> Python Series · Module 08 · File Handling · `github.com/reachsatyavs/python-tutorials`

---

## Table of Contents

1. [What is File Handling — and Why?](#1-what-is-file-handling--and-why)
2. [Opening a File — `open()`](#2-opening-a-file--open)
3. [File Modes](#3-file-modes)
4. [Reading Files](#4-reading-files)
5. [Writing and Appending Files](#5-writing-and-appending-files)
6. [The `with` Statement — Always Use It](#6-the-with-statement--always-use-it)
7. [File Paths — `os.path` and `pathlib`](#7-file-paths--ospath-and-pathlib)
8. [Working with CSV Files](#8-working-with-csv-files)
9. [Working with JSON Files](#9-working-with-json-files)
10. [Directory and File Operations](#10-directory-and-file-operations)
11. [Error Handling with Files](#11-error-handling-with-files)
12. [Quick Recap — Cheat Sheet](#12-quick-recap--cheat-sheet)

---

## 1. What is File Handling — and Why?

File handling is how your Python program **reads data from** or **writes data to** the file system.

**Why you need it:**

| Situation | File handling use |
|---|---|
| Save program output | Write results to a `.txt` or `.csv` |
| Read a configuration | Load settings from a `.json` or `.ini` |
| Process a data export | Read a CSV downloaded from a database |
| Log events | Append messages to a log file |
| Exchange data with another system | Read/write JSON, XML, or plain text |

Without file handling, every result disappears when the program ends.

---

## 2. Opening a File — `open()`

```python
f = open("filename.txt", "mode")
# ... use f ...
f.close()   # always close when done
```

`open()` returns a **file object**. You read from or write to it through that object.

```python
f = open("notes.txt", "r")    # open for reading
content = f.read()
print(content)
f.close()
```

> **Always close files.** An unclosed file wastes system resources and can cause data loss on write. The `with` statement (Section 6) handles this automatically — prefer it over manual `close()`.

---

## 3. File Modes

| Mode | Meaning | File must exist? | Overwrites? |
|---|---|---|---|
| `"r"` | Read (default) | Yes — error if not found | No |
| `"w"` | Write | No — creates if missing | **Yes — erases existing content** |
| `"a"` | Append | No — creates if missing | No — adds to end |
| `"x"` | Exclusive create | No — error if it already exists | — |
| `"r+"` | Read **and** write | Yes | No |
| `"w+"` | Write **and** read | No | **Yes** |

Add `"b"` for binary mode (images, PDFs, zip files):

| Mode | Meaning |
|---|---|
| `"rb"` | Read binary |
| `"wb"` | Write binary |
| `"ab"` | Append binary |

```python
# text mode (default) — automatically handles line endings
f = open("report.txt", "r")

# binary mode — raw bytes, no conversion
f = open("photo.jpg", "rb")
```

---

## 4. Reading Files

### `f.read()` — whole file as one string

```python
with open("poem.txt", "r") as f:
    content = f.read()
print(content)
```

### `f.readline()` — one line at a time

```python
with open("poem.txt", "r") as f:
    first  = f.readline()   # "Roses are red\n"
    second = f.readline()   # "Violets are blue\n"
print(first.strip())
print(second.strip())
```

### `f.readlines()` — all lines as a list

```python
with open("poem.txt", "r") as f:
    lines = f.readlines()   # ["Roses are red\n", "Violets are blue\n", ...]
print(lines)
print(len(lines), "lines")
```

### Iterating line by line — most memory-efficient

```python
with open("bigfile.txt", "r") as f:
    for line in f:                   # reads one line at a time
        print(line.strip())
```

> **Prefer iteration** over `readlines()` for large files — it uses constant memory (like a generator).

### `f.read(n)` — read n characters

```python
with open("poem.txt", "r") as f:
    chunk = f.read(10)   # first 10 characters
    print(repr(chunk))
```

### `f.tell()` and `f.seek()` — cursor position

```python
with open("poem.txt", "r") as f:
    f.read(5)
    print(f.tell())        # 5  — cursor is after character 5
    f.seek(0)              # move cursor back to start
    print(f.read(5))       # reads first 5 again
```

---

## 5. Writing and Appending Files

### `f.write()` — write a string

```python
with open("output.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
```

> **Mode `"w"` erases the existing file.** Always double-check the mode before writing.

### `f.writelines()` — write a list of strings

```python
lines = ["Alice,90\n", "Bob,85\n", "Carol,92\n"]

with open("scores.txt", "w") as f:
    f.writelines(lines)   # no separator added — include \n in each item
```

### Append — add to the end without erasing

```python
with open("log.txt", "a") as f:
    f.write("2026-06-01 09:00  Server started\n")

with open("log.txt", "a") as f:
    f.write("2026-06-01 09:05  User logged in\n")
```

---

## 6. The `with` Statement — Always Use It

`with open(...) as f:` is a **context manager**. It automatically closes the file when the block ends — even if an exception occurs.

```python
# ❌ Manual close — forgettable, not exception-safe
f = open("data.txt", "r")
content = f.read()
f.close()          # if an error happens above, this line never runs

# ✅ with — closes automatically, exception-safe
with open("data.txt", "r") as f:
    content = f.read()
# f is closed here — no need to call f.close()
```

**Opening two files at once:**

```python
with open("input.txt", "r") as src, open("output.txt", "w") as dst:
    for line in src:
        dst.write(line.upper())
```

> **Rule:** Always use `with open(...)`. Never use bare `open()` + manual `close()` in production code.

---

## 7. File Paths — `os.path` and `pathlib`

### Absolute vs relative paths

```python
# Relative — relative to where the script runs
open("data.txt")              # same folder as the script
open("data/scores.txt")       # subfolder

# Absolute — full path from root
open("/Users/alice/data.txt")   # macOS / Linux
open("C:\\Users\\alice\\data.txt")  # Windows
```

### `pathlib` — the modern, recommended way

```python
from pathlib import Path

# current directory
cwd = Path.cwd()
print(cwd)

# build a path with /  (works on every OS)
p = Path("data") / "scores" / "2026.csv"
print(p)          # data/scores/2026.csv

# check existence
print(p.exists())
print(p.is_file())
print(p.is_dir())

# file metadata
print(p.name)        # 2026.csv
print(p.stem)        # 2026
print(p.suffix)      # .csv
print(p.parent)      # data/scores

# open through a Path object
with p.open("r") as f:
    print(f.read())

# read/write shorthand
text = p.read_text()                # entire file as string
p.write_text("new content\n")       # write and close in one line
```

### `os.path` — older style (still common)

```python
import os

print(os.path.exists("data.txt"))
print(os.path.isfile("data.txt"))
print(os.path.dirname("/home/user/data.txt"))   # /home/user
print(os.path.basename("/home/user/data.txt"))  # data.txt
print(os.path.join("data", "scores", "2026.csv"))  # data/scores/2026.csv
print(os.path.abspath("data.txt"))              # full absolute path
```

> **Prefer `pathlib`** for new code — cleaner syntax, cross-platform by default.

---

## 8. Working with CSV Files

CSV (Comma-Separated Values) is the most common format for tabular data exports.

### Reading with `csv.reader`

```python
import csv

with open("students.csv", "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # each row is a list of strings
```

> Always pass `newline=""` when opening CSV files — prevents double newlines on Windows.

### Reading with `csv.DictReader` — rows as dicts

```python
import csv

with open("students.csv", "r", newline="") as f:
    reader = csv.DictReader(f)   # first row becomes header keys
    for row in reader:
        print(row["name"], row["score"])
```

Each `row` is an `OrderedDict` (or plain dict in Python 3.8+) keyed by column header.

### Writing with `csv.writer`

```python
import csv

rows = [
    ["name",  "score", "grade"],
    ["Alice",  90,      "A"],
    ["Bob",    75,      "B"],
    ["Carol",  88,      "A"],
]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

### Writing with `csv.DictWriter`

```python
import csv

students = [
    {"name": "Alice", "score": 90, "grade": "A"},
    {"name": "Bob",   "score": 75, "grade": "B"},
]

with open("results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score", "grade"])
    writer.writeheader()
    writer.writerows(students)
```

---

## 9. Working with JSON Files

JSON is the standard format for APIs and configuration files.

### Reading JSON

```python
import json

with open("config.json", "r") as f:
    config = json.load(f)    # parses JSON → Python dict/list

print(config["database"]["host"])
```

### Writing JSON

```python
import json

data = {
    "name": "Alice",
    "scores": [90, 85, 92],
    "active": True
}

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)   # indent=4 makes it human-readable
```

**`output.json`:**
```json
{
    "name": "Alice",
    "scores": [90, 85, 92],
    "active": true
}
```

### JSON ↔ Python type mapping

| JSON | Python |
|---|---|
| `object { }` | `dict` |
| `array [ ]` | `list` |
| `string ""` | `str` |
| `number` | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

### JSON string (without file)

```python
import json

# Python dict → JSON string
text = json.dumps({"name": "Alice", "score": 90}, indent=2)
print(text)

# JSON string → Python dict
d = json.loads('{"name": "Alice", "score": 90}')
print(d["name"])
```

---

## 10. Directory and File Operations

### Create and remove directories

```python
import os
from pathlib import Path

# create a single directory
os.mkdir("reports")

# create nested directories (like mkdir -p)
os.makedirs("data/2026/june", exist_ok=True)   # exist_ok avoids error if exists
Path("data/2026/july").mkdir(parents=True, exist_ok=True)  # pathlib version

# remove an empty directory
os.rmdir("reports")
```

### List directory contents

```python
import os
from pathlib import Path

# os style
for name in os.listdir("."):
    print(name)

# pathlib style — more powerful
for entry in Path(".").iterdir():
    print(entry.name, "DIR" if entry.is_dir() else entry.suffix)

# glob — find files by pattern
for csv_file in Path("data").glob("*.csv"):
    print(csv_file)

# rglob — recursive glob
for py_file in Path(".").rglob("*.py"):
    print(py_file)
```

### Copy, move, delete files

```python
import shutil
from pathlib import Path

# copy file
shutil.copy("source.txt", "destination.txt")

# copy entire folder
shutil.copytree("src_folder", "dst_folder")

# move / rename
shutil.move("old_name.txt", "new_name.txt")

# delete a file
Path("temp.txt").unlink()                    # pathlib
os.remove("temp.txt")                        # os

# delete entire folder tree
shutil.rmtree("temp_folder")
```

---

## 11. Error Handling with Files

### Common file errors

| Error | When it happens |
|---|---|
| `FileNotFoundError` | Reading a file that does not exist |
| `PermissionError` | No read/write permission on the file |
| `IsADirectoryError` | Trying to `open()` a directory as a file |
| `FileExistsError` | Mode `"x"` on an existing file |

### Always check / handle before reading

```python
from pathlib import Path

path = Path("data.txt")

# Option 1 — check first (LBYL — Look Before You Leap)
if path.exists():
    content = path.read_text()
else:
    print("File not found")

# Option 2 — try/except (EAFP — Easier to Ask Forgiveness than Permission)
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("No permission to read this file")
```

### Safe write — never overwrite an existing file

```python
from pathlib import Path

def safe_write(filename, content):
    path = Path(filename)
    if path.exists():
        raise FileExistsError(f"{filename} already exists — not overwriting")
    path.write_text(content)
```

---

## 12. Quick Recap — Cheat Sheet

### Opening and reading

```python
# read whole file
with open("file.txt", "r") as f:
    text = f.read()

# read line by line (memory-efficient)
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# read all lines into a list
with open("file.txt", "r") as f:
    lines = f.readlines()
```

### Writing and appending

```python
# write (creates or overwrites)
with open("file.txt", "w") as f:
    f.write("hello\n")

# append (adds to end)
with open("file.txt", "a") as f:
    f.write("another line\n")
```

### pathlib quick reference

```python
from pathlib import Path
p = Path("data/scores.csv")

p.exists()          # bool
p.is_file()         # bool
p.name              # "scores.csv"
p.stem              # "scores"
p.suffix            # ".csv"
p.parent            # Path("data")
p.read_text()       # read whole file
p.write_text("x")   # write and close
p.mkdir(parents=True, exist_ok=True)
list(p.parent.glob("*.csv"))
```

### CSV quick reference

```python
import csv

# read
with open("f.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row["col"])

# write
with open("f.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["a","b"])
    w.writeheader()
    w.writerows([{"a":1,"b":2}])
```

### JSON quick reference

```python
import json

# file → dict
with open("f.json") as f:
    data = json.load(f)

# dict → file
with open("f.json", "w") as f:
    json.dump(data, f, indent=4)

# string ↔ dict
s    = json.dumps(data)
data = json.loads(s)
```

### Key rules

- Always use `with open(...) as f:` — never manual `close()`
- Mode `"w"` **erases** existing content — double-check
- Pass `newline=""` when opening CSV files
- Prefer `pathlib.Path` over string paths for new code
- Use `json.dump(..., indent=4)` for human-readable output
- Handle `FileNotFoundError` and `PermissionError` before shipping code

---

*Python Series by Satya VS · [github.com/reachsatyavs/python-tutorials](https://github.com/reachsatyavs/python-tutorials)*
