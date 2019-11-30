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


class BTPlaneDescription692(object):
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
        'normal': 'BTVector3d389',
        'origin': 'BTVector3d389'
    }

    attribute_map = {
        'normal': 'normal',
        'origin': 'origin'
    }

    def __init__(self, normal=None, origin=None):  # noqa: E501
        """BTPlaneDescription692 - a model defined in OpenAPI"""  # noqa: E501

        self._normal = None
        self._origin = None
        self.discriminator = None

        if normal is not None:
            self.normal = normal
        if origin is not None:
            self.origin = origin

    @property
    def normal(self):
        """Gets the normal of this BTPlaneDescription692.  # noqa: E501


        :return: The normal of this BTPlaneDescription692.  # noqa: E501
        :rtype: BTVector3d389
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        """Sets the normal of this BTPlaneDescription692.


        :param normal: The normal of this BTPlaneDescription692.  # noqa: E501
        :type: BTVector3d389
        """

        self._normal = normal

    @property
    def origin(self):
        """Gets the origin of this BTPlaneDescription692.  # noqa: E501


        :return: The origin of this BTPlaneDescription692.  # noqa: E501
        :rtype: BTVector3d389
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this BTPlaneDescription692.


        :param origin: The origin of this BTPlaneDescription692.  # noqa: E501
        :type: BTVector3d389
        """

        self._origin = origin

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
        if not isinstance(other, BTPlaneDescription692):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
