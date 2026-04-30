# Python Tutorials — Course Index

A structured collection of notes, examples, and interactive scripts for teaching Python from the ground up.

---

## Course Structure

Modules use **numbered folders** so order matches your syllabus. The full roadmap (modules 06–13 + algorithm chapters) is in [`COURSE_LAYOUT.md`](COURSE_LAYOUT.md).

| # | Directory | What it covers |
|---|-----------|----------------|
| 01 | [`01-python-intro/`](01-python-intro/README.md) | Why Python; setup and JupyterLab in this README |
| 02 | [`02-data-types/`](02-data-types/README.md) | Built-in types, mutable vs immutable, `list`, `dict`, `set`, `tuple`, `str` — notes + example scripts |
| 03 | [`03-operators/`](03-operators/README.md) | Arithmetic, comparison, logical, bitwise, identity, walrus, ternary — notes + runnable examples |
| 04 | [`04-control-flows/`](04-control-flows/README.md) | `if`/`elif`/`else`, `while`, `for`, `break`, `continue`, `match`/`case`, guard clauses |
| 05 | [`05-functions/`](05-functions/README.md) | `def`, return values, argument patterns (`*args`, `**kwargs`, `/`, `*`), lambda, builtins |
| — | [`Hashing/`](Hashing/README.md) | Supplementary: how hashing works, dict internals, thread safety, try-it scripts |

---

## Root files

| File | What it is |
|------|------------|
| `README.md` | This file — course index and setup guide |
| `COURSE_LAYOUT.md` | Numbered directory plan, algorithm hours, migration notes |
| `AI_ML_Ecosystem.md` | Overview of the Python AI/ML ecosystem |
| `LLM.md` | Notes on Large Language Models in the Python context |
| `PythonInstallation.pptx` | Setup slides for class |

---

**Why Python:** see [`01-python-intro/README.md`](01-python-intro/README.md).

---

# Python + JupyterLab Setup Guide (Windows & macOS)

This guide is optimized for teaching: **one Python per project via virtual environments**.

---

## 1) Which Python should I install?

### Recommendation (for new learners)
- Install the **latest stable CPython 3.x** from the official Python website.
- As of now, Python.org lists **Python 3.14.2** as the latest release.

> Why “latest stable”? Better security, better performance, and most libraries keep up quickly.

---

## 2) Where to install from? (Official sources)

- Official downloads: https://www.python.org/downloads/ 
- Windows-specific builds: https://www.python.org/downloads/windows/

---

## 3) Best practices when you have multiple Python versions

### Golden rules
1. **Never install packages globally** for projects.
2. **Create a virtual environment per project** (`.venv/` inside the project folder).
3. Always run tools via the active environment:
   - `python -m pip ...`
   - `python -m jupyter lab`
4. Capture dependencies:
   - `pip freeze > requirements.txt`
   - or maintain a minimal `requirements.txt` manually.

Python’s `venv` module creates isolated environments with separate site-packages.

### Simple “standard” project layout
```
my-project/
  .venv/
  src/
  requirements.txt
  README.md
```

### (Optional) Managing many Python versions
- On macOS/Linux: `pyenv` is commonly used
- On Windows: the **Python Launcher** (`py`) helps you select versions
- Newer tools exist (e.g., `uv`) for managing Python versions too (optional for beginners).

---

# WINDOWS (Step-by-step)

## A) Install Python (Windows)
1. Download from Python.org: https://www.python.org/downloads/windows/
2. During installation:
   - ✅ Select **“Add Python to PATH”**
   - ✅ Ensure `pip` is installed (default)
   - ✅ Python Launcher (`py`) is typically included with the standard installer.

## B) Verify Python
Open **PowerShell**:
```powershell
py --version
py -3 --version
```

## C) Create a project + virtual environment
```powershell
mkdir python-course
cd python-course
py -m venv .venv
```

## D) Activate the virtual environment
```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation (policy), run (once):
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## E) Upgrade pip (recommended)
```powershell
python -m pip install --upgrade pip
```

## F) Install JupyterLab inside the venv
```powershell
python -m pip install jupyterlab
```

Project Jupyter recommends `pip install jupyterlab` and launching with `jupyter lab`. 

## G) Launch JupyterLab (recommended way)
Always launch through the environment’s Python:
```powershell
python -m jupyter lab
```

---

# macOS (Step-by-step)

## A) Install Python (macOS)
### Option 1: python.org installer
- Download from: https://www.python.org/downloads/

### Option 2: Homebrew (common for developers)
```bash
brew install python
```
(Use this if you already use Homebrew and want a dev-friendly setup.)

> Note: macOS has a system Python / system tools—avoid modifying or depending on system Python for class projects.

## B) Verify Python
Open **Terminal**:
```bash
python3 --version
python3 -m pip --version
```

## C) Create a project + virtual environment
```bash
mkdir python-course
cd python-course
python3 -m venv .venv
```

## D) Activate the virtual environment
```bash
source .venv/bin/activate
```

## E) Upgrade pip (recommended)
```bash
python -m pip install --upgrade pip
```

## F) Install JupyterLab inside the venv
```bash
python -m pip install jupyterlab
```

## G) Launch JupyterLab
```bash
python -m jupyter lab
```

---

## 4) How to use JupyterLab (quick  workflow)

### Key ideas
- A **Notebook** (`.ipynb`) is split into **cells**
  - Markdown cell: notes / explanation
  - Code cell: Python code
- Common shortcuts:
  - Run cell: `Shift + Enter`
  - Add cell below: `B`
  - Add cell above: `A`
  - Change to Markdown: `M`
  - Change to Code: `Y`
- In JupyterLab:
  - Left sidebar = file browser
  - You can open multiple notebooks/tabs
  - Terminal is available inside JupyterLab (useful for `pip`, git, etc.)

---

## 5) Common issues (and quick fixes)

### “jupyter” opens the wrong Python
Use:
```bash
python -m jupyter lab
```
This forces Jupyter to run from the current environment.

### Need a Jupyter kernel linked to the venv (optional)
If you don’t see the correct kernel, do:
```bash
python -m pip install ipykernel
python -m ipykernel install --user --name python-course --display-name "Python (python-course)"
```

---

## Quick checklist (what you want everyone to know)
- Create `.venv` inside each project
- Activate it before installing packages
- Install JupyterLab inside `.venv`
- Launch with: `python -m jupyter lab`
- Save dependencies in `requirements.txt`

---

### References
- Python downloads / latest release: https://www.python.org/downloads/ 
- venv (official docs): https://docs.python.org/3/library/venv.html 
- Jupyter install page: https://jupyter.org/install 
- JupyterLab installation docs: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
