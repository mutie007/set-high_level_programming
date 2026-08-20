#!/usr/bin/python3
"""Unit tests for models/base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_id_auto(self):
        """Test automatic id assignment"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_manual(self):
        """Test manual id assignment"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_none(self):
        """Test id = None"""
        b = Base(None)
        self.assertIsNotNone(b.id)


if __name__ == "__main__":
    unittest.main()
