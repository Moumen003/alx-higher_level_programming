#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [2, 4, 6, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [65, 3546, 43, 334]
        self.assertEqual(max_integer(unordered), 3546)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [3546354, 4365, 453, 65]
        self.assertEqual(max_integer(max_at_beginning), 3546354)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [90]
        self.assertEqual(max_integer(one_element), 90)

    def test_floats(self):
        """Test a list of floats."""
        floats = [3.53, 6.32, -8.13, 14.2, 564.0]
        self.assertEqual(max_integer(floats), 564.0)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.535, 155.54, -95, 159, 68]
        self.assertEqual(max_integer(ints_and_floats), 159)

    def test_string(self):
        """Test a string."""
        string = "moumen"
        self.assertEqual(max_integer(string), 'u')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["moumen", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "moumen")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
