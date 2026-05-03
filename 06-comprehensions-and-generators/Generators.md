# Python Generators
> Python Series · Module 06 · Generators · `github.com/reachsatyavs/python-tutorials`

---

## Table of Contents
1. [What is a Generator?](#1-what-is-a-generator)
2. [yield vs return](#2-yield-vs-return)
3. [Generator as Iterator — next()](#3-generator-as-iterator--next)
4. [Generator Expression ( )](#4-generator-expression--)
5. [Why Generators? — Memory & Speed](#5-why-generators--memory--speed)
6. [Use Case 1 — Large File Processing](#6-use-case-1--large-file-processing)
7. [Use Case 2 — Infinite Sequences](#7-use-case-2--infinite-sequences)
8. [Use Case 3 — Data Pipelines](#8-use-case-3--data-pipelines)
9. [Use Case 4 — Pagination / Streaming](#9-use-case-4--pagination--streaming)
10. [Use Case 5 — Fibonacci on Demand](#10-use-case-5--fibonacci-on-demand)
11. [send() — Two-way Communication](#11-send--two-way-communication)
12. [yield from — Delegating Generators](#12-yield-from--delegating-generators)
13. [Quick Recap — Cheat Sheet](#13-quick-recap--cheat-sheet)

---

## 1. What is a Generator?

A **generator** is a special type of function that uses `yield` instead of `return`. Instead of computing all values at once and returning them, it produces values **one at a time**, pausing after each `yield` and resuming from the same point when asked for the next value.

```python
def simple_gen():
    print("→ step 1")
    yield 10
    print("→ step 2")
    yield 20
    print("→ step 3")
    yield 30

gen = simple_gen()
print(type(gen))        # <class 'generator'>

print(next(gen))        # → step 1 runs, yields 10
print(next(gen))        # → step 2 runs, yields 20
print(next(gen))        # → step 3 runs, yields 30
```

Key properties:
- Calling a generator function does **not** run it — it returns a generator object
- The body runs only when `next()` is called
- Execution **pauses** at each `yield` and **resumes** from the same point

---

## 2. yield vs return

| | `return` | `yield` |
|---|---|---|
| Runs the function | Completely, all at once | One step at a time |
| Returns | One value, then done | One value, then pauses |
| Can resume? | No | Yes |
| Memory | All results built upfront | One value in memory at a time |
| Type returned | The value itself | A generator object |

```python
# return — runs fully, builds everything, done
def get_numbers_return():
    return [1, 2, 3, 4, 5]

result = get_numbers_return()   # list built immediately
print(result)                   # [1, 2, 3, 4, 5]


# yield — pauses after each value, resumes on demand
def get_numbers_yield():
    for i in range(1, 6):
        yield i

gen = get_numbers_yield()       # nothing runs yet
for val in gen:
    print(val)                  # 1, 2, 3, 4, 5 — one at a time
```

---

## 3. Generator as Iterator — next()

Every generator is an **iterator** — it implements `__next__()` internally. You can call `next()` manually or let a `for` loop handle it.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

cd = countdown(3)
print(next(cd))   # 3
print(next(cd))   # 2
print(next(cd))   # 1

try:
    print(next(cd))
except StopIteration:
    print("Generator exhausted")  # raised when no more values
```

A `for` loop handles `StopIteration` automatically — it stops cleanly when the generator is exhausted.

```python
for val in countdown(5):
    print(val)    # 5, 4, 3, 2, 1
```

---

## 4. Generator Expression `( )`

A one-line generator — same syntax as list comprehension but with `( )` instead of `[ ]`.

```python
# list comprehension — all values built immediately
sq_list = [x**2 for x in range(10)]

# generator expression — nothing computed yet
sq_gen  = (x**2 for x in range(10))

print(type(sq_list))   # <class 'list'>
print(type(sq_gen))    # <class 'generator'>

# consume it
print(list(sq_gen))    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Generator expressions work directly inside `sum()`, `max()`, `min()`, `any()`, `all()`:

```python
total = sum(x**2 for x in range(1_000_000))   # no list built!
```

---

## 5. Why Generators? — Memory & Speed

### Memory comparison

```python
import sys

n = 1_000_000

big_list = [x for x in range(n)]
big_gen  = (x for x in range(n))

print(sys.getsizeof(big_list))   # ~8,448,728 bytes  (8 MB)
print(sys.getsizeof(big_gen))    #         192 bytes
```

A generator for 1 million items uses **192 bytes** regardless of size. The list uses **8 MB**. The generator is ~44,000x more memory efficient.

### Speed comparison

```python
import time

t0 = time.perf_counter()
sum([x**2 for x in range(1_000_000)])   # list: ~250ms
t1 = time.perf_counter()

t2 = time.perf_counter()
sum(x**2 for x in range(1_000_000))     # generator: ~55ms
t3 = time.perf_counter()
```

Generator is faster too — no time wasted building and then scanning a list.

---

## 6. Use Case 1 — Large File Processing

Reading an entire large file into memory crashes programs. Generators read one line at a time.

```python
def read_students(filepath):
    """Yields one student dict at a time — never loads whole file."""
    with open(filepath) as f:
        for line in f:
            name, score = line.strip().split(",")
            yield {"name": name, "score": int(score)}

for student in read_students("students.txt"):
    status = "PASS" if student["score"] >= 60 else "FAIL"
    print(f"{student['name']:10} {student['score']}  {status}")
```

```python
# Count lines in any size file — constant memory
def line_count(filepath):
    return sum(1 for _ in open(filepath))
```

Memory stays **constant** regardless of file size — 10 KB or 10 GB, same RAM usage.

---

## 7. Use Case 2 — Infinite Sequences

A list cannot be infinite. A generator can model sequences that never end — you just take what you need.

```python
def infinite_counter(start=0, step=1):
    n = start
    while True:         # infinite — safe because of yield
        yield n
        n += step

counter = infinite_counter(start=10, step=5)
first6  = [next(counter) for _ in range(6)]
print(first6)   # [10, 15, 20, 25, 30, 35]
```

Use `itertools.islice` to take a slice from an infinite generator:

```python
from itertools import islice

def evens():
    n = 0
    while True:
        yield n
        n += 2

print(list(islice(evens(), 10)))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

## 8. Use Case 3 — Data Pipelines

Chain generators together — each stage processes one item at a time. Nothing runs until the final stage is consumed.

```python
raw_data = ["  42 ", "hello", " 17", "99", " bad ", "55 ", "abc"]

def parse_numbers(records):
    """Stage 1: strip and keep only numeric strings."""
    for r in records:
        stripped = r.strip()
        if stripped.isdigit():
            yield int(stripped)

def filter_high(numbers, threshold=50):
    """Stage 2: keep only values above threshold."""
    for n in numbers:
        if n > threshold:
            yield n

def double(numbers):
    """Stage 3: double each value."""
    for n in numbers:
        yield n * 2

# chain — nothing runs until list() triggers consumption
stage1 = parse_numbers(raw_data)
stage2 = filter_high(stage1, threshold=50)
stage3 = double(stage2)

print(list(stage3))   # [198, 110]
```

This is how tools like `pandas`, `dask`, and `spark` process data — lazy evaluation, chained stages.

---

## 9. Use Case 4 — Pagination / Streaming

```python
def paginate(data, page_size):
    """Yields one page (chunk) at a time."""
    for i in range(0, len(data), page_size):
        yield data[i : i + page_size]

records = list(range(1, 22))   # 21 records

for page_num, page in enumerate(paginate(records, page_size=5), start=1):
    print(f"Page {page_num}: {page}")

# Page 1: [1, 2, 3, 4, 5]
# Page 2: [6, 7, 8, 9, 10]
# Page 3: [11, 12, 13, 14, 15]
# Page 4: [16, 17, 18, 19, 20]
# Page 5: [21]
```

The same pattern works for streaming API responses, database cursors, and network packets — process each batch as it arrives without buffering everything.

---

## 10. Use Case 5 — Fibonacci on Demand

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib    = fibonacci()
first12 = [next(fib) for _ in range(12)]
print(first12)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# find the first Fibonacci number exceeding 1000
fib   = fibonacci()
large = next(f for f in fib if f > 1000)
print(large)   # 1597
```

---

## 11. send() — Two-way Communication

A generator can **receive** values too — `send()` passes a value in and `yield` receives it.

```python
def running_total():
    total = 0
    while True:
        value = yield total   # sends total OUT, receives value IN
        if value is None:
            break
        total += value

rt = running_total()
next(rt)                      # prime the generator (always required first)
print(rt.send(10))            # total = 10
print(rt.send(25))            # total = 35
print(rt.send(15))            # total = 50
```

> **Important:** Always call `next(gen)` once before `send()` — this primes the generator to reach the first `yield`.

---

## 12. yield from — Delegating Generators

`yield from` lets one generator delegate to another — cleaner than a manual loop.

```python
def inner():
    yield "A"
    yield "B"
    yield "C"

def outer():
    yield "start"
    yield from inner()     # delegate — no manual loop needed
    yield "end"

print(list(outer()))
# ['start', 'A', 'B', 'C', 'end']
```

A powerful use — recursive flattening of nested lists:

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # recurse
        else:
            yield item

data   = [1, [2, 3], [4, [5, 6]], 7]
result = list(flatten(data))
print(result)   # [1, 2, 3, 4, 5, 6, 7]
```

---

## 13. Quick Recap — Cheat Sheet

### yield vs return

| | `return` | `yield` |
|---|---|---|
| Runs | All at once | One step at a time |
| Resumes? | No | Yes |
| Returns | Value | Generator object |
| Memory | All upfront | One at a time |

### Generator syntax

```python
# generator function
def gen():
    yield value

# generator expression
g = (expr for x in it if cond)

# next — pull one value
next(g)

# send — push a value in
g.send(value)

# yield from — delegate
yield from other_gen()
```

### When to use generators

| Situation | Use generator? |
|---|---|
| Large file / dataset | ✅ yes — constant memory |
| Infinite sequence | ✅ yes — only `yield` can do this |
| Data pipeline / stages | ✅ yes — lazy chaining |
| Streaming / pagination | ✅ yes — process batch by batch |
| Need list indexing `[i]` | ❌ no — use a list |
| Iterate more than once | ❌ no — generators exhaust after one pass |

### Key rules

- A generator can only be iterated **once** — to iterate again, create a new generator
- `for` loops handle `StopIteration` automatically
- Always `next(gen)` once before `send()` to prime it
- Generator expressions `( )` are the quick one-liner form
- `yield from` replaces a manual `for` loop when delegating

---

*Python Series by Satya VS · [github.com/reachsatyavs/python-tutorials](https://github.com/reachsatyavs/python-tutorials)*
