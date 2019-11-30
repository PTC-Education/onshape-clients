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


class BTMIndividualCoEdgeQuery1332(object):
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
        'face_query': 'BTMIndividualQuery138',
        'edge_query': 'BTMIndividualQuery138'
    }

    attribute_map = {
        'face_query': 'faceQuery',
        'edge_query': 'edgeQuery'
    }

    def __init__(self, face_query=None, edge_query=None):  # noqa: E501
        """BTMIndividualCoEdgeQuery1332 - a model defined in OpenAPI"""  # noqa: E501

        self._face_query = None
        self._edge_query = None
        self.discriminator = None

        if face_query is not None:
            self.face_query = face_query
        if edge_query is not None:
            self.edge_query = edge_query

    @property
    def face_query(self):
        """Gets the face_query of this BTMIndividualCoEdgeQuery1332.  # noqa: E501


        :return: The face_query of this BTMIndividualCoEdgeQuery1332.  # noqa: E501
        :rtype: BTMIndividualQuery138
        """
        return self._face_query

    @face_query.setter
    def face_query(self, face_query):
        """Sets the face_query of this BTMIndividualCoEdgeQuery1332.


        :param face_query: The face_query of this BTMIndividualCoEdgeQuery1332.  # noqa: E501
        :type: BTMIndividualQuery138
        """

        self._face_query = face_query

    @property
    def edge_query(self):
        """Gets the edge_query of this BTMIndividualCoEdgeQuery1332.  # noqa: E501


        :return: The edge_query of this BTMIndividualCoEdgeQuery1332.  # noqa: E501
        :rtype: BTMIndividualQuery138
        """
        return self._edge_query

    @edge_query.setter
    def edge_query(self, edge_query):
        """Sets the edge_query of this BTMIndividualCoEdgeQuery1332.


        :param edge_query: The edge_query of this BTMIndividualCoEdgeQuery1332.  # noqa: E501
        :type: BTMIndividualQuery138
        """

        self._edge_query = edge_query

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
        if not isinstance(other, BTMIndividualCoEdgeQuery1332):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
