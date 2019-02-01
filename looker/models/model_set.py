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


class ModelSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ModelSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'models': 'list[str]',
            'built_in': 'bool',
            'all_access': 'bool',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'models': 'models',
            'built_in': 'built_in',
            'all_access': 'all_access',
            'url': 'url',
            'can': 'can'
        }

        self._id = None
        self._name = None
        self._models = None
        self._built_in = None
        self._all_access = None
        self._url = None
        self._can = None

    @property
    def id(self):
        """
        Gets the id of this ModelSet.
        Unique Id

        :return: The id of this ModelSet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ModelSet.
        Unique Id

        :param id: The id of this ModelSet.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ModelSet.
        Name of ModelSet

        :return: The name of this ModelSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModelSet.
        Name of ModelSet

        :param name: The name of this ModelSet.
        :type: str
        """
        self._name = name

    @property
    def models(self):
        """
        Gets the models of this ModelSet.


        :return: The models of this ModelSet.
        :rtype: list[str]
        """
        return self._models

    @models.setter
    def models(self, models):
        """
        Sets the models of this ModelSet.


        :param models: The models of this ModelSet.
        :type: list[str]
        """
        self._models = models

    @property
    def built_in(self):
        """
        Gets the built_in of this ModelSet.


        :return: The built_in of this ModelSet.
        :rtype: bool
        """
        return self._built_in

    @built_in.setter
    def built_in(self, built_in):
        """
        Sets the built_in of this ModelSet.


        :param built_in: The built_in of this ModelSet.
        :type: bool
        """
        self._built_in = built_in

    @property
    def all_access(self):
        """
        Gets the all_access of this ModelSet.


        :return: The all_access of this ModelSet.
        :rtype: bool
        """
        return self._all_access

    @all_access.setter
    def all_access(self, all_access):
        """
        Sets the all_access of this ModelSet.


        :param all_access: The all_access of this ModelSet.
        :type: bool
        """
        self._all_access = all_access

    @property
    def url(self):
        """
        Gets the url of this ModelSet.
        Link to get this item

        :return: The url of this ModelSet.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ModelSet.
        Link to get this item

        :param url: The url of this ModelSet.
        :type: str
        """
        self._url = url

    @property
    def can(self):
        """
        Gets the can of this ModelSet.
        Operations the current user is able to perform on this object

        :return: The can of this ModelSet.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this ModelSet.
        Operations the current user is able to perform on this object

        :param can: The can of this ModelSet.
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

