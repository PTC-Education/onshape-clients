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


class PartStudiosGetFeaturesResponse200Message(object):
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
        'path': 'str',
        'version': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'path': 'path',
        'version': 'version',
        'namespace': 'namespace'
    }

    def __init__(self, path=None, version=None, namespace=None):  # noqa: E501
        """PartStudiosGetFeaturesResponse200Message - a model defined in Swagger"""  # noqa: E501

        self._path = None
        self._version = None
        self._namespace = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if version is not None:
            self.version = version
        if namespace is not None:
            self.namespace = namespace

    @property
    def path(self):
        """Gets the path of this PartStudiosGetFeaturesResponse200Message.  # noqa: E501

        The path for an import  # noqa: E501

        :return: The path of this PartStudiosGetFeaturesResponse200Message.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PartStudiosGetFeaturesResponse200Message.

        The path for an import  # noqa: E501

        :param path: The path of this PartStudiosGetFeaturesResponse200Message.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def version(self):
        """Gets the version of this PartStudiosGetFeaturesResponse200Message.  # noqa: E501

        The version for an import  # noqa: E501

        :return: The version of this PartStudiosGetFeaturesResponse200Message.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PartStudiosGetFeaturesResponse200Message.

        The version for an import  # noqa: E501

        :param version: The version of this PartStudiosGetFeaturesResponse200Message.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def namespace(self):
        """Gets the namespace of this PartStudiosGetFeaturesResponse200Message.  # noqa: E501

        The namespace for an import  # noqa: E501

        :return: The namespace of this PartStudiosGetFeaturesResponse200Message.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this PartStudiosGetFeaturesResponse200Message.

        The namespace for an import  # noqa: E501

        :param namespace: The namespace of this PartStudiosGetFeaturesResponse200Message.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if not isinstance(other, PartStudiosGetFeaturesResponse200Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
