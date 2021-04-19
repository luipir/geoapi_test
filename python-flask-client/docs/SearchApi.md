# openapi_client.SearchApi

All URIs are relative to *https://localhost:8080/luipir/geo_test/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_area_by_date**](SearchApi.md#get_area_by_date) | **GET** /areas/date/{date} | Retrieve a Area with a specified data.
[**get_area_by_name**](SearchApi.md#get_area_by_name) | **GET** /areas/{name} | Retrieve a Area resource by unique name.
[**get_area_by_properties**](SearchApi.md#get_area_by_properties) | **POST** /areas/properties | Retrieve a Area with a specified data set of properties.
[**get_intersect**](SearchApi.md#get_intersect) | **POST** /areas/intersect | Retrieve a Area inteersecting posted polygon.
[**get_intersection**](SearchApi.md#get_intersection) | **POST** /areas/intersection | Retrieve Area inside input polygon.


# **get_area_by_date**
> [Area] get_area_by_date(date)

Retrieve a Area with a specified data.

Retrieve a Area resource by date. 

### Example

```python
import time
import openapi_client
from openapi_client.api import search_api
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
    api_instance = search_api.SearchApi(api_client)
    date = "2021-01-30" # str | Get all resources containing the name

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Area with a specified data.
        api_response = api_instance.get_area_by_date(date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_area_by_date: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **str**| Get all resources containing the name |

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
**200** | Operation success |  -  |
**400** | bad input parameter |  -  |
**404** | No resource found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_area_by_name**
> [Area] get_area_by_name(name)

Retrieve a Area resource by unique name.

Retrieve a Area resource by unique name. 

### Example

```python
import time
import openapi_client
from openapi_client.api import search_api
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
    api_instance = search_api.SearchApi(api_client)
    name = "name_example" # str | resource unique name

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Area resource by unique name.
        api_response = api_instance.get_area_by_name(name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_area_by_name: %s\n" % e)
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
**200** | Operation success |  -  |
**400** | bad input parameter |  -  |
**404** | No resource found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_area_by_properties**
> [Area] get_area_by_properties()

Retrieve a Area with a specified data set of properties.

Retrieve a Area resource by properties dict. 

### Example

```python
import time
import openapi_client
from openapi_client.api import search_api
from openapi_client.model.area import Area
from openapi_client.model.props import Props
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:8080/luipir/geo_test/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:8080/luipir/geo_test/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    props = Props(
        key="key_example",
    ) # Props | Area to retrieve with matching properties (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a Area with a specified data set of properties.
        api_response = api_instance.get_area_by_properties(props=props)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_area_by_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **props** | [**Props**](Props.md)| Area to retrieve with matching properties | [optional]

### Return type

[**[Area]**](Area.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation success |  -  |
**400** | bad input parameter |  -  |
**404** | No resource found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intersect**
> [Area] get_intersect()

Retrieve a Area inteersecting posted polygon.

Retrieve intersecting Area resources  

### Example

```python
import time
import openapi_client
from openapi_client.api import search_api
from openapi_client.model.area import Area
from openapi_client.model.polygon import Polygon
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:8080/luipir/geo_test/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:8080/luipir/geo_test/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    polygon = Polygon([
        Point3DDict(
            lat=3.14,
            lon=3.14,
            altitude=3.14,
        ),
    ]) # Polygon | Polygon to retrieve intersecting Area resources (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a Area inteersecting posted polygon.
        api_response = api_instance.get_intersect(polygon=polygon)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_intersect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **polygon** | [**Polygon**](Polygon.md)| Polygon to retrieve intersecting Area resources | [optional]

### Return type

[**[Area]**](Area.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation success |  -  |
**400** | bad input parameter |  -  |
**404** | No resource found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intersection**
> [Area] get_intersection()

Retrieve Area inside input polygon.

Retrieve Area inside input polygon 

### Example

```python
import time
import openapi_client
from openapi_client.api import search_api
from openapi_client.model.area import Area
from openapi_client.model.polygon import Polygon
from pprint import pprint
# Defining the host is optional and defaults to https://localhost:8080/luipir/geo_test/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:8080/luipir/geo_test/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    polygon = Polygon([
        Point3DDict(
            lat=3.14,
            lon=3.14,
            altitude=3.14,
        ),
    ]) # Polygon | Polygon to retrieve inner Area resources (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Area inside input polygon.
        api_response = api_instance.get_intersection(polygon=polygon)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_intersection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **polygon** | [**Polygon**](Polygon.md)| Polygon to retrieve inner Area resources | [optional]

### Return type

[**[Area]**](Area.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation success |  -  |
**400** | bad input parameter |  -  |
**404** | No resource found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

