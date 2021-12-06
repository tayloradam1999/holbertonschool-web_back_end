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
		({}, ("a")),
		({"a": 1}, ("a", "b")),
	])
	def test_access_nested_map_exception(self, map, path):
		"""
		Test access to nested map method
		"""
		from utils import access_nested_map
		self.assertRaises(KeyError, access_nested_map, map, path)


class TestGetJson(unittest.TestCase):
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
