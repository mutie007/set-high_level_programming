#!/usr/bin/python3
"""Module that defines a function to add two integers."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float), defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
