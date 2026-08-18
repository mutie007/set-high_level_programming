#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_max_at_end(self):
        """Test max at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test max at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test max in the middle of the list."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative_number(self):
        """Test one negative number in the list."""
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_only_negative_numbers(self):
        """Test only negative numbers in the list."""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_list_of_one_element(self):
        """Test list of one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_list_is_empty(self):
        """Test list is empty."""
        self.assertIsNone(max_integer([]))

    def test_unordered_list(self):
        """Test unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_floats(self):
        """Test list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_ints_and_floats(self):
        """Test mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_string(self):
        """Test string as list."""
        self.assertEqual(max_integer("abcde"), "e")

    def test_list_of_strings(self):
        """Test list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_default_argument(self):
        """Test default empty list argument."""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
