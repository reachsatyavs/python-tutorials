"""
Module 06 — Comprehensions & generators (runnable examples).

Run: python comprehensions_generators_examples.py
"""

from __future__ import annotations


def banner(title: str) -> None:
    print("\n" + "=" * 60 + f"\n{title}\n" + "=" * 60)


def demo_list_comprehensions() -> None:
    banner("List comprehensions")
    squares = [n * n for n in range(6)]
    print("squares:", squares)

    evens = [n for n in range(15) if n % 2 == 0]
    print("evens 0..14:", evens)

    words = ["hi", "there"]
    uppered = [w.upper() for w in words]
    print("uppered:", uppered)


def demo_dict_and_set_comprehensions() -> None:
    banner("Dict and set comprehensions")
    words = ["apple", "pie"]
    lengths = {w: len(w) for w in words}
    print("word -> length:", lengths)

    nums = [1, 2, 2, 3, 3, 3]
    unique_remainders = {n % 2 for n in nums}
    print("unique n % 2:", unique_remainders)


def demo_generator_expression() -> None:
    banner("Generator expression (lazy)")
    gen = (n * n for n in range(4))
    print("first next:", next(gen))
    print("rest as list:", list(gen))

    # Common: single parens — no extra brackets inside sum()
    total = sum(n * n for n in range(5))
    print("sum of squares 0..4:", total)


def demo_generator_function() -> None:
    banner("Generator function (yield)")

    def count_up_to(n: int):
        k = 1
        while k <= n:
            yield k
            k += 1

    g = count_up_to(3)
    print("manual next:", next(g), next(g))
    print("for-loop consumes:", list(count_up_to(5)))


def demo_one_shot_iterator() -> None:
    banner("Generators are one-shot")
    gen = (n for n in [1, 2, 3])
    print("first pass:", list(gen))
    print("second pass (empty):", list(gen))


def main() -> None:
    demo_list_comprehensions()
    demo_dict_and_set_comprehensions()
    demo_generator_expression()
    demo_generator_function()
    demo_one_shot_iterator()
    print("\nDone.\n")


if __name__ == "__main__":
    main()
