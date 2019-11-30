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


class BTPartMaterialInfo(object):
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
        'library_name': 'str',
        'library_reference': 'BTExternalElementReferenceInfo',
        'display_name': 'str',
        'properties': 'list[BTPartMaterialPropertyInfo]',
        'id': 'str'
    }

    attribute_map = {
        'library_name': 'libraryName',
        'library_reference': 'libraryReference',
        'display_name': 'displayName',
        'properties': 'properties',
        'id': 'id'
    }

    def __init__(self, library_name=None, library_reference=None, display_name=None, properties=None, id=None):  # noqa: E501
        """BTPartMaterialInfo - a model defined in OpenAPI"""  # noqa: E501

        self._library_name = None
        self._library_reference = None
        self._display_name = None
        self._properties = None
        self._id = None
        self.discriminator = None

        if library_name is not None:
            self.library_name = library_name
        if library_reference is not None:
            self.library_reference = library_reference
        if display_name is not None:
            self.display_name = display_name
        if properties is not None:
            self.properties = properties
        if id is not None:
            self.id = id

    @property
    def library_name(self):
        """Gets the library_name of this BTPartMaterialInfo.  # noqa: E501


        :return: The library_name of this BTPartMaterialInfo.  # noqa: E501
        :rtype: str
        """
        return self._library_name

    @library_name.setter
    def library_name(self, library_name):
        """Sets the library_name of this BTPartMaterialInfo.


        :param library_name: The library_name of this BTPartMaterialInfo.  # noqa: E501
        :type: str
        """

        self._library_name = library_name

    @property
    def library_reference(self):
        """Gets the library_reference of this BTPartMaterialInfo.  # noqa: E501


        :return: The library_reference of this BTPartMaterialInfo.  # noqa: E501
        :rtype: BTExternalElementReferenceInfo
        """
        return self._library_reference

    @library_reference.setter
    def library_reference(self, library_reference):
        """Sets the library_reference of this BTPartMaterialInfo.


        :param library_reference: The library_reference of this BTPartMaterialInfo.  # noqa: E501
        :type: BTExternalElementReferenceInfo
        """

        self._library_reference = library_reference

    @property
    def display_name(self):
        """Gets the display_name of this BTPartMaterialInfo.  # noqa: E501


        :return: The display_name of this BTPartMaterialInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BTPartMaterialInfo.


        :param display_name: The display_name of this BTPartMaterialInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def properties(self):
        """Gets the properties of this BTPartMaterialInfo.  # noqa: E501


        :return: The properties of this BTPartMaterialInfo.  # noqa: E501
        :rtype: list[BTPartMaterialPropertyInfo]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BTPartMaterialInfo.


        :param properties: The properties of this BTPartMaterialInfo.  # noqa: E501
        :type: list[BTPartMaterialPropertyInfo]
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this BTPartMaterialInfo.  # noqa: E501


        :return: The id of this BTPartMaterialInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTPartMaterialInfo.


        :param id: The id of this BTPartMaterialInfo.  # noqa: E501
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
        if not isinstance(other, BTPartMaterialInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
