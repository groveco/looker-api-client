# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class QueryTask(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueryTask - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'query_id': 'int',
            'query': 'Query',
            'generate_links': 'bool',
            'force_production': 'bool',
            'path_prefix': 'str',
            'cache': 'bool',
            'server_table_calcs': 'bool',
            'cache_only': 'bool',
            'cache_key': 'str',
            'status': 'str',
            'source': 'str',
            'runtime': 'float',
            'rebuild_pdts': 'bool',
            'result_source': 'str',
            'look_id': 'int',
            'dashboard_id': 'str',
            'result_format': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'query_id': 'query_id',
            'query': 'query',
            'generate_links': 'generate_links',
            'force_production': 'force_production',
            'path_prefix': 'path_prefix',
            'cache': 'cache',
            'server_table_calcs': 'server_table_calcs',
            'cache_only': 'cache_only',
            'cache_key': 'cache_key',
            'status': 'status',
            'source': 'source',
            'runtime': 'runtime',
            'rebuild_pdts': 'rebuild_pdts',
            'result_source': 'result_source',
            'look_id': 'look_id',
            'dashboard_id': 'dashboard_id',
            'result_format': 'result_format',
            'can': 'can'
        }

        self._id = None
        self._query_id = None
        self._query = None
        self._generate_links = None
        self._force_production = None
        self._path_prefix = None
        self._cache = None
        self._server_table_calcs = None
        self._cache_only = None
        self._cache_key = None
        self._status = None
        self._source = None
        self._runtime = None
        self._rebuild_pdts = None
        self._result_source = None
        self._look_id = None
        self._dashboard_id = None
        self._result_format = None
        self._can = None

    @property
    def id(self):
        """
        Gets the id of this QueryTask.
        Unique Id

        :return: The id of this QueryTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueryTask.
        Unique Id

        :param id: The id of this QueryTask.
        :type: str
        """
        self._id = id

    @property
    def query_id(self):
        """
        Gets the query_id of this QueryTask.
        Id of query

        :return: The query_id of this QueryTask.
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """
        Sets the query_id of this QueryTask.
        Id of query

        :param query_id: The query_id of this QueryTask.
        :type: int
        """
        self._query_id = query_id

    @property
    def query(self):
        """
        Gets the query of this QueryTask.
        Query

        :return: The query of this QueryTask.
        :rtype: Query
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this QueryTask.
        Query

        :param query: The query of this QueryTask.
        :type: Query
        """
        self._query = query

    @property
    def generate_links(self):
        """
        Gets the generate_links of this QueryTask.
        whether or not to generate links in the query response.

        :return: The generate_links of this QueryTask.
        :rtype: bool
        """
        return self._generate_links

    @generate_links.setter
    def generate_links(self, generate_links):
        """
        Sets the generate_links of this QueryTask.
        whether or not to generate links in the query response.

        :param generate_links: The generate_links of this QueryTask.
        :type: bool
        """
        self._generate_links = generate_links

    @property
    def force_production(self):
        """
        Gets the force_production of this QueryTask.
        Use production models to run query (even is user is in dev mode).

        :return: The force_production of this QueryTask.
        :rtype: bool
        """
        return self._force_production

    @force_production.setter
    def force_production(self, force_production):
        """
        Sets the force_production of this QueryTask.
        Use production models to run query (even is user is in dev mode).

        :param force_production: The force_production of this QueryTask.
        :type: bool
        """
        self._force_production = force_production

    @property
    def path_prefix(self):
        """
        Gets the path_prefix of this QueryTask.
        Prefix to use for drill links.

        :return: The path_prefix of this QueryTask.
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix):
        """
        Sets the path_prefix of this QueryTask.
        Prefix to use for drill links.

        :param path_prefix: The path_prefix of this QueryTask.
        :type: str
        """
        self._path_prefix = path_prefix

    @property
    def cache(self):
        """
        Gets the cache of this QueryTask.
        Whether or not to use the cache

        :return: The cache of this QueryTask.
        :rtype: bool
        """
        return self._cache

    @cache.setter
    def cache(self, cache):
        """
        Sets the cache of this QueryTask.
        Whether or not to use the cache

        :param cache: The cache of this QueryTask.
        :type: bool
        """
        self._cache = cache

    @property
    def server_table_calcs(self):
        """
        Gets the server_table_calcs of this QueryTask.
        Whether or not to run table calculations on the server

        :return: The server_table_calcs of this QueryTask.
        :rtype: bool
        """
        return self._server_table_calcs

    @server_table_calcs.setter
    def server_table_calcs(self, server_table_calcs):
        """
        Sets the server_table_calcs of this QueryTask.
        Whether or not to run table calculations on the server

        :param server_table_calcs: The server_table_calcs of this QueryTask.
        :type: bool
        """
        self._server_table_calcs = server_table_calcs

    @property
    def cache_only(self):
        """
        Gets the cache_only of this QueryTask.
        Retrieve any results from cache even if the results have expired.

        :return: The cache_only of this QueryTask.
        :rtype: bool
        """
        return self._cache_only

    @cache_only.setter
    def cache_only(self, cache_only):
        """
        Sets the cache_only of this QueryTask.
        Retrieve any results from cache even if the results have expired.

        :param cache_only: The cache_only of this QueryTask.
        :type: bool
        """
        self._cache_only = cache_only

    @property
    def cache_key(self):
        """
        Gets the cache_key of this QueryTask.
        cache key used to cache query.

        :return: The cache_key of this QueryTask.
        :rtype: str
        """
        return self._cache_key

    @cache_key.setter
    def cache_key(self, cache_key):
        """
        Sets the cache_key of this QueryTask.
        cache key used to cache query.

        :param cache_key: The cache_key of this QueryTask.
        :type: str
        """
        self._cache_key = cache_key

    @property
    def status(self):
        """
        Gets the status of this QueryTask.
        Status of query task.

        :return: The status of this QueryTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this QueryTask.
        Status of query task.

        :param status: The status of this QueryTask.
        :type: str
        """
        self._status = status

    @property
    def source(self):
        """
        Gets the source of this QueryTask.
        Source of query task.

        :return: The source of this QueryTask.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this QueryTask.
        Source of query task.

        :param source: The source of this QueryTask.
        :type: str
        """
        self._source = source

    @property
    def runtime(self):
        """
        Gets the runtime of this QueryTask.
        Runtime of prior queries.

        :return: The runtime of this QueryTask.
        :rtype: float
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """
        Sets the runtime of this QueryTask.
        Runtime of prior queries.

        :param runtime: The runtime of this QueryTask.
        :type: float
        """
        self._runtime = runtime

    @property
    def rebuild_pdts(self):
        """
        Gets the rebuild_pdts of this QueryTask.
        Rebuild PDTS used in query.

        :return: The rebuild_pdts of this QueryTask.
        :rtype: bool
        """
        return self._rebuild_pdts

    @rebuild_pdts.setter
    def rebuild_pdts(self, rebuild_pdts):
        """
        Sets the rebuild_pdts of this QueryTask.
        Rebuild PDTS used in query.

        :param rebuild_pdts: The rebuild_pdts of this QueryTask.
        :type: bool
        """
        self._rebuild_pdts = rebuild_pdts

    @property
    def result_source(self):
        """
        Gets the result_source of this QueryTask.
        Source of the results of the query.

        :return: The result_source of this QueryTask.
        :rtype: str
        """
        return self._result_source

    @result_source.setter
    def result_source(self, result_source):
        """
        Sets the result_source of this QueryTask.
        Source of the results of the query.

        :param result_source: The result_source of this QueryTask.
        :type: str
        """
        self._result_source = result_source

    @property
    def look_id(self):
        """
        Gets the look_id of this QueryTask.
        Id of look associated with query.

        :return: The look_id of this QueryTask.
        :rtype: int
        """
        return self._look_id

    @look_id.setter
    def look_id(self, look_id):
        """
        Sets the look_id of this QueryTask.
        Id of look associated with query.

        :param look_id: The look_id of this QueryTask.
        :type: int
        """
        self._look_id = look_id

    @property
    def dashboard_id(self):
        """
        Gets the dashboard_id of this QueryTask.
        Id of dashboard associated with query.

        :return: The dashboard_id of this QueryTask.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """
        Sets the dashboard_id of this QueryTask.
        Id of dashboard associated with query.

        :param dashboard_id: The dashboard_id of this QueryTask.
        :type: str
        """
        self._dashboard_id = dashboard_id

    @property
    def result_format(self):
        """
        Gets the result_format of this QueryTask.
        The data format of the query results.

        :return: The result_format of this QueryTask.
        :rtype: str
        """
        return self._result_format

    @result_format.setter
    def result_format(self, result_format):
        """
        Sets the result_format of this QueryTask.
        The data format of the query results.

        :param result_format: The result_format of this QueryTask.
        :type: str
        """
        self._result_format = result_format

    @property
    def can(self):
        """
        Gets the can of this QueryTask.
        Operations the current user is able to perform on this object

        :return: The can of this QueryTask.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this QueryTask.
        Operations the current user is able to perform on this object

        :param can: The can of this QueryTask.
        :type: dict(str, bool)
        """
        self._can = can

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

