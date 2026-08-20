#!/usr/bin/python3
"""Unit tests for models.square.Square."""
import io
import unittest
from contextlib import redirect_stdout

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unit tests for instantiating a Square object."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_is_rectangle(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_is_base(self):
        self.assertIsInstance(Square(1), Base)

    def test_one_arg(self):
        s = Square(5)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 0, 0))

    def test_two_args(self):
        s = Square(5, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 2, 0))

    def test_three_args(self):
        s = Square(5, 2, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 2, 3))

    def test_four_args_id(self):
        s = Square(5, 2, 3, 99)
        self.assertEqual(s.id, 99)

    def test_id_auto(self):
        s1 = Square(1)
        s2 = Square(1)
        self.assertEqual((s1.id, s2.id), (1, 2))

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(5, "2")

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(5, 2, -1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 99, 100)


class TestSquare_size_property(unittest.TestCase):
    """Unit tests for Square.size getter/setter."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_size_getter(self):
        s = Square(7)
        self.assertEqual(s.size, 7)

    def test_size_setter_updates_width_and_height(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_invalid_type(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "bad"

    def test_size_setter_invalid_value(self):
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -1

    def test_size_setter_zero(self):
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = 0


class TestSquare_area(unittest.TestCase):
    """Unit tests for Square.area (inherited from Rectangle)."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_area_after_size_change(self):
        s = Square(3)
        s.size = 5
        self.assertEqual(s.area(), 25)


class TestSquare_display(unittest.TestCase):
    """Unit tests for Square.display (inherited from Rectangle)."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_display_basic(self):
        s = Square(2)
        f = io.StringIO()
        with redirect_stdout(f):
            s.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_display_with_offsets(self):
        s = Square(2, 1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            s.display()
        self.assertEqual(f.getvalue(), "\n ##\n ##\n")


class TestSquare_str(unittest.TestCase):
    """Unit tests for Square.__str__."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str(self):
        s = Square(5, 1, 2, 12)
        self.assertEqual(str(s), "[Square] (12) 1/2 - 5")


class TestSquare_update(unittest.TestCase):
    """Unit tests for Square.update."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_args_all(self):
        s = Square(5, 1, 2, 1)
        s.update(89, 3, 4, 5)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 3, 4, 5))

    def test_update_args_partial(self):
        s = Square(5)
        s.update(1, 7)
        self.assertEqual(s.size, 7)

    def test_update_kwargs(self):
        s = Square(5, 1, 2, 1)
        s.update(size=3, x=4, y=5, id=89)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 3, 4, 5))

    def test_update_kwargs_partial(self):
        s = Square(5)
        s.update(size=9)
        self.assertEqual(s.size, 9)

    def test_update_args_none(self):
        s = Square(5, 1, 2, 1)
        s.update()
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 5, 1, 2))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unit tests for Square.to_dictionary."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dictionary_keys(self):
        s = Square(10, 1, 9, 5)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "size", "x", "y"})

    def test_to_dictionary_values(self):
        s = Square(10, 1, 9, 5)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 5, "size": 10, "x": 1, "y": 9})

    def test_to_dictionary_reconstructs(self):
        s1 = Square(10, 1, 9, 5)
        s2 = Square(1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
