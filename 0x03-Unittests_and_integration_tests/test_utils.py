#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.Testcase):
    """
    Test cases for the function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"b": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test returns expected result for the map and path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
