#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Tests for Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.y, 3)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_update(self):
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 2)
        self.assertEqual(s.size, 2)
        s.update(89, 2, 3)
        self.assertEqual(s.x, 3)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        list_s = Square.load_from_file()
        self.assertEqual(list_s, [])

    def test_save_to_file_empty_list(self):
        """Test of Square.save_to_file([]) exists"""
        Square.save_to_file([])
        list_s = Square.load_from_file()
        self.assertEqual(list_s, [])

    def test_save_to_file(self):
        s1 = Square(5)
        Square.save_to_file([s1])
        list_s = Square.load_from_file()
        self.assertEqual(str(s1), str(list_s[0]))


if __name__ == "__main__":
    unittest.main()


    def test_save_to_file_none(self):
        """Test of Square.save_to_file(None) exists"""
        Square.save_to_file(None)
        result = Square.load_from_file()
        self.assertEqual(result, [])


    def test_save_to_file_none(self):
        """Test of Square.save_to_file(None) exists"""
        Square.save_to_file(None)
        result = Square.load_from_file()
        self.assertEqual(result, [])
