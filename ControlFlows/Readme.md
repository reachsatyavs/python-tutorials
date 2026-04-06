
## Overview

Control flow determines how a program makes decisions and repeats
actions.

Python provides:

-   `if / elif / else` → conditional branching
-   `while` → condition-controlled loop
-   `for` → iterable-controlled loop
-   `break` and `continue` → loop control modifiers

------------------------------------------------------------------------

# 1️⃣ Conditional Statements (`if / elif / else`)

## Syntax

``` python
if condition:
    block
elif another_condition:
    block
else:
    block
```

## Example -- Environment-based Configuration

``` python
env = "prod"

if env == "prod":
    db_url = "prod.db.company.com"
elif env == "stage":
    db_url = "stage.db.company.com"
else:
    db_url = "localhost"

print(db_url)
```

### Before vs. After (Production Style)

#### ❌ Nested "Arrow" Code (Bad Practice)

``` python
def process_user_data(user):
    if user is not None:
        if user.is_active:
            if user.has_permission:
                # Main logic buried 3 levels deep
                return "Allowed"
            else:
                return "No Permission"
        else:
            return "Inactive"
    else:
        return "No User"
```

#### Guard Clause Pattern (Production Style)

``` python
def process_user_data(user):
    # Guard Clauses: Handle edge cases first
    if user is None:
        return "No User"
    if not user.is_active:
        return "Inactive"
    if not user.has_permission:
        return "No Permission"

    # Main logic is flat and easy to read
    return "Allowed"
```

#### Key Benefits

- **Reduced cognitive load:** You do not have to remember all the conditions from nested `if` statements.
- **Flattened structure:** Avoids the "arrow" anti-pattern (deeply nested code).
- **Early fail / return:** The function can exit early, saving work when the data is invalid.
- **Improved readability:** The happy path (successful flow) stays clear and is not buried inside nested error handling.

#### Production Techniques in Python

**Fail fast with exceptions:** Instead of `return`, use `raise` for invalid state.

``` python
def calculate_ratio(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b
```

**Using `continue` in loops:** Guard-style checks are useful for skipping invalid items.

``` python
for file in files:
    if not file.is_valid():
        continue
    process(file)
```

**Input validation:** Check inputs at the top of the function so invalid cases are handled immediately.

Guard clauses are a key part of writing clean code: structure is easier to read and maintain.

------------------------------------------------------------------------

# 2️⃣ `while` Loop (Condition Controlled)

## Example -- Retry Logic

``` python
max_retries = 3
attempt = 1

while attempt <= max_retries:
    print(f"Attempt {attempt}")
    attempt += 1
```

## Example -- Polling Pattern

``` python
status = "pending"

while status != "completed":
    print("Waiting...")
    status = "completed"
```

## Infinite Loop Pattern (Controlled Exit)

``` python
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == "exit":
        break
```

------------------------------------------------------------------------

# 3️⃣ `for` Loop (Iterable Controlled)

## Iterating Over Collection

``` python
services = ["auth", "billing", "notifications"]

for service in services:
    print("Deploying:", service)
```

## Using `range()`

``` python
for i in range(5):
    print(i)
```

``` python
for i in range(1, 10, 2):
    print(i)
```

------------------------------------------------------------------------

# 4️⃣ Loop + Condition Pattern

``` python
numbers = [10, 15, 22, 33, 40]

for n in numbers:
    if n % 2 == 0:
        print("Even:", n)
```

------------------------------------------------------------------------

# 5️⃣ `break` and `continue`

## break

``` python
for n in range(10):
    if n == 5:
        break
    print(n)
```

## continue

``` python
for n in range(5):
    if n == 2:
        continue
    print(n)
```

------------------------------------------------------------------------

# 6️⃣ Production Patterns

## Validate → Process

``` python
for user in users:
    if not user.is_active:
        continue

    process(user)
```

## Search Pattern

``` python
for item in items:
    if item.id == target_id:
        print("Found")
        break
```

## Accumulator Pattern

``` python
total = 0

for price in prices:
    total += price

print(total)
```

------------------------------------------------------------------------

# 7️⃣ Nested Loops

``` python
for i in range(3):
    for j in range(2):
        print(i, j)
```

⚠ Be cautious: Nested loops increase time complexity (O(n²)).

------------------------------------------------------------------------

# 8️⃣ When to Use What

  Scenario                Recommended
  ----------------------- -------------
  Known iteration count   `for`
  Iterating collections   `for`
  Retry logic             `while`
  State-driven exit       `while`
  Guard conditions        `if`

