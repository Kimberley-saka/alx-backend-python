#!/usr/bin/env python3
"""
Test access nested map in utils.py
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    test access nested map
    """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
            ]
    )
    def test_access_nested_map(self, nested_map, path, expecetd_result):
        """
        test access_nested_map
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expecetd_result)
