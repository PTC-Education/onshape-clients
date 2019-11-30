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


class BTPExpressionIs242(object):
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
        'operand': 'BTPExpression9',
        'type_name': 'BTPTypeName290'
    }

    attribute_map = {
        'operand': 'operand',
        'type_name': 'typeName'
    }

    def __init__(self, operand=None, type_name=None):  # noqa: E501
        """BTPExpressionIs242 - a model defined in OpenAPI"""  # noqa: E501

        self._operand = None
        self._type_name = None
        self.discriminator = None

        if operand is not None:
            self.operand = operand
        if type_name is not None:
            self.type_name = type_name

    @property
    def operand(self):
        """Gets the operand of this BTPExpressionIs242.  # noqa: E501


        :return: The operand of this BTPExpressionIs242.  # noqa: E501
        :rtype: BTPExpression9
        """
        return self._operand

    @operand.setter
    def operand(self, operand):
        """Sets the operand of this BTPExpressionIs242.


        :param operand: The operand of this BTPExpressionIs242.  # noqa: E501
        :type: BTPExpression9
        """

        self._operand = operand

    @property
    def type_name(self):
        """Gets the type_name of this BTPExpressionIs242.  # noqa: E501


        :return: The type_name of this BTPExpressionIs242.  # noqa: E501
        :rtype: BTPTypeName290
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this BTPExpressionIs242.


        :param type_name: The type_name of this BTPExpressionIs242.  # noqa: E501
        :type: BTPTypeName290
        """

        self._type_name = type_name

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
        if not isinstance(other, BTPExpressionIs242):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
