#!/usr/bin/python3
"""Unit tests for models.rectangle.Rectangle."""
import io
import unittest
from contextlib import redirect_stdout

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unit tests for instantiating a Rectangle object."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_is_base(self):
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_two_args(self):
        r = Rectangle(10, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 0, 0))

    def test_three_args(self):
        r = Rectangle(10, 2, 5)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 5, 0))

    def test_four_args(self):
        r = Rectangle(10, 2, 5, 6)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 5, 6))

    def test_five_args_id(self):
        r = Rectangle(10, 2, 5, 6, 99)
        self.assertEqual(r.id, 99)

    def test_id_auto(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual((r1.id, r2.id), (1, 2))

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "5")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 5, "6")

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -1)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 5, -1)

    def test_width_bool(self):
        with self.assertRaises(TypeError):
            Rectangle(True, 2)

    def test_width_float(self):
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_width_none(self):
        with self.assertRaises(TypeError):
            Rectangle(None, 2)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 5, 6, 99, 100)

    def test_missing_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()


class TestRectangle_properties(unittest.TestCase):
    """Unit tests for Rectangle property setters/getters."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_width_setter(self):
        r = Rectangle(1, 1)
        r.width = 20
        self.assertEqual(r.width, 20)

    def test_height_setter(self):
        r = Rectangle(1, 1)
        r.height = 20
        self.assertEqual(r.height, 20)

    def test_x_setter(self):
        r = Rectangle(1, 1)
        r.x = 20
        self.assertEqual(r.x, 20)

    def test_y_setter(self):
        r = Rectangle(1, 1)
        r.y = 20
        self.assertEqual(r.y, 20)

    def test_width_setter_invalid(self):
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.width = "bad"

    def test_x_setter_negative(self):
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.x = -5


class TestRectangle_area(unittest.TestCase):
    """Unit tests for Rectangle.area."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_area_basic(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_after_update(self):
        r = Rectangle(3, 2)
        r.width = 10
        self.assertEqual(r.area(), 20)

    def test_area_no_args(self):
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_display(unittest.TestCase):
    """Unit tests for Rectangle.display."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_display_basic(self):
        r = Rectangle(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_display_with_x(self):
        r = Rectangle(2, 2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "  ##\n  ##\n")

    def test_display_with_y(self):
        r = Rectangle(2, 2, 0, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "\n\n##\n##\n")

    def test_display_with_x_and_y(self):
        r = Rectangle(2, 2, 2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n")


class TestRectangle_str(unittest.TestCase):
    """Unit tests for Rectangle.__str__."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_via_print(self):
        r = Rectangle(4, 6, 2, 1, 12)
        f = io.StringIO()
        with redirect_stdout(f):
            print(r)
        self.assertEqual(f.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")


class TestRectangle_update(unittest.TestCase):
    """Unit tests for Rectangle.update."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_args_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_all(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 2, 3, 4, 5))

    def test_update_args_partial(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(1, 2)
        self.assertEqual(r.width, 2)

    def test_update_args_none(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update()
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (1, 1, 1, 1, 1))

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=2, height=3, x=4, y=5, id=89)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 2, 3, 4, 5))

    def test_update_kwargs_partial(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(height=7)
        self.assertEqual(r.height, 7)

    def test_update_args_invalid_value(self):
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            r.update(1, -5)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unit tests for Rectangle.to_dictionary."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dictionary_keys(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(
            set(d.keys()), {"id", "width", "height", "x", "y"})

    def test_to_dictionary_values(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_is_dict(self):
        r = Rectangle(10, 2)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_reconstructs(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
