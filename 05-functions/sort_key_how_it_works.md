# `list.sort(key=...)` — A Deep Dive

> One example. Multiple Python concepts. Built up step by step.
```python

employees = [
    {"name": "A", "salary": 50000, "age": 30},
    {"name": "B", "salary": 80000, "age": 20},
    {"name": "C", "salary": 60000, "age": 25},
]

print("------Before Sort ---------")
for e in employees:
  print(e)

def get_salary(e):
  return(e["salary"])


employees.sort(key=get_salary)
print("------After Sort ---------")
for e in employees:
  print(e)

```
---

## What concepts does this one line teach?

```python
employees.sort(key=get_salary)
```

This single line quietly contains:

- Passing functions as arguments
- Callback functions
- Sorting algorithm behaviour
- Function references vs function calls
- Functions as first-class objects in Python

Let's deeply understand each one.

---

## Step 1 — What is `employees`?

```python
employees = [
    {"name": "A", "salary": 50000, "age": 30},
    {"name": "B", "salary": 80000, "age": 20},
    {"name": "C", "salary": 60000, "age": 25},
]
```

A **list of dictionaries**. Each item in the list is one employee — a dict with three keys: `name`, `salary`, `age`.

```
Index 0 → {"name": "A", "salary": 50000, "age": 30}
Index 1 → {"name": "B", "salary": 80000, "age": 20}
Index 2 → {"name": "C", "salary": 60000, "age": 25}
```

---

## Step 2 — What is `get_salary`?

```python
def get_salary(e):
    return e["salary"]
```

This function:
- Receives **one employee dictionary**
- Returns the **salary value** from it

Test it in isolation first — before touching `.sort()`:

```python
get_salary({"name": "A", "salary": 50000, "age": 30})
# returns → 50000

get_salary({"name": "B", "salary": 80000, "age": 20})
# returns → 80000
```

Nothing magical. Just a function that looks inside a dict and pulls out the salary.

---

## Step 3 — Discover `.sort()` using `help()`

Before calling `.sort()`, ask Python itself what it expects:

```python
help(employees.sort)
```

```
sort(*, key=None, reverse=False) method of list instance

    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, based on their function values.
```

Two things to notice:

**`key=None` by default** — if you pass nothing, sort compares items directly. That is why sorting a plain list of numbers works without `key=`.

**"apply it once to each list item"** — sort calls your function once per item, uses the return value for comparison, and reorders the original items.

So `key=` expects a **reference to a callable** — a function that sort will call on each item when it is ready.

---

## Step 4 — The most important part: `key=get_salary` vs `key=get_salary()`

This is where most students get confused. Read this carefully.

```python
# ✅ correct
employees.sort(key=get_salary)

# ❌ wrong
employees.sort(key=get_salary())
```

### `get_salary` — function reference (no parentheses)

```python
key=get_salary
```

You are **not calling** the function. You are handing it over — like giving someone a recipe card. Sort stores it and calls it **later**, once per item, passing each employee as the argument.

### `get_salary()` — function call (with parentheses)

```python
key=get_salary()
```

You are calling the function **right now** — but with no argument. Sort has not given you an employee yet. This crashes immediately:

```
TypeError: get_salary() missing 1 required positional argument: 'e'
```

### The recipe card analogy

| Syntax | Analogy |
|---|---|
| `get_salary` | Handing someone the **recipe card** |
| `get_salary()` | Handing someone the **cooked dish right now** |

Sort wants the recipe card — not the cooked dish. It will cook once per item, when it is ready.

### Function reference vs function call

| Code | Meaning |
|---|---|
| `get_salary` | The function object — not called yet |
| `get_salary()` | Execute the function right now |

---

## Step 5 — What sort does internally, call by call

When `employees.sort(key=get_salary)` runs, sort first calls `get_salary` on every item:

```
Call 1 → get_salary({"name":"A","salary":50000,"age":30})
         e["salary"] → 50000
         returns 50000

Call 2 → get_salary({"name":"B","salary":80000,"age":20})
         e["salary"] → 80000
         returns 80000

Call 3 → get_salary({"name":"C","salary":60000,"age":25})
         e["salary"] → 60000
         returns 60000
```

Sort now has a picture like this internally:

| Employee item | Comparison value |
|---|---|
| `{"name":"A", ...}` | 50000 |
| `{"name":"B", ...}` | 80000 |
| `{"name":"C", ...}` | 60000 |

---

## Step 6 — Sort compares those values and reorders

```
50000 vs 80000 vs 60000

smallest → 50000 → item A stays at index 0
middle   → 60000 → item C moves to index 1
largest  → 80000 → item B moves to index 2
```

Sort now reorders the **whole items** — not just the salary numbers:

```
Index 0 → {"name": "A", "salary": 50000, "age": 30}  ← was already here
Index 1 → {"name": "C", "salary": 60000, "age": 25}  ← moved from index 2
Index 2 → {"name": "B", "salary": 80000, "age": 20}  ← moved from index 1
```

The salary numbers (50000, 80000, 60000) are **thrown away** after the decision is made. The list still contains the full dicts — all three keys travel together as one unit.

---

## Step 7 — The full visual flow

```
employees.sort(key=get_salary)
                    │
                    │  sort stores get_salary — does NOT call it yet
                    │
                    ▼
         for each item in the list:
             value = get_salary(item)   ← sort calls YOUR function
                    │
                    ▼
         gets back: 50000 / 80000 / 60000
                    │
                    ▼
         sort compares those numbers
                    │
                    ▼
         sort moves WHOLE items to new positions
                    │
                    ▼
         salary numbers discarded — list has full dicts
```

---

## Step 8 — This is called a Callback Function

`get_salary` is a **callback** — a function you pass to another function, which calls it back when it needs it.

Sort says: *"Give me a function that tells me how to compare items. I will call it back myself when I am ready."*

You never write `get_salary(something)` yourself. Sort does that.

This pattern is everywhere in Python:

| Where | Example |
|---|---|
| Sorting | `list.sort(key=fn)` |
| Filtering | `filter(fn, data)` |
| Mapping | `map(fn, data)` |
| GUI programming | button click handlers |
| Web frameworks | route handler functions |
| Event handling | `on_click=handler` |
| AI pipelines | transform functions per step |

---

## Step 9 — Why this works: functions are objects in Python

This line is only possible because of a fundamental Python feature:

> **In Python, functions are first-class objects.**

That means a function can be:

```python
# stored in a variable
fn = get_salary

# passed to another function
employees.sort(key=get_salary)

# returned from a function
def make_getter(field):
    return lambda e: e[field]   # returns a function
```

`get_salary` is not special syntax — it is just an object that happens to be callable. You can pass it around exactly like you pass a number or a string.

```python
print(type(get_salary))     # <class 'function'>
print(callable(get_salary)) # True
```

---

## Step 10 — Lambda is the same thing, written inline

```python
# named function version
def get_salary(e):
    return e["salary"]

employees.sort(key=get_salary)

# lambda version — internally identical
employees.sort(key=lambda e: e["salary"])
```

Both do exactly the same thing. The lambda is just a function without a name — written inline. Prefer the named function when teaching; use lambda once students understand the concept.

---

## Step 11 — Making it generalised: sort by any field

What if we want to sort by `name`, `salary`, or `age` without writing a new function each time?

```python
# approach 1 — lambda closes over the field variable
field = "salary"
employees.sort(key=lambda e: e[field])

# change field to sort by something else
field = "age"
employees.sort(key=lambda e: e[field])
```

```python
# approach 2 — function that returns a function
def sort_by(field):
    def get_field(employee):
        return employee[field]
    return get_field

employees.sort(key=sort_by("salary"))   # sort by salary
employees.sort(key=sort_by("age"))      # sort by age
employees.sort(key=sort_by("name"))     # sort by name
```

`sort_by("salary")` is called once — it returns `get_field`. Sort then calls `get_field` once per item.

---

## Key questions for students

**Q: Sort called `get_salary` — but who passed the argument `e`?**
Sort did. You never write `get_salary(something)` yourself.

**Q: What did sort do with 50000, 80000, 60000 after comparing?**
Threw them away. They were only used to decide the order.

**Q: Does sort know the items are dicts with name, salary, age?**
No. Sort is completely blind to what is inside. It only sees what `get_salary` returned.

**Q: What if we wanted to sort by age instead?**
```python
employees.sort(key=lambda e: e["age"])
# B(20), C(25), A(30)
```

---

## Complete working example

```python
import json

employees = [
    {"name": "A", "salary": 50000, "age": 30},
    {"name": "B", "salary": 80000, "age": 20},
    {"name": "C", "salary": 60000, "age": 25},
]

print("------ Before sort ---------")
for e in employees:
    print(e)

# define the key function
def get_salary(e):
    return e["salary"]

# hand it to sort — not get_salary(), just get_salary
employees.sort(key=get_salary)

print("\n------ After sort (by salary) ---------")
print(json.dumps(employees, indent=2))

# same result with lambda
employees.sort(key=lambda e: e["age"])

print("\n------ After sort (by age) ---------")
print(json.dumps(employees, indent=2))
```

---

## One-line takeaway

> `key=get_salary` means: *"Use this function to extract a comparison value from each item during sorting. Sort will call it — you just write the rule."*

---

## Summary

| Concept | What it means here |
|---|---|
| Passing functions as arguments | `key=get_salary` — function handed to sort |
| Callback function | Sort calls `get_salary` back when it needs it |
| Function reference | `get_salary` — the object, not the result |
| Function call | `get_salary()` — executes now, wrong here |
| Functions as objects | Python lets you pass, store, return functions |
| Sorting behaviour | Sort uses key values to compare, moves whole items |

---

*Python Series · `github.com/reachsatyavs/python-tutorials`*
