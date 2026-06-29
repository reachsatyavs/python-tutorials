# 06 — Methods — Instance, Class, and Static

---

## Why are there three types?

Not all methods need access to the same data:
- Some need **this specific object's data** → instance method
- Some need **the class itself** (e.g. to create objects or read class variables) → class method
- Some are just **utility helpers** related to the class but needing neither → static method

Using the right type makes code clearer and prevents accidental access to data the method shouldn't touch.

---

## Where is each type used?

| Method type | Common use cases |
|---|---|
| Instance method | Reading/writing object data, most regular methods |
| Class method | Factory methods (alternative constructors), modifying class variables |
| Static method | Utility/helper functions logically grouped with the class, validation |

---

## When to use each?

| Use... | When the method needs... |
|---|---|
| Instance method `def f(self)` | Access to `self` — the specific object's data |
| Class method `@classmethod def f(cls)` | Access to `cls` — the class itself, not an instance |
| Static method `@staticmethod def f()` | Neither the instance nor the class — pure utility |

---

## The Concept

```python
class MyClass:
    class_var = "I'm shared"

    def __init__(self, value):
        self.value = value

    # ── Instance method ──────────────────────────────────
    def instance_method(self):          # receives self (the object)
        return f"instance_method: self.value = {self.value}"

    # ── Class method ─────────────────────────────────────
    @classmethod
    def class_method(cls):              # receives cls (the class)
        return f"class_method: class_var = {cls.class_var}"

    # ── Static method ────────────────────────────────────
    @staticmethod
    def static_method():                # receives nothing
        return "static_method: no access to self or cls"


obj = MyClass(42)

print(obj.instance_method())   # can call on instance
print(obj.class_method())      # can call on instance OR class
print(obj.static_method())     # can call on instance OR class

print(MyClass.class_method())  # called on the class directly
print(MyClass.static_method()) # called on the class directly
```

**Output:**
```
instance_method: self.value = 42
class_method: class_var = I'm shared
static_method: no access to self or cls
class_method: class_var = I'm shared
static_method: no access to self or cls
```

---

## Basic Example — All Three Side by Side

```python
class Temperature:
    unit = "Celsius"           # class variable

    def __init__(self, degrees):
        self.degrees = degrees

    # Instance method — works with this specific temperature
    def to_fahrenheit(self):
        return (self.degrees * 9/5) + 32

    def to_kelvin(self):
        return self.degrees + 273.15

    def describe(self):
        return f"{self.degrees}°C = {self.to_fahrenheit():.1f}°F = {self.to_kelvin():.2f}K"

    # Class method — creates a Temperature from Fahrenheit (alternative constructor)
    @classmethod
    def from_fahrenheit(cls, f):
        celsius = (f - 32) * 5/9
        return cls(round(celsius, 2))

    @classmethod
    def set_unit(cls, unit):
        cls.unit = unit
        print(f"  Default unit changed to: {cls.unit}")

    # Static method — pure conversion, no object or class needed
    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0

    @staticmethod
    def is_boiling(celsius):
        return celsius >= 100


boiling  = Temperature(100)
freezing = Temperature(0)
body     = Temperature(37)

print(boiling.describe())      # 100°C = 212.0°F = 373.15K
print(freezing.describe())     # 0°C = 32.0°F = 273.15K
print(body.describe())         # 37°C = 98.6°F = 310.15K

# class method — create from Fahrenheit
t = Temperature.from_fahrenheit(98.6)
print(f"  98.6°F = {t.degrees}°C")

# static method — utility, no instance needed
print(f"  Is 0°C freezing?  {Temperature.is_freezing(0)}")
print(f"  Is 25°C freezing? {Temperature.is_freezing(25)}")
print(f"  Is 100°C boiling? {Temperature.is_boiling(100)}")
```

**Output:**
```
100°C = 212.0°F = 373.15K
0°C = 32.0°F = 273.15K
37°C = 98.6°F = 310.15K
  98.6°F = 37.0°C
  Is 0°C freezing?  True
  Is 25°C freezing? False
  Is 100°C boiling? True
```

---

## Class Methods as Factory / Alternative Constructors

A very common pattern: you want to create objects from different input formats.

```python
from datetime import date

class Person:
    def __init__(self, name, birth_year):
        self.name       = name
        self.birth_year = birth_year

    @classmethod
    def from_birth_date(cls, name, birth_date_str):
        """Create a Person from a 'YYYY-MM-DD' string."""
        year = int(birth_date_str.split("-")[0])
        return cls(name, year)

    @classmethod
    def from_dict(cls, data):
        """Create a Person from a dictionary."""
        return cls(data["name"], data["birth_year"])

    def age(self):
        return date.today().year - self.birth_year

    def info(self):
        print(f"  {self.name}, born {self.birth_year}, age {self.age()}")


# three ways to create a Person
p1 = Person("Alice", 1995)
p2 = Person.from_birth_date("Bob", "1990-06-15")
p3 = Person.from_dict({"name": "Carol", "birth_year": 2000})

p1.info()   #   Alice, born 1995, age 31
p2.info()   #   Bob,   born 1990, age 36
p3.info()   #   Carol, born 2000, age 26
```

---

## Real-World Example — User Validator

```python
import re

class User:
    min_password_length = 8   # class variable

    def __init__(self, username, email, password):
        if not self.is_valid_email(email):
            raise ValueError(f"Invalid email: {email}")
        if not self.is_strong_password(password):
            raise ValueError(f"Password must be at least {User.min_password_length} chars")

        self.username = username
        self.email    = email
        self._password = password   # private (covered in encapsulation)

    # Instance method
    def greet(self):
        return f"Hello, {self.username}!"

    # Class method — alternative constructor from a form dict
    @classmethod
    def from_form(cls, form_data):
        return cls(
            form_data["username"],
            form_data["email"],
            form_data["password"]
        )

    # Static methods — pure validation utilities
    @staticmethod
    def is_valid_email(email):
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    @staticmethod
    def is_strong_password(password):
        return len(password) >= User.min_password_length


# create directly
u1 = User("alice", "alice@example.com", "securePass1")
print(u1.greet())

# create from a form submission
form = {"username": "bob", "email": "bob@example.com", "password": "mypassword"}
u2   = User.from_form(form)
print(u2.greet())

# use static methods without creating any object
print(User.is_valid_email("bad-email"))           # False
print(User.is_valid_email("good@example.com"))    # True
print(User.is_strong_password("short"))           # False
print(User.is_strong_password("longenoughpass"))  # True

# validation in __init__
try:
    bad = User("x", "not-an-email", "pass")
except ValueError as e:
    print(f"  Error: {e}")
```

**Output:**
```
Hello, alice!
Hello, bob!
False
True
False
True
  Error: Invalid email: not-an-email
```

---

## Summary Table

| | Instance method | Class method | Static method |
|---|---|---|---|
| Decorator | *(none)* | `@classmethod` | `@staticmethod` |
| First param | `self` | `cls` | *(none)* |
| Access to instance data? | ✅ Yes | ❌ No | ❌ No |
| Access to class data? | ✅ Yes (via `self.__class__`) | ✅ Yes | ❌ No |
| Can be called on instance? | ✅ | ✅ | ✅ |
| Can be called on class? | ❌ | ✅ | ✅ |
| Common use | Regular methods | Factory / alternative constructors | Utility helpers |

---

## Common Mistakes

```python
# ❌ Calling a class method on an instance and expecting self
class Foo:
    @classmethod
    def create(cls):
        return cls()    # cls is Foo — correct

f = Foo.create()   # works
f2 = f.create()    # also works — cls is still Foo

# ❌ Trying to access self in a static method
class Math:
    precision = 2

    @staticmethod
    def round_it(n):
        return round(n, Math.precision)   # ✅ use class name
        # return round(n, self.precision) # ❌ no self in static method
```

---

## Key Takeaways

- **Instance methods** take `self` — use them for anything that reads or writes object data.
- **Class methods** take `cls` — use them as factory/alternative constructors or to modify class variables.
- **Static methods** take nothing — use them for utility functions logically related to the class.
- All three can be called on an instance; class methods and static methods can also be called on the class directly.

---

*← [05 — Class vs Instance Variables](05-class-vs-instance-variables.md) · [→ 07 — Encapsulation](07-encapsulation.md)*
