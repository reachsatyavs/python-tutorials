
# Python Mutable vs Immutable Objects – Complete Guide

This README provides a **complete, unified explanation** of:
- Why Python has mutable and immutable objects
- How Python’s memory model works
- Python vs Java comparison

---

## 🔑 What Really Matters in Python

In Python:

- **Variables do NOT store values**
- Variables store **references to objects**
- Objects have three properties:
  - **Identity** (memory address)
  - **Type**
  - **Value**

```python
x = 10
```

- `10` is an **object**
- `x` is just a **label pointing to that object**

---

### Immutable Objects
- Cannot change after creation
- Examples: int, str, tuple

### Mutable Objects
- Can change in place
- Examples: list, dict, set

---

## Memory Model (Visual)

Immutable:
```
a ──▶ 10
b ──▶ 10
```

Mutable:
```
lst1 ─┐
      ├──▶ [1, 2, 3]
lst2 ─┘
```

---

## Cheat Sheet
```
- Immutable → safe, hashable, predictable
            → share freely, reuse safely
- Mutable → fast, flexible, efficient
          → modify carefully, avoid accidental sharing
```
---

## Summary Table – Mutable vs Immutable Objects in Python

## Summary Table – Mutable vs Immutable Objects in Python

| Aspect | Immutable Objects | Mutable Objects |
|------|------------------|----------------|
| Value change | ❌ Cannot change after creation | ✅ Can change in place |
| Memory reuse | ✅ Python may reuse objects like `a=10; b=10; a is b → True` | ❌ Each mutation changes same object |
| Hashable | ✅ Can be dict keys (`d[10]="x"`, `d[(1,2)]="y"`) | ❌ Cannot be dict keys (`d[[1,2]] → TypeError`) |
| Safe sharing | ✅ Safe: functions cannot modify shared object | ❌ Unsafe: shared references can mutate |
| Best suited for | Read-heavy, constant data | Write-heavy, changing data |


---

## Python vs Java

| Aspect | Python | Java |
|------|-------|------|
| Variables | References | References |
| Primitives | All objects | Separate |
