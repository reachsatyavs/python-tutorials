"""
Python Modules & pip — 12 Runnable Examples
Module 09 · python-tutorials

Run from this folder:  python3 modules_examples.py
All examples use the Python standard library + the local myutils.py module.
"""

SEP = "─" * 60

def section(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)


# ──────────────────────────────────────────────────────────
# Example 01 — import math  (basic namespace import)
# ──────────────────────────────────────────────────────────
section("01 — import math  (access via math.name)")

import math

print(f"  math.sqrt(144)     = {math.sqrt(144)}")
print(f"  math.pi            = {math.pi:.6f}")
print(f"  math.floor(3.99)   = {math.floor(3.99)}")
print(f"  math.ceil(3.01)    = {math.ceil(3.01)}")
print(f"  math.log(100, 10)  = {math.log(100, 10)}")
print(f"  math.gcd(48, 36)   = {math.gcd(48, 36)}")
print(f"  math.factorial(6)  = {math.factorial(6)}")


# ──────────────────────────────────────────────────────────
# Example 02 — from module import name  (selective import)
# ──────────────────────────────────────────────────────────
section("02 — from module import name  (no prefix needed)")

from datetime import date, datetime, timedelta

today     = date.today()
yesterday = today - timedelta(days=1)
next_week = today + timedelta(weeks=1)

print(f"  Today      : {today}")
print(f"  Yesterday  : {yesterday}")
print(f"  Next week  : {next_week}")
print(f"  Weekday    : {today.strftime('%A')}")

now = datetime.now()
print(f"  Now        : {now.strftime('%Y-%m-%d %H:%M:%S')}")


# ──────────────────────────────────────────────────────────
# Example 03 — import module as alias
# ──────────────────────────────────────────────────────────
section("03 — import module as alias  (short name)")

import random as rnd

rnd.seed(42)    # fix seed for reproducibility
print(f"  Random int (1-10)   : {rnd.randint(1, 10)}")
print(f"  Random float (0-1)  : {rnd.random():.4f}")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"  Random choice       : {rnd.choice(fruits)}")

rnd.shuffle(fruits)
print(f"  Shuffled list       : {fruits}")

sample = rnd.sample(range(1, 50), 6)
print(f"  Lottery numbers     : {sorted(sample)}")


# ──────────────────────────────────────────────────────────
# Example 04 — os module — file system operations
# ──────────────────────────────────────────────────────────
section("04 — os module  (file system and environment)")

import os

print(f"  Current dir     : {os.getcwd()}")
print(f"  Path separator  : repr={repr(os.sep)}")
print(f"  Line separator  : repr={repr(os.linesep)}")

# environment variables
home = os.environ.get("HOME", "not set")
print(f"  HOME            : {home}")
user = os.environ.get("USER", os.environ.get("USERNAME", "unknown"))
print(f"  USER            : {user}")

# list current directory
entries = os.listdir(".")
print(f"  Items in folder : {len(entries)}")


# ──────────────────────────────────────────────────────────
# Example 05 — sys module — interpreter info
# ──────────────────────────────────────────────────────────
section("05 — sys module  (Python interpreter info)")

import sys

print(f"  Python version  : {sys.version.split()[0]}")
print(f"  Platform        : {sys.platform}")
print(f"  Executable      : {sys.executable}")
print(f"  sys.path[:2]    : {sys.path[:2]}")


# ──────────────────────────────────────────────────────────
# Example 06 — collections module
# ──────────────────────────────────────────────────────────
section("06 — collections — Counter, defaultdict, deque, namedtuple")

from collections import Counter, defaultdict, deque, namedtuple

# Counter — count occurrences
words   = "the cat sat on the mat the cat ate the rat".split()
counts  = Counter(words)
print(f"  Counter         : {counts}")
print(f"  Most common 3   : {counts.most_common(3)}")

# defaultdict — dict with a default factory
dd = defaultdict(list)
for word in words:
    dd[word[0]].append(word)    # group words by first letter
print(f"  Words starting 't': {dd['t']}")

# deque — fast append/pop from both ends
dq = deque([1, 2, 3], maxlen=5)
dq.appendleft(0)
dq.append(4)
dq.append(5)    # maxlen=5, so 1 is dropped from the left
print(f"  Deque (maxlen=5): {list(dq)}")

# namedtuple — tuple with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"  Point           : {p}")
print(f"  Distance from 0 : {math.hypot(p.x, p.y):.2f}")


# ──────────────────────────────────────────────────────────
# Example 07 — itertools module
# ──────────────────────────────────────────────────────────
section("07 — itertools — chain, combinations, product, islice")

import itertools

# chain — flatten iterables
nums    = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print(f"  chain           : {nums}")

# combinations — choose r items (no repetition, order doesn't matter)
combos  = list(itertools.combinations("ABCD", 2))
print(f"  combinations('ABCD',2): {combos}")

# permutations — ordered arrangements
perms   = list(itertools.permutations([1, 2, 3]))
print(f"  permutations([1,2,3])  : {perms}")

# product — cartesian product (like nested for loops)
grid    = list(itertools.product([0, 1], repeat=2))
print(f"  product([0,1], r=2)    : {grid}")

# islice — take the first n items from any iterator (lazy)
evens   = itertools.count(0, 2)    # 0, 2, 4, 6, ... (infinite)
first10 = list(itertools.islice(evens, 10))
print(f"  First 10 even numbers  : {first10}")


# ──────────────────────────────────────────────────────────
# Example 08 — functools module
# ──────────────────────────────────────────────────────────
section("08 — functools — reduce, lru_cache, partial")

from functools import reduce, lru_cache, partial

# reduce
product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print(f"  reduce (product 1-5) : {product}")

# lru_cache — memoize expensive function calls
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"  fibonacci(30)        : {fibonacci(30)}")
print(f"  fibonacci(40)        : {fibonacci(40)}")
print(f"  lru_cache info       : {fibonacci.cache_info()}")

# partial — fix some arguments of a function
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)
print(f"  square(7)            : {square(7)}")
print(f"  cube(4)              : {cube(4)}")


# ──────────────────────────────────────────────────────────
# Example 09 — Your own module — import myutils
# ──────────────────────────────────────────────────────────
section("09 — Your own module  (import myutils)")

import myutils

print(f"  greet()          : {myutils.greet('Alice')}")
print(f"  circle_area(5)   : {myutils.circle_area(5):.4f}")
print(f"  clamp(150,0,100) : {myutils.clamp(150, 0, 100)}")
print(f"  clamp(-10,0,100) : {myutils.clamp(-10, 0, 100)}")
print(f"  is_palindrome('racecar')    : {myutils.is_palindrome('racecar')}")
print(f"  is_palindrome('A man a plan a canal Panama'): "
      f"{myutils.is_palindrome('A man a plan a canal Panama')}")
print(f"  Module constant PI : {myutils.PI}")


# ──────────────────────────────────────────────────────────
# Example 10 — from myutils import  (selective import)
# ──────────────────────────────────────────────────────────
section("10 — from myutils import  (selective, no prefix needed)")

from myutils import greet, clamp, is_palindrome

names = ["Charlie", "Dave", "Eve"]
for name in names:
    print(f"  {greet(name)}")

values = [200, -50, 75, 101, 0]
for v in values:
    print(f"  clamp({v:4d}, 0, 100) = {clamp(v, 0, 100)}")

words2 = ["level", "python", "radar", "world", "civic"]
for w in words2:
    print(f"  is_palindrome('{w}') = {is_palindrome(w)}")


# ──────────────────────────────────────────────────────────
# Example 11 — __name__ guard explained
# ──────────────────────────────────────────────────────────
section("11 — __name__ explained  (module identity)")

print(f"  __name__ in this script : '{__name__}'")
print(f"  (When run directly, __name__ is '__main__')")
print(f"  (When imported, __name__ would be the module's filename)")
print()

# Show that imported modules have a different __name__
print(f"  math.__name__     : '{math.__name__}'")
print(f"  myutils.__name__  : '{myutils.__name__}'")
print(f"  random.__name__   : '{rnd.__name__}'")


# ──────────────────────────────────────────────────────────
# Example 12 — uuid, pprint, string  (quick utility modules)
# ──────────────────────────────────────────────────────────
section("12 — uuid, pprint, string  (useful utilities)")

import uuid
import pprint
import string

# uuid — universally unique identifier
user_id = uuid.uuid4()
print(f"  UUID v4 : {user_id}")
print(f"  Type    : {type(user_id)}")

# pprint — pretty-print nested structures
data = {
    "users": [
        {"name": "Alice", "scores": [90, 85, 92], "active": True},
        {"name": "Bob",   "scores": [75, 80, 78], "active": False},
    ],
    "total": 2,
    "course": "Python Fundamentals"
}
print("\n  pprint output:")
pprint.pprint(data, indent=4, width=60)

# string constants
print(f"\n  string.ascii_lowercase : {string.ascii_lowercase}")
print(f"  string.digits          : {string.digits}")
print(f"  string.punctuation     : {string.punctuation}")

# Build a random password using string + random
import random as r
alphabet = string.ascii_letters + string.digits + "!@#$%"
password = "".join(r.choices(alphabet, k=12))
print(f"\n  Random password (12 chars): {password}")


print(f"\n{SEP}")
print("  All 12 examples complete.")
print(SEP)
