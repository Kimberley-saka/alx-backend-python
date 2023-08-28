#!/usr/bin/env python3
"""
Test client.py
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test org
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """"
        Test GithubClient.org
        """
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, mock_get_json.return_value)
        mock_get_json.assert_called_once