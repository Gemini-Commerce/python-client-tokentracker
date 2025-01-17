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

from tokentracker.models.tokentracker_get_token_balance_response import TokentrackerGetTokenBalanceResponse

class TestTokentrackerGetTokenBalanceResponse(unittest.TestCase):
    """TokentrackerGetTokenBalanceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokentrackerGetTokenBalanceResponse:
        """Test TokentrackerGetTokenBalanceResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokentrackerGetTokenBalanceResponse`
        """
        model = TokentrackerGetTokenBalanceResponse()
        if include_optional:
            return TokentrackerGetTokenBalanceResponse(
                balance = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return TokentrackerGetTokenBalanceResponse(
        )
        """

    def testTokentrackerGetTokenBalanceResponse(self):
        """Test TokentrackerGetTokenBalanceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
