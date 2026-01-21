# Python Basics – Built-in Functions & Immutability
It covers:
- Basic built-in Python functions
- Object identity using `id()`
- Mutable vs Immutable data types
- Why immutability exists in Python

---

## 1. Basic Built-in Python Functions

Python provides many useful built-in functions that are available without installing anything.

---

### 1.2 `input()` – Take User Input

Reads input from the user.  
**Important:** Input is always read as a string.

```python
name = input("Enter your name: ")
print(name)
```

```python
age = input("Enter your age: ")
print(type(age))   # <class 'str'>
```

---

### 1.3 `type()` – Check Data Type

Used to find the data type of a variable.

```python
x = 10
print(type(x))     # int
```

---

### 1.4 `id()` – Object Identity

Returns a unique identifier for an object in memory.

```python
x = 10
print(id(x))
```

Changing the value creates a new object:

```python
x = 10
print(id(x))

x = 20
print(id(x))
```

---

### 1.5 `len()` – Length of an Object

Returns the number of elements in an object.

```python
len("Python")      # 6
len([1, 2, 3])     # 3
```

---

### 1.6 Type Conversion Functions

Convert data from one type to another.

```python
int("25")
float("99.5")
str(100)
bool(1)
bool(0)
```

---

### 1.7 `help()` – Get Documentation

Displays help information about a function or object.

```python
help(print)
```

---

### 1.8 `dir()` – Explore Object Capabilities

Lists attributes and methods available for an object.

```python
dir(str)
```

---

## 2. Mutable vs Immutable Data Types

---

## 2.1 Immutable Data Types

Immutable objects **cannot be changed after creation**.

### Common Immutable Types
- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `frozenset`

### Example

```python
x = 10
print(id(x))

x = x + 1
print(id(x))
```

A new object is created instead of modifying the existing one.

---

### String Example

```python
s = "hello"
s[0] = "H"    # Error
```

Correct approach:

```python
s = "H" + s[1:]
```

---

## 2.2 Mutable Data Types

Mutable objects **can be changed in place**.

### Common Mutable Types
- `list`
- `dict`
- `set`
- `bytearray`

### Example

```python
numbers = [1, 2, 3]
print(id(numbers))

numbers.append(4)
print(id(numbers))
```

The memory address remains the same.

---

## 3. Key Differences Between Mutable and Immutable

| Feature | Immutable | Mutable |
|------|--------|--------|
| Can change value | No | Yes |
| Memory address | New object | Same object |
| Examples | int, str, tuple | list, dict, set |
| Hashable | Yes | No |

---

## 4. Why Are Some Data Types Immutable?

### 4.1 Memory Efficiency

Python can safely reuse immutable objects.

```python
a = 10
b = 10
```

Both may refer to the same object.

---

### 4.2 Dictionary and Set Safety

Dictionary keys must be immutable.

```python
data = {"name": "Alice"}   # Valid
```

Mutable keys could break dictionary lookups.

---

### 4.3 Thread Safety

Immutable objects:
- Are safe to share between threads
- Cannot be modified accidentally

---

### 4.4 Predictable Function Behavior

Mutable default arguments can cause unexpected behavior.

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Correct approach:

```python
def add_item(item, items=None):
    if items is None:
        items = []
```

---

## 5. Tuple with Mutable Objects

Tuples themselves are immutable, but they may contain mutable objects.

```python
t = ([1, 2], [3, 4])
t[0].append(99)
```

The tuple structure does not change, but the list inside it does.

---

## 6. Beginner Rule of Thumb

- Use **immutable** types for values, constants, and configuration
- Use **mutable** types for collections and data that changes

---

## 7. Summary

- `id()` shows object identity
- Immutable objects cannot be changed
- Mutable objects can be modified in place
- Immutability improves safety, performance, and predictability

---

