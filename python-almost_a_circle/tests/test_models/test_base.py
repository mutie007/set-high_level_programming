#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_auto_id_plus_one(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_manual_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        json_str = Base.to_json_string([dictionary])
        self.assertEqual(type(json_str), str)
        self.assertIn('"id": 1', json_str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        list_input = [{'id': 89}]
        json_str = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_str)
        self.assertEqual(list_output, [{'id': 89}])
        self.assertEqual(type(list_output), list)


if __name__ == "__main__":
    unittest.main()
