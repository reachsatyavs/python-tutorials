# 11 — Multiple Inheritance & Mixins

---

## Why does multiple inheritance exist?

Some real-world things genuinely have abilities from more than one independent source:

- A **FlyingFish** can both fly and swim.
- A **ManagerEngineer** can both manage people and write code.
- A **LoggedCachedAPI** needs both logging behaviour and caching behaviour.

Copying the code into each class is the procedural mistake. Inheriting from two focused parents is the OOP solution.

---

## Where is it used?

| Pattern | Example |
|---|---|
| **Mixins** | Django's `LoginRequiredMixin`, `PermissionRequiredMixin` |
| **Abstract interfaces** | Python's own `collections.abc.Sequence`, `Mapping` |
| **Test helpers** | `unittest.TestCase` + a custom `DatabaseTestMixin` |
| **Framework extensions** | Flask-Login, Flask-Admin mix in behaviour via multiple inheritance |

---

## When should you use it?

| Use multiple inheritance when... | Avoid it when... |
|---|---|
| Parents are **independent** (no shared methods) | Parents define the **same method** — use composition instead |
| You are building **mixins** — small focused ability classes | The hierarchy gets deeper than 2–3 levels |
| Standard library or framework uses it (you must follow the pattern) | A simple `has-a` relationship would be cleaner |

---

## The Concept

```python
class Child(Parent1, Parent2):
    pass
```

`Child` gets all methods from `Parent1` **and** `Parent2`. If both parents have the same method, Python uses the **MRO (Method Resolution Order)** to decide which one wins.

---

## Example 1 — Simple Mixin: Duck

```python
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

# Duck inherits from BOTH — no conflict, different methods
class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

    def quack(self):
        return f"{self.name} says Quack!"


d = Duck("Donald")
print(d.fly())    # from Flyable   → I can fly!
print(d.swim())   # from Swimmable → I can swim!
print(d.quack())  # own method     → Donald says Quack!
```

**Output:**
```
I can fly!
I can swim!
Donald says Quack!
```

This is the cleanest form of multiple inheritance — each parent contributes **different, non-overlapping** methods. No conflicts, no confusion.

---

## Example 2 — The Diamond Problem

Multiple inheritance gets tricky when two parents define the **same method**:

```
        A
       / \
      B   C
       \ /
        D        ← who does D.hello() call?
```

```python
class A:
    def hello(self):
        return "Hello from A"

class B(A):
    def hello(self):
        return "Hello from B"

class C(A):
    def hello(self):
        return "Hello from C"

class D(B, C):   # who wins?
    pass


d = D()
print(d.hello())   # "Hello from B"
```

**Output:**
```
Hello from B
```

**B wins** — because it is listed first in `class D(B, C)`.

---

## MRO — Method Resolution Order

Python solves the diamond problem with the **C3 Linearisation algorithm**, which produces a predictable left-to-right, depth-aware order called the **MRO**.

```python
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

# Readable version
print([c.__name__ for c in D.__mro__])
# ['D', 'B', 'C', 'A', 'object']
```

Python walks this list **left to right** and stops at the **first class that has the method**:

```
D → no hello()
B → has hello() ✅  stop here → returns "Hello from B"
```

If `B` did not define `hello()`, Python would continue to `C`, then `A`, then `object`.

### Change the order — change the winner

```python
class E(C, B):   # C first this time
    pass

print(E().hello())              # "Hello from C"
print([c.__name__ for c in E.__mro__])
# ['E', 'C', 'B', 'A', 'object']
```

---

## Example 3 — `super()` follows the MRO, not just the parent

This is the subtlest part of multiple inheritance. `super()` does **not** mean "call my direct parent" — it means "call the **next class in the MRO**":

```python
class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return "B → " + super().hello()   # next in MRO after B

class C(A):
    def hello(self):
        return "C → " + super().hello()   # next in MRO after C

class D(B, C):
    def hello(self):
        return "D → " + super().hello()   # next in MRO after D


print(D().hello())
# D → B → C → A

print([c.__name__ for c in D.__mro__])
# ['D', 'B', 'C', 'A', 'object']
```

**Output:**
```
D → B → C → A
```

Each `super().hello()` calls the **next** class in `D`'s MRO — not just its own parent. This is how cooperative multiple inheritance works in Python, and why `super()` is safe to use in a chain.

---

## Example 4 — Real-World Mixin Pattern

Mixins are small classes that add one specific ability. They are the most practical use of multiple inheritance.

```python
# ── Mixins — small, focused, no __init__ ─────────────────────

class LogMixin:
    def log(self, message):
        print(f"  [LOG] {type(self).__name__}: {message}")


class SerializeMixin:
    def to_dict(self):
        return self.__dict__    # converts all instance attrs to a dict

    def summary(self):
        data = self.to_dict()
        return ", ".join(f"{k}={v}" for k, v in data.items())


# ── Base class ────────────────────────────────────────────────

class User:
    def __init__(self, name, email, role="user"):
        self.name  = name
        self.email = email
        self.role  = role


# ── Combine with mixins ───────────────────────────────────────

class TrackedUser(LogMixin, SerializeMixin, User):
    def __init__(self, name, email, role="user"):
        super().__init__(name, email, role)

    def login(self):
        self.log(f"{self.name} logged in")      # from LogMixin

    def profile(self):
        self.log(f"profile viewed: {self.summary()}")  # from both mixins


alice = TrackedUser("Alice", "alice@example.com", "admin")
alice.login()
alice.profile()
print(f"  Dict: {alice.to_dict()}")
```

**Output:**
```
  [LOG] TrackedUser: Alice logged in
  [LOG] TrackedUser: profile viewed: name=Alice, email=alice@example.com, role=admin
  Dict: {'name': 'Alice', 'email': 'alice@example.com', 'role': 'admin'}
```

The mixins add `log()`, `to_dict()`, and `summary()` without touching `User` at all. You can mix them into any class in the codebase.

---

## Example 5 — Flying Fish (natural multiple inheritance)

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"  {self.name} breathes")


class Flyable:
    def fly(self):
        print(f"  {self.name} is flying")   # uses self.name set by Animal.__init__


class Swimmable:
    def swim(self):
        print(f"  {self.name} is swimming")


class FlyingFish(Animal, Flyable, Swimmable):
    pass   # gets everything from all three


class Eagle(Animal, Flyable):
    def hunt(self):
        print(f"  {self.name} is hunting")


class Salmon(Animal, Swimmable):
    pass


fish  = FlyingFish("Exocoetus")
eagle = Eagle("Bald Eagle")
salmon = Salmon("Chinook")

fish.breathe(); fish.fly(); fish.swim()
print()
eagle.fly(); eagle.hunt()
print()
salmon.swim()

# MRO for FlyingFish
print()
print("  FlyingFish MRO:", [c.__name__ for c in FlyingFish.__mro__])
```

**Output:**
```
  Exocoetus breathes
  Exocoetus is flying
  Exocoetus is swimming

  Bald Eagle is flying
  Bald Eagle is hunting

  Chinook is swimming

  FlyingFish MRO: ['FlyingFish', 'Animal', 'Flyable', 'Swimmable', 'object']
```

---

## Rules for Safe Multiple Inheritance

| Rule | Why |
|---|---|
| Keep mixins **small and focused** | One ability per mixin — easy to read and reuse |
| Mixins should have **no `__init__`** (or call `super().__init__()`) | Avoids breaking the MRO chain |
| Always use `super()` — never call `ParentClass.method(self)` directly | Lets cooperative inheritance work correctly |
| Put the **main base class last** in the inheritance list | Mixins first, concrete base last: `class X(MixinA, MixinB, Base)` |
| Inspect `__mro__` when in doubt | `print([c.__name__ for c in MyClass.__mro__])` |

---

## Quick Summary

```
Single inheritance:    class Dog(Animal):
Multi-level:           class Dog(Mammal):  class Mammal(Animal):
Multiple inheritance:  class Duck(Flyable, Swimmable):

MRO:   Left → right through the class list, then up each branch
       Inspect: MyClass.__mro__  or  help(MyClass)

super():  Calls the NEXT class in the MRO, not just the direct parent
          Safe for cooperative inheritance chains

Mixin pattern:  Small classes that add one focused ability
                No state, no __init__, just methods
                class TrackedUser(LogMixin, SerializeMixin, User):
```

---

## Common Mistakes

```python
# ❌ Mixin with __init__ that does not call super() — breaks the chain
class LogMixin:
    def __init__(self):       # dangerous if used in multiple inheritance
        self.log_level = "INFO"
        # forgot super().__init__()

# ✅ Always pass through
class LogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   # forward all args up the chain
        self.log_level = "INFO"

# ❌ Calling parent directly instead of super()
class B(A):
    def hello(self):
        return A.hello(self)   # skips MRO — other classes in the chain are bypassed

# ✅ Use super() so the full MRO chain is respected
class B(A):
    def hello(self):
        return super().hello()
```

---

*← [08 — Inheritance](08-inheritance.md) · [→ 09 — Polymorphism](09-polymorphism.md)*
