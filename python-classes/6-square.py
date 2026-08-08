#!/usr/bin/python3
"""Defines a Square class with size and position properties."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.

        Args:
            size: the size of the square.
            position: the (x, y) position of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
            TypeError: if position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value: the new position, a tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(num) is int for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the '#' character, using position."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
