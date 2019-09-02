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


class BTPartQueryParams(object):
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
        'configuration': 'str',
        'queries': 'list[str]',
        'link_document_id': 'str'
    }

    attribute_map = {
        'configuration': 'configuration',
        'queries': 'queries',
        'link_document_id': 'linkDocumentId'
    }

    def __init__(self, configuration=None, queries=None, link_document_id=None):  # noqa: E501
        """BTPartQueryParams - a model defined in OpenAPI"""  # noqa: E501

        self._configuration = None
        self._queries = None
        self._link_document_id = None
        self.discriminator = None

        if configuration is not None:
            self.configuration = configuration
        if queries is not None:
            self.queries = queries
        if link_document_id is not None:
            self.link_document_id = link_document_id

    @property
    def configuration(self):
        """Gets the configuration of this BTPartQueryParams.  # noqa: E501


        :return: The configuration of this BTPartQueryParams.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BTPartQueryParams.


        :param configuration: The configuration of this BTPartQueryParams.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def queries(self):
        """Gets the queries of this BTPartQueryParams.  # noqa: E501


        :return: The queries of this BTPartQueryParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this BTPartQueryParams.


        :param queries: The queries of this BTPartQueryParams.  # noqa: E501
        :type: list[str]
        """

        self._queries = queries

    @property
    def link_document_id(self):
        """Gets the link_document_id of this BTPartQueryParams.  # noqa: E501


        :return: The link_document_id of this BTPartQueryParams.  # noqa: E501
        :rtype: str
        """
        return self._link_document_id

    @link_document_id.setter
    def link_document_id(self, link_document_id):
        """Sets the link_document_id of this BTPartQueryParams.


        :param link_document_id: The link_document_id of this BTPartQueryParams.  # noqa: E501
        :type: str
        """

        self._link_document_id = link_document_id

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
        if not isinstance(other, BTPartQueryParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
