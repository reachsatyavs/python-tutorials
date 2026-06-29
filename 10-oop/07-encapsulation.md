# 07 — Encapsulation

---

## Why do you need encapsulation?

Imagine a `BankAccount` class where the balance is fully public:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner   = owner
        self.balance = balance   # fully public

account = BankAccount("Alice", 50000)
account.balance = -999999        # ← anyone can do this — no validation!
print(account.balance)           # -999999  — invalid state
```

A bank balance should never go negative through direct assignment. Encapsulation lets you **control how data is accessed and modified** — you hide internal data and expose only a clean, controlled interface.

---

## Where is encapsulation used?

| Example | What is hidden |
|---|---|
| `BankAccount.balance` | Changed only via `deposit()` / `withdraw()` |
| `User.password` | Stored hashed; never exposed raw |
| `Connection.socket` | Internal socket object; you only call `send()` / `receive()` |
| `DataFrame.values` | Internal numpy array; you use DataFrame methods |

---

## When should you use encapsulation?

- When data has **validation rules** (balance ≥ 0, age > 0).
- When internal representation might **change** but the API should stay stable.
- When you want to make some data **read-only** after creation.
- When internal state should only be **modified through controlled methods**.

---

## The Concept — Access Levels in Python

Python does not have true `private`/`public` keywords like Java. Instead, it uses **naming conventions**:

| Convention | Syntax | Meaning |
|---|---|---|
| Public | `self.name` | Anyone can read/write — the default |
| Protected | `self._name` | Internal use; don't use from outside (convention) |
| Private | `self.__name` | Name-mangled; hard to access accidentally from outside |

```python
class Person:
    def __init__(self, name, age, ssn):
        self.name   = name       # public — fine to access directly
        self._age   = age        # protected — "please don't touch from outside"
        self.__ssn  = ssn        # private — name-mangled to _Person__ssn

p = Person("Alice", 28, "123-45-6789")
print(p.name)            # Alice          — ✅ public, fine
print(p._age)            # 28             — works but discouraged
print(p.__ssn)           # AttributeError — name is mangled
print(p._Person__ssn)    # 123-45-6789   — can still access if you really want to
```

> Python's philosophy: "We are all consenting adults." The convention warns you; it doesn't lock you out entirely.

---

## Basic Example — Protected and Private

```python
class Student:
    def __init__(self, name, marks):
        self.name   = name       # public
        self._marks = marks      # protected — internal data
        self.__grade = None      # private
        self.__calculate_grade() # private method

    def __calculate_grade(self):  # private — not meant to be called from outside
        if self._marks >= 90:
            self.__grade = "A"
        elif self._marks >= 75:
            self.__grade = "B"
        elif self._marks >= 60:
            self.__grade = "C"
        else:
            self.__grade = "F"

    def report(self):             # public — the controlled interface
        print(f"  {self.name}: {self._marks} marks → Grade {self.__grade}")


s1 = Student("Alice", 92)
s2 = Student("Bob",   74)

s1.report()    # Alice: 92 marks → Grade A
s2.report()    # Bob: 74 marks → Grade C

# try to access private
# s1.__grade         # AttributeError
# s1.__calculate_grade()  # AttributeError
```

**Output:**
```
  Alice: 92 marks → Grade A
  Bob: 74 marks → Grade C
```

---

## `@property` — The Pythonic Way to Control Access

`@property` lets you define **getter** and **setter** methods that look like plain attribute access from outside:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius   # store internally as protected

    @property
    def radius(self):           # getter — called when you READ  obj.radius
        return self._radius

    @radius.setter
    def radius(self, value):    # setter — called when you WRITE obj.radius = x
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):             # read-only property (no setter)
        return 3.14159 * self._radius ** 2


c = Circle(5)
print(c.radius)          # 5        — calls getter
print(c.area)            # 78.53975 — calls getter

c.radius = 10            # calls setter — validates first
print(c.radius)          # 10
print(c.area)            # 314.159

try:
    c.radius = -3        # triggers setter validation
except ValueError as e:
    print(f"  Error: {e}")

# c.area = 100           # AttributeError — no setter defined (read-only)
```

**Output:**
```
5
78.53975
10
314.159
  Error: Radius must be positive
```

---

## Real-World Example — Bank Account

```python
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.__owner   = owner
        self.__balance = initial_balance
        self.__transactions = []

    # read-only — no setter
    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.__transactions.append(f"+ ₹{amount:,}")
        print(f"  Deposited ₹{amount:,}. Balance: ₹{self.__balance:,}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError(f"Insufficient funds. Balance: ₹{self.__balance:,}")
        self.__balance -= amount
        self.__transactions.append(f"- ₹{amount:,}")
        print(f"  Withdrew ₹{amount:,}. Balance: ₹{self.__balance:,}")

    def statement(self):
        print(f"\n  Account: {self.__owner}")
        print(f"  {'─'*30}")
        for t in self.__transactions:
            print(f"    {t}")
        print(f"  {'─'*30}")
        print(f"  Balance: ₹{self.__balance:,}")


acc = BankAccount("Alice", 10000)
acc.deposit(5000)
acc.deposit(2000)
acc.withdraw(3000)
acc.withdraw(1000)
acc.statement()

# direct assignment blocked
try:
    acc.balance = 999999   # AttributeError — no setter
except AttributeError as e:
    print(f"\n  Cannot set balance directly: {e}")

try:
    acc.withdraw(50000)    # validation kicks in
except ValueError as e:
    print(f"  Error: {e}")
```

**Output:**
```
  Deposited ₹5,000. Balance: ₹15,000
  Deposited ₹2,000. Balance: ₹17,000
  Withdrew ₹3,000. Balance: ₹14,000
  Withdrew ₹1,000. Balance: ₹13,000

  Account: Alice
  ──────────────────────────────
    + ₹5,000
    + ₹2,000
    - ₹3,000
    - ₹1,000
  ──────────────────────────────
  Balance: ₹13,000

  Cannot set balance directly: property 'balance' of 'BankAccount' object has no setter
  Error: Insufficient funds. Balance: ₹13,000
```

---

## Common Mistakes

```python
# ❌ Confusing protected with truly private
class Safe:
    def __init__(self):
        self._secret = "protected"   # still accessible — just a convention

s = Safe()
print(s._secret)   # works — protection is only by convention

# ❌ Name mangling gotcha
class Outer:
    def __init__(self):
        self.__x = 10   # becomes _Outer__x

class Inner(Outer):
    def show(self):
        # print(self.__x)   # AttributeError — looks for _Inner__x
        print(self._Outer__x)   # must use mangled name in subclass

# ✅ Better — use @property for controlled access
```

---

## Key Takeaways

- **Encapsulation** = bundle data + methods + control who can access/modify them.
- Python uses naming conventions: `_protected`, `__private` (name-mangled).
- Use `@property` for clean, Pythonic getters and setters.
- A `@property` without a setter is effectively **read-only**.
- Encapsulation prevents invalid state — validation lives in the setter, not scattered everywhere.

---

*← [06 — Methods](06-methods.md) · [→ 08 — Inheritance](08-inheritance.md)*
