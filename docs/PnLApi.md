# ibkr_client.PnLApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_account_pnl_partitioned_get**](PnLApi.md#iserver_account_pnl_partitioned_get) | **GET** /iserver/account/pnl/partitioned | PnL for the selected account


# **iserver_account_pnl_partitioned_get**
> InlineResponse20026 iserver_account_pnl_partitioned_get()

PnL for the selected account

Returns an object containing PnL for the selected account and its models (if any). To receive streaming PnL the endpoint /ws can be used. Refer to [Streaming WebSocket Data](https://interactivebrokers.github.io/cpwebapi/RealtimeSubscription.html) for details. 

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.PnLApi()

try:
    # PnL for the selected account
    api_response = api_instance.iserver_account_pnl_partitioned_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PnLApi->iserver_account_pnl_partitioned_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

