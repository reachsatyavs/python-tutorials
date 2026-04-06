# set-examples.py
# Demonstrating Python SET (and frozenset) data type
#
# -----------------------------------------------------------------------------
# Set instance methods & operators
# -----------------------------------------------------------------------------
#   add                         — add one element
#   clear                       — remove all elements
#   copy                        — shallow copy of the set
#   difference (- or .difference)           — elements in self not in other
#   difference_update (-= or .difference_update)
#   discard                     — remove if present (no error if missing)
#   intersection (& or .intersection)     — common elements
#   intersection_update (&= or .intersection_update)
#   isdisjoint                  — True if no common elements
#   issubset (<= or .issubset)             — self contained in other
#   issuperset (>= or .issuperset)         — self contains other
#   pop                         — remove and return arbitrary element
#   remove                      — remove element (KeyError if missing)
#   symmetric_difference (^ or .symmetric_difference)
#   symmetric_difference_update (^= or .symmetric_difference_update)
#   union (| or .union)                   — all elements from both
#   update (|= or .update)               — add all from iterable(s)
#
# Constructors: set(), frozenset()
# -----------------------------------------------------------------------------

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

# Set operations (operators)
a = {1, 2, 3}
b = {3, 4, 5}

print("Union |:", a | b)
print("Intersection &:", a & b)
print("Difference -:", a - b)
print("Symmetric Difference ^:", a ^ b)

# Same operations via methods: union, intersection, difference, symmetric_difference
print("union():", a.union(b))
print("intersection():", a.intersection(b))
print("difference():", a.difference(b))
print("symmetric_difference():", a.symmetric_difference(b))

# copy() and clear()
s_copy_demo = {1, 2, 3}
backup = s_copy_demo.copy()
s_copy_demo.clear()
print("after clear:", s_copy_demo, "backup:", backup)

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

# 12) Update set with multiple values (.update or |=)
s.update(["d", "e"])
print(s)
s |= {"x", "y"}  # same idea as update with another set
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

# 21) difference_update / intersection_update (in-place)
left = {1, 2, 3, 4}
left.difference_update({2, 99})
print("after difference_update:", left)

right = {1, 2, 3}
right.intersection_update({2, 3, 4})
print("after intersection_update:", right)

# 22) symmetric_difference_update (in-place)
u = {1, 2, 3}
u.symmetric_difference_update({3, 4, 5})
print("after symmetric_difference_update:", u)
