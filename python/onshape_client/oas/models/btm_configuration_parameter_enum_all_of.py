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


class BTMConfigurationParameterEnumAllOf(object):
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
        'option_ids': 'list[str]',
        'enum_name': 'str',
        'options': 'list[BTMEnumOption]',
        'default_value': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'option_ids': 'optionIds',
        'enum_name': 'enumName',
        'options': 'options',
        'default_value': 'defaultValue',
        'namespace': 'namespace'
    }

    def __init__(self, option_ids=None, enum_name=None, options=None, default_value=None, namespace=None):  # noqa: E501
        """BTMConfigurationParameterEnumAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._option_ids = None
        self._enum_name = None
        self._options = None
        self._default_value = None
        self._namespace = None
        self.discriminator = None

        if option_ids is not None:
            self.option_ids = option_ids
        if enum_name is not None:
            self.enum_name = enum_name
        if options is not None:
            self.options = options
        if default_value is not None:
            self.default_value = default_value
        if namespace is not None:
            self.namespace = namespace

    @property
    def option_ids(self):
        """Gets the option_ids of this BTMConfigurationParameterEnumAllOf.  # noqa: E501


        :return: The option_ids of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._option_ids

    @option_ids.setter
    def option_ids(self, option_ids):
        """Sets the option_ids of this BTMConfigurationParameterEnumAllOf.


        :param option_ids: The option_ids of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :type: list[str]
        """

        self._option_ids = option_ids

    @property
    def enum_name(self):
        """Gets the enum_name of this BTMConfigurationParameterEnumAllOf.  # noqa: E501


        :return: The enum_name of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :rtype: str
        """
        return self._enum_name

    @enum_name.setter
    def enum_name(self, enum_name):
        """Sets the enum_name of this BTMConfigurationParameterEnumAllOf.


        :param enum_name: The enum_name of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :type: str
        """

        self._enum_name = enum_name

    @property
    def options(self):
        """Gets the options of this BTMConfigurationParameterEnumAllOf.  # noqa: E501


        :return: The options of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :rtype: list[BTMEnumOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this BTMConfigurationParameterEnumAllOf.


        :param options: The options of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :type: list[BTMEnumOption]
        """

        self._options = options

    @property
    def default_value(self):
        """Gets the default_value of this BTMConfigurationParameterEnumAllOf.  # noqa: E501


        :return: The default_value of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this BTMConfigurationParameterEnumAllOf.


        :param default_value: The default_value of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def namespace(self):
        """Gets the namespace of this BTMConfigurationParameterEnumAllOf.  # noqa: E501


        :return: The namespace of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BTMConfigurationParameterEnumAllOf.


        :param namespace: The namespace of this BTMConfigurationParameterEnumAllOf.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if not isinstance(other, BTMConfigurationParameterEnumAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
