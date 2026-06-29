# 01 — What is OOP?

---

## Why do you need OOP?

Imagine you are writing a program to manage 100 students. Without OOP:

```python
# Procedural approach — parallel variables for every student
student1_name  = "Alice"
student1_grade = 90
student1_email = "alice@school.com"

student2_name  = "Bob"
student2_grade = 75
student2_email = "bob@school.com"

# What if you need to print a report for each?
def print_report(name, grade, email):
    print(f"{name} | Grade: {grade} | {email}")

print_report(student1_name, student1_grade, student1_email)
print_report(student2_name, student2_grade, student2_email)
```

This works for 2 students. With 100 students it becomes unmaintainable — variables scatter everywhere, functions have no idea which student they belong to, and adding a new field (like `phone`) means changing every function.

**OOP solves this by keeping data and behaviour together in one place.**

```python
# OOP approach — one class, unlimited objects
class Student:
    def __init__(self, name, grade, email):
        self.name  = name
        self.grade = grade
        self.email = email

    def print_report(self):
        print(f"{self.name} | Grade: {self.grade} | {self.email}")

s1 = Student("Alice", 90, "alice@school.com")
s2 = Student("Bob",   75, "bob@school.com")

s1.print_report()   # Alice | Grade: 90 | alice@school.com
s2.print_report()   # Bob   | Grade: 75 | bob@school.com
```

---

## Where is OOP used?

OOP is everywhere in real software:

| Domain | Examples |
|---|---|
| Web frameworks | Django `Model`, Flask `Blueprint`, FastAPI `BaseModel` |
| GUI applications | Buttons, windows, forms — all objects |
| Games | Player, Enemy, Weapon — all classes |
| Data science | pandas `DataFrame`, sklearn `LinearRegression` |
| File handling | Python's own `Path`, file objects |
| Databases | SQLAlchemy models map to database tables |
| APIs | Pydantic models validate request/response data |

Even Python's built-in types are classes:

```python
print(type("hello"))    # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type(42))         # <class 'int'>
```

---

## When should you use OOP?

| Use OOP when... | Stick with functions when... |
|---|---|
| You have things with **data + behaviour** together | Simple scripts or one-off tasks |
| You need **multiple instances** of the same thing | No repeated data structures |
| Code will **grow and be maintained** over time | Quick data transformations |
| You want to **model real-world entities** | One-time calculations |
| You are building a **library or framework** | Short utility scripts |

---

## The Concept — Procedural vs OOP

**Procedural thinking:** "What steps do I perform?"
**OOP thinking:** "What things exist, and what can they do?"

| Aspect | Procedural | OOP |
|---|---|---|
| Data | Variables scattered in code | Bundled inside objects |
| Behaviour | Standalone functions | Methods attached to objects |
| Reuse | Copy-paste or import | Inheritance and composition |
| Scale | Gets messy as code grows | Stays organised at large scale |
| Real-world fit | Good for recipes, scripts | Good for modelling entities |

---

## The 4 Pillars of OOP

Every OOP language — Python, Java, C++, C# — is built on four ideas:

### 1. Encapsulation
Bundle data and methods together. Hide internal details from the outside world.

```
"A car hides its engine — you just press the accelerator."
```

### 2. Inheritance
A child class inherits data and methods from a parent class. Reuse without copy-pasting.

```
"A Labrador IS-A Dog. A Dog IS-AN Animal."
```

### 3. Polymorphism
The same method name works differently for different objects.

```
"A Dog speaks() → 'Woof'. A Cat speaks() → 'Meow'."
```

### 4. Abstraction
Hide complexity. Define what something must do, not how it does it.

```
"You press a button on the ATM — you don't need to know the banking internals."
```

---

## Basic Example — Class vs No Class

```python
# ─── WITHOUT OOP ─────────────────────────────────────────
name  = "Rex"
breed = "Labrador"
age   = 3

def dog_speak(name):
    return f"{name} says: Woof!"

def dog_info(name, breed, age):
    return f"{name} is a {breed}, {age} years old"

print(dog_speak(name))
print(dog_info(name, breed, age))

# ─── WITH OOP ─────────────────────────────────────────────
class Dog:
    def __init__(self, name, breed, age):
        self.name  = name
        self.breed = breed
        self.age   = age

    def speak(self):
        return f"{self.name} says: Woof!"

    def info(self):
        return f"{self.name} is a {self.breed}, {self.age} years old"

rex   = Dog("Rex",   "Labrador", 3)
buddy = Dog("Buddy", "Poodle",   5)

print(rex.speak())          # Rex says: Woof!
print(buddy.info())         # Buddy is a Poodle, 5 years old
print(rex.info())           # Rex is a Labrador, 3 years old
```

**Output:**
```
Rex says: Woof!
Rex is a Labrador, 3 years old
Rex says: Woof!
Buddy is a Poodle, 5 years old
Rex is a Labrador, 3 years old
```

Notice: once the `Dog` class is defined, creating another dog takes one line. With procedural code, you would need new variables for every dog.

---

## Real-World Example — Library System

```python
# Modelling a library with OOP

class Book:
    def __init__(self, title, author, copies):
        self.title   = title
        self.author  = author
        self.copies  = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"  '{self.title}' borrowed. Copies left: {self.copies}")
        else:
            print(f"  '{self.title}' is not available.")

    def return_book(self):
        self.copies += 1
        print(f"  '{self.title}' returned. Copies now: {self.copies}")

    def status(self):
        print(f"  {self.title} by {self.author} — {self.copies} copies available")


book1 = Book("Python Crash Course", "Eric Matthes", 3)
book2 = Book("Clean Code",          "Robert Martin", 1)

book1.status()      # Python Crash Course by Eric Matthes — 3 copies available
book1.borrow()      # 'Python Crash Course' borrowed. Copies left: 2
book1.borrow()      # 'Python Crash Course' borrowed. Copies left: 1
book2.borrow()      # 'Clean Code' borrowed. Copies left: 0
book2.borrow()      # 'Clean Code' is not available.
book2.return_book() # 'Clean Code' returned. Copies now: 1
```

**Output:**
```
  Python Crash Course by Eric Matthes — 3 copies available
  'Python Crash Course' borrowed. Copies left: 2
  'Python Crash Course' borrowed. Copies left: 1
  'Clean Code' borrowed. Copies left: 0
  'Clean Code' is not available.
  'Clean Code' returned. Copies now: 1
```

---

## Common Mistakes

- **OOP-ing everything** — not every script needs classes. A 20-line script that runs once does not need OOP.
- **Thinking class = function** — a class is a template for objects, not just a container for functions.
- **Ignoring `self`** — forgetting `self` in method parameters is the #1 beginner error.

---

## Key Takeaways

- OOP organises code around **objects** — things that have data and behaviour.
- A **class** is a blueprint; an **object** is one real instance of that blueprint.
- The 4 pillars are **Encapsulation, Inheritance, Polymorphism, Abstraction**.
- OOP shines when modelling real-world entities or building systems that grow over time.
- Python's built-in types (`str`, `list`, `dict`) are already classes.

---

*← [Module 09 — Modules & pip](../09-modules-and-pip/README.md) · [→ 02 — Class and Object](02-class-and-object.md)*
