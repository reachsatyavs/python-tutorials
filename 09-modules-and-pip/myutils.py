"""
myutils.py — a small sample module used by modules_examples.py
to demonstrate how to create and import your own module.
"""

PI = 3.14159   # module-level constant


def greet(name: str) -> str:
    """Return a personalised greeting."""
    return f"Hello, {name}! Welcome to Python modules."


def circle_area(radius: float) -> float:
    """Return the area of a circle with the given radius."""
    return PI * radius ** 2


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value so that lo <= result <= hi."""
    return max(lo, min(hi, value))


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards (ignores case)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    # This block runs ONLY when you execute:  python3 myutils.py
    # It does NOT run when another file does: import myutils
    print("--- myutils self-test ---")
    print(greet("World"))
    print(f"circle_area(5) = {circle_area(5):.2f}")
    print(f"clamp(150, 0, 100) = {clamp(150, 0, 100)}")
    print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")
    print(f"is_palindrome('hello')   = {is_palindrome('hello')}")
