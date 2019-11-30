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


class BTFSValue(object):
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
        'value_object': 'object',
        'configuration_value_string': 'str',
        'type_tag': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'value_object': 'valueObject',
        'configuration_value_string': 'configurationValueString',
        'type_tag': 'typeTag',
        'bt_type': 'btType'
    }

    discriminator_value_class_map = {
        'BTFSValueTooBig': 'BTFSValueTooBig',
        'BTFSValueArray': 'BTFSValueArray',
        'BTFSValueOther': 'BTFSValueOther',
        'BTFSValueWithUnits': 'BTFSValueWithUnits',
        'BTFSValueNumber': 'BTFSValueNumber',
        'BTFSValueString': 'BTFSValueString',
        'BTFSValueUndefined': 'BTFSValueUndefined',
        'BTFSValueMap': 'BTFSValueMap',
        'BTFSValueBoolean': 'BTFSValueBoolean'
    }

    def __init__(self, value_object=None, configuration_value_string=None, type_tag=None, bt_type=None):  # noqa: E501
        """BTFSValue - a model defined in OpenAPI"""  # noqa: E501

        self._value_object = None
        self._configuration_value_string = None
        self._type_tag = None
        self._bt_type = None
        self.discriminator = 'bt_type'

        if value_object is not None:
            self.value_object = value_object
        if configuration_value_string is not None:
            self.configuration_value_string = configuration_value_string
        if type_tag is not None:
            self.type_tag = type_tag
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def value_object(self):
        """Gets the value_object of this BTFSValue.  # noqa: E501


        :return: The value_object of this BTFSValue.  # noqa: E501
        :rtype: object
        """
        return self._value_object

    @value_object.setter
    def value_object(self, value_object):
        """Sets the value_object of this BTFSValue.


        :param value_object: The value_object of this BTFSValue.  # noqa: E501
        :type: object
        """

        self._value_object = value_object

    @property
    def configuration_value_string(self):
        """Gets the configuration_value_string of this BTFSValue.  # noqa: E501


        :return: The configuration_value_string of this BTFSValue.  # noqa: E501
        :rtype: str
        """
        return self._configuration_value_string

    @configuration_value_string.setter
    def configuration_value_string(self, configuration_value_string):
        """Sets the configuration_value_string of this BTFSValue.


        :param configuration_value_string: The configuration_value_string of this BTFSValue.  # noqa: E501
        :type: str
        """

        self._configuration_value_string = configuration_value_string

    @property
    def type_tag(self):
        """Gets the type_tag of this BTFSValue.  # noqa: E501


        :return: The type_tag of this BTFSValue.  # noqa: E501
        :rtype: str
        """
        return self._type_tag

    @type_tag.setter
    def type_tag(self, type_tag):
        """Sets the type_tag of this BTFSValue.


        :param type_tag: The type_tag of this BTFSValue.  # noqa: E501
        :type: str
        """

        self._type_tag = type_tag

    @property
    def bt_type(self):
        """Gets the bt_type of this BTFSValue.  # noqa: E501


        :return: The bt_type of this BTFSValue.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTFSValue.


        :param bt_type: The bt_type of this BTFSValue.  # noqa: E501
        :type: str
        """

        self._bt_type = bt_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, BTFSValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
