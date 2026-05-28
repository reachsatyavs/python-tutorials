# Python Decorators
> Python Series · Module 07 · Decorators · `github.com/reachsatyavs/python-tutorials`

---

## Table of Contents

1. [What is a Decorator?](#1-what-is-a-decorator)
2. [The Problem Decorators Solve](#2-the-problem-decorators-solve)
3. [Functions are First-Class Objects](#3-functions-are-first-class-objects)
4. [Building a Decorator Step by Step](#4-building-a-decorator-step-by-step)
5. [The `@` Syntax — Syntactic Sugar](#5-the--syntax--syntactic-sugar)
6. [Decorating Functions that Take Arguments](#6-decorating-functions-that-take-arguments)
7. [`functools.wraps` — Preserve Function Identity](#7-functoolswraps--preserve-function-identity)
8. [Stacking Multiple Decorators](#8-stacking-multiple-decorators)
9. [Decorator Factories — Decorators with Parameters](#9-decorator-factories--decorators-with-parameters)
10. [Real-World Use Cases](#10-real-world-use-cases)
11. [Decorating Built-in Functions](#11-decorating-built-in-functions)
12. [Class-Based Decorators](#12-class-based-decorators)
13. [Built-in Python Decorators](#13-built-in-python-decorators)
14. [Quick Recap — Cheat Sheet](#14-quick-recap--cheat-sheet)

---

## 1. What is a Decorator?

A **decorator** is a function that receives another function, adds behaviour around it, and returns a new function — without touching the original code.

```python
def my_decorator(func):       # receives the original function
    def wrapper():
        print("Before")       # extra behaviour BEFORE
        func()                # call the original
        print("After")        # extra behaviour AFTER
    return wrapper             # return the new function

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)   # apply the decorator
say_hello()
```

**Output:**
```
Before
Hello!
After
```

The key idea: the original `say_hello` body never changed. The decorator wrapped it.

---

## 2. The Problem Decorators Solve

Imagine you have 10 functions and you want to log every time one is called.

**Without decorators — repetition everywhere:**

```python
def add(a, b):
    print(f"[LOG] add called")      # duplicated in every function
    return a + b

def subtract(a, b):
    print(f"[LOG] subtract called") # duplicated again
    return a - b

def multiply(a, b):
    print(f"[LOG] multiply called") # duplicated again
    return a * b
```

**With a decorator — write the logging logic once:**

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

@log
def subtract(a, b):
    return a - b

@log
def multiply(a, b):
    return a * b

add(3, 5)        # [LOG] add called
subtract(10, 4)  # [LOG] subtract called
```

One decorator, zero repetition. This is the core value of decorators.

---

## 3. Functions are First-Class Objects

Decorators are only possible because Python treats functions like any other value.

```python
def greet(name):
    return f"Hello, {name}!"

# store a function in a variable
fn = greet
print(fn("Alice"))          # Hello, Alice!

# pass a function as an argument
def run(func, value):
    return func(value)

print(run(greet, "Bob"))    # Hello, Bob!

# return a function from a function
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

hi = make_greeter("Hi")
print(hi("Carol"))          # Hi, Carol!
```

A decorator is exactly this last pattern — a function that receives a function and returns a (new) function.

---

## 4. Building a Decorator Step by Step

### Step 1 — A function that receives a function

```python
def my_decorator(func):
    print(f"Decorating: {func.__name__}")
    return func              # returns it unchanged for now

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
```

**Output:**
```
Decorating: say_hello
Hello!
```

### Step 2 — Add a wrapper inside

```python
def my_decorator(func):
    def wrapper():           # new function — same signature as func
        print("Before call")
        func()               # call the original
        print("After call")
    return wrapper           # return wrapper, not func

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
```

**Output:**
```
Before call
Hello!
After call
```

### Step 3 — Verify the decorator applied

```python
print(type(say_hello))       # <class 'function'>
print(say_hello.__name__)    # wrapper  ← (we fix this in section 7)
```

### What happens internally

```
my_decorator(say_hello)
    │
    ├── func = say_hello              (original stored inside wrapper's closure)
    │
    └── returns wrapper               (a new function object)

say_hello = wrapper           (the name 'say_hello' now points to wrapper)

say_hello()                   (calls wrapper)
    │
    ├── print("Before call")
    ├── func()  →  original say_hello body runs
    └── print("After call")
```

---

## 5. The `@` Syntax — Syntactic Sugar

Writing `say_hello = my_decorator(say_hello)` every time is verbose. Python provides `@` as a shortcut.

```python
# Without @ — manual
def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)

# With @ — identical result, cleaner syntax
@my_decorator
def say_hello():
    print("Hello!")
```

These two are **exactly the same**. The `@decorator` line runs immediately when Python reads the `def`, before the function is ever called.

```python
# @ works on any callable that returns a callable
@my_decorator               # ← Python executes: say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()                 # calls the wrapper, not the original
```

> **Rule:** `@decorator` above a `def` is shorthand for `fn = decorator(fn)` immediately after the `def`.

---

## 6. Decorating Functions that Take Arguments

A wrapper with no parameters only works on zero-argument functions. Use `*args, **kwargs` to handle any signature.

### The problem

```python
def log(func):
    def wrapper():            # no parameters!
        print(f"[LOG] {func.__name__}")
        return func()
    return wrapper

@log
def add(a, b):               # but add needs 2 arguments
    return a + b

add(3, 5)   # TypeError: wrapper() takes 0 positional arguments but 2 were given
```

### The fix — `*args, **kwargs`

```python
def log(func):
    def wrapper(*args, **kwargs):       # accept anything
        print(f"[LOG] {func.__name__} called with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)  # pass everything through
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

@log
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
greet("Alice")
greet("Bob", greeting="Hi")
```

**Output:**
```
[LOG] add called with args=(3, 5) kwargs={}
[LOG] add returned 8
[LOG] greet called with args=('Alice',) kwargs={}
[LOG] greet returned Hello, Alice!
[LOG] greet called with args=('Bob',) kwargs={'greeting': 'Hi'}
[LOG] greet returned Hi, Bob!
```

> **Rule:** Always use `*args, **kwargs` in the wrapper unless you intentionally want to restrict the signature.

---

## 7. `functools.wraps` — Preserve Function Identity

After decoration, the function's `__name__` and `__doc__` point to the wrapper, not the original. This breaks debugging, `help()`, and documentation tools.

```python
def log(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)   # wrapper     ← wrong!
print(add.__doc__)    # None        ← wrong!
```

**Fix — use `@functools.wraps(func)` on the wrapper:**

```python
import functools

def log(func):
    @functools.wraps(func)          # copies __name__, __doc__, etc. from func
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)   # add         ✅
print(add.__doc__)    # Add two numbers.  ✅
```

> **Rule:** Always put `@functools.wraps(func)` on the wrapper inside every decorator you write.

---

## 8. Stacking Multiple Decorators

You can apply more than one decorator to the same function. They are applied **bottom-up** — the decorator closest to `def` runs first.

```python
import functools

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "**" + func(*args, **kwargs) + "**"
    return wrapper

def upper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@bold
@upper
def greet(name):
    return f"hello, {name}"

print(greet("alice"))
```

**Output:**
```
**HELLO, ALICE**
```

**Execution order:**
```
greet("alice")
  → bold's wrapper runs
      → upper's wrapper runs
          → original greet() runs → "hello, alice"
      → upper returns "HELLO, ALICE"
  → bold returns "**HELLO, ALICE**"
```

Reading the decorators top-down, they apply outside-in:
```python
@bold           # applied second  — outermost wrapper
@upper          # applied first   — innermost wrapper
def greet(name): ...

# equivalent to:
greet = bold(upper(greet))
```

---

## 9. Decorator Factories — Decorators with Parameters

Sometimes you want to pass configuration to the decorator itself, like `@log(level="DEBUG")`. This requires an extra layer — a **decorator factory** (a function that returns a decorator).

```python
import functools

def log(level="INFO"):             # outer: receives the parameter
    def decorator(func):           # middle: receives the function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # inner: wraps the call
            print(f"[{level}] {func.__name__} called")
            return func(*args, **kwargs)
        return wrapper
    return decorator               # returns the actual decorator

@log(level="DEBUG")
def add(a, b):
    return a + b

@log(level="WARNING")
def divide(a, b):
    return a / b

add(2, 3)
divide(10, 2)
```

**Output:**
```
[DEBUG] add called
[WARNING] divide called
```

**Three-layer structure:**

```
log(level="DEBUG")           →  returns decorator
decorator(add)               →  returns wrapper
wrapper(2, 3)                →  runs the actual call
```

---

## 10. Real-World Use Cases

### 10.1 Logging

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result!r}")
        return result
    return wrapper

@log
def multiply(a, b):
    return a * b

multiply(4, 5)
# [LOG] Calling multiply
# [LOG] multiply returned 20
```

---

### 10.2 Timing / Profiling

```python
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        print(f"[TIMER] {func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(10_000_000)
# [TIMER] slow_sum took 0.412381s
```

---

### 10.3 Caching / Memoisation

```python
import functools

def cache(func):
    """Store results so the same inputs are never recomputed."""
    store = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in store:
            store[args] = func(*args)
            print(f"  [CACHE MISS]  computing {func.__name__}{args}")
        else:
            print(f"  [CACHE HIT]   returning stored result for {args}")
        return store[args]
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(5)
# Python ships a ready-made version: @functools.lru_cache
```

**Python's built-in version:**

```python
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))   # 832040 — computed once, cached after
print(fibonacci(30))   # instant — served from cache
```

---

### 10.4 Input Validation

```python
import functools

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"{func.__name__}: negative argument {arg} not allowed")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def square_root(n):
    return n ** 0.5

print(square_root(9))    # 3.0
print(square_root(-4))   # ValueError: square_root: negative argument -4 not allowed
```

---

### 10.5 Retry on Failure

```python
import functools
import time

def retry(times=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Attempt {attempt}/{times} failed: {e}")
                    if attempt < times:
                        time.sleep(delay)
            raise RuntimeError(f"{func.__name__} failed after {times} attempts")
        return wrapper
    return decorator

@retry(times=3, delay=0)
def unstable_api_call():
    import random
    if random.random() < 0.7:   # 70% chance of failure
        raise ConnectionError("Network error")
    return "Success"

# unstable_api_call()
```

---

### 10.6 Access Control / Authentication

```python
import functools

def require_auth(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated"):
            raise PermissionError(f"{user['name']} is not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def view_dashboard(user):
    return f"Welcome, {user['name']}!"

alice = {"name": "Alice", "authenticated": True}
guest = {"name": "Guest", "authenticated": False}

print(view_dashboard(alice))   # Welcome, Alice!
print(view_dashboard(guest))   # PermissionError: Guest is not authenticated
```

---

## 11. Decorating Built-in Functions

You can wrap Python's own built-ins. This is what the `decorator.py` demo does.

```python
import builtins
import functools

# Save originals before wrapping
original_len   = builtins.len
original_print = builtins.print

# Decorator for len — logs type and length before every call
def len_decorator(func):
    def wrapper(obj):
        original_print(f"[LOG] len called on {type(obj).__name__} of size {original_len(obj)}")
        return func(obj)
    return wrapper

builtins.len = len_decorator(builtins.len)

len([1, 2, 3])          # [LOG] len called on list of size 3
len("hello world")      # [LOG] len called on str of size 11
```

**Decorating `range` to make stop inclusive:**

```python
original_range = builtins.range

def range_decorator(func):
    def wrapper(start=0, stop=10, step=1):
        original_print(f"[LOG] range({start}, {stop}, {step})")
        return func(start, stop + 1, step)   # make stop inclusive
    return wrapper

builtins.range = range_decorator(builtins.range)

print(list(range(1, 5)))          # [1, 2, 3, 4, 5]  ← includes 5
print(list(original_range(1, 5))) # [1, 2, 3, 4]     ← original behaviour
```

> **Warning:** Wrapping built-ins affects the entire program. Always save the original first. Use this technique only for debugging or patching, not in production code.

---

## 12. Class-Based Decorators

A class can be a decorator if it implements `__call__`. Useful when the decorator needs to maintain state across multiple calls.

```python
import functools

class CountCalls:
    """Decorator that counts how many times a function is called."""

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func       = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"[COUNT] {self.func.__name__} has been called {self.call_count} time(s)")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Carol")
print(f"Total calls: {greet.call_count}")
```

**Output:**
```
[COUNT] greet has been called 1 time(s)
Hello, Alice!
[COUNT] greet has been called 2 time(s)
Hello, Bob!
[COUNT] greet has been called 3 time(s)
Hello, Carol!
Total calls: 3
```

---

## 13. Built-in Python Decorators

Python ships three decorators used inside classes.

### `@staticmethod` — method with no `self` or `cls`

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(MathUtils.add(3, 5))     # 8    — called on the class, no instance needed
print(MathUtils.is_even(4))    # True
```

---

### `@classmethod` — method that receives the class as first argument

```python
class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        """Alternative constructor — create from 'Name:Salary' string."""
        name, salary = data.split(":")
        return cls(name, int(salary))

    @classmethod
    def get_company(cls):
        return cls.company

e = Employee.from_string("Alice:75000")
print(e.name, e.salary)          # Alice 75000
print(Employee.get_company())    # TechCorp
```

---

### `@property` — access a method like an attribute

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius)    # 5      — looks like an attribute, calls the method
print(c.area)      # 78.53  — computed on access
c.radius = 10      # calls the setter
print(c.radius)    # 10
```

| Decorator | `self` | `cls` | Use |
|---|---|---|---|
| `@staticmethod` | No | No | Utility function grouped inside a class |
| `@classmethod` | No | Yes | Alternative constructors, class-level logic |
| `@property` | Yes | No | Controlled attribute access with get/set logic |

---

## 14. Quick Recap — Cheat Sheet

### Anatomy of a decorator

```python
import functools

def my_decorator(func):
    @functools.wraps(func)          # always include — preserves __name__, __doc__
    def wrapper(*args, **kwargs):   # always use *args, **kwargs — works for any function
        # --- before ---
        result = func(*args, **kwargs)  # call the original
        # --- after ---
        return result
    return wrapper                  # return the wrapper, not wrapper()
```

### The `@` shortcut

```python
@my_decorator
def some_function():
    pass

# exactly the same as:
some_function = my_decorator(some_function)
```

### Decorator factory (decorator with parameters)

```python
def repeat(n):                      # outermost: receives the parameter
    def decorator(func):            # middle: receives the function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator                # returns the decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()    # Hi! Hi! Hi!
```

### Stacking decorators

```python
@decorator_a       # applied second — outermost
@decorator_b       # applied first  — innermost
def fn(): ...

# equivalent to:
fn = decorator_a(decorator_b(fn))
```

### Execution order when stacked

```
fn() called
  → decorator_a's wrapper runs
      → decorator_b's wrapper runs
          → original fn() runs
      → decorator_b's wrapper after-code
  → decorator_a's wrapper after-code
```

### Common real-world decorators

| Decorator | What it does |
|---|---|
| `@log` | Print function name and args on every call |
| `@timer` | Measure and print execution time |
| `@functools.lru_cache` | Cache results — same inputs never recomputed |
| `@retry(times=3)` | Re-call on failure up to n times |
| `@validate_positive` | Reject invalid inputs before the function runs |
| `@require_auth` | Block unauthenticated callers |
| `@staticmethod` | No `self` — utility method on a class |
| `@classmethod` | Receives `cls` — factory methods |
| `@property` | Attribute-style access with getter/setter logic |

### Key rules

- Always use `@functools.wraps(func)` on the wrapper
- Always use `*args, **kwargs` in the wrapper
- The `@` line runs at **definition time**, not at call time
- Decorators stack bottom-up: `@outer` over `@inner` → `outer(inner(fn))`
- A decorator factory needs three levels: `params → func → wrapper`
- Class-based decorators use `__call__` — useful when state is needed

---

## Exercises

1. Write a `@timer` decorator and apply it to a function that counts to 1 million. Print the elapsed time.
2. Write a `@log(level)` decorator factory. Apply `@log(level="DEBUG")` to `add()` and `@log(level="ERROR")` to `divide()`.
3. Write a `@validate_types(*types)` decorator that checks the type of each positional argument matches the expected type.
4. Stack `@timer` and `@log` on the same function. Observe the execution order.
5. Rewrite the `@cache` decorator using a class with `__call__` instead of a closure.

---

*Python Series by Satya VS · [github.com/reachsatyavs/python-tutorials](https://github.com/reachsatyavs/python-tutorials)*
