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

# tests/test_models/test_square.py
cat > tests/test_models/test_square.py << 'EOF'
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

    def test_save_load(self):
        s1 = Square(5)
        Square.save_to_file([s1])
        list_s = Square.load_from_file()
        self.assertEqual(str(s1), str(list_s[0]))

        Square.save_to_file(None)
        list_s = Square.load_from_file()
        self.assertEqual(list_s, [])

        Square.save_to_file([])
        list_s = Square.load_from_file()
        self.assertEqual(list_s, [])


if __name__ == "__main__":
    unittest.main()
