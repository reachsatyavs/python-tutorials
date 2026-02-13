
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

### Guard Clause Pattern (Production Style)

``` python
def process_payment(amount):
    if amount <= 0:
        raise ValueError("Invalid amount")

    print("Processing payment:", amount)
```

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

