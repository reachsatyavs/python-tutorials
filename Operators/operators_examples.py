"""
operators_examples.py
=====================
Runnable examples for every Python operator category.
Run with:  python operators_examples.py
"""

# ---------------------------------------------------------------------------
# Helper: section header
# ---------------------------------------------------------------------------
def section(title: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {title}")
    print('=' * 55)


# ===========================================================================
# 1. ARITHMETIC OPERATORS  (+  -  *  /  //  %  **)
# ===========================================================================
section("1. ARITHMETIC OPERATORS")

# --- Example 1: basic math ---
a, b = 15, 4
print("a =", a, "  b =", b)
print("a + b  =", a + b)   # 19
print("a - b  =", a - b)   # 11
print("a * b  =", a * b)   # 60

# --- Example 2: true division vs floor division ---
print("\nTrue division  15 / 4  =", 15 / 4)    # 3.75 (always float)
print("Floor division 15 // 4 =", 15 // 4)   # 3   (rounds toward -∞)
print("Floor division -15 // 4=", -15 // 4)  # -4  (not -3 !)

# --- Example 3: modulus and exponentiation ---
print("\n15 % 4  =", 15 % 4)   # 3   (remainder)
print("2 ** 10 =", 2 ** 10)   # 1024
print("Is 15 divisible by 3?", 15 % 3 == 0)  # True


# ===========================================================================
# 2. COMPARISON (RELATIONAL) OPERATORS  (==  !=  >  <  >=  <=)
# ===========================================================================
section("2. COMPARISON OPERATORS")

# --- Example 1: numeric comparison ---
age = 20
print("age =", age)
print("age >= 18 →", age >= 18)   # True
print("age == 21 →", age == 21)   # False
print("age != 18 →", age != 18)   # True

# --- Example 2: chained comparison (Python-exclusive syntax) ---
score = 75
print("\nscore =", score)
print("50 < score < 100  →", 50 < score < 100)   # True
print("80 <= score <= 90 →", 80 <= score <= 90)   # False

# --- Example 3: string lexicographic comparison ---
print("\n'apple' < 'banana' →", "apple" < "banana")   # True
print("'zebra' > 'ant'   →", "zebra" > "ant")         # True
print("'Cat' == 'cat'    →", "Cat" == "cat")           # False (case-sensitive)


# ===========================================================================
# 3. LOGICAL OPERATORS  (and  or  not)
# ===========================================================================
section("3. LOGICAL OPERATORS  (binary: and, or | unary: not)")

# --- Example 1: access control (and) ---
is_logged_in = True
has_permission = False
print("is_logged_in:", is_logged_in, " has_permission:", has_permission)
print("is_logged_in and has_permission →", is_logged_in and has_permission)  # False

# --- Example 2: fallback value (or) ---
username = ""
display_name = username or "Guest"
print("\nusername = ''")
print("username or 'Guest' →", display_name)   # Guest (short-circuit)

config_host = "192.168.1.1"
resolved = config_host or "localhost"
print("config_host or 'localhost' →", resolved)  # 192.168.1.1

# --- Example 3: negation (not) ---
is_raining = False
print("\nis_raining:", is_raining)
print("not is_raining  →", not is_raining)              # True
print("not (5 > 3 and 2 < 1) →", not (5 > 3 and 2 < 1))  # True


# ===========================================================================
# 4. ASSIGNMENT OPERATORS  (=  +=  -=  *=  /=  //=  %=  **=)
# ===========================================================================
section("4. ASSIGNMENT OPERATORS")

# --- Example 1: accumulate a total with += ---
total = 0
prices = [10, 25, 5, 40]
for price in prices:
    total += price
print("prices:", prices)
print("total (+=) =", total)   # 80

# --- Example 2: countdown with -= ---
lives = 3
print("\nlives =", lives)
lives -= 1
print("After lives -= 1 →", lives)   # 2
lives -= 1
print("After lives -= 1 →", lives)   # 1

# --- Example 3: compound operators chained ---
n = 3
print("\nn =", n)
n *= 4   # 12
print("n *= 4 →", n)
n //= 5  # 2
print("n //= 5 →", n)
n **= 3  # 8
print("n **= 3 →", n)


# ===========================================================================
# 5. BITWISE OPERATORS  (&  |  ^  ~  <<  >>)
# ===========================================================================
section("5. BITWISE OPERATORS  (binary: & | ^ << >> | unary: ~)")

# --- Example 1: AND, OR, XOR ---
a = 0b1010   # 10
b = 0b1100   # 12
print(f"a = {a}  ({bin(a)})   b = {b}  ({bin(b)})")
print(f"a & b  = {a & b}  ({bin(a & b)})   ← AND (bits set in both)")
print(f"a | b  = {a | b}  ({bin(a | b)})  ← OR  (bits set in either)")
print(f"a ^ b  = {a ^ b}   ({bin(a ^ b)})   ← XOR (bits differ)")

# --- Example 2: left and right shift ---
n = 4   # 0b0100
print(f"\nn = {n}  ({bin(n)})")
print(f"n << 2 = {n << 2}  (multiply by 4)")
print(f"n >> 1 = {n >> 1}   (divide by 2)")

# --- Example 3: bitwise NOT (unary ~) ---
x = 5
print(f"\n~5  = {~x}   (formula: -(n+1))")
print(f"~0  = {~0}")
print(f"~-1 = {~-1}")


# ===========================================================================
# 6. IDENTITY OPERATORS  (is  is not)
# ===========================================================================
section("6. IDENTITY OPERATORS  (binary)")

# --- Example 1: None check ---
result = None
print("result is None    →", result is None)      # True
print("result is not None →", result is not None)  # False

# --- Example 2: CPython small-int cache (-5 to 256) ---
x = 100; y = 100
print(f"\nx = 100, y = 100  →  x is y: {x is y}")   # True  (cached)

a = 1000; b = 1000
print(f"a = 1000, b = 1000 →  a is b: {a is b}")    # False (not cached)

# --- Example 3: list identity vs equality ---
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"\nlist1 == list2  →  {list1 == list2}")   # True  (same values)
print(f"list1 is list2  →  {list1 is list2}")    # False (different objects)
print(f"list1 is list3  →  {list1 is list3}")    # True  (same object / alias)


# ===========================================================================
# 7. MEMBERSHIP OPERATORS  (in  not in)
# ===========================================================================
section("7. MEMBERSHIP OPERATORS  (binary)")

# --- Example 1: list membership ---
fruits = ["apple", "banana", "cherry"]
print("fruits:", fruits)
print("'banana' in fruits     →", "banana" in fruits)    # True
print("'grape' not in fruits  →", "grape" not in fruits)  # True

# --- Example 2: substring check in a string ---
sentence = "Python is awesome"
print(f"\nsentence: '{sentence}'")
print("'awesome' in sentence  →", "awesome" in sentence)    # True
print("'Java' not in sentence →", "Java" not in sentence)   # True

# --- Example 3: dictionary key check ---
config = {"host": "localhost", "port": 8080}
print("\nconfig:", config)
print("'port' in config      →", "port" in config)       # True  (keys)
print("'timeout' in config   →", "timeout" in config)    # False
print("8080 in config.values() →", 8080 in config.values())  # True


# ===========================================================================
# 8. TERNARY OPERATOR  (value_if_true  if  condition  else  value_if_false)
#    The ONLY operator in Python that takes THREE operands.
# ===========================================================================
section("8. TERNARY (CONDITIONAL) OPERATOR  — 3 operands")

# --- Example 1: even / odd label ---
n = 7
label = "even" if n % 2 == 0 else "odd"
print(f"n = {n}  →  '{label}'")   # odd

# --- Example 2: default / fallback value ---
name = ""
display = name if name else "Anonymous"
print(f"name = ''  →  display = '{display}'")   # Anonymous

# --- Example 3: nested ternary for grade bands ---
score = 82
grade = "A" if score >= 90 else "B" if score >= 75 else "C"
print(f"score = {score}  →  grade = '{grade}'")   # B


# ===========================================================================
# 9. UNARY OPERATORS  (-x  +x  ~n  not flag)
# ===========================================================================
section("9. UNARY OPERATORS  (single operand)")

# --- Example 1: unary minus and plus ---
x = 5
print("x =", x)
print("-x =", -x)   # -5  (negate)
print("+x =", +x)   #  5  (identity — no change)

# --- Example 2: unary minus with floats ---
temperature = 36.6
print(f"\ntemperature = {temperature}")
print(f"-temperature = {-temperature}")   # -36.6

# --- Example 3: logical not (unary) ---
is_empty = len([]) == 0
print(f"\nis_empty = {is_empty}")
print(f"not is_empty  = {not is_empty}")   # False
items = [1, 2]
print(f"not items     = {not items}")      # False (non-empty list is truthy)
print(f"not []        = {not []}")         # True  (empty list is falsy)


# ===========================================================================
# 10. OPERATOR PRECEDENCE — quick demonstration
# ===========================================================================
section("10. OPERATOR PRECEDENCE")

print("2 + 3 * 4          =", 2 + 3 * 4)        # 14  (* before +)
print("(2 + 3) * 4        =", (2 + 3) * 4)      # 20  (parens override)
print("2 ** 3 ** 2        =", 2 ** 3 ** 2)      # 512 (** is right-associative: 3**2=9, 2**9=512)
print("not 5 > 3          =", not 5 > 3)         # False (> before not)
print("True or False and False =", True or False and False)  # True (and before or)
print("10 > 5 and 3 < 7   =", 10 > 5 and 3 < 7)   # True


print("\n" + "=" * 55)
print("  All examples complete.")
print("=" * 55)
