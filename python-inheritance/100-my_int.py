#!/usr/bin/python3
"""Module that defines the MyInt class."""


class MyInt(int):
    """MyInt is a rebel that inverts == and != operators."""

    def __eq__(self, other):
        """Invert the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the inequality operator."""
        return super().__eq__(other)
