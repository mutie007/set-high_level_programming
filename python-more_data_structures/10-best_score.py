#!/usr/bin/python3
"""Defines best_score."""


def best_score(a_dictionary):
    """Returns the key with the biggest integer value in a_dictionary."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
