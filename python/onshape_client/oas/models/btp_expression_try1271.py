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


class BTPExpressionTry1271(object):
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
        'expression': 'BTPExpression9',
        'space_after_try': 'BTPSpace10',
        'silent': 'bool',
        'space_after_silent': 'BTPSpace10'
    }

    attribute_map = {
        'expression': 'expression',
        'space_after_try': 'spaceAfterTry',
        'silent': 'silent',
        'space_after_silent': 'spaceAfterSilent'
    }

    def __init__(self, expression=None, space_after_try=None, silent=None, space_after_silent=None):  # noqa: E501
        """BTPExpressionTry1271 - a model defined in OpenAPI"""  # noqa: E501

        self._expression = None
        self._space_after_try = None
        self._silent = None
        self._space_after_silent = None
        self.discriminator = None

        if expression is not None:
            self.expression = expression
        if space_after_try is not None:
            self.space_after_try = space_after_try
        if silent is not None:
            self.silent = silent
        if space_after_silent is not None:
            self.space_after_silent = space_after_silent

    @property
    def expression(self):
        """Gets the expression of this BTPExpressionTry1271.  # noqa: E501


        :return: The expression of this BTPExpressionTry1271.  # noqa: E501
        :rtype: BTPExpression9
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this BTPExpressionTry1271.


        :param expression: The expression of this BTPExpressionTry1271.  # noqa: E501
        :type: BTPExpression9
        """

        self._expression = expression

    @property
    def space_after_try(self):
        """Gets the space_after_try of this BTPExpressionTry1271.  # noqa: E501


        :return: The space_after_try of this BTPExpressionTry1271.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_after_try

    @space_after_try.setter
    def space_after_try(self, space_after_try):
        """Sets the space_after_try of this BTPExpressionTry1271.


        :param space_after_try: The space_after_try of this BTPExpressionTry1271.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_after_try = space_after_try

    @property
    def silent(self):
        """Gets the silent of this BTPExpressionTry1271.  # noqa: E501


        :return: The silent of this BTPExpressionTry1271.  # noqa: E501
        :rtype: bool
        """
        return self._silent

    @silent.setter
    def silent(self, silent):
        """Sets the silent of this BTPExpressionTry1271.


        :param silent: The silent of this BTPExpressionTry1271.  # noqa: E501
        :type: bool
        """

        self._silent = silent

    @property
    def space_after_silent(self):
        """Gets the space_after_silent of this BTPExpressionTry1271.  # noqa: E501


        :return: The space_after_silent of this BTPExpressionTry1271.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_after_silent

    @space_after_silent.setter
    def space_after_silent(self, space_after_silent):
        """Sets the space_after_silent of this BTPExpressionTry1271.


        :param space_after_silent: The space_after_silent of this BTPExpressionTry1271.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_after_silent = space_after_silent

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
        if not isinstance(other, BTPExpressionTry1271):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
