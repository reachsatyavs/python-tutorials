# Python Practice Scripts — Set 1 of 20

> **Coverage:** data types · built-in functions · control flow · functions · lambda · list · dict · tuple · set · string  
> **Progression:** scripts 1–7 are beginner, 8–14 are intermediate, 15–20 are advanced  
> **How to use:** read the script, predict the output, then run it and verify

---

## Script 01 — Meet the data types

```python
# Every value in Python has a type.
# type() tells you what it is.

name    = "Alice"
age     = 30
salary  = 75000.50
is_active = True
nothing = None

print(name,    type(name))
print(age,     type(age))
print(salary,  type(salary))
print(is_active, type(is_active))
print(nothing, type(nothing))
```

**Output:**
```
Alice    <class 'str'>
30       <class 'int'>
75000.5  <class 'float'>
True     <class 'bool'>
None     <class 'NoneType'>
```

**Concepts:** `str`, `int`, `float`, `bool`, `NoneType`, `type()`

---

## Script 02 — String operations

```python
name = "alice johnson"

print(name.title())           # capitalize each word
print(name.upper())           # all caps
print(name.replace("alice", "bob"))  # replace a word
print(name.split())           # split into a list of words
print(len(name))              # number of characters including space

# f-string formatting
age = 28
print(f"Name: {name.title()}, Age: {age}")

# slicing  [start : stop : step]
print(name[0:5])              # first 5 characters
print(name[-7:])              # last 7 characters
print(name[::-1])             # reversed
```

**Output:**
```
Alice Johnson
ALICE JOHNSON
bob johnson
['alice', 'johnson']
13
Name: Alice Johnson, Age: 28
alice
johnson
nosnhoj ecila
```

**Concepts:** string methods, f-strings, slicing, `len()`

---

## Script 03 — List and built-in functions

```python
scores = [88, 45, 72, 91, 60, 55, 83]

print("Count  :", len(scores))
print("Sum    :", sum(scores))
print("Min    :", min(scores))
print("Max    :", max(scores))
print("Average:", sum(scores) / len(scores))
print("Sorted :", sorted(scores))
print("Reversed:", sorted(scores, reverse=True))

scores.append(77)          # add to end
scores.remove(45)          # remove first occurrence of 45
print("After append and remove:", scores)

print("Index of 91:", scores.index(91))
print("Count of 88:", scores.count(88))
```

**Output:**
```
Count  : 7
Sum    : 494
Min    : 45
Max    : 91
Average: 70.57142857142857
Sorted : [45, 55, 60, 72, 83, 88, 91]
Reversed: [91, 88, 83, 72, 60, 55, 45]
After append and remove: [88, 72, 91, 60, 55, 83, 77]
Index of 91: 2
Count of 88: 1
```

**Concepts:** list methods, `len()`, `sum()`, `min()`, `max()`, `sorted()`

---

## Script 04 — Tuple — ordered and unchangeable

```python
# Tuples are like lists but cannot be changed after creation.
point   = (10, 20)
rgb     = (255, 128, 0)
person  = ("Alice", 30, "Engineer")

# Unpacking — assign each value to a variable in one line
name, age, job = person
print(f"{name} is {age} years old and works as {job}")

# Swap two values using tuple unpacking
a, b = 5, 10
a, b = b, a
print(f"After swap: a={a}, b={b}")

# A function returning multiple values returns a tuple
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 8, 2, 9, 1])
print(f"Min: {low}, Max: {high}")

# Tuples can be used as dictionary keys (lists cannot)
grid = {(0, 0): "origin", (1, 0): "right", (0, 1): "up"}
print(grid[(0, 0)])
print(grid[(1, 0)])
```

**Output:**
```
Alice is 30 years old and works as Engineer
After swap: a=10, b=5
Min: 1, Max: 9
origin
right
```

**Concepts:** tuple creation, unpacking, swap, multiple return values, tuple as dict key

---

## Script 05 — Set — unique values, no order

```python
# Sets store only unique values and support math-like operations.

students_python = {"Alice", "Bob", "Carol", "Dave"}
students_java   = {"Bob", "Dave", "Eve", "Frank"}

print("Python students:", students_python)
print("Java students  :", students_java)

print("\nIn both courses (intersection):", students_python & students_java)
print("In either course (union)      :", students_python | students_java)
print("Only in Python (difference)   :", students_python - students_java)
print("Not in both (symmetric diff)  :", students_python ^ students_java)

# Sets automatically remove duplicates
tags = ["python", "data", "python", "ml", "data", "python"]
unique_tags = set(tags)
print("\nUnique tags:", unique_tags)
print("Count:", len(unique_tags))
```

**Output:**
```
Python students: {'Alice', 'Bob', 'Carol', 'Dave'}   (order may vary)
Java students  : {'Bob', 'Dave', 'Eve', 'Frank'}

In both courses (intersection): {'Bob', 'Dave'}
In either course (union)      : {'Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank'}
Only in Python (difference)   : {'Alice', 'Carol'}
Not in both (symmetric diff)  : {'Alice', 'Carol', 'Eve', 'Frank'}

Unique tags: {'data', 'ml', 'python'}
Count: 3
```

**Concepts:** set literals, `&`, `|`, `-`, `^`, de-duplication with `set()`

---

## Script 06 — Dictionary — key-value store

```python
employee = {
    "name"  : "Alice",
    "age"   : 30,
    "salary": 75000,
    "dept"  : "Engineering"
}

# Reading values
print(employee["name"])
print(employee.get("salary"))
print(employee.get("bonus", 0))    # default if key missing

# Adding and updating
employee["bonus"] = 5000
employee["salary"] = 80000
print(employee)

# Looping over a dict
print("\n--- Employee Card ---")
for key, value in employee.items():
    print(f"  {key:10} : {value}")

# Useful dict methods
print("\nKeys  :", list(employee.keys()))
print("Values:", list(employee.values()))
```

**Output:**
```
Alice
75000
0
{'name': 'Alice', 'age': 30, 'salary': 80000, 'dept': 'Engineering', 'bonus': 5000}

--- Employee Card ---
  name       : Alice
  age        : 30
  salary     : 80000
  dept       : Engineering
  bonus      : 5000

Keys  : ['name', 'age', 'salary', 'dept', 'bonus']
Values: ['Alice', 30, 80000, 'Engineering', 5000]
```

**Concepts:** dict creation, `[]` vs `.get()`, adding keys, `.items()`, `.keys()`, `.values()`

---

## Script 07 — Control flow — if / elif / else

```python
def classify_score(score):
    if score >= 90:
        return "A — Distinction"
    elif score >= 75:
        return "B — Merit"
    elif score >= 60:
        return "C — Pass"
    elif score >= 40:
        return "D — Marginal Pass"
    else:
        return "F — Fail"

scores = [95, 82, 67, 45, 30]

for score in scores:
    print(f"Score {score:3} → {classify_score(score)}")
```

**Output:**
```
Score  95 → A — Distinction
Score  82 → B — Merit
Score  67 → C — Pass
Score  45 → D — Marginal Pass
Score  30 → F — Fail
```

**Concepts:** `if/elif/else`, function returning a string, looping over a list, f-string padding

---

## Script 08 — Functions with default arguments

```python
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(greet("Alice"))                          # uses both defaults
print(greet("Bob", greeting="Good morning"))   # override one default
print(greet("Carol", "Hi", "."))               # override both
print(greet(name="Dave", punctuation="..."))   # keyword arguments
```

**Output:**
```
Hello, Alice!
Good morning, Bob!
Hi, Carol.
Hello, Dave...
```

**Concepts:** default arguments, positional vs keyword arguments

---

## Script 09 — `*args` and `**kwargs`

```python
# *args collects extra positional arguments into a tuple
def add_all(*numbers):
    print(f"Numbers received: {numbers}  (type: {type(numbers).__name__})")
    return sum(numbers)

print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40, 50))

# **kwargs collects extra keyword arguments into a dict
def show_profile(**details):
    print(f"Details received: {details}  (type: {type(details).__name__})")
    for key, value in details.items():
        print(f"  {key}: {value}")

show_profile(name="Alice", age=30, city="Mumbai")
```

**Output:**
```
Numbers received: (1, 2, 3)  (type: tuple)
6
Numbers received: (10, 20, 30, 40, 50)  (type: tuple)
150
Details received: {'name': 'Alice', 'age': 30, 'city': 'Mumbai'}  (type: dict)
  name: Alice
  age: 30
  city: Mumbai
```

**Concepts:** `*args` → tuple, `**kwargs` → dict, variable-length arguments

---

## Script 10 — Lambda with `sorted`, `min`, `max`, `map`, `filter`

```python
employees = [
    {"name": "Alice", "salary": 50000, "age": 30},
    {"name": "Bob",   "salary": 80000, "age": 20},
    {"name": "Carol", "salary": 60000, "age": 25},
]

# sorted — returns new list
print("By salary:")
for e in sorted(employees, key=lambda e: e["salary"]):
    print(" ", e["name"], e["salary"])

# min / max — returns the whole dict
youngest = min(employees, key=lambda e: e["age"])
highest  = max(employees, key=lambda e: e["salary"])
print(f"\nYoungest : {youngest['name']} (age {youngest['age']})")
print(f"Highest  : {highest['name']}  (salary {highest['salary']})")

# map — transform every item
names = list(map(lambda e: e["name"].upper(), employees))
print("\nNames uppercased:", names)

# filter — keep items that pass a test
senior = list(filter(lambda e: e["age"] >= 25, employees))
print("\nAge 25 or older:")
for e in senior:
    print(" ", e)
```

**Output:**
```
By salary:
  Alice 50000
  Carol 60000
  Bob 80000

Youngest : Bob (age 20)
Highest  : Bob  (salary 80000)

Names uppercased: ['ALICE', 'BOB', 'CAROL']

Age 25 or older:
  {'name': 'Alice', 'salary': 50000, 'age': 30}
  {'name': 'Carol', 'salary': 60000, 'age': 25}
```

**Concepts:** lambda, `sorted`, `min`, `max`, `map`, `filter`

---

## Script 11 — List comprehension

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic: transform every item
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# With condition: keep only even numbers, then square them
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("Even squares:", even_squares)

# From a list of strings
words = ["hello", "world", "python", "is", "fun"]
long_words = [w.upper() for w in words if len(w) > 3]
print("Long words (upper):", long_words)

# Flattening a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print("Flat:", flat)
```

**Output:**
```
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Even squares: [4, 16, 36, 64, 100]
Long words (upper): ['HELLO', 'WORLD', 'PYTHON']
Flat: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Concepts:** list comprehension, filtering with condition, nested loops in comprehension

---

## Script 12 — Dictionary comprehension

```python
employees = ["Alice", "Bob", "Carol"]
salaries  = [50000, 80000, 60000]

# Build a dict from two lists using zip
salary_map = {name: sal for name, sal in zip(employees, salaries)}
print("Salary map:", salary_map)

# Transform values — give everyone a 10% raise
raised = {name: sal * 1.10 for name, sal in salary_map.items()}
print("After raise:", raised)

# Filter — keep only those earning above 55000
high_earners = {name: sal for name, sal in salary_map.items() if sal > 55000}
print("High earners:", high_earners)

# Count character frequency in a word
word = "mississippi"
freq = {ch: word.count(ch) for ch in set(word)}
print("Char frequency:", freq)
```

**Output:**
```
Salary map: {'Alice': 50000, 'Bob': 80000, 'Carol': 60000}
After raise: {'Alice': 55000.0, 'Bob': 88000.0, 'Carol': 66000.0}
High earners: {'Bob': 80000, 'Carol': 60000}
Char frequency: {'p': 2, 's': 4, 'm': 1, 'i': 4}
```

**Concepts:** dict comprehension, `zip()`, `.items()`, filtering in comprehension

---

## Script 13 — Reading a nested dictionary

```python
# A nested dict is a dict where some values are themselves dicts (or lists).

company = {
    "name": "TechCorp",
    "location": "Bangalore",
    "departments": {
        "engineering": {
            "head": "Raj",
            "team_size": 25,
            "technologies": ["Python", "Go", "Kubernetes"]
        },
        "marketing": {
            "head": "Priya",
            "team_size": 10,
            "technologies": ["SEO", "Analytics", "Figma"]
        }
    }
}

# Reading nested values — chain the keys
print(company["name"])
print(company["departments"]["engineering"]["head"])
print(company["departments"]["marketing"]["team_size"])

# Reading a value inside a nested list
print(company["departments"]["engineering"]["technologies"][0])

# Looping over nested dicts
print("\n--- Department Summary ---")
for dept_name, dept_info in company["departments"].items():
    techs = ", ".join(dept_info["technologies"])
    print(f"  {dept_name.title():15} | Head: {dept_info['head']:8} | Team: {dept_info['team_size']:3} | Tech: {techs}")
```

**Output:**
```
TechCorp
Raj
10
Python

--- Department Summary ---
  Engineering     | Head: Raj      | Team:  25 | Tech: Python, Go, Kubernetes
  Marketing       | Head: Priya    | Team:  10 | Tech: SEO, Analytics, Figma
```

**Concepts:** nested dict access, chaining keys, loop over `.items()`, list inside dict

---

## Script 14 — Nested list of dicts — student records

```python
students = [
    {"name": "Alice", "marks": [85, 90, 78, 92, 88]},
    {"name": "Bob",   "marks": [60, 55, 70, 65, 58]},
    {"name": "Carol", "marks": [95, 98, 92, 97, 99]},
]

def grade(avg):
    if avg >= 90: return "A"
    if avg >= 75: return "B"
    if avg >= 60: return "C"
    return "F"

print(f"{'Name':<10} {'Total':>6} {'Average':>8} {'Grade':>6}")
print("-" * 35)

for s in students:
    total = sum(s["marks"])
    avg   = total / len(s["marks"])
    print(f"{s['name']:<10} {total:>6} {avg:>8.1f} {grade(avg):>6}")

# Who topped?
topper = max(students, key=lambda s: sum(s["marks"]))
print(f"\nTopper: {topper['name']}")
```

**Output:**
```
Name        Total  Average  Grade
-----------------------------------
Alice         433     86.6      B
Bob           308     61.6      C
Carol         481     96.2      A

Topper: Carol
```

**Concepts:** list of dicts, nested list, `sum()`, `max()` with lambda, f-string alignment

---

## Script 15 — Functions as first-class objects

```python
# In Python, a function is just an object.
# You can store it in a variable, put it in a list, pass it as an argument.

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):   return a / b if b != 0 else "Cannot divide by zero"

# Store functions in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate(a, operator, b):
    fn = operations.get(operator)
    if fn:
        return fn(a, b)
    return "Unknown operator"

print(calculate(10, "+", 5))
print(calculate(10, "-", 3))
print(calculate(4,  "*", 7))
print(calculate(20, "/", 4))
print(calculate(10, "/", 0))
print(calculate(5,  "%", 2))   # not in the dict
```

**Output:**
```
15
7
28
5.0
Cannot divide by zero
Unknown operator
```

**Concepts:** functions as values, dict of functions, passing functions, first-class objects

---

## Script 16 — Higher-order function — function that accepts a function

```python
# A higher-order function takes another function as an argument.

def apply_to_all(numbers, operation):
    """Apply any function to every number in the list."""
    return [operation(n) for n in numbers]

def square(n):  return n ** 2
def cube(n):    return n ** 3
def negate(n):  return -n

numbers = [1, 2, 3, 4, 5]

print("Original:", numbers)
print("Squared :", apply_to_all(numbers, square))
print("Cubed   :", apply_to_all(numbers, cube))
print("Negated :", apply_to_all(numbers, negate))

# Same thing with a lambda — no need to define a named function
print("x + 10  :", apply_to_all(numbers, lambda n: n + 10))
```

**Output:**
```
Original: [1, 2, 3, 4, 5]
Squared : [1, 4, 9, 16, 25]
Cubed   : [1, 8, 27, 64, 125]
Negated : [-1, -2, -3, -4, -5]
x + 10  : [11, 12, 13, 14, 15]
```

**Concepts:** higher-order function, passing named functions and lambdas, list comprehension inside a function

---

## Script 17 — Closure — a function that remembers its environment

```python
# A closure is a function defined inside another function.
# The inner function remembers the variables from the outer function
# even after the outer function has finished.

def make_multiplier(factor):
    def multiply(n):           # inner function — closure
        return n * factor      # remembers 'factor' from outer scope
    return multiply            # return the inner function itself

double = make_multiplier(2)
triple = make_multiplier(3)
times10 = make_multiplier(10)

print(double(5))    # 5 * 2 = 10
print(triple(5))    # 5 * 3 = 15
print(times10(7))   # 7 * 10 = 70

# Each closure remembers its own factor independently
print([double(n) for n in range(1, 6)])
print([triple(n) for n in range(1, 6)])
```

**Output:**
```
10
15
70
[2, 4, 6, 8, 10]
[3, 6, 9, 12, 15]
```

**Concepts:** closure, inner function, returning a function, each closure holds its own state

---

## Script 18 — Recursive function

```python
# A recursive function calls itself to solve a smaller version of the same problem.

def factorial(n):
    if n == 0 or n == 1:   # base case — stop here
        return 1
    return n * factorial(n - 1)   # recursive case

for i in range(6):
    print(f"{i}! = {factorial(i)}")

# Fibonacci — each number is the sum of the two before it
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci sequence:")
print([fibonacci(i) for i in range(10)])
```

**Output:**
```
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120

Fibonacci sequence:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Concepts:** recursion, base case, recursive case, `factorial`, `fibonacci`

---

## Script 19 — Working with a deeply nested dict (real-world shape)

```python
# Real APIs and config files often return deeply nested dicts.
# Practice navigating them safely.

order = {
    "order_id": "ORD-1042",
    "customer": {
        "name": "Ravi Kumar",
        "contact": {
            "email": "ravi@example.com",
            "phone": "9876543210"
        }
    },
    "items": [
        {"product": "Laptop",  "qty": 1, "price": 85000},
        {"product": "Mouse",   "qty": 2, "price": 1200},
        {"product": "Keyboard","qty": 1, "price": 2500},
    ],
    "payment": {
        "method": "UPI",
        "status": "Paid"
    }
}

# Direct access
print("Order ID :", order["order_id"])
print("Customer :", order["customer"]["name"])
print("Email    :", order["customer"]["contact"]["email"])
print("Payment  :", order["payment"]["method"], "—", order["payment"]["status"])

# Looping over nested list
print("\n--- Items Ordered ---")
total = 0
for item in order["items"]:
    line_total = item["qty"] * item["price"]
    total += line_total
    print(f"  {item['product']:<12} x{item['qty']}  ₹{item['price']:>6}  →  ₹{line_total:>7}")

print(f"\n  {'Total':>22}         ₹{total:>7}")

# Safe access with .get() — avoids KeyError if key is missing
discount = order.get("discount", 0)
print(f"\n  Discount: ₹{discount}")
print(f"  Final   : ₹{total - discount}")
```

**Output:**
```
Order ID : ORD-1042
Customer : Ravi Kumar
Email    : ravi@example.com
Payment  : UPI — Paid

--- Items Ordered ---
  Laptop       x1  ₹ 85000  →  ₹  85000
  Mouse        x2  ₹  1200  →  ₹   2400
  Keyboard     x1  ₹  2500  →  ₹   2500

  Total                         ₹  89900

  Discount: ₹0
  Final   : ₹89900
```

**Concepts:** deep nesting, `["key"]["key"]`, list of dicts inside a dict, `.get()` with default

---

## Script 20 — Mini data pipeline: filter → sort → map → report

```python
# Combine everything: read raw data, clean it, filter, sort, transform, report.

employees = [
    {"name": "Alice",  "dept": "Engineering", "salary": 50000, "years": 5},
    {"name": "Bob",    "dept": "Marketing",   "salary": 80000, "years": 8},
    {"name": "Carol",  "dept": "Engineering", "salary": 60000, "years": 3},
    {"name": "Dave",   "dept": "HR",          "salary": 45000, "years": 2},
    {"name": "Eve",    "dept": "Engineering", "salary": 95000, "years": 10},
    {"name": "Frank",  "dept": "Marketing",   "salary": 70000, "years": 6},
]

# Step 1 — filter: keep only Engineering dept
eng = list(filter(lambda e: e["dept"] == "Engineering", employees))

# Step 2 — sort by salary descending
eng_sorted = sorted(eng, key=lambda e: e["salary"], reverse=True)

# Step 3 — map: apply 15% raise and add a seniority tag
def enrich(e):
    return {
        "name"      : e["name"],
        "salary"    : round(e["salary"] * 1.15),
        "seniority" : "Senior" if e["years"] >= 5 else "Junior",
    }

enriched = list(map(enrich, eng_sorted))

# Step 4 — report
print(f"{'Name':<10} {'New Salary':>12} {'Level':>8}")
print("-" * 35)
for e in enriched:
    print(f"{e['name']:<10} ₹{e['salary']:>10,} {e['seniority']:>8}")

# Step 5 — summary stats using lambda + built-ins
total = sum(e["salary"] for e in enriched)
highest = max(enriched, key=lambda e: e["salary"])
print(f"\nTotal Engineering payroll : ₹{total:,}")
print(f"Top earner                : {highest['name']} at ₹{highest['salary']:,}")
```

**Output:**
```
Name        New Salary    Level
-----------------------------------
Eve         ₹   109,250   Senior
Carol       ₹    69,000   Junior
Alice       ₹    57,500   Senior

Total Engineering payroll : ₹235,750
Top earner                : Eve at ₹109,250
```

**Concepts:** `filter`, `sorted`, `map`, named function + lambda together, `sum()` with generator, `max()` with lambda, f-string number formatting

---

## Progression summary

| Range | Level | Concepts introduced |
|---|---|---|
| 01–04 | Beginner | `str`, `int`, `float`, `bool`, `None`, `type()`, string methods, list built-ins, tuple unpacking |
| 05–07 | Beginner | `set` operations, dict access and looping, `if/elif/else` in a function |
| 08–09 | Intermediate | Default args, `*args`, `**kwargs` |
| 10–12 | Intermediate | Lambda, `sorted`/`min`/`max`/`map`/`filter`, list comprehension, dict comprehension |
| 13–14 | Intermediate | Nested dict, list of dicts, reading nested structures |
| 15–16 | Advanced | Functions as objects, higher-order functions |
| 17–18 | Advanced | Closures, recursion |
| 19–20 | Advanced | Deep nested dict navigation, mini data pipeline |

---

*Next set (Scripts 21–40) will cover: `reduce`, `zip`, `enumerate`, `any`/`all`, exception handling, file I/O, classes and objects, and more real-world data shapes.*
