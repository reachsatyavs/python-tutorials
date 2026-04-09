# Hashing in Python

This folder covers **how Python hashing works** — from the concept to the internals — with teaching notes, runnable scripts, and presentation slides.

---

## Contents


| File                          | Type   | What it covers                                                                          |
| ----------------------------- | ------ | --------------------------------------------------------------------------------------- |
| `WhatIsHashing.md`            | Notes  | Concept guide: what a hash is, why it exists, O(1) lookups, immutable keys              |
| `ThreadSafety_and_Hashing.md` | Notes  | Hashing + thread safety together — with runnable examples and a speed benchmark         |
| `hash_explorer.py`            | Script | **Interactive** — visualises hash values, bucket layout, collisions, O(1) proof         |
| `dict_table_size.py`          | Script | Shows how Python decides dict table size, when it resizes, and why powers of 2          |
| `dict_internals.py`           | Script | **Interactive menu** — live memory view of `dict`, `set`, `list`, and `tuple` internals |
| `WhatIsHashing.pptx`          | Slides | Presentation slides for the hashing topic                                               |
| `Python_Hashing_Buckets.pptx` | Slides | Slides focused on bucket layout and collision resolution                                |


---

## Key Concepts

### What is a hash?

> A hash is a number Python computes from a key so it can find the matching value **instantly** — without scanning every item.

```
key  →  hash(key)  →  slot index  →  value
```

Think of it like a **locker number**: you don't open every locker — you go directly to your slot.

### Why it matters


| Lookup         | Time complexity | What Python does                   |
| -------------- | --------------- | ---------------------------------- |
| `x in my_list` | O(n)            | Scans every element from the start |
| `x in my_set`  | O(1) avg        | Computes hash → jumps to slot      |
| `my_dict[key]` | O(1) avg        | Computes hash → jumps to slot      |


### Why dict keys must be immutable

If you change a key after storing it, its hash changes. Python would look in the **wrong slot** and never find the value — the key is effectively lost. Python prevents this by only allowing **hashable** (immutable) types as keys: `str`, `int`, `float`, `tuple`, `frozenset`.

```python
d = {}
d[(1, 2)] = "tuple key"   # ✅ tuple is immutable and hashable
d[[1, 2]] = "list key"    # ❌ TypeError: unhashable type: 'list'
```

---

## Running the scripts

```bash
# See hash values, bucket layout, and collisions visualised
python hash_explorer.py

# Understand how dict table size grows and when Python resizes
python dict_table_size.py

# Interactive memory explorer for dict, set, list, and tuple
python dict_internals.py
```

All three scripts use colour output and run in any standard terminal (macOS / Linux / Windows 10+).

---

## Script summaries

### `hash_explorer.py`

Walks through 5 parts automatically:

1. `hash()` values for `str`, `int`, `tuple`, and `list` (with error)
2. Simulated bucket array — where each key lands and when collisions happen
3. Real CPython dict internals via `sys.getsizeof()` and `id()`
4. Forced collision example with a tiny table (size = 4)
5. Speed comparison — list O(n) vs dict O(1) on 500,000 items

### `dict_table_size.py`

Explains the rules Python uses to manage dict memory:

- Table size is always a **power of 2** (8 → 16 → 32 → ...)
- Resize happens when **used > (size × 2) // 3** (the ⅔ load factor)
- Why bitwise AND (`hash & (size-1)`) is used instead of modulo (`%`)
- Full resize schedule from 0 → 100,000 keys (only 17 resizes!)

### `dict_internals.py`

Interactive menu with four modes:


| Option    | Shows                                                  |
| --------- | ------------------------------------------------------ |
| `1` dict  | Hash table slots: `cached_hash                         |
| `2` set   | Hash table slots: `cached_hash                         |
| `3` list  | Index array: sequential `→ addr` pointers, O(n) search |
| `4` tuple | Same as list but immutable; hashable if elements are   |


In each mode you can **add items live** and watch the table rebuild, and **look up keys/values** to see the exact hash, slot, and memory address Python uses.

---

## Teaching order

1. **Concept** — `WhatIsHashing.md` (what, why, locker analogy)
2. **Examples + speed proof** — `ThreadSafety_and_Hashing.md` (runnable snippets, benchmark)
3. **Visualised internals** — `hash_explorer.py` (bucket layout, collisions)
4. **Deep dive** — `dict_table_size.py` (resize rules, load factor, bitwise AND)
5. **Live explorer** — `dict_internals.py` (interactive, great for classroom demos)
6. **Slides** — `WhatIsHashing.pptx` / `Python_Hashing_Buckets.pptx`

