# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.103
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTExportModelVertex(object):
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
        'point': 'BTVector3d',
        'id': 'str'
    }

    attribute_map = {
        'point': 'point',
        'id': 'id'
    }

    def __init__(self, point=None, id=None):  # noqa: E501
        """BTExportModelVertex - a model defined in OpenAPI"""  # noqa: E501

        self._point = None
        self._id = None
        self.discriminator = None

        if point is not None:
            self.point = point
        if id is not None:
            self.id = id

    @property
    def point(self):
        """Gets the point of this BTExportModelVertex.  # noqa: E501


        :return: The point of this BTExportModelVertex.  # noqa: E501
        :rtype: BTVector3d
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this BTExportModelVertex.


        :param point: The point of this BTExportModelVertex.  # noqa: E501
        :type: BTVector3d
        """

        self._point = point

    @property
    def id(self):
        """Gets the id of this BTExportModelVertex.  # noqa: E501


        :return: The id of this BTExportModelVertex.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTExportModelVertex.


        :param id: The id of this BTExportModelVertex.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, BTExportModelVertex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
