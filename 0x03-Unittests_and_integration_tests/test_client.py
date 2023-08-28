#!/usr/bin/env python3
"""
Test client.py
"""
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """
        test public_repos_url property
        """

        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org_url:
            mock_org_url.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
