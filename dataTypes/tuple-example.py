# Creating a tuple with different data types
basic_tuple = (1, "hello", 3.14, True)
print(basic_tuple)  # Output: (1, 'hello', 3.14, True)


# Accessing elements by index
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # Output: 10
print(my_tuple[2])  # Output: 30
print(my_tuple[-1]) # Output: 50


# Slicing a tuple
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_tuple[:3])   # Output: (10, 20, 30)
print(my_tuple[3:])   # Output: (40, 50)


# Creating a nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)       # Output: (1, (2, 3), (4, 5, 6))
print(nested_tuple[1])    # Output: (2, 3)
print(nested_tuple[2][1]) # Output: 5


# Unpacking a tuple
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30

# Creating a single element tuple (note the comma)
single_element_tuple = (10,)
print(single_element_tuple)  # Output: (10,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

# Without the comma, it is not a tuple
not_a_tuple = (10)
print(type(not_a_tuple))  # Output: <class 'int'>


# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repeating elements in a tuple
my_tuple = (1, 2, 3)
multiplied_tuple = my_tuple * 3
print(multiplied_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Using tuples as dictionary keys
coordinates = {
    (0, 0): "Origin",
    (1, 0): "Point A",
    (0, 1): "Point B",
    (1, 1): "Point C"
}
print(coordinates[(0, 0)])  # Output: Origin
print(coordinates[(1, 1)])  # Output: Point C


# Using tuple methods
my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2))  # Output: 3 (number of times 2 appears in the tuple)
print(my_tuple.index(3))  # Output: 2 (index of the first occurrence of 3)


# Demonstrating immutability of tuples
immutable_tuple = (1, 2, 3)
try:
    immutable_tuple[0] = 10
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment

# ------------------------------
# BASIC TUPLE EXAMPLES
# ------------------------------

# 1) Creating a tuple with different data types
basic_tuple = (1, "hello", 3.14, True)
print(basic_tuple)

# 2) Accessing elements by index
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1])

# 3) Slicing a tuple
print(my_tuple[1:4])
print(my_tuple[:3])
print(my_tuple[3:])

# 4) Nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)
print(nested_tuple[1])
print(nested_tuple[2][1])

# 5) Tuple unpacking
a, b, c = (10, 20, 30)
print(a, b, c)

# 6) Single-element tuple
single = (10,)
print(single)
print(type(single))

# 7) Not a tuple (no comma)
not_tuple = (10)
print(type(not_tuple))

# 8) Tuple concatenation
t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2)

# 9) Tuple repetition
print(t2 * 3)

# 10) Tuple as dictionary key
points = {(0, 0): "origin", (1, 1): "diagonal"}
print(points[(0, 0)])

# ------------------------------
# ADVANCED / ADDITIONAL TUPLE EXAMPLES
# ------------------------------

# 11) Tuple with mutable element (list inside tuple)
t = (1, [2, 3], 4)
t[1].append(99)
print(t)

# 12) Tuple immutability demonstration
immutable = (1, 2, 3)
try:
    immutable[0] = 100
except TypeError as e:
    print(e)

# 13) Tuple count() method
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))

# 14) Tuple index() method
print(t.index(3))

# 15) Returning multiple values from a function
def calculate(a, b):
    return a + b, a * b

result = calculate(3, 4)
print(result)

# 16) Unpacking returned tuple
sum_val, product_val = calculate(5, 6)
print(sum_val, product_val)

# 17) Ignoring values using underscore
x, _, z = (10, 20, 30)
print(x, z)

# 18) Extended unpacking
a, *middle, b = (1, 2, 3, 4, 5)
print(a)
print(middle)
print(b)

# 19) Tuple as fixed record
employee = ("E123", "Sathya", "QA", "Mysore")
emp_id, name, role, city = employee
print(name, role)

# 20) Hashable tuple usage (in set)
coords = {(1, 2), (3, 4), (1, 2)}
print(coords)

# 21) Tuple comparison (lexicographical)
print((1, 2, 3) < (1, 2, 4))
print((2, 0) > (1, 9))

# 22) Enumerate with tuples
colors = ("red", "green", "blue")
for index, color in enumerate(colors):
    print(index, color)

# 23) zip() produces tuples
names = ("A", "B", "C")
scores = (90, 80, 85)
for pair in zip(names, scores):
    print(pair)

# 24) Convert list to tuple
numbers = [1, 2, 3, 4]
safe_numbers = tuple(numbers)
print(safe_numbers)

# 25) Tuple as constant configuration
DB_CONFIG = ("localhost", 5432, "appdb")
print(DB_CONFIG)

