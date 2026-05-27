# `range()` — The Built-in Sequence Generator

> `range` produces a sequence of integers on demand — without storing them all in memory.  
> It is the most common way to drive `for` loops, generate indices, and feed comprehensions.

---

## Table of Contents

1. [What is `range`?](#1-what-is-range)
2. [The three signatures](#2-the-three-signatures)
3. [range is lazy — not a list](#3-range-is-lazy--not-a-list)
4. [Counting up](#4-counting-up)
5. [Counting down](#5-counting-down)
6. [Custom step](#6-custom-step)
7. [Common loop patterns](#7-common-loop-patterns)
8. [range with len — index-based loops](#8-range-with-len--index-based-loops)
9. [range in list / set / dict comprehensions](#9-range-in-list--set--dict-comprehensions)
10. [range arithmetic — slicing without a list](#10-range-arithmetic--slicing-without-a-list)
11. [Checking membership — `in` on range](#11-checking-membership--in-on-range)
12. [Common mistakes](#12-common-mistakes)
13. [Quick reference](#13-quick-reference)

---

## 1. What is `range`?

`range` is a built-in that produces an **immutable sequence of integers**.

```python
r = range(5)
print(r)          # range(0, 5)   ← not the numbers yet
print(type(r))    # <class 'range'>
print(list(r))    # [0, 1, 2, 3, 4]
```

Key properties:

| Property | Detail |
|---|---|
| **Lazy** | Numbers are computed on demand — not stored in memory |
| **Immutable** | Cannot change a range after creation |
| **Iterable** | Works directly in `for`, `list()`, `sum()`, comprehensions |
| **Memory-efficient** | `range(1_000_000)` uses the same tiny memory as `range(5)` |

---

## 2. The three signatures

```python
range(stop)                  # from 0, up to (not including) stop
range(start, stop)           # from start, up to (not including) stop
range(start, stop, step)     # from start, up to stop, jumping by step
```

### Parameters

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `start` | `int` | `0` | First value (included) |
| `stop` | `int` | required | Last value is `stop - 1` (excluded) |
| `step` | `int` | `1` | How much to add each time |

```python
range(5)          # 0, 1, 2, 3, 4        — stop only
range(1, 6)       # 1, 2, 3, 4, 5        — start and stop
range(0, 10, 2)   # 0, 2, 4, 6, 8        — with step
range(10, 0, -1)  # 10, 9, 8, ..., 1     — negative step (countdown)
range(10, 0, -2)  # 10, 8, 6, 4, 2       — negative step with size
```

> **The stop value is always excluded.**  
> `range(1, 6)` gives `1, 2, 3, 4, 5` — **not** `6`.

---

## 3. `range` is lazy — not a list

```python
import sys

big_list  = list(range(1_000_000))   # builds 1 million integers in RAM
big_range = range(1_000_000)         # stores only 3 integers: start, stop, step

print(sys.getsizeof(big_list))       # ~8,000,056 bytes  (~8 MB)
print(sys.getsizeof(big_range))      # 48 bytes
```

`range` remembers only `start`, `stop`, and `step`.  
It calculates each value when you ask for it — just like a generator.

---

## 4. Counting up

```python
# simplest — 0 to n-1
for i in range(5):
    print(i, end=" ")
# 0 1 2 3 4

# 1 to n
for i in range(1, 6):
    print(i, end=" ")
# 1 2 3 4 5

# repeat something n times
for _ in range(3):       # _ = "I don't need the variable"
    print("hello")
# hello
# hello
# hello
```

---

## 5. Counting down

```python
# countdown from 5 to 1
for i in range(5, 0, -1):
    print(i, end=" ")
# 5 4 3 2 1

# countdown from 10 to 0 (inclusive)
for i in range(10, -1, -1):
    print(i, end=" ")
# 10 9 8 7 6 5 4 3 2 1 0
```

> **Rule:** when `step` is negative, `start` must be greater than `stop`.

---

## 6. Custom step

```python
# even numbers 0–10
for i in range(0, 11, 2):
    print(i, end=" ")
# 0 2 4 6 8 10

# odd numbers 1–9
for i in range(1, 10, 2):
    print(i, end=" ")
# 1 3 5 7 9

# multiples of 5 up to 50
for i in range(5, 51, 5):
    print(i, end=" ")
# 5 10 15 20 25 30 35 40 45 50

# every third character of a string
s = "abcdefghij"
for i in range(0, len(s), 3):
    print(s[i], end=" ")
# a d g j
```

---

## 7. Common loop patterns

### Repeat n times
```python
for _ in range(n):
    do_something()
```

### Loop with an index
```python
items = ["apple", "banana", "cherry"]
for i in range(len(items)):
    print(f"[{i}] {items[i]}")
# [0] apple
# [1] banana
# [2] cherry
```

### Print a multiplication table
```python
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i*j:4}", end="")
    print()
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
```

### Accumulate — running total
```python
total = 0
for i in range(1, 101):    # sum 1 to 100
    total += i
print(total)   # 5050
```

### Build a star pattern
```python
for row in range(1, 6):
    print("*" * row)
# *
# **
# ***
# ****
# *****
```

---

## 8. `range` with `len` — index-based loops

Use when you need the **index** alongside the value, or when you need to modify the list in-place.

```python
scores = [45, 82, 60, 91, 38]

# read with index
for i in range(len(scores)):
    print(f"Index {i}: {scores[i]}")

# modify in-place (cannot do this with a plain for-in loop)
for i in range(len(scores)):
    scores[i] = scores[i] * 1.10   # apply 10% bonus
print(scores)   # [49.5, 90.2, 66.0, 100.1, 41.8]
```

> **Prefer `enumerate`** when you only need to read:
> ```python
> for i, score in enumerate(scores):   # cleaner
>     print(i, score)
> ```
> Use `range(len(...))` only when you genuinely need to write back to the list by index.

---

## 9. `range` in list / set / dict comprehensions

`range` feeds directly into any comprehension — it is just an iterable.

```python
# list comprehension
squares = [n**2 for n in range(1, 6)]
print(squares)           # [1, 4, 9, 16, 25]

# with filter
evens = [n for n in range(20) if n % 2 == 0]
print(evens)             # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# set comprehension — unique last digits
last_digits = {n % 10 for n in range(1, 30)}
print(last_digits)       # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# dict comprehension — number → square
sq_map = {n: n**2 for n in range(1, 6)}
print(sq_map)            # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# generator expression — memory-efficient sum
total = sum(n**2 for n in range(1, 101))
print(total)             # 338350
```

---

## 10. `range` arithmetic — slicing without a list

`range` supports indexing and slicing just like a list, but without building one.

```python
r = range(10, 100, 10)   # 10, 20, 30, 40, 50, 60, 70, 80, 90

print(r[0])              # 10      — first element
print(r[-1])             # 90      — last element
print(r[2])              # 30      — third element
print(len(r))            # 9       — number of elements

# slicing a range returns another range
print(r[2:5])            # range(30, 60, 10)
print(list(r[2:5]))      # [30, 40, 50]
```

`range` also knows how many elements it has and can answer **instantly** — no iteration needed:

```python
print(len(range(0, 1_000_000, 7)))   # 142858  — instant, no loop
```

---

## 11. Checking membership — `in` on `range`

Testing `x in range(...)` is **O(1)** — it uses math, not a loop.

```python
print(50 in range(0, 101, 10))   # True   — 50 is a multiple of 10 in [0,100]
print(55 in range(0, 101, 10))   # False  — 55 is not
print(99 in range(100))          # True
print(100 in range(100))         # False  — stop is excluded
```

Compare:
```python
# range — O(1), instant even for huge ranges
999_999 in range(0, 1_000_000)     # True  — no loop

# list — O(n), scans every element
999_999 in list(range(0, 1_000_000))  # True — but slow
```

---

## 12. Common mistakes

### Stop is excluded

```python
# ❌ expecting 1 to 5
for i in range(5):          # gives 0, 1, 2, 3, 4
    print(i)

# ✅ 1 to 5
for i in range(1, 6):
    print(i)
```

### Negative step — start must be greater than stop

```python
# ❌ produces nothing
for i in range(0, 5, -1):
    print(i)           # nothing prints — 0 is not > 5

# ✅ count down
for i in range(5, 0, -1):
    print(i)           # 5 4 3 2 1
```

### Step cannot be zero

```python
range(0, 10, 0)    # ValueError: range() arg 3 must not be zero
```

### `range` is not a list — convert when you need list operations

```python
r = range(5)
r.append(5)          # AttributeError — range has no append

lst = list(range(5))
lst.append(5)        # ✅ [0, 1, 2, 3, 4, 5]
```

### Empty range — no error, just nothing to iterate

```python
for i in range(5, 1):        # start > stop with positive step
    print(i)                  # nothing prints — silent, no error

print(list(range(5, 1)))     # []
```

---

## 13. Quick reference

### Signatures

| Call | Sequence produced |
|---|---|
| `range(n)` | `0, 1, 2, ..., n-1` |
| `range(a, b)` | `a, a+1, ..., b-1` |
| `range(a, b, s)` | `a, a+s, a+2s, ...` up to but not including `b` |
| `range(n, 0, -1)` | `n, n-1, ..., 1` |
| `range(n, -1, -1)` | `n, n-1, ..., 0` |

### Recipes

```python
range(n)               # repeat n times
range(1, n+1)          # 1 to n (inclusive)
range(n, 0, -1)        # countdown n → 1
range(n, -1, -1)       # countdown n → 0
range(0, n, 2)         # even numbers 0, 2, 4 ...
range(1, n, 2)         # odd  numbers 1, 3, 5 ...
range(0, n, k)         # every k-th number
range(len(lst))        # all valid indices of lst
```

### Comparison with alternatives

| Goal | Prefer |
|---|---|
| Loop n times, index matters | `range(n)` |
| Loop n times, index not needed | `for _ in range(n)` |
| Loop over items + index | `enumerate(iterable)` |
| Loop over two lists together | `zip(a, b)` |
| All integers from 0 to n in memory | `list(range(n+1))` |
| Infinite counter | generator with `while True: yield` |

---

*Python Series · Module 06 · `github.com/reachsatyavs/python-tutorials`*
