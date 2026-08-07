#!/usr/bin/python3
"""Defines simple_delete."""


def simple_delete(a_dictionary, key=""):
    """Deletes a key from a_dictionary if it exists."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
