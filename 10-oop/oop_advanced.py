"""
OOP Advanced — 10 Runnable Examples
Module 10 · python-tutorials

Covers: Encapsulation, Inheritance, Polymorphism, Abstraction
Run:  python3 oop_advanced.py
"""

from abc import ABC, abstractmethod

SEP = "─" * 60

def section(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)


# ──────────────────────────────────────────────────────────
# Example 01 — Encapsulation: @property + validation
# ──────────────────────────────────────────────────────────
section("01 — Encapsulation: @property with getter and setter")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age        # calls the setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError(f"Invalid age: {value}")
        self._age = value

    @property
    def is_adult(self):       # read-only computed property
        return self._age >= 18

    def __str__(self):
        status = "adult" if self.is_adult else "minor"
        return f"  {self.name}, age {self._age} ({status})"


alice = Person("Alice", 28)
kid   = Person("Tim",   12)

print(alice)
print(kid)

alice.age = 29
print(f"  Updated: {alice}")

try:
    alice.age = -5
except ValueError as e:
    print(f"  Error: {e}")


# ──────────────────────────────────────────────────────────
# Example 02 — Encapsulation: BankAccount with private balance
# ──────────────────────────────────────────────────────────
section("02 — Encapsulation: BankAccount with private attributes")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner   = owner
        self.__balance = balance

    @property
    def owner(self):   return self.__owner

    @property
    def balance(self): return self.__balance

    def deposit(self, amount):
        if amount <= 0: raise ValueError("Amount must be positive")
        self.__balance += amount
        print(f"  Deposited ₹{amount:,}  →  Balance: ₹{self.__balance:,}")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError(f"Insufficient funds (have ₹{self.__balance:,})")
        self.__balance -= amount
        print(f"  Withdrew  ₹{amount:,}  →  Balance: ₹{self.__balance:,}")

    def __str__(self):
        return f"  Account[{self.__owner}]: ₹{self.__balance:,}"


acc = BankAccount("Alice", 10000)
acc.deposit(5000)
acc.withdraw(3000)
print(acc)

try:
    acc.balance = 999999    # AttributeError — read-only property
except AttributeError as e:
    print(f"  Cannot set balance directly: {type(e).__name__}")

try:
    acc.withdraw(100000)
except ValueError as e:
    print(f"  Error: {e}")


# ──────────────────────────────────────────────────────────
# Example 03 — Inheritance: Animal → Dog, Cat, Bird
# ──────────────────────────────────────────────────────────
section("03 — Inheritance: Animal parent → Dog, Cat, Bird children")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):
        print(f"  {self.name} is eating")

    def sleep(self):
        print(f"  {self.name} is sleeping")

    def info(self):
        print(f"  {type(self).__name__}: {self.name}, {self.age} yrs")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self): print(f"  {self.name}: Woof!")
    def fetch(self): print(f"  {self.name} fetches the ball!")


class Cat(Animal):
    def speak(self): print(f"  {self.name}: Meow!")
    def purr(self):  print(f"  {self.name} purrs...")


class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def speak(self): print(f"  {self.name}: Tweet!")
    def fly(self):
        if self.can_fly:
            print(f"  {self.name} is flying!")
        else:
            print(f"  {self.name} cannot fly")


animals = [Dog("Rex", 3, "Labrador"), Cat("Whiskers", 5), Bird("Tweety", 2)]

for a in animals:
    a.info()
    a.speak()
    a.eat()

animals[0].fetch()    # Dog-specific
animals[1].purr()     # Cat-specific
animals[2].fly()      # Bird-specific


# ──────────────────────────────────────────────────────────
# Example 04 — Inheritance: super() and method overriding
# ──────────────────────────────────────────────────────────
section("04 — super() and method overriding")

class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

    def fuel_cost(self, km):
        return 0   # base — children override

    def trip_cost(self, km):
        cost = self.fuel_cost(km)
        print(f"  {self.description()} | {km} km trip | Cost: ₹{cost:,.0f}")


class PetrolCar(Vehicle):
    def __init__(self, make, model, year, mileage_kmpl):
        super().__init__(make, model, year)
        self.mileage = mileage_kmpl     # km per litre

    def fuel_cost(self, km):
        litres = km / self.mileage
        return litres * 100             # ₹100 per litre


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, efficiency_km_per_kwh):
        super().__init__(make, model, year)
        self.efficiency = efficiency_km_per_kwh

    def fuel_cost(self, km):
        kwh = km / self.efficiency
        return kwh * 8                  # ₹8 per kWh


cars = [
    PetrolCar("Honda", "City",       2021, mileage_kmpl=17),
    PetrolCar("Toyota", "Innova",    2020, mileage_kmpl=12),
    ElectricCar("Tesla", "Model 3",  2023, efficiency_km_per_kwh=6),
    ElectricCar("Tata",  "Nexon EV", 2022, efficiency_km_per_kwh=5),
]

for car in cars:
    car.trip_cost(300)


# ──────────────────────────────────────────────────────────
# Example 05 — Polymorphism: shapes with area and perimeter
# ──────────────────────────────────────────────────────────
section("05 — Polymorphism: shapes — same method, different result")

class Shape:
    def area(self):      return 0
    def perimeter(self): return 0
    def describe(self):
        print(f"  {type(self).__name__:<12} "
              f"area={self.area():>8.2f}  perimeter={self.perimeter():>8.2f}")


class Circle(Shape):
    def __init__(self, r):       self.r = r
    def area(self):              return 3.14159 * self.r ** 2
    def perimeter(self):         return 2 * 3.14159 * self.r

class Rectangle(Shape):
    def __init__(self, w, h):    self.w, self.h = w, h
    def area(self):              return self.w * self.h
    def perimeter(self):         return 2 * (self.w + self.h)

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
    def perimeter(self):         return self.a + self.b + self.c


shapes = [Circle(7), Rectangle(4, 9), Triangle(3, 4, 5), Circle(3), Rectangle(10, 2)]

for s in shapes:
    s.describe()

total_area = sum(s.area() for s in shapes)
largest    = max(shapes, key=lambda s: s.area())
print(f"\n  Total area : {total_area:.2f}")
print(f"  Largest    : {type(largest).__name__} (area={largest.area():.2f})")


# ──────────────────────────────────────────────────────────
# Example 06 — Polymorphism: duck typing
# ──────────────────────────────────────────────────────────
section("06 — Polymorphism: duck typing (no inheritance needed)")

class Dog:
    def speak(self): return "Woof!"
    def __str__(self): return "Dog"

class Cat:
    def speak(self): return "Meow!"
    def __str__(self): return "Cat"

class Robot:                          # completely unrelated class
    def speak(self): return "Beep boop!"
    def __str__(self): return "Robot"

class Person:
    def __init__(self, name): self.name = name
    def speak(self): return f"Hi, I'm {self.name}!"
    def __str__(self): return f"Person({self.name})"


def introduce(thing):
    print(f"  {thing}: {thing.speak()}")   # works for ANY object with speak()

things = [Dog(), Cat(), Robot(), Person("Alice")]
for t in things:
    introduce(t)


# ──────────────────────────────────────────────────────────
# Example 07 — Polymorphism: Payment system
# ──────────────────────────────────────────────────────────
section("07 — Polymorphism: payment system (real-world)")

class Payment:
    def __init__(self, amount): self.amount = amount

    def pay(self): raise NotImplementedError


class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self):
        print(f"  [UPI]  ₹{self.amount:,} → {self.upi_id}")
        return True


class CardPayment(Payment):
    def __init__(self, amount, last4):
        super().__init__(amount)
        self.last4 = last4

    def pay(self):
        print(f"  [Card] ₹{self.amount:,} → card *{self.last4}")
        return True


class CashPayment(Payment):
    def __init__(self, amount, tendered):
        super().__init__(amount)
        self.tendered = tendered

    def pay(self):
        change = self.tendered - self.amount
        if change < 0:
            print(f"  [Cash] Insufficient. Need ₹{self.amount:,}, got ₹{self.tendered:,}")
            return False
        print(f"  [Cash] ₹{self.amount:,} paid. Change: ₹{change:,}")
        return True


def checkout(payment):
    success = payment.pay()
    status  = "✓ Success" if success else "✗ Failed"
    print(f"  {status}\n")


checkout(UPIPayment(1500, "alice@upi"))
checkout(CardPayment(3200, "4242"))
checkout(CashPayment(500,  600))
checkout(CashPayment(750,  400))   # insufficient


# ──────────────────────────────────────────────────────────
# Example 08 — Abstraction: ABC + @abstractmethod
# ──────────────────────────────────────────────────────────
section("08 — Abstraction: ABC enforces a contract")

class Notifier(ABC):
    def __init__(self, recipient):
        self.recipient = recipient

    @abstractmethod
    def send(self, message): ...

    # concrete — shared by all
    def broadcast(self, messages):
        for msg in messages:
            self.send(msg)


class EmailNotifier(Notifier):
    def send(self, message):
        print(f"  [Email→{self.recipient}] {message}")


class SMSNotifier(Notifier):
    def send(self, message):
        print(f"  [SMS→{self.recipient}] {message}")


class SlackNotifier(Notifier):
    def send(self, message):
        print(f"  [Slack→#{self.recipient}] {message}")


notifiers = [
    EmailNotifier("alice@company.com"),
    SMSNotifier("+91-98765-43210"),
    SlackNotifier("engineering"),
]

alert = "🚨 Deployment failed on production"
for n in notifiers:
    n.send(alert)

print()
updates = ["Sprint 12 started", "PR #42 merged", "Tests passing ✓"]
SlackNotifier("general").broadcast(updates)

# Cannot instantiate abstract class
try:
    n = Notifier("x")
except TypeError as e:
    print(f"\n  Cannot create Notifier directly: {type(e).__name__}")


# ──────────────────────────────────────────────────────────
# Example 09 — Abstraction: Storage backends
# ──────────────────────────────────────────────────────────
section("09 — Abstraction: pluggable storage backends")

class StorageBackend(ABC):
    @abstractmethod
    def save(self, key, data): ...

    @abstractmethod
    def load(self, key): ...

    @abstractmethod
    def delete(self, key): ...

    @abstractmethod
    def exists(self, key): ...

    def save_if_new(self, key, data):      # concrete — all backends get this
        if not self.exists(key):
            self.save(key, data)
        else:
            print(f"  '{key}' already exists — skip")


class MemoryStorage(StorageBackend):
    def __init__(self): self._data = {}
    def save(self, k, v):   self._data[k] = v;          print(f"  [Mem] saved '{k}'")
    def load(self, k):      return self._data.get(k)
    def delete(self, k):    self._data.pop(k, None);     print(f"  [Mem] deleted '{k}'")
    def exists(self, k):    return k in self._data


class FileStorage(StorageBackend):
    def __init__(self): self._files = {}
    def save(self, k, v):   self._files[k] = v;         print(f"  [File] wrote '{k}'")
    def load(self, k):      return self._files.get(k)
    def delete(self, k):    self._files.pop(k, None);    print(f"  [File] removed '{k}'")
    def exists(self, k):    return k in self._files


def run_pipeline(storage: StorageBackend):
    storage.save("user_001", {"name": "Alice", "score": 95})
    storage.save("user_002", {"name": "Bob",   "score": 78})
    storage.save_if_new("user_001", {"name": "duplicate"})  # skip
    print(f"  Loaded: {storage.load('user_002')}")
    storage.delete("user_001")
    print(f"  user_001 exists? {storage.exists('user_001')}")

print("  --- Memory Storage ---")
run_pipeline(MemoryStorage())

print("\n  --- File Storage ---")
run_pipeline(FileStorage())


# ──────────────────────────────────────────────────────────
# Example 10 — Putting it all together: all 4 pillars in one
# ──────────────────────────────────────────────────────────
section("10 — All 4 pillars: Employee payroll system")

class Employee(ABC):
    company = "TechCorp"

    def __init__(self, name, emp_id):
        self.name   = name
        self.emp_id = emp_id
        self.__performance = 100   # private — encapsulation

    @property
    def performance(self):
        return self.__performance

    @performance.setter
    def performance(self, score):
        if not 0 <= score <= 100:
            raise ValueError("Performance score must be 0–100")
        self.__performance = score

    @abstractmethod
    def salary(self): ...         # abstraction — subclasses must implement

    def bonus(self):
        return self.salary() * (self.performance / 100) * 0.10

    def payslip(self):
        print(f"  [{self.emp_id}] {self.name:<12} | "
              f"{type(self).__name__:<10} | "
              f"Salary: ₹{self.salary():>8,.0f} | "
              f"Bonus: ₹{self.bonus():>6,.0f} | "
              f"Perf: {self.performance}%")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly):
        super().__init__(name, emp_id)
        self.__monthly = monthly

    def salary(self):               # polymorphism — each type calculates differently
        return self.__monthly


class ContractEmployee(Employee):
    def __init__(self, name, emp_id, daily_rate, days_worked):
        super().__init__(name, emp_id)
        self.__rate  = daily_rate
        self.__days  = days_worked

    def salary(self):
        return self.__rate * self.__days


class InternEmployee(Employee):
    def __init__(self, name, emp_id, stipend):
        super().__init__(name, emp_id)
        self.__stipend = stipend

    def salary(self):
        return self.__stipend

    def bonus(self):                # override bonus — interns get a flat ₹500
        return 500


employees = [
    FullTimeEmployee("Alice",   "FT001", 120000),
    FullTimeEmployee("Bob",     "FT002",  90000),
    ContractEmployee("Carol",   "CT001",  3000, 22),
    ContractEmployee("Dave",    "CT002",  4000, 18),
    InternEmployee("Eve",       "IN001",  20000),
]

employees[0].performance = 95
employees[1].performance = 72
employees[2].performance = 88

print(f"  {'─'*75}")
for emp in employees:
    emp.payslip()
print(f"  {'─'*75}")

total_payroll = sum(emp.salary() + emp.bonus() for emp in employees)
print(f"  Total payroll (salary + bonus): ₹{total_payroll:,.0f}")

# inheritance check
full_time   = [e for e in employees if isinstance(e, FullTimeEmployee)]
contractors = [e for e in employees if isinstance(e, ContractEmployee)]
print(f"\n  Full-time  : {[e.name for e in full_time]}")
print(f"  Contractors: {[e.name for e in contractors]}")


print(f"\n{SEP}")
print("  All 10 OOP advanced examples complete.")
print(SEP)
