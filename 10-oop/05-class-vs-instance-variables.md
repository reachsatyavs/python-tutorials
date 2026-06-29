# 05 — Class Variables vs Instance Variables

---

## Why does this distinction matter?

When you put data on a class, you have two choices:
- Store it **per object** (instance variable) — each object has its own copy.
- Store it **on the class itself** (class variable) — all objects share one copy.

Getting this wrong leads to subtle bugs where changing one object accidentally changes all objects.

---

## Where is this used?

| Use case | Variable type |
|---|---|
| Each student's name and grade | Instance variable |
| Company name shared by all employees | Class variable |
| Counting total objects created | Class variable |
| Default settings that can be overridden per object | Class variable with instance override |
| Per-user shopping cart items | Instance variable |

---

## When to use each?

| Use instance variable when... | Use class variable when... |
|---|---|
| Data is unique to each object | Data is shared across all objects |
| Value set at creation or changes over lifetime | Value set once for the entire class |
| e.g. `name`, `age`, `balance` | e.g. `species`, `tax_rate`, `object_count` |

---

## The Concept

```python
class Employee:
    company = "Acme Corp"      # ← class variable — lives on the class, shared

    def __init__(self, name, salary):
        self.name   = name     # ← instance variable — lives on each object
        self.salary = salary
```

```
                  Employee class
                 ┌──────────────────┐
                 │ company="Acme"   │  ← one copy, shared
                 └────────┬─────────┘
                          │
            ┌─────────────┴─────────────┐
            │                           │
     alice (instance)             bob (instance)
    ┌───────────────┐           ┌───────────────┐
    │ name="Alice"  │           │ name="Bob"    │
    │ salary=90000  │           │ salary=75000  │
    └───────────────┘           └───────────────┘
```

---

## Basic Example

```python
class Employee:
    company    = "Acme Corp"   # class variable — shared by all
    headcount  = 0             # class variable — tracks total employees

    def __init__(self, name, salary):
        self.name   = name     # instance variable
        self.salary = salary   # instance variable
        Employee.headcount += 1  # update shared counter

    def info(self):
        print(f"  {self.name:<10} | {Employee.company} | ₹{self.salary:,}")


alice = Employee("Alice", 90000)
bob   = Employee("Bob",   75000)
carol = Employee("Carol", 95000)

alice.info()   # Alice      | Acme Corp | ₹90,000
bob.info()     # Bob        | Acme Corp | ₹75,000
carol.info()   # Carol      | Acme Corp | ₹95,000

print(f"  Total employees: {Employee.headcount}")   # 3
```

**Output:**
```
  Alice      | Acme Corp | ₹90,000
  Bob        | Acme Corp | ₹75,000
  Carol      | Acme Corp | ₹95,000
  Total employees: 3
```

---

## Changing a class variable — affects everyone

```python
class Employee:
    company = "Acme Corp"

    def __init__(self, name):
        self.name = name

alice = Employee("Alice")
bob   = Employee("Bob")

print(alice.company)   # Acme Corp
print(bob.company)     # Acme Corp

Employee.company = "Globex Corp"    # change on the class

print(alice.company)   # Globex Corp  ← changed!
print(bob.company)     # Globex Corp  ← changed!
```

**Output:**
```
Acme Corp
Acme Corp
Globex Corp
Globex Corp
```

---

## Instance variable shadows a class variable

If you set an attribute with the same name on an **instance**, it creates a new instance variable that shadows (hides) the class variable for that object only:

```python
class Dog:
    species = "Canis familiaris"    # class variable

    def __init__(self, name):
        self.name = name

rex   = Dog("Rex")
buddy = Dog("Buddy")

print(rex.species)      # Canis familiaris  — from class
print(buddy.species)    # Canis familiaris  — from class

rex.species = "Canis lupus familiaris"   # creates an INSTANCE variable on rex only
print(rex.species)      # Canis lupus familiaris  — from rex's own copy
print(buddy.species)    # Canis familiaris          — buddy still uses the class variable
print(Dog.species)      # Canis familiaris          — class variable unchanged
```

**Output:**
```
Canis familiaris
Canis familiaris
Canis lupus familiaris
Canis familiaris
Canis familiaris
```

> This is powerful but can cause confusion. Reserve class variables for truly shared data.

---

## Inspecting what's on an object vs on the class

```python
class Employee:
    company = "Acme Corp"
    headcount = 0

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary
        Employee.headcount += 1

alice = Employee("Alice", 90000)

# __dict__ shows only instance variables
print(alice.__dict__)            # {'name': 'Alice', 'salary': 90000}

# class variables live on the class __dict__
print(Employee.__dict__.keys())  # ... 'company', 'headcount' ...

# vars() is a readable alias for __dict__
print(vars(alice))               # {'name': 'Alice', 'salary': 90000}
```

---

## Real-World Example — Bank with Interest Rate

```python
class BankAccount:
    interest_rate = 0.04        # 4% — shared by all accounts (class variable)

    def __init__(self, owner, balance=0):
        self.owner   = owner    # instance variable
        self.balance = balance  # instance variable

    def deposit(self, amount):
        self.balance += amount
        print(f"  {self.owner}: Deposited ₹{amount:,}. Balance: ₹{self.balance:,}")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"  {self.owner}: Interest ₹{interest:,.2f} added. Balance: ₹{self.balance:,.2f}")

    @classmethod
    def change_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"  Interest rate changed to {new_rate*100:.1f}% for all accounts")


a1 = BankAccount("Alice", 100000)
a2 = BankAccount("Bob",   200000)

a1.apply_interest()
a2.apply_interest()

print()
BankAccount.change_rate(0.06)       # change for ALL accounts
a1.apply_interest()
a2.apply_interest()
```

**Output:**
```
  Alice: Interest ₹4,000.00 added. Balance: ₹1,04,000.00
  Bob: Interest ₹8,000.00 added. Balance: ₹2,08,000.00

  Interest rate changed to 6.0% for all accounts
  Alice: Interest ₹6,240.00 added. Balance: ₹1,10,240.00
  Bob: Interest ₹12,480.00 added. Balance: ₹2,20,480.00
```

---

## Common Mistakes

```python
# ❌ Using a mutable class variable — shared mutation surprises everyone
class Team:
    members = []              # ONE list shared by all Team objects!

    def add(self, name):
        self.members.append(name)  # modifies the shared list

t1 = Team()
t2 = Team()
t1.add("Alice")
print(t2.members)   # ['Alice']  ← oops! t2 is contaminated

# ✅ Put mutable data in __init__ as an instance variable
class Team:
    def __init__(self):
        self.members = []     # each Team gets its own list

t1 = Team()
t2 = Team()
t1.add("Alice")
print(t2.members)   # []  ← correct, t2 is empty
```

> **Golden rule:** Never use a mutable type (list, dict, set) as a class variable unless you truly intend to share it.

---

## Key Takeaways

- **Instance variables** (`self.x`) are unique to each object — changing one doesn't affect others.
- **Class variables** (`ClassName.x`) are shared across all instances.
- Access class variables via `ClassName.x` (not `self.x`) to avoid shadowing surprises.
- Setting `self.x = value` when a class variable `x` exists creates a **new instance variable** that shadows the class one.
- Never use mutable class variables (list, dict) — use `self.x = []` in `__init__` instead.

---

*← [04 — `self` Keyword](04-self-keyword.md) · [→ 06 — Methods](06-methods.md)*
