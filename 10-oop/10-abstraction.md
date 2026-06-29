# 10 — Abstraction

---

## Why do you need abstraction?

Consider a team building a notification system. You want Email, SMS, and Push notifications — all of which must have a `send()` method. Without abstraction, there is no guarantee. A developer might forget to implement `send()` in one class, and the bug shows up only at runtime:

```python
# ❌ No contract — anything can be forgotten
class EmailNotifier:
    def send(self, msg): print(f"Email: {msg}")

class SMSNotifier:
    def sned(self, msg): print(f"SMS: {msg}")   # typo! 'sned' not 'send'
    # nobody catches this until runtime

notifiers = [EmailNotifier(), SMSNotifier()]
for n in notifiers:
    n.send("Hello")   # AttributeError on SMSNotifier — caught too late
```

Abstraction solves this by defining a **contract** — a set of methods every subclass **must** implement. If a subclass forgets, Python raises an error at object creation time — not at runtime:

```python
# ✅ With abstract class — contract enforced at creation time
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message): ...

class SMSNotifier(Notifier):
    pass   # forgot to implement send()

sms = SMSNotifier()   # TypeError immediately — "Can't instantiate abstract class"
```

---

## Where is abstraction used?

| Example | Abstract base defines |
|---|---|
| Python's `collections.abc` | `Iterable`, `Sequence`, `Mapping` contracts |
| Django ORM | `Model` enforces `save()`, `delete()` |
| sklearn | `BaseEstimator` requires `fit()`, `predict()` |
| Payment gateways | Every gateway must have `charge()`, `refund()` |
| File storage backends | S3, local, GCS all must have `read()`, `write()` |

---

## When should you use abstraction?

Use an abstract class when:
- You want to **enforce a contract** — guarantee every subclass has specific methods.
- The base class should **never be instantiated directly** — only its children should.
- You are building a **framework or plugin system** where others will extend your base class.

---

## The Concept

An **Abstract Base Class (ABC)** is a class that:
1. Cannot be instantiated directly.
2. Defines methods that subclasses **must** implement (`@abstractmethod`).
3. Can have regular (concrete) methods too — shared logic all children use.

```python
from abc import ABC, abstractmethod

class Shape(ABC):                      # inherits from ABC → abstract class

    @abstractmethod
    def area(self):                    # MUST be implemented by subclasses
        pass

    @abstractmethod
    def perimeter(self):               # MUST be implemented by subclasses
        pass

    def describe(self):                # concrete method — shared by all
        print(f"  {type(self).__name__}: area={self.area():.2f}, "
              f"perimeter={self.perimeter():.2f}")
```

---

## Basic Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    def describe(self):
        print(f"  {type(self).__name__:<12} "
              f"area={self.area():.2f}  perimeter={self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for s in shapes:
    s.describe()

# try to instantiate the abstract class directly
try:
    s = Shape()
except TypeError as e:
    print(f"\n  Cannot create Shape directly: {e}")

# try a subclass that forgets to implement a method
class BadShape(Shape):
    def area(self):
        return 0
    # forgot perimeter!

try:
    b = BadShape()
except TypeError as e:
    print(f"  Incomplete subclass: {e}")
```

**Output:**
```
  Circle       area=78.54  perimeter=31.42
  Rectangle    area=24.00  perimeter=20.00
  Triangle     area=6.00   perimeter=12.00

  Cannot create Shape directly: Can't instantiate abstract class Shape without an implementation for abstract methods 'area', 'perimeter'
  Incomplete subclass: Can't instantiate abstract class BadShape without an implementation for abstract method 'perimeter'
```

---

## Abstract class with concrete methods

An abstract class can also have fully implemented methods — shared logic that all children get:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    @abstractmethod
    def fuel_type(self): pass       # must be implemented

    @abstractmethod
    def range_km(self): pass        # must be implemented

    # concrete — shared by all vehicles
    def age(self):
        return 2026 - self.year

    def info(self):
        print(f"  {self.year} {self.make} {self.model} | "
              f"Fuel: {self.fuel_type()} | "
              f"Range: {self.range_km()} km | "
              f"Age: {self.age()} yrs")


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh

    def fuel_type(self):
        return "Electric"

    def range_km(self):
        return self.battery_kwh * 6   # rough estimate: 6 km per kWh


class PetrolCar(Vehicle):
    def __init__(self, make, model, year, tank_litres):
        super().__init__(make, model, year)
        self.tank_litres = tank_litres

    def fuel_type(self):
        return "Petrol"

    def range_km(self):
        return self.tank_litres * 15  # rough estimate: 15 km per litre


tesla  = ElectricCar("Tesla",   "Model 3", 2023, battery_kwh=75)
honda  = PetrolCar("Honda",     "City",    2021, tank_litres=40)
tata   = ElectricCar("Tata",    "Nexon EV",2022, battery_kwh=40)

tesla.info()
honda.info()
tata.info()

total_range = sum(v.range_km() for v in [tesla, honda, tata])
print(f"\n  Combined range: {total_range} km")
```

**Output:**
```
  2023 Tesla Model 3 | Fuel: Electric | Range: 450 km | Age: 3 yrs
  2021 Honda City | Fuel: Petrol | Range: 600 km | Age: 5 yrs
  2022 Tata Nexon EV | Fuel: Electric | Range: 240 km | Age: 4 yrs

  Combined range: 1290 km
```

---

## Real-World Example — Storage Backend

```python
from abc import ABC, abstractmethod

class StorageBackend(ABC):
    """Abstract contract that all storage backends must follow."""

    @abstractmethod
    def save(self, filename, data):   pass

    @abstractmethod
    def load(self, filename):         pass

    @abstractmethod
    def delete(self, filename):       pass

    @abstractmethod
    def exists(self, filename):       pass

    # concrete — every backend gets this for free
    def save_if_not_exists(self, filename, data):
        if not self.exists(filename):
            self.save(filename, data)
        else:
            print(f"  '{filename}' already exists — skipping")


class LocalStorage(StorageBackend):
    def __init__(self):
        self._store = {}

    def save(self, filename, data):
        self._store[filename] = data
        print(f"  [Local] Saved '{filename}'")

    def load(self, filename):
        return self._store.get(filename, None)

    def delete(self, filename):
        self._store.pop(filename, None)
        print(f"  [Local] Deleted '{filename}'")

    def exists(self, filename):
        return filename in self._store


class CloudStorage(StorageBackend):
    def __init__(self, bucket):
        self.bucket = bucket
        self._store = {}

    def save(self, filename, data):
        self._store[filename] = data
        print(f"  [Cloud:{self.bucket}] Uploaded '{filename}'")

    def load(self, filename):
        return self._store.get(filename, None)

    def delete(self, filename):
        self._store.pop(filename, None)
        print(f"  [Cloud:{self.bucket}] Deleted '{filename}'")

    def exists(self, filename):
        return filename in self._store


def backup(storage: StorageBackend, files: dict):
    """Works with ANY StorageBackend — local, cloud, S3, GCS..."""
    for name, content in files.items():
        storage.save_if_not_exists(name, content)


local = LocalStorage()
cloud = CloudStorage("my-bucket")

files = {"config.json": "{}", "report.csv": "name,score\n", "log.txt": "started\n"}

print("--- Local storage ---")
backup(local, files)
backup(local, files)   # second call — files already exist

print("\n--- Cloud storage ---")
backup(cloud, files)
```

**Output:**
```
--- Local storage ---
  [Local] Saved 'config.json'
  [Local] Saved 'report.csv'
  [Local] Saved 'log.txt'
  'config.json' already exists — skipping
  'report.csv' already exists — skipping
  'log.txt' already exists — skipping

--- Cloud storage ---
  [Cloud:my-bucket] Uploaded 'config.json'
  [Cloud:my-bucket] Uploaded 'report.csv'
  [Cloud:my-bucket] Uploaded 'log.txt'
```

---

## Abstract vs Interface vs Concrete

| | Abstract class | "Interface" (pure ABC) | Concrete class |
|---|---|---|---|
| Can be instantiated? | ❌ No | ❌ No | ✅ Yes |
| Has abstract methods? | ✅ Some | ✅ All | ❌ None |
| Has concrete methods? | ✅ Yes | ❌ No | ✅ Yes |
| Python keyword | `class X(ABC)` | `class X(ABC)` (all `@abstractmethod`) | `class X:` |

Python doesn't have a separate `interface` keyword like Java — an ABC where all methods are abstract serves the same purpose.

---

## Common Mistakes

```python
# ❌ Forgetting to import ABC and abstractmethod
from abc import ABC, abstractmethod   # always import both

# ❌ Abstract method with an implementation — still abstract!
class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0    # this body is ignored — subclasses must still override

# ✅ Use ... or pass for abstract methods
class Shape(ABC):
    @abstractmethod
    def area(self): ...

# ❌ Not calling super().__init__ in child
class Circle(Shape):
    def __init__(self, r):
        # forgot super().__init__() if Shape.__init__ exists
        self.r = r
```

---

## Key Takeaways

- **Abstraction** hides complexity and defines *what* something must do, not *how*.
- `ABC` (Abstract Base Class) from the `abc` module enforces a **contract**.
- Mark required methods with `@abstractmethod` — subclasses must implement them.
- An abstract class **cannot be instantiated** — only its concrete subclasses can.
- Abstract classes can also have **concrete methods** — shared logic for all children.
- This is the foundation of **plugin systems, frameworks, and extensible APIs**.

---

*← [09 — Polymorphism](09-polymorphism.md) · [→ Module README](README.md)*
