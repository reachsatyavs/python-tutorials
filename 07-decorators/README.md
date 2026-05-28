# Module 07 — Decorators

A decorator is a function that **wraps another function** to add behaviour before, after, or around it — without changing the original function's code. It is Python's clean solution to cross-cutting concerns like logging, timing, authentication, and caching.

**Prerequisites:** `[05-functions/](../05-functions/README.md)` — closures, `*args`/`**kwargs`, functions as first-class objects.

---

## Contents

| File | Type | What it covers |
| ---- | ---- | -------------- |
| `[Decorators.md](Decorators.md)` | Notes | Full topic write-up — what decorators are, `@` syntax, wrappers, `functools.wraps`, stacking, decorator factories, real-world uses, built-in decorators, cheat sheet |
| `[decorators.py](decorators.py)` | Script | 16 runnable examples — from bare wrapper to class-based decorators, logging, timing, caching, retry, auth |

---

## Learning order

1. Read `[Decorators.md](Decorators.md)` in section order — each section builds on the previous one.
2. Run `python decorators.py` to see all examples live on the terminal.
3. Try the exercises at the bottom of `Decorators.md`.

---

## Quick mental model

| You write | What happens |
| --------- | ------------ |
| `def decorator(func): ...` | A function that receives a function |
| `def wrapper(*args, **kwargs): ...` | The new behaviour wraps the original |
| `return wrapper` | The decorator hands back the wrapper |
| `@decorator` above a `def` | Python replaces the function with its decorated version |
| `@decorator` ≡ `fn = decorator(fn)` | The `@` line is just syntactic sugar |

---

## Next module

**08 — File Handling** (planned): `open`, `with`, reading/writing files, `pathlib`, CSV, JSON.
