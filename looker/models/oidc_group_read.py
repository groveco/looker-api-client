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


class OIDCGroupRead(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OIDCGroupRead - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'roles': 'list[Role]',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'name': 'name',
            'roles': 'roles',
            'url': 'url',
            'can': 'can'
        }

        self._name = None
        self._roles = None
        self._url = None
        self._can = None

    @property
    def name(self):
        """
        Gets the name of this OIDCGroupRead.
        Name of group in OIDC

        :return: The name of this OIDCGroupRead.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OIDCGroupRead.
        Name of group in OIDC

        :param name: The name of this OIDCGroupRead.
        :type: str
        """
        self._name = name

    @property
    def roles(self):
        """
        Gets the roles of this OIDCGroupRead.
        Looker Roles

        :return: The roles of this OIDCGroupRead.
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this OIDCGroupRead.
        Looker Roles

        :param roles: The roles of this OIDCGroupRead.
        :type: list[Role]
        """
        self._roles = roles

    @property
    def url(self):
        """
        Gets the url of this OIDCGroupRead.
        Link to oidc config

        :return: The url of this OIDCGroupRead.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this OIDCGroupRead.
        Link to oidc config

        :param url: The url of this OIDCGroupRead.
        :type: str
        """
        self._url = url

    @property
    def can(self):
        """
        Gets the can of this OIDCGroupRead.
        Operations the current user is able to perform on this object

        :return: The can of this OIDCGroupRead.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this OIDCGroupRead.
        Operations the current user is able to perform on this object

        :param can: The can of this OIDCGroupRead.
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

