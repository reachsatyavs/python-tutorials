# Functions

How to define and call functions in Python — from basic `def` to lambda, argument types (`*args`, `**kwargs`), and when to choose lambda vs list comprehension.

---

## Contents

| File | Type | What it covers |
|------|------|----------------|
| `Functions.md` | Notes | What a function is, types of functions, all argument types (`*`, `**`, `/`, defaults), 10 sample functions |
| `Lambda.md` | Notes | Lambda syntax, characteristics, use with `map`/`filter`/`sorted`, limitations, when to use |
| `Lambda_vs_ListComprehension.md` | Notes | Side-by-side comparison — when to pick lambda vs list comprehension |
| `functions_examples.py` | Script | 14 runnable real-world examples: `*args`, `**kwargs`, keyword-only, recursion, higher-order functions, invoice calculator |

---

## Key Concepts

### Defining a function

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))   # Hello, Alice!
```

### Types of functions

| Type | Description | Example |
|------|-------------|---------|
| Built-in | Provided by Python | `len()`, `print()`, `sum()` |
| User-defined | Written with `def` | `def my_func(): ...` |
| Lambda | Anonymous, one-liner | `lambda x: x * 2` |
| Method | Bound to an object | `"hello".upper()` |

### Argument types

```python
def example(pos,             # positional
            kw="default",    # keyword with default
            *args,           # extra positional → tuple
            kw_only,         # keyword-only (after *)
            **kwargs):       # extra keyword → dict
    pass
```

| Syntax | Meaning |
|--------|---------|
| `a, b` | Positional arguments |
| `a=1` | Default value |
| `*args` | Any number of extra positional args → tuple |
| `**kwargs` | Any number of extra keyword args → dict |
| `*` | Everything after must be keyword-only |
| `/` | Everything before is positional-only |

### Lambda

```python
square   = lambda x: x ** 2
is_even  = lambda n: n % 2 == 0
add      = lambda a, b: a + b
```

Common with `sorted`, `map`, `filter`:

```python
names = ["Zoe", "Ana", "Mohan"]
print(sorted(names, key=lambda n: len(n)))   # sort by length
```

### Lambda vs list comprehension

| Goal | Use |
|------|-----|
| Pass behaviour to another function | Lambda |
| Build a new list | List comprehension |
| Filter + transform in one step | List comprehension |
| Replace `map` / `filter` | List comprehension (usually clearer) |

---

## Learning order

1. `Functions.md` — what functions are, all argument types, 10 examples
2. `Lambda.md` — anonymous functions, when and how to use them
3. `Lambda_vs_ListComprehension.md` — knowing which tool to reach for
