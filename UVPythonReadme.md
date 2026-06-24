# uv — Python Version & Package Manager

`uv` is a fast, modern replacement for `pip`, `pip-tools`, `virtualenv`, and `pyenv` — all in one tool. It is written in Rust and is 10–100× faster than pip for installs.

**Official docs:** https://docs.astral.sh/uv/

---

## Table of Contents

1. [Install uv](#1-install-uv)
2. [Install a Specific Python Version](#2-install-a-specific-python-version)
3. [Create a Virtual Environment](#3-create-a-virtual-environment)
4. [Activate and Deactivate the Environment](#4-activate-and-deactivate-the-environment)
5. [Install Packages](#5-install-packages)
6. [Verify Your Setup](#6-verify-your-setup)
7. [Manage Dependencies — pyproject.toml](#7-manage-dependencies--pyprojecttoml)
8. [requirements.txt Workflow with uv](#8-requirementstxt-workflow-with-uv)
9. [Useful uv Commands Reference](#9-useful-uv-commands-reference)
10. [Quick Start — Full Workflow](#10-quick-start--full-workflow)
11. [Common Issues & Fixes](#11-common-issues--fixes)

---

## 1. Install uv

### macOS / Linux (recommended — curl installer)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After install, restart your terminal or run:

```bash
source ~/.bashrc       # bash
source ~/.zshrc        # zsh (macOS default)
```

### macOS via Homebrew

```bash
brew install uv
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Verify installation

```bash
uv --version
# uv 0.x.x (...)
```

---

## 2. Install a Specific Python Version

`uv` can download and manage Python versions for you — no need for `pyenv`.

```bash
# install Python 3.12 (downloads it automatically)
uv python install 3.12

# install multiple versions
uv python install 3.11 3.12 3.13

# list all Python versions uv has installed
uv python list

# list all available versions (including ones not yet installed)
uv python list --all-versions
```

Installed Pythons are stored in `~/.local/share/uv/python/` and are available to any project.

---

## 3. Create a Virtual Environment

Always create one virtual environment per project. Run this from the project root folder.

```bash
cd /path/to/your/project

# create .venv using Python 3.12
uv venv --python 3.12

# or use whatever version is already default
uv venv
```

This creates a `.venv/` folder in your project directory.

> **Add `.venv` to your `.gitignore`** — never commit the virtual environment.
>
> ```
> .venv/
> ```

---

## 4. Activate and Deactivate the Environment

You must activate the environment before running Python or installing packages.

### Activate

```bash
# macOS / Linux
source .venv/bin/activate

# Windows — Command Prompt
.venv\Scripts\activate.bat

# Windows — PowerShell
.venv\Scripts\Activate.ps1
```

Your prompt changes to show `(.venv)` when active:

```
(.venv) ssri@mac python-tutorials %
```

### Deactivate

```bash
deactivate
```

### Check which Python is active

```bash
which python
# → /path/to/project/.venv/bin/python   ← correct, inside venv

python --version
# → Python 3.12.x
```

---

## 5. Install Packages

With the venv **activated**, use `uv pip` instead of `pip`:

```bash
# install a package
uv pip install requests

# install multiple packages
uv pip install requests pandas numpy

# install a specific version
uv pip install "requests==2.31.0"

# install from requirements.txt
uv pip install -r requirements.txt

# upgrade a package
uv pip install --upgrade requests

# uninstall a package
uv pip uninstall requests

# list installed packages
uv pip list

# show info about a package
uv pip show requests
```

### Install Jupyter Lab

```bash
uv pip install jupyterlab

# launch
jupyter lab
```

### Install common data science stack

```bash
uv pip install jupyterlab pandas numpy matplotlib
```

---

## 6. Verify Your Setup

Run these checks after creating and activating your environment:

```bash
# 1. Confirm you are inside the venv
which python
# should show .venv/bin/python

# 2. Confirm the Python version
python --version
# Python 3.12.x

# 3. Confirm uv sees the right pip
uv pip list

# 4. Confirm sys.executable from inside Python
python -c "import sys; print(sys.executable)"
# /path/to/project/.venv/bin/python

# 5. Confirm a specific package is installed
python -c "import requests; print(requests.__version__)"
```

---

## 7. Manage Dependencies — pyproject.toml

For more structured projects, `uv` can manage a `pyproject.toml` — the modern standard for Python project metadata.

### Initialise a new project

```bash
uv init my-project
cd my-project
```

This creates:

```
my-project/
├── pyproject.toml    ← project metadata + dependencies
├── .python-version   ← pins the Python version
├── README.md
└── main.py
```

### Add dependencies (updates pyproject.toml automatically)

```bash
uv add requests
uv add "pandas>=2.0"
uv add jupyterlab --dev       # dev-only dependency
```

### Remove a dependency

```bash
uv remove requests
```

### Sync environment to match pyproject.toml

```bash
uv sync
```

### `pyproject.toml` example

```toml
[project]
name = "python-tutorials"
version = "1.0.0"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.31",
    "pandas>=2.0",
]

[project.optional-dependencies]
dev = [
    "jupyterlab",
    "pytest",
]
```

---

## 8. requirements.txt Workflow with uv

If you prefer the traditional `requirements.txt` approach:

### Generate requirements.txt from the current venv

```bash
uv pip freeze > requirements.txt
```

### Install from requirements.txt

```bash
uv pip install -r requirements.txt
```

### Compile a locked requirements file (reproducible builds)

```bash
# generate requirements.txt from pyproject.toml with exact pinned versions
uv pip compile pyproject.toml -o requirements.txt
```

---

## 9. Useful uv Commands Reference

### Python management

| Command | What it does |
|---|---|
| `uv python install 3.12` | Download and install Python 3.12 |
| `uv python list` | List installed Python versions |
| `uv python list --all-versions` | List all available versions |
| `uv python pin 3.12` | Write `.python-version` to pin this project to 3.12 |
| `uv python find` | Show which Python uv would use right now |

### Virtual environment

| Command | What it does |
|---|---|
| `uv venv` | Create `.venv` with the default Python |
| `uv venv --python 3.12` | Create `.venv` pinned to Python 3.12 |
| `source .venv/bin/activate` | Activate (macOS/Linux) |
| `deactivate` | Deactivate |

### Package management

| Command | What it does |
|---|---|
| `uv pip install pkg` | Install a package |
| `uv pip install -r requirements.txt` | Install from file |
| `uv pip uninstall pkg` | Remove a package |
| `uv pip list` | List installed packages |
| `uv pip show pkg` | Show package details |
| `uv pip freeze` | Print pinned versions (for requirements.txt) |
| `uv pip freeze > requirements.txt` | Save snapshot |

### Project (pyproject.toml) workflow

| Command | What it does |
|---|---|
| `uv init` | Initialise a new project |
| `uv add requests` | Add a dependency |
| `uv remove requests` | Remove a dependency |
| `uv sync` | Install all deps from pyproject.toml |
| `uv lock` | Create / update `uv.lock` |
| `uv run python main.py` | Run a script inside the project env without activating |

---

## 10. Quick Start — Full Workflow

Everything from scratch for the **python-tutorials** project:

```bash
# 1. install uv (if not already)
brew install uv

# 2. install Python 3.12
uv python install 3.12

# 3. go to the project folder
cd /Users/ssri/satya/python_tutor/python-tutorials

# 4. create the virtual environment
uv venv --python 3.12

# 5. activate it
source .venv/bin/activate

# 6. install packages
uv pip install jupyterlab pandas numpy matplotlib

# 7. verify
python --version        # Python 3.12.x
uv pip list             # shows installed packages

# 8. launch Jupyter Lab
jupyter lab

# 9. when done, deactivate
deactivate
```

**Every new terminal session:** you only need to run step 5 (activate). Steps 1–4 are one-time setup.

```bash
cd /Users/ssri/satya/python_tutor/python-tutorials
source .venv/bin/activate
jupyter lab
```

---

## 11. Common Issues & Fixes

### `uv: command not found`

```bash
# add uv to PATH — paste into ~/.zshrc
export PATH="$HOME/.cargo/bin:$HOME/.local/bin:$PATH"
source ~/.zshrc
```

### `python: command not found` (only `python3` works)

```bash
# inside the venv, python always works
source .venv/bin/activate
python --version    # works now
```

### Activated venv but still shows system Python

```bash
# check that activation worked
echo $VIRTUAL_ENV
# should print:  /path/to/project/.venv

# if empty, activate again
source .venv/bin/activate
```

### Package installed but `import` fails

```bash
# make sure you are in the venv where you installed it
which python    # must point to .venv/bin/python
uv pip list     # must show the package
```

### `jupyter lab` opens but wrong kernel

Inside Jupyter Lab, go to **Kernel → Change Kernel** and select the kernel that matches `.venv`. If the kernel is missing:

```bash
uv pip install ipykernel
python -m ipykernel install --user --name=python312 --display-name "Python 3.12 (tutorials)"
```

Then restart Jupyter Lab and select **Python 3.12 (tutorials)** as the kernel.

---

*Python Series by Satya VS · [github.com/reachsatyavs/python-tutorials](https://github.com/reachsatyavs/python-tutorials)*
