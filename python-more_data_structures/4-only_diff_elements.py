#!/usr/bin/python3
"""Defines only_diff_elements."""


def only_diff_elements(set_1, set_2):
    """Returns a set of elements present in only one of set_1 or set_2."""
    return set_1 ^ set_2
