#!/usr/bin/python3
"""
Module that adds two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int/float): first number
        b (int/float): second number (default 98)

    Returns:
        int: the addition of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
