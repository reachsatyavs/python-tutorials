# Thread Safety and Hashing in Python

Two questions students often ask together:

1. **What is hashing, and how does Python use it for fast lookups?**
2. **What does "thread safe" mean, and why do immutable keys matter?**

Each section has a plain-English explanation followed by runnable examples you can paste into a file or notebook cell.

---

## Part 1 — Hashing

### What is a hash?

> A **hash** is a number Python computes from a value so it can find things in a dictionary or set **instantly**, without scanning every item.

Think of it like a **locker number at a gym**.  
Instead of opening every locker to find your stuff, you are given a number — you walk directly to that locker.

```
key → hash(key) → locker number → value
```

### Example 1 — see a hash with your own eyes

```python
print(hash("Alice"))   # e.g. 3713082716806266542
print(hash("Bob"))     # e.g. 5765530498355573184
print(hash(42))        # 42  (integers hash to themselves)
print(hash((1, 2)))    # tuples are hashable
```

Every run may give you a different number (Python randomizes hash seeds for security), but within one run, the same object always gives the **same number**.

---

### Example 2 — why dicts are fast (mental model)

```python
marks = {}
marks["Alice"] = 95
marks["Bob"]   = 88

# Python internally does something like:
#   slot = hash("Alice") % table_size  → slot 3
#   table[3] = ("Alice", 95)
#
# On lookup:
#   slot = hash("Alice") % table_size  → slot 3  (same jump!)
#   return table[3].value              → 95

print(marks["Alice"])  # instant — no scanning
```

Compare this to searching a plain list:

```python
# List: must scan one by one  → O(n)  slow for big data
students = ["Bob", "Carol", "Alice", "Dave"]
print("Alice" in students)   # checks Bob... Carol... Alice ✓

# Set: hash jump              → O(1)  fast regardless of size
students_set = {"Bob", "Carol", "Alice", "Dave"}
print("Alice" in students_set)   # hash("Alice") → directly there ✓
```

---

### Example 3 — proof: measuring the speed difference yourself

Run this on your machine — the numbers will convince students immediately.

```python
import time

numbers = list(range(10000000))
numbers_dict = {i: i * i for i in numbers}
value_to_fetch = 3333333

# list lookup — scans from the beginning until it finds the value
start = time.perf_counter()
value_to_fetch in numbers
list_time = time.perf_counter() - start
print(f"List time:  {list_time:.10f} seconds")

# dict lookup — computes hash(key), jumps directly to the slot
start = time.perf_counter()
value = numbers_dict[value_to_fetch]
dict_time = time.perf_counter() - start
print(f"Dict value: {value}")
print(f"Dict time:  {dict_time:.10f} seconds")

# comparison
difference = list_time - dict_time
speed = list_time / dict_time if dict_time > 0 else 0

print(f"\nDifference (list - dict): {difference:.10f} seconds")
print(f"Dict is faster by:        {speed:.2f}x")
```

**What to expect:** the list takes microseconds to milliseconds (it scans ~2.2 million items); the dict takes nanoseconds (one hash jump). The ratio is typically **hundreds to thousands of times faster** for the dict.

**Why:** the list has no choice but to check every element from index 0 until it finds `2_222_222`. The dict computes `hash(2_222_222)`, lands on the right slot, and returns immediately — regardless of how large the dict is.

---

### Example 4 — why keys must be immutable

```python
# Tuple key — works fine
d = {}
d[(10, 20)] = "point A"
print(d[(10, 20)])   # "point A"

# List key — Python raises an error
d[[1, 2]] = "bad"    # TypeError: unhashable type: 'list'
```

**Why?**  
If you could use a list as a key and then change the list, its hash would change. Python would look in the **old locker** and find nothing. The key would be lost forever. Python blocks this upfront.

```python
# Imagine this was allowed (it is NOT):
key = [1, 2]
# d = {key: "value"}   # TypeError

# If it were allowed, then:
key.append(3)
# hash(key) would now be different
# Python looks in the wrong locker → value lost
```

**Rule:** to be a dict key or a set member, an object must be **hashable**, which means its value (and hash) must never change. Immutable types (`int`, `str`, `tuple`, `frozenset`) meet this rule.

---

## Part 2 — Thread Safety

### What is a thread?

A **thread** is a separate "worker" inside your program that can run at the same time as other workers.

Think of a café: one thread takes orders, another makes coffee, another cleans tables — all at the same time. They share the same kitchen (memory).

> **Thread safety** means: even when multiple threads run at the same time, the program gives **correct** results without data getting corrupted.

---

### Why sharing mutable objects causes problems

When two threads change the **same mutable object simultaneously**, results become unpredictable.

### Example 5 — a data race (shared mutable list)

> **Note on CPython's GIL:** CPython has a "Global Interpreter Lock" that often prevents the simplest integer-counter race. This is a CPython implementation detail — not a language guarantee, and not present in other Python implementations (PyPy, Jython). Good code does **not** rely on the GIL for safety.

A more reliable way to show the race: two threads each append to a shared list using a deliberate read-then-write gap:

```python
import threading
import time

shared_list = []

def add_items(label):
    for i in range(5):
        # simulate: read current list, do some work, write back
        current = shared_list[:]   # read snapshot
        time.sleep(0.001)          # another thread can run here
        current.append(f"{label}-{i}")
        shared_list.clear()
        shared_list.extend(current)  # write back — may overwrite other thread's work!

t1 = threading.Thread(target=add_items, args=("T1",))
t2 = threading.Thread(target=add_items, args=("T2",))

t1.start(); t2.start()
t1.join();  t2.join()

print("Items added:", len(shared_list), "(expected 10)")
print(sorted(shared_list))
# You will likely see FEWER than 10 items — some were overwritten
```

Run this a few times. You will likely see different wrong answers. `T1` reads the list, `T2` also reads the list, `T1` writes back, then `T2` overwrites with its own snapshot — `T1`'s work is lost.

---

### Example 6 — fixing it with a Lock

```python
import threading

counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(100_000):
        with lock:               # only one thread enters at a time
            counter += 1

t1 = threading.Thread(target=increment_safe)
t2 = threading.Thread(target=increment_safe)

t1.start()
t2.start()
t1.join()
t2.join()

print("Expected:", 200_000)
print("Got:     ", counter)    # always 200,000
```

`with lock:` says: "only one thread can be here at a time — everyone else waits."

---

### How immutable objects help thread safety

Immutable objects **cannot be changed** after creation. If no thread can change an object, there is nothing to race over.

### Example 7 — immutable dict keys are always safe

```python
import threading

# Using tuple keys (immutable) — completely safe to read from multiple threads
locations = {
    (0, 0): "Warehouse A",
    (1, 5): "Warehouse B",
    (3, 2): "Warehouse C",
}

results = []

def find_nearest(coord):
    # Just reading the dict — no mutation → no race condition
    result = locations.get(coord, "Not found")
    results.append(result)

threads = [threading.Thread(target=find_nearest, args=((0, 0),)) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print(results)   # always correct, no lock needed
```

Multiple threads can **read** the same dict at the same time safely. The tuple keys cannot be changed by any thread, so the hash is always valid.

---

### Example 8 — mutable value inside dict still needs care

```python
import threading

# The KEY is a safe immutable string
# But the VALUE is a mutable list → still needs protection
scores = {
    "Alice": [],
    "Bob":   [],
}
lock = threading.Lock()

def add_score(student, score):
    with lock:                      # protect the mutable value
        scores[student].append(score)

threads = [
    threading.Thread(target=add_score, args=("Alice", i)) for i in range(5)
] + [
    threading.Thread(target=add_score, args=("Bob", i)) for i in range(5)
]

for t in threads: t.start()
for t in threads: t.join()

print("Alice:", sorted(scores["Alice"]))
print("Bob:  ", sorted(scores["Bob"]))
```

The dict keys are safe (strings are immutable). The list values are mutable, so they still need a lock if multiple threads write to them.

---

## Summary Table


| Question                                       | Answer                                                                         |
| ---------------------------------------------- | ------------------------------------------------------------------------------ |
| What is a hash?                                | A number computed from a key so Python can find values instantly               |
| Why must dict keys be immutable?               | So the hash never changes; otherwise Python loses the key                      |
| What is thread safety?                         | The guarantee that shared data stays correct when multiple threads run at once |
| Why do immutable objects help?                 | They cannot be changed, so no thread can corrupt them — no race condition      |
| Do immutable keys make everything thread safe? | Only the keys; mutable values still need a lock when written                   |


---

## One-line takeaways for students

- **Hashing** → locker analogy: key → number → jump directly → value. Fast. O(1).
- **Immutable keys** → hash never changes → locker number is always reliable.
- **Thread safety** → two threads changing the same thing at the same time = data race = wrong answer.
- **Fix**: `threading.Lock()` (only one thread at a time) or use objects that cannot be changed at all.

