#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A list subclass with a print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
