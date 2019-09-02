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


class BTCacheItemInfo(object):
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
        'cache_name': 'str',
        'cache_key': 'str',
        'cached': 'bool',
        'last_modified_at': 'int',
        'href': 'str',
        'view_ref': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'cache_name': 'cacheName',
        'cache_key': 'cacheKey',
        'cached': 'cached',
        'last_modified_at': 'lastModifiedAt',
        'href': 'href',
        'view_ref': 'viewRef',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, cache_name=None, cache_key=None, cached=None, last_modified_at=None, href=None, view_ref=None, id=None, name=None):  # noqa: E501
        """BTCacheItemInfo - a model defined in OpenAPI"""  # noqa: E501

        self._cache_name = None
        self._cache_key = None
        self._cached = None
        self._last_modified_at = None
        self._href = None
        self._view_ref = None
        self._id = None
        self._name = None
        self.discriminator = None

        if cache_name is not None:
            self.cache_name = cache_name
        if cache_key is not None:
            self.cache_key = cache_key
        if cached is not None:
            self.cached = cached
        if last_modified_at is not None:
            self.last_modified_at = last_modified_at
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def cache_name(self):
        """Gets the cache_name of this BTCacheItemInfo.  # noqa: E501


        :return: The cache_name of this BTCacheItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._cache_name

    @cache_name.setter
    def cache_name(self, cache_name):
        """Sets the cache_name of this BTCacheItemInfo.


        :param cache_name: The cache_name of this BTCacheItemInfo.  # noqa: E501
        :type: str
        """

        self._cache_name = cache_name

    @property
    def cache_key(self):
        """Gets the cache_key of this BTCacheItemInfo.  # noqa: E501


        :return: The cache_key of this BTCacheItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._cache_key

    @cache_key.setter
    def cache_key(self, cache_key):
        """Sets the cache_key of this BTCacheItemInfo.


        :param cache_key: The cache_key of this BTCacheItemInfo.  # noqa: E501
        :type: str
        """

        self._cache_key = cache_key

    @property
    def cached(self):
        """Gets the cached of this BTCacheItemInfo.  # noqa: E501


        :return: The cached of this BTCacheItemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._cached

    @cached.setter
    def cached(self, cached):
        """Sets the cached of this BTCacheItemInfo.


        :param cached: The cached of this BTCacheItemInfo.  # noqa: E501
        :type: bool
        """

        self._cached = cached

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this BTCacheItemInfo.  # noqa: E501


        :return: The last_modified_at of this BTCacheItemInfo.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this BTCacheItemInfo.


        :param last_modified_at: The last_modified_at of this BTCacheItemInfo.  # noqa: E501
        :type: int
        """

        self._last_modified_at = last_modified_at

    @property
    def href(self):
        """Gets the href of this BTCacheItemInfo.  # noqa: E501


        :return: The href of this BTCacheItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTCacheItemInfo.


        :param href: The href of this BTCacheItemInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTCacheItemInfo.  # noqa: E501


        :return: The view_ref of this BTCacheItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTCacheItemInfo.


        :param view_ref: The view_ref of this BTCacheItemInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def id(self):
        """Gets the id of this BTCacheItemInfo.  # noqa: E501


        :return: The id of this BTCacheItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTCacheItemInfo.


        :param id: The id of this BTCacheItemInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BTCacheItemInfo.  # noqa: E501


        :return: The name of this BTCacheItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTCacheItemInfo.


        :param name: The name of this BTCacheItemInfo.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, BTCacheItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
