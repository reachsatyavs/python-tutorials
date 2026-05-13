# `sorted`, `min`, `max`, `map`, `filter` — High Order Fuctions

A higher-order function is a function that either accepts a function as an argument, or returns a function, or both.
> All examples use the same employee list.  
> Every example is shown **twice** — once with a named function, once with a lambda — so you can see that both do exactly the same thing.

---

## The data

```python
employees = [
    {"name": "Alice", "salary": 50000, "age": 30},
    {"name": "Bob",   "salary": 80000, "age": 20},
    {"name": "Carol", "salary": 60000, "age": 25},
]
```

---

## Named function vs lambda — quick reminder

```python
# named function
def get_salary(e):
    return e["salary"]

# lambda — exactly the same thing, written inline
lambda e: e["salary"]
```

A lambda is just a function without a name. Both are callables. Both can be passed to `sorted`, `min`, `max`, `map` and `filter` identically.

Use named functions when teaching the concept. Use lambda once students understand it.

---

## 1. `sorted()` — returns a new sorted list

`list.sort()` sorts **in place** (changes the original list).  
`sorted()` returns a **new list** — the original is untouched.

### Named function version

```python
def get_salary(e):
    return e["salary"]

by_salary = sorted(employees, key=get_salary)

print("Original is unchanged:")
for e in employees:
    print(e)

print("\nSorted by salary (new list):")
for e in by_salary:
    print(e)
```

### Lambda version

```python
by_salary = sorted(employees, key=lambda e: e["salary"])

print("Sorted by salary (new list):")
for e in by_salary:
    print(e)
```

**Output (same for both):**
```
Original is unchanged:
{'name': 'Alice', 'salary': 50000, 'age': 30}
{'name': 'Bob',   'salary': 80000, 'age': 20}
{'name': 'Carol', 'salary': 60000, 'age': 25}

Sorted by salary (new list):
{'name': 'Alice', 'salary': 50000, 'age': 30}
{'name': 'Carol', 'salary': 60000, 'age': 25}
{'name': 'Bob',   'salary': 80000, 'age': 20}
```

### Descending order

```python
# named function
by_salary_desc = sorted(employees, key=get_salary, reverse=True)

# lambda
by_salary_desc = sorted(employees, key=lambda e: e["salary"], reverse=True)
```

**Output:**
```
{'name': 'Bob',   'salary': 80000, 'age': 20}
{'name': 'Carol', 'salary': 60000, 'age': 25}
{'name': 'Alice', 'salary': 50000, 'age': 30}
```

| `list.sort(key=fn)` | `sorted(list, key=fn)` |
|---|---|
| Modifies the original list | Returns a new list |
| Returns `None` | Returns the sorted list |
| Only works on lists | Works on any iterable |

---

## 2. `min()` — find the item with the smallest key value

`min()` calls the key function on every item, then returns the **whole item** that produced the smallest value — not the value itself.

### Named function version

```python
def get_age(e):
    return e["age"]

def get_salary(e):
    return e["salary"]

youngest   = min(employees, key=get_age)
lowest_paid = min(employees, key=get_salary)

print("Youngest :", youngest)
print("Lowest   :", lowest_paid)
```

### Lambda version

```python
youngest    = min(employees, key=lambda e: e["age"])
lowest_paid = min(employees, key=lambda e: e["salary"])

print("Youngest :", youngest)
print("Lowest   :", lowest_paid)
```

**Output (same for both):**
```
Youngest : {'name': 'Bob',   'salary': 80000, 'age': 20}
Lowest   : {'name': 'Alice', 'salary': 50000, 'age': 30}
```

---

## 3. `max()` — find the item with the largest key value

### Named function version

```python
def get_age(e):
    return e["age"]

def get_salary(e):
    return e["salary"]

oldest       = max(employees, key=get_age)
highest_paid = max(employees, key=get_salary)

print("Oldest  :", oldest)
print("Highest :", highest_paid)
```

### Lambda version

```python
oldest       = max(employees, key=lambda e: e["age"])
highest_paid = max(employees, key=lambda e: e["salary"])

print("Oldest  :", oldest)
print("Highest :", highest_paid)
```

**Output (same for both):**
```
Oldest  : {'name': 'Alice', 'salary': 50000, 'age': 30}
Highest : {'name': 'Bob',   'salary': 80000, 'age': 20}
```

---

## 4. `map()` — apply a function to every item, get back transformed results

`map(fn, iterable)` calls `fn` on each item and returns a **map object** (lazy — not computed yet).  
Wrap it in `list()` to see the results. The original list is untouched.

### Example A — extract all salaries

#### Named function

```python
def get_salary(e):
    return e["salary"]

salaries = list(map(get_salary, employees))
print("All salaries:", salaries)
```

#### Lambda

```python
salaries = list(map(lambda e: e["salary"], employees))
print("All salaries:", salaries)
```

**Output (same for both):**
```
All salaries: [50000, 80000, 60000]
```

---

### Example B — apply a 10% raise to every employee

#### Named function

```python
def apply_raise(e):
    return {
        "name":   e["name"],
        "salary": e["salary"] * 1.10,
        "age":    e["age"]
    }

raised = list(map(apply_raise, employees))

print("After 10% raise:")
for e in raised:
    print(e)
```

#### Lambda

```python
raised = list(map(
    lambda e: {"name": e["name"], "salary": e["salary"] * 1.10, "age": e["age"]},
    employees
))

print("After 10% raise:")
for e in raised:
    print(e)
```

**Output (same for both):**
```
After 10% raise:
{'name': 'Alice', 'salary': 55000.0, 'age': 30}
{'name': 'Bob',   'salary': 88000.0, 'age': 20}
{'name': 'Carol', 'salary': 66000.0, 'age': 25}
```

> Notice: the lambda version becomes hard to read when the transformation is multi-line.  
> This is a natural point to prefer a named function.

---

### Example C — build name labels

#### Named function

```python
def make_label(e):
    return f"{e['name']} (age {e['age']})"

labels = list(map(make_label, employees))
print("Labels:", labels)
```

#### Lambda

```python
labels = list(map(lambda e: f"{e['name']} (age {e['age']})", employees))
print("Labels:", labels)
```

**Output (same for both):**
```
Labels: ['Alice (age 30)', 'Bob (age 20)', 'Carol (age 25)']
```

---

## 5. `filter()` — keep only the items that pass a test

`filter(fn, iterable)` calls `fn` on each item.  
- If `fn` returns `True` (or truthy) → item is **kept**  
- If `fn` returns `False` (or falsy) → item is **dropped**

Returns a **filter object** — wrap in `list()` to see results.

### Example A — employees earning more than 55000

#### Named function

```python
def earns_above_55k(e):
    return e["salary"] > 55000

high_earners = list(filter(earns_above_55k, employees))

print("High earners:")
for e in high_earners:
    print(e)
```

#### Lambda

```python
high_earners = list(filter(lambda e: e["salary"] > 55000, employees))

print("High earners:")
for e in high_earners:
    print(e)
```

**Output (same for both):**
```
High earners:
{'name': 'Bob',   'salary': 80000, 'age': 20}
{'name': 'Carol', 'salary': 60000, 'age': 25}
```

---

### Example B — employees aged 25 or older

#### Named function

```python
def is_25_or_older(e):
    return e["age"] >= 25

seniors = list(filter(is_25_or_older, employees))

print("Age 25 or older:")
for e in seniors:
    print(e)
```

#### Lambda

```python
seniors = list(filter(lambda e: e["age"] >= 25, employees))

print("Age 25 or older:")
for e in seniors:
    print(e)
```

**Output (same for both):**
```
Age 25 or older:
{'name': 'Alice', 'salary': 50000, 'age': 30}
{'name': 'Carol', 'salary': 60000, 'age': 25}
```



## When to use a named function vs a lambda

| Situation | Prefer |
|---|---|
| Teaching for the first time | Named function — easier to read and debug |
| Simple one-liner expression | Lambda |
| Multi-line or complex logic | Named function |
| Reusing the same logic in multiple places | Named function |
| Quick inline one-off transformation | Lambda |

---

## Quick comparison

| Function | Input | Output | Changes original? |
|---|---|---|---|
| `sorted(lst, key=fn)` | list | new sorted list | No |
| `list.sort(key=fn)` | list | None (in-place) | Yes |
| `min(lst, key=fn)` | list | one item (whole dict) | No |
| `max(lst, key=fn)` | list | one item (whole dict) | No |
| `map(fn, lst)` | list | new transformed values | No |
| `filter(fn, lst)` | list | subset of original items | No |

---

## All five together — named function version

```python
from functools import reduce

employees = [
    {"name": "Alice", "salary": 50000, "age": 30},
    {"name": "Bob",   "salary": 80000, "age": 20},
    {"name": "Carol", "salary": 60000, "age": 25},
]

def get_salary(e):      return e["salary"]
def get_age(e):         return e["age"]
def apply_raise(e):     return {"name": e["name"], "salary": e["salary"] * 1.10, "age": e["age"]}
def earns_above_55k(e): return e["salary"] > 55000
def add_salaries(acc, e): return acc + e["salary"]

print("=== sorted (by salary) ===")
for e in sorted(employees, key=get_salary):
    print(e)

print("\n=== min / max ===")
print("Youngest :", min(employees, key=get_age))
print("Oldest   :", max(employees, key=get_age))
print("Lowest   :", min(employees, key=get_salary))
print("Highest  :", max(employees, key=get_salary))

print("\n=== map (10% raise) ===")
for e in map(apply_raise, employees):
    print(e)

print("\n=== filter (salary > 55000) ===")
for e in filter(earns_above_55k, employees):
    print(e)

```

---

## All five together — lambda version

```python
from functools import reduce

employees = [
    {"name": "Alice", "salary": 50000, "age": 30},
    {"name": "Bob",   "salary": 80000, "age": 20},
    {"name": "Carol", "salary": 60000, "age": 25},
]

print("=== sorted (by salary) ===")
for e in sorted(employees, key=lambda e: e["salary"]):
    print(e)

print("\n=== min / max ===")
print("Youngest :", min(employees, key=lambda e: e["age"]))
print("Oldest   :", max(employees, key=lambda e: e["age"]))
print("Lowest   :", min(employees, key=lambda e: e["salary"]))
print("Highest  :", max(employees, key=lambda e: e["salary"]))

print("\n=== map (10% raise) ===")
for e in map(lambda e: {"name": e["name"], "salary": e["salary"] * 1.10, "age": e["age"]}, employees):
    print(e)

print("\n=== filter (salary > 55000) ===")
for e in filter(lambda e: e["salary"] > 55000, employees):
    print(e)

```

**Output (same for both scripts):**
```
=== sorted (by salary) ===
{'name': 'Alice', 'salary': 50000, 'age': 30}
{'name': 'Carol', 'salary': 60000, 'age': 25}
{'name': 'Bob',   'salary': 80000, 'age': 20}

=== min / max ===
Youngest : {'name': 'Bob',   'salary': 80000, 'age': 20}
Oldest   : {'name': 'Alice', 'salary': 50000, 'age': 30}
Lowest   : {'name': 'Alice', 'salary': 50000, 'age': 30}
Highest  : {'name': 'Bob',   'salary': 80000, 'age': 20}

=== map (10% raise) ===
{'name': 'Alice', 'salary': 55000.0, 'age': 30}
{'name': 'Bob',   'salary': 88000.0, 'age': 20}
{'name': 'Carol', 'salary': 66000.0, 'age': 25}

=== filter (salary > 55000) ===
{'name': 'Bob',   'salary': 80000, 'age': 20}
{'name': 'Carol', 'salary': 60000, 'age': 25}

```

---

