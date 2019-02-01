# coding: utf-8

"""
IntegrationApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class IntegrationApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def accept_integration_hub_legal_agreement(self, integration_hub_id, **kwargs):
        """
        Accept Integration Hub Legal Agreement
        Accepts the legal agreement for a given integration hub. This only works for integration hubs that have legal_agreement_required set to true and legal_agreement_signed set to false.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.accept_integration_hub_legal_agreement(integration_hub_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int integration_hub_id: Id of integration_hub (required)
        :return: IntegrationHub
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_hub_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_integration_hub_legal_agreement" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_hub_id' is set
        if ('integration_hub_id' not in params) or (params['integration_hub_id'] is None):
            raise ValueError("Missing the required parameter `integration_hub_id` when calling `accept_integration_hub_legal_agreement`")

        resource_path = '/integration_hubs/{integration_hub_id}/accept_legal_agreement'.replace('{format}', 'json')
        path_params = {}
        if 'integration_hub_id' in params:
            path_params['integration_hub_id'] = params['integration_hub_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='IntegrationHub',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def all_integration_hubs(self, **kwargs):
        """
        Get All Integration Hubs
        ### Get information about all Integration Hubs.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_integration_hubs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :return: list[IntegrationHub]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_integration_hubs" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/integration_hubs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[IntegrationHub]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def all_integrations(self, **kwargs):
        """
        Get All Integrations
        ### Get information about all Integrations.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_integrations(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :param str integration_hub_id: Filter to a specific provider
        :return: list[Integration]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'integration_hub_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_integrations" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/integrations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'integration_hub_id' in params:
            query_params['integration_hub_id'] = params['integration_hub_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Integration]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_integration_hub(self, **kwargs):
        """
        Create Integration Hub
        ### Create a new Integration Hub.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_integration_hub(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param IntegrationHub body: Integration Hub
        :param str fields: Requested fields.
        :return: IntegrationHub
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_integration_hub" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/integration_hubs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='IntegrationHub',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_integration_hub(self, integration_hub_id, **kwargs):
        """
        Delete Integration Hub
        ### Delete a Integration Hub.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_integration_hub(integration_hub_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int integration_hub_id: Id of integration_hub (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_hub_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_integration_hub" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_hub_id' is set
        if ('integration_hub_id' not in params) or (params['integration_hub_id'] is None):
            raise ValueError("Missing the required parameter `integration_hub_id` when calling `delete_integration_hub`")

        resource_path = '/integration_hubs/{integration_hub_id}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_hub_id' in params:
            path_params['integration_hub_id'] = params['integration_hub_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def fetch_integration_form(self, integration_id, **kwargs):
        """
        Fetch Remote Integration Form
        Returns the Integration form for presentation to the user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.fetch_integration_form(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int integration_id: Id of Integration (required)
        :return: DataActionForm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_integration_form" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `fetch_integration_form`")

        resource_path = '/integrations/{integration_id}/form'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integration_id'] = params['integration_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DataActionForm',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def integration(self, integration_id, **kwargs):
        """
        Get Integration
        ### Get information about a Integration.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.integration(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int integration_id: Id of Integration (required)
        :param str fields: Requested fields.
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method integration" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `integration`")

        resource_path = '/integrations/{integration_id}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integration_id'] = params['integration_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Integration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def integration_hub(self, integration_hub_id, **kwargs):
        """
        Get Integration Hub
        ### Get information about a Integration Hub.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.integration_hub(integration_hub_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int integration_hub_id: Id of Integration Hub (required)
        :param str fields: Requested fields.
        :return: IntegrationHub
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_hub_id', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method integration_hub" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_hub_id' is set
        if ('integration_hub_id' not in params) or (params['integration_hub_id'] is None):
            raise ValueError("Missing the required parameter `integration_hub_id` when calling `integration_hub`")

        resource_path = '/integration_hubs/{integration_hub_id}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_hub_id' in params:
            path_params['integration_hub_id'] = params['integration_hub_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='IntegrationHub',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def test_integration(self, integration_id, **kwargs):
        """
        Test integration
        Tests the integration to make sure all the settings are working.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_integration(integration_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int integration_id: Id of Integration (required)
        :return: IntegrationTestResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_integration" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `test_integration`")

        resource_path = '/integrations/{integration_id}/test'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integration_id'] = params['integration_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='IntegrationTestResult',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_integration(self, integration_id, body, **kwargs):
        """
        Update Integration
        ### Update parameters on a Integration.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_integration(integration_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int integration_id: Id of Integration (required)
        :param Integration body: Integration (required)
        :param str fields: Requested fields.
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'body', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_integration" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params) or (params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `update_integration`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_integration`")

        resource_path = '/integrations/{integration_id}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_id' in params:
            path_params['integration_id'] = params['integration_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Integration',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_integration_hub(self, integration_hub_id, body, **kwargs):
        """
        Update Integration Hub
        ### Update a Integration Hub definition.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_integration_hub(integration_hub_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int integration_hub_id: Id of Integration Hub (required)
        :param IntegrationHub body: Integration Hub (required)
        :param str fields: Requested fields.
        :return: IntegrationHub
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_hub_id', 'body', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_integration_hub" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'integration_hub_id' is set
        if ('integration_hub_id' not in params) or (params['integration_hub_id'] is None):
            raise ValueError("Missing the required parameter `integration_hub_id` when calling `update_integration_hub`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_integration_hub`")

        resource_path = '/integration_hubs/{integration_hub_id}'.replace('{format}', 'json')
        path_params = {}
        if 'integration_hub_id' in params:
            path_params['integration_hub_id'] = params['integration_hub_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='IntegrationHub',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response