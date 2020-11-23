# ibkr_client.ContractApi

All URIs are relative to *https://localhost:5000/v1/portal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iserver_contract_conid_info_get**](ContractApi.md#iserver_contract_conid_info_get) | **GET** /iserver/contract/{conid}/info | Contract Details
[**iserver_secdef_info_get**](ContractApi.md#iserver_secdef_info_get) | **GET** /iserver/secdef/info | Get available conids of future/option/warrant/cash/CFD
[**iserver_secdef_search_post**](ContractApi.md#iserver_secdef_search_post) | **POST** /iserver/secdef/search | Search by symbol or name
[**iserver_secdef_strikes_get**](ContractApi.md#iserver_secdef_strikes_get) | **GET** /iserver/secdef/strikes | Get strikes for Options/Warrant
[**trsrv_futures_get**](ContractApi.md#trsrv_futures_get) | **GET** /trsrv/futures | Security Futures by Symbol
[**trsrv_secdef_post**](ContractApi.md#trsrv_secdef_post) | **POST** /trsrv/secdef | Secdef by Conid
[**trsrv_secdef_schedule_get**](ContractApi.md#trsrv_secdef_schedule_get) | **GET** /trsrv/secdef/schedule | Get trading schedule for symbol
[**trsrv_stocks_get**](ContractApi.md#trsrv_stocks_get) | **GET** /trsrv/stocks | Security Stocks by Symbol


# **iserver_contract_conid_info_get**
> Contract iserver_contract_conid_info_get(conid)

Contract Details

Using the Contract Identifier get contract info. You can use this to prefill your order before you submit an order

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.ContractApi()
conid = 'conid_example' # str | contract id

try:
    # Contract Details
    api_response = api_instance.iserver_contract_conid_info_get(conid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_contract_conid_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| contract id | 

### Return type

[**Contract**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_secdef_info_get**
> object iserver_secdef_info_get(conid, sectype, month=month, exchange=exchange, strike=strike, right=right)

Get available conids of future/option/warrant/cash/CFD

For option and warrant, you can get strike price from \"/iserver/secdef/strikes\" endpoint. Must call /secdef/search for the underlying contract first.

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.ContractApi()
conid = 'conid_example' # str | underlying contract id
sectype = 'sectype_example' # str | FUT/OPT/WAR/CASH/CFD
month = 'month_example' # str | contract month, only required for FUT/OPT/WAR in the format MMMYY, example JAN00 (optional)
exchange = 'exchange_example' # str | optional, default is SMART (optional)
strike = 'strike_example' # str | optional, only required for OPT/WAR (optional)
right = 'right_example' # str | C for call, P for put (optional)

try:
    # Get available conids of future/option/warrant/cash/CFD
    api_response = api_instance.iserver_secdef_info_get(conid, sectype, month=month, exchange=exchange, strike=strike, right=right)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_secdef_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| underlying contract id | 
 **sectype** | **str**| FUT/OPT/WAR/CASH/CFD | 
 **month** | **str**| contract month, only required for FUT/OPT/WAR in the format MMMYY, example JAN00 | [optional] 
 **exchange** | **str**| optional, default is SMART | [optional] 
 **strike** | **str**| optional, only required for OPT/WAR | [optional] 
 **right** | **str**| C for call, P for put | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_secdef_search_post**
> list[InlineResponse20022] iserver_secdef_search_post(symbol)

Search by symbol or name

Specify an underlying to search what derivative contract(s) it has. This endpoint must be called before using /secdef/info

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.ContractApi()
symbol = ibkr_client.Symbol() # Symbol | Symbol or Company Name to be searched

try:
    # Search by symbol or name
    api_response = api_instance.iserver_secdef_search_post(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_secdef_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | [**Symbol**](Symbol.md)| Symbol or Company Name to be searched | 

### Return type

[**list[InlineResponse20022]**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iserver_secdef_strikes_get**
> InlineResponse20023 iserver_secdef_strikes_get(conid, sectype, month, exchange=exchange)

Get strikes for Options/Warrant

You can get available contract months and exchanges from \"/iserver/secdef/search\"

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.ContractApi()
conid = 'conid_example' # str | contract id
sectype = 'sectype_example' # str | OPT/WAR
month = 'month_example' # str | contract month
exchange = 'exchange_example' # str | optional, default is SMART (optional)

try:
    # Get strikes for Options/Warrant
    api_response = api_instance.iserver_secdef_strikes_get(conid, sectype, month, exchange=exchange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->iserver_secdef_strikes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conid** | **str**| contract id | 
 **sectype** | **str**| OPT/WAR | 
 **month** | **str**| contract month | 
 **exchange** | **str**| optional, default is SMART | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trsrv_futures_get**
> InlineResponse20028 trsrv_futures_get(symbols)

Security Futures by Symbol

Returns a list of non-expired future contracts for given symbol(s)

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.ContractApi()
symbols = 'symbols_example' # str | list of case-sensitive symbols separated by comma

try:
    # Security Futures by Symbol
    api_response = api_instance.trsrv_futures_get(symbols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->trsrv_futures_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| list of case-sensitive symbols separated by comma | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trsrv_secdef_post**
> Secdef trsrv_secdef_post(body)

Secdef by Conid

Returns a list of security definitions for the given conids

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.ContractApi()
body = ibkr_client.Body8() # Body8 | request body

try:
    # Secdef by Conid
    api_response = api_instance.trsrv_secdef_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->trsrv_secdef_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body8**](Body8.md)| request body | 

### Return type

[**Secdef**](Secdef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trsrv_secdef_schedule_get**
> InlineResponse20027 trsrv_secdef_schedule_get(asset_class, symbol, exchange=exchange)

Get trading schedule for symbol

Returns the trading schedule up to a month for the requested contract

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.ContractApi()
asset_class = 'asset_class_example' # str | specify the asset class of the contract. Available values-- Stock: STK, Option: OPT, Future: FUT, Contract For Difference: CFD, Warrant: WAR, Forex: SWP, Mutual Fund: FND, Bond: BND, Inter-Commodity Spreads: ICS 
symbol = 'symbol_example' # str | Underlying Symbol for specified contract, for example 'AAPL' for US Stock - Apple Inc.
exchange = 'exchange_example' # str | Native exchange for contract, for example 'NASDAQ' for US Stock - Apple Inc. (optional)

try:
    # Get trading schedule for symbol
    api_response = api_instance.trsrv_secdef_schedule_get(asset_class, symbol, exchange=exchange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->trsrv_secdef_schedule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_class** | **str**| specify the asset class of the contract. Available values-- Stock: STK, Option: OPT, Future: FUT, Contract For Difference: CFD, Warrant: WAR, Forex: SWP, Mutual Fund: FND, Bond: BND, Inter-Commodity Spreads: ICS  | 
 **symbol** | **str**| Underlying Symbol for specified contract, for example &#39;AAPL&#39; for US Stock - Apple Inc. | 
 **exchange** | **str**| Native exchange for contract, for example &#39;NASDAQ&#39; for US Stock - Apple Inc. | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trsrv_stocks_get**
> InlineResponse20029 trsrv_stocks_get(symbols)

Security Stocks by Symbol

Returns an object contains all stock contracts for given symbol(s)

### Example
```python
from __future__ import print_function
import time
import ibkr_client
from ibkr_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibkr_client.ContractApi()
symbols = 'symbols_example' # str | list of upper-sensitive symbols separated by comma

try:
    # Security Stocks by Symbol
    api_response = api_instance.trsrv_stocks_get(symbols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->trsrv_stocks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| list of upper-sensitive symbols separated by comma | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

