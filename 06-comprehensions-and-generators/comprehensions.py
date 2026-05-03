"""
============================================================
  Python Comprehensions — 32 Examples
  Module 4 · github.com/reachsatyavs/python-tutorials
============================================================
  Sections:
    1. List Comprehension      [ ]       — Examples 1–8
    2. Set Comprehension       { }       — Examples 9–16
    3. Dict Comprehension      { k:v }   — Examples 17–24
    4. Generator Expression    ( )       — Examples 25–32
============================================================
"""

from itertools import islice

SEP  = "=" * 55
DASH = "-" * 55

# ─────────────────────────────────────────────────────────
#  SECTION 1 — LIST COMPREHENSION  [ ]
#  Returns: list · Ordered · Allows duplicates
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 1 — LIST COMPREHENSION  [ ]")
print(SEP)

# ── Example 1: Squares of numbers ────────────────────────
print("\n[Ex 01] Squares of numbers")
print(DASH)

squares = [x**2 for x in range(1, 6)]

print(f"  squares = {squares}")
# [1, 4, 9, 16, 25]


# ── Example 2: Filter even numbers ───────────────────────
print("\n[Ex 02] Filter even numbers")
print(DASH)

nums  = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in nums if x % 2 == 0]

print(f"  nums  = {nums}")
print(f"  evens = {evens}")
# [2, 4, 6, 8]


# ── Example 3: Uppercase names ───────────────────────────
print("\n[Ex 03] Uppercase names")
print(DASH)

names = ["rajeev", "priya", "arun"]
upper = [n.upper() for n in names]

print(f"  names = {names}")
print(f"  upper = {upper}")
# ['RAJEEV', 'PRIYA', 'ARUN']


# ── Example 4: Pass / Fail labels ────────────────────────
print("\n[Ex 04] Pass / Fail labels  (if-else in expression)")
print(DASH)

marks  = [45, 82, 60, 38, 91]
result = ["pass" if m >= 60 else "fail" for m in marks]

print(f"  marks  = {marks}")
print(f"  result = {result}")
# ['fail', 'pass', 'pass', 'fail', 'pass']


# ── Example 5: Flatten a nested list ─────────────────────
print("\n[Ex 05] Flatten a nested list  (nested for clauses)")
print(DASH)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [val for row in matrix for val in row]

print(f"  matrix = {matrix}")
print(f"  flat   = {flat}")
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ── Example 6: Extract vowels from a string ───────────────
print("\n[Ex 06] Extract vowels from a string")
print(DASH)

sentence = "hello world"
vowels   = [ch for ch in sentence if ch in "aeiou"]

print(f"  sentence = {sentence!r}")
print(f"  vowels   = {vowels}")
# ['e', 'o', 'o']


# ── Example 7: Clean & filter student records ─────────────
print("\n[Ex 07] Clean & filter student records")
print(DASH)

students = [
    {"name": "  Rajeev ", "score": 82},
    {"name": "Priya",     "score": 45},
    {"name": " Arun  ",   "score": 91},
    {"name": "Meena",     "score": 38},
]
toppers = [s["name"].strip() for s in students if s["score"] >= 60]

print(f"  toppers = {toppers}")
# ['Rajeev', 'Arun']


# ── Example 8: Multiplication table ──────────────────────
print("\n[Ex 08] Multiplication table for n=5")
print(DASH)

n     = 5
table = [n * i for i in range(1, 11)]

print(f"  {n} x table = {table}")
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


# ─────────────────────────────────────────────────────────
#  SECTION 2 — SET COMPREHENSION  { }
#  Returns: set · Unordered · No duplicates
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 2 — SET COMPREHENSION  { }")
print(SEP)

# ── Example 9: Unique cities ──────────────────────────────
print("\n[Ex 09] Unique cities")
print(DASH)

cities = ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai"]
unique = {c for c in cities}

print(f"  cities = {cities}")
print(f"  unique = {unique}")
# {'Delhi', 'Mumbai', 'Bangalore'}  — order may vary


# ── Example 10: Unique first letters ─────────────────────
print("\n[Ex 10] Unique first letters of words")
print(DASH)

words   = ["apple", "avocado", "banana", "blueberry"]
letters = {w[0] for w in words}

print(f"  words   = {words}")
print(f"  letters = {letters}")
# {'a', 'b'}


# ── Example 11: Unique word lengths ──────────────────────
print("\n[Ex 11] Unique word lengths")
print(DASH)

words   = ["hi", "hello", "hey", "howdy", "hi"]
lengths = {len(w) for w in words}

print(f"  words   = {words}")
print(f"  lengths = {lengths}")
# {2, 3, 5}


# ── Example 12: Common items between two lists ────────────
print("\n[Ex 12] Common items between two lists")
print(DASH)

a      = [1, 2, 3, 4, 5, 6]
b      = [4, 5, 6, 7, 8, 9]
common = {x for x in a if x in b}

print(f"  a      = {a}")
print(f"  b      = {b}")
print(f"  common = {common}")
# {4, 5, 6}


# ── Example 13: Unique domains from emails ────────────────
print("\n[Ex 13] Unique domain names from emails")
print(DASH)

emails  = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "d@outlook.com"]
domains = {e.split("@")[1] for e in emails}

print(f"  emails  = {emails}")
print(f"  domains = {domains}")
# {'gmail.com', 'yahoo.com', 'outlook.com'}


# ── Example 14: Filter + deduplicate scores ───────────────
print("\n[Ex 14] Filter and deduplicate scores in one shot")
print(DASH)

scores = [45, 82, 60, 91, 38, 82, 60, 74]
high   = {s for s in scores if s >= 60}

print(f"  scores = {scores}")
print(f"  high   = {high}")
# {60, 74, 82, 91}


# ── Example 15: Unique characters excluding spaces ────────
print("\n[Ex 15] Unique characters, excluding spaces")
print(DASH)

sentence = "hello world"
chars    = {ch for ch in sentence if ch != " "}

print(f"  sentence = {sentence!r}")
print(f"  chars    = {chars}")
# {'h', 'e', 'l', 'o', 'w', 'r', 'd'}


# ── Example 16: Unique even squares ──────────────────────
print("\n[Ex 16] Unique even squares")
print(DASH)

nums   = [1, 2, 3, 4, 5, 4, 3, 2, 1]
result = {x**2 for x in nums if x % 2 == 0}

print(f"  nums   = {nums}")
print(f"  result = {result}")
# {4, 16}


# ─────────────────────────────────────────────────────────
#  SECTION 3 — DICT COMPREHENSION  { k:v }
#  Returns: dict · Key-value pairs
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 3 — DICT COMPREHENSION  { k:v }")
print(SEP)

# ── Example 17: Zip two lists into a dict ─────────────────
print("\n[Ex 17] Zip two lists into a dict")
print(DASH)

names  = ["Rajeev", "Priya", "Arun"]
scores = [82, 91, 74]
result = {n: s for n, s in zip(names, scores)}

print(f"  result = {result}")
# {'Rajeev': 82, 'Priya': 91, 'Arun': 74}


# ── Example 18: Invert a dict ─────────────────────────────
print("\n[Ex 18] Invert a dict  (swap key ↔ value)")
print(DASH)

original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

print(f"  original = {original}")
print(f"  inverted = {inverted}")
# {1: 'a', 2: 'b', 3: 'c'}


# ── Example 19: Filter dict — keep high scorers ───────────
print("\n[Ex 19] Filter dict — keep high scorers only")
print(DASH)

data    = {"Rajeev": 82, "Priya": 45, "Arun": 91, "Meena": 38}
toppers = {k: v for k, v in data.items() if v >= 60}

print(f"  data    = {data}")
print(f"  toppers = {toppers}")
# {'Rajeev': 82, 'Arun': 91}


# ── Example 20: Word frequency count ─────────────────────
print("\n[Ex 20] Word frequency count")
print(DASH)

words = ["hi", "hello", "hi", "hey", "hello", "hi"]
freq  = {w: words.count(w) for w in set(words)}

print(f"  words = {words}")
print(f"  freq  = {freq}")
# {'hi': 3, 'hello': 2, 'hey': 1}


# ── Example 21: Square lookup table ──────────────────────
print("\n[Ex 21] Square lookup table")
print(DASH)

lookup = {x: x**2 for x in range(1, 6)}

print(f"  lookup = {lookup}")
print(f"  lookup[4] = {lookup[4]}")
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ── Example 22: ASCII value of each character ────────────
print("\n[Ex 22] ASCII value of each character in a string")
print(DASH)

text  = "hello"
ascii = {ch: ord(ch) for ch in text}

print(f"  text  = {text!r}")
print(f"  ascii = {ascii}")
# {'h': 104, 'e': 101, 'l': 108, 'o': 111}
# Note: duplicate 'l' maps to same value — last one wins


# ── Example 23: Grade classification (A / B / C) ─────────
print("\n[Ex 23] Grade classification  A / B / C")
print(DASH)

scores = {"Rajeev": 82, "Priya": 45, "Arun": 91, "Meena": 67}
grades = {
    k: "A" if v >= 80 else "B" if v >= 60 else "C"
    for k, v in scores.items()
}

print(f"  scores = {scores}")
print(f"  grades = {grades}")
# {'Rajeev': 'A', 'Priya': 'C', 'Arun': 'A', 'Meena': 'B'}


# ── Example 24: Apply overrides on top of defaults ────────
print("\n[Ex 24] Config defaults + user overrides")
print(DASH)

defaults  = {"theme": "light", "lang": "en", "timeout": 30}
overrides = {"theme": "dark"}
merged    = {k: overrides.get(k, v) for k, v in defaults.items()}

print(f"  defaults  = {defaults}")
print(f"  overrides = {overrides}")
print(f"  merged    = {merged}")
# {'theme': 'dark', 'lang': 'en', 'timeout': 30}


# ─────────────────────────────────────────────────────────
#  SECTION 4 — GENERATOR EXPRESSION  ( )
#  Returns: generator · Lazy · Memory-efficient
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 4 — GENERATOR EXPRESSION  ( )")
print(SEP)

# ── Example 25: Sum of squares — large range ──────────────
print("\n[Ex 25] Sum of squares — large range, no list in memory")
print(DASH)

total = sum(x**2 for x in range(1_000_000))

print(f"  sum(x**2 for x in range(1_000_000)) = {total}")
# 333332833333500000


# ── Example 26: Find first match with next() ─────────────
print("\n[Ex 26] Find first item > 8 using next()")
print(DASH)

nums  = [3, 7, 2, 9, 4, 11, 6]
first = next(x for x in nums if x > 8)

print(f"  nums  = {nums}")
print(f"  first item > 8 = {first}")
# 9  — stops immediately, doesn't scan the rest


# ── Example 27: any() — short-circuit check ───────────────
print("\n[Ex 27] any() — does at least one score pass?")
print(DASH)

scores = [45, 38, 29, 52, 61]
passed = any(s >= 60 for s in scores)

print(f"  scores = {scores}")
print(f"  any >= 60 = {passed}")
# True  — stops as soon as 61 is found


# ── Example 28: all() — short-circuit check ───────────────
print("\n[Ex 28] all() — do all scores pass?")
print(DASH)

scores = [75, 82, 91, 68]
all_ok = all(s >= 60 for s in scores)

print(f"  scores = {scores}")
print(f"  all >= 60 = {all_ok}")
# True


# ── Example 29: max() without building a list ─────────────
print("\n[Ex 29] max() score without building an intermediate list")
print(DASH)

students = [
    {"name": "Rajeev", "score": 82},
    {"name": "Priya",  "score": 91},
    {"name": "Arun",   "score": 74},
]
top = max(s["score"] for s in students)

print(f"  top score = {top}")
# 91


# ── Example 30: Lazy file line reader ────────────────────
print("\n[Ex 30] Lazy file reader — one line at a time")
print(DASH)

# writing a temp file to demo
with open("/tmp/demo.txt", "w") as f:
    f.write("  Rajeev\n\nPriya  \n   \nArun\n")

lines = (line.strip() for line in open("/tmp/demo.txt") if line.strip())

print("  Lines read lazily:")
for line in lines:
    print(f"    {line!r}")
# 'Rajeev'
# 'Priya'
# 'Arun'


# ── Example 31: islice — take first N from huge sequence ──
print("\n[Ex 31] islice — first 5 even numbers from huge range")
print(DASH)

evens  = (x for x in range(10**9) if x % 2 == 0)
first5 = list(islice(evens, 5))

print(f"  first5 = {first5}")
# [0, 2, 4, 6, 8]
# range(10**9) never fully iterated — generator is lazy


# ── Example 32: Chained generator pipeline ───────────────
print("\n[Ex 32] Chained generator pipeline — strip → filter → collect")
print(DASH)

raw       = ["  Rajeev  ", "", "  Priya", "   ", "Arun  "]
cleaned   = (s.strip() for s in raw)           # stage 1: strip
non_empty = (s for s in cleaned if s)          # stage 2: filter blanks
result    = list(non_empty)                    # stage 3: materialise

print(f"  raw    = {raw}")
print(f"  result = {result}")
# ['Rajeev', 'Priya', 'Arun']
# Nothing runs until list() is called — fully lazy pipeline


print(f"\n{SEP}")
print("  All 32 examples complete.")
print(f"  github.com/reachsatyavs/python-tutorials")
print(SEP)
