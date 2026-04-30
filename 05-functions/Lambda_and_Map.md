# Lambda Functions & `map()` — From Simple to Complex

> A progressive guide for understanding lambda syntax and the `map()` function,
> with every example building on the previous one.

---

## Part 1 — Lambda Functions

### What is a Lambda?

A lambda is a **one-line anonymous function**. It has no name, no `def`, no `return` — just inputs and an expression.

```
lambda  <inputs>  :  <expression>
   ↑        ↑             ↑
keyword  parameters   auto-returned result
```

**Every lambda has an exact `def` equivalent:**

```python
# Regular function
def square(x):
    return x ** 2

# Same thing as lambda
square = lambda x: x ** 2
```

> 💡 **Read it like a sentence:** `lambda x: x ** 2` → *"Given x, give back x squared."*

---

### Level 1 — Single Input, Simple Expression

```python
# Double a number
double = lambda x: x * 2
print(double(5))        # 10

# Square a number
square = lambda x: x ** 2
print(square(4))        # 16

# Check if a number is even
is_even = lambda n: n % 2 == 0
print(is_even(6))       # True
print(is_even(7))       # False

# Get the length of a string
str_len = lambda s: len(s)
print(str_len("hello")) # 5
```

**Pattern:** `lambda x: <one thing done to x>`

---

### Level 2 — Two Inputs

```python
# Add two numbers
add = lambda a, b: a + b
print(add(3, 4))            # 7

# Multiply
multiply = lambda a, b: a * b
print(multiply(3, 4))       # 12

# Return the larger of two values
larger = lambda a, b: a if a > b else b
print(larger(10, 7))        # 10
print(larger(3, 9))         # 9

# Concatenate with separator
join = lambda s1, s2: s1 + " " + s2
print(join("Hello", "World"))  # Hello World
```

**Pattern:** `lambda a, b: <expression using both>`

> 💡 The ternary `a if condition else b` is allowed inside lambda — it's still one expression.

---

### Level 3 — Working with Strings and Collections

```python
# Uppercase first letter
capitalize = lambda s: s.capitalize()
print(capitalize("python"))     # Python

# Get the last character
last_char = lambda s: s[-1]
print(last_char("hello"))       # o

# Get second element of a tuple (very common in sorting!)
second = lambda t: t[1]
print(second(("Alice", 85)))    # 85

# Get value from a dict by key
get_name = lambda d: d["name"]
print(get_name({"name": "Bob", "age": 25}))  # Bob

# Reverse a string
reverse = lambda s: s[::-1]
print(reverse("python"))        # nohtyp
```

**Pattern:** `lambda x: x.<method>()` or `lambda x: x[index]`

---

### Level 4 — Used Inline with `sorted()`, `filter()`, `max()`

This is where lambda becomes most powerful — **passed directly as an argument**.

```python
students = [("Alice", 85), ("Bob", 72), ("Carol", 91), ("Dan", 65)]

# Sort by marks (ascending)
by_marks = sorted(students, key=lambda s: s[1])
print(by_marks)
# [('Dan', 65), ('Bob', 72), ('Alice', 85), ('Carol', 91)]

# Sort by marks (descending)
by_marks_desc = sorted(students, key=lambda s: s[1], reverse=True)
print(by_marks_desc)
# [('Carol', 91), ('Alice', 85), ('Bob', 72), ('Dan', 65)]

# Sort by name (alphabetical)
by_name = sorted(students, key=lambda s: s[0])
print(by_name)
# [('Alice', 85), ('Bob', 72), ('Carol', 91), ('Dan', 65)]

# Filter: only students who passed (>= 75)
passed = list(filter(lambda s: s[1] >= 75, students))
print(passed)
# [('Alice', 85), ('Carol', 91)]

# Find the top scorer
topper = max(students, key=lambda s: s[1])
print(topper)
# ('Carol', 91)
```

**Pattern:** `sorted(data, key=lambda item: item[field])`

---

### Level 5 — Lambda with Dicts and Real-world Data

```python
products = [
    {"name": "Laptop",  "price": 75000, "stock": 10},
    {"name": "Phone",   "price": 45000, "stock": 0},
    {"name": "Tablet",  "price": 30000, "stock": 5},
    {"name": "Monitor", "price": 20000, "stock": 3},
]

# Sort by price
by_price = sorted(products, key=lambda p: p["price"])
print([p["name"] for p in by_price])
# ['Monitor', 'Tablet', 'Phone', 'Laptop']

# Filter: only in-stock items
in_stock = list(filter(lambda p: p["stock"] > 0, products))
print([p["name"] for p in in_stock])
# ['Laptop', 'Tablet', 'Monitor']

# Find most expensive
priciest = max(products, key=lambda p: p["price"])
print(priciest["name"])   # Laptop

# Check if any item has 0 stock
out_of_stock = list(filter(lambda p: p["stock"] == 0, products))
print([p["name"] for p in out_of_stock])
# ['Phone']
```

---

### Level 6 — Lambda Stored in Collections (Advanced)

```python
# A list of transformation functions
transforms = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x - 10,
]

value = 5
results = [f(value) for f in transforms]
print(results)   # [6, 10, 25, -5]

# A dict of operations (like a mini calculator)
ops = {
    "add":  lambda a, b: a + b,
    "sub":  lambda a, b: a - b,
    "mul":  lambda a, b: a * b,
    "div":  lambda a, b: a / b,
}

print(ops["add"](10, 5))   # 15
print(ops["mul"](4, 3))    # 12

# Apply transforms in a pipeline
pipeline = [
    lambda x: x * 2,
    lambda x: x + 3,
    lambda x: x ** 2,
]

value = 4
for step in pipeline:
    value = step(value)
print(value)   # ((4*2)+3)^2 = 121
```

---

### Lambda — Quick Reference

| Use case | Lambda pattern |
|---|---|
| Transform a value | `lambda x: x * 2` |
| Two inputs | `lambda a, b: a + b` |
| Conditional | `lambda x: "yes" if x > 0 else "no"` |
| Access index | `lambda t: t[1]` |
| Access dict key | `lambda d: d["key"]` |
| Sort key | `sorted(data, key=lambda x: x[field])` |
| Filter condition | `filter(lambda x: x > 0, data)` |
| Find max/min | `max(data, key=lambda x: x["score"])` |

> ❌ **When NOT to use lambda:** If your logic needs more than one expression, a loop, or will be reused — use `def` instead.

---
---

## Part 2 — The `map()` Function

### What is `map()`?

`map()` applies a function to **every item** in an iterable and returns the transformed results.

```
map(function, iterable)
  ↑               ↑
what to do    what to do it to
```

Think of it as an **assembly line** — every item goes in, gets processed the same way, comes out transformed.

> 💡 `map()` returns a lazy *map object*. Always wrap with `list()` to see results.

---

### Level 1 — map with a Named Function

Start with a plain `def` function, then pass it to `map()`.

```python
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
result = list(map(double, numbers))
print(result)   # [2, 4, 6, 8, 10]
```

```python
def square(x):
    return x ** 2

result = list(map(square, [1, 2, 3, 4, 5]))
print(result)   # [1, 4, 9, 16, 25]
```

**Pattern:** `list(map(named_function, list))`

---

### Level 2 — map with Lambda (most common usage)

Replace the named function with a lambda — no need for a separate `def`.

```python
numbers = [1, 2, 3, 4, 5]

# Double every number
print(list(map(lambda x: x * 2,    numbers)))  # [2, 4, 6, 8, 10]

# Square every number
print(list(map(lambda x: x ** 2,   numbers)))  # [1, 4, 9, 16, 25]

# Add tax (18%) to every price
prices = [100, 200, 50, 300]
with_tax = list(map(lambda p: round(p * 1.18, 2), prices))
print(with_tax)   # [118.0, 236.0, 59.0, 354.0]

# Celsius to Fahrenheit
temps_c = [0, 20, 37, 100]
temps_f = list(map(lambda c: (c * 9/5) + 32, temps_c))
print(temps_f)    # [32.0, 68.0, 98.6, 212.0]
```

**Pattern:** `list(map(lambda x: <transform>, list))`

---

### Level 3 — map on Strings

```python
words = ["hello", "world", "python", "functions"]

# Uppercase every word
upper = list(map(lambda w: w.upper(), words))
print(upper)    # ['HELLO', 'WORLD', 'PYTHON', 'FUNCTIONS']

# Get length of each word
lengths = list(map(lambda w: len(w), words))
print(lengths)  # [5, 5, 6, 9]

# Capitalize first letter
titled = list(map(lambda w: w.capitalize(), words))
print(titled)   # ['Hello', 'World', 'Python', 'Functions']

# Add prefix
prefixed = list(map(lambda w: "py_" + w, words))
print(prefixed) # ['py_hello', 'py_world', 'py_python', 'py_functions']
```

---

### Level 4 — map with Two Lists

`map()` can take **multiple iterables** when the function takes multiple arguments.

```python
# Add corresponding elements
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)   # [11, 22, 33]

# Multiply corresponding elements
products = list(map(lambda x, y: x * y, a, b))
print(products) # [10, 40, 90]

# Build full names from two lists
first_names = ["Alice", "Bob", "Carol"]
last_names  = ["Smith", "Jones", "Brown"]
full_names  = list(map(lambda f, l: f + " " + l, first_names, last_names))
print(full_names)  # ['Alice Smith', 'Bob Jones', 'Carol Brown']
```

**Pattern:** `list(map(lambda x, y: ..., list1, list2))`

---

### Level 5 — map on Dicts and Complex Data

```python
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob",   "marks": 72},
    {"name": "Carol", "marks": 91},
]

# Extract just the names
names = list(map(lambda s: s["name"], students))
print(names)    # ['Alice', 'Bob', 'Carol']

# Add a grade field to each student
def add_grade(s):
    grade = "A" if s["marks"] >= 85 else "B" if s["marks"] >= 70 else "C"
    return {**s, "grade": grade}

graded = list(map(add_grade, students))
for g in graded:
    print(g)
# {'name': 'Alice', 'marks': 85, 'grade': 'A'}
# {'name': 'Bob',   'marks': 72, 'grade': 'B'}
# {'name': 'Carol', 'marks': 91, 'grade': 'A'}

# Apply 10% bonus to all marks
boosted = list(map(lambda s: {**s, "marks": min(100, s["marks"] + 10)}, students))
print([s["marks"] for s in boosted])  # [95, 82, 100]  (Carol capped at 100)
```

---

### Level 6 — Chaining map, filter, sorted

Real power comes from **combining** these tools in a pipeline.

```python
products = [
    {"name": "Laptop",  "price": 75000, "stock": 10},
    {"name": "Phone",   "price": 45000, "stock": 0},
    {"name": "Tablet",  "price": 30000, "stock": 5},
    {"name": "Monitor", "price": 20000, "stock": 3},
]

# Step 1: Keep only in-stock items
in_stock = filter(lambda p: p["stock"] > 0, products)

# Step 2: Add discounted price (10% off)
discounted = map(lambda p: {**p, "sale_price": p["price"] * 0.9}, in_stock)

# Step 3: Sort by sale price
result = sorted(discounted, key=lambda p: p["sale_price"])

for p in result:
    print(f"{p['name']}: ₹{p['sale_price']:,.0f}")
# Monitor:  ₹18,000
# Tablet:   ₹27,000
# Laptop:   ₹67,500
```

---

### map vs for loop — When to Use Which

```python
numbers = [1, 2, 3, 4, 5]

# for loop (verbose but very readable)
result = []
for n in numbers:
    result.append(n ** 2)

# map (concise, functional style)
result = list(map(lambda x: x ** 2, numbers))

# list comprehension (often the most Pythonic middle ground)
result = [x ** 2 for x in numbers]
```

| Approach | Use when |
|---|---|
| `for` loop | Logic is complex or multi-step |
| `map()` | Simple transformation, functional style |
| List comprehension | Simple transformation, Pythonic style |

> 💡 `map()` is slightly faster than a list comprehension for very large datasets because it's lazy — it doesn't compute all results upfront.

---

### map — Quick Reference

| Task | Code |
|---|---|
| Transform numbers | `list(map(lambda x: x*2, nums))` |
| Transform strings | `list(map(lambda s: s.upper(), words))` |
| Use two lists | `list(map(lambda x,y: x+y, list1, list2))` |
| Extract from dicts | `list(map(lambda d: d["key"], records))` |
| Chain with filter | `list(map(fn, filter(cond, data)))` |
| Use named function | `list(map(my_func, data))` |
