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


class ValidationError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ValidationError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'errors': 'list[ValidationErrorDetail]',
            'documentation_url': 'str'
        }

        self.attribute_map = {
            'message': 'message',
            'errors': 'errors',
            'documentation_url': 'documentation_url'
        }

        self._message = None
        self._errors = None
        self._documentation_url = None

    @property
    def message(self):
        """
        Gets the message of this ValidationError.
        Error details

        :return: The message of this ValidationError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ValidationError.
        Error details

        :param message: The message of this ValidationError.
        :type: str
        """
        self._message = message

    @property
    def errors(self):
        """
        Gets the errors of this ValidationError.
        Error detail array

        :return: The errors of this ValidationError.
        :rtype: list[ValidationErrorDetail]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ValidationError.
        Error detail array

        :param errors: The errors of this ValidationError.
        :type: list[ValidationErrorDetail]
        """
        self._errors = errors

    @property
    def documentation_url(self):
        """
        Gets the documentation_url of this ValidationError.
        Documentation link

        :return: The documentation_url of this ValidationError.
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """
        Sets the documentation_url of this ValidationError.
        Documentation link

        :param documentation_url: The documentation_url of this ValidationError.
        :type: str
        """
        self._documentation_url = documentation_url

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
