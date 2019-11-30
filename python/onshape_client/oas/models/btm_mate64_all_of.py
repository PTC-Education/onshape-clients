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


class BTMMate64AllOf(object):
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
        'mate_connector_query_list': 'BTMParameterQueryWithOccurrenceList67',
        'primary_axis_alignment': 'bool',
        'secondary_axis_alignment': 'str',
        'mate_offset': 'BTVector3d389',
        'mate_connectors': 'list[BTMMateConnector66]'
    }

    attribute_map = {
        'mate_connector_query_list': 'mateConnectorQueryList',
        'primary_axis_alignment': 'primaryAxisAlignment',
        'secondary_axis_alignment': 'secondaryAxisAlignment',
        'mate_offset': 'mateOffset',
        'mate_connectors': 'mateConnectors'
    }

    def __init__(self, mate_connector_query_list=None, primary_axis_alignment=None, secondary_axis_alignment=None, mate_offset=None, mate_connectors=None):  # noqa: E501
        """BTMMate64AllOf - a model defined in OpenAPI"""  # noqa: E501

        self._mate_connector_query_list = None
        self._primary_axis_alignment = None
        self._secondary_axis_alignment = None
        self._mate_offset = None
        self._mate_connectors = None
        self.discriminator = None

        if mate_connector_query_list is not None:
            self.mate_connector_query_list = mate_connector_query_list
        if primary_axis_alignment is not None:
            self.primary_axis_alignment = primary_axis_alignment
        if secondary_axis_alignment is not None:
            self.secondary_axis_alignment = secondary_axis_alignment
        if mate_offset is not None:
            self.mate_offset = mate_offset
        if mate_connectors is not None:
            self.mate_connectors = mate_connectors

    @property
    def mate_connector_query_list(self):
        """Gets the mate_connector_query_list of this BTMMate64AllOf.  # noqa: E501


        :return: The mate_connector_query_list of this BTMMate64AllOf.  # noqa: E501
        :rtype: BTMParameterQueryWithOccurrenceList67
        """
        return self._mate_connector_query_list

    @mate_connector_query_list.setter
    def mate_connector_query_list(self, mate_connector_query_list):
        """Sets the mate_connector_query_list of this BTMMate64AllOf.


        :param mate_connector_query_list: The mate_connector_query_list of this BTMMate64AllOf.  # noqa: E501
        :type: BTMParameterQueryWithOccurrenceList67
        """

        self._mate_connector_query_list = mate_connector_query_list

    @property
    def primary_axis_alignment(self):
        """Gets the primary_axis_alignment of this BTMMate64AllOf.  # noqa: E501


        :return: The primary_axis_alignment of this BTMMate64AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._primary_axis_alignment

    @primary_axis_alignment.setter
    def primary_axis_alignment(self, primary_axis_alignment):
        """Sets the primary_axis_alignment of this BTMMate64AllOf.


        :param primary_axis_alignment: The primary_axis_alignment of this BTMMate64AllOf.  # noqa: E501
        :type: bool
        """

        self._primary_axis_alignment = primary_axis_alignment

    @property
    def secondary_axis_alignment(self):
        """Gets the secondary_axis_alignment of this BTMMate64AllOf.  # noqa: E501


        :return: The secondary_axis_alignment of this BTMMate64AllOf.  # noqa: E501
        :rtype: str
        """
        return self._secondary_axis_alignment

    @secondary_axis_alignment.setter
    def secondary_axis_alignment(self, secondary_axis_alignment):
        """Sets the secondary_axis_alignment of this BTMMate64AllOf.


        :param secondary_axis_alignment: The secondary_axis_alignment of this BTMMate64AllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["PLUS_X", "PLUS_Y", "MINUS_X", "MINUS_Y", "UNKNOWN"]  # noqa: E501
        if secondary_axis_alignment not in allowed_values:
            raise ValueError(
                "Invalid value for `secondary_axis_alignment` ({0}), must be one of {1}"  # noqa: E501
                .format(secondary_axis_alignment, allowed_values)
            )

        self._secondary_axis_alignment = secondary_axis_alignment

    @property
    def mate_offset(self):
        """Gets the mate_offset of this BTMMate64AllOf.  # noqa: E501


        :return: The mate_offset of this BTMMate64AllOf.  # noqa: E501
        :rtype: BTVector3d389
        """
        return self._mate_offset

    @mate_offset.setter
    def mate_offset(self, mate_offset):
        """Sets the mate_offset of this BTMMate64AllOf.


        :param mate_offset: The mate_offset of this BTMMate64AllOf.  # noqa: E501
        :type: BTVector3d389
        """

        self._mate_offset = mate_offset

    @property
    def mate_connectors(self):
        """Gets the mate_connectors of this BTMMate64AllOf.  # noqa: E501


        :return: The mate_connectors of this BTMMate64AllOf.  # noqa: E501
        :rtype: list[BTMMateConnector66]
        """
        return self._mate_connectors

    @mate_connectors.setter
    def mate_connectors(self, mate_connectors):
        """Sets the mate_connectors of this BTMMate64AllOf.


        :param mate_connectors: The mate_connectors of this BTMMate64AllOf.  # noqa: E501
        :type: list[BTMMateConnector66]
        """

        self._mate_connectors = mate_connectors

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
        if not isinstance(other, BTMMate64AllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
