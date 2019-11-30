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


class BTPartMaterialProperty1453(object):
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
        'category': 'str',
        'units': 'str',
        'display_name': 'str',
        'description': 'str',
        'name': 'str',
        'value': 'str',
        'type': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'units': 'units',
        'display_name': 'displayName',
        'description': 'description',
        'name': 'name',
        'value': 'value',
        'type': 'type',
        'bt_type': 'btType'
    }

    def __init__(self, category=None, units=None, display_name=None, description=None, name=None, value=None, type=None, bt_type=None):  # noqa: E501
        """BTPartMaterialProperty1453 - a model defined in OpenAPI"""  # noqa: E501

        self._category = None
        self._units = None
        self._display_name = None
        self._description = None
        self._name = None
        self._value = None
        self._type = None
        self._bt_type = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if units is not None:
            self.units = units
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def category(self):
        """Gets the category of this BTPartMaterialProperty1453.  # noqa: E501


        :return: The category of this BTPartMaterialProperty1453.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this BTPartMaterialProperty1453.


        :param category: The category of this BTPartMaterialProperty1453.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def units(self):
        """Gets the units of this BTPartMaterialProperty1453.  # noqa: E501


        :return: The units of this BTPartMaterialProperty1453.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this BTPartMaterialProperty1453.


        :param units: The units of this BTPartMaterialProperty1453.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def display_name(self):
        """Gets the display_name of this BTPartMaterialProperty1453.  # noqa: E501


        :return: The display_name of this BTPartMaterialProperty1453.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BTPartMaterialProperty1453.


        :param display_name: The display_name of this BTPartMaterialProperty1453.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this BTPartMaterialProperty1453.  # noqa: E501


        :return: The description of this BTPartMaterialProperty1453.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTPartMaterialProperty1453.


        :param description: The description of this BTPartMaterialProperty1453.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this BTPartMaterialProperty1453.  # noqa: E501


        :return: The name of this BTPartMaterialProperty1453.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTPartMaterialProperty1453.


        :param name: The name of this BTPartMaterialProperty1453.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this BTPartMaterialProperty1453.  # noqa: E501


        :return: The value of this BTPartMaterialProperty1453.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BTPartMaterialProperty1453.


        :param value: The value of this BTPartMaterialProperty1453.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def type(self):
        """Gets the type of this BTPartMaterialProperty1453.  # noqa: E501


        :return: The type of this BTPartMaterialProperty1453.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTPartMaterialProperty1453.


        :param type: The type of this BTPartMaterialProperty1453.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def bt_type(self):
        """Gets the bt_type of this BTPartMaterialProperty1453.  # noqa: E501


        :return: The bt_type of this BTPartMaterialProperty1453.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTPartMaterialProperty1453.


        :param bt_type: The bt_type of this BTPartMaterialProperty1453.  # noqa: E501
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
        if not isinstance(other, BTPartMaterialProperty1453):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
