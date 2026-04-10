# functions_examples.py
# ──────────────────────────────────────────────────────────────
# Real-world style function examples for teaching.
# Each example is self-contained — copy any block and run it.
# ──────────────────────────────────────────────────────────────

# ── Example 1: Basic function with return ────────────────────
print("── 1. Basic function ──")

def add(a, b):
    return a + b

print(add(3, 5))     # 8
print(add(10, 20))   # 30


# ── Example 2: Default arguments ─────────────────────────────
print("\n── 2. Default arguments ──")

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!
print(greet("Carol", "Namaste"))


# ── Example 3: *args — accept any number of values ───────────
print("\n── 3. *args ──")

def total(*prices):
    return sum(prices)

print(total(100, 200, 50))          # 350
print(total(10, 20, 30, 40, 50))    # 150


# ── Example 4: **kwargs — accept named config ─────────────────
print("\n── 4. **kwargs ──")

def show_profile(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

show_profile(name="Alice", age=25, city="Bangalore", role="Engineer")


# ── Example 5: *args and **kwargs together ────────────────────
print("\n── 5. *args + **kwargs ──")

def build_request(method, *endpoints, **headers):
    print(f"  Method   : {method}")
    print(f"  Endpoints: {endpoints}")
    print(f"  Headers  : {headers}")

build_request("GET", "/users", "/orders",
              Authorization="Bearer token123", Content_Type="application/json")


# ── Example 6: Keyword-only arguments (after *) ──────────────
print("\n── 6. Keyword-only arguments ──")

def send_email(to, subject, *, cc="", priority="normal"):
    print(f"  To      : {to}")
    print(f"  Subject : {subject}")
    print(f"  CC      : {cc or 'none'}")
    print(f"  Priority: {priority}")

send_email("alice@example.com", "Meeting", priority="high")
# send_email("a@b.com", "Hi", "c@b.com")   # TypeError — cc must be named


# ── Example 7: Return multiple values ────────────────────────
print("\n── 7. Return multiple values ──")

def min_max_avg(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = min_max_avg([4, 9, 1, 7, 3])
print(f"  Min: {lo}  Max: {hi}  Avg: {avg:.1f}")


# ── Example 8: Type hints and docstring ──────────────────────
print("\n── 8. Type hints + docstring ──")

def calculate_discount(price: float, pct: float = 10.0) -> float:
    """
    Return the price after applying a percentage discount.

    Args:
        price: Original price
        pct:   Discount percentage (default 10%)

    Returns:
        Discounted price
    """
    return price * (1 - pct / 100)

print(f"  ₹1000 after 20% off → ₹{calculate_discount(1000, 20):.2f}")
print(f"  ₹500  after 10% off → ₹{calculate_discount(500):.2f}")


# ── Example 9: Unpacking with * and ** when calling ──────────
print("\n── 9. Unpacking * and ** when calling ──")

def describe(name, age, city):
    print(f"  {name}, age {age}, from {city}")

# Unpack a list into positional args
args = ["Alice", 25, "Mumbai"]
describe(*args)

# Unpack a dict into keyword args
kwargs = {"name": "Bob", "age": 30, "city": "Delhi"}
describe(**kwargs)


# ── Example 10: Lambda with sorted ───────────────────────────
print("\n── 10. Lambda — sort by second element ──")

students = [("Alice", 88), ("Bob", 72), ("Carol", 95), ("Dave", 60)]

by_score = sorted(students, key=lambda s: s[1], reverse=True)
for name, score in by_score:
    print(f"  {name:<8}  {score}")


# ── Example 11: Lambda with map and filter ────────────────────
print("\n── 11. Lambda — map and filter ──")

prices = [100, 250, 430, 80, 610, 175]

discounted = list(map(lambda p: round(p * 0.9, 2), prices))
expensive   = list(filter(lambda p: p > 200, prices))

print(f"  Original  : {prices}")
print(f"  After 10% discount: {discounted}")
print(f"  Over ₹200 : {expensive}")


# ── Example 12: Recursive function (factorial) ───────────────
print("\n── 12. Recursion — factorial ──")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

for i in range(8):
    print(f"  {i}! = {factorial(i)}")


# ── Example 13: Function as argument (higher-order) ──────────
print("\n── 13. Passing a function as an argument ──")

def apply(numbers, operation):
    return [operation(n) for n in numbers]

nums = [1, 2, 3, 4, 5]
print("  Squares:", apply(nums, lambda n: n ** 2))
print("  Doubled:", apply(nums, lambda n: n * 2))
print("  Evens?  ", apply(nums, lambda n: n % 2 == 0))


# ── Example 14: Real-world — invoice calculator ──────────────
print("\n── 14. Invoice calculator ──")

def calculate_invoice(items: list, tax_rate: float = 18.0) -> dict:
    """
    Given a list of (name, qty, unit_price) tuples,
    return an invoice summary dict.
    """
    subtotal = sum(qty * price for _, qty, price in items)
    tax      = subtotal * tax_rate / 100
    total    = subtotal + tax
    return {"subtotal": subtotal, "tax": tax, "total": total}

order = [
    ("Pen",      10, 15),
    ("Notebook",  5, 80),
    ("Folder",    3, 120),
]

invoice = calculate_invoice(order)
print(f"  Subtotal : ₹{invoice['subtotal']:>8,.2f}")
print(f"  GST 18%  : ₹{invoice['tax']:>8,.2f}")
print(f"  Total    : ₹{invoice['total']:>8,.2f}")
