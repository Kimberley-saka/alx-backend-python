#!/usr/bin/env python3
"""
Test access nested map in utils.py
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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

    @parameterized.expand(
        [
            ({}, ("a"), "a"),
            ({"a": 1}, ("a", "b"), "b")
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, output):
        """
        test exceptions
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    test utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, expected_result):
        """
        test get json
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_result
        with patch('requests.get', return_value=mock_response):
            response = get_json(test_url)
            self.assertEqual(response, expected_result)


class TestMemoize(unittest.TestCase):
    """
    test memoize
    """
    class TestClass:
        """
        test class
        """
        def a_method(self):
            """
            test func
            """
            return 42

        @memoize
        def a_property(self):
            """
            test func
            """
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        test memoize
        """
        instance = self.TestClass()

        mock_a_method.return_value = 42

        result1 = instance.a_property
        result2 = instance.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_a_method.assert_called_once()
