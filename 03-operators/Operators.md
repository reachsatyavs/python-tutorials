# Python Operators – Complete Guide

---

## 1. What is an Operator?

An **operator** is a built-in symbol or keyword that performs an operation on one or more **operands** (values or variables) and produces a result.

```python
result = 10 + 3   # '+' is the operator; 10 and 3 are operands; 13 is the result
```

### Why are operators important?

| Reason | Explanation |
|--------|-------------|
| **Computation** | Arithmetic, bit manipulation, power calculations |
| **Decision making** | Comparison and logical operators drive `if` / `while` conditions |
| **Concise code** | Assignment operators like `+=` avoid repetition |
| **Data lookup** | Membership operators (`in`) replace verbose loops |
| **Low-level control** | Bitwise operators let you work directly with binary data |

---

## 2. Operator Arity

**Arity** = how many operands an operator needs.

| Arity | Name | Python Examples |
|-------|------|----------------|
| 1 operand | **Unary** | `-x`, `+x`, `~n`, `not flag` |
| 2 operands | **Binary** | `a + b`, `x >= y`, `a and b` |
| 3 operands | **Ternary** | `val if condition else other` |

> Python has one explicit **ternary operator** — the *conditional expression* (sometimes called an inline `if`).  
> Almost everything else is **binary**.

---

## 3. Categories of Operators

---

### 3.1 Arithmetic Operators (Binary)

Perform standard mathematical operations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `7 + 3` | `10` |
| `-` | Subtraction | `7 - 3` | `4` |
| `*` | Multiplication | `7 * 3` | `21` |
| `/` | True division | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Modulus (remainder) | `7 % 3` | `1` |
| `**` | Exponentiation | `2 ** 8` | `256` |

**Examples:**

```python
# Example 1 – basic math
a, b = 15, 4
print(a + b)    # 19
print(a - b)    # 11
print(a * b)    # 60

# Example 2 – floor division vs true division
print(15 / 4)   # 3.75  (always returns float)
print(15 // 4)  # 3     (rounds down to nearest integer)

# Example 3 – modulus and exponentiation
print(15 % 4)   # 3     (remainder after dividing 15 by 4)
print(2 ** 10)  # 1024  (2 to the power of 10)
```

---

### 3.2 Comparison (Relational) Operators (Binary)

Compare two values and always return a **bool** (`True` or `False`).

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `7 > 3` | `True` |
| `<` | Less than | `3 < 7` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `4 <= 3` | `False` |

**Examples:**

```python
# Example 1 – numeric comparison
age = 20
print(age >= 18)    # True  → can vote
print(age == 21)    # False

# Example 2 – chained comparisons (Python allows this)
score = 75
print(50 < score < 100)   # True  → score is between 50 and 100

# Example 3 – string comparison (lexicographic order)
print("apple" < "banana")   # True  → 'a' comes before 'b' in ASCII
print("zebra" > "ant")      # True
```

---

### 3.3 Logical Operators (Binary + Unary)

Combine or negate boolean expressions.

| Operator | Arity | Behaviour | Example | Result |
|----------|-------|-----------|---------|--------|
| `and` | Binary | `True` only if **both** sides are truthy | `True and False` | `False` |
| `or` | Binary | `True` if **at least one** side is truthy | `True or False` | `True` |
| `not` | **Unary** | Reverses the boolean value | `not True` | `False` |

> **Short-circuit evaluation**: `and` stops at the first falsy value; `or` stops at the first truthy value.

**Examples:**

```python
# Example 1 – access control
is_logged_in = True
has_permission = False
print(is_logged_in and has_permission)  # False → both must be True

# Example 2 – fallback with or
username = ""
display = username or "Guest"
print(display)   # Guest  → username is falsy, so 'or' returns the right side

# Example 3 – negation with not
is_raining = False
print(not is_raining)           # True
print(not (5 > 3 and 2 < 1))   # True  → not (True and False) → not False
```

---

### 3.4 Assignment Operators

Store a value in a variable. The **augmented** forms (`+=`, `-=`, …) update the variable in-place and are shorthand for `x = x op value`.

| Operator | Equivalent to | Example | After example |
|----------|---------------|---------|---------------|
| `=` | — | `x = 10` | `x = 10` |
| `+=` | `x = x + n` | `x += 3` | `x = 13` |
| `-=` | `x = x - n` | `x -= 2` | `x = 8` |
| `*=` | `x = x * n` | `x *= 4` | `x = 40` |
| `/=` | `x = x / n` | `x /= 2` | `x = 5.0` |
| `//=` | `x = x // n` | `x //= 3` | `x = 3` |
| `%=` | `x = x % n` | `x %= 3` | `x = 1` |
| `**=` | `x = x ** n` | `x **= 2` | `x = 100` |
| `&=` | `x = x & n` | `x &= 0b1100` | bitwise AND |
| `\|=` | `x = x \| n` | `x \|= 0b0011` | bitwise OR |
| `^=` | `x = x ^ n` | `x ^= 0b1010` | bitwise XOR |
| `>>=` | `x = x >> n` | `x >>= 1` | right shift |
| `<<=` | `x = x << n` | `x <<= 2` | left shift |

**Examples:**

```python
# Example 1 – accumulating a total
total = 0
for price in [10, 25, 5, 40]:
    total += price
print(total)   # 80

# Example 2 – countdown with -=
lives = 3
lives -= 1
print(lives)   # 2

# Example 3 – power with **=
base = 2
base **= 8
print(base)    # 256
```

---

### 3.5 Bitwise Operators (Binary + Unary)

Operate on integers at the **individual bit** level.

| Operator | Name | Arity | Description |
|----------|------|-------|-------------|
| `&` | AND | Binary | 1 only where **both** bits are 1 |
| `\|` | OR | Binary | 1 where **either** bit is 1 |
| `^` | XOR | Binary | 1 where bits are **different** |
| `~` | NOT | **Unary** | Flips all bits (`~n = -(n+1)`) |
| `<<` | Left shift | Binary | Shifts bits left (multiply by 2ⁿ) |
| `>>` | Right shift | Binary | Shifts bits right (divide by 2ⁿ) |

**Examples:**

```python
# Example 1 – AND, OR, XOR
a = 0b1010   # 10
b = 0b1100   # 12
print(bin(a & b))   # 0b1000  (8)  → AND
print(bin(a | b))   # 0b1110  (14) → OR
print(bin(a ^ b))   # 0b0110  (6)  → XOR

# Example 2 – left and right shift
n = 4            # 0b0100
print(n << 2)    # 16  → shift left by 2 = multiply by 4
print(n >> 1)    # 2   → shift right by 1 = divide by 2

# Example 3 – bitwise NOT (unary)
x = 5
print(~x)    # -6   (flips all bits; result is -(x+1))
```

---

### 3.6 Identity Operators (Binary)

Test whether two names point to the **same object in memory** — not just equal values.

| Operator | Meaning | Example |
|----------|---------|---------|
| `is` | Same object | `a is b` |
| `is not` | Different objects | `a is not b` |

> Use `is` / `is not` for `None` checks and singleton comparisons. Use `==` for value equality.

**Examples:**

```python
# Example 1 – None check (the idiomatic way)
result = None
if result is None:
    print("No result yet")   # printed

# Example 2 – small integer caching (CPython caches -5 to 256)
x = 100
y = 100
print(x is y)    # True  → same cached object

a = 1000
b = 1000
print(a is b)    # False → different objects (outside cache range)

# Example 3 – list identity vs equality
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 == list2)    # True  → same values
print(list1 is list2)    # False → different objects
print(list1 is list3)    # True  → same object (aliased)
```

---

### 3.7 Membership Operators (Binary)

Test whether a value exists **inside** a sequence or collection.

| Operator | Returns `True` when… | Works with |
|----------|----------------------|------------|
| `in` | value is found in the container | `str`, `list`, `tuple`, `set`, `dict`, `range` |
| `not in` | value is NOT found | same |

**Examples:**

```python
# Example 1 – list membership
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)       # True
print("grape" not in fruits)    # True

# Example 2 – string substring check
sentence = "Python is awesome"
print("awesome" in sentence)    # True
print("Java" not in sentence)   # True

# Example 3 – dictionary key check
config = {"host": "localhost", "port": 8080}
print("port" in config)         # True  → checks keys by default
print("timeout" not in config)  # True
```

---

### 3.8 Ternary Operator (Conditional Expression) — the only Ternary operator

Python's **ternary operator** is a compact, single-line `if-else` expression. It is the **only operator in Python that takes three operands**.

**Syntax:**

```
value_if_true  if  condition  else  value_if_false
```

| Part | Role |
|------|------|
| `condition` | Evaluated first — any truthy/falsy expression |
| `value_if_true` | Returned when `condition` is `True` |
| `value_if_false` | Returned when `condition` is `False` |

**Examples:**

```python
# Example 1 – simple even/odd label
n = 7
label = "even" if n % 2 == 0 else "odd"
print(label)    # odd

# Example 2 – default value assignment
name = ""
display = name if name else "Anonymous"
print(display)   # Anonymous

# Example 3 – nested ternary (use sparingly — readability drops fast)
score = 82
grade = "A" if score >= 90 else "B" if score >= 75 else "C"
print(grade)    # B
```

---

### 3.9 Unary Operators

Operate on a **single operand**.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `-` | Unary minus | `-x` | negates `x` |
| `+` | Unary plus | `+x` | no change (identity) |
| `~` | Bitwise NOT | `~n` | `-(n+1)` |
| `not` | Logical NOT | `not flag` | inverts bool |

**Examples:**

```python
# Example 1 – unary minus and plus
x = 5
print(-x)    # -5
print(+x)    #  5  (no-op on plain numbers)

# Example 2 – unary minus on a float
temp = 3.7
print(-temp)   # -3.7

# Example 3 – logical not
is_empty = len([]) == 0
print(is_empty)        # True
print(not is_empty)    # False
```

---

## 4. Operator Precedence Table

Operators higher in the table are evaluated **first** (higher precedence).

| Precedence | Operator(s) | Description |
|------------|-------------|-------------|
| 1 (highest) | `**` | Exponentiation |
| 2 | `+x` `-x` `~x` | Unary |
| 3 | `*` `/` `//` `%` | Multiplicative |
| 4 | `+` `-` | Additive |
| 5 | `<<` `>>` | Bit shifts |
| 6 | `&` | Bitwise AND |
| 7 | `^` | Bitwise XOR |
| 8 | `\|` | Bitwise OR |
| 9 | `==` `!=` `>` `<` `>=` `<=` `is` `is not` `in` `not in` | Comparison / identity / membership |
| 10 | `not` | Logical NOT |
| 11 | `and` | Logical AND |
| 12 | `or` | Logical OR |
| 13 (lowest expression) | `x if cond else y` | Ternary |

> **Tip:** When in doubt, use parentheses `()` to make the intended order explicit.

```python
# precedence in action
print(2 + 3 * 4)       # 14  (not 20) → * before +
print((2 + 3) * 4)     # 20  → parentheses override precedence
print(not 5 > 3)       # False → (5 > 3) evaluated first → not True → False
```

---

## 5. Summary

| Operator type | Arity | Typical use |
|---------------|-------|-------------|
| Arithmetic | Binary | Math calculations |
| Comparison | Binary | Conditions, sorting |
| Logical | Binary (`and`/`or`) + Unary (`not`) | Boolean logic |
| Assignment | Binary | Store / update variables |
| Bitwise | Binary + Unary (`~`) | Flags, low-level data, cryptography |
| Identity | Binary | `None` checks, singleton tests |
| Membership | Binary | Searching in collections |
| Ternary | **Ternary** (3 operands) | Inline conditional expressions |
| Unary | Unary | Negate, invert single values |
