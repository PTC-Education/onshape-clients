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


class BTCloudStorageObjectListInfo(object):
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
        'href': 'str',
        'path_to_root': 'list[CloudObjectPathSegment]',
        'items': 'list[BTCloudStorageObjectInfo]',
        'next': 'str'
    }

    attribute_map = {
        'href': 'href',
        'path_to_root': 'pathToRoot',
        'items': 'items',
        'next': 'next'
    }

    def __init__(self, href=None, path_to_root=None, items=None, next=None):  # noqa: E501
        """BTCloudStorageObjectListInfo - a model defined in OpenAPI"""  # noqa: E501

        self._href = None
        self._path_to_root = None
        self._items = None
        self._next = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if path_to_root is not None:
            self.path_to_root = path_to_root
        if items is not None:
            self.items = items
        if next is not None:
            self.next = next

    @property
    def href(self):
        """Gets the href of this BTCloudStorageObjectListInfo.  # noqa: E501


        :return: The href of this BTCloudStorageObjectListInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTCloudStorageObjectListInfo.


        :param href: The href of this BTCloudStorageObjectListInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def path_to_root(self):
        """Gets the path_to_root of this BTCloudStorageObjectListInfo.  # noqa: E501


        :return: The path_to_root of this BTCloudStorageObjectListInfo.  # noqa: E501
        :rtype: list[CloudObjectPathSegment]
        """
        return self._path_to_root

    @path_to_root.setter
    def path_to_root(self, path_to_root):
        """Sets the path_to_root of this BTCloudStorageObjectListInfo.


        :param path_to_root: The path_to_root of this BTCloudStorageObjectListInfo.  # noqa: E501
        :type: list[CloudObjectPathSegment]
        """

        self._path_to_root = path_to_root

    @property
    def items(self):
        """Gets the items of this BTCloudStorageObjectListInfo.  # noqa: E501


        :return: The items of this BTCloudStorageObjectListInfo.  # noqa: E501
        :rtype: list[BTCloudStorageObjectInfo]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this BTCloudStorageObjectListInfo.


        :param items: The items of this BTCloudStorageObjectListInfo.  # noqa: E501
        :type: list[BTCloudStorageObjectInfo]
        """

        self._items = items

    @property
    def next(self):
        """Gets the next of this BTCloudStorageObjectListInfo.  # noqa: E501


        :return: The next of this BTCloudStorageObjectListInfo.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this BTCloudStorageObjectListInfo.


        :param next: The next of this BTCloudStorageObjectListInfo.  # noqa: E501
        :type: str
        """

        self._next = next

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
        if not isinstance(other, BTCloudStorageObjectListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
