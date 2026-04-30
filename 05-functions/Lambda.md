# Lambda Functions in Python

## 1. What is a Lambda Function?

A **lambda function** is a **small, anonymous function** written in **one single line**.

It is used when you need a **simple function for a very short duration**, usually **only once**.

### Syntax
```python
lambda arguments: expression
```

### Example
```python
square = lambda x: x * x
print(square(5))  # 25
```

Equivalent regular function:
```python
def square(x):
    return x * x
```

---

## 2. Key Characteristics of Lambda Functions

| Feature | Lambda Function |
|------|------|
| Function name | ❌ No name |
| Lines of code | 1 |
| return keyword | ❌ Not used (implicit return) |
| Statements | ❌ Not allowed |
| Expressions | ✅ Allowed |
| Reusability | Low |
| Readability | Best for very small logic |

---

## 3. Why Do Lambda Functions Exist?

> Lambda functions exist **not because regular functions cannot do the job**,  
but because regular functions are **too heavy** for small, temporary logic.

Lambda functions are useful when:
- The logic is very small
- The function is used only once
- The function is passed as an argument
- You want to avoid creating unnecessary helper functions

---

## 4. Core Concept: Functions as Data

In Python, functions are **first-class citizens**:
- Functions can be passed as arguments
- Functions can be returned from other functions
- Functions can be stored in variables

Lambda functions allow you to **inject behavior inline**.

---

## 5. Real-World Example: Sorting Data

### Problem
Sort employees by salary.

```python
employees = [
    {"name": "A", "salary": 50000},
    {"name": "B", "salary": 80000},
    {"name": "C", "salary": 60000},
]
```

### Using Regular Function (Overkill)
```python
# Program 1: Sorting using a regular function

employees = [
    {"name": "A", "salary": 50000},
    {"name": "B", "salary": 80000},
    {"name": "C", "salary": 60000},
]

def get_salary(emp):
    # emp is one employee dictionary
    return emp["salary"]

print("Before sorting:")
for e in employees:
    print(e)

# Pass the function (do NOT call it)
employees.sort(key=get_salary)

print("\nAfter sorting by salary (using def):")
for e in employees:
    print(e)
```

### Using Lambda (Preferred)
```python
# Program 2: Sorting using lambda function

employees = [
    {"name": "A", "salary": 50000},
    {"name": "B", "salary": 80000},
    {"name": "C", "salary": 60000},
]

print("Before sorting:")
for e in employees:
    print(e)

# Lambda does the same job inline
employees.sort(key=lambda emp: emp["salary"])

print("\nAfter sorting by salary (using lambda):")
for e in employees:
    print(e)
```

---

## 6. Lambda with `map()` – Transformation

### Convert Celsius temperatures to Fahrenheit using normal function
```python
# Convert Celsius temperatures to Fahrenheit
# Using a normal function and a for loop

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


temps = [20, 25, 30]
fahrenheit = []

for c in temps:
    f = celsius_to_fahrenheit(c)
    fahrenheit.append(f)

print("Celsius:", temps)
print("Fahrenheit:", fahrenheit)
```

### Convert Celsius to Fahrenheit using just lambda
```python

celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32

temps = [20, 25, 30]
fahrenheit = []

for c in temps:
    f = celsius_to_fahrenheit(c)
    fahrenheit.append(f)

print("Celsius:", temps)
print("Fahrenheit:", fahrenheit)

```

### Convert Celsius to Fahrenheit using just lambda and map

```python
temps = [20, 25, 30]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps))
print(fahrenheit)
```
map() applies a function to every element in a collection and returns the transformed results.

---

## 7. Lambda with `filter()` – Selection

Filter even numbers from a list.

```python
nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

---

## 8. Lambda with `max()` and `min()`

Find the student with the highest marks.

```python
students = [
    ("A", 70),
    ("B", 85),
    ("C", 78),
]

topper = max(students, key=lambda s: s[1])
print(topper)
```

---

## 9. Lambda for Custom Sorting Logic

```python
numbers = [10, 3, 7, 1]

print(sorted(numbers, key=lambda x: x % 10))
print(sorted(numbers, key=lambda x: -x))
```

---

## 10. What Lambda Functions CANNOT Do

Lambda functions cannot:
- Contain multiple statements
- Use loops (`for`, `while`)
- Use `try/except`
- Assign variables
- Contain complex logic

---

## 11. When NOT to Use Lambda

❌ Business logic  
❌ Reusable logic  
❌ Multi-step processing  

---

## 12. Lambda vs Regular Function

| Aspect | def | lambda |
|----|----|----|
| Has name | Yes | No |
| Lines of code | Multiple | One |
| Reusable | Yes | No |
| Best use case | Business logic | Inline logic |

---

## 13. Rule, when to use proper function and when to use Lambdas

> **Reuse → def**  
> **One-time small logic → lambda**

---

## 14. Practice Exercises

1. Square numbers using lambda  
2. Filter values greater than 10  
3. Sort tuples by second element  
4. Find max using lambda  


# Lambda Exercises (With Answers)

## Exercise 1
Square all numbers
```python
nums = [1,2,3,4]
```

### Answer
```python
list(map(lambda x: x*x, nums))
```

---

## Exercise 2
Filter numbers > 10
```python
nums = [5, 12, 3, 20]
```

### Answer
```python
list(filter(lambda x: x > 10, nums))
```

---

## Exercise 3
Sort tuples by second value
```python
data = [(1,3), (4,1), (2,2)]
```

### Answer
```python
sorted(data, key=lambda x: x[1])
```

---

## Exercise 4
Find max salary
```python
emps = [("A",50000), ("B",80000)]
```

### Answer
```python
max(emps, key=lambda x: x[1])
```


---

## 15. One-Line Summary

> **Lambda functions are small, anonymous, one-line functions used for temporary inline logic.**
