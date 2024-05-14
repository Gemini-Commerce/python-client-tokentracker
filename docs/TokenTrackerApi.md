# tokentracker.TokenTrackerApi

All URIs are relative to *https://token-tracker.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_tracker_adjust_token_balance**](TokenTrackerApi.md#token_tracker_adjust_token_balance) | **POST** /v1/{tenantId}/adjust_token_balance | AdjustTokenBalance
[**token_tracker_get_token_balance**](TokenTrackerApi.md#token_tracker_get_token_balance) | **POST** /v1/{tenantId}/get_token_balance | GetTokenBalance
[**token_tracker_stripe_webhook**](TokenTrackerApi.md#token_tracker_stripe_webhook) | **POST** /v1/stripe/webhook | StripeWebhook


# **token_tracker_adjust_token_balance**
> TokentrackerAdjustTokenBalanceResponse token_tracker_adjust_token_balance(tenant_id, body)

AdjustTokenBalance

Adjust token balance

### Example

* OAuth Authentication (standardAuthorization):

```python
import time
import os
import tokentracker
from tokentracker.models.token_tracker_adjust_token_balance_request import TokenTrackerAdjustTokenBalanceRequest
from tokentracker.models.tokentracker_adjust_token_balance_response import TokentrackerAdjustTokenBalanceResponse
from tokentracker.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://token-tracker.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = tokentracker.Configuration(
    host = "https://token-tracker.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tokentracker.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tokentracker.TokenTrackerApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = tokentracker.TokenTrackerAdjustTokenBalanceRequest() # TokenTrackerAdjustTokenBalanceRequest | 

    try:
        # AdjustTokenBalance
        api_response = api_instance.token_tracker_adjust_token_balance(tenant_id, body)
        print("The response of TokenTrackerApi->token_tracker_adjust_token_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenTrackerApi->token_tracker_adjust_token_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**TokenTrackerAdjustTokenBalanceRequest**](TokenTrackerAdjustTokenBalanceRequest.md)|  | 

### Return type

[**TokentrackerAdjustTokenBalanceResponse**](TokentrackerAdjustTokenBalanceResponse.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_tracker_get_token_balance**
> TokentrackerGetTokenBalanceResponse token_tracker_get_token_balance(tenant_id, body)

GetTokenBalance

Get token balance

### Example

* OAuth Authentication (standardAuthorization):

```python
import time
import os
import tokentracker
from tokentracker.models.tokentracker_get_token_balance_response import TokentrackerGetTokenBalanceResponse
from tokentracker.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://token-tracker.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = tokentracker.Configuration(
    host = "https://token-tracker.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tokentracker.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tokentracker.TokenTrackerApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = None # object | 

    try:
        # GetTokenBalance
        api_response = api_instance.token_tracker_get_token_balance(tenant_id, body)
        print("The response of TokenTrackerApi->token_tracker_get_token_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenTrackerApi->token_tracker_get_token_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**TokentrackerGetTokenBalanceResponse**](TokentrackerGetTokenBalanceResponse.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_tracker_stripe_webhook**
> object token_tracker_stripe_webhook(body)

StripeWebhook

Stripe webhook

### Example

* OAuth Authentication (standardAuthorization):

```python
import time
import os
import tokentracker
from tokentracker.models.tokentracker_stripe_webhook_request import TokentrackerStripeWebhookRequest
from tokentracker.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://token-tracker.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = tokentracker.Configuration(
    host = "https://token-tracker.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with tokentracker.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tokentracker.TokenTrackerApi(api_client)
    body = tokentracker.TokentrackerStripeWebhookRequest() # TokentrackerStripeWebhookRequest | 

    try:
        # StripeWebhook
        api_response = api_instance.token_tracker_stripe_webhook(body)
        print("The response of TokenTrackerApi->token_tracker_stripe_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenTrackerApi->token_tracker_stripe_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokentrackerStripeWebhookRequest**](TokentrackerStripeWebhookRequest.md)|  | 

### Return type

**object**

### Authorization

[standardAuthorization](../README.md#standardAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

