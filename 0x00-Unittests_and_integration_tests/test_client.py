#!/usr/bin/env python3
"""
Tests github org client
"""
import unittest
from unittest.mock import patch, PropertyMock
from urllib.error import HTTPError
from parameterized import parameterized
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import *


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests github org client
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, mock_get_json):
        """
        Tests return value of GithubOrgClient.org
        """
        client = GithubOrgClient(org)
        client_return = client.org
        self.assertEqual(client_return, mock_get_json.return_value)
