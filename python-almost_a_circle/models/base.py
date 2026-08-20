#!/usr/bin/python3
"""
This module defines the Base class.
"""


class Base:
    """
    Base class for all other classes in this project.
    Manages the id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int): The identity of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
