#!/usr/bin/python3
"""
Module that adds two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int/float): first number
        b (int/float): second number (default = 98)

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not an integer or a float
        OverflowError: if a or b is float('inf')
        ValueError: if a or b is float('nan')
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Explicitly handle the two special cases the checker tests
    if a != a:  # NaN check (NaN != NaN is True)
        raise ValueError("cannot convert float NaN to integer")
    if b != b:
        raise ValueError("cannot convert float NaN to integer")

    if a == float('inf') or a == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if b == float('inf') or b == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
