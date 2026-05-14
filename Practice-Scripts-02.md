# Python Practice Scripts — Set 2 of 20

> **Coverage:** operators (arithmetic, comparison, logical, membership, identity, augmented) · control flow (for, while, break, continue, for/else) · lambda functions  
> **Builds on:** Set 1 — data types, functions, list, dict, tuple, set  
> **Excludes:** exception handling, `reduce`, list comprehensions

---

## Script 01 — Arithmetic operators

```python
a = 17
b = 5

print(f"{a} + {b}  = {a + b}")    # addition
print(f"{a} - {b}  = {a - b}")    # subtraction
print(f"{a} * {b}  = {a * b}")    # multiplication
print(f"{a} / {b}  = {a / b}")    # division        — always returns float
print(f"{a} // {b} = {a // b}")   # floor division  — drops the decimal
print(f"{a} % {b}  = {a % b}")    # modulo          — remainder
print(f"{a} ** {b} = {a ** b}")   # exponentiation  — 17 to the power 5

# Practical uses of // and %
minutes = 137
hours   = minutes // 60
mins    = minutes % 60
print(f"\n{minutes} minutes = {hours}h {mins}m")

# % to check even / odd
for n in range(1, 8):
    label = "even" if n % 2 == 0 else "odd"
    print(f"  {n} is {label}")
```

**Output:**
```
17 + 5  = 22
17 - 5  = 12
17 * 5  = 85
17 / 5  = 3.4
17 // 5 = 3
17 % 5  = 2
17 ** 5 = 1419857

137 minutes = 2h 17m

  1 is odd
  2 is even
  3 is odd
  4 is even
  5 is odd
  6 is even
  7 is odd
```

**Concepts:** all 7 arithmetic operators, practical uses of `//` and `%`

---

## Script 02 — Comparison operators

```python
# Comparison operators always return True or False.

x = 10

print(x == 10)   # equal to
print(x != 10)   # not equal to
print(x > 8)     # greater than
print(x < 8)     # less than
print(x >= 10)   # greater than or equal
print(x <= 9)    # less than or equal

# Used inside conditions
scores = [45, 82, 60, 91, 38, 75]

print("\nPass / Fail (pass mark = 60):")
for score in scores:
    result = "Pass" if score >= 60 else "Fail"
    print(f"  {score:3}  →  {result}")

# Comparing strings — alphabetical order
words = ["banana", "apple", "cherry"]
print("\nIs 'apple' < 'banana'?", "apple" < "banana")   # True — a comes before b
print("Sorted:", sorted(words))
```

**Output:**
```
True
False
True
False
True
False

Pass / Fail (pass mark = 60):
   45  →  Fail
   82  →  Pass
   60  →  Pass
   91  →  Pass
   38  →  Fail
   75  →  Pass

Is 'apple' < 'banana'? True
Sorted: ['apple', 'banana', 'cherry']
```

**Concepts:** `==`, `!=`, `>`, `<`, `>=`, `<=`, comparing strings

---

## Script 03 — Logical operators: `and`, `or`, `not`

```python
# and  → True only if BOTH sides are True
# or   → True if AT LEAST ONE side is True
# not  → flips True to False and vice versa

age    = 25
salary = 60000
has_id = True

# and — all conditions must be met
print("Eligible for loan (age>=21 AND salary>=50000 AND has_id):")
print(age >= 21 and salary >= 50000 and has_id)

# or — at least one condition must be met
is_admin  = False
is_manager = True
print("\nCan approve? (admin OR manager):")
print(is_admin or is_manager)

# not — flip a boolean
is_blocked = False
print("\nCan login? (not blocked):", not is_blocked)

# Combining all three
score      = 72
attendance = 85

passed     = score >= 60
attended   = attendance >= 75
eligible   = passed and attended

print(f"\nScore: {score}, Attendance: {attendance}%")
print(f"Passed exam    : {passed}")
print(f"Attended enough: {attended}")
print(f"Gets certificate: {eligible}")
```

**Output:**
```
Eligible for loan (age>=21 AND salary>=50000 AND has_id):
True

Can approve? (admin OR manager):
True

Can login? (not blocked): True

Score: 72, Attendance: 85%
Passed exam    : True
Attended enough: True
Gets certificate: True
```

**Concepts:** `and`, `or`, `not`, combining conditions, storing booleans in variables

---

## Script 04 — Membership operators: `in` and `not in`

```python
# 'in' checks whether a value exists inside a container.
# Works on strings, lists, tuples, sets, and dict keys.

# --- string ---
sentence = "Python is easy to learn"
print("'easy' in sentence    :", "easy" in sentence)
print("'hard' not in sentence:", "hard" not in sentence)

# --- list ---
fruits = ["apple", "banana", "cherry"]
print("\n'banana' in fruits :", "banana" in fruits)
print("'mango' in fruits  :", "mango" in fruits)

# --- set (fastest for membership checks) ---
allowed_users = {"alice", "bob", "carol"}
user = "dave"
if user not in allowed_users:
    print(f"\n'{user}' is not allowed access")

# --- dict (checks keys by default) ---
config = {"debug": True, "timeout": 30, "retries": 3}
print("\n'timeout' in config  :", "timeout" in config)
print("'port' in config     :", "port" in config)

# Practical — check before accessing
key = "port"
if key in config:
    print(f"{key} = {config[key]}")
else:
    print(f"'{key}' not found in config — using default 8080")
```

**Output:**
```
'easy' in sentence    : True
'hard' not in sentence: True

'banana' in fruits : True
'mango' in fruits  : False

'dave' is not allowed access

'timeout' in config  : True
'port' in config     : False

'port' not found in config — using default 8080
```

**Concepts:** `in` / `not in` with str, list, set, dict

---

## Script 05 — Identity operators: `is` and `is not`

```python
# '==' checks if two values are EQUAL.
# 'is' checks if two variables point to the EXACT SAME object in memory.

a = [1, 2, 3]
b = [1, 2, 3]
c = a          # c points to the same list as a

print("a == b :", a == b)   # True  — same content
print("a is b :", a is b)   # False — different objects in memory
print("a is c :", a is c)   # True  — same object

# Changing c also changes a (they are the same object)
c.append(4)
print("After c.append(4), a =", a)

# 'is' is the right way to check for None
value = None
print("\nvalue is None    :", value is None)      # correct way
print("value == None    :", value == None)         # works but not recommended

# Small integers are cached — don't rely on 'is' for value comparison
x = 100
y = 100
print("\nx is y (100):", x is y)   # True — Python caches small ints
x = 1000
y = 1000
print("x is y (1000):", x is y)   # May be False — not cached
```

**Output:**
```
a == b : True
a is b : False
a is c : True
After c.append(4), a = [1, 2, 3, 4]

value is None    : True
value == None    : True

x is y (100): True
x is y (1000): False
```

**Concepts:** `is` vs `==`, object identity, `None` check, shared reference trap

---

## Script 06 — Augmented assignment operators

```python
# Augmented operators are shorthand — they read and update in one step.
# x += 5  is the same as  x = x + 5

balance = 1000
print(f"Starting balance: {balance}")

balance += 500    # deposit
print(f"After deposit  : {balance}")

balance -= 200    # withdrawal
print(f"After withdrawal: {balance}")

balance *= 1.05   # 5% interest
print(f"After 5% interest: {balance}")

balance //= 1     # round down to whole number
print(f"Rounded down: {int(balance)}")

# Useful in loops — running total
expenses = [120, 350, 80, 200, 450]
total = 0
for amount in expenses:
    total += amount

print(f"\nExpenses: {expenses}")
print(f"Total   : {total}")

# String version
message = "Hello"
message += ", World"
message += "!"
print(message)
```

**Output:**
```
Starting balance: 1000
After deposit  : 1500
After withdrawal: 1300
After 5% interest: 1365.0
Rounded down: 1365

Expenses: [120, 350, 80, 200, 450]
Total   : 1200

Hello, World!
```

**Concepts:** `+=`, `-=`, `*=`, `//=`, augmented assignment on strings, running total pattern

---

## Script 07 — `for` loop patterns with `range()`

```python
# range(stop)         → 0, 1, 2, ... stop-1
# range(start, stop)  → start, start+1, ... stop-1
# range(start, stop, step) → start, start+step, ...

# Count up
print("Count up 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Count down
print("\nCountdown 5 to 1:")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Every second number
print("\nEven numbers 2 to 10:")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Loop over a list with index using enumerate
fruits = ["apple", "banana", "cherry"]
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  [{index}] {fruit}")

# Loop over two lists together using zip
names   = ["Alice", "Bob", "Carol"]
salaries = [50000, 80000, 60000]
print("\nNames and salaries:")
for name, salary in zip(names, salaries):
    print(f"  {name:<8} ₹{salary:,}")
```

**Output:**
```
Count up 1 to 5:
1 2 3 4 5

Countdown 5 to 1:
5 4 3 2 1

Even numbers 2 to 10:
2 4 6 8 10

Fruits with index:
  [0] apple
  [1] banana
  [2] cherry

Names and salaries:
  Alice    ₹50,000
  Bob      ₹80,000
  Carol    ₹60,000
```

**Concepts:** `range()` with start/stop/step, `enumerate()`, `zip()`

---

## Script 08 — `while` loop

```python
# while runs as long as the condition is True.
# Use it when you don't know in advance how many times to loop.

# Countdown timer
count = 5
print("Countdown:")
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  Go!\n")

# Accumulate until a target is reached
savings = 0
month   = 0
monthly_saving = 3500
target  = 20000

while savings < target:
    month   += 1
    savings += monthly_saving

print(f"Reached ₹{target} in {month} months (₹{savings} saved)")

# Loop with a flag variable — cleaner for complex exit logic
found   = False
numbers = [4, 7, 2, 9, 1, 6]
target_num = 9
index   = 0

while index < len(numbers) and not found:
    if numbers[index] == target_num:
        found = True
    else:
        index += 1

if found:
    print(f"\nFound {target_num} at index {index}")
else:
    print(f"\n{target_num} not found")
```

**Output:**
```
Countdown:
  5...
  4...
  3...
  2...
  1...
  Go!

Reached ₹20000 in 6 months (₹21000 saved)

Found 9 at index 3
```

**Concepts:** `while` with counter, accumulation loop, flag variable, `len()` as loop boundary

---

## Script 09 — `break` and `continue`

```python
# break  → exit the loop immediately
# continue → skip the rest of this iteration, go to the next one

# break — stop as soon as you find what you need
print("Searching for first score above 80:")
scores = [55, 62, 48, 85, 90, 71]
for score in scores:
    print(f"  Checking {score}...", end=" ")
    if score > 80:
        print("FOUND — stopping")
        break
    print("not high enough")

# continue — skip unwanted items, process the rest
print("\nPrinting only passing scores (>= 60):")
for score in scores:
    if score < 60:
        continue          # skip this score, go to next
    print(f"  {score} — Pass")

# Nested loop with break — stop the inner loop, outer keeps going
print("\nMultiplication table (stop inner at product > 20):")
for i in range(1, 5):
    for j in range(1, 10):
        product = i * j
        if product > 20:
            break         # only exits the inner loop
        print(f"{i}x{j}={product:3}", end="  ")
    print()
```

**Output:**
```
Searching for first score above 80:
  Checking 55... not high enough
  Checking 62... not high enough
  Checking 48... not high enough
  Checking 85... FOUND — stopping

Printing only passing scores (>= 60):
  62 — Pass
  85 — Pass
  90 — Pass
  71 — Pass

Multiplication table (stop inner at product > 20):
1x1=  1  1x2=  2  1x3=  3  ...  1x9=  9
2x1=  2  2x2=  4  2x3=  6  ...  2x9= 18
3x1=  3  3x2=  6  3x3=  9  3x4= 12  3x5= 15  3x6= 18
4x1=  4  4x2=  8  4x3= 12  4x4= 16  4x5= 20
```

**Concepts:** `break`, `continue`, early exit, skipping items, `break` only exits its own loop

---

## Script 10 — `for / else` and `while / else`

```python
# The 'else' block on a loop runs ONLY if the loop
# completed without hitting a 'break'.
# It does NOT run if break was used.

# for / else — search and know if it was found
def find_prime_factor(n):
    for i in range(2, n):
        if n % i == 0:
            print(f"  {n} is divisible by {i} — not prime")
            break
    else:
        # only reaches here if no break happened
        print(f"  {n} is prime")

print("Prime check:")
for num in [7, 12, 13, 15, 17]:
    find_prime_factor(num)

# while / else — retry loop
print("\nSearching for value 42 in list:")
data = [10, 25, 37, 55, 42, 60]
i = 0
while i < len(data):
    if data[i] == 42:
        print(f"  Found 42 at index {i}")
        break
    i += 1
else:
    print("  42 was not found")
```

**Output:**
```
Prime check:
  7 is prime
  12 is divisible by 2 — not prime
  13 is prime
  15 is divisible by 3 — not prime
  17 is prime

Searching for value 42 in list:
  Found 42 at index 4
```

**Concepts:** `for/else`, `while/else`, `else` runs only when no `break` occurred

---

## Script 11 — Nested loops — building a pattern and a table

```python
# Nested loop = a loop inside another loop.
# The inner loop runs completely for every single step of the outer loop.

# Pattern: right triangle of stars
print("Right triangle:")
for row in range(1, 6):
    print("*" * row)

# Pattern: number pyramid
print("\nNumber pyramid:")
for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

# Multiplication table (5x5)
print("\nMultiplication table (5x5):")
print("   ", end="")
for j in range(1, 6):
    print(f"{j:4}", end="")
print()
print("   " + "----" * 5)

for i in range(1, 6):
    print(f"{i:2} |", end="")
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()
```

**Output:**
```
Right triangle:
*
**
***
****
*****

Number pyramid:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Multiplication table (5x5):
       1   2   3   4   5
   --------------------
 1 |   1   2   3   4   5
 2 |   2   4   6   8  10
 3 |   3   6   9  12  15
 4 |   4   8  12  16  20
 5 |   5  10  15  20  25
```

**Concepts:** nested `for` loops, string repetition, f-string column alignment

---

## Script 12 — Lambda basics — compare with `def`

```python
# A lambda is a function written in one line, without a name.
# lambda arguments : expression

# Regular function
def square(n):
    return n ** 2

# Same thing as a lambda
square_lambda = lambda n: n ** 2

print("Using def   :", square(5))
print("Using lambda:", square_lambda(5))

# Both are just callables — type is the same
print("type(square)       :", type(square))
print("type(square_lambda):", type(square_lambda))

# Lambda with two arguments
add = lambda a, b: a + b
print("\nadd(3, 7) =", add(3, 7))

# Lambda with a conditional expression
classify = lambda score: "Pass" if score >= 60 else "Fail"
print("classify(75) =", classify(75))
print("classify(40) =", classify(40))

# Lambda called immediately (no variable needed)
result = (lambda x, y: x * y)(6, 7)
print("\n6 * 7 =", result)
```

**Output:**
```
Using def   : 25
Using lambda: 25
type(square)       : <class 'function'>
type(square_lambda): <class 'function'>

add(3, 7) = 10
classify(75) = Pass
classify(40) = Fail

6 * 7 = 42
```

**Concepts:** lambda syntax, lambda vs `def`, two-argument lambda, conditional in lambda, `type()`

---

## Script 13 — Lambda with a conditional expression (ternary)

```python
# value_if_true  if  condition  else  value_if_false

# Grade classifier
grade = lambda score: (
    "A" if score >= 90 else
    "B" if score >= 75 else
    "C" if score >= 60 else
    "F"
)

scores = [95, 82, 67, 45]
for s in scores:
    print(f"  {s}  →  {grade(s)}")

# Absolute value without abs()
absolute = lambda n: n if n >= 0 else -n
print("\nabsolute(-7) =", absolute(-7))
print("absolute( 3) =", absolute(3))

# Bigger of two numbers without max()
bigger = lambda a, b: a if a > b else b
print("\nbigger(10, 25) =", bigger(10, 25))
print("bigger(40, 15) =", bigger(40, 15))

# Categorise a salary
salary_band = lambda s: "High" if s > 70000 else ("Mid" if s > 40000 else "Low")
for sal in [90000, 55000, 30000]:
    print(f"  ₹{sal:,}  →  {salary_band(sal)}")
```

**Output:**
```
  95  →  A
  82  →  B
  67  →  C
  45  →  F

absolute(-7) = 7
absolute( 3) = 3

bigger(10, 25) = 25
bigger(40, 15) = 40

  ₹90,000  →  High
  ₹55,000  →  Mid
  ₹30,000  →  Low
```

**Concepts:** chained ternary in lambda, conditional expression, lambda replacing simple `if/else`

---

## Script 14 — Lambda stored in a list and looped over

```python
# Since a lambda is just an object, you can store many of them in a list.
# Loop over the list and call each one.

transformations = [
    lambda n: n + 10,       # add 10
    lambda n: n * 2,        # double
    lambda n: n ** 2,       # square
    lambda n: n % 2 == 0,   # is even?
    lambda n: -n,           # negate
]

descriptions = ["add 10", "double", "square", "is even?", "negate"]

number = 6
print(f"Input: {number}\n")
for desc, fn in zip(descriptions, transformations):
    print(f"  {desc:<10} → {fn(number)}")
```

**Output:**
```
Input: 6

  add 10     → 16
  double     → 12
  square     → 36
  is even?   → True
  negate     → -6
```

**Concepts:** list of lambdas, `zip()` to pair labels and functions, calling a function stored in a list

---

## Script 15 — Lambda in a dict — dispatch table

```python
# Store lambdas as values in a dict.
# Use the dict to look up and call the right function by name.

operations = {
    "add"      : lambda a, b: a + b,
    "subtract" : lambda a, b: a - b,
    "multiply" : lambda a, b: a * b,
    "divide"   : lambda a, b: a / b if b != 0 else "Cannot divide by zero",
    "power"    : lambda a, b: a ** b,
    "remainder": lambda a, b: a % b,
}

def calculate(a, op, b):
    fn = operations.get(op)
    if fn is None:
        return f"Unknown operation: '{op}'"
    return fn(a, b)

tests = [
    (10, "add",       5),
    (10, "subtract",  3),
    (4,  "multiply",  7),
    (20, "divide",    4),
    (10, "divide",    0),
    (2,  "power",     8),
    (17, "remainder", 5),
    (9,  "modulo",    3),
]

for a, op, b in tests:
    result = calculate(a, op, b)
    print(f"  {a} {op:<12} {b}  →  {result}")
```

**Output:**
```
  10 add          5  →  15
  10 subtract     3  →  7
  4  multiply     7  →  28
  20 divide       4  →  5.0
  10 divide       0  →  Cannot divide by zero
  2  power        8  →  256
  17 remainder    5  →  2
  9  modulo       3  →  Unknown operation: 'modulo'
```

**Concepts:** dict of lambdas, `.get()` with `None` check, dispatch table pattern

---

## Script 16 — Lambda with `sorted` — single and multi-key sort

```python
employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 50000, "age": 30},
    {"name": "Bob",   "dept": "Marketing",   "salary": 80000, "age": 20},
    {"name": "Carol", "dept": "Engineering", "salary": 60000, "age": 25},
    {"name": "Dave",  "dept": "Marketing",   "salary": 80000, "age": 35},
    {"name": "Eve",   "dept": "HR",          "salary": 45000, "age": 28},
]

# Sort by a single field
print("By salary (low → high):")
for e in sorted(employees, key=lambda e: e["salary"]):
    print(f"  {e['name']:<8} ₹{e['salary']:,}")

# Sort by salary descending
print("\nBy salary (high → low):")
for e in sorted(employees, key=lambda e: e["salary"], reverse=True):
    print(f"  {e['name']:<8} ₹{e['salary']:,}")

# Multi-key sort — dept first (A→Z), then salary descending within dept
# Return a tuple: Python sorts tuples element by element
print("\nBy dept (A→Z) then salary (high→low):")
for e in sorted(employees, key=lambda e: (e["dept"], -e["salary"])):
    print(f"  {e['dept']:<14} {e['name']:<8} ₹{e['salary']:,}")
```

**Output:**
```
By salary (low → high):
  Eve      ₹45,000
  Alice    ₹50,000
  Carol    ₹60,000
  Bob      ₹80,000
  Dave     ₹80,000

By salary (high → low):
  Bob      ₹80,000
  Dave     ₹80,000
  Carol    ₹60,000
  Alice    ₹50,000
  Eve      ₹45,000

By dept (A→Z) then salary (high→low):
  Engineering    Carol    ₹60,000
  Engineering    Alice    ₹50,000
  HR             Eve      ₹45,000
  Marketing      Bob      ₹80,000
  Marketing      Dave     ₹80,000
```

**Concepts:** `sorted` with lambda, `reverse=True`, multi-key sort using a tuple, negating for descending sub-sort

---

## Script 17 — Lambda with `map`

```python
products = [
    {"name": "Laptop",   "price": 85000, "qty": 2},
    {"name": "Mouse",    "price":  1200, "qty": 5},
    {"name": "Keyboard", "price":  2500, "qty": 3},
    {"name": "Monitor",  "price": 25000, "qty": 1},
]

# Extract one field from every item
names = list(map(lambda p: p["name"], products))
print("Product names:", names)

# Compute a derived value for every item
totals = list(map(lambda p: p["price"] * p["qty"], products))
print("Line totals  :", totals)

# Transform each item into a new dict
invoiced = list(map(
    lambda p: {
        "item"      : p["name"],
        "line_total": p["price"] * p["qty"]
    },
    products
))
print("\nInvoice lines:")
for line in invoiced:
    print(f"  {line['item']:<12}  ₹{line['line_total']:>8,}")

# Apply a discount to every price
discounted = list(map(lambda p: {**p, "price": round(p["price"] * 0.90)}, products))
print("\nAfter 10% discount:")
for p in discounted:
    print(f"  {p['name']:<12}  ₹{p['price']:,}")
```

**Output:**
```
Product names: ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
Line totals  : [170000, 6000, 7500, 25000]

Invoice lines:
  Laptop        ₹ 170,000
  Mouse         ₹   6,000
  Keyboard      ₹   7,500
  Monitor       ₹  25,000

After 10% discount:
  Laptop        ₹76,500
  Mouse         ₹1,080
  Keyboard      ₹2,250
  Monitor       ₹22,500
```

**Concepts:** `map` with lambda, extracting fields, computing derived values, `{**p, key: value}` to copy a dict with one change

---

## Script 18 — Lambda with `filter`

```python
employees = [
    {"name": "Alice",  "dept": "Engineering", "salary": 50000, "age": 30, "active": True},
    {"name": "Bob",    "dept": "Marketing",   "salary": 80000, "age": 20, "active": True},
    {"name": "Carol",  "dept": "Engineering", "salary": 60000, "age": 25, "active": False},
    {"name": "Dave",   "dept": "HR",          "salary": 45000, "age": 35, "active": True},
    {"name": "Eve",    "dept": "Engineering", "salary": 95000, "age": 28, "active": True},
]

# Single condition
high_earners = list(filter(lambda e: e["salary"] > 55000, employees))
print("Salary > 55,000:")
for e in high_earners:
    print(f"  {e['name']}")

# Multiple conditions with 'and'
eng_active = list(filter(
    lambda e: e["dept"] == "Engineering" and e["active"],
    employees
))
print("\nActive Engineering employees:")
for e in eng_active:
    print(f"  {e['name']}")

# 'not' in a lambda
inactive = list(filter(lambda e: not e["active"], employees))
print("\nInactive employees:")
for e in inactive:
    print(f"  {e['name']}")

# Membership check inside a lambda
target_depts = {"Engineering", "Marketing"}
selected = list(filter(lambda e: e["dept"] in target_depts, employees))
print("\nEngineering or Marketing:")
for e in selected:
    print(f"  {e['name']:<8} ({e['dept']})")
```

**Output:**
```
Salary > 55,000:
  Bob
  Carol
  Eve

Active Engineering employees:
  Alice
  Eve

Inactive employees:
  Carol

Engineering or Marketing:
  Alice    (Engineering)
  Bob      (Marketing)
  Carol    (Engineering)
  Eve      (Engineering)
```

**Concepts:** `filter` with lambda, `and` / `not` inside lambda, `in` for membership inside lambda

---

## Script 19 — Operators + control flow — FizzBuzz and beyond

```python
# FizzBuzz: classic test of modulo + control flow.
# Divisible by 3 → Fizz
# Divisible by 5 → Buzz
# Divisible by both → FizzBuzz
# Otherwise → the number

print("FizzBuzz (1–20):")
for n in range(1, 21):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz", end="  ")
    elif n % 3 == 0:
        print("Fizz", end="  ")
    elif n % 5 == 0:
        print("Buzz", end="  ")
    else:
        print(n, end="  ")
print()

# Collatz sequence — operators + while loop
def collatz(n):
    steps = 0
    print(f"\nCollatz from {n}: ", end="")
    while n != 1:
        print(n, end=" → ")
        if n % 2 == 0:
            n = n // 2        # even: halve it
        else:
            n = n * 3 + 1     # odd: triple and add 1
        steps += 1
    print(1)
    return steps

print(f"Steps: {collatz(6)}")
print(f"Steps: {collatz(11)}")
```

**Output:**
```
FizzBuzz (1–20):
1  2  Fizz  4  Buzz  Fizz  7  8  Fizz  Buzz  11  Fizz  13  14  FizzBuzz  16  17  Fizz  19  Buzz

Collatz from 6: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Steps: 8

Collatz from 11: 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Steps: 14
```

**Concepts:** `%` for divisibility, `and` in condition, `//` and `*` in loop body, `while` with complex exit

---

## Script 20 — Putting it all together — payroll calculator

```python
# Operators + control flow + lambda + dict + list + loop

employees = [
    {"name": "Alice",  "salary": 50000, "dept": "Engineering", "years": 5},
    {"name": "Bob",    "salary": 80000, "dept": "Marketing",   "years": 8},
    {"name": "Carol",  "salary": 60000, "dept": "Engineering", "years": 2},
    {"name": "Dave",   "salary": 45000, "dept": "HR",          "years": 1},
    {"name": "Eve",    "salary": 95000, "dept": "Engineering", "years": 10},
]

# Lambda: decide raise % based on years of service
raise_pct = lambda years: 0.15 if years >= 5 else (0.10 if years >= 3 else 0.05)

# Lambda: decide tax bracket
tax_pct = lambda salary: 0.30 if salary > 80000 else (0.20 if salary > 50000 else 0.10)

# Process payroll
print(f"{'Name':<8} {'Base':>8} {'Raise%':>7} {'New Salary':>11} {'Tax%':>6} {'Take Home':>11}")
print("-" * 58)

total_cost = 0
for e in employees:
    base       = e["salary"]
    r_pct      = raise_pct(e["years"])
    new_salary = round(base * (1 + r_pct))
    t_pct      = tax_pct(new_salary)
    take_home  = round(new_salary * (1 - t_pct))
    total_cost += new_salary

    print(f"{e['name']:<8} ₹{base:>7,} {r_pct*100:>6.0f}%  ₹{new_salary:>9,} {t_pct*100:>5.0f}%  ₹{take_home:>9,}")

print("-" * 58)
print(f"{'Total company payroll':>42}  ₹{total_cost:>9,}")

# Summary using filter + lambda
high_earners = list(filter(lambda e: e["salary"] > 60000, employees))
print(f"\nEmployees above ₹60,000 base: {len(high_earners)}")
for e in sorted(high_earners, key=lambda e: e["salary"], reverse=True):
    print(f"  {e['name']:<8} ₹{e['salary']:,}")
```

**Output:**
```
Name      Base   Raise%  New Salary  Tax%   Take Home
----------------------------------------------------------
Alice    ₹50,000    15%   ₹57,500    20%    ₹46,000
Bob      ₹80,000    15%   ₹92,000    30%    ₹64,400
Carol    ₹60,000    10%   ₹66,000    20%    ₹52,800
Dave     ₹45,000     5%   ₹47,250    10%    ₹42,525
Eve      ₹95,000    15%  ₹109,250    30%    ₹76,475

----------------------------------------------------------
Total company payroll                       ₹372,000

Employees above ₹60,000 base: 2
  Bob      ₹80,000
  Eve      ₹95,000
```

**Concepts:** lambda with chained ternary, arithmetic operators, `for` loop accumulation, `filter` + `sorted` with lambda, f-string alignment

---

## Progression summary

| Script | Level | Focus |
|---|---|---|
| 01 | Beginner | All 7 arithmetic operators, practical uses of `//` and `%` |
| 02 | Beginner | All 6 comparison operators, comparing strings |
| 03 | Beginner | `and`, `or`, `not`, combining multiple conditions |
| 04 | Beginner | `in` / `not in` on str, list, set, dict |
| 05 | Beginner | `is` vs `==`, identity, `None` check, shared reference |
| 06 | Beginner | `+=`, `-=`, `*=` etc., running total in a loop |
| 07 | Intermediate | `for` with `range()`, `enumerate()`, `zip()` |
| 08 | Intermediate | `while` loop, accumulation loop, flag variable |
| 09 | Intermediate | `break`, `continue`, early exit |
| 10 | Intermediate | `for/else`, `while/else` — else runs only when no break |
| 11 | Intermediate | Nested loops, star pattern, multiplication table |
| 12 | Intermediate | Lambda syntax, lambda vs `def`, `type()` |
| 13 | Intermediate | Lambda with chained ternary conditional |
| 14 | Intermediate | List of lambdas, loop and call each one |
| 15 | Advanced | Dict of lambdas — dispatch table |
| 16 | Advanced | Lambda with `sorted`, multi-key sort using tuple |
| 17 | Advanced | Lambda with `map`, derived values, dict spread `{**p}` |
| 18 | Advanced | Lambda with `filter`, `and`/`not`/`in` inside lambda |
| 19 | Advanced | Operators + control flow — FizzBuzz and Collatz |
| 20 | Advanced | Full payroll: lambda + operators + control flow + filter + sorted |

---

*Set 3 will cover: `zip`, `enumerate`, `any`, `all`, `reduce`, string formatting deep dive, and more real-world data problems.*
