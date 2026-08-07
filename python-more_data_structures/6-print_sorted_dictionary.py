#!/usr/bin/python3
"""Defines print_sorted_dictionary."""


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
