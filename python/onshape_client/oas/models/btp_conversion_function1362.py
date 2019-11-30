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


class BTPConversionFunction1362(object):
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
        '_from': 'BTPLiteralNumber258',
        'to': 'BTPLiteralNumber258',
        'type_name': 'BTPIdentifier8',
        'space_after_type': 'BTPSpace10'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'type_name': 'typeName',
        'space_after_type': 'spaceAfterType'
    }

    def __init__(self, _from=None, to=None, type_name=None, space_after_type=None):  # noqa: E501
        """BTPConversionFunction1362 - a model defined in OpenAPI"""  # noqa: E501

        self.__from = None
        self._to = None
        self._type_name = None
        self._space_after_type = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if type_name is not None:
            self.type_name = type_name
        if space_after_type is not None:
            self.space_after_type = space_after_type

    @property
    def _from(self):
        """Gets the _from of this BTPConversionFunction1362.  # noqa: E501


        :return: The _from of this BTPConversionFunction1362.  # noqa: E501
        :rtype: BTPLiteralNumber258
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this BTPConversionFunction1362.


        :param _from: The _from of this BTPConversionFunction1362.  # noqa: E501
        :type: BTPLiteralNumber258
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this BTPConversionFunction1362.  # noqa: E501


        :return: The to of this BTPConversionFunction1362.  # noqa: E501
        :rtype: BTPLiteralNumber258
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this BTPConversionFunction1362.


        :param to: The to of this BTPConversionFunction1362.  # noqa: E501
        :type: BTPLiteralNumber258
        """

        self._to = to

    @property
    def type_name(self):
        """Gets the type_name of this BTPConversionFunction1362.  # noqa: E501


        :return: The type_name of this BTPConversionFunction1362.  # noqa: E501
        :rtype: BTPIdentifier8
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this BTPConversionFunction1362.


        :param type_name: The type_name of this BTPConversionFunction1362.  # noqa: E501
        :type: BTPIdentifier8
        """

        self._type_name = type_name

    @property
    def space_after_type(self):
        """Gets the space_after_type of this BTPConversionFunction1362.  # noqa: E501


        :return: The space_after_type of this BTPConversionFunction1362.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_after_type

    @space_after_type.setter
    def space_after_type(self, space_after_type):
        """Sets the space_after_type of this BTPConversionFunction1362.


        :param space_after_type: The space_after_type of this BTPConversionFunction1362.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_after_type = space_after_type

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
        if not isinstance(other, BTPConversionFunction1362):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
