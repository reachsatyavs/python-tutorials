"""
Python Decorators — 16 Runnable Examples
Module 07 · python-tutorials

Run:  python decorators.py
Each section prints a header so you can follow along with Decorators.md.
"""

import functools
import time
import builtins

SEP = "─" * 60

def section(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)


# ──────────────────────────────────────────────────────────
# Example 01 — Bare-minimum decorator (no arguments)
# ──────────────────────────────────────────────────────────
section("01 — Bare-minimum decorator")

def my_decorator(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)   # manual application
say_hello()


# ──────────────────────────────────────────────────────────
# Example 02 — @ syntax (shorthand for the same thing)
# ──────────────────────────────────────────────────────────
section("02 — @ syntax")

def shout(func):
    def wrapper():
        func()
        print("(said loudly)")
    return wrapper

@shout
def greet():
    print("Hi there")

greet()


# ──────────────────────────────────────────────────────────
# Example 03 — *args and **kwargs — handle any signature
# ──────────────────────────────────────────────────────────
section("03 — *args and **kwargs in wrapper")

def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called  args={args}  kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result!r}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

@log
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
greet_person("Alice")
greet_person("Bob", greeting="Hi")


# ──────────────────────────────────────────────────────────
# Example 04 — functools.wraps — preserve function identity
# ──────────────────────────────────────────────────────────
section("04 — functools.wraps")

def log_v2(func):
    @functools.wraps(func)         # ← copies __name__, __doc__, __module__
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_v2
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

multiply(4, 7)
print(f"  __name__ : {multiply.__name__}")   # multiply  ✅
print(f"  __doc__  : {multiply.__doc__}")    # Multiply two numbers.  ✅


# ──────────────────────────────────────────────────────────
# Example 05 — Timing decorator
# ──────────────────────────────────────────────────────────
section("05 — Timer decorator")

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    """Sum integers from 0 to n."""
    return sum(range(n))

result = slow_sum(5_000_000)
print(f"  Result: {result:,}")


# ──────────────────────────────────────────────────────────
# Example 06 — Stacking two decorators
# ──────────────────────────────────────────────────────────
section("06 — Stacking decorators (bottom-up application)")

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

@bold          # applied second — outer
@upper         # applied first  — inner
def message(name):
    return f"hello, {name}"

print(message("alice"))           # **HELLO, ALICE**
print(f"  (equivalent to: bold(upper(message))('alice'))")


# ──────────────────────────────────────────────────────────
# Example 07 — Decorator factory (decorator with parameters)
# ──────────────────────────────────────────────────────────
section("07 — Decorator factory  @log(level='DEBUG')")

def log_level(level="INFO"):      # outer: receives parameter
    def decorator(func):          # middle: receives function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):   # inner: wraps the call
            print(f"[{level}] {func.__name__} called")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_level(level="DEBUG")
def divide(a, b):
    return a / b

@log_level(level="WARNING")
def sqrt(n):
    return n ** 0.5

divide(10, 2)
sqrt(16)


# ──────────────────────────────────────────────────────────
# Example 08 — Repeat decorator factory
# ──────────────────────────────────────────────────────────
section("08 — @repeat(n) — call the function n times")

def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("  Hi!")

say_hi()


# ──────────────────────────────────────────────────────────
# Example 09 — Caching decorator (manual implementation)
# ──────────────────────────────────────────────────────────
section("09 — Manual cache decorator")

def cache(func):
    store = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in store:
            print(f"  [HIT]  {func.__name__}{args} → {store[args]}")
        else:
            store[args] = func(*args)
            print(f"  [MISS] {func.__name__}{args} → computed {store[args]}")
        return store[args]
    return wrapper

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(6):
    fib(i)


# ──────────────────────────────────────────────────────────
# Example 10 — functools.lru_cache (Python built-in cache)
# ──────────────────────────────────────────────────────────
section("10 — @functools.lru_cache  (built-in memoisation)")

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"  fib(30) = {fibonacci(30)}")
print(f"  fib(35) = {fibonacci(35)}")
info = fibonacci.cache_info()
print(f"  cache_info: hits={info.hits}  misses={info.misses}  maxsize={info.maxsize}")


# ──────────────────────────────────────────────────────────
# Example 11 — Input validation decorator
# ──────────────────────────────────────────────────────────
section("11 — Input validation decorator")

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"{func.__name__}: negative argument {arg!r} not allowed")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def square_root(n):
    return n ** 0.5

print(f"  sqrt(9)  = {square_root(9)}")
print(f"  sqrt(25) = {square_root(25)}")
try:
    square_root(-4)
except ValueError as e:
    print(f"  ValueError: {e}")


# ──────────────────────────────────────────────────────────
# Example 12 — Access control decorator
# ──────────────────────────────────────────────────────────
section("12 — Access control / authentication decorator")

def require_auth(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated"):
            raise PermissionError(f"'{user['name']}' is not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def view_dashboard(user):
    return f"Welcome to the dashboard, {user['name']}!"

alice = {"name": "Alice", "authenticated": True}
guest = {"name": "Guest", "authenticated": False}

print(f"  {view_dashboard(alice)}")
try:
    view_dashboard(guest)
except PermissionError as e:
    print(f"  PermissionError: {e}")


# ──────────────────────────────────────────────────────────
# Example 13 — Retry decorator factory
# ──────────────────────────────────────────────────────────
section("13 — @retry(times, delay) — retry on failure")

import random
random.seed(42)

def retry(times=3, delay=0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Attempt {attempt}/{times} failed: {e}")
                    if attempt < times and delay:
                        time.sleep(delay)
            raise RuntimeError(f"{func.__name__} failed after {times} attempts")
        return wrapper
    return decorator

call_count = 0

@retry(times=5, delay=0)
def flaky_service():
    global call_count
    call_count += 1
    if call_count < 4:           # fail first 3 times
        raise ConnectionError("Network timeout")
    return "Service responded OK"

result = flaky_service()
print(f"  Final result: {result}")


# ──────────────────────────────────────────────────────────
# Example 14 — Decorating built-in len and range
# (from demo_samples/decorator.py)
# ──────────────────────────────────────────────────────────
section("14 — Wrapping built-in len and range")

original_len   = builtins.len
original_print = builtins.print
original_range = builtins.range

def len_decorator(func):
    def wrapper(obj):
        original_print(f"  [LOG] len on {type(obj).__name__} → size {original_len(obj)}")
        return func(obj)
    return wrapper

builtins.len = len_decorator(builtins.len)

len([1, 2, 3])
len({"a": 1, "b": 2})
len("hello world")

# restore so the rest of the script is not affected
builtins.len = original_len

# range decorator — makes stop inclusive
def range_decorator(func):
    def wrapper(start=0, stop=10, step=1):
        original_print(f"  [LOG] range({start}, {stop}, {step}) → making stop inclusive")
        return func(start, stop + 1, step)
    return wrapper

builtins.range = range_decorator(builtins.range)

print(f"  range(1, 5) with decorator : {list(range(1, 5))}")   # [1,2,3,4,5]
print(f"  original range(1, 5)       : {list(original_range(1, 5))}")  # [1,2,3,4]

builtins.range = original_range   # restore


# ──────────────────────────────────────────────────────────
# Example 15 — Class-based decorator (maintains state)
# ──────────────────────────────────────────────────────────
section("15 — Class-based decorator with __call__")

class CountCalls:
    """Counts how many times the decorated function is called."""

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func       = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"  [COUNT] {self.func.__name__} called {self.call_count} time(s)")
        return self.func(*args, **kwargs)

@CountCalls
def greet_user(name):
    print(f"  Hello, {name}!")

greet_user("Alice")
greet_user("Bob")
greet_user("Carol")
print(f"  Total calls: {greet_user.call_count}")


# ──────────────────────────────────────────────────────────
# Example 16 — Combining timer + log + lru_cache
# ──────────────────────────────────────────────────────────
section("16 — Stack: @timer + @log_level + @lru_cache")

@timer
@log_level(level="INFO")
@functools.lru_cache(maxsize=64)
def expensive(n):
    """Simulate expensive computation."""
    time.sleep(0.001 * n)
    return n * n

print(f"  expensive(10) = {expensive(10)}")
print(f"  expensive(10) = {expensive(10)}  ← from cache, faster")
print(f"  expensive(20) = {expensive(20)}")

print(f"\n{SEP}")
print("  All 16 examples complete.")
print(SEP)
