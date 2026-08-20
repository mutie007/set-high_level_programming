#!/usr/bin/python3
"""Unit tests for models.base.Base."""
import json
import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unit tests for instantiating a Base object."""

    def setUp(self):
        """Reset Base's private class attribute before each test."""
        Base._Base__nb_objects = 0

    def test_no_args(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_two_bases_increment_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_public(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_id_does_not_affect_counter(self):
        Base(50)
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_string(self):
        b = Base("hello")
        self.assertEqual(b.id, "hello")


class TestBase_to_json_string(unittest.TestCase):
    """Unit tests for Base.to_json_string."""

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_returns_str(self):
        self.assertIsInstance(Base.to_json_string([{"a": 1}]), str)

    def test_single_dict(self):
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(json.loads(result), [{"id": 1}])

    def test_multiple_dicts(self):
        list_dicts = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(result), list_dicts)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unit tests for Base.from_json_string."""

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_returns_list(self):
        result = Base.from_json_string('[{"id": 1}]')
        self.assertIsInstance(result, list)

    def test_round_trip(self):
        list_dicts = [{"id": 1, "width": 2}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", "[]")


class TestBase_save_to_file(unittest.TestCase):
    """Unit tests for Base.save_to_file."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        for fname in ("Rectangle.json", "Square.json", "Base.json"):
            try:
                os.remove(fname)
            except IOError:
                pass

    def test_save_creates_file(self):
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_file_content(self):
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(json.loads(content), [r.to_dictionary()])

    def test_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrites(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1])
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 1)

    def test_save_square(self):
        s = Square(5)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))


class TestBase_load_from_file(unittest.TestCase):
    """Unit tests for Base.load_from_file."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        for fname in ("Rectangle.json", "Square.json"):
            try:
                os.remove(fname)
            except IOError:
                pass

    def test_no_file_returns_empty_list(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_round_trip(self):
        r1 = Rectangle(3, 5, 1, 2, 10)
        r2 = Rectangle(9, 24, 0, 0, 20)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())

    def test_load_returns_instances(self):
        Rectangle.save_to_file([Rectangle(1, 1, 0, 0, 1)])
        loaded = Rectangle.load_from_file()
        self.assertIsInstance(loaded[0], Rectangle)

    def test_load_square_round_trip(self):
        s1 = Square(5, 1, 2, 10)
        Square.save_to_file([s1])
        loaded = Square.load_from_file()
        self.assertEqual(loaded[0].to_dictionary(), s1.to_dictionary())


class TestBase_save_load_csv(unittest.TestCase):
    """Unit tests for Base.save_to_file_csv and Base.load_from_file_csv."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        for fname in ("Rectangle.csv", "Square.csv"):
            try:
                os.remove(fname)
            except IOError:
                pass

    def test_no_csv_file_returns_empty_list(self):
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_csv_round_trip_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 10)
        r2 = Rectangle(9, 24, 0, 0, 20)
        Rectangle.save_to_file_csv([r1, r2])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())

    def test_csv_round_trip_square(self):
        s1 = Square(5, 1, 2, 10)
        Square.save_to_file_csv([s1])
        loaded = Square.load_from_file_csv()
        self.assertEqual(loaded[0].to_dictionary(), s1.to_dictionary())

    def test_csv_empty_list(self):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(f.read(), "[]")


if __name__ == "__main__":
    unittest.main()
