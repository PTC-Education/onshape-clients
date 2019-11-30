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


class BTParameterSpecReferencePartStudio1256(object):
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
        'max_number_of_picks': 'int',
        'allowed_insertable_types': 'list[str]',
        'computed_configuration_inputs': 'list[BTComputedConfigurationInputSpec2525]'
    }

    attribute_map = {
        'max_number_of_picks': 'maxNumberOfPicks',
        'allowed_insertable_types': 'allowedInsertableTypes',
        'computed_configuration_inputs': 'computedConfigurationInputs'
    }

    def __init__(self, max_number_of_picks=None, allowed_insertable_types=None, computed_configuration_inputs=None):  # noqa: E501
        """BTParameterSpecReferencePartStudio1256 - a model defined in OpenAPI"""  # noqa: E501

        self._max_number_of_picks = None
        self._allowed_insertable_types = None
        self._computed_configuration_inputs = None
        self.discriminator = None

        if max_number_of_picks is not None:
            self.max_number_of_picks = max_number_of_picks
        if allowed_insertable_types is not None:
            self.allowed_insertable_types = allowed_insertable_types
        if computed_configuration_inputs is not None:
            self.computed_configuration_inputs = computed_configuration_inputs

    @property
    def max_number_of_picks(self):
        """Gets the max_number_of_picks of this BTParameterSpecReferencePartStudio1256.  # noqa: E501


        :return: The max_number_of_picks of this BTParameterSpecReferencePartStudio1256.  # noqa: E501
        :rtype: int
        """
        return self._max_number_of_picks

    @max_number_of_picks.setter
    def max_number_of_picks(self, max_number_of_picks):
        """Sets the max_number_of_picks of this BTParameterSpecReferencePartStudio1256.


        :param max_number_of_picks: The max_number_of_picks of this BTParameterSpecReferencePartStudio1256.  # noqa: E501
        :type: int
        """

        self._max_number_of_picks = max_number_of_picks

    @property
    def allowed_insertable_types(self):
        """Gets the allowed_insertable_types of this BTParameterSpecReferencePartStudio1256.  # noqa: E501


        :return: The allowed_insertable_types of this BTParameterSpecReferencePartStudio1256.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_insertable_types

    @allowed_insertable_types.setter
    def allowed_insertable_types(self, allowed_insertable_types):
        """Sets the allowed_insertable_types of this BTParameterSpecReferencePartStudio1256.


        :param allowed_insertable_types: The allowed_insertable_types of this BTParameterSpecReferencePartStudio1256.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["SOLID", "SURFACE", "WIRE", "MESH", "SKETCH", "FLATTENED_SHEET_METAL", "ENTIRE_PART_STUDIO", "CONSTRUCTION_PLANE", "COMPOSITE_PART", "UNKNOWN"]  # noqa: E501
        if not set(allowed_insertable_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allowed_insertable_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_insertable_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_insertable_types = allowed_insertable_types

    @property
    def computed_configuration_inputs(self):
        """Gets the computed_configuration_inputs of this BTParameterSpecReferencePartStudio1256.  # noqa: E501


        :return: The computed_configuration_inputs of this BTParameterSpecReferencePartStudio1256.  # noqa: E501
        :rtype: list[BTComputedConfigurationInputSpec2525]
        """
        return self._computed_configuration_inputs

    @computed_configuration_inputs.setter
    def computed_configuration_inputs(self, computed_configuration_inputs):
        """Sets the computed_configuration_inputs of this BTParameterSpecReferencePartStudio1256.


        :param computed_configuration_inputs: The computed_configuration_inputs of this BTParameterSpecReferencePartStudio1256.  # noqa: E501
        :type: list[BTComputedConfigurationInputSpec2525]
        """

        self._computed_configuration_inputs = computed_configuration_inputs

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
        if not isinstance(other, BTParameterSpecReferencePartStudio1256):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
