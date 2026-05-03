# Python Comprehensions
> Python Series · Module 06 · Comprehensions & generators · `github.com/reachsatyavs/python-tutorials`

---

## Table of Contents
1. [What is a Comprehension?](#1-what-is-a-comprehension)
2. [Why Do We Need Comprehensions?](#2-why-do-we-need-comprehensions)
3. [List Comprehension `[ ]`](#3-list-comprehension--)
4. [Set Comprehension `{ }`](#4-set-comprehension--)
5. [Dict Comprehension `{ k:v }`](#5-dict-comprehension--kv-)
6. [Generator Expression `( )`](#6-generator-expression--)
7. [All 4 Types — Side by Side](#7-all-4-types--side-by-side)
8. [The Mental Model](#8-the-mental-model)
9. [Why No Tuple Comprehension?](#9-why-no-tuple-comprehension)
10. [Input: Any Iterable · Output: Fixed by Brackets](#10-input-any-iterable--output-fixed-by-brackets)
11. [When NOT to Use Comprehensions](#11-when-not-to-use-comprehensions)
12. [Quick Recap — Cheat Sheet](#12-quick-recap--cheat-sheet)

---

## 1. What is a Comprehension?

> A comprehension is a **concise, readable way to build a collection** (list, set, or dict) from an existing iterable — all in a single expression.

### Without it vs With it

| Without | With |
|---|---|
| 3–4 lines | 1 line |
| Create empty list | Expression |
| `for` loop | `for` clause |
| `.append()` | optional `if` |

### The anatomy — just 3 parts

```python
[ expression    for item in iterable    if condition ]
#  ↑                  ↑                      ↑
#  what to produce    the loop          optional filter
```

- **Expression** — what to produce for each item
- **for clause** — the loop variable and source
- **if condition** — optional filter (only items passing this are included)

---

## 2. Why Do We Need Comprehensions?

### Side by side

```python
# Traditional for-loop — 3 lines
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# List comprehension — 1 line
squares = [n**2 for n in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

Same result. Same logic. Half the lines.

### 4 reasons to use comprehensions

| Reason | Detail |
|---|---|
| **Less code** | 3 lines → 1 line |
| **Faster** | Runs at C speed internally |
| **Readable** | Reads like English |
| **Pythonic** | The community-accepted way |

---

## 3. List Comprehension `[ ]`

**Returns:** `list` · Ordered · Allows duplicates

```python
[ expression    for item in iterable    if condition ]
```

### Pattern 1 — Transform every item

```python
names = ['rajeev', 'priya', 'arun']
upper = [n.upper() for n in names]
# ['RAJEEV', 'PRIYA', 'ARUN']
```

### Pattern 2 — Filter with `if`

```python
scores = [45, 82, 60, 91, 38, 74]
passed = [s for s in scores if s >= 60]
# [82, 60, 91, 74]
```

### Pattern 3 — Transform + Filter (`if-else` in expression)

```python
marks  = [45, 82, 60, 91, 38]
grades = ["pass" if m >= 60 else "fail" for m in marks]
# ['fail', 'pass', 'pass', 'pass', 'fail']
```

### Real-world — data cleaning

```python
students = [
    {"name": "  Rajeev ", "score": 82},
    {"name": "Priya",     "score": 45},
    {"name": " Arun  ",   "score": 91},
]

# clean names + filter only passed
toppers = [s["name"].strip() for s in students if s["score"] >= 60]
# ['Rajeev', 'Arun']

# build report dict per student
report = [
    {"name": s["name"].strip(), "grade": "A" if s["score"] >= 80 else "B"}
    for s in students if s["score"] >= 60
]
# [{'name': 'Rajeev', 'grade': 'A'}, {'name': 'Arun', 'grade': 'A'}]
```

> **Key rule:**
> - `if` at the **end** → filter (some items dropped)
> - `if-else` in the **expression** → transform all items differently (nothing dropped)

---

## 4. Set Comprehension `{ }`

**Returns:** `set` · Unordered · No duplicates

```python
{ expression    for item in iterable    if condition }
```

Same syntax as list comprehension — just swap `[ ]` for `{ }`. Duplicates are automatically removed. Order is **not** guaranteed.

### Example 1 — Deduplicate

```python
cities = ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai"]

unique = {c.upper() for c in cities}
# {'DELHI', 'MUMBAI', 'BANGALORE'}  ← no duplicates, order may vary
```

### Example 2 — Unique first letters

```python
letters = {c[0] for c in cities}
# {'D', 'M', 'B'}
```

### When to use set comprehension

- You want **unique values** only
- **Deduplication** is needed
- **Order doesn't matter**

> **Quick rule:** `[ ]` keeps duplicates · `{ }` removes duplicates

---

## 5. Dict Comprehension `{ k:v }`

**Returns:** `dict` · Key-value pairs

```python
{ key: value    for item in iterable    if condition }
```

Same curly braces as set — but the **colon (`:`)** tells Python "this is a dict, not a set".

### Pattern 1 — Zip two lists into a dict

```python
students = ["Rajeev", "Priya", "Arun"]
scores   = [82, 91, 74]

result = {name: score for name, score in zip(students, scores)}
# {'Rajeev': 82, 'Priya': 91, 'Arun': 74}
```

### Pattern 2 — Invert a dict (swap key ↔ value)

```python
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

### Pattern 3 — Filter a dict

```python
data    = {"Rajeev": 82, "Priya": 45, "Arun": 91}
toppers = {k: v for k, v in data.items() if v >= 60}
# {'Rajeev': 82, 'Arun': 91}
```

> The colon is the **only** difference between `{ x ... }` (set) and `{ k:v ... }` (dict).

---

## 6. Generator Expression `( )`

**Returns:** `generator` object · Lazy · Memory-efficient

```python
( expression    for item in iterable    if condition )
```

Parentheses instead of brackets. Values are computed **one at a time, only when asked**. Nothing is stored in memory upfront.

### List vs Generator

```python
# list — ALL values built immediately in memory
sq_list = [x**2 for x in range(10)]
print(sq_list)        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(type(sq_list))  # <class 'list'>

# generator — nothing computed yet
sq_gen = (x**2 for x in range(10))
print(sq_gen)         # <generator object <genexpr> at 0x...>
print(type(sq_gen))   # <class 'generator'>

# pull one value at a time with next()
print(next(sq_gen))   # 0  ← computed NOW
print(next(sq_gen))   # 1  ← computed NOW
```

### Most common use — pass directly to `sum()`, `max()`, `any()`

```python
# never stores 1 million values in memory!
total = sum(x**2 for x in range(1_000_000))
print(total)  # 333332833333500000
```

### When to use List `[ ]` vs Generator `( )`

| List `[ ]` | Generator `( )` |
|---|---|
| Builds full list in RAM | Computes on demand |
| Use when you need indexing | Memory-efficient for large data |
| Use when you loop multiple times | Use with `sum` / `max` / `min` / `any` / `all` |
| Can iterate multiple times | Can only iterate **once** |

> **Rule:** Passing to `sum()` / `max()` / `any()`? → use `( )` not `[ ]` — no need to build the full list first.

---

## 7. All 4 Types — Side by Side

| Type | Syntax | Returns | Key property | Use case |
|---|---|---|---|---|
| List `[ ]` | `[expr for x in it]` | `list` | Ordered · allows duplicates | General transformation |
| Set `{ }` | `{expr for x in it}` | `set` | Unordered · no duplicates | Deduplication |
| Dict `{ k:v }` | `{k:v for x in it}` | `dict` | Key-value pairs | Build / invert / filter dicts |
| Generator `( )` | `(expr for x in it)` | `generator` | Lazy · memory-efficient | Large data, `sum`/`max`/`any` |

---

## 8. The Mental Model

> How every comprehension works — regardless of type

```
ANY iterable          →   brackets              →   fixed output type
─────────────────         ──────────────────        ─────────────────────────
list, str, tuple,         [ ]   →  list             list      ordered, duplicates ok
range, dict, set,         { }   →  set              set       unique values only
file, generator...        {k:v} →  dict             dict      key → value pairs
                          ( )   →  generator         generator lazy, one at a time
```

- **Input side** — any iterable goes in. If Python can `for` loop over it, it works.
- **Middle** — you pick the bracket. That is the **only** decision.
- **Output side** — determined entirely by which bracket you chose.

> **The bracket is the only decision you make — everything else follows from it.**

---

## 9. Why No Tuple Comprehension?

### Reason 1 — `( )` is already taken

Parentheses are claimed by **generator expressions**.

```python
(x**2 for x in range(5))  # → generator, NOT a tuple
```

There is no bracket left to assign to tuple comprehension.

### Reason 2 — Immutability (partially)

Immutability does **not** prevent creation — `tuple([1,2,3])` works fine.
But there is no point adding a new syntax just for tuple when `tuple(generator)` already does the job cleanly.

```python
# ❌ no such syntax exists
# (x**2 for x in range(5))  ← this is a GENERATOR

# ✅ correct way to get a tuple
t = tuple(x**2 for x in range(5))
print(t)        # (0, 1, 4, 9, 16)
print(type(t))  # <class 'tuple'>
```

### Has comprehension? — Full table

| Type | Syntax | Has comprehension? |
|---|---|---|
| `list` | `[x for x in it]` | ✅ yes |
| `set` | `{x for x in it}` | ✅ yes |
| `dict` | `{k:v for x in it}` | ✅ yes |
| `generator` | `(x for x in it)` | ✅ yes — this IS the `( )` syntax |
| `tuple` | `tuple(x for x in it)` | ❌ no native syntax — wrap a generator |
| `string` | `"".join(x for x in it)` | ❌ no native syntax — use `join()` |

> `( )` is claimed by generator — tuple and string have no native comprehension syntax.

---

## 10. Input: Any Iterable · Output: Fixed by Brackets

> If Python can loop over it with `for` → you can use it as source in a comprehension.

### Any iterable as INPUT

| Iterable | Example |
|---|---|
| `list` | `[x for x in [1,2,3]]` |
| `str` | `[ch for ch in "hello"]` |
| `range` | `[x for x in range(5)]` |
| `tuple` | `[x for x in (1,2,3)]` |
| `dict` | `[k for k in {"a":1}]` |
| `set` | `[x for x in {1,2,3}]` |
| `file` | `[line for line in open("f.txt")]` |

### String — the special case

**String AS INPUT — works perfectly ✅**

```python
# extract vowels
vowels = [ch for ch in "hello world" if ch in "aeiou"]
# ['e', 'o', 'o']

# uppercase each character
upper = [ch.upper() for ch in "hello"]
# ['H', 'E', 'L', 'L', 'O']
```

**String AS OUTPUT — no native syntax ❌**

```python
# ✅ use join() instead
it = "helow word"
y  = "".join(x + "-" for x in it)
print(y)  # h-e-l-o-w- -w-o-r-d-
```

`"".join(...)` is not a comprehension — it is a **string method** that accepts any iterable, including a generator expression.

> String is iterable as **INPUT** — but `join()` is needed to get a string **OUTPUT**.

---

## 11. When NOT to Use Comprehensions

> **Golden rule:** If it doesn't fit on 1–2 readable lines, use a regular `for` loop instead.

### ❌ Avoid — side effects inside comprehension

```python
# wrong — comprehensions are not for side effects
[print(x) for x in range(5)]

# correct — use a plain loop for side effects
for x in range(5):
    print(x)
```

### ❌ Avoid — too complex to read

```python
# wrong — too many conditions, hard to read
result = [f(x) if g(x) > 0 else h(x) for x in data if p(x) and q(x)]

# correct — break it into a loop when logic grows
result = []
for x in data:
    if p(x) and q(x):
        result.append(f(x) if g(x) > 0 else h(x))
```

### Three don'ts

| Don't | Why |
|---|---|
| Side effects inside | `print()`, `write()`, `.append()` with external state |
| Deeply nested | More than 2 `for` clauses gets unreadable fast |
| Complex logic | If you need a comment to explain it, use a loop |

> **Comprehensions are for BUILDING collections — not for running side effects.**

---

## 12. Quick Recap — Cheat Sheet

### Syntax table

| Type | Syntax | Returns | Key property |
|---|---|---|---|
| List `[ ]` | `[expr for x in it if cond]` | `list` | Ordered, keeps duplicates |
| Set `{ }` | `{expr for x in it if cond}` | `set` | Unordered, no duplicates |
| Dict `{ k:v }` | `{k:v for x in it if cond}` | `dict` | Key-value pairs |
| Generator `( )` | `(expr for x in it if cond)` | `generator` | Lazy — computes on demand |

### Key takeaways

- `[ ]` list · `{ }` set · `{ k:v }` dict · `( )` generator — just change the brackets
- All share the same `for...if` clause structure
- Generator is lazy — use it with `sum()` / `max()` / `any()` for large data
- Too complex to read in one line? Use a regular `for` loop instead
- Input can be **any iterable** — string, tuple, range, file, generator...
- Tuple and string have **no native comprehension output syntax**

---

*Python Series by Satya VS · [github.com/reachsatyavs/python-tutorials](https://github.com/reachsatyavs/python-tutorials)*
