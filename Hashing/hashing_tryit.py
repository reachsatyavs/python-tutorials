# hashing_tryit.py
# ─────────────────────────────────────────────────────────────
# Simple, standalone hashing examples students can try one by one.
# No functions needed — copy any block into a file and run it.
# ─────────────────────────────────────────────────────────────

# ── Example 1: See a hash value with your own eyes ───────────
print("── Example 1: hash() values ──")
print(hash("Alice"))      # a big integer — the locker number
print(hash("alice"))      # different from "Alice"!
print(hash(42))           # integers hash to themselves in CPython
print(hash((1, 2, 3)))    # tuples are hashable

# Same key → same hash (within one run)
print(hash("Alice") == hash("Alice"))   # True

# ── Example 2: Lists are NOT hashable ────────────────────────
print("\n── Example 2: lists cannot be hashed ──")
try:
    print(hash([1, 2, 3]))
except TypeError as e:
    print("Error:", e)    # unhashable type: 'list'

# ── Example 3: Dict uses hashing to find values fast ─────────
print("\n── Example 3: dict lookup ──")
marks = {"Alice": 95, "Bob": 88, "Carol": 74}

# Python computes hash("Alice") and jumps directly to the slot
print(marks["Alice"])     # 95 — instant, no scanning

# ── Example 4: Only immutable types can be dict keys ─────────
print("\n── Example 4: valid and invalid dict keys ──")
d = {}

d["name"]   = "Alice"     # str key ✅
d[42]       = "age"       # int key ✅
d[(0, 0)]   = "origin"    # tuple key ✅

print(d)

try:
    d[[1, 2]] = "bad"     # list key ❌
except TypeError as e:
    print("Error:", e)

# ── Example 5: Set uses hashing for fast membership ──────────
print("\n── Example 5: set membership ──")
allowed = {"admin", "editor", "viewer"}

print("admin" in allowed)    # True  — O(1) hash jump
print("guest" in allowed)    # False — O(1) hash jump

# ── Example 6: Changing a key's hash would break the dict ────
print("\n── Example 6: why mutable keys would be dangerous ──")
# Tuples are safe because they cannot change
coord = (1, 2)
locations = {coord: "Point A"}
print(locations[(1, 2)])    # "Point A" — hash unchanged, found ✅

# If lists were allowed (they are NOT), this would happen:
# key = [1, 2]
# d = {key: "value"}
# key.append(3)             # hash(key) changes!
# print(d[key])             # KeyError — Python looks in wrong slot
print("(list-as-key demo skipped — Python correctly raises TypeError)")

# ── Example 7: Speed comparison — list vs dict ───────────────
print("\n── Example 7: list O(n) vs dict O(1) ──")
import time

SIZE = 1_000_000
data_list = list(range(SIZE))
data_dict = {i: True for i in range(SIZE)}
target = SIZE - 1    # worst case for list: at the very end

start = time.perf_counter()
_ = target in data_list
list_ms = (time.perf_counter() - start) * 1000

start = time.perf_counter()
_ = target in data_dict
dict_ms = (time.perf_counter() - start) * 1000

print(f"List search : {list_ms:.4f} ms  (scans up to {SIZE:,} items)")
print(f"Dict lookup : {dict_ms:.4f} ms  (one hash jump)")
if dict_ms > 0:
    print(f"Dict is ~{list_ms / dict_ms:.0f}x faster")

# ── Example 8: frozenset is hashable; set is not ─────────────
print("\n── Example 8: frozenset as a dict key ──")
fs = frozenset([1, 2, 3])
d = {fs: "immutable set key"}
print(d[fs])                  # "immutable set key"

try:
    bad = {frozenset([1, 2]): "ok", {1, 2}: "bad"}
except TypeError as e:
    print("set as key:", e)   # unhashable type: 'set'

# ── Example 9: hash collision (same slot, different keys) ────
print("\n── Example 9: slot collision demo ──")
TABLE_SIZE = 8
keys = ["alice", "bob", "carol", "dave", "eve"]

print(f"{'Key':<8}  {'hash':>22}  slot (% {TABLE_SIZE})")
print("-" * 42)
for k in keys:
    h = hash(k)
    slot = h % TABLE_SIZE
    print(f"{k:<8}  {h:>22}  {slot}")

print("\nTwo keys landing on the same slot = collision.")
print("Python handles it by probing nearby slots — still correct.")

# ── Example 10: Consistent hashing within a run ──────────────
print("\n── Example 10: same key, same hash every time (within one run) ──")
key = "python"
print("First  call:", hash(key))
print("Second call:", hash(key))
print("Same?       ", hash(key) == hash(key))   # always True
print()
print("Note: run the script twice and compare the numbers.")
print("They change between runs (PYTHONHASHSEED randomises string hashes),")
print("but are stable WITHIN one run — that is all Python needs.")
