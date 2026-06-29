# 03 — `__init__` — The Constructor

---

## Why do you need `__init__`?

Without `__init__`, every object starts blank — you have to set attributes manually after creation, and there is nothing stopping you from forgetting one:

```python
# ❌ Without __init__ — error-prone
class Dog:
    def speak(self):
        return f"{self.name} says Woof!"

rex = Dog()
# rex.speak()  →  AttributeError: 'Dog' object has no attribute 'name'

rex.name = "Rex"      # have to remember to do this manually
rex.speak()           # now works — but only if you didn't forget
```

`__init__` guarantees that **every object is born in a valid, complete state**:

```python
# ✅ With __init__ — every Dog is born complete
class Dog:
    def __init__(self, name, breed):
        self.name  = name
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

rex = Dog("Rex", "Labrador")  # name and breed set automatically
rex.speak()                   # works immediately
```

---

## Where is `__init__` used?

- **Every class** that needs to set up initial data uses `__init__`.
- Django models, Pydantic schemas, dataclasses — all use constructors.
- When you call `pd.DataFrame(data)` or `Path("file.txt")`, Python calls their `__init__`.

---

## When should you use `__init__`?

Always — unless your class truly has no initial data (very rare). Even then, it is good practice to define `__init__` explicitly so the class's intent is clear.

---

## The Concept

`__init__` is called a **constructor** because it constructs (builds) the object. Python calls it automatically the instant you write `Dog("Rex", "Labrador")`.

```
Dog("Rex", "Labrador")
        │
        ▼
Python creates a blank Dog object
        │
        ▼
Python calls __init__(self, "Rex", "Labrador") automatically
        │
        ▼
self.name = "Rex", self.breed = "Labrador" are set
        │
        ▼
The fully-built object is returned and stored in  rex
```

### The double underscores — `__init__`

Methods with double underscores on both sides are called **dunder methods** (double-underscore) or **magic methods**. They are part of Python's data model — Python calls them automatically in specific situations. `__init__` is one of many:

| Dunder | When Python calls it |
|---|---|
| `__init__` | When object is created |
| `__str__` | When you `print(obj)` |
| `__len__` | When you `len(obj)` |
| `__add__` | When you `obj1 + obj2` |

---

## Basic Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


alice = Person("Alice", 28)
bob   = Person("Bob",   35)

print(alice.greet())    # Hi, I'm Alice and I'm 28 years old.
print(bob.greet())      # Hi, I'm Bob and I'm 35 years old.

# attributes set by __init__ are accessible directly
print(alice.name)       # Alice
print(bob.age)          # 35
```

**Output:**
```
Hi, I'm Alice and I'm 28 years old.
Hi, I'm Bob and I'm 35 years old.
Alice
35
```

---

## Default Parameter Values in `__init__`

Just like regular functions, `__init__` can have default values:

```python
class Coffee:
    def __init__(self, size="medium", milk=True, sugar=1):
        self.size  = size
        self.milk  = milk
        self.sugar = sugar

    def describe(self):
        milk_str  = "with milk"  if self.milk  else "black"
        sugar_str = f"{self.sugar} sugar" if self.sugar else "no sugar"
        return f"{self.size.title()} coffee, {milk_str}, {sugar_str}"


c1 = Coffee()                            # all defaults
c2 = Coffee("large")                     # override size
c3 = Coffee("small", milk=False, sugar=0) # override all

print(c1.describe())   # Medium coffee, with milk, 1 sugar
print(c2.describe())   # Large coffee, with milk, 1 sugar
print(c3.describe())   # Small coffee, black, no sugar
```

**Output:**
```
Medium coffee, with milk, 1 sugar
Large coffee, with milk, 1 sugar
Small coffee, black, no sugar
```

---

## Can you rename `__init__`?

**No.** `__init__` is a Python protocol — the name is fixed. Python specifically looks for `__init__` when creating an object. If you rename it, Python will not call it automatically:

```python
class Dog:
    def setup(self, name):       # renamed — Python will NEVER call this automatically
        self.name = name

rex = Dog()
# rex.name doesn't exist — setup() was never called
```

However, you can call `__init__` manually (though you almost never should):

```python
rex = Dog.__new__(Dog)           # create object without calling __init__
Dog.__init__(rex, "Rex")         # manually call __init__
print(rex.name)                  # Rex  — but don't do this in real code
```

> **Rule:** Always name your constructor `__init__`. It is a fixed Python contract.

---

## `__init__` vs `__new__`

Python actually uses two methods to create objects:

| Method | What it does | When you override it |
|---|---|---|
| `__new__` | Creates the raw object in memory | Rarely — singleton patterns, metaclasses |
| `__init__` | Populates the object with data | **Always** — this is your constructor |

You will almost never need `__new__`. Just use `__init__`.

---

## Real-World Example — User Account

```python
class UserAccount:
    def __init__(self, username, email, role="user"):
        if not username:
            raise ValueError("Username cannot be empty")
        if "@" not in email:
            raise ValueError("Invalid email address")

        self.username   = username
        self.email      = email
        self.role       = role
        self.is_active  = True          # default — every new user is active
        self.login_count = 0            # computed default

    def login(self):
        if self.is_active:
            self.login_count += 1
            print(f"  {self.username} logged in. (Login #{self.login_count})")
        else:
            print(f"  Account '{self.username}' is deactivated.")

    def deactivate(self):
        self.is_active = False
        print(f"  Account '{self.username}' deactivated.")

    def info(self):
        status = "active" if self.is_active else "inactive"
        print(f"  {self.username} | {self.email} | {self.role} | {status} | logins: {self.login_count}")


alice = UserAccount("alice",  "alice@example.com")
admin = UserAccount("satya",  "satya@example.com", role="admin")

alice.info()
admin.info()

alice.login()
alice.login()
alice.login()
alice.deactivate()
alice.login()       # blocked — account inactive

print()
alice.info()

# validation in __init__
try:
    bad = UserAccount("", "not-an-email")
except ValueError as e:
    print(f"  Error: {e}")
```

**Output:**
```
  alice | alice@example.com | user | active | logins: 0
  satya | satya@example.com | admin | active | logins: 0
  alice logged in. (Login #1)
  alice logged in. (Login #2)
  alice logged in. (Login #3)
  Account 'alice' is deactivated.
  Account 'alice' is deactivated.

  alice | alice@example.com | user | inactive | logins: 3
  Error: Username cannot be empty
```

---

## Common Mistakes

```python
# ❌ Forgetting self as the first parameter
class Dog:
    def __init__(name, breed):      # TypeError when creating Dog("Rex", "Lab")
        self.name = name

# ✅
class Dog:
    def __init__(self, name, breed):
        self.name  = name
        self.breed = breed

# ❌ Returning something from __init__
class Dog:
    def __init__(self, name):
        self.name = name
        return self                 # TypeError — __init__ must return None

# ✅ __init__ never has a return statement (except bare return)
```

---

## Key Takeaways

- `__init__` is called automatically when you create an object — it **constructs** the object.
- It **cannot be renamed** — Python specifically looks for `__init__`.
- Use it to set all instance attributes and validate input data.
- Default values in `__init__` work exactly like default values in regular functions.
- `__init__` must not return anything (Python enforces this).

---

*← [02 — Class and Object](02-class-and-object.md) · [→ 04 — `self` Keyword](04-self-keyword.md)*
