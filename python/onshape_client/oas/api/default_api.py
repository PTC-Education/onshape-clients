# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.103
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from onshape_client.oas.api_client import ApiClient
from onshape_client.oas.exceptions import (
    ApiTypeError,
    ApiValueError
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_open_api(self, **kwargs):  # noqa: E501
        """OpenAPI spec documentation for the Onshape REST API.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_open_api(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str file_type: The type of file to return. Defaults to JSON.
        :param str excluded_tags: If an operation contains an excluded tag, it is not returned from this endpoint.
        :param str included_tags: Return at most all the operations with tags included in includedTags. If not given, this will default to all tags.
        :param bool include_deprecated: Include deprecated endpoints.
        :param list[str] documentation_status: Only return endpoints that have the specified document status. Default is to return all the endpoints the user should have access to.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: OpenAPI
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_open_api_with_http_info(**kwargs)  # noqa: E501

    def get_open_api_with_http_info(self, **kwargs):  # noqa: E501
        """OpenAPI spec documentation for the Onshape REST API.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_open_api_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str file_type: The type of file to return. Defaults to JSON.
        :param str excluded_tags: If an operation contains an excluded tag, it is not returned from this endpoint.
        :param str included_tags: Return at most all the operations with tags included in includedTags. If not given, this will default to all tags.
        :param bool include_deprecated: Include deprecated endpoints.
        :param list[str] documentation_status: Only return endpoints that have the specified document status. Default is to return all the endpoints the user should have access to.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(OpenAPI, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['file_type', 'excluded_tags', 'included_tags', 'include_deprecated', 'documentation_status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_open_api" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_type' in local_var_params:
            query_params.append(('fileType', local_var_params['file_type']))  # noqa: E501
        if 'excluded_tags' in local_var_params:
            query_params.append(('excludedTags', local_var_params['excluded_tags']))  # noqa: E501
        if 'included_tags' in local_var_params:
            query_params.append(('includedTags', local_var_params['included_tags']))  # noqa: E501
        if 'include_deprecated' in local_var_params:
            query_params.append(('includeDeprecated', local_var_params['include_deprecated']))  # noqa: E501
        if 'documentation_status' in local_var_params:
            query_params.append(('documentationStatus', local_var_params['documentation_status']))  # noqa: E501
            collection_formats['documentationStatus'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/openapi', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OpenAPI',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
