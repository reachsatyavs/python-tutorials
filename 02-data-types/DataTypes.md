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

**About the Size column:** Values are **approximate** for **CPython on 64-bit** (measured with `sys.getsizeof()`). They change between Python versions. For **containers** (`list`, `dict`, `set`, etc.), the figure is mainly the **container object**; memory for **elements** (other objects they reference) is separate. `int` has **no fixed max size**—it grows as needed (arbitrary precision).

| Type         | Description                                | Example                             | Size (approx., CPython 64-bit) | Common Usage                                  |
|--------------|--------------------------------------------|-------------------------------------|--------------------------------|----------------------------------------------|
| `int`        | Integer numbers                            | `x = 42`                            | Not fixed; small ints often ~28 B; grows with magnitude | Counting, indexing, math operations          |
| `float`      | Floating-point numbers                     | `y = 3.14`                          | ~24 B (object + 8-byte IEEE 754 double) | Scientific calculations                     |
| `complex`    | Complex numbers                            | `z = 1 + 2j`                        | ~32 B (object + two floats) | Engineering, signal processing               |
| `str`        | Text strings                               | `s = "hello"`                       | Depends on length; empty str often ~40–50 B + storage for text | Text processing, input/output                |
| `list`       | Ordered, mutable sequence                  | `lst = [1, 2, 3]`                   | Empty list often ~56 B; grows with allocated slots + separate element objects | Dynamic collections                          |
| `tuple`      | Ordered, immutable sequence                | `tpl = (1, 2, 3)`                   | Empty tuple often ~40–50 B; grows with item slots + referenced items | Fixed collections, dictionary keys           |
| `dict`       | Key-value mapping                          | `dct = {"a": 1, "b": 2}`            | Empty dict often ~64 B; grows with number of keys/values | Fast lookup, structured data                 |
| `set`        | Unordered unique elements                  | `st = {1, 2, 3}`                    | Empty/small sets often ~200+ B; grows with elements | Removing duplicates, membership tests        |
| `frozenset`  | Immutable set                              | `fst = frozenset([1, 2, 3])`        | Similar idea to `set`; depends on element count | Dictionary keys, constants                   |
| `bool`       | Boolean values                             | `flag = True`                       | ~28 B; `True` / `False` are single shared objects | Conditional logic                            |
| `bytes`      | Immutable byte sequence                    | `b = b"hello"`                      | Header often ~33 B + about 1 B per byte in the sequence | Binary data, networking                      |
| `bytearray`  | Mutable byte sequence                      | `ba = bytearray(b"hello")`          | Mutable buffer + header; grows if you resize | Mutable binary data                          |
| `memoryview` | View of memory without copying             | `mv = memoryview(b"hello")`         | Small view object (~100–200 B typical); **does not copy** the underlying buffer | Efficient data access                        |
| `NoneType`   | Represents absence of value                | `x = None`                          | ~16 B; `None` is a single singleton | Defaults, optional values                    |

---

## 3. Quick Summary

- **Immutable** → values cannot change
- **Mutable** → values can change in place
- **Sequences** → ordered data
- **Mappings** → key–value pairs
- **Sets** → unique elements

---

Happy Learning Python 🐍
