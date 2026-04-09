"""
hash_explorer.py
================
A teaching tool that makes Python's internal hash table visible.

Run:  python hash_explorer.py

What this shows:
  1. hash() values for different types
  2. How bucket_index is computed  (hash % table_size)
  3. A simulated bucket array — where each key lands
  4. A collision example — two keys landing on same bucket
  5. Why lists cannot be dict keys (unhashable)
  6. Proof that dict lookup is O(1) via id() and slot inspection
"""


import sys
import ctypes

# ─────────────────────────────────────────────────────────────────────
# ANSI colours for terminal output (works on macOS / Linux / Win 10+)
# ─────────────────────────────────────────────────────────────────────
TEAL    = "\033[96m"
AMBER   = "\033[93m"
GREEN   = "\033[92m"
RED     = "\033[91m"
PURPLE  = "\033[95m"
BLUE    = "\033[94m"
MUTED   = "\033[90m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

def header(title):
    width = 62
    print()
    print(f"{TEAL}{BOLD}{'═' * width}{RESET}")
    print(f"{TEAL}{BOLD}  {title}{RESET}")
    print(f"{TEAL}{BOLD}{'═' * width}{RESET}")

def section(title):
    print(f"\n{AMBER}{BOLD}  ── {title} ──{RESET}")

def row(label, value, color=GREEN):
    print(f"  {MUTED}{label:<28}{RESET} {color}{value}{RESET}")


# ═════════════════════════════════════════════════════════════════════
# PART 1 — hash() values for different types
# ═════════════════════════════════════════════════════════════════════
header("PART 1 — hash() values for different Python types")

section("Strings")
for s in ["alice", "bob", "carol", "dave", "alice"]:  # alice repeated!
    row(f'hash("{s}")', hash(s), TEAL)

print(f"\n  {GREEN}✅ Notice: hash('alice') is always the same — deterministic{RESET}")

section("Integers")
for n in [0, 1, 42, 100, -5]:
    row(f"hash({n})", hash(n), AMBER)
print(f"\n  {GREEN}✅ Small integers hash to themselves in CPython{RESET}")

section("Tuples  (immutable → hashable)")
for t in [(1, 2), ("a", "b"), (1, 2, 3)]:
    row(f"hash({t})", hash(t), PURPLE)

section("Lists  (mutable → NOT hashable)")
try:
    hash([1, 2, 3])
except TypeError as e:
    row("hash([1, 2, 3])", f"TypeError: {e}", RED)
print(f"\n  {RED}❌ Lists are mutable — hash would change if content changes{RESET}")


# ═════════════════════════════════════════════════════════════════════
# PART 2 — Simulated bucket array  (bucket_index = hash(key) % size)
# ═════════════════════════════════════════════════════════════════════
header("PART 2 — Simulated bucket array")

TABLE_SIZE = 8   # small table so collisions are easy to see

section(f"Formula:  bucket_index = hash(key) % {TABLE_SIZE}")

keys   = ["alice", "bob", "carol", "dave", "eve"]
values = [92, 78, 88, 55, 71]

# Build a simple bucket array (list of lists for chaining display)
buckets = [[] for _ in range(TABLE_SIZE)]

print(f"\n  {'Key':<10} {'hash(key)':>22}  {'% ' + str(TABLE_SIZE):>4}  {'→  Bucket':>10}")
print(f"  {MUTED}{'─'*56}{RESET}")

for k, v in zip(keys, values):
    h   = hash(k)
    idx = h % TABLE_SIZE
    buckets[idx].append((k, v))
    collision = " 💥 COLLISION!" if len(buckets[idx]) > 1 else ""
    print(f"  {TEAL}{k:<10}{RESET} {MUTED}{h:>22}{RESET}  {AMBER}% {TABLE_SIZE}  → slot {idx}{RESET}{RED}{collision}{RESET}")

section("Resulting bucket array")
print()
for i, bucket in enumerate(buckets):
    if bucket:
        entries = "  |  ".join([f'{GREEN}key="{k}" val={v}{RESET}' for k, v in bucket])
        marker  = f"{AMBER}●{RESET}"
    else:
        entries = f"{MUTED}(empty){RESET}"
        marker  = " "
    print(f"  {MUTED}slot {i}{RESET}  {marker}  {entries}")


# ═════════════════════════════════════════════════════════════════════
# PART 3 — Real Python dict internals via sys and ctypes
# ═════════════════════════════════════════════════════════════════════
header("PART 3 — Real Python dict internals")

scores = {"alice": 92, "bob": 78, "carol": 88}

section("Memory size as dict grows")
print()
for n in range(1, 9):
    d    = {f"key{i}": i for i in range(n)}
    size = sys.getsizeof(d)
    bar  = "█" * (size // 20)
    print(f"  {MUTED}{n} keys →{RESET} {AMBER}{size:4d} bytes{RESET}  {TEAL}{bar}{RESET}")

print(f"""
  {GREEN}✅ Python over-allocates buckets (load factor ~⅔) so there
     is always room and collisions stay rare.
     When the table gets too full, Python DOUBLES it and
     re-hashes every key into the new larger table.{RESET}""")

section("id() — memory address of each key's value")
print()
for key in scores:
    val     = scores[key]
    address = id(val)
    bucket  = hash(key) % 8
    print(f"  {TEAL}scores['{key}']{RESET} = {GREEN}{val}{RESET}   "
          f"{MUTED}id={RESET}{AMBER}{address}{RESET}   "
          f"{MUTED}→ simulated slot{RESET} {PURPLE}{hash(key) % 8}{RESET}")

print(f"""
  {GREEN}✅ Python uses these addresses to jump directly to the value.
     That is why dict lookup is O(1) — no scanning, just jumping.{RESET}""")


# ═════════════════════════════════════════════════════════════════════
# PART 4 — Collision example (forced with small table)
# ═════════════════════════════════════════════════════════════════════
header("PART 4 — Hash collision example")

SIZE = 4   # tiny table — forces collisions

section(f"Using table size = {SIZE} to force collisions")
print()
words = ["cat", "dog", "hat", "rat", "bat"]
mini  = [[] for _ in range(SIZE)]

print(f"  {'Word':<8} {'hash':>20}  {'% ' + str(SIZE):>5}  {'Slot':>6}  Status")
print(f"  {MUTED}{'─'*52}{RESET}")

for w in words:
    h   = hash(w)
    idx = h % SIZE
    status = f"{RED}💥 COLLISION → probe for next free slot{RESET}" if mini[idx] else f"{GREEN}✅ stored{RESET}"
    mini[idx].append(w)
    print(f"  {TEAL}{w:<8}{RESET} {MUTED}{h:>20}{RESET}  {AMBER}% {SIZE} = {idx:>2}{RESET}  {status}")

print()
section("After collision resolution (Python probes for free slot)")
for i, bucket in enumerate(mini):
    content = f"{GREEN}{', '.join(bucket)}{RESET}" if bucket else f"{MUTED}empty{RESET}"
    print(f"  {MUTED}slot {i}:{RESET}  {content}")

print(f"""
  {AMBER}ℹ  Python uses open addressing with perturbation probing:
     next = (5 * current + 1 + perturbation) % size
     This spreads entries evenly — not just "check next slot".{RESET}""")


# ═════════════════════════════════════════════════════════════════════
# PART 5 — List vs Dict lookup speed (conceptual)
# ═════════════════════════════════════════════════════════════════════
header("PART 5 — Why dict beats list for lookups")

import time

N = 500_000
big_list = list(range(N))
big_dict = {i: True for i in range(N)}
target   = N - 1   # worst case — at the very end

section(f"Looking up {target} in {N:,} items")
print()

# list search — O(n)
start = time.perf_counter()
_ = target in big_list
list_time = (time.perf_counter() - start) * 1000

# dict lookup — O(1)
start = time.perf_counter()
_ = target in big_dict
dict_time = (time.perf_counter() - start) * 1000

print(f"  {MUTED}list (scans every item):  {RESET}{RED}{list_time:.4f} ms{RESET}  ← O(n) — gets slower as list grows")
print(f"  {MUTED}dict (hash → jump):       {RESET}{GREEN}{dict_time:.4f} ms{RESET}  ← O(1) — same speed no matter the size")
speedup = list_time / dict_time if dict_time > 0 else float("inf")
print(f"\n  {AMBER}dict is ~{speedup:.0f}× faster for this lookup{RESET}")
print(f"""
  {GREEN}✅ This is the entire point of hashing — the hash function
     converts the key into an address so Python can JUMP directly
     to the value instead of scanning from the start.{RESET}""")


# ═════════════════════════════════════════════════════════════════════
# SUMMARY
# ═════════════════════════════════════════════════════════════════════
header("SUMMARY — The full hashing pipeline")

print(f"""
  {TEAL}key  →  hash(key)  →  % table_size  →  bucket slot  →  value{RESET}

  {BOLD}Step by step:{RESET}
  {AMBER}1.{RESET} Python calls {GREEN}hash(key){RESET} to get a big integer
  {AMBER}2.{RESET} Applies {GREEN}% table_size{RESET} to get a slot index that fits
  {AMBER}3.{RESET} Jumps directly to that slot in memory
  {AMBER}4.{RESET} If the slot has the right key → return value  ✅
  {AMBER}5.{RESET} If slot is occupied by a different key → probe (collision)
  {AMBER}6.{RESET} If slot is empty → key does not exist → KeyError

  {BOLD}Why keys must be immutable:{RESET}
  {RED}If a key's content changes after storage, its hash changes.
  Python would look in the WRONG bucket and never find the value.
  This is why lists/dicts/sets cannot be dict keys — only
  immutable types (str, int, tuple, frozenset) are allowed.{RESET}

  {MUTED}Run this script again — hash values may differ each run
  (Python randomises string hashes for security — PYTHONHASHSEED){RESET}
""")