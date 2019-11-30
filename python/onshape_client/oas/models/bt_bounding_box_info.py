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


class BTBoundingBoxInfo(object):
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
        'low_x': 'float',
        'low_z': 'float',
        'low_y': 'float',
        'high_z': 'float',
        'high_x': 'float',
        'high_y': 'float'
    }

    attribute_map = {
        'low_x': 'lowX',
        'low_z': 'lowZ',
        'low_y': 'lowY',
        'high_z': 'highZ',
        'high_x': 'highX',
        'high_y': 'highY'
    }

    def __init__(self, low_x=None, low_z=None, low_y=None, high_z=None, high_x=None, high_y=None):  # noqa: E501
        """BTBoundingBoxInfo - a model defined in OpenAPI"""  # noqa: E501

        self._low_x = None
        self._low_z = None
        self._low_y = None
        self._high_z = None
        self._high_x = None
        self._high_y = None
        self.discriminator = None

        if low_x is not None:
            self.low_x = low_x
        if low_z is not None:
            self.low_z = low_z
        if low_y is not None:
            self.low_y = low_y
        if high_z is not None:
            self.high_z = high_z
        if high_x is not None:
            self.high_x = high_x
        if high_y is not None:
            self.high_y = high_y

    @property
    def low_x(self):
        """Gets the low_x of this BTBoundingBoxInfo.  # noqa: E501


        :return: The low_x of this BTBoundingBoxInfo.  # noqa: E501
        :rtype: float
        """
        return self._low_x

    @low_x.setter
    def low_x(self, low_x):
        """Sets the low_x of this BTBoundingBoxInfo.


        :param low_x: The low_x of this BTBoundingBoxInfo.  # noqa: E501
        :type: float
        """

        self._low_x = low_x

    @property
    def low_z(self):
        """Gets the low_z of this BTBoundingBoxInfo.  # noqa: E501


        :return: The low_z of this BTBoundingBoxInfo.  # noqa: E501
        :rtype: float
        """
        return self._low_z

    @low_z.setter
    def low_z(self, low_z):
        """Sets the low_z of this BTBoundingBoxInfo.


        :param low_z: The low_z of this BTBoundingBoxInfo.  # noqa: E501
        :type: float
        """

        self._low_z = low_z

    @property
    def low_y(self):
        """Gets the low_y of this BTBoundingBoxInfo.  # noqa: E501


        :return: The low_y of this BTBoundingBoxInfo.  # noqa: E501
        :rtype: float
        """
        return self._low_y

    @low_y.setter
    def low_y(self, low_y):
        """Sets the low_y of this BTBoundingBoxInfo.


        :param low_y: The low_y of this BTBoundingBoxInfo.  # noqa: E501
        :type: float
        """

        self._low_y = low_y

    @property
    def high_z(self):
        """Gets the high_z of this BTBoundingBoxInfo.  # noqa: E501


        :return: The high_z of this BTBoundingBoxInfo.  # noqa: E501
        :rtype: float
        """
        return self._high_z

    @high_z.setter
    def high_z(self, high_z):
        """Sets the high_z of this BTBoundingBoxInfo.


        :param high_z: The high_z of this BTBoundingBoxInfo.  # noqa: E501
        :type: float
        """

        self._high_z = high_z

    @property
    def high_x(self):
        """Gets the high_x of this BTBoundingBoxInfo.  # noqa: E501


        :return: The high_x of this BTBoundingBoxInfo.  # noqa: E501
        :rtype: float
        """
        return self._high_x

    @high_x.setter
    def high_x(self, high_x):
        """Sets the high_x of this BTBoundingBoxInfo.


        :param high_x: The high_x of this BTBoundingBoxInfo.  # noqa: E501
        :type: float
        """

        self._high_x = high_x

    @property
    def high_y(self):
        """Gets the high_y of this BTBoundingBoxInfo.  # noqa: E501


        :return: The high_y of this BTBoundingBoxInfo.  # noqa: E501
        :rtype: float
        """
        return self._high_y

    @high_y.setter
    def high_y(self, high_y):
        """Sets the high_y of this BTBoundingBoxInfo.


        :param high_y: The high_y of this BTBoundingBoxInfo.  # noqa: E501
        :type: float
        """

        self._high_y = high_y

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
        if not isinstance(other, BTBoundingBoxInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
