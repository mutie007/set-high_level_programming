#!/usr/bin/python3
"""Module that defines inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class (but is not a_class itself)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
