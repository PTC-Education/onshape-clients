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


class BTMParameterQueryList148(object):
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
        'queries': 'list[BTMIndividualQueryBase139]'
    }

    attribute_map = {
        'queries': 'queries'
    }

    def __init__(self, queries=None):  # noqa: E501
        """BTMParameterQueryList148 - a model defined in OpenAPI"""  # noqa: E501

        self._queries = None
        self.discriminator = None

        if queries is not None:
            self.queries = queries

    @property
    def queries(self):
        """Gets the queries of this BTMParameterQueryList148.  # noqa: E501


        :return: The queries of this BTMParameterQueryList148.  # noqa: E501
        :rtype: list[BTMIndividualQueryBase139]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this BTMParameterQueryList148.


        :param queries: The queries of this BTMParameterQueryList148.  # noqa: E501
        :type: list[BTMIndividualQueryBase139]
        """

        self._queries = queries

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
        if not isinstance(other, BTMParameterQueryList148):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
