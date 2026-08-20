#!/usr/bin/python3
"""
This module defines the Base class.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation, or "[]" if None/empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string, or [] if None/empty.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
