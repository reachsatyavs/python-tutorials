# Python Generators
> Python Series · Module 06 · Generators · `github.com/reachsatyavs/python-tutorials`

---

## Table of Contents
1. [What is a Generator?](#1-what-is-a-generator)
2. [yield vs return](#2-yield-vs-return)
3. [Generator as Iterator — next()](#3-generator-as-iterator--next)
4. [Generator Expression ( )](#4-generator-expression--)
5. [sum() with Generators vs List Comprehensions](#5-sum-with-generators-vs-list-comprehensions)
6. [Why Generators? — Memory & Speed](#6-why-generators--memory--speed)
7. [Generator vs range — Key Differences](#7-generator-vs-range--key-differences)
8. [Use of Generators — 7 Practical Uses](#8-use-of-generators--7-practical-uses)
9. [Use Case 1 — Large File Processing](#9-use-case-1--large-file-processing)
10. [Use Case 2 — Infinite Sequences](#10-use-case-2--infinite-sequences)
11. [Use Case 3 — Data Pipelines](#11-use-case-3--data-pipelines)
12. [Use Case 4 — Pagination / Streaming](#12-use-case-4--pagination--streaming)
13. [Use Case 5 — Fibonacci on Demand](#13-use-case-5--fibonacci-on-demand)
14. [send() — Two-way Communication](#14-send--two-way-communication)
15. [yield from — Delegating Generators](#15-yield-from--delegating-generators)
16. [Quick Recap — Cheat Sheet](#16-quick-recap--cheat-sheet)

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

**How to tell them apart — just the brackets:**

| Syntax | Type | Behaviour |
|---|---|---|
| `(x**2 for x in range(10))` | `generator` | Lazy — one value at a time |
| `[x**2 for x in range(10)]` | `list` | Eager — all values in memory now |

---

## 5. `sum()` with Generators vs List Comprehensions

**Generators are preferred when passing directly to `sum`, `max`, `min`, `any`, `all`.**

```python
# Generator expression — lazy (preferred)
total = sum(x**2 for x in range(1_000_000))

# List comprehension — eager (avoid for large data)
total = sum([x**2 for x in range(1_000_000)])
```

Both give the same answer. The memory behaviour is completely different:

```python
import sys

gen = (x**2 for x in range(1_000_000))
lst = [x**2 for x in range(1_000_000)]

print(sys.getsizeof(gen))   # 104 bytes
print(sys.getsizeof(lst))   # 8448728 bytes  (~8 MB)
```

> **Rule:** If you are passing directly into `sum()`, `max()`, `min()`, `any()`, or `all()` — always use a generator expression `( )`. There is no reason to build the full list first.

```python
# All of these work with a generator expression — no list needed
total   = sum(e["salary"] for e in employees)
highest = max(e["salary"] for e in employees)
any_rich = any(e["salary"] > 100_000 for e in employees)
all_pass = all(score >= 60 for score in scores)
```

---

## 6. Why Generators? — Memory & Speed

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

## 7. Generator vs `range` — Key Differences

Both are **lazy** — they produce values on demand without storing them all in memory. But they are different types with different capabilities.

```python
r = range(10)
print(type(r))               # <class 'range'>

g = (x**2 for x in range(10))
print(type(g))               # <class 'generator'>
```

### Side-by-side comparison

| Feature | `range` | Generator |
|---|---|---|
| Lazy (computes on demand) | ✅ | ✅ |
| One value at a time | ✅ | ✅ |
| **Can iterate again** | ✅ reusable | ❌ exhausted after first use |
| **Supports `len()`** | ✅ | ❌ |
| **Supports indexing `[i]`** | ✅ | ❌ |
| **Can be infinite** | ❌ | ✅ |
| **Custom logic per value** | ❌ only integers | ✅ any expression |

### Key difference — reusability

```python
# range — can iterate multiple times
r = range(5)
for i in r: print(i, end=" ")    # 0 1 2 3 4
for i in r: print(i, end=" ")    # 0 1 2 3 4  ✅ works again

# generator — one time only
g = (x**2 for x in range(5))
for i in g: print(i, end=" ")    # 0 1 4 9 16
for i in g: print(i, end=" ")    # (nothing)  ❌ already exhausted
```

### Mental model

```
range      →  lazy integer sequence  (reusable, has length, has index, integers only)
generator  →  lazy value stream      (one-time, no length, no index, any logic/type)
```

### When to use which

| You need | Use |
|---|---|
| Integers from A to B with a step | `range` |
| Iterate the same sequence more than once | `range` or list |
| Access by index `seq[3]` | `range` or list |
| Values produced by custom logic | Generator |
| Infinite sequence | Generator |
| Transform or filter items on the fly | Generator |
| Memory-efficient one-pass processing | Generator |

---

## 8. Use of Generators — 7 Practical Uses

> A generator is not just a memory trick.
> It is the right tool whenever you need to **produce values one at a time** instead of building everything upfront.

### At a glance

| Use | Problem it solves | Key idea |
|---|---|---|
| **Large file / dataset** | Cannot load the whole file into RAM | Read and yield one line at a time |
| **Infinite sequence** | A list cannot be infinite | `while True: yield` — take only what you need |
| **Data pipeline** | Multi-step transform without intermediate lists | Chain generators — nothing runs until consumed |
| **Pagination / streaming** | Process results in batches, not all at once | Yield one page/chunk at a time |
| **On-demand values** | Produce the next value only when asked | Generator remembers state between calls |
| **Database rows** | Cannot load millions of DB rows into memory | Yield one row at a time from the cursor |
| **ML / AI batches** | GPU memory cannot hold the full dataset | Yield one batch at a time during training |

---

### Use 1 — Large data without running out of memory

```python
# Without generator — loads every line into a list first (dangerous for big files)
lines = open("sales.csv").readlines()   # could be millions of lines

# With generator — reads one line at a time, constant memory
def read_csv(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip().split(",")

for row in read_csv("sales.csv"):
    print(row[0], row[1])   # process one row, then move on
```

Memory used = one row at a time, regardless of file size.

---

### Use 2 — Infinite sequences

```python
# A list of "all even numbers" is impossible.
# A generator can model it — you just take what you need.

def even_numbers():
    n = 0
    while True:          # runs forever — safe because of yield
        yield n
        n += 2

evens = even_numbers()
print(next(evens))   # 0
print(next(evens))   # 2
print(next(evens))   # 4

# Take only the first 5
from itertools import islice
print(list(islice(even_numbers(), 5)))   # [0, 2, 4, 6, 8]
```

---

### Use 3 — Lazy data pipeline

```python
# Each stage is a generator. Nothing runs until the final loop consumes it.

def read_numbers(data):
    for x in data:
        yield int(x)           # stage 1: convert to int

def keep_positive(numbers):
    for n in numbers:
        if n > 0:
            yield n            # stage 2: filter

def doubled(numbers):
    for n in numbers:
        yield n * 2            # stage 3: transform

raw    = ["3", "-1", "7", "-2", "5"]
stage1 = read_numbers(raw)     # nothing runs yet
stage2 = keep_positive(stage1) # nothing runs yet
stage3 = doubled(stage2)       # nothing runs yet

for val in stage3:             # NOW it runs, one item at a time
    print(val)
# 6  14  10
```

---

### Use 4 — Pagination / chunked streaming

```python
# Instead of returning all records at once, yield one page at a time.

def paginate(records, page_size):
    for i in range(0, len(records), page_size):
        yield records[i : i + page_size]

records = list(range(1, 22))   # 21 records

for page_num, page in enumerate(paginate(records, 5), start=1):
    print(f"Page {page_num}: {page}")

# Page 1: [1, 2, 3, 4, 5]
# Page 2: [6, 7, 8, 9, 10]
# Page 3: [11, 12, 13, 14, 15]
# Page 4: [16, 17, 18, 19, 20]
# Page 5: [21]
```

Same pattern works for database cursors, API responses, and network streams.

---

### Use 5 — On-demand values (generator as a stateful counter)

```python
# The generator remembers where it left off between calls.

def counter(start=1):
    n = start
    while True:
        yield n
        n += 1

ticket = counter(start=1000)   # ticket number machine
print(next(ticket))   # 1000
print(next(ticket))   # 1001
print(next(ticket))   # 1002
# each call gives the next number — state is kept inside the generator
```

---

### Use 6 — Database rows

Loading all rows from a large table into memory at once can crash a program. Generators let you process one row at a time.

```python
def fetch_rows(cursor):
    """Yield one database row at a time — never loads all rows into memory."""
    for row in cursor:
        yield row

# Usage
# cursor = db.execute("SELECT * FROM orders")
# for row in fetch_rows(cursor):
#     process(row)
```

Memory stays flat no matter how many rows are in the table.

---

### Use 7 — ML / AI batch training

GPU memory cannot hold an entire dataset. Generators feed one batch at a time.

```python
def batch_generator(data, batch_size=32):
    """Yield one training batch at a time."""
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]

# training_data = [...]   # could be millions of samples
for batch in batch_generator(training_data, batch_size=32):
    model.train(batch)    # only 32 samples in memory at once
```

> This is exactly how PyTorch `DataLoader` and TensorFlow `tf.data` feed training data — generators under the hood.

---

### When to use a generator vs a list

| Situation | Use |
|---|---|
| Data is large or comes from a file/API | Generator — constant memory |
| Sequence is infinite | Generator — only `yield` can do this |
| You need to iterate **more than once** | List — generators exhaust after one pass |
| You need random access by index `lst[3]` | List — generators cannot be indexed |
| Passing to `sum()` / `max()` / `any()` / `all()` | Generator expression `()` — no list needed |
| You need to build the full collection first | List |
| Integers only, with a step | `range` — reusable, supports index and len |

---

## 9. Use Case 1 — Large File Processing

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

## 10. Use Case 2 — Infinite Sequences

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

## 11. Use Case 3 — Data Pipelines

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

## 12. Use Case 4 — Pagination / Streaming

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

## 13. Use Case 5 — Fibonacci on Demand

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

## 14. send() — Two-way Communication

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

## 15. yield from — Delegating Generators

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

## 16. Quick Recap — Cheat Sheet

### yield vs return

| | `return` | `yield` |
|---|---|---|
| Runs | All at once | One step at a time |
| Resumes? | No | Yes |
| Returns | Value | Generator object |
| Memory | All upfront | One at a time |

### Generator vs range

| Feature | `range` | Generator |
|---|---|---|
| Lazy | ✅ | ✅ |
| Reusable | ✅ | ❌ exhausted after one pass |
| `len()` / indexing | ✅ | ❌ |
| Infinite sequences | ❌ | ✅ |
| Custom logic / any type | ❌ integers only | ✅ |

### Generator syntax

```python
# generator function
def gen():
    yield value

# generator expression — one-liner
g = (expr for x in it if cond)

# next — pull one value
next(g)

# send — push a value in
g.send(value)

# yield from — delegate to another generator
yield from other_gen()
```

### sum() — generator vs list

```python
# Preferred — generator expression, no list built
total = sum(x**2 for x in range(1_000_000))

# Avoid — list comprehension, 8 MB wasted
total = sum([x**2 for x in range(1_000_000)])
```

### When to use generators

| Situation | Use generator? |
|---|---|
| Large file / dataset | ✅ yes — constant memory |
| Infinite sequence | ✅ yes — only `yield` can do this |
| Data pipeline / stages | ✅ yes — lazy chaining |
| Streaming / pagination / DB rows | ✅ yes — process batch by batch |
| ML / AI training batches | ✅ yes — GPU memory cannot hold full dataset |
| Passing to `sum` / `max` / `any` / `all` | ✅ yes — use `()` not `[]` |
| Need list indexing `[i]` | ❌ no — use a list |
| Iterate more than once | ❌ no — generators exhaust after one pass |
| Integer range, reusable | ❌ no — use `range` |

### Key rules

- A generator can only be iterated **once** — to iterate again, create a new generator
- `for` loops handle `StopIteration` automatically
- Always `next(gen)` once before `send()` to prime it
- Generator expressions `( )` are the quick one-liner form
- `yield from` replaces a manual `for` loop when delegating
- `range` is reusable; a generator is not

---

*Python Series by Satya VS · [github.com/reachsatyavs/python-tutorials](https://github.com/reachsatyavs/python-tutorials)*
