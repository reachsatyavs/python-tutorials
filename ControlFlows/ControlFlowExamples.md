
Focus: **`if/elif/else`, `while`, `for`**  
Tip: Run these in order—examples gradually add concepts.

---

## Contents
- [A. `if / elif / else` (10 examples)](#a-if--elif--else-10-examples)
- [B. `while` (10 examples)](#b-while-10-examples)
- [C. `for` (10 examples)](#c-for-10-examples)
- [Quick Reference: Common Pitfalls](#quick-reference-common-pitfalls)

---

## A. `if / elif / else` (10 examples)

### 1) Basic boolean check
```python
is_prod = True

if is_prod:
    print("Running in production mode")
else:
    print("Running in non-production mode")
```

### 2) Numeric comparison
```python
cpu_usage = 82

if cpu_usage > 80:
    print("High CPU usage")
else:
    print("CPU usage normal")
```

### 3) Multiple branches with `elif`
```python
status_code = 404

if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")
else:
    print("Other status")
```

### 4) String membership (`in`)
```python
log_line = "ERROR: disk full"

if "ERROR" in log_line:
    print("Route to incident channel")
else:
    print("Normal log")
```

### 5) Compound conditions (`and` / `or`)
```python
env = "prod"
region = "asia-south1"

if env == "prod" and region.startswith("asia-"):
    print("Production in Asia region")
else:
    print("Other environment/region")
```

### 6) Nested `if` (then refactor later)
```python
user_role = "admin"
mfa_enabled = False

if user_role == "admin":
    if not mfa_enabled:
        print("Admin must enable MFA")
    else:
        print("Admin access granted")
else:
    print("Standard access")
```

### 7) Guard clause pattern (preferred in production)
```python
def deploy(service_name: str):
    if not service_name:
        raise ValueError("service_name is required")

    print(f"Deploying {service_name}...")

deploy("auth")
```

### 8) Validate config values
```python
timeout_seconds = 0

if timeout_seconds <= 0:
    print("Invalid timeout; must be > 0")
else:
    print("Timeout OK:", timeout_seconds)
```

### 9) Mapping-like logic using dict (reduces `elif` chains)
```python
handlers = {
    "start": "Starting service...",
    "stop": "Stopping service...",
    "restart": "Restarting service...",
}

action = "restart"

if action in handlers:
    print(handlers[action])
else:
    print("Unknown action")
```

### 10) Ternary (inline if) for simple assignments
```python
pta_mode = "PTA2"
label = "PTA2" if pta_mode == "PTA2" else "PTA1"
print(label)
```

---

## B. `while` (10 examples)

### 1) Count from 1 to 5
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### 2) Sum numbers until user enters 0
```python
total = 0

while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    total += n

print("Total:", total)
```

### 3) Simple password retry (max attempts)
```python
correct = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pwd = input("Password: ")
    if pwd == correct:
        print("Access granted")
        break
    attempts += 1
else:
    # runs only if loop ended without break
    print("Account locked")
```

### 4) Process queue until empty
```python
queue = ["job1", "job2", "job3"]

while queue:
    job = queue.pop(0)
    print("Processing:", job)
```

### 5) Retry pattern with backoff (simulation)
```python
import time

max_retries = 4
attempt = 1

while attempt <= max_retries:
    print(f"Attempt {attempt}...")
    success = (attempt == 3)  # simulate success on 3rd attempt

    if success:
        print("Success!")
        break

    sleep_seconds = 2 ** (attempt - 1)  # 1, 2, 4, 8
    print(f"Failed. Sleeping {sleep_seconds}s")
    time.sleep(0.1)  # keep demo fast; replace with sleep_seconds in real code
    attempt += 1
```

### 6) Polling until state changes (simulation)
```python
state = "PENDING"
checks = 0

while state != "DONE" and checks < 5:
    print("Checking status...", state)
    checks += 1
    if checks == 4:
        state = "DONE"

print("Final:", state)
```

### 7) Read lines until "exit"
```python
while True:
    line = input("Type something (exit to stop): ")
    if line.strip().lower() == "exit":
        break
    print("You typed:", line)
```

### 8) Validate input until correct type
```python
while True:
    raw = input("Enter an integer: ")
    if raw.isdigit():
        value = int(raw)
        break
    print("Not an integer. Try again.")

print("Got:", value)
```

### 9) Two-pointer technique (algorithmic use case)
```python
nums = [1, 2, 3, 4, 5, 6]
left, right = 0, len(nums) - 1
target_sum = 9

while left < right:
    s = nums[left] + nums[right]
    if s == target_sum:
        print("Pair found:", nums[left], nums[right])
        break
    elif s < target_sum:
        left += 1
    else:
        right -= 1
```

### 10) Stateful loop with multiple exits (realistic workflow)
```python
running = True
health = 100

while running:
    cmd = input("cmd (hit/heal/quit): ").strip().lower()

    if cmd == "hit":
        health -= 30
        print("Health:", health)
        if health <= 0:
            print("Game over")
            running = False

    elif cmd == "heal":
        health = min(100, health + 20)
        print("Health:", health)

    elif cmd == "quit":
        print("Bye")
        running = False

    else:
        print("Unknown cmd")
```

---

## C. `for` (10 examples)

### 1) Iterate over a list
```python
apps = ["auth", "billing", "search"]

for app in apps:
    print("Deploy:", app)
```

### 2) `range(n)` basic
```python
for i in range(5):
    print(i)
```

### 3) `range(start, stop)`
```python
for port in range(8000, 8003):
    print("Checking port:", port)
```

### 4) `range(start, stop, step)`
```python
for i in range(10, 0, -2):
    print(i)
```

### 5) Loop through string characters
```python
name = "satya"

for ch in name:
    print(ch)
```

### 6) `enumerate()` for index + value
```python
services = ["api", "worker", "cron"]

for idx, svc in enumerate(services, start=1):
    print(idx, svc)
```

### 7) Loop through dict keys/values/items
```python
config = {"env": "prod", "region": "asia-south1", "retries": 3}

for key, value in config.items():
    print(key, "=", value)
```

### 8) Filter + build a new list (list comprehension alternative shown)
```python
nums = [10, 15, 22, 33, 40]
evens = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)

print("Evens:", evens)

# same as:
# evens = [n for n in nums if n % 2 == 0]
```

### 9) Nested loops (matrix / grid)
```python
rows = 3
cols = 4

for r in range(rows):
    for c in range(cols):
        print(f"({r},{c})", end=" ")
    print()
```

### 10) Realistic processing pipeline (parse → validate → act)
```python
logs = [
    "INFO user=alice action=login",
    "ERROR user=bob action=pay",
    "INFO user=carol action=logout",
]

for line in logs:
    level = line.split()[0]

    if level == "ERROR":
        print("ALERT:", line)
    else:
        print("OK:", line)
```

---

## Quick Reference: Common Pitfalls

### 1) Indentation matters
```python
# Wrong:
# if True:
# print("hi")  # IndentationError

# Right:
if True:
    print("hi")
```

### 2) `=` vs `==`
- `=` assignment
- `==` comparison

### 3) Infinite loops
```python
# Always ensure the loop condition changes or use break.
i = 1
while i <= 3:
    print(i)
    i += 1
```

### 4) `for` is for iterables; `while` is for conditions
- Use `for` when iterating over known data.
- Use `while` when the stop condition depends on runtime state.

