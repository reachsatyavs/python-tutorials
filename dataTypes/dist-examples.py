# dict-example.py
# Demonstrating Python DICTIONARY (dict) data type

# Creating a dictionary
user = {
    "name": "Sathya",
    "city": "Mysore",
    "age": 40
}
print(user)

# Accessing values
print(user["name"])
print(user.get("city"))

# Adding / updating values
user["role"] = "Engineer"
user["age"] = 41
print(user)

# Removing a key
del user["city"]
print(user)

# Iterating over dictionary
for key, value in user.items():
    print(key, "=>", value)

# Dictionary comprehension
squares = {x: x * x for x in range(1, 6)}
print(squares)

# Counting frequency using dict
word = "banana"
frequency = {}
for ch in word:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)

# Nested dictionary
config = {
    "db": {"host": "localhost", "port": 5432},
    "features": {"new_ui": True}
}
print(config["db"]["host"])

# Tuple as dictionary key
coordinates = {
    (0, 0): "Origin",
    (1, 1): "Point C"
}
print(coordinates[(1, 1)])

# ------------------------------
# 10 MORE DICT EXAMPLES
# ------------------------------

# 11) Create dict using dict() constructor
employee = dict(name="Ravi", dept="QA", level=3)
print(employee)

# 12) Update multiple keys at once
employee.update({"level": 4, "location": "Bengaluru"})
print(employee)

# 13) pop() removes a key and returns its value
level = employee.pop("level")
print("popped level:", level)
print(employee)

# 14) popitem() removes and returns the last inserted (Python 3.7+ keeps insertion order)
last_kv = employee.popitem()
print("popitem:", last_kv)
print(employee)

# 15) setdefault(): get existing value or insert default
settings = {"timeout": 30}
print(settings.setdefault("timeout", 10))  # existing
print(settings.setdefault("retries", 3))   # inserted
print(settings)

# 16) Merge dictionaries (Python 3.9+)
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}
merged = a | b
print(merged)  # y overwritten by b

# 17) Merge in-place
c = {"env": "dev"}
c |= {"region": "in-south-1"}
print(c)

# 18) Invert a dict (value->key) when values are unique
code_to_name = {"IN": "India", "US": "USA"}
name_to_code = {v: k for k, v in code_to_name.items()}
print(name_to_code)

# 19) Group items by a key
people = [
    {"name": "A", "team": "X"},
    {"name": "B", "team": "Y"},
    {"name": "C", "team": "X"},
]
by_team = {}
for p in people:
    by_team.setdefault(p["team"], []).append(p["name"])
print(by_team)

# 20) Build a simple cache (memoization)
cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        cache[n] = n
    else:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

print(fib(10))
print(cache)
