#!/usr/bin/python3
"""Module that defines a function to create an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
