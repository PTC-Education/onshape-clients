# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.87
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ElementsEncodeConfigurationResponse200(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'encoded_id': 'str'
    }

    attribute_map = {
        'encoded_id': 'encodedId'
    }

    def __init__(self, encoded_id=None):  # noqa: E501
        """ElementsEncodeConfigurationResponse200 - a model defined in Swagger"""  # noqa: E501

        self._encoded_id = None
        self.discriminator = None

        if encoded_id is not None:
            self.encoded_id = encoded_id

    @property
    def encoded_id(self):
        """Gets the encoded_id of this ElementsEncodeConfigurationResponse200.  # noqa: E501

        The configuration encoding string  # noqa: E501

        :return: The encoded_id of this ElementsEncodeConfigurationResponse200.  # noqa: E501
        :rtype: str
        """
        return self._encoded_id

    @encoded_id.setter
    def encoded_id(self, encoded_id):
        """Sets the encoded_id of this ElementsEncodeConfigurationResponse200.

        The configuration encoding string  # noqa: E501

        :param encoded_id: The encoded_id of this ElementsEncodeConfigurationResponse200.  # noqa: E501
        :type: str
        """

        self._encoded_id = encoded_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, ElementsEncodeConfigurationResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
