# Python Data Types – Categories & Overview

This README explains **Python data types** by grouping them into **categories such as immutable and mutable**.
---

## 1. Categories of Python Data Types

Python standard data types can be broadly classified into the following categories:

---

### 1.1 Immutable Data Types

**Immutable data types cannot be changed after they are created.**  
If you try to modify them, Python creates a **new object** instead.

#### Common Immutable Types
- Numbers (`int`, `float`, `complex`)
- Strings (`str`)
- Tuples (`tuple`)
- Frozen Sets (`frozenset`)
- Boolean (`bool`)
- Bytes (`bytes`)
- `NoneType`

#### Example
```python
x = 10
print(id(x))

x = x + 1
print(id(x))  # New object created
```

**Why immutability matters:**
- Memory efficiency
- Safe to use as dictionary keys
- Thread-safe
- Predictable behavior

---

### 1.2 Mutable Data Types

**Mutable data types can be changed in place** without creating a new object.

#### Common Mutable Types
- Lists (`list`)
- Dictionaries (`dict`)
- Sets (`set`)
- Byte Arrays (`bytearray`)
- Memory Views (`memoryview`)
- Custom objects (default behavior)

#### Example
```python
numbers = [1, 2, 3]
print(id(numbers))

numbers.append(4)
print(id(numbers))  # Same object
```

**Why mutability matters:**
- Efficient updates
- Useful for collections
- Suitable for dynamic data

---

### 1.3 Sequence Data Types

Used to store **ordered collections** of items.

| Type | Mutable | Example |
|----|--------|--------|
| `str` | ❌ | `"hello"` |
| `list` | ✅ | `[1, 2, 3]` |
| `tuple` | ❌ | `(1, 2, 3)` |
| `bytes` | ❌ | `b"abc"` |
| `bytearray` | ✅ | `bytearray(b"abc")` |

---

### 1.4 Mapping Data Types

Used to store **key–value pairs**.

| Type | Mutable | Example |
|----|--------|--------|
| `dict` | ✅ | `{"a": 1, "b": 2}` |

Keys **must be immutable**.

---

### 1.5 Set Data Types

Used to store **unordered, unique elements**.

| Type | Mutable | Example |
|----|--------|--------|
| `set` | ✅ | `{1, 2, 3}` |
| `frozenset` | ❌ | `frozenset([1, 2, 3])` |

---

## 2. Python Data Types (Detailed Table)

In Python, data types define the nature and behavior of data.

| Type         | Description                                | Example                             | Common Usage                                  |
|--------------|--------------------------------------------|-------------------------------------|----------------------------------------------|
| `int`        | Integer numbers                            | `x = 42`                            | Counting, indexing, math operations          |
| `float`      | Floating-point numbers                     | `y = 3.14`                          | Scientific calculations                     |
| `complex`    | Complex numbers                            | `z = 1 + 2j`                        | Engineering, signal processing               |
| `str`        | Text strings                               | `s = "hello"`                       | Text processing, input/output                |
| `list`       | Ordered, mutable sequence                  | `lst = [1, 2, 3]`                   | Dynamic collections                          |
| `tuple`      | Ordered, immutable sequence                | `tpl = (1, 2, 3)`                   | Fixed collections, dictionary keys           |
| `dict`       | Key-value mapping                          | `dct = {"a": 1, "b": 2}`            | Fast lookup, structured data                 |
| `set`        | Unordered unique elements                  | `st = {1, 2, 3}`                    | Removing duplicates, membership tests        |
| `frozenset`  | Immutable set                              | `fst = frozenset([1, 2, 3])`        | Dictionary keys, constants                   |
| `bool`       | Boolean values                             | `flag = True`                       | Conditional logic                            |
| `bytes`      | Immutable byte sequence                    | `b = b"hello"`                      | Binary data, networking                      |
| `bytearray`  | Mutable byte sequence                      | `ba = bytearray(b"hello")`          | Mutable binary data                          |
| `memoryview` | View of memory without copying             | `mv = memoryview(b"hello")`         | Efficient data access                        |
| `NoneType`   | Represents absence of value                | `x = None`                          | Defaults, optional values                    |

---

## 3. Quick Summary

- **Immutable** → values cannot change
- **Mutable** → values can change in place
- **Sequences** → ordered data
- **Mappings** → key–value pairs
- **Sets** → unique elements

---

Happy Learning Python 🐍
