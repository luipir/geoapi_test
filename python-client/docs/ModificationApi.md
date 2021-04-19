# openapi_client.ModificationApi

All URIs are relative to *https://localhost:8080/luipir/geo_test/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_area**](ModificationApi.md#add_area) | **POST** /areas | Add new/modify Area resource
[**delete_are_by_name**](ModificationApi.md#delete_are_by_name) | **DELETE** /areas/{name} | Delete a Area resource by name.


# **add_area**
> add_area()

Add new/modify Area resource

Add a new Area resource or modify existing if unique name already exist 

### Example

```python
import time
import openapi_client
from openapi_client.api import modification_api
from openapi_client.model.area import Area
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:8080/luipir/geo_test/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:8080/luipir/geo_test/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = modification_api.ModificationApi(api_client)
    area = Area(
        name="Luigi Pirelli",
        date="2021-04-17",
        props=Props(
            key="key_example",
        ),
        poly=Polygon([
            Point3DDict(
                lat=3.14,
                lon=3.14,
                altitude=3.14,
            ),
        ]),
    ) # Area | Area resource to add/substitute (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add new/modify Area resource
        api_instance.add_area(area=area)
    except openapi_client.ApiException as e:
        print("Exception when calling ModificationApi->add_area: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | [**Area**](Area.md)| Area resource to add/substitute | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was created/substited successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_are_by_name**
> [Area] delete_are_by_name(name)

Delete a Area resource by name.

Delete a Area resource by name. 

### Example

```python
import time
import openapi_client
from openapi_client.api import modification_api
from openapi_client.model.area import Area
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:8080/luipir/geo_test/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:8080/luipir/geo_test/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = modification_api.ModificationApi(api_client)
    name = "name_example" # str | resource unique name

    # example passing only required values which don't have defaults set
    try:
        # Delete a Area resource by name.
        api_response = api_instance.delete_are_by_name(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModificationApi->delete_are_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| resource unique name |

### Return type

[**[Area]**](Area.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |
**200** | Operation success |  -  |
**400** | bad input parameter |  -  |
**404** | No resource found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

