# Module 06 — Comprehensions & generators

**Yes — one module is the right place.** List / dict / set comprehensions and generators are the same *idea* (iterate, optionally filter, produce values) with two flavours: **eager** (materialise a whole `list`, `dict`, or `set`) vs **lazy** (generator expression or `yield` function). Teaching them together makes the memory trade-off obvious.

**Prerequisites:** [`05-functions/`](../05-functions/README.md) (loops, functions, iterables). Optional cross-read: [`Lambda_vs_ListComprehension.md`](../05-functions/Lambda_vs_ListComprehension.md).

---

## Contents

| File | Type | What it covers |
|------|------|----------------|
| [`Comprehensions.md`](Comprehensions.md) | Notes | Full topic write-up — list / set / dict comprehensions, generator expressions, mental model, cheat sheet |
| [`Python_Comprehensions.pptx`](Python_Comprehensions.pptx) | Slides | Deck aligned with `Comprehensions.md` |

---

## Learning order

1. Walk through [`Comprehensions.md`](Comprehensions.md) (or the slides) in section order.
2. Add your own examples script here when ready (e.g. `examples.py`).

---

## Quick mental model

| You write | You get |
|-----------|--------|
| `[ ... for ... ]` | New `list` (all items now) |
| `{ k: v for ... }` | New `dict` |
| `{ ... for ... }` | New `set` |
| `( ... for ... )` or `f(... for ...)` | Generator iterator (lazy) |
| `def f(): yield x` | Generator function → iterator |

---

## Next module

**07 — File handling** (planned): paths, `open`, context managers.
