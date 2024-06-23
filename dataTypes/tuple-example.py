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
