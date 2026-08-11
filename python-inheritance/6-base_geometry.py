#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area method."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
