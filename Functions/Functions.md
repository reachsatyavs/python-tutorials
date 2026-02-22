# Python Functions – Overview & Examples

A guide to **what functions are**, **types of functions**, **argument types** (including `*` and `**`), and **10 sample functions** 
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

### 2.4 Methods

Functions bound to objects (called with dot notation):

```python
"hello".upper()
[1, 2, 3].append(4)
```

---

## 3. Types of Arguments in Python

### 3.1 Positional Arguments

Arguments passed in the same order as parameters:

```python
def greet(first, last):
    return f"{first} {last}"

greet("John", "Doe")  # John Doe
```

### 3.2 Keyword Arguments

Arguments passed by parameter name:

```python
def greet(first, last):
    return f"{first} {last}"

greet(last="Doe", first="John")  # John Doe
```

### 3.3 Default Arguments

Parameters with default values when not provided:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")           # Hello, Alice!
greet("Bob", "Hi")       # Hi, Bob!
```

### 3.4 `*args` – Variable Positional Arguments

Collects extra positional arguments into a tuple:

```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4, 5)   # 15
```

### 3.5 `**kwargs` – Variable Keyword Arguments

Collects extra keyword arguments into a dictionary:

```python
def print_config(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

print_config(env="prod", region="asia", retries=3)
```

### 3.6 `*` – Keyword-Only Arguments (PEP 3102)

Everything after `*` must be passed by keyword:

```python
def connect(host, port, *, timeout=10, ssl=True):
    print(f"{host}:{port}, timeout={timeout}, ssl={ssl}")

connect("localhost", 8080)                    # OK
connect("localhost", 8080, timeout=30)        # OK
connect("localhost", 8080, 30)                # TypeError: positional after *
```

### 3.7 `**` in Function Signature – Unpacking

Used when **calling** a function to unpack a dict into keyword arguments:

```python
config = {"name": "Alice", "age": 25}

def greet(name, age):
    return f"{name} is {age} years old"

greet(**config)  # "Alice is 25 years old"
```

### 3.8 Argument Order (Summary)

Recommended order for parameters:

```python
def example(pos1, pos2, /, pos_or_kw, *, kw_only):
    pass
```

| Symbol   | Meaning                                  |
|----------|------------------------------------------|
| `/`      | Everything before is positional-only     |
| (none)   | Can be positional or keyword             |
| `*`      | Everything after is keyword-only         |
| `*args`  | Collects extra positional args (tuple)   |
| `**kwargs` | Collects extra keyword args (dict)    |

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

### Example 3: *args – variable positional

```python
def average(*numbers):
    """Compute the average of any number of values."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(average(10, 20, 30))      # 20.0
print(average(1, 2, 3, 4, 5))   # 3.0
```

### Example 4: **kwargs – variable keyword

```python
def build_profile(**info):
    """Build a user profile from keyword arguments."""
    return info

profile = build_profile(name="Alice", age=25, city="Mumbai")
print(profile)  # {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
```

### Example 5: *args and **kwargs together

```python
def log_message(prefix, *args, **kwargs):
    """Log a message with optional extra args and metadata."""
    msg = " ".join(str(a) for a in args)
    meta = " ".join(f"{k}={v}" for k, v in kwargs.items())
    return f"[{prefix}] {msg} {meta}"

print(log_message("INFO", "User logged in", user="alice", ip="127.0.0.1"))
# [INFO] User logged in user=alice ip=127.0.0.1
```

### Example 6: Keyword-only arguments (using *)

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

### Example 9: Unpacking with * and ** when calling

```python
def describe(name, age, city):
    return f"{name}, {age}, from {city}"

# Unpack list with *
args = ["Alice", 25, "Mumbai"]
print(describe(*args))

# Unpack dict with **
kwargs = {"name": "Bob", "age": 30, "city": "Delhi"}
print(describe(**kwargs))
```

### Example 10: Positional-only parameters (Python 3.8+)

```python
def power(base, exponent, /):
    """Compute base^exponent. Both args must be positional."""
    return base ** exponent

print(power(2, 10))   # 1024
# power(base=2, exponent=10)  # TypeError: positional-only
```

---

## Quick Reference: Argument Types

| Pattern      | Purpose                              |
|-------------|--------------------------------------|
| `a, b`      | Positional                           |
| `a=1`       | Default value                        |
| `*args`     | Extra positional → tuple             |
| `**kwargs`  | Extra keyword → dict                 |
| `/`         | Before: positional-only              |
| `*`         | After: keyword-only                  |

---

## Suggested Teaching Order

1. Basic `def` and `return`
2. Default arguments
3. `*args`
4. `**kwargs`
5. `*args` + `**kwargs` together
6. `*` for keyword-only
7. `/` for positional-only
8. Unpacking with `*` and `**` when calling
