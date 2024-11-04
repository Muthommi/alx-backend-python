#!/usr/bin/env python3
"""
Unit tests for the client module.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
