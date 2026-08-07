#!/usr/bin/python3
"""Module that defines a function to replace elements in a list."""


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
        my_list (list): The initial list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        list: A new list with all occurrences of `search` replaced by `replace`.
              The original list is not modified.
    """
    return [replace if x == search else x for x in my_list]
