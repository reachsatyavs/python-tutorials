# Python File Handling — Complete Chapter

A step-by-step walkthrough: from basic file read/write to using the `os` module for file system operations.

---

## Part 1: Why Do We Need Files?

Before any code — ask the class:

> "If I store your name in a variable, then close the program and run it again — does it remember your name?"

Answer: **No.** Variables live in RAM and disappear when the program ends. Files let us **persist** data on disk.

---

## Part 2: Writing to a File (the manual way)

Every file operation follows this pattern: **open → read/write → close**

```python
f = open("notes.txt", "w")
f.write("Hello, this is my first file!")
f.close()
```

Run this, then open `notes.txt` in a text editor (or run `cat notes.txt` / `type notes.txt`) to **see the file appear on disk**. This is the key "aha" moment.

---

## Part 3: Write Modes — `"w"` vs `"a"`

**`"w"` (write) — overwrites the file every time:**

```python
f = open("notes.txt", "w")
f.write("Second write\n")
f.close()
```

Run this twice. Ask: *"What happened to the first line?"* — it's gone. `"w"` always starts fresh.

**`"a"` (append) — adds to the end without erasing:**

```python
f = open("notes.txt", "a")
f.write("Appended line\n")
f.close()
```

Run this twice — both lines survive.

---

## Part 4: Reading a File — Three Ways

```python
# 1. Read entire file as one string
f = open("notes.txt", "r")
content = f.read()
f.close()
print(content)
```

```python
# 2. Read file as a list of lines
f = open("notes.txt", "r")
lines = f.readlines()
f.close()
print(lines)
```

```python
# 3. Loop through file line-by-line (memory efficient)
f = open("notes.txt", "r")
for line in f:
    print(line.strip())
f.close()
```

**Discussion:** Which method would break if the file were 10 GB? (`.read()` and `.readlines()` load everything into memory — looping does not.)

---

## Part 5: The Problem With Manual `close()`

```python
f = open("notes.txt", "w")
f.write("test")
# Forgot to close! If an error happens above, file may never close properly.
```

**The fix — `with` statement:**

```python
with open("notes.txt", "w") as f:
    f.write("test")
# File is automatically closed here, even if an error occurs inside the block
```

From this point on, **always use `with`** — it's the professional standard.

---

## Part 6: What Happens If the File Doesn't Exist?

```python
# Run this on a file that does NOT exist
with open("missing.txt", "r") as f:
    content = f.read()
```

This crashes with `FileNotFoundError`. This is the motivation for everything in Part 7.

---

## Part 7: Using the `os` Module

`open()` is a Python **builtin** — no import needed. But to check things about files/folders *before* opening them, we need the `os` module.

```python
import os
```

### 7.1 — Check if a file exists

```python
import os

filename = "notes.txt"

if os.path.exists(filename):
    print(f"{filename} exists!")
else:
    print(f"{filename} not found.")
```

### 7.2 — Tell files apart from folders

```python
import os

path = "notes.txt"

print(os.path.exists(path))   # True/False
print(os.path.isfile(path))   # is it a file?
print(os.path.isdir(path))    # is it a folder?
```

### 7.3 — List contents of a directory

```python
import os

files = os.listdir(".")   # "." = current directory
print(files)
```

Filter files vs folders:

```python
import os

for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"FILE: {item}")
    else:
        print(f"FOLDER: {item}")
```

### 7.4 — Get file size

```python
import os

size = os.path.getsize("notes.txt")
print(f"Size: {size} bytes")
```

### 7.5 — Create and remove a directory

```python
import os

os.mkdir("test_folder")          # create folder
print(os.listdir("."))           # confirm it's there

os.rmdir("test_folder")          # remove it (must be empty)
print(os.listdir("."))           # confirm it's gone
```

### 7.6 — Rename and delete a file

```python
import os

os.rename("notes.txt", "renamed_notes.txt")
print(os.listdir("."))

os.remove("renamed_notes.txt")
print(os.listdir("."))
```

Try `os.remove()` on a file that doesn't exist — it raises `FileNotFoundError` again, which ties back to Part 6.

### 7.7 — Build file paths safely

```python
import os

folder = "data"
filename = "notes.txt"

full_path = os.path.join(folder, filename)
print(full_path)
```

`os.path.join()` builds paths correctly on **both Windows (`\`) and Mac/Linux (`/`)** — never glue path strings manually.

---

## Part 8: Capstone Exercise

> Write a program that:
> 1. Asks the user for 3 favorite movies and saves them to `movies.txt` (one per line) using `with`.
> 2. Reads the file back and prints them numbered.
> 3. Checks if a folder called `backup` exists; if not, creates it with `os.mkdir()`.
> 4. Checks if `movies.txt` exists, prints its size with `os.path.getsize()`.
> 5. Moves it into `backup` using `os.rename()` + `os.path.join()`.
> 6. Lists the contents of both folders at the end to confirm.

**Quick reference table:**

| Task | Tool |
|---|---|
| Open, read, write, append a file | `open()` (builtin) |
| Check if a file exists | `os.path.exists()` |
| List files in a folder | `os.listdir()` |
| Delete a file | `os.remove()` |
| Get file size | `os.path.getsize()` |
| Create/remove a directory | `os.mkdir()` / `os.rmdir()` |
| Build cross-platform paths | `os.path.join()` |
