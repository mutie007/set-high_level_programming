#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size: the size of the square.
        """
        self.__size = size
