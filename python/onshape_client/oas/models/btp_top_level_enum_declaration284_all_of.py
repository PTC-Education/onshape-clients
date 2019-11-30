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


class BTPTopLevelEnumDeclaration284AllOf(object):
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
        'annotations': 'list[BTPAnnotation231]',
        'space_in_empty_list': 'BTPSpace10',
        'trailing_comma': 'bool',
        'values': 'list[BTPIdentifier8]'
    }

    attribute_map = {
        'annotations': 'annotations',
        'space_in_empty_list': 'spaceInEmptyList',
        'trailing_comma': 'trailingComma',
        'values': 'values'
    }

    def __init__(self, annotations=None, space_in_empty_list=None, trailing_comma=None, values=None):  # noqa: E501
        """BTPTopLevelEnumDeclaration284AllOf - a model defined in OpenAPI"""  # noqa: E501

        self._annotations = None
        self._space_in_empty_list = None
        self._trailing_comma = None
        self._values = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if space_in_empty_list is not None:
            self.space_in_empty_list = space_in_empty_list
        if trailing_comma is not None:
            self.trailing_comma = trailing_comma
        if values is not None:
            self.values = values

    @property
    def annotations(self):
        """Gets the annotations of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501


        :return: The annotations of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501
        :rtype: list[BTPAnnotation231]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this BTPTopLevelEnumDeclaration284AllOf.


        :param annotations: The annotations of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501
        :type: list[BTPAnnotation231]
        """

        self._annotations = annotations

    @property
    def space_in_empty_list(self):
        """Gets the space_in_empty_list of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501


        :return: The space_in_empty_list of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_in_empty_list

    @space_in_empty_list.setter
    def space_in_empty_list(self, space_in_empty_list):
        """Sets the space_in_empty_list of this BTPTopLevelEnumDeclaration284AllOf.


        :param space_in_empty_list: The space_in_empty_list of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_in_empty_list = space_in_empty_list

    @property
    def trailing_comma(self):
        """Gets the trailing_comma of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501


        :return: The trailing_comma of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._trailing_comma

    @trailing_comma.setter
    def trailing_comma(self, trailing_comma):
        """Sets the trailing_comma of this BTPTopLevelEnumDeclaration284AllOf.


        :param trailing_comma: The trailing_comma of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501
        :type: bool
        """

        self._trailing_comma = trailing_comma

    @property
    def values(self):
        """Gets the values of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501


        :return: The values of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501
        :rtype: list[BTPIdentifier8]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this BTPTopLevelEnumDeclaration284AllOf.


        :param values: The values of this BTPTopLevelEnumDeclaration284AllOf.  # noqa: E501
        :type: list[BTPIdentifier8]
        """

        self._values = values

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
        if not isinstance(other, BTPTopLevelEnumDeclaration284AllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
