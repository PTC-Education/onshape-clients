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


class BTExternalElementReferenceInfo(object):
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
        'version_id': 'str',
        'element_id': 'str',
        'document_id': 'str',
        'element_microversion_id': 'str'
    }

    attribute_map = {
        'version_id': 'versionId',
        'element_id': 'elementId',
        'document_id': 'documentId',
        'element_microversion_id': 'elementMicroversionId'
    }

    def __init__(self, version_id=None, element_id=None, document_id=None, element_microversion_id=None):  # noqa: E501
        """BTExternalElementReferenceInfo - a model defined in OpenAPI"""  # noqa: E501

        self._version_id = None
        self._element_id = None
        self._document_id = None
        self._element_microversion_id = None
        self.discriminator = None

        if version_id is not None:
            self.version_id = version_id
        if element_id is not None:
            self.element_id = element_id
        if document_id is not None:
            self.document_id = document_id
        if element_microversion_id is not None:
            self.element_microversion_id = element_microversion_id

    @property
    def version_id(self):
        """Gets the version_id of this BTExternalElementReferenceInfo.  # noqa: E501


        :return: The version_id of this BTExternalElementReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTExternalElementReferenceInfo.


        :param version_id: The version_id of this BTExternalElementReferenceInfo.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def element_id(self):
        """Gets the element_id of this BTExternalElementReferenceInfo.  # noqa: E501


        :return: The element_id of this BTExternalElementReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTExternalElementReferenceInfo.


        :param element_id: The element_id of this BTExternalElementReferenceInfo.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def document_id(self):
        """Gets the document_id of this BTExternalElementReferenceInfo.  # noqa: E501


        :return: The document_id of this BTExternalElementReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTExternalElementReferenceInfo.


        :param document_id: The document_id of this BTExternalElementReferenceInfo.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def element_microversion_id(self):
        """Gets the element_microversion_id of this BTExternalElementReferenceInfo.  # noqa: E501


        :return: The element_microversion_id of this BTExternalElementReferenceInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_microversion_id

    @element_microversion_id.setter
    def element_microversion_id(self, element_microversion_id):
        """Sets the element_microversion_id of this BTExternalElementReferenceInfo.


        :param element_microversion_id: The element_microversion_id of this BTExternalElementReferenceInfo.  # noqa: E501
        :type: str
        """

        self._element_microversion_id = element_microversion_id

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
        if not isinstance(other, BTExternalElementReferenceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
