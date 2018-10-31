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


class DocumentsShareDocumentResponse200Owner1(object):
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
        'type': 'float',
        'id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id'
    }

    def __init__(self, type=None, id=None):  # noqa: E501
        """DocumentsShareDocumentResponse200Owner1 - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id

    @property
    def type(self):
        """Gets the type of this DocumentsShareDocumentResponse200Owner1.  # noqa: E501

        Type of the object owner. Possible values include 0=User, 1=Company,       2=Team, 3=<Reserved>, 4=Application  # noqa: E501

        :return: The type of this DocumentsShareDocumentResponse200Owner1.  # noqa: E501
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DocumentsShareDocumentResponse200Owner1.

        Type of the object owner. Possible values include 0=User, 1=Company,       2=Team, 3=<Reserved>, 4=Application  # noqa: E501

        :param type: The type of this DocumentsShareDocumentResponse200Owner1.  # noqa: E501
        :type: float
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this DocumentsShareDocumentResponse200Owner1.  # noqa: E501

        ID of the object owner  # noqa: E501

        :return: The id of this DocumentsShareDocumentResponse200Owner1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsShareDocumentResponse200Owner1.

        ID of the object owner  # noqa: E501

        :param id: The id of this DocumentsShareDocumentResponse200Owner1.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, DocumentsShareDocumentResponse200Owner1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
