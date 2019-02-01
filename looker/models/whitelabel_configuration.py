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


class WhitelabelConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WhitelabelConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'logo_file': 'str',
            'logo_url': 'str',
            'favicon_file': 'str',
            'favicon_url': 'str',
            'default_title': 'str',
            'show_help_menu': 'bool',
            'show_docs': 'bool',
            'show_email_sub_options': 'bool',
            'allow_looker_mentions': 'bool',
            'allow_looker_links': 'bool',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'logo_file': 'logo_file',
            'logo_url': 'logo_url',
            'favicon_file': 'favicon_file',
            'favicon_url': 'favicon_url',
            'default_title': 'default_title',
            'show_help_menu': 'show_help_menu',
            'show_docs': 'show_docs',
            'show_email_sub_options': 'show_email_sub_options',
            'allow_looker_mentions': 'allow_looker_mentions',
            'allow_looker_links': 'allow_looker_links',
            'can': 'can'
        }

        self._id = None
        self._logo_file = None
        self._logo_url = None
        self._favicon_file = None
        self._favicon_url = None
        self._default_title = None
        self._show_help_menu = None
        self._show_docs = None
        self._show_email_sub_options = None
        self._allow_looker_mentions = None
        self._allow_looker_links = None
        self._can = None

    @property
    def id(self):
        """
        Gets the id of this WhitelabelConfiguration.
        Unique Id

        :return: The id of this WhitelabelConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WhitelabelConfiguration.
        Unique Id

        :param id: The id of this WhitelabelConfiguration.
        :type: int
        """
        self._id = id

    @property
    def logo_file(self):
        """
        Gets the logo_file of this WhitelabelConfiguration.
        Customer logo image. Expected base64 encoded data (write-only)

        :return: The logo_file of this WhitelabelConfiguration.
        :rtype: str
        """
        return self._logo_file

    @logo_file.setter
    def logo_file(self, logo_file):
        """
        Sets the logo_file of this WhitelabelConfiguration.
        Customer logo image. Expected base64 encoded data (write-only)

        :param logo_file: The logo_file of this WhitelabelConfiguration.
        :type: str
        """
        self._logo_file = logo_file

    @property
    def logo_url(self):
        """
        Gets the logo_url of this WhitelabelConfiguration.
        Logo image url (read-only)

        :return: The logo_url of this WhitelabelConfiguration.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """
        Sets the logo_url of this WhitelabelConfiguration.
        Logo image url (read-only)

        :param logo_url: The logo_url of this WhitelabelConfiguration.
        :type: str
        """
        self._logo_url = logo_url

    @property
    def favicon_file(self):
        """
        Gets the favicon_file of this WhitelabelConfiguration.
        Custom favicon image. Expected base64 encoded data (write-only)

        :return: The favicon_file of this WhitelabelConfiguration.
        :rtype: str
        """
        return self._favicon_file

    @favicon_file.setter
    def favicon_file(self, favicon_file):
        """
        Sets the favicon_file of this WhitelabelConfiguration.
        Custom favicon image. Expected base64 encoded data (write-only)

        :param favicon_file: The favicon_file of this WhitelabelConfiguration.
        :type: str
        """
        self._favicon_file = favicon_file

    @property
    def favicon_url(self):
        """
        Gets the favicon_url of this WhitelabelConfiguration.
        Favicon image url (read-only)

        :return: The favicon_url of this WhitelabelConfiguration.
        :rtype: str
        """
        return self._favicon_url

    @favicon_url.setter
    def favicon_url(self, favicon_url):
        """
        Sets the favicon_url of this WhitelabelConfiguration.
        Favicon image url (read-only)

        :param favicon_url: The favicon_url of this WhitelabelConfiguration.
        :type: str
        """
        self._favicon_url = favicon_url

    @property
    def default_title(self):
        """
        Gets the default_title of this WhitelabelConfiguration.
        Default page title

        :return: The default_title of this WhitelabelConfiguration.
        :rtype: str
        """
        return self._default_title

    @default_title.setter
    def default_title(self, default_title):
        """
        Sets the default_title of this WhitelabelConfiguration.
        Default page title

        :param default_title: The default_title of this WhitelabelConfiguration.
        :type: str
        """
        self._default_title = default_title

    @property
    def show_help_menu(self):
        """
        Gets the show_help_menu of this WhitelabelConfiguration.
        Boolean to toggle showing help menus

        :return: The show_help_menu of this WhitelabelConfiguration.
        :rtype: bool
        """
        return self._show_help_menu

    @show_help_menu.setter
    def show_help_menu(self, show_help_menu):
        """
        Sets the show_help_menu of this WhitelabelConfiguration.
        Boolean to toggle showing help menus

        :param show_help_menu: The show_help_menu of this WhitelabelConfiguration.
        :type: bool
        """
        self._show_help_menu = show_help_menu

    @property
    def show_docs(self):
        """
        Gets the show_docs of this WhitelabelConfiguration.
        Boolean to toggle showing docs

        :return: The show_docs of this WhitelabelConfiguration.
        :rtype: bool
        """
        return self._show_docs

    @show_docs.setter
    def show_docs(self, show_docs):
        """
        Sets the show_docs of this WhitelabelConfiguration.
        Boolean to toggle showing docs

        :param show_docs: The show_docs of this WhitelabelConfiguration.
        :type: bool
        """
        self._show_docs = show_docs

    @property
    def show_email_sub_options(self):
        """
        Gets the show_email_sub_options of this WhitelabelConfiguration.
        Boolean to toggle showing email subscription options.

        :return: The show_email_sub_options of this WhitelabelConfiguration.
        :rtype: bool
        """
        return self._show_email_sub_options

    @show_email_sub_options.setter
    def show_email_sub_options(self, show_email_sub_options):
        """
        Sets the show_email_sub_options of this WhitelabelConfiguration.
        Boolean to toggle showing email subscription options.

        :param show_email_sub_options: The show_email_sub_options of this WhitelabelConfiguration.
        :type: bool
        """
        self._show_email_sub_options = show_email_sub_options

    @property
    def allow_looker_mentions(self):
        """
        Gets the allow_looker_mentions of this WhitelabelConfiguration.
        Boolean to toggle mentions of Looker in emails

        :return: The allow_looker_mentions of this WhitelabelConfiguration.
        :rtype: bool
        """
        return self._allow_looker_mentions

    @allow_looker_mentions.setter
    def allow_looker_mentions(self, allow_looker_mentions):
        """
        Sets the allow_looker_mentions of this WhitelabelConfiguration.
        Boolean to toggle mentions of Looker in emails

        :param allow_looker_mentions: The allow_looker_mentions of this WhitelabelConfiguration.
        :type: bool
        """
        self._allow_looker_mentions = allow_looker_mentions

    @property
    def allow_looker_links(self):
        """
        Gets the allow_looker_links of this WhitelabelConfiguration.
        Boolean to toggle links to Looker in emails

        :return: The allow_looker_links of this WhitelabelConfiguration.
        :rtype: bool
        """
        return self._allow_looker_links

    @allow_looker_links.setter
    def allow_looker_links(self, allow_looker_links):
        """
        Sets the allow_looker_links of this WhitelabelConfiguration.
        Boolean to toggle links to Looker in emails

        :param allow_looker_links: The allow_looker_links of this WhitelabelConfiguration.
        :type: bool
        """
        self._allow_looker_links = allow_looker_links

    @property
    def can(self):
        """
        Gets the can of this WhitelabelConfiguration.
        Operations the current user is able to perform on this object

        :return: The can of this WhitelabelConfiguration.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this WhitelabelConfiguration.
        Operations the current user is able to perform on this object

        :param can: The can of this WhitelabelConfiguration.
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

