# ibkr_client.PortfolioAnalystApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pa_performance_post**](PortfolioAnalystApi.md#pa_performance_post) | **POST** /pa/performance | Account Performance
[**pa_summary_post**](PortfolioAnalystApi.md#pa_summary_post) | **POST** /pa/summary | Account Balance&#39;s Summary
[**pa_transactions_post**](PortfolioAnalystApi.md#pa_transactions_post) | **POST** /pa/transactions | Position&#39;s Transaction History


# **pa_performance_post**
> Performance pa_performance_post(body)

Account Performance

Returns the performance (MTM) for the given accounts, if more than one account is passed, the result is consolidated.

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.PortfolioAnalystApi()
body = ibkr_client.Body2() # Body2 | an array of account ids

try:
    # Account Performance
    api_response = api_instance.pa_performance_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAnalystApi->pa_performance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| an array of account ids | 

### Return type

[**Performance**](Performance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pa_summary_post**
> Summary pa_summary_post(body)

Account Balance's Summary

Returns a summary of all account balances for the given accounts, if more than one account is passed, the result is consolidated.

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.PortfolioAnalystApi()
body = ibkr_client.Body3() # Body3 | an array of account ids

try:
    # Account Balance's Summary
    api_response = api_instance.pa_summary_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAnalystApi->pa_summary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| an array of account ids | 

### Return type

[**Summary**](Summary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pa_transactions_post**
> Transactions pa_transactions_post(body)

Position's Transaction History

transaction history for a given number of conids and accounts. Types of transactions include dividend payments, buy and sell transactions, transfers. 

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.PortfolioAnalystApi()
body = ibkr_client.Body4() # Body4 | 

try:
    # Position's Transaction History
    api_response = api_instance.pa_transactions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioAnalystApi->pa_transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)|  | 

### Return type

[**Transactions**](Transactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

