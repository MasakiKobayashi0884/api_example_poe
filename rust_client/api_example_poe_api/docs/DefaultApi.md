# \DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bytes_pure_bytes_get**](DefaultApi.md#bytes_pure_bytes_get) | **GET** /pure/bytes | Bytes 
[**enum_io_enum_enum_io_post**](DefaultApi.md#enum_io_enum_enum_io_post) | **POST** /enum/enum_io | Enum Io
[**gif_frame_media_gif_frame_get**](DefaultApi.md#gif_frame_media_gif_frame_get) | **GET** /media/gif/{frame} | Gif Frame
[**gif_media_gif_get**](DefaultApi.md#gif_media_gif_get) | **GET** /media/gif | Gif
[**health_check_health_check_get**](DefaultApi.md#health_check_health_check_get) | **GET** /health_check | Health Check
[**image_pil_media_image_pil_get**](DefaultApi.md#image_pil_media_image_pil_get) | **GET** /media/image_pil | Image Pil
[**path_param_params_path_p_get**](DefaultApi.md#path_param_params_path_p_get) | **GET** /params/{path_p} | Path Param
[**str_pure_str_get**](DefaultApi.md#str_pure_str_get) | **GET** /pure/str | Str 
[**text_pure_text_get**](DefaultApi.md#text_pure_text_get) | **GET** /pure/text | Text
[**union_model_labsunion_post**](DefaultApi.md#union_model_labsunion_post) | **POST** /labsunion | Union Model



## bytes_pure_bytes_get

> std::path::PathBuf bytes_pure_bytes_get()
Bytes 

### Parameters

This endpoint does not need any parameter.

### Return type

[**std::path::PathBuf**](std::path::PathBuf.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## enum_io_enum_enum_io_post

> crate::models::EnumModel enum_io_enum_enum_io_post(enum_model)
Enum Io

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**enum_model** | [**EnumModel**](EnumModel.md) |  | [required] |

### Return type

[**crate::models::EnumModel**](EnumModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## gif_frame_media_gif_frame_get

> String gif_frame_media_gif_frame_get(frame)
Gif Frame

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**frame** | **i32** |  | [required] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## gif_media_gif_get

> String gif_media_gif_get()
Gif

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/gif

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## health_check_health_check_get

> ::std::collections::HashMap<String, String> health_check_health_check_get()
Health Check

### Parameters

This endpoint does not need any parameter.

### Return type

**::std::collections::HashMap<String, String>**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## image_pil_media_image_pil_get

> String image_pil_media_image_pil_get()
Image Pil

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## path_param_params_path_p_get

> crate::models::ParamRespModel path_param_params_path_p_get(path_p, query_p)
Path Param

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path_p** | **String** |  | [required] |
**query_p** | **f32** |  | [required] |

### Return type

[**crate::models::ParamRespModel**](ParamRespModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## str_pure_str_get

> String str_pure_str_get()
Str 

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## text_pure_text_get

> String text_pure_text_get()
Text

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## union_model_labsunion_post

> crate::models::UnionModel union_model_labsunion_post(union_model)
Union Model

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**union_model** | [**UnionModel**](UnionModel.md) |  | [required] |

### Return type

[**crate::models::UnionModel**](UnionModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

