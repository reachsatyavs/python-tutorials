# 02 — Class and Object

---

## Why do you need classes?

A plain dictionary can hold data about a student:

```python
student = {"name": "Alice", "grade": 90, "email": "alice@school.com"}
```

But dictionaries have no behaviour — you cannot attach a `print_report()` function to a dictionary cleanly, and nothing stops you from adding a wrong key (`student["grrade"] = 95` — silent typo). A class solves both problems: it bundles data **and** behaviour together in one unit, and gives your data a proper type.

---

## Where is it used?

- Every Python built-in (`str`, `list`, `int`) is a class.
- Django models — `class Article(models.Model):` maps to a database table.
- `dataclasses.dataclass` — generate classes from field definitions.
- Any time you need multiple instances of the same structure (users, products, orders).

---

## When should you use a class?

Use a class when:
- You need **multiple objects** with the same structure.
- Data and the operations on it **belong together**.
- You want **type safety** — `isinstance(obj, Student)` instead of checking dict keys.

---

## The Concept

### Anatomy of a class

```python
class Dog:                          # class keyword + PascalCase name
    # ── instance method ──────────────────────────────────
    def __init__(self, name, breed):  # constructor — runs when object is created
        self.name  = name             # instance attribute
        self.breed = breed

    def speak(self):                  # instance method
        return f"{self.name} says Woof!"
```

| Part | Meaning |
|---|---|
| `class Dog:` | Defines the blueprint named `Dog` |
| `def __init__(self, ...)` | Constructor — initialises every new object |
| `self.name = name` | Instance attribute — stored on the object |
| `def speak(self):` | Instance method — a function that belongs to the object |

### Creating an object (instantiation)

```python
rex = Dog("Rex", "Labrador")   # Dog(...) calls __init__ automatically
```

`rex` is now an **instance** (object) of the `Dog` class. You can create as many as you like:

```python
buddy = Dog("Buddy", "Poodle")
max_  = Dog("Max",   "German Shepherd")
```

Each object has **its own copy** of `name` and `breed`.

---

## Basic Example

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year

    def description(self):
        return f"{self.year} {self.brand} {self.model}"

    def age(self):
        return 2026 - self.year


car1 = Car("Toyota", "Camry",   2020)
car2 = Car("Tesla",  "Model 3", 2023)
car3 = Car("Honda",  "Civic",   2018)

print(car1.description())   # 2020 Toyota Camry
print(car2.description())   # 2023 Tesla Model 3
print(car1.age())           # 6
print(car3.age())           # 8

# access attributes directly
print(car2.brand)           # Tesla
print(car2.year)            # 2023
```

**Output:**
```
2020 Toyota Camry
2023 Tesla Model 3
6
8
Tesla
2023
```

---

## Real-World Example — Product Inventory

```python
class Product:
    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    def sell(self, qty=1):
        if qty > self.stock:
            print(f"  Not enough stock for '{self.name}'. Have {self.stock}, need {qty}.")
        else:
            self.stock -= qty
            print(f"  Sold {qty} x '{self.name}'. Remaining stock: {self.stock}")

    def restock(self, qty):
        self.stock += qty
        print(f"  Restocked '{self.name}' by {qty}. Total: {self.stock}")

    def summary(self):
        status = "In Stock" if self.is_available() else "Out of Stock"
        print(f"  {self.name:<20} ₹{self.price:>8.2f}   {status} ({self.stock})")


laptop = Product("Laptop",       75000, 10)
mouse  = Product("Wireless Mouse", 999,  3)
cable  = Product("USB Cable",      299,  0)

laptop.summary()
mouse.summary()
cable.summary()

print()
laptop.sell(3)
mouse.sell(5)        # not enough stock
cable.sell()         # out of stock
mouse.restock(10)
mouse.sell(5)        # now works

print()
laptop.summary()
mouse.summary()
```

**Output:**
```
  Laptop               ₹75000.00   In Stock (10)
  Wireless Mouse       ₹  999.00   In Stock (3)
  USB Cable            ₹  299.00   Out of Stock (0)

  Sold 3 x 'Laptop'. Remaining stock: 7
  Not enough stock for 'Wireless Mouse'. Have 3, need 5.
  Not enough stock for 'USB Cable'. Have 0, need 1.
  Restocked 'Wireless Mouse' by 10. Total: 13
  Sold 5 x 'Wireless Mouse'. Remaining stock: 8

  Laptop               ₹75000.00   In Stock (7)
  Wireless Mouse       ₹  999.00   In Stock (8)
```

---

## Common Mistakes

```python
# ❌ Forgetting parentheses — this is the class itself, not an object
dog = Dog             # dog IS the class
dog = Dog()           # ✅ this creates an instance

# ❌ Accessing an attribute that was never set in __init__
class Cat:
    def __init__(self, name):
        self.name = name

c = Cat("Whiskers")
print(c.color)        # AttributeError: 'Cat' object has no attribute 'color'

# ✅ Set all attributes in __init__
class Cat:
    def __init__(self, name, color="unknown"):
        self.name  = name
        self.color = color

# ❌ Using the class name instead of self inside a method
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{Dog.name} says Woof!"   # AttributeError — Dog has no .name
        # return f"{self.name} says Woof!"  ✅
```

---

## Key Takeaways

- A **class** is a blueprint; an **object** (instance) is created from it with `ClassName(...)`.
- `__init__` sets up the object's initial data.
- `self` refers to the specific instance — see `[04-self-keyword.md](04-self-keyword.md)`.
- Each object has **its own copy** of instance attributes — changing one does not affect another.
- Class names use **PascalCase** by convention (`Dog`, `BankAccount`, `HttpRequest`).

---

*← [01 — What is OOP?](01-what-is-oop.md) · [→ 03 — `__init__` Constructor](03-init-constructor.md)*
