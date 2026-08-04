#!/usr/bin/python3
"""Defines magic_calculation."""


def magic_calculation(a, b, c):
    """Performs a calculation based on comparisons of a, b, and c."""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
