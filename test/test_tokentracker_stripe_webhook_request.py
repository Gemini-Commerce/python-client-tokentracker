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

from tokentracker.models.tokentracker_stripe_webhook_request import TokentrackerStripeWebhookRequest

class TestTokentrackerStripeWebhookRequest(unittest.TestCase):
    """TokentrackerStripeWebhookRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokentrackerStripeWebhookRequest:
        """Test TokentrackerStripeWebhookRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokentrackerStripeWebhookRequest`
        """
        model = TokentrackerStripeWebhookRequest()
        if include_optional:
            return TokentrackerStripeWebhookRequest(
                data = tokentracker.models.stripe_event_data.StripeEventData(
                    object = tokentracker.models.object.object(), 
                    previous_attributes = tokentracker.models.previous_attributes.previousAttributes(), 
                    raw = '', ),
                account = '',
                api_version = '',
                created = '',
                id = '',
                livemode = True,
                object = '',
                pending_webhooks = '',
                request = tokentracker.models.stripe_event_request.StripeEventRequest(
                    id = '', 
                    idempotency_key = '', ),
                type = ''
            )
        else:
            return TokentrackerStripeWebhookRequest(
        )
        """

    def testTokentrackerStripeWebhookRequest(self):
        """Test TokentrackerStripeWebhookRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()