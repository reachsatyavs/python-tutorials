# Comprehensions & generators

Notes for **module 06** — building collections and lazy iterators without writing long `for` loops for every case.

---

## 1. Why this topic exists

You already know how to build a list with a loop:

```python
squares = []
for n in range(5):
    squares.append(n * n)
```

A **list comprehension** expresses the same idea in one line. **Generator expressions** and **`yield`** functions do something similar but **do not store every result in memory at once**—they produce values **when asked** (lazy).

---

## 2. List comprehensions

**Syntax:** `[ expression for name in iterable if condition_optional ]`

- The `for … in …` mirrors a loop; `expression` is what each new element becomes.
- The `if` part filters; it is optional.

```python
[n * n for n in range(5)]                    # [0, 1, 4, 9, 16]
[n for n in range(10) if n % 2 == 0]       # even numbers
```

**Nested loops** (read left-to-right like nested `for` loops):

```python
[(i, j) for i in range(2) for j in range(3)]
```

Use nested comprehensions sparingly—deep nesting hurts readability.

---

## 3. Dict and set comprehensions

**Dict:** `{ key_expr: value_expr for name in iterable if optional }`

```python
words = ["apple", "pie"]
{w: len(w) for w in words}    # {'apple': 5, 'pie': 3}
```

**Set:** `{ expression for name in iterable if optional }`

```python
{n % 3 for n in range(10)}    # remainder values, unique
```

---

## 4. Generator expressions

Same shape as a list comprehension, but **round parentheses** (often call them “genexps”):

```python
g = (n * n for n in range(5))
next(g)   # 0
next(g)   # 1
list(g)   # consume rest: [4, 9, 16]
```

Passing a genexp to a function: **one pair of parentheses** can do double duty—no extra parens needed inside `sum(...)`:

```python
sum(n * n for n in range(5))   # generator expression, not a tuple
```

---

## 5. Generator functions (`yield`)

A function that uses **`yield`** returns a **generator iterator** when you call it—not the final “answer” in one shot.

```python
def count_up_to(n):
    k = 1
    while k <= n:
        yield k
        k += 1

for x in count_up_to(3):
    print(x)
```

- **`return`** ends the function and stops the generator.
- **`yield`** pauses, sends a value out, and resumes on the next iteration.

---

## 6. Eager vs lazy (memory and behaviour)

| Approach | Typical memory | When it helps |
|----------|----------------|---------------|
| List comprehension | Holds all items | Small or bounded results; you need random access or length |
| Generator expression / `yield` | O(1) extra for the iterator | Large files, pipelines, “infinite” sequences |

---

## 7. Common pitfalls

1. **Consuming a generator twice** — iterators are one-shot; call the function again or rebuild the genexp.
2. **Side effects inside comprehensions** — avoid `append`-style mutations; keep expressions pure when possible.
3. **Shadowing** — the loop variable `n` exists after the comprehension in Python 3 (same as a normal `for` loop).

---

## 8. Relation to `map` / `filter` / lambda

`map` and `filter` return iterators in Python 3. Comprehensions are often **more readable** for simple transforms. See **module 05** — `Lambda_vs_ListComprehension.md`.

---

## References

- [Python tutorial — list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Generator expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)
- [yield](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)
