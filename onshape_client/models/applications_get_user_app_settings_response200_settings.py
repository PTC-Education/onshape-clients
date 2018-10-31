# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.87
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApplicationsGetUserAppSettingsResponse200Settings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'value': 'object',
        'key': 'str'
    }

    attribute_map = {
        'value': 'value',
        'key': 'key'
    }

    def __init__(self, value=None, key=None):  # noqa: E501
        """ApplicationsGetUserAppSettingsResponse200Settings - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._key = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if key is not None:
            self.key = key

    @property
    def value(self):
        """Gets the value of this ApplicationsGetUserAppSettingsResponse200Settings.  # noqa: E501

        Value associated with requested key  # noqa: E501

        :return: The value of this ApplicationsGetUserAppSettingsResponse200Settings.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ApplicationsGetUserAppSettingsResponse200Settings.

        Value associated with requested key  # noqa: E501

        :param value: The value of this ApplicationsGetUserAppSettingsResponse200Settings.  # noqa: E501
        :type: object
        """

        self._value = value

    @property
    def key(self):
        """Gets the key of this ApplicationsGetUserAppSettingsResponse200Settings.  # noqa: E501

        Requested key  # noqa: E501

        :return: The key of this ApplicationsGetUserAppSettingsResponse200Settings.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ApplicationsGetUserAppSettingsResponse200Settings.

        Requested key  # noqa: E501

        :param key: The key of this ApplicationsGetUserAppSettingsResponse200Settings.  # noqa: E501
        :type: str
        """

        self._key = key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApplicationsGetUserAppSettingsResponse200Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
