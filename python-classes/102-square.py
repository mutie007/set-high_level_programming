#!/usr/bin/python3
"""Defines a Square class with comparison operators based on area."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size: the size of the square.

        Raises:
            TypeError: if size is not a number (int or float).
            ValueError: if size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value: the new size.

        Raises:
            TypeError: if value is not a number (int or float).
            ValueError: if value is less than 0.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Checks equality based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks inequality based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks less-than based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks less-than-or-equal based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks greater-than based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks greater-than-or-equal based on area."""
        return self.area() >= other.area()
