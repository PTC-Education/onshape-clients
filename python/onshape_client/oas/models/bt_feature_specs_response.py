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


class BTFeatureSpecsResponse(object):
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
        'feature_specs': 'list[BTFeatureSpec]',
        'source_microversion': 'str',
        'reject_microversion_skew': 'bool',
        'microversion_skew': 'bool',
        'library_version': 'int',
        'serialization_version': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'feature_specs': 'featureSpecs',
        'source_microversion': 'sourceMicroversion',
        'reject_microversion_skew': 'rejectMicroversionSkew',
        'microversion_skew': 'microversionSkew',
        'library_version': 'libraryVersion',
        'serialization_version': 'serializationVersion',
        'bt_type': 'btType'
    }

    def __init__(self, feature_specs=None, source_microversion=None, reject_microversion_skew=None, microversion_skew=None, library_version=None, serialization_version=None, bt_type=None):  # noqa: E501
        """BTFeatureSpecsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._feature_specs = None
        self._source_microversion = None
        self._reject_microversion_skew = None
        self._microversion_skew = None
        self._library_version = None
        self._serialization_version = None
        self._bt_type = None
        self.discriminator = None

        if feature_specs is not None:
            self.feature_specs = feature_specs
        if source_microversion is not None:
            self.source_microversion = source_microversion
        if reject_microversion_skew is not None:
            self.reject_microversion_skew = reject_microversion_skew
        if microversion_skew is not None:
            self.microversion_skew = microversion_skew
        if library_version is not None:
            self.library_version = library_version
        if serialization_version is not None:
            self.serialization_version = serialization_version
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def feature_specs(self):
        """Gets the feature_specs of this BTFeatureSpecsResponse.  # noqa: E501


        :return: The feature_specs of this BTFeatureSpecsResponse.  # noqa: E501
        :rtype: list[BTFeatureSpec]
        """
        return self._feature_specs

    @feature_specs.setter
    def feature_specs(self, feature_specs):
        """Sets the feature_specs of this BTFeatureSpecsResponse.


        :param feature_specs: The feature_specs of this BTFeatureSpecsResponse.  # noqa: E501
        :type: list[BTFeatureSpec]
        """

        self._feature_specs = feature_specs

    @property
    def source_microversion(self):
        """Gets the source_microversion of this BTFeatureSpecsResponse.  # noqa: E501


        :return: The source_microversion of this BTFeatureSpecsResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_microversion

    @source_microversion.setter
    def source_microversion(self, source_microversion):
        """Sets the source_microversion of this BTFeatureSpecsResponse.


        :param source_microversion: The source_microversion of this BTFeatureSpecsResponse.  # noqa: E501
        :type: str
        """

        self._source_microversion = source_microversion

    @property
    def reject_microversion_skew(self):
        """Gets the reject_microversion_skew of this BTFeatureSpecsResponse.  # noqa: E501


        :return: The reject_microversion_skew of this BTFeatureSpecsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._reject_microversion_skew

    @reject_microversion_skew.setter
    def reject_microversion_skew(self, reject_microversion_skew):
        """Sets the reject_microversion_skew of this BTFeatureSpecsResponse.


        :param reject_microversion_skew: The reject_microversion_skew of this BTFeatureSpecsResponse.  # noqa: E501
        :type: bool
        """

        self._reject_microversion_skew = reject_microversion_skew

    @property
    def microversion_skew(self):
        """Gets the microversion_skew of this BTFeatureSpecsResponse.  # noqa: E501


        :return: The microversion_skew of this BTFeatureSpecsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._microversion_skew

    @microversion_skew.setter
    def microversion_skew(self, microversion_skew):
        """Sets the microversion_skew of this BTFeatureSpecsResponse.


        :param microversion_skew: The microversion_skew of this BTFeatureSpecsResponse.  # noqa: E501
        :type: bool
        """

        self._microversion_skew = microversion_skew

    @property
    def library_version(self):
        """Gets the library_version of this BTFeatureSpecsResponse.  # noqa: E501


        :return: The library_version of this BTFeatureSpecsResponse.  # noqa: E501
        :rtype: int
        """
        return self._library_version

    @library_version.setter
    def library_version(self, library_version):
        """Sets the library_version of this BTFeatureSpecsResponse.


        :param library_version: The library_version of this BTFeatureSpecsResponse.  # noqa: E501
        :type: int
        """

        self._library_version = library_version

    @property
    def serialization_version(self):
        """Gets the serialization_version of this BTFeatureSpecsResponse.  # noqa: E501


        :return: The serialization_version of this BTFeatureSpecsResponse.  # noqa: E501
        :rtype: str
        """
        return self._serialization_version

    @serialization_version.setter
    def serialization_version(self, serialization_version):
        """Sets the serialization_version of this BTFeatureSpecsResponse.


        :param serialization_version: The serialization_version of this BTFeatureSpecsResponse.  # noqa: E501
        :type: str
        """

        self._serialization_version = serialization_version

    @property
    def bt_type(self):
        """Gets the bt_type of this BTFeatureSpecsResponse.  # noqa: E501


        :return: The bt_type of this BTFeatureSpecsResponse.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTFeatureSpecsResponse.


        :param bt_type: The bt_type of this BTFeatureSpecsResponse.  # noqa: E501
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
        if not isinstance(other, BTFeatureSpecsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
