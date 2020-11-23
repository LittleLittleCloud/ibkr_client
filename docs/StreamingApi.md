# ibkr_client.StreamingApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ws_post**](StreamingApi.md#ws_post) | **POST** /ws | Websocket Endpoint


# **ws_post**
> ws_post()

Websocket Endpoint

The streaming API is documented under [Streaming WebSocket Data](https://interactivebrokers.github.io/cpwebapi/RealtimeSubscription.html) for details.

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.StreamingApi()

try:
    # Websocket Endpoint
    api_instance.ws_post()
except ApiException as e:
    print("Exception when calling StreamingApi->ws_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

