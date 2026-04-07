## Overview

**Copy-paste examples (no functions required):** see [`ControlFlowExamples.md`](ControlFlowExamples.md) — run one snippet at a time in a file or notebook cell.

Control flow determines how a program makes decisions and repeats actions.

Python provides:

- `if / elif / else` → conditional branching
- `while` → condition-controlled loop
- `for` → iterable-controlled loop
- `break`, `continue`, and `pass` → loop / block modifiers
- `for ... else` / `while ... else` → run a block when the loop **finishes without** `break` (often used for “not found” searches)
- `match / case` (Python **3.10+**) → structural pattern matching (optional advanced topic)

---

## 1. Conditional Statements (`if / elif / else`)

### Syntax

```python
if condition:
    block
elif another_condition:
    block
else:
    block
```

### Example — environment-based configuration

```python
env = "prod"

if env == "prod":
    db_url = "prod.db.company.com"
elif env == "stage":
    db_url = "stage.db.company.com"
else:
    db_url = "localhost"

print(db_url)
```

### Truthiness (common gotcha)

Python treats many values as “false” in `if`: `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, etc.  
For **optional values**, prefer an explicit check when it matters:

```python
# Often what you want for "missing" optional config
if value is None:
    ...

# Different from "empty string" or 0
if not value:
    ...  # treats 0 and "" as false too
```

### `pass` — placeholder block

Use when syntax requires a body but you have nothing to do yet:

```python
def todo_later():
    pass
```

### Before vs. After (production style)

#### Nested “arrow” code (harder to read)

```python
def process_user_data(user):
    if user is not None:
        if user.is_active:
            if user.has_permission:
                return "Allowed"
            else:
                return "No Permission"
        else:
            return "Inactive"
    else:
        return "No User"
```

#### Guard clause pattern (flatter, clearer)

```python
def process_user_data(user):
    if user is None:
        return "No User"
    if not user.is_active:
        return "Inactive"
    if not user.has_permission:
        return "No Permission"
    return "Allowed"
```

**Benefits:** less nesting, early exits, happy path stays obvious.

**Fail fast with exceptions** when invalid state is an error:

```python
def calculate_ratio(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b
```

`**continue` in loops** (guard-style skip):

```python
for file in files:
    if not file.is_valid():
        continue
    process(file)
```

---

## 2. `while` Loop (condition-controlled)

### Retry logic

```python
max_retries = 3
attempt = 1

while attempt <= max_retries:
    print(f"Attempt {attempt}")
    attempt += 1
```

### `while ... else`

The `else` block runs **only if the loop exits normally** (condition becomes false), **not** if you `break` out.

```python
attempts = 0
while attempts < 3:
    if success():
        break
    attempts += 1
else:
    print("Exhausted retries without success")
```

### Infinite loop with `break`

```python
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == "exit":
        break
```

---

## 3. `for` Loop (iterable-controlled)

```python
services = ["auth", "billing", "notifications"]
for service in services:
    print("Deploying:", service)
```

### `range()`

```python
for i in range(5):
    print(i)

for i in range(1, 10, 2):
    print(i)
```

### `zip()` — parallel iteration

```python
names = ("A", "B", "C")
scores = (90, 80, 85)
for name, score in zip(names, scores):
    print(name, score)
```

Python 3.10+ also supports `zip(..., strict=True)` to raise if lengths differ.

### `for ... else`

Runs if the loop completes **without** `break` (useful for “search and not found”):

```python
for item in items:
    if item.id == target_id:
        print("Found")
        break
else:
    print("Not found")
```

---

## 4. Loop + Condition Pattern

```python
numbers = [10, 15, 22, 33, 40]
for n in numbers:
    if n % 2 == 0:
        print("Even:", n)
```

---

## 5. `break` and `continue`

- `**break**` — exit the innermost loop immediately.  
- `**continue**` — skip the rest of this iteration; go to the next one.

---

## 6. Production-Oriented Patterns

### Validate → process

```python
for user in users:
    if not user.is_active:
        continue
    process(user)
```

### Search pattern

```python
for item in items:
    if item.id == target_id:
        print("Found")
        break
```

### Accumulator pattern

```python
total = 0
for price in prices:
    total += price
print(total)
```

---

## 7. Nested Loops

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Nested loops can mean **O(n²)** time or worse—keep inner work cheap when data grows.

---

## 8. Structural pattern matching (`match` / `case`) — Python 3.10+

Good for branching on **shape** of data (not always better than `if`/`dict` dispatch—use when readability wins):

```python
def http_message(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Other"
```

---

## 9. When to Use What


| Scenario                         | Prefer                                   |
| -------------------------------- | ---------------------------------------- |
| Known iteration count            | `for` + `range`                          |
| Iterating a collection           | `for`                                    |
| Need index + value               | `for i, x in enumerate(...)`             |
| Parallel iteration               | `for a, b in zip(...)`                   |
| Retry / polling / unknown length | `while`                                  |
| Loop finished without `break`    | `for`/`while` + `else`                   |
| Deeply nested `if` chains        | Guard clauses, `dict` lookup, or `match` |


---

## 10. Common Pitfalls

1. **Indentation** — blocks after `if`/`for`/`while` must be indented consistently.
2. **`=` vs `==`** — assignment vs comparison.
3. **Infinite `while`** — ensure the condition changes or you `break`.
4. **`for` vs `while`** — `for` for iterables; `while` when exit depends on evolving state.
5. **Mutable default arguments** — not control flow per se, but often confused near `if`/`def`; avoid `def f(x=[])` patterns.

**Practice:** standalone snippets are in [`ControlFlowExamples.md`](ControlFlowExamples.md).
