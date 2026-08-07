#!/usr/bin/python3
"""Defines search_replace."""


def search_replace(my_list, search, replace):
    """Returns a new list with occurrences of search replaced by replace."""
    return [replace if item == search else item for item in my_list]
