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


class BTExportTessellatedEdgesEdge(object):
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
        'vertices': 'list[BTVector3d]',
        'id': 'str'
    }

    attribute_map = {
        'vertices': 'vertices',
        'id': 'id'
    }

    def __init__(self, vertices=None, id=None):  # noqa: E501
        """BTExportTessellatedEdgesEdge - a model defined in OpenAPI"""  # noqa: E501

        self._vertices = None
        self._id = None
        self.discriminator = None

        if vertices is not None:
            self.vertices = vertices
        if id is not None:
            self.id = id

    @property
    def vertices(self):
        """Gets the vertices of this BTExportTessellatedEdgesEdge.  # noqa: E501


        :return: The vertices of this BTExportTessellatedEdgesEdge.  # noqa: E501
        :rtype: list[BTVector3d]
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        """Sets the vertices of this BTExportTessellatedEdgesEdge.


        :param vertices: The vertices of this BTExportTessellatedEdgesEdge.  # noqa: E501
        :type: list[BTVector3d]
        """

        self._vertices = vertices

    @property
    def id(self):
        """Gets the id of this BTExportTessellatedEdgesEdge.  # noqa: E501


        :return: The id of this BTExportTessellatedEdgesEdge.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTExportTessellatedEdgesEdge.


        :param id: The id of this BTExportTessellatedEdgesEdge.  # noqa: E501
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
        if not isinstance(other, BTExportTessellatedEdgesEdge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
