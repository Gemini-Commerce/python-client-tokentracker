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
import datetime

from tokentracker.models.token_tracker_adjust_token_balance_request import TokenTrackerAdjustTokenBalanceRequest

class TestTokenTrackerAdjustTokenBalanceRequest(unittest.TestCase):
    """TokenTrackerAdjustTokenBalanceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenTrackerAdjustTokenBalanceRequest:
        """Test TokenTrackerAdjustTokenBalanceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenTrackerAdjustTokenBalanceRequest`
        """
        model = TokenTrackerAdjustTokenBalanceRequest()
        if include_optional:
            return TokenTrackerAdjustTokenBalanceRequest(
                amount = ''
            )
        else:
            return TokenTrackerAdjustTokenBalanceRequest(
        )
        """

    def testTokenTrackerAdjustTokenBalanceRequest(self):
        """Test TokenTrackerAdjustTokenBalanceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
