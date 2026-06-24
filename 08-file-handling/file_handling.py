"""
Python File Handling — 15 Runnable Examples
Module 08 · python-tutorials

Run:  python3 file_handling.py
All temporary files are created inside a  temp/  subfolder and cleaned up at the end.
"""

import csv
import json
import os
import shutil
from pathlib import Path

SEP = "─" * 60
TEMP = Path("temp")

def section(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)

# create a clean temp directory for all examples
if TEMP.exists():
    shutil.rmtree(TEMP)
TEMP.mkdir()


# ──────────────────────────────────────────────────────────
# Example 01 — Write a text file (mode "w")
# ──────────────────────────────────────────────────────────
section("01 — Write a text file  (mode 'w')")

path = TEMP / "poem.txt"
with open(path, "w") as f:
    f.write("Roses are red\n")
    f.write("Violets are blue\n")
    f.write("Python is elegant\n")
    f.write("And so are you\n")

print(f"  Written: {path}")


# ──────────────────────────────────────────────────────────
# Example 02 — Read whole file with f.read()
# ──────────────────────────────────────────────────────────
section("02 — Read whole file  (f.read())")

with open(path, "r") as f:
    content = f.read()

print(content)
print(f"  Total characters: {len(content)}")


# ──────────────────────────────────────────────────────────
# Example 03 — Read line by line (for loop — memory-efficient)
# ──────────────────────────────────────────────────────────
section("03 — Read line by line  (for line in f)")

with open(path, "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"  Line {i}: {line.strip()}")


# ──────────────────────────────────────────────────────────
# Example 04 — readlines() → list of strings
# ──────────────────────────────────────────────────────────
section("04 — readlines() — all lines as a list")

with open(path, "r") as f:
    lines = f.readlines()

print(f"  Type: {type(lines)}")
print(f"  Lines: {lines}")
print(f"  First line stripped: {lines[0].strip()}")
print(f"  Last  line stripped: {lines[-1].strip()}")


# ──────────────────────────────────────────────────────────
# Example 05 — Append to a file (mode "a")
# ──────────────────────────────────────────────────────────
section("05 — Append to a file  (mode 'a')")

log_path = TEMP / "log.txt"

entries = [
    "2026-06-24 09:00  Server started",
    "2026-06-24 09:05  User alice logged in",
    "2026-06-24 09:12  User bob logged in",
    "2026-06-24 09:30  Backup completed",
]

for entry in entries:
    with open(log_path, "a") as f:        # opens and closes each time
        f.write(entry + "\n")

print(f"  Log written: {log_path}")
with open(log_path, "r") as f:
    print(f.read())


# ──────────────────────────────────────────────────────────
# Example 06 — Copy file contents (read src, write dst)
# ──────────────────────────────────────────────────────────
section("06 — Copy file: read source, write destination")

src = TEMP / "poem.txt"
dst = TEMP / "poem_upper.txt"

with open(src, "r") as s, open(dst, "w") as d:
    for line in s:
        d.write(line.upper())

print("  Original:")
print(src.read_text())
print("  Uppercased copy:")
print(dst.read_text())


# ──────────────────────────────────────────────────────────
# Example 07 — pathlib — path operations
# ──────────────────────────────────────────────────────────
section("07 — pathlib — building and inspecting paths")

p = TEMP / "data" / "scores" / "june_2026.csv"

print(f"  Full path : {p}")
print(f"  Name      : {p.name}")
print(f"  Stem      : {p.stem}")
print(f"  Suffix    : {p.suffix}")
print(f"  Parent    : {p.parent}")
print(f"  Exists?   : {p.exists()}")

# Create parent dirs and the file
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("name,score\nAlice,90\nBob,85\n")
print(f"  Created   : {p}")
print(f"  Exists now: {p.exists()}")


# ──────────────────────────────────────────────────────────
# Example 08 — pathlib glob — find files by pattern
# ──────────────────────────────────────────────────────────
section("08 — pathlib glob — find files matching a pattern")

# Create a few more files to glob
for name in ["jan.csv", "feb.csv", "mar.csv", "notes.txt"]:
    (TEMP / "data" / "scores" / name).write_text(f"data for {name}\n")

print("  All .csv files under temp/data/scores/:")
for csv_file in sorted((TEMP / "data" / "scores").glob("*.csv")):
    print(f"    {csv_file.name}")

print("\n  All files anywhere under temp/ (rglob):")
for f in sorted(TEMP.rglob("*")):
    if f.is_file():
        print(f"    {f.relative_to(TEMP)}")


# ──────────────────────────────────────────────────────────
# Example 09 — CSV write with csv.writer
# ──────────────────────────────────────────────────────────
section("09 — Write CSV  (csv.writer)")

csv_path = TEMP / "students.csv"

rows = [
    ["name",  "score", "grade"],
    ["Alice",  90,      "A"],
    ["Bob",    75,      "B"],
    ["Carol",  88,      "A"],
    ["Dave",   55,      "C"],
]

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"  Written: {csv_path}")
print(csv_path.read_text())


# ──────────────────────────────────────────────────────────
# Example 10 — CSV read with csv.DictReader
# ──────────────────────────────────────────────────────────
section("10 — Read CSV  (csv.DictReader — rows as dicts)")

with open(csv_path, "r", newline="") as f:
    reader = csv.DictReader(f)
    students = list(reader)

for s in students:
    print(f"  {s['name']:<8}  score={s['score']}  grade={s['grade']}")

# find the topper
topper = max(students, key=lambda s: int(s["score"]))
print(f"\n  Topper: {topper['name']} ({topper['score']})")


# ──────────────────────────────────────────────────────────
# Example 11 — CSV write with csv.DictWriter
# ──────────────────────────────────────────────────────────
section("11 — Write CSV  (csv.DictWriter — from list of dicts)")

employees = [
    {"name": "Alice",  "dept": "Engineering", "salary": 90000},
    {"name": "Bob",    "dept": "Marketing",   "salary": 75000},
    {"name": "Carol",  "dept": "Engineering", "salary": 95000},
]

emp_csv = TEMP / "employees.csv"
with open(emp_csv, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "dept", "salary"])
    writer.writeheader()
    writer.writerows(employees)

print(emp_csv.read_text())


# ──────────────────────────────────────────────────────────
# Example 12 — JSON write (json.dump)
# ──────────────────────────────────────────────────────────
section("12 — Write JSON  (json.dump)")

config = {
    "app":      "python-tutorials",
    "version":  "1.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "tutorialdb"
    },
    "features": ["file_handling", "modules", "decorators"],
    "debug":    False
}

json_path = TEMP / "config.json"
with open(json_path, "w") as f:
    json.dump(config, f, indent=4)

print(json_path.read_text())


# ──────────────────────────────────────────────────────────
# Example 13 — JSON read (json.load)
# ──────────────────────────────────────────────────────────
section("13 — Read JSON  (json.load)")

with open(json_path, "r") as f:
    loaded = json.load(f)

print(f"  App     : {loaded['app']}")
print(f"  DB host : {loaded['database']['host']}")
print(f"  DB port : {loaded['database']['port']}")
print(f"  Features: {loaded['features']}")
print(f"  Debug   : {loaded['debug']}")

# update a value and write back
loaded["version"] = "1.1"
loaded["features"].append("generators")
with open(json_path, "w") as f:
    json.dump(loaded, f, indent=4)
print(f"\n  Updated version: {loaded['version']}")


# ──────────────────────────────────────────────────────────
# Example 14 — Error handling with files
# ──────────────────────────────────────────────────────────
section("14 — Error handling  (FileNotFoundError, PermissionError)")

# FileNotFoundError
try:
    with open("this_does_not_exist.txt", "r") as f:
        f.read()
except FileNotFoundError as e:
    print(f"  FileNotFoundError: {e}")

# Check before opening (LBYL pattern)
ghost = Path("ghost.txt")
if ghost.exists():
    text = ghost.read_text()
else:
    print(f"  '{ghost}' not found — using default value")
    text = ""

# Safe exclusive create — mode "x" errors if file already exists
exclusive = TEMP / "once.txt"
try:
    with open(exclusive, "x") as f:     # creates new file
        f.write("created once\n")
    print(f"  Created: {exclusive}")
except FileExistsError:
    print(f"  '{exclusive}' already exists — skipping")

# Run again to see the FileExistsError path
try:
    with open(exclusive, "x") as f:
        f.write("should not happen\n")
except FileExistsError as e:
    print(f"  FileExistsError (second attempt): {e}")


# ──────────────────────────────────────────────────────────
# Example 15 — Directory operations
# ──────────────────────────────────────────────────────────
section("15 — Directory operations  (mkdir, listdir, rmdir)")

reports = TEMP / "reports" / "2026"
reports.mkdir(parents=True, exist_ok=True)
print(f"  Created: {reports}")

# create some dummy report files
for month in ["jan", "feb", "mar"]:
    (reports / f"{month}_report.txt").write_text(f"Report for {month}\n")

print("\n  Contents of reports/2026:")
for entry in sorted(reports.iterdir()):
    print(f"    {entry.name}")

# copy one file
shutil.copy(reports / "jan_report.txt", reports / "jan_report_backup.txt")
print(f"\n  Backup created: jan_report_backup.txt")

# remove one file
(reports / "jan_report_backup.txt").unlink()
print(f"  Backup removed")

print("\n  Final contents:")
for entry in sorted(reports.iterdir()):
    print(f"    {entry.name}")


# ──────────────────────────────────────────────────────────
# Cleanup — remove temp folder
# ──────────────────────────────────────────────────────────
shutil.rmtree(TEMP)
print(f"\n{SEP}")
print(f"  Temp folder '{TEMP}' cleaned up.")
print(f"  All 15 examples complete.")
print(SEP)
