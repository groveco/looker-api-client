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


class Project(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Project - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'uses_git': 'bool',
            'git_remote_url': 'str',
            'git_username': 'str',
            'git_password': 'str',
            'git_username_user_attribute': 'str',
            'git_password_user_attribute': 'str',
            'git_service_name': 'str',
            'deploy_secret': 'str',
            'unset_deploy_secret': 'bool',
            'pull_request_mode': 'str',
            'validation_required': 'bool',
            'allow_warnings': 'bool',
            'is_example': 'bool',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'uses_git': 'uses_git',
            'git_remote_url': 'git_remote_url',
            'git_username': 'git_username',
            'git_password': 'git_password',
            'git_username_user_attribute': 'git_username_user_attribute',
            'git_password_user_attribute': 'git_password_user_attribute',
            'git_service_name': 'git_service_name',
            'deploy_secret': 'deploy_secret',
            'unset_deploy_secret': 'unset_deploy_secret',
            'pull_request_mode': 'pull_request_mode',
            'validation_required': 'validation_required',
            'allow_warnings': 'allow_warnings',
            'is_example': 'is_example',
            'can': 'can'
        }

        self._id = None
        self._name = None
        self._uses_git = None
        self._git_remote_url = None
        self._git_username = None
        self._git_password = None
        self._git_username_user_attribute = None
        self._git_password_user_attribute = None
        self._git_service_name = None
        self._deploy_secret = None
        self._unset_deploy_secret = None
        self._pull_request_mode = None
        self._validation_required = None
        self._allow_warnings = None
        self._is_example = None
        self._can = None

    @property
    def id(self):
        """
        Gets the id of this Project.
        Project Id

        :return: The id of this Project.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Project.
        Project Id

        :param id: The id of this Project.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Project.
        Project display name

        :return: The name of this Project.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Project.
        Project display name

        :param name: The name of this Project.
        :type: str
        """
        self._name = name

    @property
    def uses_git(self):
        """
        Gets the uses_git of this Project.
        If true the project is configured with a git repository

        :return: The uses_git of this Project.
        :rtype: bool
        """
        return self._uses_git

    @uses_git.setter
    def uses_git(self, uses_git):
        """
        Sets the uses_git of this Project.
        If true the project is configured with a git repository

        :param uses_git: The uses_git of this Project.
        :type: bool
        """
        self._uses_git = uses_git

    @property
    def git_remote_url(self):
        """
        Gets the git_remote_url of this Project.
        Git remote repository url

        :return: The git_remote_url of this Project.
        :rtype: str
        """
        return self._git_remote_url

    @git_remote_url.setter
    def git_remote_url(self, git_remote_url):
        """
        Sets the git_remote_url of this Project.
        Git remote repository url

        :param git_remote_url: The git_remote_url of this Project.
        :type: str
        """
        self._git_remote_url = git_remote_url

    @property
    def git_username(self):
        """
        Gets the git_username of this Project.
        Git username for HTTPS authentication. (For production only, if using user attributes.)

        :return: The git_username of this Project.
        :rtype: str
        """
        return self._git_username

    @git_username.setter
    def git_username(self, git_username):
        """
        Sets the git_username of this Project.
        Git username for HTTPS authentication. (For production only, if using user attributes.)

        :param git_username: The git_username of this Project.
        :type: str
        """
        self._git_username = git_username

    @property
    def git_password(self):
        """
        Gets the git_password of this Project.
        (Write-Only) Git password for HTTPS authentication. (For production only, if using user attributes.)

        :return: The git_password of this Project.
        :rtype: str
        """
        return self._git_password

    @git_password.setter
    def git_password(self, git_password):
        """
        Sets the git_password of this Project.
        (Write-Only) Git password for HTTPS authentication. (For production only, if using user attributes.)

        :param git_password: The git_password of this Project.
        :type: str
        """
        self._git_password = git_password

    @property
    def git_username_user_attribute(self):
        """
        Gets the git_username_user_attribute of this Project.
        User attribute name for username in per-user HTTPS authentication.

        :return: The git_username_user_attribute of this Project.
        :rtype: str
        """
        return self._git_username_user_attribute

    @git_username_user_attribute.setter
    def git_username_user_attribute(self, git_username_user_attribute):
        """
        Sets the git_username_user_attribute of this Project.
        User attribute name for username in per-user HTTPS authentication.

        :param git_username_user_attribute: The git_username_user_attribute of this Project.
        :type: str
        """
        self._git_username_user_attribute = git_username_user_attribute

    @property
    def git_password_user_attribute(self):
        """
        Gets the git_password_user_attribute of this Project.
        User attribute name for password in per-user HTTPS authentication.

        :return: The git_password_user_attribute of this Project.
        :rtype: str
        """
        return self._git_password_user_attribute

    @git_password_user_attribute.setter
    def git_password_user_attribute(self, git_password_user_attribute):
        """
        Sets the git_password_user_attribute of this Project.
        User attribute name for password in per-user HTTPS authentication.

        :param git_password_user_attribute: The git_password_user_attribute of this Project.
        :type: str
        """
        self._git_password_user_attribute = git_password_user_attribute

    @property
    def git_service_name(self):
        """
        Gets the git_service_name of this Project.
        Name of the git service provider

        :return: The git_service_name of this Project.
        :rtype: str
        """
        return self._git_service_name

    @git_service_name.setter
    def git_service_name(self, git_service_name):
        """
        Sets the git_service_name of this Project.
        Name of the git service provider

        :param git_service_name: The git_service_name of this Project.
        :type: str
        """
        self._git_service_name = git_service_name

    @property
    def deploy_secret(self):
        """
        Gets the deploy_secret of this Project.
        (Write-Only) Optional secret token with which to authenticate requests to the webhook deploy endpoint. If not set, endpoint is unauthenticated.

        :return: The deploy_secret of this Project.
        :rtype: str
        """
        return self._deploy_secret

    @deploy_secret.setter
    def deploy_secret(self, deploy_secret):
        """
        Sets the deploy_secret of this Project.
        (Write-Only) Optional secret token with which to authenticate requests to the webhook deploy endpoint. If not set, endpoint is unauthenticated.

        :param deploy_secret: The deploy_secret of this Project.
        :type: str
        """
        self._deploy_secret = deploy_secret

    @property
    def unset_deploy_secret(self):
        """
        Gets the unset_deploy_secret of this Project.
        (Write-Only) When true, unsets the deploy secret to allow unauthenticated access to the webhook deploy endpoint.

        :return: The unset_deploy_secret of this Project.
        :rtype: bool
        """
        return self._unset_deploy_secret

    @unset_deploy_secret.setter
    def unset_deploy_secret(self, unset_deploy_secret):
        """
        Sets the unset_deploy_secret of this Project.
        (Write-Only) When true, unsets the deploy secret to allow unauthenticated access to the webhook deploy endpoint.

        :param unset_deploy_secret: The unset_deploy_secret of this Project.
        :type: bool
        """
        self._unset_deploy_secret = unset_deploy_secret

    @property
    def pull_request_mode(self):
        """
        Gets the pull_request_mode of this Project.
        The git pull request policy for this project. Valid values are: \"off\", \"links\", \"recommended\", \"required\".

        :return: The pull_request_mode of this Project.
        :rtype: str
        """
        return self._pull_request_mode

    @pull_request_mode.setter
    def pull_request_mode(self, pull_request_mode):
        """
        Sets the pull_request_mode of this Project.
        The git pull request policy for this project. Valid values are: \"off\", \"links\", \"recommended\", \"required\".

        :param pull_request_mode: The pull_request_mode of this Project.
        :type: str
        """
        self._pull_request_mode = pull_request_mode

    @property
    def validation_required(self):
        """
        Gets the validation_required of this Project.
        Validation policy: If true, the project must pass validation checks before project changes can be committed to the git repository

        :return: The validation_required of this Project.
        :rtype: bool
        """
        return self._validation_required

    @validation_required.setter
    def validation_required(self, validation_required):
        """
        Sets the validation_required of this Project.
        Validation policy: If true, the project must pass validation checks before project changes can be committed to the git repository

        :param validation_required: The validation_required of this Project.
        :type: bool
        """
        self._validation_required = validation_required

    @property
    def allow_warnings(self):
        """
        Gets the allow_warnings of this Project.
        Validation policy: If true, the project can be committed with warnings when `validation_required` is true. (`allow_warnings` does nothing if `validation_required` is false).

        :return: The allow_warnings of this Project.
        :rtype: bool
        """
        return self._allow_warnings

    @allow_warnings.setter
    def allow_warnings(self, allow_warnings):
        """
        Sets the allow_warnings of this Project.
        Validation policy: If true, the project can be committed with warnings when `validation_required` is true. (`allow_warnings` does nothing if `validation_required` is false).

        :param allow_warnings: The allow_warnings of this Project.
        :type: bool
        """
        self._allow_warnings = allow_warnings

    @property
    def is_example(self):
        """
        Gets the is_example of this Project.
        If true the project is an example project and cannot be modified

        :return: The is_example of this Project.
        :rtype: bool
        """
        return self._is_example

    @is_example.setter
    def is_example(self, is_example):
        """
        Sets the is_example of this Project.
        If true the project is an example project and cannot be modified

        :param is_example: The is_example of this Project.
        :type: bool
        """
        self._is_example = is_example

    @property
    def can(self):
        """
        Gets the can of this Project.
        Operations the current user is able to perform on this object

        :return: The can of this Project.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Project.
        Operations the current user is able to perform on this object

        :param can: The can of this Project.
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
