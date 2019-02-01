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


class DBConnectionOverride(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DBConnectionOverride - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'context': 'str',
            'host': 'str',
            'port': 'str',
            'username': 'str',
            'password': 'str',
            'has_password': 'bool',
            'certificate': 'str',
            'file_type': 'str',
            'database': 'str',
            'schema': 'str',
            'jdbc_additional_params': 'str',
            'after_connect_statements': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'context': 'context',
            'host': 'host',
            'port': 'port',
            'username': 'username',
            'password': 'password',
            'has_password': 'has_password',
            'certificate': 'certificate',
            'file_type': 'file_type',
            'database': 'database',
            'schema': 'schema',
            'jdbc_additional_params': 'jdbc_additional_params',
            'after_connect_statements': 'after_connect_statements',
            'can': 'can'
        }

        self._context = None
        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self._has_password = None
        self._certificate = None
        self._file_type = None
        self._database = None
        self._schema = None
        self._jdbc_additional_params = None
        self._after_connect_statements = None
        self._can = None

    @property
    def context(self):
        """
        Gets the context of this DBConnectionOverride.
        Context in which to override (`pdt` is the only allowed value)

        :return: The context of this DBConnectionOverride.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this DBConnectionOverride.
        Context in which to override (`pdt` is the only allowed value)

        :param context: The context of this DBConnectionOverride.
        :type: str
        """
        self._context = context

    @property
    def host(self):
        """
        Gets the host of this DBConnectionOverride.
        Host name/address of server

        :return: The host of this DBConnectionOverride.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this DBConnectionOverride.
        Host name/address of server

        :param host: The host of this DBConnectionOverride.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this DBConnectionOverride.
        Port number on server

        :return: The port of this DBConnectionOverride.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this DBConnectionOverride.
        Port number on server

        :param port: The port of this DBConnectionOverride.
        :type: str
        """
        self._port = port

    @property
    def username(self):
        """
        Gets the username of this DBConnectionOverride.
        Username for server authentication

        :return: The username of this DBConnectionOverride.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this DBConnectionOverride.
        Username for server authentication

        :param username: The username of this DBConnectionOverride.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this DBConnectionOverride.
        (Write-Only) Password for server authentication

        :return: The password of this DBConnectionOverride.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this DBConnectionOverride.
        (Write-Only) Password for server authentication

        :param password: The password of this DBConnectionOverride.
        :type: str
        """
        self._password = password

    @property
    def has_password(self):
        """
        Gets the has_password of this DBConnectionOverride.
        Whether or not the password is overridden in this context

        :return: The has_password of this DBConnectionOverride.
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """
        Sets the has_password of this DBConnectionOverride.
        Whether or not the password is overridden in this context

        :param has_password: The has_password of this DBConnectionOverride.
        :type: bool
        """
        self._has_password = has_password

    @property
    def certificate(self):
        """
        Gets the certificate of this DBConnectionOverride.
        (Write-Only) Base64 encoded Certificate body for server authentication (when appropriate for dialect).

        :return: The certificate of this DBConnectionOverride.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this DBConnectionOverride.
        (Write-Only) Base64 encoded Certificate body for server authentication (when appropriate for dialect).

        :param certificate: The certificate of this DBConnectionOverride.
        :type: str
        """
        self._certificate = certificate

    @property
    def file_type(self):
        """
        Gets the file_type of this DBConnectionOverride.
        (Write-Only) Certificate keyfile type - .json or .p12

        :return: The file_type of this DBConnectionOverride.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """
        Sets the file_type of this DBConnectionOverride.
        (Write-Only) Certificate keyfile type - .json or .p12

        :param file_type: The file_type of this DBConnectionOverride.
        :type: str
        """
        self._file_type = file_type

    @property
    def database(self):
        """
        Gets the database of this DBConnectionOverride.
        Database name

        :return: The database of this DBConnectionOverride.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this DBConnectionOverride.
        Database name

        :param database: The database of this DBConnectionOverride.
        :type: str
        """
        self._database = database

    @property
    def schema(self):
        """
        Gets the schema of this DBConnectionOverride.
        Scheme name

        :return: The schema of this DBConnectionOverride.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this DBConnectionOverride.
        Scheme name

        :param schema: The schema of this DBConnectionOverride.
        :type: str
        """
        self._schema = schema

    @property
    def jdbc_additional_params(self):
        """
        Gets the jdbc_additional_params of this DBConnectionOverride.
        Additional params to add to JDBC connection string

        :return: The jdbc_additional_params of this DBConnectionOverride.
        :rtype: str
        """
        return self._jdbc_additional_params

    @jdbc_additional_params.setter
    def jdbc_additional_params(self, jdbc_additional_params):
        """
        Sets the jdbc_additional_params of this DBConnectionOverride.
        Additional params to add to JDBC connection string

        :param jdbc_additional_params: The jdbc_additional_params of this DBConnectionOverride.
        :type: str
        """
        self._jdbc_additional_params = jdbc_additional_params

    @property
    def after_connect_statements(self):
        """
        Gets the after_connect_statements of this DBConnectionOverride.
        SQL statements (semicolon separated) to issue after connecting to the database. Requires `custom_after_connect_statements` license feature

        :return: The after_connect_statements of this DBConnectionOverride.
        :rtype: str
        """
        return self._after_connect_statements

    @after_connect_statements.setter
    def after_connect_statements(self, after_connect_statements):
        """
        Sets the after_connect_statements of this DBConnectionOverride.
        SQL statements (semicolon separated) to issue after connecting to the database. Requires `custom_after_connect_statements` license feature

        :param after_connect_statements: The after_connect_statements of this DBConnectionOverride.
        :type: str
        """
        self._after_connect_statements = after_connect_statements

    @property
    def can(self):
        """
        Gets the can of this DBConnectionOverride.
        Operations the current user is able to perform on this object

        :return: The can of this DBConnectionOverride.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this DBConnectionOverride.
        Operations the current user is able to perform on this object

        :param can: The can of this DBConnectionOverride.
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
