#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x coordinate. Defaults to 0.
            y (int): The y coordinate. Defaults to 0.
            id (int): The identity of the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (assigns both width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns the string representation of the Square.

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates the Square attributes.

        Args:
            *args: Variable number of arguments in this order:
                   1st - id, 2nd - size, 3rd - x, 4th - y
            **kwargs: Key/value pairs of attributes to update.
                      Skipped if *args exists and is not empty.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
