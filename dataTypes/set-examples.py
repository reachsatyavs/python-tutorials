# set-example.py
# Demonstrating Python SET data type

# Creating a set
basic_set = {1, 2, 3, 3, 4}
print(basic_set)  # duplicates removed

# Adding elements
basic_set.add(5)
print(basic_set)

# Removing elements
basic_set.remove(2)
print(basic_set)

# Discard (no error if element not present)
basic_set.discard(999)
print(basic_set)

# Membership test (very fast)
print(3 in basic_set)
print(10 in basic_set)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# Removing duplicates from list using set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

# Unique words in a sentence
sentence = "python is fun and python is powerful"
unique_words = set(sentence.split())
print(unique_words)

# ------------------------------
# 10 MORE SET EXAMPLES
# ------------------------------

# 11) Create set from an iterable
s = set(["a", "b", "a", "c"])
print(s)

# 12) Update set with multiple values
s.update(["d", "e"])
print(s)

# 13) remove vs discard difference
x = {1, 2, 3}
# x.remove(99)  # would raise KeyError
x.discard(99)   # safe
print(x)

# 14) pop(): removes and returns an arbitrary element
vals = {"red", "green", "blue"}
removed = vals.pop()
print("popped:", removed)
print("remaining:", vals)

# 15) issubset / issuperset
small = {1, 2}
big = {1, 2, 3, 4}
print(small.issubset(big))
print(big.issuperset(small))

# 16) isdisjoint: no common elements
print({1, 2}.isdisjoint({3, 4}))
print({1, 2}.isdisjoint({2, 3}))

# 17) Set comprehension
squares = {x * x for x in range(1, 6)}
print(squares)

# 18) Deduplicate while preserving order (using seen set)
items = ["a", "b", "a", "c", "b", "d"]
seen = set()
ordered_unique = []
for item in items:
    if item not in seen:
        seen.add(item)
        ordered_unique.append(item)
print(ordered_unique)

# 19) Find duplicates using a set
nums = [1, 2, 2, 3, 3, 3, 4]
seen = set()
dups = set()
for n in nums:
    if n in seen:
        dups.add(n)
    else:
        seen.add(n)
print("duplicates:", dups)

# 20) Use frozenset for immutable set (hashable)
fs = frozenset([1, 2, 2, 3])
print(fs)
# can be used as a dict key
mapping = {fs: "immutable set key"}
print(mapping[fs])
