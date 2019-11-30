# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.106
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTMParameterEnum145(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'namespace': 'str',
        'enum_name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'enum_name': 'enumName',
        'value': 'value'
    }

    def __init__(self, namespace=None, enum_name=None, value=None):  # noqa: E501
        """BTMParameterEnum145 - a model defined in OpenAPI"""  # noqa: E501

        self._namespace = None
        self._enum_name = None
        self._value = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if enum_name is not None:
            self.enum_name = enum_name
        if value is not None:
            self.value = value

    @property
    def namespace(self):
        """Gets the namespace of this BTMParameterEnum145.  # noqa: E501


        :return: The namespace of this BTMParameterEnum145.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BTMParameterEnum145.


        :param namespace: The namespace of this BTMParameterEnum145.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def enum_name(self):
        """Gets the enum_name of this BTMParameterEnum145.  # noqa: E501


        :return: The enum_name of this BTMParameterEnum145.  # noqa: E501
        :rtype: str
        """
        return self._enum_name

    @enum_name.setter
    def enum_name(self, enum_name):
        """Sets the enum_name of this BTMParameterEnum145.


        :param enum_name: The enum_name of this BTMParameterEnum145.  # noqa: E501
        :type: str
        """

        self._enum_name = enum_name

    @property
    def value(self):
        """Gets the value of this BTMParameterEnum145.  # noqa: E501


        :return: The value of this BTMParameterEnum145.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BTMParameterEnum145.


        :param value: The value of this BTMParameterEnum145.  # noqa: E501
        :type: str
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, BTMParameterEnum145):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
