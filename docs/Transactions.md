# Transactions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | will always be getTransactions | [optional] 
**currency** | **str** | same as request | [optional] 
**includes_real_time** | **bool** | Indicates whether current day and realtime data is included in the result | [optional] 
**_from** | **float** | Period start date. Epoch time, GMT | [optional] 
**to** | **float** | Period end date. Epoch time, GMT | [optional] 
**transactions** | [**list[TransactionsTransactions]**](TransactionsTransactions.md) | Sorted by date descending | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


