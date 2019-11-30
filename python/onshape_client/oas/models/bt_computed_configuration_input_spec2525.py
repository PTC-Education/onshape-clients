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


class BTComputedConfigurationInputSpec2525(object):
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
        'input_id': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'input_id': 'inputId',
        'bt_type': 'btType'
    }

    def __init__(self, input_id=None, bt_type=None):  # noqa: E501
        """BTComputedConfigurationInputSpec2525 - a model defined in OpenAPI"""  # noqa: E501

        self._input_id = None
        self._bt_type = None
        self.discriminator = None

        if input_id is not None:
            self.input_id = input_id
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def input_id(self):
        """Gets the input_id of this BTComputedConfigurationInputSpec2525.  # noqa: E501


        :return: The input_id of this BTComputedConfigurationInputSpec2525.  # noqa: E501
        :rtype: str
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        """Sets the input_id of this BTComputedConfigurationInputSpec2525.


        :param input_id: The input_id of this BTComputedConfigurationInputSpec2525.  # noqa: E501
        :type: str
        """

        self._input_id = input_id

    @property
    def bt_type(self):
        """Gets the bt_type of this BTComputedConfigurationInputSpec2525.  # noqa: E501


        :return: The bt_type of this BTComputedConfigurationInputSpec2525.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTComputedConfigurationInputSpec2525.


        :param bt_type: The bt_type of this BTComputedConfigurationInputSpec2525.  # noqa: E501
        :type: str
        """

        self._bt_type = bt_type

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
        if not isinstance(other, BTComputedConfigurationInputSpec2525):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
