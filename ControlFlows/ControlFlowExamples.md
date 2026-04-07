# Control flow — copy-paste examples

These snippets are **standalone**: copy **one** example into a new file or a single notebook cell and run it. You do **not** need to know functions yet—each block is a tiny program by itself.

**Sections:** [A. `if`](#a-if--elif--else) · [B. `while`](#b-while) · [C. `for`](#c-for) · [D. Guard clauses](#d-guard-clauses-flat-vs-nested) · [E. Pitfalls](#e-quick-reference-common-pitfalls)

**Note:** Examples that use `input()` wait for you to type in the terminal or notebook—run those on their own.

---

## A. `if` / `elif` / `else`

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

### 6) Nested `if` (harder to read—refactor when you can)

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

### 7) Guard style: check before you act (no function—just variables)

```python
service_name = "auth"

if not service_name:
    print("Error: service_name is required")
else:
    print("Deploying " + service_name + "...")
```

### 8) Validate a value

```python
timeout_seconds = 0

if timeout_seconds <= 0:
    print("Invalid timeout; must be > 0")
else:
    print("Timeout OK:", timeout_seconds)
```

### 9) Dict lookup instead of a long `elif` chain

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

### 10) Ternary (inline `if` for simple assignments)

```python
pta_mode = "PTA2"
label = "PTA2" if pta_mode == "PTA2" else "PTA1"
print(label)
```

### 11) `pass` — empty block placeholder

```python
# You need a block under if, but you are not ready to write it yet:
x = 1
if x > 0:
    pass  # add real code later
print("done")
```

### 12) Truthiness vs `None` (explicit check when it matters)

```python
value = ""

if value is None:
    print("Explicit None branch")
elif not value:
    print("Empty string: falsy, but not None")

value2 = None
print("value2 is None?", value2 is None)
```

### 13) `match` / `case` (Python 3.10+ only)

```python
code = 404

match code:
    case 200:
        msg = "OK"
    case 404:
        msg = "Not Found"
    case _:
        msg = "Other"

print(msg)
```

---

## B. `while`

### 1) Count from 1 to 5

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### 2) Sum numbers until you enter 0 (uses `input()`)

```python
total = 0

while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    total += n

print("Total:", total)
```

### 3) Password retry with `while` / `else` (`else` runs only if no `break`)

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
    print("Account locked")
```

### 4) Process a list like a queue until empty

```python
queue = ["job1", "job2", "job3"]

while queue:
    job = queue.pop(0)
    print("Processing:", job)
```

### 5) Retry with pause (`import time`)

```python
import time

max_retries = 4
attempt = 1

while attempt <= max_retries:
    print("Attempt", attempt, "...")
    success = attempt == 3

    if success:
        print("Success!")
        break

    sleep_seconds = 2 ** (attempt - 1)
    print("Failed. Sleeping", sleep_seconds, "s")
    time.sleep(0.1)
    attempt += 1
```

### 6) Polling until state changes (simulated)

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

### 7) Read lines until `"exit"` (uses `input()`)

```python
while True:
    line = input("Type something (exit to stop): ")
    if line.strip().lower() == "exit":
        break
    print("You typed:", line)
```

### 8) Keep asking until the input is digits (uses `input()`)

```python
while True:
    raw = input("Enter an integer: ")
    if raw.isdigit():
        value = int(raw)
        break
    print("Not an integer. Try again.")

print("Got:", value)
```

### 9) Two pointers on a sorted list (find pair with a target sum)

```python
nums = [1, 2, 3, 4, 5, 6]
left = 0
right = len(nums) - 1
target_sum = 9

while left < right:
    s = nums[left] + nums[right]
    if s == target_sum:
        print("Pair found:", nums[left], nums[right])
        break
    if s < target_sum:
        left += 1
    else:
        right -= 1
```

### 10) Simple menu loop (uses `input()`)

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

### 11) `while` / `else`: only if the loop did **not** `break`

```python
attempts = 0
success_flag = False

while attempts < 3:
    if success_flag:
        print("Succeeded inside loop")
        break
    attempts += 1
else:
    print("while-else: finished without break (e.g. retries used up)")
```

---

## C. `for`

### 1) Iterate over a list

```python
apps = ["auth", "billing", "search"]

for app in apps:
    print("Deploy:", app)
```

### 2) `range(n)`

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

### 5) Loop through characters in a string

```python
name = "satya"

for ch in name:
    print(ch)
```

### 6) `enumerate()` — index and value

```python
services = ["api", "worker", "cron"]

for idx, svc in enumerate(services, start=1):
    print(idx, svc)
```

### 7) Loop through a dictionary

```python
config = {"env": "prod", "region": "asia-south1", "retries": 3}

for key, value in config.items():
    print(key, "=", value)
```

### 8) Filter into a new list

```python
nums = [10, 15, 22, 33, 40]
evens = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)

print("Evens:", evens)
```

### 9) Nested loops (grid)

```python
rows = 3
cols = 4

for r in range(rows):
    for c in range(cols):
        print("(" + str(r) + "," + str(c) + ")", end=" ")
    print()
```

### 10) Parse lines and branch on a token

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

### 11) `zip()` — two lists in parallel

```python
names = ("A", "B", "C")
scores = (90, 80, 85)

for name, score in zip(names, scores):
    print(name, score)
```

### 12) `for` / `else`: run `else` if **no** `break` happened

```python
items = [{"id": 1}, {"id": 2}, {"id": 3}]
target_id = 99

for item in items:
    if item["id"] == target_id:
        print("Found")
        break
else:
    print("for-else: not found (loop finished without break)")
```

### 13) `break` vs `continue`

```python
for n in range(10):
    if n == 5:
        break
    print("break demo:", n)

for n in range(5):
    if n == 2:
        continue
    print("continue demo:", n)
```

---

## D. Guard clauses (flat vs nested)

Use **early checks** so the main logic stays at the left margin. Here `user` is either `None` or a **dictionary** (no classes needed).

### Nested style (harder to follow)

```python
user = {"is_active": True, "has_permission": False}

if user is not None:
    if user["is_active"]:
        if user["has_permission"]:
            result = "Allowed"
        else:
            result = "No Permission"
    else:
        result = "Inactive"
else:
    result = "No User"

print(result)
```

### Guard style (same logic, flatter)

```python
user = {"is_active": True, "has_permission": True}

if user is None:
    result = "No User"
elif not user["is_active"]:
    result = "Inactive"
elif not user["has_permission"]:
    result = "No Permission"
else:
    result = "Allowed"

print(result)
```

### `continue` to skip bad items (list of dicts)

```python
files = [
    {"name": "a.txt", "valid": True},
    {"name": "bad.log", "valid": False},
    {"name": "b.txt", "valid": True},
]

for file in files:
    if not file["valid"]:
        continue
    print("processing", file["name"])
```

### Fail fast with `raise` (optional)

```python
a = 10
b = 0

if b == 0:
    raise ValueError("Denominator cannot be zero")

print(a / b)
```

---

## E. Quick reference: common pitfalls

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

- `=` assigns a value.
- `==` compares two values.

### 3) Infinite `while`

Make sure something changes, or use `break`:

```python
i = 1
while i <= 3:
    print(i)
    i += 1
```

### 4) `for` vs `while`

- Use `for` when you are stepping through a known iterable.
- Use `while` when stopping depends on state that changes as you go (retries, menus, `input()`).

---

For concepts and diagrams, see **`ControlFlow.md`**.
