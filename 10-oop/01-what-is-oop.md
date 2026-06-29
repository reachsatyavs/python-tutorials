# 01 — What is OOP?

---

## Why do you need OOP?

### The real problem — a silent bug

Here is a bank account simulation written the procedural way:

```python
# ───── WITHOUT OOP — a bug creeps in silently ─────────────

satya_balance = 1000
priya_balance = 500

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds")
        return balance
    return balance - amount

satya_balance = withdraw(satya_balance, 200)   # ✅ balance reassigned: 800
priya_balance = withdraw(priya_balance, 100)   # ✅ balance reassigned: 400

# Now a teammate writes a new feature and forgets to reassign:
withdraw(satya_balance, 50)   # ← called but return value thrown away!
                               #   nothing ties "balance" to "satya"

print(satya_balance)  # 800 — wrong! should be 750
                      # No error. No warning. Silent bug.
```

**Why does this happen?** In procedural code, the data (`satya_balance`) and the function that changes it (`withdraw`) are two separate things connected only by convention, you have to remember to pass the right variable *and* reassign the result. Forget either step and you get a wrong answer with no feedback from Python.

```python
# ───── WITH OOP — the bug becomes impossible ──────────────

class Account:
    def __init__(self, owner, balance):
        self.owner   = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"  Insufficient funds for {self.owner}")
            return
        self.balance -= amount   # data and method are one unit — state lives here

satya = Account("Satya", 1000)
priya = Account("Priya",  500)

satya.withdraw(200)   # satya.balance is now 800
priya.withdraw(100)   # priya.balance is now 400
satya.withdraw(50)    # satya.balance is now 750 — no reassignment needed

print(satya.balance)  # 750 — correct, always
```

**Output:**
```
750
```

The bug from the procedural version is *structurally impossible* here. `satya.withdraw(50)` operates directly on `satya.balance` — there is no separate variable to reassign, and it cannot accidentally change `priya`'s balance. The data and the method that changes it are the same unit.

> **OOP advantage isn't just organisation — it's correctness, by construction.**

---

### The scaling problem — copy-paste explodes

Beyond bugs, procedural code does not scale. Every new "thing" requires a fresh round of copy-pasted variables and functions:

```python
# ─── Procedural — adding a third account means more parallel variables ───
satya_balance  = 1000
priya_balance  = 500
ravi_balance   = 2000   # new variable
ravi_owner     = "Ravi" # another new variable

def withdraw(balance, amount): ...
def deposit(balance, amount):  ...
def show_balance(owner, balance): ...

show_balance("Satya", satya_balance)
show_balance("Priya", priya_balance)
show_balance("Ravi",  ravi_balance)   # easy to pass wrong variable

# ─── OOP — adding a third account is one line ────────────────────────────
ravi = Account("Ravi", 2000)          # done
```

> With a class, every new object is **one line**. The logic is written once, reused forever.

---

**OOP solves both problems by keeping data and behaviour together in one place.**

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
Bundle data and methods together. **Protect internal data** from being changed incorrectly from outside.

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
Hide complexity. Define **what** something must do, not **how** it does it.

```
"You press a button on the ATM — you don't need to know the banking internals."
```

---

## Encapsulation vs Abstraction — The Confusion Cleared

These two are the most commonly confused pillars because both involve "hiding something". Here is the exact difference:

| Pillar | What it hides | Who benefits |
|---|---|---|
| **Encapsulation** | How **data** is stored and changed | Protects the object's own state from being corrupted |
| **Abstraction** | How something **works internally** | Protects the caller from needing to know the implementation |

### The ATM example

```
Encapsulation  →  The ATM's balance is __balance.
                  You cannot reach in and set it to any number you like.
                  You can only change it through deposit() and withdraw(),
                  which validate your input first.
                  → The DATA is protected.

Abstraction    →  You press "Withdraw ₹500" and money comes out.
                  You have no idea whether it talks to a Visa network,
                  a local bank server, or a third-party processor.
                  → The COMPLEXITY is hidden.
```

### Code side by side

```python
from abc import ABC, abstractmethod

# ── ABSTRACTION ──────────────────────────────────────────────
# Defines WHAT must be done — hides HOW it is done internally
class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount): ...    # caller just calls charge()
                                     # has no idea what happens inside

# ── ENCAPSULATION ────────────────────────────────────────────
# Controls HOW internal data is read and written
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance     # hidden — cannot be set directly from outside

    @property
    def balance(self):               # controlled READ
        return self.__balance

    def deposit(self, amount):       # controlled WRITE — validates first
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

# ── BOTH TOGETHER — the usual real-world pattern ─────────────
class UPIGateway(PaymentGateway):    # satisfies the abstraction contract
    def __init__(self):
        self.__api_key = "secret"    # encapsulated — nobody outside sees this

    def charge(self, amount):        # implements the abstract method
        # caller has no idea about __api_key or the UPI network call
        print(f"  Charging ₹{amount} via UPI")
```

### The sharpest way to remember it

```
Encapsulation  →  "Don't touch my internals directly."   (protects DATA)
Abstraction    →  "Don't worry about how I work."        (protects COMPLEXITY)
```

- **Encapsulation** answers: *"How is this object's data kept safe?"*
- **Abstraction** answers: *"What can I do with this object without knowing its guts?"*

They solve different problems and are often used together, but they are not the same thing.

---

## Basic Example — Score Tracker (procedural bug vs OOP fix)

A score tracker for two players. Watch the bug appear in procedural code and disappear in OOP.

```python
# ─── WITHOUT OOP — easy to write a bug ───────────────────

player1_name  = "Alice"
player1_score = 0

player2_name  = "Bob"
player2_score = 0

def add_score(score, points):
    return score + points

# Teammate writes this — looks right, but result is discarded
add_score(player1_score, 10)        # ← bug! result not saved
player2_score = add_score(player2_score, 5)  # ✅ saved correctly

print(player1_score)  # 0  ← wrong! should be 10, silent bug
print(player2_score)  # 5  ← correct

# ─── WITH OOP — state lives inside the object ─────────────

class Player:
    def __init__(self, name):
        self.name  = name
        self.score = 0

    def add_score(self, points):
        self.score += points        # always updates this player's score
        print(f"  {self.name}: +{points} → total {self.score}")

    def reset(self):
        self.score = 0

    def status(self):
        return f"  {self.name}: {self.score} pts"


alice = Player("Alice")
bob   = Player("Bob")

alice.add_score(10)   # Alice: +10 → total 10
alice.add_score(5)    # Alice: +5  → total 15
bob.add_score(8)      # Bob:   +8  → total 8
bob.add_score(12)     # Bob:   +12 → total 20

print(alice.status())  # Alice: 15 pts
print(bob.status())    # Bob:   20 pts
```

**Output:**
```
  Alice: +10 → total 10
  Alice: +5  → total 15
  Bob:   +8  → total 8
  Bob:   +12 → total 20
  Alice: 15 pts
  Bob:   20 pts
```

`alice.add_score(10)` can only ever update Alice's score. You cannot accidentally call it on Bob's data, and there is no return value to forget to save. The state and the method are the same thing.

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

- OOP organises code around **objects** — things that have data and behaviour bundled together.
- A **class** is a blueprint; an **object** is one real instance of that blueprint.
- In procedural code, data and the function that changes it are two separate things — you can forget to pass the right variable or forget to save the return value. **OOP makes that category of bug impossible.**
- Every new "thing" (account, player, book) in OOP is **one line**: `x = ClassName(...)`. In procedural code it is a new round of copy-pasted variables.
- The real OOP advantage is **correctness by construction**, not just shorter code.
- The 4 pillars are **Encapsulation, Inheritance, Polymorphism, Abstraction** — each covered in its own file.
- Python's built-in types (`str`, `list`, `dict`) are already classes.

---

*← [Module 09 — Modules & pip](../09-modules-and-pip/README.md) · [→ 02 — Class and Object](02-class-and-object.md)*
