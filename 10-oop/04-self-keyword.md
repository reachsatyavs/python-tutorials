# 04 — `self` — The Keyword That Points to the Object

---

## Why does `self` exist?

Consider this: you have two `Dog` objects — `rex` and `buddy`. When you call `rex.speak()`, Python needs to know "which dog's name should I use?" — is it Rex or Buddy?

`self` is the answer. It is the way Python passes the **current object** into every method call.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"   # which .name? → self tells Python

rex   = Dog("Rex")
buddy = Dog("Buddy")

print(rex.speak())      # Rex says Woof!   — self = rex
print(buddy.speak())    # Buddy says Woof! — self = buddy
```

When you write `rex.speak()`, Python translates this internally to:

```python
Dog.speak(rex)    # rex is passed as self
```

`self` is that first argument — automatically filled in by Python.

---

## Where is `self` used?

- **Every instance method** in every class uses `self`.
- You use `self.attribute` to read or write instance data.
- You use `self.method()` to call another method on the same object.

---

## When to use `self`?

- Use `self.x` to store data that **belongs to one specific object**.
- Use `self.method()` to call another method on **the same object**.
- Do NOT use `self` in `@staticmethod` — static methods don't belong to an instance.

---

## The Concept

Think of `self` as the answer to: **"whose data are we talking about?"**

```
rex.speak()
│
├── Python sees: "call speak() on the rex object"
└── Python translates to: Dog.speak(rex)
                                     │
                                     └── self = rex inside the method
```

Every instance method receives `self` as its first parameter. `self.name` means "the `name` attribute of this particular object."

---

## Basic Example — self in Action

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius                    # self.radius belongs to this circle

    def area(self):
        return 3.14159 * self.radius ** 2       # uses this circle's radius

    def circumference(self):
        return 2 * 3.14159 * self.radius        # same

    def scale(self, factor):
        self.radius = self.radius * factor      # modifies this circle's radius
        return self                             # returns self for chaining


small  = Circle(3)
large  = Circle(10)

print(f"small  radius={small.radius}  area={small.area():.2f}")
print(f"large  radius={large.radius}  area={large.area():.2f}")

small.scale(2)
print(f"small after scale(2): radius={small.radius}  area={small.area():.2f}")
print(f"large unchanged:       radius={large.radius}  area={large.area():.2f}")
```

**Output:**
```
small  radius=3  area=28.27
large  radius=10  area=314.16
small after scale(2): radius=6  area=113.10
large unchanged:       radius=10  area=314.16
```

Scaling `small` did not affect `large` — each object's `self` points to its own data.

---

## `self` calling another method on the same object

```python
class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def describe(self):
        shape = "square" if self.is_square() else "rectangle"   # self.is_square()
        return (f"A {shape}: {self.width}×{self.height}, "
                f"area={self.area()}, perimeter={self.perimeter()}")
                # ↑ self.area() and self.perimeter() called on the same object


r1 = Rectangle(4, 6)
r2 = Rectangle(5, 5)

print(r1.describe())    # A rectangle: 4×6, area=24, perimeter=20
print(r2.describe())    # A square: 5×5, area=25, perimeter=20
```

**Output:**
```
A rectangle: 4×6, area=24, perimeter=20
A square: 5×5, area=25, perimeter=20
```

---

## Can you rename `self`?

**Yes** — technically `self` is just a convention. Python does not enforce the name.

```python
class Dog:
    def __init__(this, name):    # 'this' instead of 'self' — works!
        this.name = name

    def speak(this):
        return f"{this.name} says Woof!"

rex = Dog("Rex")
print(rex.speak())               # Rex says Woof!
```

**But you should never rename it.** Every Python programmer in the world uses `self`. Using `this`, `me`, or `dog` will confuse every reader and every tool (linters, IDEs, AI). It is one of the strongest conventions in Python.

> **Rule:** Always name it `self`. It is not enforced by Python, but it is enforced by every team and style guide.

---

## `self` vs class name

```python
class Counter:
    count = 0               # class variable (shared)

    def __init__(self):
        Counter.count += 1  # access class variable via class name
        self.id = Counter.count  # self.id is per-instance

    def show(self):
        print(f"  Instance id={self.id}, total counters={Counter.count}")


a = Counter()   # Counter.count = 1, a.id = 1
b = Counter()   # Counter.count = 2, b.id = 2
c = Counter()   # Counter.count = 3, c.id = 3

a.show()   # Instance id=1, total counters=3
b.show()   # Instance id=2, total counters=3
c.show()   # Instance id=3, total counters=3
```

---

## Real-World Example — Shopping Cart

```python
class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []           # each cart has its own list

    def add(self, name, price, qty=1):
        self.items.append({"name": name, "price": price, "qty": qty})
        print(f"  Added {qty}x {name} (₹{price}) to {self.owner}'s cart")

    def total(self):
        return sum(item["price"] * item["qty"] for item in self.items)

    def summary(self):
        print(f"\n  {self.owner}'s Cart:")
        for item in self.items:
            print(f"    {item['name']:<20} ₹{item['price']:>7.2f} x{item['qty']}")
        print(f"    {'─'*35}")
        print(f"    {'Total':<20} ₹{self.total():>7.2f}")


alice_cart = ShoppingCart("Alice")
bob_cart   = ShoppingCart("Bob")

alice_cart.add("Laptop",  75000)
alice_cart.add("Mouse",     999, qty=2)
bob_cart.add("Keyboard",  2500)
bob_cart.add("Monitor",  15000)

alice_cart.summary()
bob_cart.summary()
```

**Output:**
```
  Added 1x Laptop (₹75000) to Alice's cart
  Added 2x Mouse (₹999) to Alice's cart
  Added 1x Keyboard (₹2500) to Bob's cart
  Added 1x Monitor (₹15000) to Bob's cart

  Alice's Cart:
    Laptop               ₹75000.00 x1
    Mouse                ₹  999.00 x2
    ───────────────────────────────────
    Total                ₹76998.00

  Bob's Cart:
    Keyboard             ₹ 2500.00 x1
    Monitor              ₹15000.00 x1
    ───────────────────────────────────
    Total                ₹17500.00
```

Note: `alice_cart.items` and `bob_cart.items` are completely separate lists — `self` ensures each cart's methods operate on its own data.

---

## Common Mistakes

```python
# ❌ Forgetting self parameter in a method
class Dog:
    def speak():           # missing self
        print("Woof")

d = Dog()
d.speak()      # TypeError: speak() takes 0 positional arguments but 1 was given
               # Python passes the object as first arg — there's nowhere to put it

# ✅
class Dog:
    def speak(self):
        print("Woof")

# ❌ Accessing attribute without self
class Dog:
    def __init__(self, name):
        name = name       # creates a LOCAL variable, not an attribute!
        # self.name = name  ← correct

d = Dog("Rex")
print(d.name)   # AttributeError — never stored on self
```

---

## Key Takeaways

- `self` is the **object itself** — it is automatically passed as the first argument to every instance method.
- Python translates `rex.speak()` into `Dog.speak(rex)` — `rex` is `self`.
- `self.x` stores or reads data on the specific instance.
- `self.method()` calls another method on the same object.
- You **can** rename `self` but you **should not** — it is a universal Python convention.

---

*← [03 — `__init__` Constructor](03-init-constructor.md) · [→ 05 — Class vs Instance Variables](05-class-vs-instance-variables.md)*
