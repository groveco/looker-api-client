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


class LDAPUserAttributeRead(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LDAPUserAttributeRead - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'required': 'bool',
            'user_attributes': 'list[UserAttribute]',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'name': 'name',
            'required': 'required',
            'user_attributes': 'user_attributes',
            'url': 'url',
            'can': 'can'
        }

        self._name = None
        self._required = None
        self._user_attributes = None
        self._url = None
        self._can = None

    @property
    def name(self):
        """
        Gets the name of this LDAPUserAttributeRead.
        Name of User Attribute in LDAP

        :return: The name of this LDAPUserAttributeRead.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LDAPUserAttributeRead.
        Name of User Attribute in LDAP

        :param name: The name of this LDAPUserAttributeRead.
        :type: str
        """
        self._name = name

    @property
    def required(self):
        """
        Gets the required of this LDAPUserAttributeRead.
        Required to be in LDAP assertion for login to be allowed to succeed

        :return: The required of this LDAPUserAttributeRead.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this LDAPUserAttributeRead.
        Required to be in LDAP assertion for login to be allowed to succeed

        :param required: The required of this LDAPUserAttributeRead.
        :type: bool
        """
        self._required = required

    @property
    def user_attributes(self):
        """
        Gets the user_attributes of this LDAPUserAttributeRead.
        Looker User Attributes

        :return: The user_attributes of this LDAPUserAttributeRead.
        :rtype: list[UserAttribute]
        """
        return self._user_attributes

    @user_attributes.setter
    def user_attributes(self, user_attributes):
        """
        Sets the user_attributes of this LDAPUserAttributeRead.
        Looker User Attributes

        :param user_attributes: The user_attributes of this LDAPUserAttributeRead.
        :type: list[UserAttribute]
        """
        self._user_attributes = user_attributes

    @property
    def url(self):
        """
        Gets the url of this LDAPUserAttributeRead.
        Link to LDAP config

        :return: The url of this LDAPUserAttributeRead.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this LDAPUserAttributeRead.
        Link to LDAP config

        :param url: The url of this LDAPUserAttributeRead.
        :type: str
        """
        self._url = url

    @property
    def can(self):
        """
        Gets the can of this LDAPUserAttributeRead.
        Operations the current user is able to perform on this object

        :return: The can of this LDAPUserAttributeRead.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this LDAPUserAttributeRead.
        Operations the current user is able to perform on this object

        :param can: The can of this LDAPUserAttributeRead.
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

