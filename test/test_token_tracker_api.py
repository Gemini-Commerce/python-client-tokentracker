# coding: utf-8

"""
    Token Tracker Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tokentracker.api.token_tracker_api import TokenTrackerApi


class TestTokenTrackerApi(unittest.TestCase):
    """TokenTrackerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TokenTrackerApi()

    def tearDown(self) -> None:
        pass

    def test_token_tracker_adjust_token_balance(self) -> None:
        """Test case for token_tracker_adjust_token_balance

        AdjustTokenBalance
        """
        pass

    def test_token_tracker_get_token_balance(self) -> None:
        """Test case for token_tracker_get_token_balance

        GetTokenBalance
        """
        pass

    def test_token_tracker_stripe_webhook(self) -> None:
        """Test case for token_tracker_stripe_webhook

        StripeWebhook
        """
        pass


if __name__ == '__main__':
    unittest.main()