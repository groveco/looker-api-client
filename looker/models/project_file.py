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


class ProjectFile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProjectFile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'path': 'str',
            'title': 'str',
            'type': 'str',
            'extension': 'str',
            'mime_type': 'str',
            'git_status': 'GitStatus',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'path': 'path',
            'title': 'title',
            'type': 'type',
            'extension': 'extension',
            'mime_type': 'mime_type',
            'git_status': 'git_status',
            'can': 'can'
        }

        self._id = None
        self._path = None
        self._title = None
        self._type = None
        self._extension = None
        self._mime_type = None
        self._git_status = None
        self._can = None

    @property
    def id(self):
        """
        Gets the id of this ProjectFile.
        An opaque token uniquely identifying a file within a project. Avoid parsing or decomposing the text of this token. This token is stable within a Looker release but may change between Looker releases

        :return: The id of this ProjectFile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProjectFile.
        An opaque token uniquely identifying a file within a project. Avoid parsing or decomposing the text of this token. This token is stable within a Looker release but may change between Looker releases

        :param id: The id of this ProjectFile.
        :type: str
        """
        self._id = id

    @property
    def path(self):
        """
        Gets the path of this ProjectFile.
        Path, file name, and extension of the file relative to the project root directory

        :return: The path of this ProjectFile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ProjectFile.
        Path, file name, and extension of the file relative to the project root directory

        :param path: The path of this ProjectFile.
        :type: str
        """
        self._path = path

    @property
    def title(self):
        """
        Gets the title of this ProjectFile.
        Display name

        :return: The title of this ProjectFile.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ProjectFile.
        Display name

        :param title: The title of this ProjectFile.
        :type: str
        """
        self._title = title

    @property
    def type(self):
        """
        Gets the type of this ProjectFile.
        File type: model, view, etc

        :return: The type of this ProjectFile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProjectFile.
        File type: model, view, etc

        :param type: The type of this ProjectFile.
        :type: str
        """
        self._type = type

    @property
    def extension(self):
        """
        Gets the extension of this ProjectFile.
        The extension of the file: .view.lkml, .model.lkml, etc

        :return: The extension of this ProjectFile.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this ProjectFile.
        The extension of the file: .view.lkml, .model.lkml, etc

        :param extension: The extension of this ProjectFile.
        :type: str
        """
        self._extension = extension

    @property
    def mime_type(self):
        """
        Gets the mime_type of this ProjectFile.
        File mime type

        :return: The mime_type of this ProjectFile.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this ProjectFile.
        File mime type

        :param mime_type: The mime_type of this ProjectFile.
        :type: str
        """
        self._mime_type = mime_type

    @property
    def git_status(self):
        """
        Gets the git_status of this ProjectFile.
        Status of the file according to git

        :return: The git_status of this ProjectFile.
        :rtype: GitStatus
        """
        return self._git_status

    @git_status.setter
    def git_status(self, git_status):
        """
        Sets the git_status of this ProjectFile.
        Status of the file according to git

        :param git_status: The git_status of this ProjectFile.
        :type: GitStatus
        """
        self._git_status = git_status

    @property
    def can(self):
        """
        Gets the can of this ProjectFile.
        Operations the current user is able to perform on this object

        :return: The can of this ProjectFile.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this ProjectFile.
        Operations the current user is able to perform on this object

        :param can: The can of this ProjectFile.
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

