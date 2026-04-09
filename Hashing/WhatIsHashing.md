# Understanding Hashing in Python

This README explains **how hashing works in Python** using **simple, runnable examples**.
It is designed so that:
- **run every example**
- **understand the concept**
- No internal or hidden Python behavior is required

---

## What Is Hashing? 

> **Hashing converts a key into a number so Python can quickly find the value without searching.**

---

## Why Hashing Exists

Without hashing:
- Python would have to **search every element**
- Lookups would be slow (`O(n)`)

With hashing:
- Python jumps directly to the location
- Lookups are fast (`O(1)` on average)

This is why:
- `dict`
- `set`

are extremely fast data structures.

---

## Step-by-Step Example (Runnable)

### Step 1: Create a dictionary

```python
marks = {}
marks["Alice"] = 95
marks["Bob"] = 88
```

✔ This runs  
✔ Nothing special yet  

---

### Step 2: What Python does internally (conceptually)

When you write:

```python
marks["Alice"] = 95
```

Python internally computes a hash:

```text
hash("Alice") → some number
```

You can see this yourself:

```python
print(hash("Alice"))
print(hash("Bob"))
```

✔ Try running this  
✔ You will see integers  

---

## How Hash Is Used (Mental Model)

Python internally works like this:

```
key → hash(key) → bucket → value
```

### Example

```python
value = marks["Alice"]
print(value)
```

Python:
1. Computes `hash("Alice")`
2. Finds the correct bucket
3. Returns `95`

✅ No searching  
✅ Very fast  

---

## Why Hashing Is Faster Than Lists

### List lookup (slow)

```python
students = ["Bob", "Alice", "Eve"]
print("Alice" in students)
```

Python checks:
```
Bob ❌
Alice ✅
```

⏱ Time: `O(n)`

---

### Set lookup (fast, hash-based)

```python
students = {"Bob", "Alice", "Eve"}
print("Alice" in students)
```

Python:
```
hash("Alice") → found
```

⏱ Time: `O(1)`

---

## Why Dictionary Keys Must Be Immutable

### Safe example (immutable key)

```python
d = {}
d[(1, 2)] = "tuple key"
print(d[(1, 2)])
```

✔ Works  
✔ Tuple is immutable  
✔ Hash never changes  

---

### Unsafe example (mutable key – NOT allowed)

```python
d = {}
d[[1, 2]] = "list key"
```

❌ Raises:
```
TypeError: unhashable type: 'list'
```

---

## Why Python Forbids Mutable Keys

Imagine this was allowed (it is NOT):

```python
lst = [1, 2]
d = {lst: "value"}

lst.append(3)

print(d[lst])   # ❓ Where is the key now?
```

- The list changed
- Its hash would change
- Python would lose the key

🚫 Python prevents this by disallowing mutable keys.

---

## Hashable vs Non-Hashable (Try This)

```python
print(hash(10))          # ✅
print(hash("hello"))     # ✅
print(hash((1, 2)))      # ✅

hash([1, 2])             # ❌ TypeError
hash({1, 2})             # ❌ TypeError
```

---

## Real-Life Analogy

- **Hashable object** → ID card number
- **Mutable object** → Home address

You index people by:
✔ ID number  
❌ Not by address  

---

## One-Line Explanation

> **Hashing is a shortcut that converts a key into a number so Python can find values instantly instead of searching.**

---

## Blackboard Summary

```
Dictionary:
Key → hash(key) → bucket → value

Rules:
- Key must be immutable
- Hash must never change
- That’s why lists and sets cannot be keys
```


