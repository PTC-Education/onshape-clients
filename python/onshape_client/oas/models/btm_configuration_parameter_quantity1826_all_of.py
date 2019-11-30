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


class BTMConfigurationParameterQuantity1826AllOf(object):
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
        'quantity_type': 'str',
        'range_and_default': 'BTQuantityRange181'
    }

    attribute_map = {
        'quantity_type': 'quantityType',
        'range_and_default': 'rangeAndDefault'
    }

    def __init__(self, quantity_type=None, range_and_default=None):  # noqa: E501
        """BTMConfigurationParameterQuantity1826AllOf - a model defined in OpenAPI"""  # noqa: E501

        self._quantity_type = None
        self._range_and_default = None
        self.discriminator = None

        if quantity_type is not None:
            self.quantity_type = quantity_type
        if range_and_default is not None:
            self.range_and_default = range_and_default

    @property
    def quantity_type(self):
        """Gets the quantity_type of this BTMConfigurationParameterQuantity1826AllOf.  # noqa: E501


        :return: The quantity_type of this BTMConfigurationParameterQuantity1826AllOf.  # noqa: E501
        :rtype: str
        """
        return self._quantity_type

    @quantity_type.setter
    def quantity_type(self, quantity_type):
        """Sets the quantity_type of this BTMConfigurationParameterQuantity1826AllOf.


        :param quantity_type: The quantity_type of this BTMConfigurationParameterQuantity1826AllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "INTEGER", "REAL", "LENGTH", "ANGLE", "MASS", "TIME", "TEMPERATURE", "CURRENT", "ANYTHING"]  # noqa: E501
        if quantity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `quantity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(quantity_type, allowed_values)
            )

        self._quantity_type = quantity_type

    @property
    def range_and_default(self):
        """Gets the range_and_default of this BTMConfigurationParameterQuantity1826AllOf.  # noqa: E501


        :return: The range_and_default of this BTMConfigurationParameterQuantity1826AllOf.  # noqa: E501
        :rtype: BTQuantityRange181
        """
        return self._range_and_default

    @range_and_default.setter
    def range_and_default(self, range_and_default):
        """Sets the range_and_default of this BTMConfigurationParameterQuantity1826AllOf.


        :param range_and_default: The range_and_default of this BTMConfigurationParameterQuantity1826AllOf.  # noqa: E501
        :type: BTQuantityRange181
        """

        self._range_and_default = range_and_default

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
        if not isinstance(other, BTMConfigurationParameterQuantity1826AllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
