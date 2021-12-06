#!/usr/bin/env python3
"""
Unittests for utils.py
"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
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
		({}, ("a",)),
		({"a": 1}, ("a", "b")),
	])
	def test_access_nested_map_error(self, map, path):
		"""
		Test access to nested map method
		"""
		from utils import access_nested_map
		self.assertRaises(KeyError, access_nested_map, map, path)
