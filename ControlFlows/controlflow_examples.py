# controlflow_examples.py
# ──────────────────────────────────────────────────────────────
# Real-world style control flow examples for teaching.
# Each example is self-contained — copy any block and run it.
# ──────────────────────────────────────────────────────────────

# ── Example 1: Traffic light (if / elif / else) ──────────────
print("── 1. Traffic light ──")
light = "red"

if light == "green":
    print("Go!")
elif light == "yellow":
    print("Slow down.")
elif light == "red":
    print("Stop!")
else:
    print("Unknown signal.")


# ── Example 2: Grade classifier ──────────────────────────────
print("\n── 2. Grade classifier ──")
score = 73

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")


# ── Example 3: Login attempt counter (while) ─────────────────
print("\n── 3. Login attempts (simulated) ──")
correct_password = "python123"
attempts = 0
max_attempts = 3
passwords_to_try = ["wrong1", "wrong2", "python123"]   # simulated input

while attempts < max_attempts:
    pwd = passwords_to_try[attempts]
    print(f"  Trying: '{pwd}'")
    if pwd == correct_password:
        print("  Access granted!")
        break
    attempts += 1
else:
    print("  Too many failed attempts. Account locked.")


# ── Example 4: Count down timer (while) ──────────────────────
print("\n── 4. Countdown ──")
count = 5
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  Blast off!")


# ── Example 5: FizzBuzz (for + if) ───────────────────────────
print("\n── 5. FizzBuzz (1–20) ──")
for n in range(1, 21):
    if n % 15 == 0:
        print("FizzBuzz", end="  ")
    elif n % 3 == 0:
        print("Fizz", end="  ")
    elif n % 5 == 0:
        print("Buzz", end="  ")
    else:
        print(n, end="  ")
print()


# ── Example 6: Shopping cart total (for + accumulator) ───────
print("\n── 6. Shopping cart ──")
cart = [
    {"item": "Laptop",  "price": 75000},
    {"item": "Mouse",   "price": 1200},
    {"item": "Keyboard","price": 2500},
    {"item": "Monitor", "price": 18000},
]

total = 0
for product in cart:
    print(f"  {product['item']:<12}  ₹{product['price']:>7,}")
    total += product["price"]

print(f"  {'─' * 24}")
print(f"  {'Total':<12}  ₹{total:>7,}")


# ── Example 7: Filter — find failing students ─────────────────
print("\n── 7. Find failing students ──")
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob",   "score": 42},
    {"name": "Carol", "score": 55},
    {"name": "Dave",  "score": 91},
    {"name": "Eve",   "score": 38},
]

print("  Failing (score < 60):")
for s in students:
    if s["score"] < 60:
        print(f"    {s['name']}  →  {s['score']}")


# ── Example 8: Number guessing game (while + break) ───────────
print("\n── 8. Number guessing game (simulated guesses) ──")
secret = 42
guesses = [10, 60, 42]    # simulated player guesses
found = False

for guess in guesses:
    print(f"  Guess: {guess}", end="  →  ")
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        found = True
        break

if not found:
    print(f"  Ran out of guesses. The number was {secret}.")


# ── Example 9: Multiplication table (nested for) ─────────────
print("\n── 9. Multiplication table (1–5) ──")
for i in range(1, 6):
    row = ""
    for j in range(1, 6):
        row += f"{i * j:>4}"
    print(row)


# ── Example 10: ATM menu (while + elif) ─────────────────────
print("\n── 10. ATM simulation (simulated commands) ──")
balance = 10000
commands = ["balance", "withdraw 2000", "deposit 500", "withdraw 9999", "exit"]

for cmd in commands:
    print(f"\n  Command: {cmd}")
    if cmd == "balance":
        print(f"  Balance: ₹{balance:,}")

    elif cmd.startswith("withdraw"):
        amount = int(cmd.split()[1])
        if amount > balance:
            print(f"  Insufficient funds. Balance: ₹{balance:,}")
        else:
            balance -= amount
            print(f"  Withdrew ₹{amount:,}. Remaining: ₹{balance:,}")

    elif cmd.startswith("deposit"):
        amount = int(cmd.split()[1])
        balance += amount
        print(f"  Deposited ₹{amount:,}. New balance: ₹{balance:,}")

    elif cmd == "exit":
        print("  Thank you. Goodbye!")
        break

    else:
        print("  Unknown command.")


# ── Example 11: Skip weekends, process weekdays (continue) ────
print("\n── 11. Skip weekends ──")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for day in days:
    if day in ("Sat", "Sun"):
        print(f"  {day}: Weekend — skipping")
        continue
    print(f"  {day}: Processing work tasks...")


# ── Example 12: Search and for/else ──────────────────────────
print("\n── 12. Search with for/else ──")
inventory = ["pen", "notebook", "stapler", "ruler", "eraser"]
item_to_find = "scissors"

for item in inventory:
    if item == item_to_find:
        print(f"  Found '{item_to_find}' in inventory.")
        break
else:
    print(f"  '{item_to_find}' not found — needs to be ordered.")


# ── Example 13: Validate ages in a list (guard + continue) ────
print("\n── 13. Validate age entries ──")
raw_ages = [25, -3, 17, 200, 34, 0, 42]

valid_ages = []
for age in raw_ages:
    if age < 0 or age > 120:
        print(f"  Skipping invalid age: {age}")
        continue
    valid_ages.append(age)

print(f"  Valid ages: {valid_ages}")
print(f"  Average:    {sum(valid_ages) / len(valid_ages):.1f}")
