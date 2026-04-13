## 1. Built-in (Direct) Functions in Python

These are functions you can call directly without attaching them to any object.

### Commonly Used Built-in Functions

```
print()      # Display output
input()      # Take input from user
len()        # Length of object
id()         # Memory address of object
type()       # Type of object
hash()       # Hash value
int()        # Convert to integer
float()      # Convert to float
str()        # Convert to string
list()       # Convert to list
dict()       # Convert to dictionary
set()        # Convert to set
bool()       # Convert to boolean
range()      # Generate sequence
sum()        # Sum of elements
min()        # Minimum value
max()        # Maximum value
abs()        # Absolute value
round()      # Round number
sorted()     # Sort elements
reversed()   # Reverse sequence
enumerate()  # Index + value pairs
zip()        # Combine iterables
any()        # True if any element is True
all()        # True if all elements are True
help()       # Documentation
```

---

## 2. Analogy to Understand Functions

### 🔹 Built-in Functions (Global Functions)

Think of these like **tools in your toolbox**.

- You don’t need anything special to use them
- Just call them directly

👉 Example:

```
print("Hello")
len([1,2,3])
```

🧠 Analogy:

> Like using a **calculator** — you just press buttons directly.

---

### 🔹 Object Methods (Functions attached to objects)

These belong to specific objects.

- You must have an object first
- Then call function using dot (`.`)

👉 Example:

```
name = "python"
name.upper()

nums = [3,1,2]
nums.sort()
```

🧠 Analogy:

> Like **remote control for a TV**

- TV (object) must exist
- Remote buttons (methods) work only on that TV

---

## 3. Key Difference (Very Important)


| Feature             | Built-in Function | Object Method |
| ------------------- | ----------------- | ------------- |
| How to call         | print(x)          | x.method()    |
| Needs object first? | No                | Yes           |
| Example             | len(list)         | list.append() |


---

## 4. Examples by Data Type

### String Methods

```
text = "hello"
text.upper()
text.lower()
text.strip()
text.replace("h","H")
text.split()
```

### List Methods

```
nums = [1,2,3]
nums.append(4)
nums.remove(2)
nums.sort()
nums.reverse()
```

### Dictionary Methods

```
data = {"a":1}
data.get("a")
data.keys()
data.values()
data.items()
```

### Set Methods

```
s = {1,2,3}
s.add(4)
s.remove(2)
s.union({5,6})
```

---

## 5. Simple Rule for Students

👉 If function is written like:

```
function(x)
```

➡️ It is a **built-in function**

👉 If function is written like:

```
x.function()
```

➡️ It is a **method of object x**

---

## 6. Teaching Tip (Very Important)

Tell students:

> "Python has two types of actions:\
>
> 1. General tools (functions)\
> 2. Object-specific actions (methods)"

---

## 7. Quick Practice

Identify type:

```
len([1,2,3])        # ?
"hello".upper()     # ?
print(10)           # ?
[1,2,3].append(4)   # ?
```

---

## 8. Summary

- Built-in functions → global tools
- Methods → tied to objects
- Use dot (`.`) for methods

---

## 9. Bonus: How to Explore More

```
dir(str)
dir(list)
help(str)
```

---

### End of Guide

