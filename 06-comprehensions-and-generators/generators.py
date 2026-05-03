"""
============================================================
  Python Generators — Complete Guide with Examples
  Module 06 · Generators · github.com/reachsatyavs/python-tutorials
============================================================
  Sections:
    1. What is a Generator?
    2. yield vs return
    3. Generator as Iterator — next()
    4. Generator Expression  ( )
    5. Why Generators? — Memory comparison
    6. Use Case 1 — Large file processing
    7. Use Case 2 — Infinite sequences
    8. Use Case 3 — Data pipelines
    9. Use Case 4 — Pagination / streaming API
   10. Use Case 5 — Fibonacci on demand
   11. send() — Two-way communication
   12. yield from — Delegating generators
============================================================
"""

import sys
import time
from itertools import islice

SEP  = "=" * 55
DASH = "-" * 55


# ─────────────────────────────────────────────────────────
#  SECTION 1 — WHAT IS A GENERATOR?
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 1 — WHAT IS A GENERATOR?")
print(SEP)

print("\n[Ex 01] A function with yield instead of return")
print(DASH)

def simple_gen():
    print("  → step 1")
    yield 10
    print("  → step 2")
    yield 20
    print("  → step 3")
    yield 30

gen = simple_gen()
print(f"  type = {type(gen)}")   # <class 'generator'>

print(f"  next() = {next(gen)}")  # step 1 runs → yields 10
print(f"  next() = {next(gen)}")  # step 2 runs → yields 20
print(f"  next() = {next(gen)}")  # step 3 runs → yields 30


# ─────────────────────────────────────────────────────────
#  SECTION 2 — yield vs return
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 2 — yield vs return")
print(SEP)

print("\n[Ex 02] return — runs fully, returns one value, done")
print(DASH)

def get_numbers_return():
    return [1, 2, 3, 4, 5]   # all built at once

result = get_numbers_return()
print(f"  result = {result}")
print(f"  type   = {type(result)}")


print("\n[Ex 03] yield — pauses, resumes, produces one at a time")
print(DASH)

def get_numbers_yield():
    for i in range(1, 6):
        yield i               # pause here, hand over i, resume later

gen = get_numbers_yield()
print(f"  type = {type(gen)}")
for val in gen:
    print(f"  got: {val}")


# ─────────────────────────────────────────────────────────
#  SECTION 3 — GENERATOR AS ITERATOR — next()
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 3 — GENERATOR AS ITERATOR — next()")
print(SEP)

print("\n[Ex 04] Manual iteration with next() and StopIteration")
print(DASH)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

cd = countdown(3)
print(f"  next() = {next(cd)}")   # 3
print(f"  next() = {next(cd)}")   # 2
print(f"  next() = {next(cd)}")   # 1

try:
    print(f"  next() = {next(cd)}")
except StopIteration:
    print("  StopIteration raised — generator exhausted")


print("\n[Ex 05] for loop handles StopIteration automatically")
print(DASH)

for val in countdown(5):
    print(f"  {val}", end=" ")
print()


# ─────────────────────────────────────────────────────────
#  SECTION 4 — GENERATOR EXPRESSION  ( )
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 4 — GENERATOR EXPRESSION  ( )")
print(SEP)

print("\n[Ex 06] Generator expression vs list comprehension")
print(DASH)

# list — all values built NOW, stored in memory
sq_list = [x**2 for x in range(10)]
print(f"  list      = {sq_list}")
print(f"  list size = {sys.getsizeof(sq_list)} bytes")

# generator — nothing computed yet
sq_gen = (x**2 for x in range(10))
print(f"  generator = {sq_gen}")
print(f"  gen size  = {sys.getsizeof(sq_gen)} bytes")

print(f"\n  Values from generator:")
print(f"  {list(sq_gen)}")


# ─────────────────────────────────────────────────────────
#  SECTION 5 — WHY GENERATORS? — Memory comparison
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 5 — WHY GENERATORS? Memory comparison")
print(SEP)

print("\n[Ex 07] Memory: list vs generator for 1 million items")
print(DASH)

n = 1_000_000

big_list = [x for x in range(n)]
big_gen  = (x for x in range(n))

list_size = sys.getsizeof(big_list)
gen_size  = sys.getsizeof(big_gen)

print(f"  list size : {list_size:,} bytes  ({list_size // 1024 // 1024} MB)")
print(f"  gen  size : {gen_size:,} bytes")
print(f"  gen is {list_size // gen_size}x more memory efficient")


print("\n[Ex 08] Speed: sum with list vs generator")
print(DASH)

t0 = time.perf_counter()
total_list = sum([x**2 for x in range(1_000_000)])
t1 = time.perf_counter()

t2 = time.perf_counter()
total_gen = sum(x**2 for x in range(1_000_000))
t3 = time.perf_counter()

print(f"  list result  = {total_list}  time = {(t1-t0)*1000:.1f}ms")
print(f"  gen  result  = {total_gen}  time = {(t3-t2)*1000:.1f}ms")
print(f"  Both give same answer — generator avoids building the list")


# ─────────────────────────────────────────────────────────
#  SECTION 6 — USE CASE 1: Large file processing
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 6 — USE CASE 1: Large file processing")
print(SEP)

print("\n[Ex 09] Read and process a large file line by line")
print(DASH)

# create a demo file
with open("/tmp/students.txt", "w") as f:
    f.write("Rajeev,82\nPriya,45\nArun,91\nMeena,38\nVijay,74\n")

def read_students(filepath):
    """Yields one student dict at a time — never loads whole file."""
    with open(filepath) as f:
        for line in f:
            name, score = line.strip().split(",")
            yield {"name": name, "score": int(score)}

# process without loading entire file
for student in read_students("/tmp/students.txt"):
    status = "PASS" if student["score"] >= 60 else "FAIL"
    print(f"  {student['name']:10} {student['score']}  {status}")


print("\n[Ex 10] Count lines in large file — zero RAM overhead")
print(DASH)

def line_count(filepath):
    return sum(1 for _ in open(filepath))

count = line_count("/tmp/students.txt")
print(f"  Line count = {count}")
# reads one line at a time — file can be 10GB, memory stays constant


# ─────────────────────────────────────────────────────────
#  SECTION 7 — USE CASE 2: Infinite sequences
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 7 — USE CASE 2: Infinite sequences")
print(SEP)

print("\n[Ex 11] Infinite counter — take only what you need")
print(DASH)

def infinite_counter(start=0, step=1):
    n = start
    while True:         # infinite loop — safe because of yield
        yield n
        n += step

counter = infinite_counter(start=10, step=5)
first6  = [next(counter) for _ in range(6)]
print(f"  first 6 = {first6}")
# [10, 15, 20, 25, 30, 35]


print("\n[Ex 12] Infinite even numbers using islice")
print(DASH)

def evens():
    n = 0
    while True:
        yield n
        n += 2

first10_evens = list(islice(evens(), 10))
print(f"  first 10 evens = {first10_evens}")
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# ─────────────────────────────────────────────────────────
#  SECTION 8 — USE CASE 3: Data pipelines
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 8 — USE CASE 3: Data pipelines")
print(SEP)

print("\n[Ex 13] Lazy pipeline — nothing runs until consumed")
print(DASH)

raw_data = ["  42 ", "hello", " 17", "99", " bad ", "55 ", "abc"]

def parse_numbers(records):
    """Stage 1: strip and keep only numeric strings."""
    for r in records:
        stripped = r.strip()
        if stripped.isdigit():
            yield int(stripped)

def filter_high(numbers, threshold=50):
    """Stage 2: keep only values above threshold."""
    for n in numbers:
        if n > threshold:
            yield n

def double(numbers):
    """Stage 3: double each value."""
    for n in numbers:
        yield n * 2

# chain the pipeline — nothing executes yet
stage1 = parse_numbers(raw_data)
stage2 = filter_high(stage1, threshold=50)
stage3 = double(stage2)

print(f"  raw_data = {raw_data}")
print(f"  pipeline result = {list(stage3)}")
# [198, 110]  — only 99 and 55 survived all stages


# ─────────────────────────────────────────────────────────
#  SECTION 9 — USE CASE 4: Pagination / streaming
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 9 — USE CASE 4: Pagination / streaming")
print(SEP)

print("\n[Ex 14] Paginate a large dataset in chunks")
print(DASH)

def paginate(data, page_size):
    """Yields one page (chunk) at a time."""
    for i in range(0, len(data), page_size):
        yield data[i : i + page_size]

records = list(range(1, 22))   # 21 records

for page_num, page in enumerate(paginate(records, page_size=5), start=1):
    print(f"  Page {page_num}: {page}")
# Page 1: [1, 2, 3, 4, 5]
# Page 2: [6, 7, 8, 9, 10]
# ...


print("\n[Ex 15] Simulate streaming API response")
print(DASH)

def stream_api_results(total, batch_size=3):
    """Simulates fetching results from an API in batches."""
    fetched = 0
    batch   = 1
    while fetched < total:
        chunk = list(range(fetched + 1, min(fetched + batch_size + 1, total + 1)))
        yield chunk
        fetched += len(chunk)
        batch   += 1

for batch in stream_api_results(total=10, batch_size=3):
    print(f"  batch received: {batch}")


# ─────────────────────────────────────────────────────────
#  SECTION 10 — USE CASE 5: Fibonacci on demand
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 10 — USE CASE 5: Fibonacci on demand")
print(SEP)

print("\n[Ex 16] Fibonacci generator — infinite, zero memory waste")
print(DASH)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib    = fibonacci()
first12 = [next(fib) for _ in range(12)]
print(f"  first 12 = {first12}")
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


print("\n[Ex 17] First Fibonacci number exceeding 1000")
print(DASH)

fib   = fibonacci()
large = next(f for f in fib if f > 1000)
print(f"  first Fibonacci > 1000 = {large}")
# 1597


# ─────────────────────────────────────────────────────────
#  SECTION 11 — send() — Two-way communication
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 11 — send() — Two-way communication")
print(SEP)

print("\n[Ex 18] send() — pass a value INTO a running generator")
print(DASH)

def running_total():
    total = 0
    while True:
        value = yield total   # yield sends total OUT, receives value IN
        if value is None:
            break
        total += value

rt = running_total()
next(rt)                          # prime the generator (required first step)
print(f"  send(10) → {rt.send(10)}")   # total = 10
print(f"  send(25) → {rt.send(25)}")   # total = 35
print(f"  send(15) → {rt.send(15)}")   # total = 50


# ─────────────────────────────────────────────────────────
#  SECTION 12 — yield from — Delegating generators
# ─────────────────────────────────────────────────────────
print(f"\n{SEP}")
print("  SECTION 12 — yield from — Delegating generators")
print(SEP)

print("\n[Ex 19] yield from — delegate to a sub-generator")
print(DASH)

def inner():
    yield "A"
    yield "B"
    yield "C"

def outer():
    yield "start"
    yield from inner()     # delegate to inner — no manual loop needed
    yield "end"

print(f"  result = {list(outer())}")
# ['start', 'A', 'B', 'C', 'end']


print("\n[Ex 20] yield from — flatten nested lists elegantly")
print(DASH)

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # recursive delegation
        else:
            yield item

data   = [1, [2, 3], [4, [5, 6]], 7]
result = list(flatten(data))
print(f"  data   = {data}")
print(f"  result = {result}")
# [1, 2, 3, 4, 5, 6, 7]


print(f"\n{SEP}")
print("  All 20 generator examples complete.")
print(f"  github.com/reachsatyavs/python-tutorials")
print(SEP)
