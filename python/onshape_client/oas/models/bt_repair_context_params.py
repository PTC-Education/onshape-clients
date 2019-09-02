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


class BTRepairContextParams(object):
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
        'old_occurrences': 'list[BTOccurrence]',
        'new_occurrences': 'list[BTOccurrence]',
        'context_assembly_id': 'str',
        'context_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'old_occurrences': 'oldOccurrences',
        'new_occurrences': 'newOccurrences',
        'context_assembly_id': 'contextAssemblyId',
        'context_id': 'contextId',
        'description': 'description'
    }

    def __init__(self, old_occurrences=None, new_occurrences=None, context_assembly_id=None, context_id=None, description=None):  # noqa: E501
        """BTRepairContextParams - a model defined in OpenAPI"""  # noqa: E501

        self._old_occurrences = None
        self._new_occurrences = None
        self._context_assembly_id = None
        self._context_id = None
        self._description = None
        self.discriminator = None

        if old_occurrences is not None:
            self.old_occurrences = old_occurrences
        if new_occurrences is not None:
            self.new_occurrences = new_occurrences
        if context_assembly_id is not None:
            self.context_assembly_id = context_assembly_id
        if context_id is not None:
            self.context_id = context_id
        if description is not None:
            self.description = description

    @property
    def old_occurrences(self):
        """Gets the old_occurrences of this BTRepairContextParams.  # noqa: E501


        :return: The old_occurrences of this BTRepairContextParams.  # noqa: E501
        :rtype: list[BTOccurrence]
        """
        return self._old_occurrences

    @old_occurrences.setter
    def old_occurrences(self, old_occurrences):
        """Sets the old_occurrences of this BTRepairContextParams.


        :param old_occurrences: The old_occurrences of this BTRepairContextParams.  # noqa: E501
        :type: list[BTOccurrence]
        """

        self._old_occurrences = old_occurrences

    @property
    def new_occurrences(self):
        """Gets the new_occurrences of this BTRepairContextParams.  # noqa: E501


        :return: The new_occurrences of this BTRepairContextParams.  # noqa: E501
        :rtype: list[BTOccurrence]
        """
        return self._new_occurrences

    @new_occurrences.setter
    def new_occurrences(self, new_occurrences):
        """Sets the new_occurrences of this BTRepairContextParams.


        :param new_occurrences: The new_occurrences of this BTRepairContextParams.  # noqa: E501
        :type: list[BTOccurrence]
        """

        self._new_occurrences = new_occurrences

    @property
    def context_assembly_id(self):
        """Gets the context_assembly_id of this BTRepairContextParams.  # noqa: E501


        :return: The context_assembly_id of this BTRepairContextParams.  # noqa: E501
        :rtype: str
        """
        return self._context_assembly_id

    @context_assembly_id.setter
    def context_assembly_id(self, context_assembly_id):
        """Sets the context_assembly_id of this BTRepairContextParams.


        :param context_assembly_id: The context_assembly_id of this BTRepairContextParams.  # noqa: E501
        :type: str
        """

        self._context_assembly_id = context_assembly_id

    @property
    def context_id(self):
        """Gets the context_id of this BTRepairContextParams.  # noqa: E501


        :return: The context_id of this BTRepairContextParams.  # noqa: E501
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """Sets the context_id of this BTRepairContextParams.


        :param context_id: The context_id of this BTRepairContextParams.  # noqa: E501
        :type: str
        """

        self._context_id = context_id

    @property
    def description(self):
        """Gets the description of this BTRepairContextParams.  # noqa: E501


        :return: The description of this BTRepairContextParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTRepairContextParams.


        :param description: The description of this BTRepairContextParams.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, BTRepairContextParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
