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

from tokentracker.models.stripe_event_request import StripeEventRequest

class TestStripeEventRequest(unittest.TestCase):
    """StripeEventRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StripeEventRequest:
        """Test StripeEventRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StripeEventRequest`
        """
        model = StripeEventRequest()
        if include_optional:
            return StripeEventRequest(
                id = '',
                idempotency_key = ''
            )
        else:
            return StripeEventRequest(
        )
        """

    def testStripeEventRequest(self):
        """Test StripeEventRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
