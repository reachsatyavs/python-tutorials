# 09 — Polymorphism

---

## Why do you need polymorphism?

Without polymorphism, code that works with different types has to check what type each thing is:

```python
# ❌ Without polymorphism — type-checking everywhere
def make_sound(animal):
    if type(animal).__name__ == "Dog":
        print("Woof!")
    elif type(animal).__name__ == "Cat":
        print("Meow!")
    elif type(animal).__name__ == "Bird":
        print("Tweet!")
    # add a new animal type → must edit this function
```

With polymorphism, you just call the same method on every object and trust each type to do the right thing:

```python
# ✅ With polymorphism — one call works for all
def make_sound(animal):
    animal.speak()     # each animal knows how to speak — just call it

# add a new animal type → zero changes here
```

---

## Where is polymorphism used?

| Example | How polymorphism appears |
|---|---|
| `len("hello")`, `len([1,2,3])`, `len({"a":1})` | `len()` calls `__len__()` on each type |
| `for x in list/dict/generator` | iteration calls `__iter__()` |
| `print(obj)` | calls `__str__()` on each object |
| Django views | every view class has `get()` / `post()` |
| Payment systems | `UPI`, `Card`, `Cash` all have `pay()` |
| sklearn models | every model has `.fit()` and `.predict()` |

---

## When should you use polymorphism?

Use polymorphism when:
- Multiple classes have the **same method name** but different implementations.
- You want to write code that works on a **group of objects without caring about their exact type**.
- You are building extensible systems — new types should work with existing code.

---

## The Concept

**Poly = many, Morph = form** → "many forms of the same interface."

The same method name (`speak`, `area`, `pay`) does different things depending on which object you call it on.

```
                    .speak()
                   /    |    \
             "Woof!"  "Meow!"  "Tweet!"
              Dog      Cat      Bird
```

Python achieves polymorphism through:
1. **Method overriding** (inheritance-based) — child classes override parent methods.
2. **Duck typing** — no inheritance needed; any object that has the right method works.

---

## Basic Example — Method Overriding Polymorphism

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."      # default — child classes will override


class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} says: Tweet!"

class Fish(Animal):
    pass       # no override — uses Animal's default speak()


animals = [Dog("Rex"), Cat("Whiskers"), Bird("Tweety"), Fish("Nemo")]

# polymorphism in action — same call, different behaviour
for animal in animals:
    print(f"  {animal.speak()}")
```

**Output:**
```
  Rex says: Woof!
  Whiskers says: Meow!
  Tweety says: Tweet!
  ...
```

Notice: the `for` loop doesn't care what type each animal is — it just calls `.speak()` and each object handles it appropriately.

---

## Duck Typing — Polymorphism Without Inheritance

Python's most powerful form of polymorphism. The rule:

> **"If it walks like a duck and quacks like a duck, it is a duck."**
> — if an object has the method you need, use it. No inheritance required.

```python
class Dog:
    def speak(self): return "Woof!"

class Robot:                           # NOT related to Animal at all
    def speak(self): return "Beep boop!"

class Person:
    def speak(self): return "Hello!"


# This function works with ANY object that has a speak() method
def introduce(thing):
    print(f"  {type(thing).__name__}: {thing.speak()}")

introduce(Dog())
introduce(Robot())
introduce(Person())
```

**Output:**
```
  Dog: Woof!
  Robot: Beep boop!
  Person: Hello!
```

`Robot` and `Person` don't inherit from any common base class — they just have a `speak()` method, and that's enough.

---

## Built-in Polymorphism — `+`, `len()`, `str()`

Python's built-in operators are polymorphic:

```python
# + does different things for different types
print(1     + 2)         # 3         — integer addition
print("a"   + "b")       # ab        — string concatenation
print([1,2] + [3,4])     # [1,2,3,4] — list joining

# len() works on anything with __len__
print(len("hello"))      # 5
print(len([1,2,3]))      # 3
print(len({"a":1,"b":2}))# 2

# str() / print() work on anything with __str__
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):          # makes + work for Points
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)            # Point(1, 2)   — __str__
print(p1 + p2)       # Point(4, 6)   — __add__
```

---

## Real-World Example — Payment System

```python
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        raise NotImplementedError("Subclasses must implement pay()")

    def receipt(self):
        print(f"  Payment of ₹{self.amount:,} via {type(self).__name__}")


class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self):
        print(f"  [UPI] Sending ₹{self.amount:,} to {self.upi_id}")
        return True


class CardPayment(Payment):
    def __init__(self, amount, last4):
        super().__init__(amount)
        self.last4 = last4

    def pay(self):
        print(f"  [Card] Charging ₹{self.amount:,} to card ending {self.last4}")
        return True


class CashPayment(Payment):
    def __init__(self, amount, tendered):
        super().__init__(amount)
        self.tendered = tendered

    def pay(self):
        change = self.tendered - self.amount
        if change < 0:
            print(f"  [Cash] Insufficient cash. Need ₹{self.amount:,}")
            return False
        print(f"  [Cash] ₹{self.amount:,} received. Change: ₹{change:,}")
        return True


def process_payment(payment):      # works for ALL payment types
    success = payment.pay()
    if success:
        payment.receipt()
    print()


payments = [
    UPIPayment(1500,  "alice@upi"),
    CardPayment(3200, "4242"),
    CashPayment(500,  600),
    CashPayment(750,  500),   # insufficient
]

for p in payments:
    process_payment(p)
```

**Output:**
```
  [UPI] Sending ₹1,500 to alice@upi
  Payment of ₹1,500 via UPIPayment

  [Card] Charging ₹3,200 to card ending 4242
  Payment of ₹3,200 via CardPayment

  [Cash] ₹500 received. Change: ₹100
  Payment of ₹500 via CashPayment

  [Cash] Insufficient cash. Need ₹750
```

Adding a new payment type (`CryptoPayment`) only requires:
1. Creating a new class with `pay()`.
2. Zero changes to `process_payment()`.

---

## Polymorphism with `isinstance()` when needed

Sometimes you genuinely need to check the type — but keep it rare:

```python
animals = [Dog("Rex"), Cat("Whiskers"), Bird("Tweety")]

for a in animals:
    a.speak()                   # polymorphism — preferred

    if isinstance(a, Dog):      # type check — only when truly needed
        a.fetch()
```

---

## Common Mistakes

```python
# ❌ Thinking polymorphism requires inheritance
# Duck typing is more Pythonic — if it has the method, use it

# ❌ Using type() checks instead of polymorphism
def process(shape):
    if type(shape) == Circle:
        return 3.14 * shape.radius ** 2
    elif type(shape) == Rectangle:
        return shape.w * shape.h
    # ← adding Triangle requires editing this function

# ✅ Let the object decide
def process(shape):
    return shape.area()   # each shape handles its own area
```

---

## Key Takeaways

- **Polymorphism** = same method name, different behaviour per type.
- In Python, you get it two ways: **method overriding** (via inheritance) and **duck typing** (no inheritance needed).
- Duck typing is more Pythonic: "if it has the method, use it."
- Built-in operators (`+`, `len()`, `str()`) are already polymorphic via dunder methods.
- Polymorphism makes code **open for extension, closed for modification** — new types plug in without changing existing code.

---

*← [08 — Inheritance](08-inheritance.md) · [→ 10 — Abstraction](10-abstraction.md)*
