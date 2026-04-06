# string-example.py
# Demonstrating Python str (string) type — common methods and patterns
#
# -----------------------------------------------------------------------------
# Case & normalization
# -----------------------------------------------------------------------------
#   lower, upper, capitalize, title, swapcase, casefold
#
# Searching & counting
# -----------------------------------------------------------------------------
#   find, rfind, index, rindex, count, startswith, endswith
#
# Splitting & joining
# -----------------------------------------------------------------------------
#   split, rsplit, splitlines, join (called on separator: " ".join(parts))
#
# Stripping whitespace
# -----------------------------------------------------------------------------
#   strip, lstrip, rstrip
#
# Replacing & splitting on separators
# -----------------------------------------------------------------------------
#   replace, partition, rpartition
#
# Alignment & padding
# -----------------------------------------------------------------------------
#   center, ljust, rjust, zfill
#
# Character-class tests (return True/False)
# -----------------------------------------------------------------------------
#   isalpha, isdigit, isalnum, isspace, islower, isupper, isnumeric, isdecimal
#
# Other useful
# -----------------------------------------------------------------------------
#   encode, format, format_map  (f-strings often replace .format in new code)
# -----------------------------------------------------------------------------

text = "Hello, Python World"
print(text)

# --- Case & normalization ---
print(text.lower())
print(text.upper())
print("hello world".capitalize())
print("hello world".title())
print("Hello".swapcase())
print("Straße".casefold())  # strong lowercase (locale-aware comparisons)

# --- Searching & counting ---
s = "banana"
print(s.find("na"))       # first index or -1
print(s.rfind("na"))      # from the right
print(s.index("na"))      # like find but raises ValueError if missing
print(s.rindex("na"))     # like rfind but raises if missing
print(s.count("na"))
print("file.txt".startswith("file"))
print("file.txt".endswith(".txt"))

# --- split / rsplit / splitlines ---
print("a,b,c".split(","))
print("one  two   three".split())       # default: any whitespace
print("a|b|c".rsplit("|", 1))          # maxsplit from right
print("line1\nline2\r\nline3".splitlines())

# --- join (method on the separator string) ---
words = ["Python", "is", "readable"]
print(" ".join(words))
print("-".join(["2025", "04", "06"]))

# --- strip ---
padded = "  spaced  \n"
print(repr(padded.strip()))
print(repr(">>>value<<<".strip("<>")))

# --- replace, partition ---
print("hello world".replace("world", "Python"))
print("key=value".partition("="))
print("path/to/file.py".rpartition("/"))

# --- alignment ---
print("42".zfill(5))
print("hi".center(10, "-"))
print("left".ljust(10, "."))
print("right".rjust(10, "."))

# --- Character-class tests ---
print("abc".isalpha())
print("123".isdigit())
print("ab12".isalnum())
print("   \t".isspace())
print("hello".islower(), "HELLO".isupper())
print("42".isnumeric(), "42".isdecimal())
print("3.14".isdecimal())  # False: dot is not a decimal digit

# --- encode (bytes) ---
b = "café".encode("utf-8")
print(b, b.decode("utf-8"))

# --- format (positional / named) ---
print("{} + {} = {}".format(2, 3, 5))
print("{name} is {age} years old".format(name="Ada", age=36))

# format_map (expects a mapping, no ** unpacking needed)
print("{user} scored {score}".format_map({"user": "Ada", "score": 100}))

# f-string (preferred in modern Python; same ideas as format)
name, version = "Python", 3
print(f"{name} {version}")

# --- Practical mini-examples ---
csv_line = "apple,5,0.99"
fruit, qty, price = csv_line.split(",")
print(fruit, int(qty), float(price))

slug = "  Some Article Title  ".strip().lower().replace(" ", "-")
print(slug)
