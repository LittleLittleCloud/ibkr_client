# ibkr_client.OrderApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_account_account_id_order_order_id_delete**](OrderApi.md#iserver_account_account_id_order_order_id_delete) | **DELETE** /iserver/account/{accountId}/order/{orderId} | Cancel Order
[**iserver_account_account_id_order_order_id_post**](OrderApi.md#iserver_account_account_id_order_order_id_post) | **POST** /iserver/account/{accountId}/order/{orderId} | Modify Order
[**iserver_account_account_id_order_post**](OrderApi.md#iserver_account_account_id_order_post) | **POST** /iserver/account/{accountId}/order | Place Order
[**iserver_account_account_id_order_whatif_post**](OrderApi.md#iserver_account_account_id_order_whatif_post) | **POST** /iserver/account/{accountId}/order/whatif | Preview Order
[**iserver_account_account_id_orders_post**](OrderApi.md#iserver_account_account_id_orders_post) | **POST** /iserver/account/{accountId}/orders | Place Orders (Support bracket orders)
[**iserver_account_orders_fa_group_post**](OrderApi.md#iserver_account_orders_fa_group_post) | **POST** /iserver/account/orders/{faGroup} | Place Orders for Financial Advisor Groups
[**iserver_account_orders_get**](OrderApi.md#iserver_account_orders_get) | **GET** /iserver/account/orders | Live Orders
[**iserver_reply_replyid_post**](OrderApi.md#iserver_reply_replyid_post) | **POST** /iserver/reply/{replyid} | Place Order Reply


# **iserver_account_account_id_order_order_id_delete**
> InlineResponse20018 iserver_account_account_id_order_order_id_delete(account_id, order_id)

Cancel Order

Cancels an open order. Must call /iserver/accounts endpoint prior to cancelling an order. Use /iservers/account/orders endpoint to review open-order(s) and get latest order status.

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.OrderApi()
account_id = 'account_id_example' # str | account id, or fa group if deleting a group order
order_id = 'order_id_example' # str | Customer order id, use /iservers/account/orders endpoint to query orderId.

try:
    # Cancel Order
    api_response = api_instance.iserver_account_account_id_order_order_id_delete(account_id, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_order_order_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id, or fa group if deleting a group order | 
 **order_id** | **str**| Customer order id, use /iservers/account/orders endpoint to query orderId. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_account_id_order_order_id_post**
> list[InlineResponse20017] iserver_account_account_id_order_order_id_post(account_id, order_id, body)

Modify Order

Modifies an open order. Must call /iserver/accounts endpoint prior to modifying an order. Use /iservers/account/orders endpoint to review open-order(s).

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.OrderApi()
account_id = 'account_id_example' # str | account id, or fa group if modifying a group order
order_id = 'order_id_example' # str | Customer order id, use /iservers/account/orders endpoint to query orderId.
body = ibkr_client.ModifyOrder() # ModifyOrder | modify-order request

try:
    # Modify Order
    api_response = api_instance.iserver_account_account_id_order_order_id_post(account_id, order_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_order_order_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id, or fa group if modifying a group order | 
 **order_id** | **str**| Customer order id, use /iservers/account/orders endpoint to query orderId. | 
 **body** | [**ModifyOrder**](ModifyOrder.md)| modify-order request | 

### Return type

[**list[InlineResponse20017]**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_account_id_order_post**
> list[InlineResponse20014] iserver_account_account_id_order_post(account_id, body)

Place Order

Please note here, sometimes this endpoint alone can't make sure you submit the order successfully, you could receive some questions in the response, you have to to answer them in order to submit the order successfully. You can use \"/iserver/reply/{replyid}\" endpoint to answer questions 

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.OrderApi()
account_id = 'account_id_example' # str | account id
body = ibkr_client.OrderRequest() # OrderRequest | order request info

try:
    # Place Order
    api_response = api_instance.iserver_account_account_id_order_post(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **body** | [**OrderRequest**](OrderRequest.md)| order request info | 

### Return type

[**list[InlineResponse20014]**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_account_id_order_whatif_post**
> InlineResponse20016 iserver_account_account_id_order_whatif_post(account_id, body)

Preview Order

This endpoint allows you to preview order without actually submitting the order and you can get commission information in the response. 

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.OrderApi()
account_id = 'account_id_example' # str | account id
body = ibkr_client.OrderRequest() # OrderRequest | order info

try:
    # Preview Order
    api_response = api_instance.iserver_account_account_id_order_whatif_post(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_order_whatif_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **body** | [**OrderRequest**](OrderRequest.md)| order info | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_account_id_orders_post**
> list[InlineResponse20014] iserver_account_account_id_orders_post(account_id, body)

Place Orders (Support bracket orders)

You can pass a list of orders here 

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.OrderApi()
account_id = 'account_id_example' # str | account id
body = ibkr_client.Body6() # Body6 | order request info

try:
    # Place Orders (Support bracket orders)
    api_response = api_instance.iserver_account_account_id_orders_post(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_account_id_orders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| account id | 
 **body** | [**Body6**](Body6.md)| order request info | 

### Return type

[**list[InlineResponse20014]**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_orders_fa_group_post**
> list[InlineResponse20014] iserver_account_orders_fa_group_post(fa_group, body)

Place Orders for Financial Advisor Groups

Financial Advisors can use this endpoint to place an order for a specified group. To place an order for a specified account use the endpoint /iserver/account/{accountId}/order. More information about groups can be found in the [TWS Users' Guide:](https://guides.interactivebrokers.com/twsguide/twsguide.htm#usersguidebook/financialadvisors/create_an_account_group_for_share_allocation.htm). 

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.OrderApi()
fa_group = 'fa_group_example' # str | financial advisor group
body = ibkr_client.OrderRequest() # OrderRequest | order request info

try:
    # Place Orders for Financial Advisor Groups
    api_response = api_instance.iserver_account_orders_fa_group_post(fa_group, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_orders_fa_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fa_group** | **str**| financial advisor group | 
 **body** | [**OrderRequest**](OrderRequest.md)| order request info | 

### Return type

[**list[InlineResponse20014]**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_account_orders_get**
> InlineResponse20013 iserver_account_orders_get()

Live Orders

The endpoint is meant to be used in polling mode, e.g. requesting every x seconds. The response will contain two objects, one is notification, the other is orders.  Orders is the list of live orders (cancelled, filled, submitted).  Notifications contains information about execute orders as they happen, see status field. To receive streaming live orders the endpoint /ws can be used. Refer to [Streaming WebSocket Data](https://interactivebrokers.github.io/cpwebapi/RealtimeSubscription.html) for details. 

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.OrderApi()

try:
    # Live Orders
    api_response = api_instance.iserver_account_orders_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_account_orders_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_reply_replyid_post**
> list[InlineResponse20015] iserver_reply_replyid_post(replyid, body)

Place Order Reply

Reply to questions when placing orders and submit orders

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.OrderApi()
replyid = 'replyid_example' # str | Please use the \"id\" from the response of \"Place Order\" endpoint
body = ibkr_client.Body7() # Body7 | Answer to question

try:
    # Place Order Reply
    api_response = api_instance.iserver_reply_replyid_post(replyid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->iserver_reply_replyid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replyid** | **str**| Please use the \&quot;id\&quot; from the response of \&quot;Place Order\&quot; endpoint | 
 **body** | [**Body7**](Body7.md)| Answer to question | 

### Return type

[**list[InlineResponse20015]**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

