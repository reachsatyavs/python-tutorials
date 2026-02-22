# Lambda vs List Comprehension

## Purpose
Both **lambda functions** and **list comprehensions** are used to write concise Python code.
They solve different problems and should not be confused.

---

## What Lambda Is For
- Represents **small logic**
- Used when **passing behavior**
- Common with `map`, `filter`, `sorted`, `min`, `max`

```python
squares = list(map(lambda x: x*x, [1,2,3]))
```

---

## What List Comprehension Is For
- Used for **creating lists**
- Combines loop + condition + expression
- Replaces `map` + `filter` in many cases

```python
squares = [x*x for x in [1,2,3]]
```

---

## Key Differences

| Aspect | Lambda | List Comprehension |
|---|---|---|
| Produces | Function | List |
| Purpose | Pass logic | Build data |
| Readability | Medium | High |
| Best with | map/filter/sort | loops + conditions |

---

## Rule to Note
> **If you are creating a list → list comprehension**  
> **If you are passing logic → lambda**
