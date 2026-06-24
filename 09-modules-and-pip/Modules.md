# Python Modules & pip
> Python Series · Module 09 · Modules & pip · `github.com/reachsatyavs/python-tutorials`

---

## Table of Contents

1. [What is a Module — and Why?](#1-what-is-a-module--and-why)
2. [The Three Import Forms](#2-the-three-import-forms)
3. [The Standard Library — Batteries Included](#3-the-standard-library--batteries-included)
4. [Creating Your Own Module](#4-creating-your-own-module)
5. [The `__name__ == "__main__"` Guard](#5-the-__name__--__main__-guard)
6. [Packages — Folders of Modules](#6-packages--folders-of-modules)
7. [pip — Installing Third-Party Packages](#7-pip--installing-third-party-packages)
8. [Virtual Environments — `venv`](#8-virtual-environments--venv)
9. [requirements.txt — Capturing Dependencies](#9-requirementstxt--capturing-dependencies)
10. [Popular Third-Party Packages at a Glance](#10-popular-third-party-packages-at-a-glance)
11. [Quick Recap — Cheat Sheet](#11-quick-recap--cheat-sheet)

---

## 1. What is a Module — and Why?

A **module** is simply a `.py` file. Every Python file you write is already a module.

```
math.py          ← the standard-library math module
os.py            ← file-system operations
myutils.py       ← a module you write yourself
```

**Why modules exist:**

| Problem | Module solves it |
|---|---|
| One huge file is hard to read | Split into focused files |
| Copying code between projects | Import it instead |
| Sharing code with the world | Publish as a package on PyPI |
| Using other people's work | `pip install` a package |

**Module vs Package vs Library:**

| Term | What it is |
|---|---|
| **Module** | A single `.py` file |
| **Package** | A folder containing modules and an `__init__.py` file |
| **Library** | A collection of packages — the standard library, NumPy, etc. |

---

## 2. The Three Import Forms

### `import module`

```python
import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.141592653589793
print(math.floor(3.7))  # 3
```

Keeps names in the module's namespace — you always write `math.something`.

### `from module import name`

```python
from math import sqrt, pi

print(sqrt(16))   # 4.0
print(pi)         # 3.141592653589793
# math.ceil would still fail — only sqrt and pi are imported
```

Brings specific names into the local namespace.

### `import module as alias`

```python
import datetime as dt

today = dt.date.today()
print(today)
```

Useful for long module names — `numpy as np`, `pandas as pd` are the canonical examples.

### `from module import name as alias`

```python
from datetime import datetime as DateTime

now = DateTime.now()
print(now.strftime("%Y-%m-%d %H:%M"))
```

### What to avoid — `from module import *`

```python
from math import *    # ← don't do this in production code
```

Dumps every name from `math` into your namespace, which can silently overwrite your own variable names. Fine in a quick REPL session, bad in a script.

---

## 3. The Standard Library — Batteries Included

Python ships with over 200 modules. You do not need to install them — they are always available.

### Frequently used standard-library modules

| Module | What it does | Key names |
|---|---|---|
| `math` | Mathematical functions | `sqrt`, `floor`, `ceil`, `log`, `pi`, `e` |
| `os` | Operating system interface | `os.getcwd()`, `os.listdir()`, `os.environ` |
| `sys` | Python interpreter info | `sys.argv`, `sys.path`, `sys.exit()` |
| `pathlib` | Object-oriented file paths | `Path`, `.read_text()`, `.glob()` |
| `datetime` | Dates and times | `date`, `datetime`, `timedelta` |
| `random` | Random numbers | `random()`, `randint()`, `choice()`, `shuffle()` |
| `json` | JSON encode / decode | `json.load()`, `json.dump()`, `json.loads()`, `json.dumps()` |
| `csv` | CSV read / write | `csv.reader`, `csv.DictReader`, `csv.writer` |
| `collections` | Specialised containers | `Counter`, `defaultdict`, `deque`, `namedtuple` |
| `itertools` | Iterator combinators | `chain`, `product`, `combinations`, `permutations`, `islice` |
| `functools` | Higher-order functions | `reduce`, `wraps`, `lru_cache`, `partial` |
| `re` | Regular expressions | `re.match()`, `re.search()`, `re.findall()`, `re.sub()` |
| `string` | String constants | `string.ascii_letters`, `string.digits` |
| `time` | Low-level time | `time.time()`, `time.sleep()` |
| `typing` | Type hints | `List`, `Dict`, `Optional`, `Union`, `Any` |
| `copy` | Shallow / deep copy | `copy.copy()`, `copy.deepcopy()` |
| `hashlib` | Hashing functions | `hashlib.md5()`, `hashlib.sha256()` |
| `uuid` | Unique identifiers | `uuid.uuid4()` |
| `pprint` | Pretty printer | `pprint.pprint()` |
| `enum` | Enumeration types | `Enum`, `IntEnum` |
| `dataclasses` | `@dataclass` decorator | `@dataclass`, `field()` |

### A few quick examples

```python
import math
print(math.sqrt(144))           # 12.0
print(math.gcd(48, 36))         # 12

from datetime import date, timedelta
today     = date.today()
yesterday = today - timedelta(days=1)
print(today, yesterday)

from collections import Counter
words   = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts  = Counter(words)
print(counts)                   # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counts.most_common(2))    # [('apple', 3), ('banana', 2)]

import random
print(random.randint(1, 10))         # random integer between 1 and 10
print(random.choice(["a", "b", "c"]))
```

---

## 4. Creating Your Own Module

Any `.py` file is a module. You import it by its filename (without `.py`).

**File: `myutils.py`**

```python
"""
myutils.py — a small collection of reusable helpers.
"""

PI = 3.14159   # module-level constant

def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"

def circle_area(radius):
    """Return the area of a circle."""
    return PI * radius ** 2

def clamp(value, lo, hi):
    """Clamp value between lo and hi (inclusive)."""
    return max(lo, min(hi, value))
```

**File: `main.py`** (in the same folder)

```python
import myutils

print(myutils.greet("Alice"))        # Hello, Alice!
print(myutils.circle_area(5))        # 78.53975
print(myutils.clamp(120, 0, 100))    # 100
print(myutils.PI)                    # 3.14159
```

Or with selective imports:

```python
from myutils import greet, clamp

print(greet("Bob"))
print(clamp(-5, 0, 100))   # 0
```

> **Rule:** Put the module in the **same folder** as the script that imports it (or in a location Python's `sys.path` can find).

---

## 5. The `__name__ == "__main__"` Guard

When Python loads a file it sets a special variable `__name__`:

| How the file is used | `__name__` |
|---|---|
| Run directly (`python3 myutils.py`) | `"__main__"` |
| Imported by another file | `"myutils"` (the module name) |

This lets you write code that **only runs when the file is the entry point**:

```python
# myutils.py

def greet(name):
    return f"Hello, {name}!"

def circle_area(radius):
    return 3.14159 * radius ** 2

if __name__ == "__main__":
    # This block runs only when you do:  python3 myutils.py
    # It does NOT run when another file does:  import myutils
    print("--- Testing myutils ---")
    print(greet("World"))
    print(circle_area(5))
```

> **Rule:** Always protect test/demo code with `if __name__ == "__main__":`. Without it, your test code runs every time someone imports your module.

---

## 6. Packages — Folders of Modules

A **package** is a folder that contains:
1. An `__init__.py` file (can be empty)
2. One or more `.py` module files

```
myproject/
├── main.py
└── utils/              ← this is a package
    ├── __init__.py
    ├── math_helpers.py
    └── string_helpers.py
```

**Importing from a package:**

```python
# import a module from the package
import utils.math_helpers as mh
print(mh.circle_area(5))

# import a specific name
from utils.string_helpers import slugify
print(slugify("Hello World"))

# __init__.py can re-export names for convenience
# utils/__init__.py:
#   from .math_helpers import circle_area
# Then you can do:
from utils import circle_area
```

**`__init__.py`** runs when the package is first imported — use it to:
- Re-export the most-used names from sub-modules
- Run package-level initialisation
- Define `__all__` to control what `from utils import *` exposes

---

## 7. pip — Installing Third-Party Packages

`pip` is Python's package installer. It downloads packages from [PyPI](https://pypi.org/) (the Python Package Index).

### Basic pip commands

```bash
# install a package
pip install requests

# install a specific version
pip install requests==2.31.0

# install the latest version that is < 3.0
pip install "requests<3.0"

# upgrade an installed package
pip install --upgrade requests

# uninstall a package
pip uninstall requests

# list installed packages
pip list

# show details about one package
pip show requests

# search PyPI (if enabled)
pip search requests
```

> On some systems, use `pip3` instead of `pip` to ensure you are targeting Python 3.

### Where packages are installed

```bash
# see where pip installs packages (site-packages folder)
pip show requests | grep Location
```

Packages installed this way are **global** — available to every Python script on the machine. This is why virtual environments are important (next section).

---

## 8. Virtual Environments — `venv`

A **virtual environment** is an isolated Python installation for one project. It has its own `pip` and `site-packages` folder, completely separate from other projects and the system Python.

**Why you need one:**
- Project A needs `requests==2.28` and Project B needs `requests==2.31` — you cannot install both globally.
- A new project should not be affected by packages installed for a different project.
- When you share code, a `requirements.txt` from a venv gives exact reproducibility.

### Create, activate, deactivate

```bash
# create a venv called "venv" in the current folder
python3 -m venv venv

# activate (macOS / Linux)
source venv/bin/activate

# activate (Windows — Command Prompt)
venv\Scripts\activate.bat

# activate (Windows — PowerShell)
venv\Scripts\Activate.ps1

# you will see (venv) in your prompt — all pip/python commands now use the venv
(venv) $ pip install requests

# deactivate — return to system Python
(venv) $ deactivate
```

> **Rule:** Create one virtual environment per project. Never install packages with pip outside a virtual environment (except `virtualenv` or `pipx` for global tools).

---

## 9. requirements.txt — Capturing Dependencies

`requirements.txt` lists every package (and version) your project needs. It lets anyone reproduce your exact environment.

### Generate

```bash
# with the venv activated — write current packages to requirements.txt
pip freeze > requirements.txt
```

**Example `requirements.txt`:**

```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.7
requests==2.31.0
urllib3==2.2.0
```

### Install from requirements.txt

```bash
# recreate the environment on a different machine
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Keeping requirements.txt manually (simpler approach)

Many small projects maintain it by hand, listing only direct dependencies:

```
requests>=2.28
pandas>=2.0
```

Then pin exact versions only when you need strict reproducibility.

---

## 10. Popular Third-Party Packages at a Glance

| Package | `pip install` | What it does |
|---|---|---|
| `requests` | `requests` | HTTP — call REST APIs, download URLs |
| `pandas` | `pandas` | Data analysis — DataFrames, CSV, Excel |
| `numpy` | `numpy` | Numerical computing — arrays, linear algebra |
| `matplotlib` | `matplotlib` | Plotting — line, bar, scatter, histogram |
| `fastapi` | `fastapi uvicorn` | Build REST APIs quickly |
| `flask` | `flask` | Lightweight web framework |
| `sqlalchemy` | `sqlalchemy` | ORM — work with databases in Python |
| `pytest` | `pytest` | Testing framework |
| `pydantic` | `pydantic` | Data validation with type hints |
| `httpx` | `httpx` | Async-capable HTTP client |
| `rich` | `rich` | Beautiful terminal output, tables, progress bars |
| `python-dotenv` | `python-dotenv` | Load `.env` files into `os.environ` |
| `click` | `click` | Build command-line tools |
| `Pillow` | `Pillow` | Image processing |
| `openpyxl` | `openpyxl` | Read/write `.xlsx` Excel files |

---

## 11. Quick Recap — Cheat Sheet

### Import patterns

```python
import math                    # math.sqrt(4)
from math import sqrt, pi      # sqrt(4), pi
import numpy as np             # np.array([1,2,3])
from datetime import datetime as dt  # dt.now()
```

### Standard library one-liners

```python
import math;      print(math.sqrt(81))                     # 9.0
import random;    print(random.randint(1, 6))               # dice roll
import datetime;  print(datetime.date.today())              # today's date
from collections import Counter; Counter("hello")           # {'l': 2, ...}
from itertools import combinations; list(combinations([1,2,3], 2))  # [(1,2)...]
import uuid;      print(uuid.uuid4())                       # unique id
import pprint;    pprint.pprint({"a": [1,2,3], "b": "x"})  # pretty print
```

### Creating a module

```python
# mymodule.py
def hello(name): return f"Hi {name}"
PI = 3.14
if __name__ == "__main__":
    print(hello("test"))

# main.py
import mymodule
print(mymodule.hello("Alice"))
print(mymodule.PI)
```

### pip commands

```bash
pip install package         # install
pip install package==1.2.3  # specific version
pip install --upgrade pkg   # upgrade
pip uninstall package       # remove
pip list                    # show installed
pip freeze > requirements.txt   # save snapshot
pip install -r requirements.txt # restore snapshot
```

### venv workflow

```bash
python3 -m venv venv          # create
source venv/bin/activate      # activate (macOS/Linux)
pip install -r requirements.txt  # install deps
python3 main.py               # run
deactivate                    # exit
```

### Key rules

- Use `import module` to keep namespaces clean
- Always guard test code with `if __name__ == "__main__":`
- One virtual environment per project — never install globally
- Pin versions in `requirements.txt` for reproducible builds
- Prefer `pathlib` over `os.path` for file path work
- Check PyPI before writing code that already exists as a package

---

*Python Series by Satya VS · [github.com/reachsatyavs/python-tutorials](https://github.com/reachsatyavs/python-tutorials)*
