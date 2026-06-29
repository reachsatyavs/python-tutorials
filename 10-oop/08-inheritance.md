# 08 — Inheritance

---

## Why do you need inheritance?

Without inheritance, sharing behaviour between related classes means copy-pasting code:

```python
# ❌ Copy-paste — every animal has eat() and sleep()
class Dog:
    def __init__(self, name): self.name = name
    def eat(self):   print(f"{self.name} is eating")
    def sleep(self): print(f"{self.name} is sleeping")
    def speak(self): print(f"{self.name} says: Woof!")

class Cat:
    def __init__(self, name): self.name = name
    def eat(self):   print(f"{self.name} is eating")    # duplicate!
    def sleep(self): print(f"{self.name} is sleeping")  # duplicate!
    def speak(self): print(f"{self.name} says: Meow!")
```

Now imagine fixing a bug in `eat()` — you have to fix it in every class. Inheritance solves this: put shared code in a parent class, and child classes get it for free.

---

## Where is inheritance used?

| Example | Inheritance chain |
|---|---|
| Django ORM | `models.Model → YourModel` |
| Python exceptions | `BaseException → Exception → ValueError` |
| Test framework | `unittest.TestCase → YourTestClass` |
| Pydantic | `BaseModel → YourSchema` |
| FastAPI | `APIRouter → ...` |

---

## When should you use inheritance?

Use inheritance when there is a clear **IS-A** relationship:

- A `Dog` IS-A `Animal` ✅
- A `Manager` IS-A `Employee` ✅
- A `Car` IS-A `Vehicle` ✅
- A `ShoppingCart` IS-A `User` ❌ (wrong — use composition instead)

> **Prefer composition over inheritance** when the relationship is HAS-A:
> "A `Car` HAS-A `Engine`" — use `self.engine = Engine()`, not `class Car(Engine)`.

---

## The Concept

```python
class Animal:               # Parent class (also called Base class, Superclass)
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):          # Child class inherits from Animal
    def speak(self):        # new method — only Dog has this
        print(f"{self.name} says: Woof!")


class Cat(Animal):          # Another child class
    def speak(self):
        print(f"{self.name} says: Meow!")
```

`Dog` and `Cat` get `eat()` and `sleep()` for free from `Animal`. They only define what is different about them.

---

## Basic Example

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):
        print(f"  {self.name} is eating")

    def sleep(self):
        print(f"  {self.name} is sleeping")

    def info(self):
        print(f"  {self.name}, {self.age} years old ({type(self).__name__})")


class Dog(Animal):
    def speak(self):
        print(f"  {self.name} says: Woof!")

    def fetch(self):
        print(f"  {self.name} fetches the ball!")


class Cat(Animal):
    def speak(self):
        print(f"  {self.name} says: Meow!")

    def purr(self):
        print(f"  {self.name} purrs...")


rex    = Dog("Rex",     3)
whisky = Cat("Whiskers", 5)

rex.info()       # Rex, 3 years old (Dog)
rex.eat()        # Rex is eating         ← from Animal
rex.speak()      # Rex says: Woof!       ← from Dog
rex.fetch()      # Rex fetches the ball! ← from Dog

whisky.info()    # Whiskers, 5 years old (Cat)
whisky.sleep()   # Whiskers is sleeping  ← from Animal
whisky.speak()   # Whiskers says: Meow! ← from Cat
whisky.purr()    # Whiskers purrs...     ← from Cat
```

**Output:**
```
  Rex, 3 years old (Dog)
  Rex is eating
  Rex says: Woof!
  Rex fetches the ball!
  Whiskers, 5 years old (Cat)
  Whiskers is sleeping
  Whiskers says: Meow!
  Whiskers purrs...
```

---

## `super()` — Calling the Parent

When the child class has its own `__init__`, use `super()` to call the parent's `__init__` first so the parent's attributes are set up properly:

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call Animal.__init__ first
        self.breed = breed            # then add Dog-specific attribute

    def info(self):
        print(f"  {self.name} ({self.breed}), {self.age} yrs")


rex = Dog("Rex", 3, "Labrador")
rex.info()    # Rex (Labrador), 3 yrs
```

> **Rule:** Always call `super().__init__(...)` in a child's `__init__` to ensure the parent is set up correctly.

---

## Method Overriding

A child class can **override** (replace) a parent method with its own version:

```python
class Shape:
    def area(self):
        return 0

    def describe(self):
        print(f"  I am a {type(self).__name__} with area {self.area():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                     # overrides Shape.area()
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):                     # overrides Shape.area()
        return self.w * self.h


c = Circle(5)
r = Rectangle(4, 6)

c.describe()   # I am a Circle with area 78.54
r.describe()   # I am a Rectangle with area 24.00
```

---

## Multi-level Inheritance

```python
class Animal:
    def breathe(self): print(f"  {self.name} breathes")

class Mammal(Animal):
    def warm_blooded(self): print(f"  {self.name} is warm-blooded")

class Dog(Mammal):
    def __init__(self, name):
        self.name = name

    def speak(self): print(f"  {self.name} says: Woof!")


d = Dog("Rex")
d.breathe()         # from Animal
d.warm_blooded()    # from Mammal
d.speak()           # from Dog

# all three work — Dog inherits the whole chain
print(isinstance(d, Dog))     # True
print(isinstance(d, Mammal))  # True
print(isinstance(d, Animal))  # True
```

---

## Real-World Example — Employee Hierarchy

```python
class Employee:
    company = "TechCorp"

    def __init__(self, name, emp_id, base_salary):
        self.name        = name
        self.emp_id      = emp_id
        self.base_salary = base_salary

    def salary(self):
        return self.base_salary

    def info(self):
        print(f"  [{self.emp_id}] {self.name:<12} | {type(self).__name__:<10} "
              f"| Salary: ₹{self.salary():>8,.0f}")


class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, team_size):
        super().__init__(name, emp_id, base_salary)
        self.team_size = team_size

    def salary(self):                                   # override
        return self.base_salary + (self.team_size * 5000)  # bonus per team member


class Engineer(Employee):
    def __init__(self, name, emp_id, base_salary, tech_stack):
        super().__init__(name, emp_id, base_salary)
        self.tech_stack = tech_stack

    def salary(self):                                   # override
        bonus = 10000 if "python" in self.tech_stack else 0
        return self.base_salary + bonus


class Intern(Employee):
    def salary(self):                                   # override
        return self.base_salary * 0.5                  # 50% of base


employees = [
    Manager("Alice",   "M001", 120000, team_size=8),
    Manager("Bob",     "M002",  95000, team_size=4),
    Engineer("Carol",  "E001",  80000, ["python", "fastapi"]),
    Engineer("Dave",   "E002",  80000, ["java", "spring"]),
    Intern("Eve",      "I001",  40000),
]

for emp in employees:
    emp.info()

total = sum(emp.salary() for emp in employees)
print(f"\n  Total payroll: ₹{total:,.0f}")

# type checking
managers   = [e for e in employees if isinstance(e, Manager)]
engineers  = [e for e in employees if isinstance(e, Engineer)]
print(f"\n  Managers: {[m.name for m in managers]}")
print(f"  Engineers: {[e.name for e in engineers]}")
```

**Output:**
```
  [M001] Alice        | Manager    | Salary: ₹1,60,000
  [M002] Bob          | Manager    | Salary: ₹1,15,000
  [E001] Carol        | Engineer   | Salary: ₹  90,000
  [E002] Dave         | Engineer   | Salary: ₹  80,000
  [I001] Eve          | Intern     | Salary: ₹  20,000

  Total payroll: ₹4,65,000

  Managers: ['Alice', 'Bob']
  Engineers: ['Carol', 'Dave']
```

---

## `isinstance()` and `issubclass()`

```python
print(isinstance(d, Dog))            # True — d is a Dog
print(isinstance(d, Animal))         # True — Dog inherits from Animal
print(isinstance(d, str))            # False

print(issubclass(Dog, Animal))       # True
print(issubclass(Manager, Employee)) # True
print(issubclass(int, str))          # False
```

---

## Common Mistakes

```python
# ❌ Forgetting super().__init__() — parent attributes never set
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # forgot super().__init__(name)
        self.breed = breed

d = Dog("Rex", "Lab")
print(d.breed)   # Lab
print(d.name)    # AttributeError — never set!

# ✅
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # parent sets self.name
        self.breed = breed
```

---

## Key Takeaways

- Inheritance lets a child class **reuse** all code from the parent class.
- Use `class Child(Parent):` syntax.
- Use `super().__init__(...)` to call the parent constructor.
- **Method overriding** = child defines a method with the same name as the parent's.
- `isinstance(obj, Class)` checks the inheritance chain, not just the exact type.
- Prefer **composition** over inheritance when the relationship is HAS-A, not IS-A.

---

*← [07 — Encapsulation](07-encapsulation.md) · [→ 09 — Polymorphism](09-polymorphism.md)*
