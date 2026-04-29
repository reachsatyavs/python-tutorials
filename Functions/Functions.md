# Python Functions – Overview & Examples

## A guide to **what functions are**, **types of functions**, **argument types** (including `*` and `*`*), and **10 sample functions**

---

## 1. What is a Function?

A **function** is a reusable block of code that:

- Performs a specific task
- Can accept **inputs** (arguments) and return **outputs** (return values)
- Can be called multiple times without duplicating code

### Why use functions?

- **Reusability** – write once, use many times
- **Modularity** – break programs into smaller, understandable pieces
- **Maintainability** – change logic in one place
- **Readability** – give meaningful names to operations

---

## 2. Types of Functions

### 2.1 Built-in Functions

Python provides many built-in functions you can use directly:

```python
print("Hello")
len([1, 2, 3])
type(42)
sum([1, 2, 3, 4])
max(5, 10, 2)
```

### 2.2 User-defined Functions (Regular)

Functions you define with `def`:

```python
def greet(name):
    return f"Hello, {name}!"
```

### 2.3 Lambda Functions (Anonymous)

Single-expression functions created with `lambda`:

```python
square = lambda x: x ** 2
add = lambda a, b: a + b
```

> **Functions are values too.**
> Notice that `square` and `add` above are variables — but instead of holding a number or string, they hold a function.
> This is a key idea: in Python, a function *with* `()` runs and gives you the result; a function *without* `()` is the function itself, and can be stored or passed just like any other value.
> This is exactly why `sorted(students, key=lambda s: s[1])` works — `key=` accepts a function as a value.

### 2.4 Methods

Functions bound to objects (called with dot notation):

```python
"hello".upper()
[1, 2, 3].append(4)
```

---

## 3. Types of Arguments in Python

> **Why do so many argument types exist?**
>
> A single argument style cannot cover all real-world situations. Each type was introduced to solve a specific problem that the previous types could not handle cleanly. As you read through each section, notice the pattern: every new type exists because the simpler types had a limitation.

---

### 3.1 Positional Arguments

**What it is:** Arguments passed in the same order as the parameters defined in the function.

**Why it exists:** This is the simplest, most natural way to pass data — match values left to right, just like filling in blanks in a sentence.

**The limitation it leaves:** Order is rigid. If you call the function with values in the wrong order, you get wrong results silently — Python won't warn you. This becomes a real problem as functions grow more parameters.

```python
def greet(first, last):
    return f"{first} {last}"

greet("John", "Doe")   # ✅ John Doe
greet("Doe", "John")   # ❌ Doe John — wrong, but no error!
```

---

### 3.2 Keyword Arguments

**What it is:** Arguments passed by explicitly naming the parameter — `name=value` — so order no longer matters.

**Why it exists:** Positional arguments break when you change the order of parameters, add a new one in the middle, or call a function you haven't memorized. Keyword arguments make calls self-documenting and order-independent.

**The connection to lambda:** This is exactly how `sorted()`, `filter()`, `max()`, and `min()` accept a function as input — through a keyword argument called `key=`. Because `key=` is a keyword argument, you can pass a lambda by name, clearly and without ambiguity.

```python
def greet(first, last):
    return f"{first} {last}"

greet(last="Doe", first="John")   # ✅ John Doe — order doesn't matter

# Real example: passing a function as a keyword argument
students = [("Alice", 85), ("Bob", 72), ("Carol", 91)]
sorted(students, key=lambda s: s[1])   # key= is a keyword argument
```

---

### 3.3 Default Arguments

**What it is:** Parameters that have a pre-set value, used when the caller doesn't provide one.

**Why it exists:** Not every caller needs to specify every argument. Without defaults, callers are forced to pass values they don't care about. With defaults, functions become flexible — callers provide only what they want to change.

**The limitation it leaves:** Defaults are fixed at definition time. If a caller wants to pass *any* number of extra values beyond what's defined, defaults alone can't help. That's what `*args` solves.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")           # Hello, Alice!  — uses the default
greet("Bob", "Hi")       # Hi, Bob!       — overrides the default
```

---

### 3.4 `*args` – Variable Positional Arguments

**What it is:** A parameter prefixed with `*` that collects any number of extra positional values into a **tuple**.

**Why it exists:** Sometimes you genuinely don't know how many values will be passed — a sum function, an average function, a logging function. Defining a fixed number of parameters would mean writing a different function for every case. `*args` lets one function handle two values or two hundred.

**The limitation it leaves:** `*args` only collects *positional* extras. If callers want to pass named configuration — like `env="prod"` or `region="asia"` — `*args` can't capture those. That's what `**kwargs` solves.

```python
def average(*numbers):
    return sum(numbers) / len(numbers)

average(10, 20, 30)        # 20.0
average(1, 2, 3, 4, 5)    # 3.0

# numbers arrives as a tuple inside the function: (10, 20, 30)
```

---

### 3.5 `**kwargs` – Variable Keyword Arguments

**What it is:** A parameter prefixed with `*`* that collects any number of named arguments into a **dictionary**.

**Why it exists:** Some functions need to accept an open-ended set of named inputs — building a user profile, configuring a connection, forwarding settings to another function. Without `**kwargs`, you'd have to predefine every possible field. With it, the function adapts to whatever the caller provides.

```python
def build_profile(**info):
    return info

build_profile(name="Alice", age=25, city="Mumbai")
# {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

# info arrives as a dict inside the function
# Loop over it with: for k, v in info.items()
```

---

### 3.6 `*` – Keyword-Only Arguments (PEP 3102)

**What it is:** A bare `*` in the parameter list forces everything that comes after it to be passed by keyword — they cannot be passed positionally.

**Why it exists:** Some arguments are sensitive enough that passing them in the wrong position would create silent, hard-to-debug bugs. For example, `timeout=30` and `ssl=True` in a database connection — if a caller accidentally passes `30` positionally thinking it's the port number, everything breaks silently. Keyword-only arguments make this impossible by requiring the caller to always write the name explicitly.

```python
def connect(host, port, *, timeout=10, ssl=True):
    print(f"{host}:{port}, timeout={timeout}, ssl={ssl}")

connect("localhost", 8080)                  # ✅ uses defaults
connect("localhost", 8080, timeout=30)      # ✅ explicit and clear
connect("localhost", 8080, 30)              # ❌ TypeError — timeout must be named
```

---

### 3.7 `**` When Calling – Dictionary Unpacking

**What it is:** Using `*`* at the *call site* (not the definition) to unpack a dictionary into keyword arguments.

**Why it exists:** You often already have data sitting in a dictionary — from a config file, an API response, or user input. Without `*`*, you'd have to manually extract every key and pass it. With `**`, the dictionary maps directly to the function's parameters in one clean step.

```python
config = {"name": "Alice", "age": 25}

def greet(name, age):
    return f"{name} is {age} years old"

greet(**config)   # "Alice is 25 years old"
# Same as: greet(name="Alice", age=25)
```

---

### 3.8 `/` – Positional-Only Arguments (Python 3.8+)

**What it is:** A bare `/` in the parameter list forces everything before it to be passed positionally — those parameter names cannot be used as keywords by the caller.

**Why it exists:** When you're writing a library or API, you might want to freely rename internal parameters later without breaking callers who might have started using those names as keyword arguments. `/` locks the interface to position only, keeping the internal names private. Python's own built-in functions like `len()` and `abs()` work this way internally.

```python
def power(base, exponent, /):
    return base ** exponent

power(2, 10)                    # ✅ 1024
power(base=2, exponent=10)      # ❌ TypeError — positional-only
```

---

### 3.9 Mixed Arguments Example

All argument types can be combined in one function. The order must be:

```python
def example(pos_only, /, pos_or_kw, *, kw_only):
    pass
```

A real example combining all styles:

```python
def demo(x, y, /, z, *, debug=False):
    print(x, y, z, debug)

# Allowed:
demo(1, 2, 3)
demo(1, 2, z=3)
demo(1, 2, 3, debug=True)
demo(1, 2, z=3, debug=True)

# NOT allowed:
demo(x=1, y=2, z=3)      # ❌ x, y are positional-only
demo(1, y=2, z=3)        # ❌ y is positional-only
demo(1, 2, 3, True)      # ❌ debug is keyword-only
```

---

### 3.10 Argument Order – The Full Picture

```python
def example(pos1, pos2, /, pos_or_kw, *args, kw_only, **kwargs):
    pass
```


| Symbol      | Meaning                  | Why it exists                                              |
| ----------- | ------------------------ | ---------------------------------------------------------- |
| `a, b`      | Positional               | Simple, natural left-to-right matching                     |
| `a=1`       | Default                  | Makes parameters optional                                  |
| `key=value` | Keyword                  | Order freedom, self-documenting, enables passing functions |
| `*args`     | Extra positional → tuple | Unknown count of inputs                                    |
| `**kwargs`  | Extra keyword → dict     | Unknown set of named inputs                                |
| `*`         | After: keyword-only      | Forces critical args to always be named                    |
| `/`         | Before: positional-only  | Keeps parameter names private from callers                 |


---

## 4. Ten Sample Functions for Reference

### Example 1: Basic function with return

```python
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(3, 5)
print(result)  # 8
```

### Example 2: Default arguments

```python
def greet(name, greeting="Hello"):
    """Greet a person with an optional custom greeting."""
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!
```

### Example 3: `*args` – variable positional

```python
def average(*numbers):
    """Compute the average of any number of values."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(average(10, 20, 30))      # 20.0
print(average(1, 2, 3, 4, 5))   # 3.0
```

### Example 4: `**kwargs` – variable keyword

```python
def build_profile(**info):
    """Build a user profile from keyword arguments."""
    return info

profile = build_profile(name="Alice", age=25, city="Mumbai")
print(profile)  # {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
```

### Example 5: `*args` and `**kwargs` together

```python
def log_message(prefix, *args, **kwargs):
    """Log a message with optional extra args and metadata."""
    msg = " ".join(str(a) for a in args)
    meta = " ".join(f"{k}={v}" for k, v in kwargs.items())
    return f"[{prefix}] {msg} {meta}"

print(log_message("INFO", "User logged in", user="alice", ip="127.0.0.1"))
# [INFO] User logged in user=alice ip=127.0.0.1
```

> `prefix` is required and positional. `*args` collects any extra messages. `**kwargs` collects any named metadata. One function handles them all.

### Example 6: Keyword-only arguments (using `*`)

```python
def connect(host, port, *, timeout=10, ssl=True):
    """Connect with required host/port and optional keyword-only settings."""
    return f"{host}:{port} timeout={timeout} ssl={ssl}"

print(connect("localhost", 8080))
print(connect("localhost", 8080, timeout=30, ssl=False))
```

### Example 7: Lambda function

```python
square = lambda x: x ** 2
is_even = lambda n: n % 2 == 0

print(square(5))      # 25
print(is_even(4))     # True
```

> `square` and `is_even` are variables that hold functions. Calling them with `()` runs the function and returns the result. Without `()`, they are just the function object — which is why you can pass them to `sorted()`, `filter()`, `map()`, and `max()` as the `key=` argument.

### Example 8: Function with docstring and type hints

```python
def calculate_total(prices: list[float], tax_rate: float = 0.18) -> float:
    """
    Calculate total price including tax.

    Args:
        prices: List of item prices
        tax_rate: Tax rate (default 18%)

    Returns:
        Total including tax
    """
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)

total = calculate_total([100.0, 200.0, 50.0])
print(total)  # 413.0
```

### Example 9: Unpacking with `*` and `**` when calling

```python
def describe(name, age, city):
    return f"{name}, {age}, from {city}"

# Unpack a list with *
args = ["Alice", 25, "Mumbai"]
print(describe(*args))

# Unpack a dict with **
kwargs = {"name": "Bob", "age": 30, "city": "Delhi"}
print(describe(**kwargs))
```

> You already have the data in a list or dict. `*` and `**` at the call site let you pass that data directly without manually unpacking each value.

### Example 10: Positional-only parameters (Python 3.8+)

```python
def power(base, exponent, /):
    """Compute base^exponent. Both args must be positional."""
    return base ** exponent

print(power(2, 10))   # 1024
# power(base=2, exponent=10)  # ❌ TypeError: positional-only
```

---

## Quick Reference: Why Each Argument Type Exists


| Pattern           | Name                   | Problem it solves                                              |
| ----------------- | ---------------------- | -------------------------------------------------------------- |
| `a, b`            | Positional             | Simple ordered inputs — fast and natural                       |
| `a="Hello"`       | Default                | Optional inputs — caller provides only what changes            |
| `key=value`       | Keyword                | Order freedom — readable, safe, enables passing functions      |
| `*args`           | Variable positional    | Unknown count of inputs — collected as a tuple                 |
| `**kwargs`        | Variable keyword       | Unknown set of named inputs — collected as a dict              |
| `*`               | Keyword-only marker    | Forces critical args to always be named — prevents silent bugs |
| `**` at call site | Dict unpacking         | Reuse existing dict data as keyword arguments                  |
| `/`               | Positional-only marker | Keeps parameter names private — safe API design                |


---

## Suggested Teaching Order

1. Basic `def` and `return`
2. Positional arguments — the default, and its limitation
3. Keyword arguments — order freedom, and how this enables `key=lambda`
4. Default arguments — optional inputs
5. `*args` — unknown count of positional inputs
6. `**kwargs` — unknown set of named inputs
7. `*args` + `**kwargs` together
8. `*` for keyword-only — forcing clarity
9. `/` for positional-only — locking the interface
10. Unpacking with `*` and `**` when calling

