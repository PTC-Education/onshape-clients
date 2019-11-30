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


class BTCacheDataPath191(object):
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
        'url': 'str',
        'document_id': 'str',
        'element_id': 'str',
        'full_file_path': 'str',
        'use_local_file_cache': 'bool',
        'expire_secs': 'str',
        'is_persisted': 'bool',
        'key': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'url': 'url',
        'document_id': 'documentId',
        'element_id': 'elementId',
        'full_file_path': 'fullFilePath',
        'use_local_file_cache': 'useLocalFileCache',
        'expire_secs': 'expireSecs',
        'is_persisted': 'isPersisted',
        'key': 'key',
        'bt_type': 'btType'
    }

    def __init__(self, url=None, document_id=None, element_id=None, full_file_path=None, use_local_file_cache=None, expire_secs=None, is_persisted=None, key=None, bt_type=None):  # noqa: E501
        """BTCacheDataPath191 - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._document_id = None
        self._element_id = None
        self._full_file_path = None
        self._use_local_file_cache = None
        self._expire_secs = None
        self._is_persisted = None
        self._key = None
        self._bt_type = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if document_id is not None:
            self.document_id = document_id
        if element_id is not None:
            self.element_id = element_id
        if full_file_path is not None:
            self.full_file_path = full_file_path
        if use_local_file_cache is not None:
            self.use_local_file_cache = use_local_file_cache
        if expire_secs is not None:
            self.expire_secs = expire_secs
        if is_persisted is not None:
            self.is_persisted = is_persisted
        if key is not None:
            self.key = key
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def url(self):
        """Gets the url of this BTCacheDataPath191.  # noqa: E501


        :return: The url of this BTCacheDataPath191.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BTCacheDataPath191.


        :param url: The url of this BTCacheDataPath191.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def document_id(self):
        """Gets the document_id of this BTCacheDataPath191.  # noqa: E501


        :return: The document_id of this BTCacheDataPath191.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTCacheDataPath191.


        :param document_id: The document_id of this BTCacheDataPath191.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def element_id(self):
        """Gets the element_id of this BTCacheDataPath191.  # noqa: E501


        :return: The element_id of this BTCacheDataPath191.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTCacheDataPath191.


        :param element_id: The element_id of this BTCacheDataPath191.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def full_file_path(self):
        """Gets the full_file_path of this BTCacheDataPath191.  # noqa: E501


        :return: The full_file_path of this BTCacheDataPath191.  # noqa: E501
        :rtype: str
        """
        return self._full_file_path

    @full_file_path.setter
    def full_file_path(self, full_file_path):
        """Sets the full_file_path of this BTCacheDataPath191.


        :param full_file_path: The full_file_path of this BTCacheDataPath191.  # noqa: E501
        :type: str
        """

        self._full_file_path = full_file_path

    @property
    def use_local_file_cache(self):
        """Gets the use_local_file_cache of this BTCacheDataPath191.  # noqa: E501


        :return: The use_local_file_cache of this BTCacheDataPath191.  # noqa: E501
        :rtype: bool
        """
        return self._use_local_file_cache

    @use_local_file_cache.setter
    def use_local_file_cache(self, use_local_file_cache):
        """Sets the use_local_file_cache of this BTCacheDataPath191.


        :param use_local_file_cache: The use_local_file_cache of this BTCacheDataPath191.  # noqa: E501
        :type: bool
        """

        self._use_local_file_cache = use_local_file_cache

    @property
    def expire_secs(self):
        """Gets the expire_secs of this BTCacheDataPath191.  # noqa: E501


        :return: The expire_secs of this BTCacheDataPath191.  # noqa: E501
        :rtype: str
        """
        return self._expire_secs

    @expire_secs.setter
    def expire_secs(self, expire_secs):
        """Sets the expire_secs of this BTCacheDataPath191.


        :param expire_secs: The expire_secs of this BTCacheDataPath191.  # noqa: E501
        :type: str
        """

        self._expire_secs = expire_secs

    @property
    def is_persisted(self):
        """Gets the is_persisted of this BTCacheDataPath191.  # noqa: E501


        :return: The is_persisted of this BTCacheDataPath191.  # noqa: E501
        :rtype: bool
        """
        return self._is_persisted

    @is_persisted.setter
    def is_persisted(self, is_persisted):
        """Sets the is_persisted of this BTCacheDataPath191.


        :param is_persisted: The is_persisted of this BTCacheDataPath191.  # noqa: E501
        :type: bool
        """

        self._is_persisted = is_persisted

    @property
    def key(self):
        """Gets the key of this BTCacheDataPath191.  # noqa: E501


        :return: The key of this BTCacheDataPath191.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this BTCacheDataPath191.


        :param key: The key of this BTCacheDataPath191.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def bt_type(self):
        """Gets the bt_type of this BTCacheDataPath191.  # noqa: E501


        :return: The bt_type of this BTCacheDataPath191.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTCacheDataPath191.


        :param bt_type: The bt_type of this BTCacheDataPath191.  # noqa: E501
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
        if not isinstance(other, BTCacheDataPath191):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
