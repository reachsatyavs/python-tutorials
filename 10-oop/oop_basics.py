"""
OOP Basics — 10 Runnable Examples
Module 10 · python-tutorials

Covers: class, object, __init__, self, class vs instance variables, methods
Run:  python3 oop_basics.py
"""

SEP = "─" * 60

def section(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)


# ──────────────────────────────────────────────────────────
# Example 01 — Simplest class: Dog with __init__ and a method
# ──────────────────────────────────────────────────────────
section("01 — Simplest class: __init__ and a method")

class Dog:
    def __init__(self, name, breed):
        self.name  = name
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof!"

    def info(self):
        return f"{self.name} is a {self.breed}"


rex   = Dog("Rex",   "Labrador")
buddy = Dog("Buddy", "Poodle")

print(rex.speak())
print(buddy.speak())
print(rex.info())
print(buddy.info())


# ──────────────────────────────────────────────────────────
# Example 02 — Multiple instances, each with its own data
# ──────────────────────────────────────────────────────────
section("02 — Multiple instances: same blueprint, different data")

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90: return "A"
        if self.marks >= 75: return "B"
        if self.marks >= 60: return "C"
        return "F"

    def report(self):
        print(f"  {self.name:<10} | Marks: {self.marks} | Grade: {self.grade()}")


students = [
    Student("Alice",  92),
    Student("Bob",    74),
    Student("Carol",  85),
    Student("Dave",   55),
    Student("Eve",    60),
]

for s in students:
    s.report()

toppers = [s for s in students if s.grade() == "A"]
print(f"\n  Toppers: {[s.name for s in toppers]}")


# ──────────────────────────────────────────────────────────
# Example 03 — self in action: two objects, same method
# ──────────────────────────────────────────────────────────
section("03 — self in action: each object has its own data")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"  {self.owner}: Insufficient funds")

    def show(self):
        print(f"  {self.owner:<10} | Balance: ₹{self.balance:,}")


alice = BankAccount("Alice", 50000)
bob   = BankAccount("Bob",   30000)

alice.deposit(10000)
bob.deposit(5000)
alice.withdraw(5000)
bob.withdraw(50000)   # insufficient

alice.show()
bob.show()

# Proof that self separates them
print(f"\n  alice.balance = {alice.balance}")
print(f"  bob.balance   = {bob.balance}")


# ──────────────────────────────────────────────────────────
# Example 04 — Class variable vs instance variable
# ──────────────────────────────────────────────────────────
section("04 — Class variable vs instance variable")

class Employee:
    company   = "TechCorp"    # class variable — shared
    headcount = 0             # class variable — counts all employees

    def __init__(self, name, salary):
        self.name   = name    # instance variable — per object
        self.salary = salary
        Employee.headcount += 1

    def info(self):
        print(f"  {self.name:<10} | {Employee.company} | ₹{self.salary:,}")


e1 = Employee("Alice",  90000)
e2 = Employee("Bob",    75000)
e3 = Employee("Carol",  95000)

e1.info()
e2.info()
e3.info()
print(f"\n  Total employees: {Employee.headcount}")

# change class variable — affects all
Employee.company = "Globex Corp"
print(f"\n  After rebrand:")
e1.info()
e2.info()


# ──────────────────────────────────────────────────────────
# Example 05 — Mutable class variable trap
# ──────────────────────────────────────────────────────────
section("05 — Mutable class variable trap & correct solution")

# ❌ BAD — shared list
class TeamBad:
    members = []              # ONE list for all TeamBad objects

    def add(self, name):
        self.members.append(name)

t1 = TeamBad(); t2 = TeamBad()
t1.add("Alice")
print(f"  t1.members = {t1.members}")
print(f"  t2.members = {t2.members}  ← oops! contaminated by t1")

# ✅ GOOD — instance list
class TeamGood:
    def __init__(self):
        self.members = []     # each team has its own list

    def add(self, name):
        self.members.append(name)

g1 = TeamGood(); g2 = TeamGood()
g1.add("Alice")
g1.add("Bob")
g2.add("Carol")
print(f"\n  g1.members = {g1.members}")
print(f"  g2.members = {g2.members}  ← correct, separate lists")


# ──────────────────────────────────────────────────────────
# Example 06 — Instance / Class / Static methods side by side
# ──────────────────────────────────────────────────────────
section("06 — Instance, @classmethod, @staticmethod side by side")

class Temperature:
    unit = "Celsius"

    def __init__(self, degrees):
        self.degrees = degrees

    # instance method — works with THIS object
    def to_fahrenheit(self):
        return (self.degrees * 9/5) + 32

    def describe(self):
        return f"{self.degrees}°C = {self.to_fahrenheit():.1f}°F"

    # class method — alternative constructor
    @classmethod
    def from_fahrenheit(cls, f):
        return cls(round((f - 32) * 5/9, 2))

    # static method — utility, no object or class needed
    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0


boiling = Temperature(100)
body    = Temperature(37)
print(f"  {boiling.describe()}")
print(f"  {body.describe()}")

body_from_f = Temperature.from_fahrenheit(98.6)
print(f"  98.6°F → {body_from_f.degrees}°C")

print(f"  Is 0°C freezing?  {Temperature.is_freezing(0)}")
print(f"  Is 20°C freezing? {Temperature.is_freezing(20)}")


# ──────────────────────────────────────────────────────────
# Example 07 — __str__ and __repr__ — string representation
# ──────────────────────────────────────────────────────────
section("07 — __str__ and __repr__: customise print(obj)")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):               # print(obj) uses this
        return f"Point({self.x}, {self.y})"

    def __repr__(self):              # repr(obj) and REPL uses this
        return f"Point(x={self.x}, y={self.y})"

    def __add__(self, other):        # makes + work for Points
        return Point(self.x + other.x, self.y + other.y)

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5


p1 = Point(3, 4)
p2 = Point(1, 2)

print(f"  str:  {p1}")           # Point(3, 4)
print(f"  repr: {repr(p1)}")     # Point(x=3, y=4)
print(f"  p1 + p2 = {p1 + p2}") # Point(4, 6)
print(f"  distance from origin: {p1.distance():.2f}")


# ──────────────────────────────────────────────────────────
# Example 08 — Real-world class: Product
# ──────────────────────────────────────────────────────────
section("08 — Real-world class: Product inventory")

class Product:
    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def sell(self, qty=1):
        if qty > self.stock:
            print(f"  Not enough stock for '{self.name}'. Have {self.stock}")
            return False
        self.stock -= qty
        print(f"  Sold {qty}x '{self.name}'. Stock left: {self.stock}")
        return True

    def restock(self, qty):
        self.stock += qty
        print(f"  Restocked '{self.name}' +{qty}. Total: {self.stock}")

    def __str__(self):
        status = "✓" if self.stock > 0 else "✗"
        return f"  {status} {self.name:<20} ₹{self.price:>8,.2f}  ({self.stock} in stock)"


inventory = [
    Product("Laptop",         75000, 5),
    Product("Wireless Mouse",   999, 10),
    Product("USB-C Hub",       2499,  3),
]

print("  --- Inventory ---")
for p in inventory:
    print(p)

print()
inventory[0].sell(2)
inventory[1].sell(15)   # not enough
inventory[2].restock(7)

print("\n  --- Updated Inventory ---")
for p in inventory:
    print(p)


# ──────────────────────────────────────────────────────────
# Example 09 — Real-world class: Student with statistics
# ──────────────────────────────────────────────────────────
section("09 — Real-world class: Student with mark statistics")

class Student:
    def __init__(self, name, subject_marks: dict):
        self.name           = name
        self.subject_marks  = subject_marks

    def total(self):
        return sum(self.subject_marks.values())

    def average(self):
        return self.total() / len(self.subject_marks)

    def best_subject(self):
        return max(self.subject_marks, key=self.subject_marks.get)

    def worst_subject(self):
        return min(self.subject_marks, key=self.subject_marks.get)

    def grade(self):
        avg = self.average()
        if avg >= 90: return "A"
        if avg >= 75: return "B"
        if avg >= 60: return "C"
        return "F"

    def report(self):
        print(f"\n  {self.name}")
        for subj, marks in self.subject_marks.items():
            print(f"    {subj:<12}: {marks}")
        print(f"    {'─'*22}")
        print(f"    Total  : {self.total()}")
        print(f"    Average: {self.average():.1f}  → Grade {self.grade()}")
        print(f"    Best   : {self.best_subject()} ({self.subject_marks[self.best_subject()]})")
        print(f"    Worst  : {self.worst_subject()} ({self.subject_marks[self.worst_subject()]})")


s1 = Student("Alice", {"Math": 95, "Science": 88, "English": 92, "History": 78})
s2 = Student("Bob",   {"Math": 60, "Science": 55, "English": 70, "History": 65})

s1.report()
s2.report()


# ──────────────────────────────────────────────────────────
# Example 10 — isinstance() and type() checks
# ──────────────────────────────────────────────────────────
section("10 — isinstance() and type() — type inspection")

class Animal:
    def __init__(self, name): self.name = name

class Dog(Animal):
    def speak(self): return "Woof!"

class Cat(Animal):
    def speak(self): return "Meow!"


rex     = Dog("Rex")
whisky  = Cat("Whiskers")
number  = 42

print(f"  type(rex)   = {type(rex)}")
print(f"  type(rex) == Dog?    {type(rex) == Dog}")
print(f"  type(rex) == Animal? {type(rex) == Animal}")  # False! exact match only

print()
print(f"  isinstance(rex, Dog)?    {isinstance(rex, Dog)}")
print(f"  isinstance(rex, Animal)? {isinstance(rex, Animal)}")  # True — checks chain
print(f"  isinstance(rex, Cat)?    {isinstance(rex, Cat)}")

print()
# practical use — filter by type
zoo = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy"), Cat("Luna"), Dog("Max")]
dogs = [a for a in zoo if isinstance(a, Dog)]
cats = [a for a in zoo if isinstance(a, Cat)]
print(f"  Dogs: {[d.name for d in dogs]}")
print(f"  Cats: {[c.name for c in cats]}")


print(f"\n{SEP}")
print("  All 10 OOP basics examples complete.")
print(SEP)
