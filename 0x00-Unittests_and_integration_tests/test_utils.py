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
		{"a": 1}, ("a",),
		{"a": {"b": 2}}, ("a",),
		{"a": {"b": 2}}, ("a", "b"),
	])
	def test_access_nested_map(self, d, keys):
		"""
		Test access to nested map method
		"""
		from utils import access_nested_map
		self.assertEqual(access_nested_map(d, keys), d[keys[0]][keys[1]])
