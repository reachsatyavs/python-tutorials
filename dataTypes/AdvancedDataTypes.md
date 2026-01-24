# Python Core Data Types: `tuple`, `list`, `dict`, `set`

This document explains **what each type is**, **why it exists**, **where it’s used**, provides **10 practical examples each**, and ends with a **comparison table** (ordered, unique, duplicates, mutability, hashable, “thread-safe”, etc.).

> **Quick note on “thread-safe”:** Python’s built-in containers (`list`, `dict`, `set`) are **not designed to be thread-safe** for multi-step operations. With CPython’s GIL, *some single operations appear atomic*, but you should still use **locks** (or thread-safe structures like `queue.Queue`) for correctness.  
> `tuple` is **immutable**, so it’s the safest to share across threads.

---

## 1) `tuple`

### What it is
A **tuple** is an **ordered, immutable** sequence of items.

### Why it’s needed
- **Immutability**: Once created, it can’t be changed — helpful for safety and predictability.
- **Hashability** (when it contains only hashable items): usable as **dictionary keys** and in **sets**.
- **Performance**: often a bit lighter/faster than lists for fixed collections.

### Where it’s used
- **Returning multiple values** from a function (`return a, b`)
- **Fixed records** (e.g., `(x, y)` coordinates)
- **Dictionary keys** like `(row, col)` or `(user_id, date)`
- **Data that should not be modified** by mistake

### 10 examples
```python
# 1) Basic tuple
t = (1, 2, 3)

# 2) Tuple without parentheses (packing)
t = 1, 2, 3

# 3) Single-item tuple (comma is required)
t = (42,)

# 4) Unpacking
a, b, c = (10, 20, 30)

# 5) Swap variables (classic tuple unpacking)
x, y = 5, 9
x, y = y, x

# 6) Return multiple values
def min_max(nums):
    return min(nums), max(nums)

mn, mx = min_max([2, 9, 1, 7])

# 7) Use tuple as dict key (2D grid)
grid = {(0, 0): "start", (0, 1): "wall", (1, 0): "path"}

# 8) Iterate fixed pairs
for point in [(0, 0), (1, 2), (5, 8)]:
    print(point)

# 9) Slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])  # (20, 30, 40)

# 10) Tuple can hold duplicates
t = ("a", "b", "a", "c")
```

---

## 2) `list`

### What it is
A **list** is an **ordered, mutable** sequence of items.

### Why it’s needed
- You often need a collection that can **grow**, **shrink**, and **change**.
- Great for **dynamic data** and iterative processing.

### Where it’s used
- Collecting items from loops (e.g., building results)
- Storing ordered data (e.g., steps in a pipeline)
- Data processing (filtering, mapping, sorting)
- Stacks/queues (basic) and general-purpose containers

### 10 examples
```python
# 1) Create a list
nums = [1, 2, 3]

# 2) Append
nums.append(4)  # [1, 2, 3, 4]

# 3) Insert at position
nums.insert(1, 99)  # [1, 99, 2, 3, 4]

# 4) Remove by value
nums.remove(99)

# 5) Pop by index (default last)
last = nums.pop()  # removes 4

# 6) List slicing
nums = [10, 20, 30, 40, 50]
print(nums[::2])  # [10, 30, 50]

# 7) List comprehension (transform)
squares = [x * x for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# 8) Filter with comprehension
evens = [x for x in range(10) if x % 2 == 0]  # [0,2,4,6,8]

# 9) Sort (in-place)
names = ["Zoe", "Ana", "Mohan"]
names.sort()  # ["Ana", "Mohan", "Zoe"]

# 10) Nested list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1][2])  # 6
```

---

## 3) `dict` (dictionary)

### What it is
A **dictionary** maps **keys → values** (a hash table). Keys are **unique** and usually **hashable**.

### Why it’s needed
- Fast lookup by key: “Give me the value for this name/id/config key”
- Represents structured data naturally (like JSON objects)

### Where it’s used
- Configs, settings, feature toggles
- Caching results (`{input: output}`)
- Counting frequency (`{item: count}`)
- Data records (`{"name": "...", "age": ...}`)
- Fast membership checks on keys

### 10 examples
```python
# 1) Create dict
user = {"name": "Sathya", "city": "Mysore"}

# 2) Access value
print(user["name"])  # Sathya

# 3) Safe access with default
print(user.get("age", 0))  # 0

# 4) Add/update
user["age"] = 40

# 5) Delete
del user["city"]

# 6) Iterate keys/values/items
for k, v in user.items():
    print(k, "=", v)

# 7) Dictionary comprehension
squares = {x: x * x for x in range(1, 6)}  # {1:1, 2:4, ...}

# 8) Counting frequency
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
# {'b':1, 'a':3, 'n':2}

# 9) Nested dict (like JSON)
cfg = {
    "db": {"host": "localhost", "port": 5432},
    "feature_flags": {"new_ui": True}
}

# 10) Tuple as a key (compound key)
prices = {("apple", "INR"): 120, ("apple", "USD"): 1.5}
```

---

## 4) `set`

### What it is
A **set** is an **unordered** collection of **unique** items (hash-based).

### Why it’s needed
- Automatically removes duplicates
- Very fast membership checks (`x in s`)
- Great for mathematical set operations: union/intersection/difference

### Where it’s used
- De-duplicating data (unique IDs, unique words)
- Checking membership quickly (allowed/blocked lists)
- Finding common items between two groups
- Data cleaning and comparisons

### 10 examples
```python
# 1) Create a set
s = {1, 2, 3}

# 2) Set removes duplicates automatically
s = {1, 2, 2, 3}  # {1, 2, 3}

# 3) Add element
s.add(4)

# 4) Remove element (error if not present)
s.remove(4)

# 5) Discard element (no error if missing)
s.discard(999)

# 6) Membership test (fast)
allowed = {"admin", "editor"}
print("admin" in allowed)  # True

# 7) Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # {1,2,3,4,5}

# 8) Intersection
print(a & b)  # {3}

# 9) Difference
print(a - b)  # {1,2}

# 10) Unique words from a sentence
sentence = "python is fun and python is powerful"
unique_words = set(sentence.split())
```

---

## Practical comparisons and “gotchas”

### Uniqueness vs duplicates
- **set**: only unique items (duplicates are removed)
- **tuple/list**: duplicates allowed
- **dict**: **keys** are unique; **values** can repeat

### Ordered vs unordered
- **list/tuple**: ordered (index-based)
- **dict**: preserves **insertion order** (Python 3.7+ as language guarantee)
- **set**: not ordered (don’t rely on order)

### Mutability
- **tuple**: immutable (cannot change)
- **list/dict/set**: mutable

### Thread-safety (practical view)
- **tuple**: safest to share across threads because it’s immutable.
- **list/dict/set**: not thread-safe for compound operations. Use locks if multiple threads write or if correctness depends on multi-step logic.

If you truly need concurrent access patterns:
- Use `threading.Lock`
- Consider `queue.Queue` for producer-consumer
- For shared state, guard read-modify-write sequences

---

## Comparison table

| Type  | Literal example | Ordered? | Indexed? | Mutable? | Allows duplicates? | Unique enforced? | Key/Value? | Hashable itself? | Typical lookup speed | “Thread-safe” to share?* |
|------|------------------|----------|----------|----------|--------------------|------------------|------------|------------------|----------------------|---------------------------|
| `tuple` | `(1, 2, 3)` | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes | ❌ No | ❌ No | ✅ Often (if elements hashable) | Index O(1) | ✅ Best (immutable) |
| `list`  | `[1, 2, 3]` | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | ❌ No | ❌ No | Index O(1) | ⚠️ Needs locks if shared writes |
| `dict`  | `{"a": 1}` | ✅ Insertion order | ⚠️ By key | ✅ Yes | Values ✅ / Keys ❌ | Keys ✅ | ✅ Yes | ❌ No | Key O(1) avg | ⚠️ Needs locks if shared writes |
| `set`   | `{1, 2, 3}` | ❌ No | ❌ No | ✅ Yes | ❌ No | ✅ Yes | ❌ No | ❌ No | Membership O(1) avg | ⚠️ Needs locks if shared writes |

\* “Thread-safe to share” here means: safe to share without worrying about someone mutating it out from under you. For correctness in multi-threaded programs, **use locks** for shared mutable structures.

---

## Choosing the right one (rule of thumb)

- Use **`list`** when you need an **ordered, changeable** collection.
- Use **`tuple`** for **fixed** collections, returns, records, and **keys**.
- Use **`dict`** for **named fields**, configuration, and **fast lookup by key**.
- Use **`set`** for **uniqueness**, de-duplication, and **fast membership** + set operations.

---

## Mini cheat-sheet

```python
# list: ordered, mutable
a = [1, 2, 3]
a.append(4)

# tuple: ordered, immutable
t = (1, 2, 3)

# dict: key -> value
d = {"env": "dev", "retries": 3}

# set: unique items, fast membership
s = {"dev", "stage", "prod"}
```
