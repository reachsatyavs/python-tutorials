# Python Practice Scripts — Set 3 of 16

> **Coverage:** data types · mutability · strings · tuples · dicts · sets · functions · scope · closures · lambda · control flow · recursion · higher-order functions  
> **Builds on:** Set 1 (data types, built-ins, collections) · Set 2 (operators, control flow, lambda)  
> **Format:** each script has runnable code, expected output, concepts covered, and 3 learning tasks to deepen understanding

---

## Script 01 — Type Inspector

```python
values = [42, 3.14, "hello", True, None, [1, 2], (3, 4), {5, 6}, {"a": 1}]

for v in values:
    print(f"Value: {v!r:20} | type: {type(v).__name__:10} | is int? {isinstance(v, int)}")
```

**Output:**
```
Value: 42                   | type: int        | is int? True
Value: 3.14                 | type: float      | is int? False
Value: 'hello'              | type: str        | is int? False
Value: True                 | type: bool       | is int? True
Value: None                 | type: NoneType   | is int? False
Value: [1, 2]               | type: list       | is int? False
Value: (3, 4)               | type: tuple      | is int? False
Value: {5, 6}               | type: set        | is int? False
Value: {'a': 1}             | type: dict       | is int? False
```

**Concepts:** `type()`, `isinstance()`, `!r` repr format, all 9 built-in types in one loop

**Learning tasks:**
1. `isinstance(True, int)` returns `True` — why? What does this tell you about `bool` and `int`?
2. Add a check: print `"Number"` if the value is `int` or `float`, else print `"Other"`.
3. What is the type of `type(42)` itself? Run `type(type(42))` and explain.

---

## Script 02 — Mutable vs Immutable

```python
# Lists are mutable — assignment copies the reference, not the data
a = [1, 2, 3]
b = a          # b points to the same list as a
b.append(4)
print("a:", a)

# Tuples are immutable — cannot change items after creation
t = (1, 2, 3)
try:
    t[0] = 99
except TypeError as e:
    print("Error:", e)

# Strings are immutable — += creates a new object
s = "hello"
print("id before:", id(s))
s += " world"
print("id after :", id(s))
print("s        :", s)
```

**Output:**
```
a: [1, 2, 3, 4]
Error: 'tuple' object does not support item assignment
id before: 140234567890   (any number — will differ on your machine)
id after : 140234512345   (different number — new object)
s        : hello world
```

**Concepts:** mutable vs immutable, shared reference trap, `id()`, `+=` on strings creates new object

**Learning tasks:**
1. How do you make a true independent copy of a list so changes to `b` do NOT affect `a`? (Hint: two ways)
2. Can a tuple contain a mutable element? Try `t = ([1, 2], 3)` and then `t[0].append(99)`.
3. Why does `s += " world"` create a new object instead of modifying `s` in place?

---

## Script 03 — String Swiss Army Knife

```python
sentence = "  Python is Awesome and Python is Fun!  "

print(sentence.strip())
print(sentence.lower().strip())
print(sentence.count("Python"))
print(sentence.replace("Python", "Java"))
print(sentence.strip().split())

words = sentence.strip().split()
print("Word count:", len(words))
print("First word:", words[0])
print("Last word :", words[-1])
print("Reversed  :", sentence.strip()[::-1])
print("Contains 'Awesome':", "Awesome" in sentence)
```

**Output:**
```
Python is Awesome and Python is Fun!
python is awesome and python is fun!
2
  Java is Awesome and Java is Fun!  
['Python', 'is', 'Awesome', 'and', 'Python', 'is', 'Fun!']
Word count: 7
First word: Python
Last word : Fun!
Reversed  : !nuF si nohtyP dna emosewA si nohtyP
Contains 'Awesome': True
```

**Concepts:** `.strip()`, `.lower()`, `.count()`, `.replace()`, `.split()`, `[::-1]` reverse, `in` on strings

**Learning tasks:**
1. Extract only the word `"Awesome"` using slicing (no `split()`). What start and end index do you need?
2. Write a one-liner that returns `True` if the stripped sentence has more than 5 words.
3. Use an f-string to print: `The sentence has N words and M characters.` (M excludes spaces)

---

## Script 04 — Tuple Unpacking and Swap

```python
# Basic unpacking
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")

# Swap without a temp variable
a, b = 5, 9
a, b = b, a
print(f"a={a}, b={b}")

# Extended unpacking with *
first, *middle, last = [10, 20, 30, 40, 50]
print(f"first={first}, middle={middle}, last={last}")

# Unpacking in a loop
learners = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
for name, score in learners:
    print(f"  {name}: {score}")
```

**Output:**
```
x=10, y=20
a=9, b=5
first=10, middle=[20, 30, 40], last=50
  Alice: 90
  Bob: 85
  Charlie: 92
```

**Concepts:** tuple unpacking, `*` splat to collect remainder, swap idiom, unpacking in a `for` loop

**Learning tasks:**
1. Unpack `learners` in one pass so you end up with two separate lists: one of names, one of scores.
2. What happens when you write `first, second = (1, 2, 3)`? Explain the error and fix it two different ways.
3. Can you use `*` to merge two tuples without converting them to lists? Try `(*t1, *t2)`.

---

## Script 05 — Dictionary Deep Dive

```python
person = {
    "name"   : "Alice",
    "age"    : 22,
    "scores" : {"math": 95, "english": 88, "science": 91},
    "hobbies": ["reading", "coding", "chess"]
}

# Safe access — returns default if key is missing
print(person.get("grade", "Not assigned"))

# Iterating key-value pairs
for key, value in person.items():
    print(f"  {key}: {value}")

# Dict comprehension — keep only int values
simple = {k: v for k, v in person.items() if isinstance(v, int)}
print("Int fields:", simple)

# Nested access
print("Math score :", person["scores"]["math"])
print("First hobby:", person["hobbies"][0])
```

**Output:**
```
Not assigned
  name: Alice
  age: 22
  scores: {'math': 95, 'english': 88, 'science': 91}
  hobbies: ['reading', 'coding', 'chess']
Int fields: {'age': 22}
Math score : 95
First hobby: reading
```

**Concepts:** `.get()` with default, `.items()`, dict comprehension with `isinstance()`, nested dict and list access

**Learning tasks:**
1. Add key `"grade"` with value `"A"` using `.setdefault()`. What does `.setdefault()` do differently from plain `=` assignment?
2. Write a function that accepts this `person` dict and returns the average of all values in `scores`.
3. Invert the `scores` sub-dict so scores become keys and subjects become values: `{95: "math", ...}`.

---

## Script 06 — Nested Dictionary Navigation

```python
company = {
    "name": "TechCorp",
    "departments": {
        "engineering": {
            "head": "Alice",
            "team_size": 12,
            "projects": ["Apollo", "Zeta"]
        },
        "marketing": {
            "head": "Bob",
            "team_size": 5,
            "projects": ["Campaign X"]
        }
    },
    "location": {"city": "Bengaluru", "country": "India"}
}

# Direct nested access
print(company["departments"]["engineering"]["head"])

# Safe deep access — chain .get() with empty dict defaults
dept = "hr"
head = company.get("departments", {}).get(dept, {}).get("head", "N/A")
print(f"Head of {dept}: {head}")

# Iterate all departments
for dept_name, info in company["departments"].items():
    print(f"  {dept_name.title()}: {info['team_size']} people, led by {info['head']}")
```

**Output:**
```
Alice
Head of hr: N/A
  Engineering: 12 people, led by Alice
  Marketing: 5 people, led by Bob
```

**Concepts:** chained `[]` access, chained `.get()` with `{}` default to avoid `KeyError`, looping nested dict

**Learning tasks:**
1. Print all project names across all departments as a single flat list: `["Apollo", "Zeta", "Campaign X"]`.
2. Find the department with the largest `team_size` — use `max()` with a lambda `key`.
3. Add a new department `"finance"` with `head`, `team_size`, and `projects` keys.

---

## Script 07 — Set Operations

```python
python_devs = {"Alice", "Bob", "Charlie", "Diana"}
java_devs   = {"Bob", "Eve", "Charlie", "Frank"}

print("Union           :", python_devs | java_devs)
print("Intersection    :", python_devs & java_devs)
print("Only Python     :", python_devs - java_devs)
print("Only Java       :", java_devs - python_devs)
print("Symmetric diff  :", python_devs ^ java_devs)

# Membership test — O(1) in a set, O(n) in a list
print("Is Alice a Python dev?", "Alice" in python_devs)

# De-duplicate a list by converting to set and back
tags = ["python", "web", "python", "ml", "web", "python"]
unique_tags = sorted(set(tags))
print("Unique tags:", unique_tags)
```

**Output:**
```
Union           : {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'}
Intersection    : {'Bob', 'Charlie'}
Only Python     : {'Alice', 'Diana'}
Only Java       : {'Eve', 'Frank'}
Symmetric diff  : {'Alice', 'Diana', 'Eve', 'Frank'}
Is Alice a Python dev? True
Unique tags: ['ml', 'python', 'web']
```

**Concepts:** `|`, `&`, `-`, `^` set operators, O(1) membership, de-duplication with `set()`

**Learning tasks:**
1. What is a `frozenset`? Convert `python_devs` to one and try calling `.add()` on it.
2. Write a function `common_skills(team_a, team_b)` that returns shared skills as a sorted list.
3. Given any string, use a set to count how many unique characters it contains.

---

## Script 08 — Function Fundamentals

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def total(*numbers):
    return sum(numbers)

def profile(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

def mixed(required, *args, flag=False, **kwargs):
    print(f"required={required}, args={args}, flag={flag}, kwargs={kwargs}")

print(greet("Alice"))
print(greet("Bob", "Hi"))
print(total(1, 2, 3, 4, 5))
profile(name="Alice", age=22, city="Bengaluru")
mixed("must", 1, 2, 3, flag=True, color="blue", size="L")
```

**Output:**
```
Hello, Alice!
Hi, Bob!
15
  name: Alice
  age: 22
  city: Bengaluru
required=must, args=(1, 2, 3), flag=True, kwargs={'color': 'blue', 'size': 'L'}
```

**Concepts:** default args, `*args` → tuple, `**kwargs` → dict, keyword-only args (after `*args`), mixing all four

**Learning tasks:**
1. What is the difference between `*args` and `**kwargs`? What type does each arrive as inside the function?
2. Write a function `describe_list(label, *items)` that prints: `label: item1, item2, item3`.
3. Can you call `greet(greeting="Hi", name="Eve")`? Why does the argument order not matter here?

---

## Script 09 — Scope and Closures

```python
x = "global"

def outer():
    x = "outer"

    def inner():
        nonlocal x        # modify outer's x, not global x
        x = "inner"
        print("inner x:", x)

    inner()
    print("outer x after inner():", x)

outer()
print("global x:", x)    # untouched — nonlocal did not reach here

# Closure — inner function remembers the enclosing variable
def make_multiplier(factor):
    def multiply(n):
        return n * factor   # 'factor' is captured from outer scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))
```

**Output:**
```
inner x: inner
outer x after inner(): inner
global x: global
10
15
```

**Concepts:** LEGB scope rule, `nonlocal`, closure, inner function retains outer variable after outer returns

**Learning tasks:**
1. What is a closure? Why is `factor` still accessible inside `multiply` after `make_multiplier` has returned?
2. Modify `make_multiplier` to also track and print how many times the returned `multiply` has been called.
3. Replace `nonlocal x` with `global x` inside `inner()`. What changes, and why?

---

## Script 10 — Lambda Basics

```python
# Named function
def square(n):
    return n ** 2

# Equivalent lambda — same type, same behaviour
sq = lambda n: n ** 2

print(square(5))
print(sq(5))
print(type(square), type(sq))   # both are <class 'function'>

# Multi-argument lambda
add   = lambda a, b: a + b
clamp = lambda val, lo, hi: max(lo, min(val, hi))

print(add(3, 7))
print(clamp(15, 0, 10))   # 10 — clamped to upper bound
print(clamp(-5, 0, 10))   # 0  — clamped to lower bound

# Lambda in a dict — dispatch table
ops = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
}
for name, fn in ops.items():
    print(f"10 {name} 3 = {fn(10, 3)}")
```

**Output:**
```
25
25
<class 'function'> <class 'function'>
10
10
0
10 add 3 = 13
10 sub 3 = 7
10 mul 3 = 30
```

**Concepts:** lambda vs `def`, both are `function` objects, multi-arg lambda, conditional in lambda, dispatch table

**Learning tasks:**
1. Write a lambda that returns `True` if a number is even.
2. Write a lambda that returns `"pass"` if a score is >= 50, else `"fail"`.
3. Why can't lambdas have multiple statements? What is the design constraint?

---

## Script 11 — Sorting with Lambda

```python
learners = [
    ("Alice",   "F", 92),
    ("Bob",     "M", 85),
    ("Charlie", "M", 92),
    ("Diana",   "F", 78),
    ("Eve",     "F", 85),
]

# Sort by score descending
by_score = sorted(learners, key=lambda s: s[2], reverse=True)

# Sort by name alphabetically
by_name = sorted(learners, key=lambda s: s[0])

# Multi-key: score descending, then name ascending within same score
by_score_name = sorted(learners, key=lambda s: (-s[2], s[0]))

print("By score (desc):")
for s in by_score:
    print(" ", s)

print("\nBy score desc, then name asc:")
for s in by_score_name:
    print(" ", s)
```

**Output:**
```
By score (desc):
  ('Alice', 'F', 92)
  ('Charlie', 'M', 92)
  ('Bob', 'M', 85)
  ('Eve', 'F', 85)
  ('Diana', 'F', 78)

By score desc, then name asc:
  ('Alice', 'F', 92)
  ('Charlie', 'M', 92)
  ('Bob', 'M', 85)
  ('Eve', 'F', 85)
  ('Diana', 'F', 78)
```

**Concepts:** `sorted()` with `key=`, `reverse=True`, multi-key sort using a tuple, negating a number for descending sub-sort

**Learning tasks:**
1. Sort `learners` so female (`"F"`) entries appear first, then by score descending within each group.
2. Find the entry with the highest score using `max()` with a lambda `key`.
3. What is the difference between `list.sort()` and `sorted()`? When would you choose each?

---

## Script 12 — `map()` and `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map — apply a function to every element
squares    = list(map(lambda n: n ** 2, numbers))
as_strings = list(map(str, numbers))

# filter — keep elements where the function returns True
evens = list(filter(lambda n: n % 2 == 0, numbers))
big   = list(filter(lambda n: n > 6, numbers))

print("Squares     :", squares)
print("As strings  :", as_strings)
print("Evens       :", evens)
print("Greater than 6:", big)

# Chaining — squares of even numbers only
even_squares = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers)))
print("Even squares:", even_squares)

# map with two iterables — adds element pairs
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print("Element-wise sums:", sums)
```

**Output:**
```
Squares     : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
As strings  : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
Evens       : [2, 4, 6, 8, 10]
Greater than 6: [7, 8, 9, 10]
Even squares: [4, 16, 36, 64, 100]
Element-wise sums: [11, 22, 33]
```

**Concepts:** `map()`, `filter()`, lazy evaluation, `list()` to materialise, chaining, `map` with two iterables

**Learning tasks:**
1. Use `filter()` to extract strings longer than 4 characters from `["hi", "hello", "hey", "python", "ok"]`.
2. Use `map()` to convert `[0, 20, 37, 100]` from Celsius to Fahrenheit: `F = C * 9/5 + 32`.
3. What does `map()` return in Python 3 before you call `list()` on it? Why is it lazy?

---

## Script 13 — Control Flow: `if / elif / else`

```python
def classify_score(score):
    if not isinstance(score, (int, float)):
        return "Invalid input"
    elif score < 0 or score > 100:
        return "Out of range"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

test_scores = [105, -5, 95, 83, 71, 60, 45, "abc"]
for s in test_scores:
    print(f"Score {s!r:>6} → Grade: {classify_score(s)}")

# Ternary — conditional expression in one line
x = 17
label = "odd" if x % 2 != 0 else "even"
print(f"\n{x} is {label}")
```

**Output:**
```
Score    105 → Grade: Out of range
Score     -5 → Grade: Out of range
Score     95 → Grade: A
Score     83 → Grade: B
Score     71 → Grade: C
Score     60 → Grade: D
Score     45 → Grade: F
Score  'abc' → Grade: Invalid input

17 is odd
```

**Concepts:** `isinstance()` input guard, chained `elif`, ternary expression, `!r` format spec

**Learning tasks:**
1. Rewrite `classify_score` using a list of `(threshold, grade)` tuples and a loop instead of `elif`.
2. Add a `+/-` modifier: `B+` if score ≥ 87, `B` if ≥ 83, `B-` if ≥ 80.
3. What is short-circuit evaluation? Show how `and` and `or` can stop early.

---

## Script 14 — Loops: `for`, `while`, `break`, `continue`, `else`

```python
# enumerate — get index and value together
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit}")

# zip — loop two lists in parallel
names  = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# while True with break and continue
n = 0
print("\nOdd numbers up to 9:")
while True:
    n += 1
    if n % 2 == 0:
        continue       # skip even numbers
    if n > 9:
        break          # stop when past 9
    print(n, end=" ")
print()

# for / else — else runs only if no break occurred
print("\nDivisibility check for 10:")
for i in range(2, 10):
    if 10 % i == 0:
        print(f"  10 is divisible by {i}")
        break
else:
    print("  10 has no divisors in range 2–9")
```

**Output:**
```
  1. apple
  2. banana
  3. cherry
  Alice: 92
  Bob: 85
  Charlie: 78

Odd numbers up to 9:
1 3 5 7 9

Divisibility check for 10:
  10 is divisible by 2
```

**Concepts:** `enumerate(start=)`, `zip`, `while True` with `break`/`continue`, `for/else`

**Learning tasks:**
1. Use `zip` to pair names and scores, then sort the pairs by score descending.
2. Explain precisely when the `else` block on a `for` loop runs vs. does not run.
3. Rewrite the `while True` loop as a regular `while` loop with a proper condition (no `break`).

---

## Script 15 — Recursion vs Iteration

```python
# Factorial — iterative
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Factorial — recursive
def factorial_rec(n):
    if n <= 1:           # base case
        return 1
    return n * factorial_rec(n - 1)  # recursive case

for i in range(6):
    print(f"  {i}! iterative={factorial_iter(i)}  recursive={factorial_rec(i)}")

# Fibonacci — naive recursive (recomputes subproblems)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Fibonacci — memoised (cache results in a dict)
_memo = {}
def fib_memo(n):
    if n in _memo:
        return _memo[n]
    if n <= 1:
        return n
    _memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return _memo[n]

print("\nFibonacci (0–7):")
for i in range(8):
    print(f"  fib({i}) = {fib_memo(i)}")
```

**Output:**
```
  0! iterative=1  recursive=1
  1! iterative=1  recursive=1
  2! iterative=2  recursive=2
  3! iterative=6  recursive=6
  4! iterative=24  recursive=24
  5! iterative=120  recursive=120

Fibonacci (0–7):
  fib(0) = 0
  fib(1) = 1
  fib(2) = 1
  fib(3) = 2
  fib(4) = 3
  fib(5) = 5
  fib(6) = 8
  fib(7) = 13
```

**Concepts:** recursion, base case, recursive case, memoisation with a dict, iterative vs recursive

**Learning tasks:**
1. What is the base case in `factorial_rec`? Remove it and observe what happens.
2. Measure the time difference between `fib_naive(30)` and `fib_memo(30)` using `import time`.
3. Replace the manual `_memo` dict with Python's built-in `@functools.lru_cache` decorator.

---

## Script 16 — Higher-Order Functions

```python
# A higher-order function takes a function as an argument or returns one.

def apply(func, value):
    return func(value)

def compose(f, g):
    """Returns a new function where compose(f, g)(x) == f(g(x))"""
    return lambda x: f(g(x))

double   = lambda x: x * 2
inc      = lambda x: x + 1
to_upper = lambda s: s.upper()
exclaim  = lambda s: s + "!"

print(apply(double, 5))           # 10
print(apply(to_upper, "hello"))   # HELLO

double_then_inc = compose(inc, double)   # inc( double(x) )
inc_then_double = compose(double, inc)   # double( inc(x) )

print(double_then_inc(3))   # (3*2)+1 = 7
print(inc_then_double(3))   # (3+1)*2 = 8

shout = compose(exclaim, to_upper)
print(shout("python"))      # PYTHON!

# Pipeline — list of functions applied left to right
pipeline = [str.strip, str.lower, lambda s: s.replace(" ", "_")]
text = "  Hello World  "
for step in pipeline:
    text = step(text)
print(text)    # hello_world
```

**Output:**
```
10
HELLO
7
8
PYTHON!
hello_world
```

**Concepts:** higher-order function, `compose`, functions stored in a list, pipeline pattern, lambda chaining

**Learning tasks:**
1. Write a `pipe(*funcs)` function that applies a list of functions left to right to an input value.
2. What does "functions are first-class objects" mean in Python? Give two examples from this script.
3. Extend `compose` to accept any number of functions: `compose(f, g, h)(x)` → `f(g(h(x)))`.

---

## Progression summary

| Script | Level | Concepts |
|---|---|---|
| 01 | Beginner | `type()`, `isinstance()`, all 9 built-in types |
| 02 | Beginner | Mutability, shared references, `id()`, immutable strings |
| 03 | Beginner | String methods, slicing, f-strings, `in` |
| 04 | Beginner | Tuple unpacking, `*` splat, swap, loop unpacking |
| 05 | Intermediate | Dict `.get()`, `.items()`, nested access, dict comprehension |
| 06 | Intermediate | Nested dict navigation, chained `.get()`, safe deep access |
| 07 | Intermediate | Set operators `\|`, `&`, `-`, `^`, membership, de-duplication |
| 08 | Intermediate | Default args, `*args`, `**kwargs`, keyword-only args |
| 09 | Intermediate | LEGB scope, `nonlocal`, closures |
| 10 | Intermediate | Lambda syntax, lambda vs `def`, dispatch table |
| 11 | Intermediate | `sorted()` with `key=`, multi-key sort with tuple |
| 12 | Intermediate | `map()`, `filter()`, lazy evaluation, chaining |
| 13 | Intermediate | `if/elif/else`, `isinstance()` guard, ternary expression |
| 14 | Intermediate | `enumerate`, `zip`, `while True`, `break`, `continue`, `for/else` |
| 15 | Advanced | Recursion, base case, memoisation |
| 16 | Advanced | Higher-order functions, `compose`, pipeline pattern |

---

*Set 4 will cover: `zip`, `enumerate`, `any`, `all`, `reduce`, string formatting deep dive, and more real-world data problems.*
