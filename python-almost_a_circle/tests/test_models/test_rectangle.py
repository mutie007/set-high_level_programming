#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_creation(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_save_load(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        list_r = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_r[0]))

        Rectangle.save_to_file(None)
        list_r = Rectangle.load_from_file()
        self.assertEqual(list_r, [])

        Rectangle.save_to_file([])
        list_r = Rectangle.load_from_file()
        self.assertEqual(list_r, [])


if __name__ == "__main__":
    unittest.main()


    def test_display_without_x_y(self):
        """Test display without x and y"""
        r = Rectangle(2, 3)
        # Just check that it runs without error
        r.display()

    def test_display_without_y(self):
        """Test display without y"""
        r = Rectangle(2, 3, 2)
        r.display()

    def test_display(self):
        """Test display with x and y"""
        r = Rectangle(2, 3, 2, 2)
        r.display()

    def test_save_to_file_empty_list(self):
        """Test save_to_file with empty list"""
        Rectangle.save_to_file([])
        list_r = Rectangle.load_from_file()
        self.assertEqual(list_r, [])
