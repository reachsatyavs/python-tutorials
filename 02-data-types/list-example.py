# list-example.py
# Demonstrating Python LIST data type
#
# -----------------------------------------------------------------------------
# List instance methods (mutate or inspect the list object)
# -----------------------------------------------------------------------------
#   append    — add one element at the end
#   clear     — remove all elements
#   copy      — shallow copy of the list
#   count     — count occurrences of a value
#   extend    — append all items from an iterable
#   index     — index of first occurrence (optional start/stop)
#   insert    — insert at index
#   pop       — remove and return item at index (default last)
#   remove    — remove first occurrence of value
#   reverse   — reverse list in place
#   sort      — sort list in place (optional key, reverse)
#
# Built-ins commonly used with lists
# -----------------------------------------------------------------------------
#   len, min, max, sum, sorted, reversed, enumerate, list (constructor)
# -----------------------------------------------------------------------------

# Creating a list with different data types
basic_list = [1, "hello", 3.14, True]
print(basic_list)

# Accessing elements by index
my_list = [10, 20, 30, 40, 50]
print(my_list[0])
print(my_list[2])
print(my_list[-1])

# Built-ins: len, min, max, sum
print("len/min/max/sum:", len(my_list), min(my_list), max(my_list), sum(my_list))

# Slicing a list
print(my_list[1:4])
print(my_list[:3])
print(my_list[3:])

# Modifying elements (lists are mutable)
my_list[0] = 100
print(my_list)

# Adding elements
my_list.append(60)
print(my_list)

# Inserting elements
my_list.insert(1, 999)
print(my_list)

# Removing elements
my_list.remove(999)
print(my_list)

# Popping elements
last_element = my_list.pop()
print(last_element, my_list)

# sort (in place) vs sorted() (new list)
to_sort = [3, 1, 4, 1, 5]
to_sort.sort()
print("sort in place:", to_sort)

# clear (remove all items)
cleared_demo = [1, 2, 3]
cleared_demo.clear()
print("after clear:", cleared_demo)

# reversed (built-in iterator)
print("reversed:", list(reversed([1, 2, 3])))

# List comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1][2])  # 6

# list() constructor (copy from iterable)
from_tuple = list((1, 2, 3))
print("list from tuple:", from_tuple)

# enumerate with list
for i, v in enumerate(["a", "b", "c"]):
    print(i, v)

# ------------------------------
# 10 MORE LIST EXAMPLES
# ------------------------------

# 11) Extend (add multiple items at once)
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)

# 12) Combine lists (creates a new list)
b = [10, 20]
c = b + [30, 40]
print(c)

# 13) Copy a list (shallow copy)
orig = [[1, 2], [3, 4]]
shallow = orig.copy()
shallow[0].append(99)
print("orig:", orig)       # inner list shared
print("shallow:", shallow)

# 14) Deep copy (independent nested lists)
import copy
orig2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(orig2)
deep[0].append(99)
print("orig2:", orig2)
print("deep:", deep)

# 15) Reverse (in-place)
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)

# 16) Sorted (returns a new list)
names = ["Zoe", "Ana", "Mohan"]
sorted_names = sorted(names)
print("original:", names)
print("sorted:", sorted_names)

# 17) Find index of an element
letters = ["a", "b", "c", "b"]
print(letters.index("b"))  # first 'b'

# 18) Count occurrences
print(letters.count("b"))

# 19) Join list of strings into one string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)

# 20) Use list as a stack (LIFO)
stack = []
stack.append("task1")
stack.append("task2")
stack.append("task3")
print(stack.pop())  # task3
print(stack)
