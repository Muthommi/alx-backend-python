#!/usr/bin/env python3
"""
Unit tests for the client module.
"""

import unittest
from unittest import TestCase
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """
    Test cases for GithuOrgClient class.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_response, mock_get_json):
        """
        Tests that GithubOrgClient.org returns the correct value.
        """
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        result = client.org
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(result, expected_response)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Tests that _public_repos_url returns the expected URL.
        """
        repos_url = "https://api.github.com/orgs/test_org/repos"
        mock_org.return_value = {"repos_url": repos_url}
        client = GithubOrgClient("test_org")
        result = client._public_repos_url
        self.assertEqual(result, repos_url)


if __name__ == '__main__':
    unittest.main()
