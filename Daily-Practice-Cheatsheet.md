# Python Daily Practice — 20-Minute Morning Drill

> **How to use:** Read each section, close it, type the patterns from memory, then check.  
> One section per day to start. Full sheet in one sitting once you are comfortable.

---

## ① Data Types — Initialization (2 min)

```python
# --- primitives ---
name    = "Alice"           # str   — quotes required
age     = 30                # int
salary  = 75_000.50         # float — underscore ok for readability
active  = True              # bool  — capital T/F
nothing = None              # NoneType

# --- collections ---
my_list  = [1, "two", 3.0]         # list  — ordered, mutable,   [ ]
my_tuple = (1, "two", 3.0)         # tuple — ordered, immutable, ( )
my_set   = {1, 2, 3}               # set   — unordered, unique,  { }
my_dict  = {"name": "Alice", "age": 30}  # dict  — key:value,   { : }

# --- empty containers ---
empty_list  = []
empty_tuple = ()
empty_set   = set()          # NOT {} — that creates an empty dict
empty_dict  = {}
```

**Type check:**

```python
type(42)           # <class 'int'>
isinstance(True, int)   # True — bool is a subclass of int
```

---

## ② Key Methods per Type (3 min)

### str

```python
s = "  hello world  "
s.strip()           # "hello world"    — remove whitespace
s.upper()           # "  HELLO WORLD  "
s.lower()
s.title()           # "  Hello World  "
s.split()           # ['hello', 'world']
s.replace("hello", "hi")
s.count("l")        # 3
len(s)              # 15
"world" in s        # True
s[0:5]              # "  hel"
s[::-1]             # reversed
f"Name: {s.strip().title()}"   # f-string
```

### list

```python
lst = [3, 1, 4, 1, 5]
lst.append(9)       # add to end
lst.remove(1)       # remove first occurrence
lst.pop()           # remove & return last
lst.sort()          # in-place sort
lst.index(4)        # position of value
lst.count(1)        # how many times
len(lst)
sum(lst)
min(lst)  /  max(lst)
sorted(lst)         # returns new list, original untouched
sorted(lst, reverse=True)
```

### dict

```python
d = {"name": "Alice", "age": 30}
d["name"]           # "Alice"
d.get("salary", 0)  # 0 — safe, no KeyError
d["city"] = "Mumbai"       # add / update
d.keys()   /  d.values()  /  d.items()
for k, v in d.items():
    print(k, v)
"name" in d         # True — checks keys
```

### tuple

```python
t = (10, 20, 30)
a, b, c = t             # unpack
first, *rest = t        # first=10, rest=[20,30]
a, b = b, a             # swap
```

### set

```python
a = {1, 2, 3}
b = {2, 3, 4}
a | b    # union        {1,2,3,4}
a & b    # intersection {2,3}
a - b    # difference   {1}
a ^ b    # symmetric diff {1,4}
"x" in a            # membership check
set([1,1,2,2,3])    # remove duplicates → {1,2,3}
```

---

## ③ Built-in Functions (2 min)

```python
# --- on any iterable ---
len([1,2,3])         # 3
sum([1,2,3])         # 6
min([3,1,2])         # 1
max([3,1,2])         # 3
sorted([3,1,2])      # [1,2,3]
sorted([3,1,2], reverse=True)

# --- type / check ---
type(42)             # <class 'int'>
isinstance(42, int)  # True
callable(len)        # True

# --- iteration helpers ---
range(5)             # 0,1,2,3,4
range(1, 6)          # 1,2,3,4,5
range(0, 10, 2)      # 0,2,4,6,8

for i, v in enumerate(["a","b","c"], start=1):
    print(i, v)      # 1 a  /  2 b  /  3 c

for x, y in zip([1,2,3], ["a","b","c"]):
    print(x, y)      # 1 a  /  2 b  /  3 c

# --- any / all ---
any([False, True, False])   # True  — at least one True
all([True,  True, True ])   # True  — every one True

# --- conversion ---
int("42")   /  float("3.14")  /  str(100)  /  list((1,2,3))
abs(-5)     /  round(3.7)     /  pow(2, 8)
```

---

## ④ Operators (2 min)

### Arithmetic

```python
17 + 5   # 22      addition
17 - 5   # 12      subtraction
17 * 5   # 85      multiplication
17 / 5   # 3.4     division          → always float
17 // 5  # 3       floor division    → drops decimal
17 % 5   # 2       modulo / remainder
2 ** 8   # 256     exponentiation

# Practical memory tricks
137 // 60  # hours  (2)
137 %  60  # minutes (17)
n % 2 == 0 # is even
n % 2 != 0 # is odd
```

### Comparison  (always return True / False)

```python
==   !=   >   <   >=   <=
```

### Logical

```python
and   # True only if BOTH sides are True
or    # True if AT LEAST ONE side is True
not   # flips True → False
```

### Membership / Identity

```python
"x" in  lst      # is x inside?
"x" not in lst
a is None        # identity — same object?
a is not None    # ← preferred way to check None
```

### Augmented Assignment

```python
x += 5   # x = x + 5
x -= 5
x *= 2
x //= 2
x **= 2
```

---

## ⑤ Control Flow (3 min)

### if / elif / else

```python
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

# ternary — one-liner
label = "pass" if score >= 60 else "fail"
```

### for loop

```python
for item in collection:
    print(item)

for i in range(1, 6):          # 1 2 3 4 5
    print(i)

for i, v in enumerate(lst, start=1):
    print(i, v)

for k, v in d.items():
    print(k, v)

for x, y in zip(lst_a, lst_b):
    print(x, y)
```

### while loop

```python
while condition:
    # body
    counter += 1

while True:          # infinite — needs break
    if done:
        break
```

### break / continue / for-else

```python
for item in collection:
    if skip_condition:
        continue      # skip to next iteration
    if stop_condition:
        break         # exit loop immediately
else:
    # runs ONLY if loop completed without a break
    print("not found")
```

---

## ⑥ Functions (3 min)

### def patterns

```python
# basic
def greet(name):
    return f"Hello, {name}!"

# default argument
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# *args  — extra positionals → tuple
def total(*numbers):
    return sum(numbers)
total(1, 2, 3, 4)   # numbers = (1, 2, 3, 4)

# **kwargs — extra keyword args → dict
def show(**info):
    for k, v in info.items():
        print(k, v)
show(name="Alice", age=30)

# all four together
def fn(pos, default="x", *args, kw_only, **kwargs):
    pass
```

### Closures

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor   # 'factor' remembered from outer scope
    return multiply

double = make_multiplier(2)
double(5)   # 10
```

### Recursion pattern

```python
def factorial(n):
    if n <= 1:          # base case — ALWAYS first
        return 1
    return n * factorial(n - 1)   # recursive case
```

---

## ⑦ Lambda (2 min)

```python
# syntax
lambda arguments : expression

# vs def
def square(n):      return n ** 2
sq = lambda n:      n ** 2       # identical

# two arguments
add   = lambda a, b: a + b

# with conditional (ternary)
grade = lambda s: "A" if s >= 90 else ("B" if s >= 75 else "F")

# immediately called
result = (lambda x, y: x * y)(6, 7)   # 42

# in a dict — dispatch table
ops = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
}
ops["add"](10, 3)   # 13
```

---

## ⑧ sorted · min · max · map · filter · reduce (3 min)

```python
employees = [
    {"name": "Alice", "salary": 50000, "age": 30},
    {"name": "Bob",   "salary": 80000, "age": 20},
    {"name": "Carol", "salary": 60000, "age": 25},
]

# sorted — new list, original untouched
sorted(employees, key=lambda e: e["salary"])              # low → high
sorted(employees, key=lambda e: e["salary"], reverse=True) # high → low
sorted(employees, key=lambda e: (e["dept"], -e["salary"])) # multi-key

# min / max — returns the WHOLE item, not just the key value
youngest     = min(employees, key=lambda e: e["age"])
highest_paid = max(employees, key=lambda e: e["salary"])

# map — transform every item → lazy, wrap in list()
salaries = list(map(lambda e: e["salary"], employees))
raised   = list(map(lambda e: {**e, "salary": e["salary"]*1.1}, employees))

# filter — keep items where fn returns True → lazy, wrap in list()
seniors  = list(filter(lambda e: e["age"] >= 25, employees))
rich     = list(filter(lambda e: e["salary"] > 55000, employees))

# reduce — collapse all items to ONE value
from functools import reduce
total = reduce(lambda acc, e: acc + e["salary"], employees, 0)
#                                                              ↑
#                                                    initial value (required for dicts)
```

**Quick recall table:**


| Function                | Receives                          | Returns                           |
| ----------------------- | --------------------------------- | --------------------------------- |
| `sorted(lst, key=fn)`   | iterable + key fn                 | new sorted **list**               |
| `min(lst, key=fn)`      | iterable + key fn                 | whole **item** with smallest key  |
| `max(lst, key=fn)`      | iterable + key fn                 | whole **item** with largest key   |
| `map(fn, lst)`          | transform fn + iterable           | lazy **map object** → `list()`    |
| `filter(fn, lst)`       | test fn + iterable                | lazy **filter object** → `list()` |
| `reduce(fn, lst, init)` | accumulator fn + iterable + start | single **value**                  |


---

## ⑨ Comprehensions (2 min)

```python
# THE PATTERN:   [  expression    for item in iterable    if condition  ]
#                    what to make      the loop            optional filter

# List [ ] — ordered, allows duplicates
squares  = [n**2 for n in range(1, 6)]
passed   = [s for s in scores if s >= 60]
grades   = ["pass" if s >= 60 else "fail" for s in scores]   # if-else in expression

# Set { } — unordered, no duplicates
unique   = {s.lower() for s in words}

# Dict { k:v } — key value pairs
name_sal = {e["name"]: e["salary"] for e in employees}
filtered = {k: v for k, v in d.items() if v > 0}
inverted = {v: k for k, v in d.items()}

# Generator ( ) — lazy, memory-efficient, use with sum/max/any
total    = sum(e["salary"] for e in employees)
big      = any(e["salary"] > 90000 for e in employees)

# Bracket is the ONLY decision — everything else is identical
#   [ ]   → list
#   { }   → set
#   {k:v} → dict
#   ( )   → generator  (lazy)
```

**If-else placement rule:**

```python
# filter  — if at the END
[x for x in data if x > 0]          # drops negatives

# transform — if-else in the EXPRESSION (nothing dropped)
[x if x > 0 else 0 for x in data]   # keeps all, negatives → 0
```

---

## ⑩ Generators (2 min)

```python
# generator function — uses yield instead of return
def count_up(n):
    for i in range(1, n+1):
        yield i       # pauses here, resumes next call

gen = count_up(3)
next(gen)   # 1
next(gen)   # 2
next(gen)   # 3
# next(gen) → StopIteration

for val in count_up(5):   # for loop handles StopIteration
    print(val)

# generator expression — one-liner form
sq_gen = (x**2 for x in range(10))
list(sq_gen)    # [0,1,4,9,16,25,36,49,64,81]

# most common real use — pass to sum/max/any, no list built
total  = sum(x**2 for x in range(1_000_000))   # 192 bytes, not 8 MB
big    = any(e["salary"] > 90000 for e in employees)

# yield from — delegate to another generator
def outer():
    yield "start"
    yield from inner()   # replaces: for x in inner(): yield x
    yield "end"
```

`**return` vs `yield`:**


|          | `return`           | `yield`             |
| -------- | ------------------ | ------------------- |
| Runs     | All at once        | One step at a time  |
| Resumes? | No                 | Yes                 |
| Memory   | All values upfront | One value at a time |
| Returns  | The value          | A generator object  |


---

## ⑪ Nested Dict — Read Pattern (1 min)

```python
data = {
    "company": "TechCorp",
    "dept": {
        "engineering": {
            "head": "Alice",
            "skills": ["Python", "Go"]
        }
    }
}

# chain keys
data["dept"]["engineering"]["head"]          # "Alice"
data["dept"]["engineering"]["skills"][0]     # "Python"

# safe deep access — .get() with {} default
dept = "hr"
head = data.get("dept", {}).get(dept, {}).get("head", "N/A")

# loop over nested dict
for dept_name, info in data["dept"].items():
    print(dept_name, info["head"])
```

---

## ⑫ 20-Minute Practice Schedule


| Time        | Task                                                                          |
| ----------- | ----------------------------------------------------------------------------- |
| 0:00 – 0:02 | Type all **data type initialisations** from memory (Section ①)                |
| 0:02 – 0:05 | Write 3 str methods, 3 list methods, 2 dict loops (Section ②)                 |
| 0:05 – 0:07 | Write `len / sum / min / max / enumerate / zip / any / all` calls (Section ③) |
| 0:07 – 0:09 | Write arithmetic, comparison, logical, membership operators (Section ④)       |
| 0:09 – 0:12 | Write `if/elif/else`, `for`, `while`, `break/continue/else` (Section ⑤)       |
| 0:12 – 0:15 | Write a `def` with default arg, `*args`, `**kwargs`, closure (Section ⑥)      |
| 0:15 – 0:17 | Write a lambda, a ternary lambda, a dispatch dict (Section ⑦)                 |
| 0:17 – 0:19 | Write `sorted`, `map`, `filter`, `reduce` on the employee list (Section ⑧)    |
| 0:19 – 0:20 | Write one list, dict, set, generator comprehension (Section ⑨)                |


---

## ⑬ Common Mistakes — Quick Reminder

```python
# ❌  empty set
x = {}         # this is an empty DICT
x = set()      # ✅ this is an empty set

# ❌  key=fn() calls the function now
sorted(lst, key=get_salary())    # crashes — missing argument
sorted(lst, key=get_salary)      # ✅ pass the function reference

# ❌  map/filter return lazy objects, not lists
map(str, [1,2,3])                # <map object>
list(map(str, [1,2,3]))          # ✅ ['1','2','3']

# ❌  is vs ==
x = [1,2,3];  y = [1,2,3]
x is y     # False — different objects
x == y     # True  — same content
x is None  # ✅ correct way to check None

# ❌  reduce without initial value on non-numbers
reduce(lambda acc, e: acc + e["salary"], employees)   # crashes
reduce(lambda acc, e: acc + e["salary"], employees, 0) # ✅

# ❌  modifying a list while looping over it
# ✅  loop over a copy: for item in lst[:]:

# ❌  if-else placement in comprehension
[x for x in data if x else 0]     # wrong syntax
[x if x else 0 for x in data]     # ✅ if-else in expression, no filter
```

---

*Python Series · Modules 01–06 · `github.com/reachsatyavs/python-tutorials`*