# Control Flow

How Python makes decisions and repeats actions — `if`, `while`, `for`, `break`, `continue`, `pass`, guard clauses, and more.

---

## Contents

| File | Type | What it covers |
|------|------|----------------|
| `ControlFlow.md` | Notes | Concepts, syntax, guard clauses, `for`/`while` + `else`, `match`/`case` (3.10+), when to use what |
| `ControlFlowExamples.md` | Examples | 40+ standalone copy-paste snippets — one per concept, no functions needed |
| `Python_ControlFlow.pptx` | Slides | Presentation slides for the control flow topic |

---

## Key Concepts

### `if` / `elif` / `else` — make decisions

```python
status = 404

if status == 200:
    print("OK")
elif status == 404:
    print("Not Found")
else:
    print("Other")
```

### `while` — repeat while a condition is true

```python
attempt = 1
while attempt <= 3:
    print("Attempt", attempt)
    attempt += 1
```

### `for` — iterate over a collection

```python
for service in ["auth", "billing", "search"]:
    print("Deploy:", service)
```

### `break` and `continue`

- **`break`** — exit the loop immediately
- **`continue`** — skip this iteration, go to the next
- **`pass`** — do nothing (placeholder for an empty block)

### Guard clauses (flat code beats nested code)

```python
# ❌ Nested (harder to read)
if user:
    if user.is_active:
        if user.has_permission:
            result = "Allowed"

# ✅ Guard style (flat, clear)
if user is None:       result = "No User"
elif not user.is_active:    result = "Inactive"
elif not user.has_permission: result = "No Permission"
else:                       result = "Allowed"
```

### `for` / `while` + `else`

The `else` block runs **only if the loop finished without a `break`** — useful for "search and not found":

```python
for item in items:
    if item["id"] == target:
        print("Found")
        break
else:
    print("Not found")
```

---

## When to use what

| Scenario | Use |
|----------|-----|
| Iterate a known list or range | `for` |
| Need index + value | `for i, x in enumerate(...)` |
| Two lists in parallel | `for a, b in zip(...)` |
| Retry / polling / unknown count | `while` |
| Deeply nested branches | Guard clauses or `match`/`case` |
| Loop finished without break | `for`/`while` + `else` |

---

## Using the examples

`ControlFlowExamples.md` has **standalone snippets** organised into sections:

- **A** — `if` / `elif` / `else` (13 examples)
- **B** — `while` (11 examples, including `while`/`else` and retry patterns)
- **C** — `for` (13 examples, including `zip`, `enumerate`, `for`/`else`)
- **D** — Guard clauses and flat vs nested code
- **E** — Common pitfalls

Copy any single example into a `.py` file or notebook cell and run it on its own.

---

## Learning order

1. `ControlFlow.md` — read the concepts and syntax
2. `ControlFlowExamples.md` — try the examples one by one
3. `Python_ControlFlow.pptx` — slides for classroom use
