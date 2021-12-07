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
    """ Class that handles testing the GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, mock_get_json):
        """ Tests return value of GithubOrgClient """
        client = GithubOrgClient(org)
        client_return = client.org
        self.assertEqual(client_return, mock_get_json.return_value)

    def test_public_repos(self):
        """
        Tests return value of GithubOrgClient.public_repos_url
        """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_org:
            test_json = {"repos_url": "holberton"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            self.assertEqual(
                test_return, mock_org.return_value.get("repos_url"))
