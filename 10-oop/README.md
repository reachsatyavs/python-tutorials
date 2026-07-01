# Module 10 — Object-Oriented Programming (OOP)

OOP is a way of organising code around **objects** — bundles of data and behaviour — instead of loose functions and variables. Python is fully object-oriented: everything you have used so far (`str`, `list`, `dict`, even functions) is an object under the hood.

**Prerequisites:** `[05-functions/](../05-functions/README.md)` — functions, scope. `[09-modules-and-pip/](../09-modules-and-pip/README.md)` — modules, `import`.

---

## Contents

| # | File | Type | What it covers |
|---|------|------|----------------|
| 1 | `[01-what-is-oop.md](01-what-is-oop.md)` | Notes | What OOP is, why it exists, the 4 pillars, OOP vs procedural |
| 2 | `[02-class-and-object.md](02-class-and-object.md)` | Notes | `class` keyword, creating objects, attributes, methods |
| 3 | `[03-init-constructor.md](03-init-constructor.md)` | Notes | `__init__`, constructors, can you rename `__init__`? |
| 4 | `[04-self-keyword.md](04-self-keyword.md)` | Notes | Why `self` exists, can you rename it? |
| 5 | `[05-class-vs-instance-variables.md](05-class-vs-instance-variables.md)` | Notes | Shared vs per-object data, class variables, instance variables |
| 6 | `[06-methods.md](06-methods.md)` | Notes | Instance methods, `@classmethod`, `@staticmethod` |
| 7 | `[07-encapsulation.md](07-encapsulation.md)` | Notes | Public / protected / private, `@property`, getters & setters |
| 8 | `[08-inheritance.md](08-inheritance.md)` | Notes | Parent/child classes, `super()`, method overriding |
| 9 | `[09-polymorphism.md](09-polymorphism.md)` | Notes | Same interface, different behaviour, duck typing |
| 10 | `[10-abstraction.md](10-abstraction.md)` | Notes | `ABC`, `@abstractmethod`, defining contracts |
| 11 | `[11-multiple-inheritance.md](11-multiple-inheritance.md)` | Notes | Multiple inheritance, mixins, diamond problem, MRO, `super()` in chains |
| — | `[oop_basics.py](oop_basics.py)` | Script | 10 runnable examples — class, object, init, self, variables, methods |
| — | `[oop_advanced.py](oop_advanced.py)` | Script | 10 runnable examples — encapsulation, inheritance, polymorphism, abstraction |

---

## Learning order

1. Read `[01-what-is-oop.md](01-what-is-oop.md)` — get the big picture before writing any class.
2. Read `[02-class-and-object.md](02-class-and-object.md)` then `[03-init-constructor.md](03-init-constructor.md)` and `[04-self-keyword.md](04-self-keyword.md)` together — these three are the core of every class.
3. Read `[05-class-vs-instance-variables.md](05-class-vs-instance-variables.md)` and `[06-methods.md](06-methods.md)`.
4. Run `python3 oop_basics.py` to see all fundamentals in action.
5. Read `[07-encapsulation.md](07-encapsulation.md)` → `[08-inheritance.md](08-inheritance.md)` → `[09-polymorphism.md](09-polymorphism.md)` → `[10-abstraction.md](10-abstraction.md)` — the four pillars.
6. Run `python3 oop_advanced.py` to see all four pillars in action.

---

## Quick mental model

| Concept | One line |
|---------|----------|
| **Class** | A blueprint — `class Dog:` |
| **Object** | An instance of the blueprint — `my_dog = Dog("Rex")` |
| `__init__` | Runs automatically when you create an object; sets up initial data |
| `self` | The object itself, passed automatically to every instance method |
| **Instance variable** | Belongs to one object — `self.name = name` |
| **Class variable** | Shared across all objects — `Dog.count = 0` |
| **Encapsulation** | Hide internal details; expose only what's needed |
| **Inheritance** | Child class reuses parent class code — `class Labrador(Dog):` |
| **Polymorphism** | Same method name, different behaviour per class |
| **Abstraction** | Define *what* a class must do, not *how* — `ABC` + `@abstractmethod` |

---

## The 4 Pillars at a glance

```
┌─────────────────────────────────────────────────────┐
│                   4 Pillars of OOP                  │
├──────────────────┬──────────────────────────────────┤
│  Encapsulation   │  Bundle data + methods together  │
│                  │  Hide internal details            │
├──────────────────┼──────────────────────────────────┤
│  Inheritance     │  Child reuses parent's code      │
│                  │  Extend without copy-pasting      │
├──────────────────┼──────────────────────────────────┤
│  Polymorphism    │  One interface, many forms        │
│                  │  Same method name, different output│
├──────────────────┼──────────────────────────────────┤
│  Abstraction     │  Hide complexity behind an API   │
│                  │  Force a contract with ABC        │
└──────────────────┴──────────────────────────────────┘
```

---

## Next module

**11 — Exception Handling** (planned): `try / except / else / finally`, raising custom exceptions, best practices for error handling.
