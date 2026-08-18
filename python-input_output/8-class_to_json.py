#!/usr/bin/python3
"""Module that defines a function to return the dictionary description
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
