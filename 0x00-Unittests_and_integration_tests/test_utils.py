#!/usr/bin/env python3
"""
Unittests for utils.py
"""
from unittest import TestCase, mock
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """
        Test access to nested map method
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, expected):
        """
        Test access to nested map method
        """
        from utils import access_nested_map
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, map, path):
        """
        Test access to nested map method
        """
        from utils import access_nested_map
        self.assertRaises(KeyError, access_nested_map, map, path)


class TestGetJson(TestCase):
    """
    Test get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Use unittest.mock.patch to patch requests.get

        Makes sure it returns a <Mock> obj with a <json> method
        that returns <test_payload> which you parameterize alongside the
        <test_url> that will pass to <get_json> with the parameterized inputs:
        """
        from utils import get_json
        import requests
        from unittest import mock
        with mock.patch('requests.get', return_value=mock.Mock(
                json=lambda: test_payload)):
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(TestCase):
    """ Tests for memoize method """

    def test_memoize(self):
        """ Test for memoize """
        from utils import memoize

        class TestClass:
            """ Test class for memoize method """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, "a_method",
                               return_value=42) as mock_method:
            test2 = TestClass()
            self.assertEqual(test2.a_property, 42)
            self.assertEqual(test2.a_property, 42)
            mock_method.assert_called_once()
