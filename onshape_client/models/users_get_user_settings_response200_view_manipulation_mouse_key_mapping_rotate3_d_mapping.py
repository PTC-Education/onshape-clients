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


class UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping(object):
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
        'keys': 'list[str]',
        'mouse_buttons': 'list[str]'
    }

    attribute_map = {
        'keys': 'keys',
        'mouse_buttons': 'mouseButtons'
    }

    def __init__(self, keys=None, mouse_buttons=None):  # noqa: E501
        """UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping - a model defined in Swagger"""  # noqa: E501

        self._keys = None
        self._mouse_buttons = None
        self.discriminator = None

        if keys is not None:
            self.keys = keys
        if mouse_buttons is not None:
            self.mouse_buttons = mouse_buttons

    @property
    def keys(self):
        """Gets the keys of this UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping.  # noqa: E501

        Array of modifier keys for set of button and key presses  # noqa: E501

        :return: The keys of this UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping.  # noqa: E501
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping.

        Array of modifier keys for set of button and key presses  # noqa: E501

        :param keys: The keys of this UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping.  # noqa: E501
        :type: list[str]
        """

        self._keys = keys

    @property
    def mouse_buttons(self):
        """Gets the mouse_buttons of this UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping.  # noqa: E501

        Array of mouse buttons for set of button and key presses  # noqa: E501

        :return: The mouse_buttons of this UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping.  # noqa: E501
        :rtype: list[str]
        """
        return self._mouse_buttons

    @mouse_buttons.setter
    def mouse_buttons(self, mouse_buttons):
        """Sets the mouse_buttons of this UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping.

        Array of mouse buttons for set of button and key presses  # noqa: E501

        :param mouse_buttons: The mouse_buttons of this UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping.  # noqa: E501
        :type: list[str]
        """

        self._mouse_buttons = mouse_buttons

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
        if not isinstance(other, UsersGetUserSettingsResponse200ViewManipulationMouseKeyMappingRotate3DMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
