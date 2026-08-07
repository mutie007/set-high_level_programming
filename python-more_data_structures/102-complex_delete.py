#!/usr/bin/python3
"""Defines complex_delete."""


def complex_delete(a_dictionary, value):
    """Deletes all keys in a_dictionary that have the given value."""
    keys_to_delete = [
        key for key in a_dictionary if a_dictionary[key] == value
    ]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
