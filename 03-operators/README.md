# Operators

Everything you need to know about Python operators — what they are, why they exist, and how every category works, from arithmetic to the ternary (conditional) expression.

---

## Contents

| File | Type | What it covers |
|------|------|----------------|
| `Operators.md` | Notes | What operators are, all categories (unary, binary, ternary), operator precedence table |
| `operators_examples.py` | Script | 2–3 runnable examples for every operator type |

---

## Key Concepts at a Glance

### What is an Operator?

An **operator** is a symbol (or keyword) that tells Python to perform a specific operation on one or more values called **operands**.

```
operand  operator  operand
  5        +         3      →  8
```

### Operator Arity (how many operands they take)

| Arity | Name | Example |
|-------|------|---------|
| 1 operand | **Unary** | `-x`, `not flag`, `~n` |
| 2 operands | **Binary** | `a + b`, `x == y` |
| 3 operands | **Ternary** | `value if condition else other` |

> Almost all Python operators are **binary**. There is exactly **one ternary operator** — the conditional expression (inline `if-else`).

---

### Categories

| # | Category | Symbols / Keywords | Purpose |
|---|----------|--------------------|---------|
| 1 | Arithmetic | `+` `-` `*` `/` `//` `%` `**` | Math |
| 2 | Comparison (Relational) | `==` `!=` `>` `<` `>=` `<=` | Compare values → bool |
| 3 | Logical | `and` `or` `not` | Combine boolean expressions |
| 4 | Assignment | `=` `+=` `-=` `*=` `/=` `//=` `%=` `**=` `&=` `\|=` `^=` `>>=` `<<=` | Store / update values |
| 5 | Bitwise | `&` `\|` `^` `~` `<<` `>>` | Operate on individual bits |
| 6 | Identity | `is` `is not` | Check object identity (same object in memory) |
| 7 | Membership | `in` `not in` | Check containment in a sequence |
| 8 | **Ternary** (Conditional) | `x if cond else y` | Inline if-else — Python's only 3-operand operator |
| 9 | Unary | `+` `-` `~` `not` | Single-operand operations |

---

### Ternary Operator — Quick Look

The ternary operator is the **only operator in Python that takes three operands**.

```python
# Syntax
value_if_true  if  condition  else  value_if_false

# Examples
label  = "even" if n % 2 == 0 else "odd"
name   = username if username else "Anonymous"
grade  = "A" if score >= 90 else "B" if score >= 75 else "C"
```

---

### Operator Precedence (high → low)

```
**                          (exponentiation)
+x  -x  ~x                  (unary)
*  /  //  %                 (multiplicative)
+  -                        (additive)
<<  >>                      (bit shifts)
&                           (bitwise AND)
^                           (bitwise XOR)
|                           (bitwise OR)
==  !=  >  <  >=  <=  is  is not  in  not in   (comparison / identity / membership)
not                         (logical NOT)
and                         (logical AND)
or                          (logical OR)
x if cond else y            (ternary / conditional expression)
=  +=  -=  …               (assignment — statement, not expression)
```

> **Tip:** When in doubt, add parentheses `()` to make intent explicit.

---

## Learning order

1. `Operators.md` — understand every category with definitions and 2–3 examples each
2. `operators_examples.py` — run every example and observe the output (`python3 operators_examples.py`)
