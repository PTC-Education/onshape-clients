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

from onshape_client.models.part_studios_get_features_response200_feature_states import PartStudiosGetFeaturesResponse200FeatureStates  # noqa: F401,E501
from onshape_client.models.part_studios_get_features_response200_features import PartStudiosGetFeaturesResponse200Features  # noqa: F401,E501


class AssembliesGetFeaturesResponse200(object):
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
        'source_microversion': 'str',
        'feature_states': 'list[PartStudiosGetFeaturesResponse200FeatureStates]',
        'serialization_version': 'str',
        'features': 'list[PartStudiosGetFeaturesResponse200Features]',
        'is_complete': 'bool'
    }

    attribute_map = {
        'source_microversion': 'sourceMicroversion',
        'feature_states': 'featureStates',
        'serialization_version': 'serializationVersion',
        'features': 'features',
        'is_complete': 'isComplete'
    }

    def __init__(self, source_microversion=None, feature_states=None, serialization_version=None, features=None, is_complete=None):  # noqa: E501
        """AssembliesGetFeaturesResponse200 - a model defined in Swagger"""  # noqa: E501

        self._source_microversion = None
        self._feature_states = None
        self._serialization_version = None
        self._features = None
        self._is_complete = None
        self.discriminator = None

        if source_microversion is not None:
            self.source_microversion = source_microversion
        if feature_states is not None:
            self.feature_states = feature_states
        if serialization_version is not None:
            self.serialization_version = serialization_version
        if features is not None:
            self.features = features
        if is_complete is not None:
            self.is_complete = is_complete

    @property
    def source_microversion(self):
        """Gets the source_microversion of this AssembliesGetFeaturesResponse200.  # noqa: E501

        The document microversion from which the feature was extracted  # noqa: E501

        :return: The source_microversion of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :rtype: str
        """
        return self._source_microversion

    @source_microversion.setter
    def source_microversion(self, source_microversion):
        """Sets the source_microversion of this AssembliesGetFeaturesResponse200.

        The document microversion from which the feature was extracted  # noqa: E501

        :param source_microversion: The source_microversion of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :type: str
        """

        self._source_microversion = source_microversion

    @property
    def feature_states(self):
        """Gets the feature_states of this AssembliesGetFeaturesResponse200.  # noqa: E501

        List of feature state information  # noqa: E501

        :return: The feature_states of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :rtype: list[PartStudiosGetFeaturesResponse200FeatureStates]
        """
        return self._feature_states

    @feature_states.setter
    def feature_states(self, feature_states):
        """Sets the feature_states of this AssembliesGetFeaturesResponse200.

        List of feature state information  # noqa: E501

        :param feature_states: The feature_states of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :type: list[PartStudiosGetFeaturesResponse200FeatureStates]
        """

        self._feature_states = feature_states

    @property
    def serialization_version(self):
        """Gets the serialization_version of this AssembliesGetFeaturesResponse200.  # noqa: E501

        The version of the serialization protocol for the response  # noqa: E501

        :return: The serialization_version of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :rtype: str
        """
        return self._serialization_version

    @serialization_version.setter
    def serialization_version(self, serialization_version):
        """Sets the serialization_version of this AssembliesGetFeaturesResponse200.

        The version of the serialization protocol for the response  # noqa: E501

        :param serialization_version: The serialization_version of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :type: str
        """

        self._serialization_version = serialization_version

    @property
    def features(self):
        """Gets the features of this AssembliesGetFeaturesResponse200.  # noqa: E501

        List of features  # noqa: E501

        :return: The features of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :rtype: list[PartStudiosGetFeaturesResponse200Features]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this AssembliesGetFeaturesResponse200.

        List of features  # noqa: E501

        :param features: The features of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :type: list[PartStudiosGetFeaturesResponse200Features]
        """

        self._features = features

    @property
    def is_complete(self):
        """Gets the is_complete of this AssembliesGetFeaturesResponse200.  # noqa: E501

        True if the full feature list is present, or false if it is filtered  # noqa: E501

        :return: The is_complete of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this AssembliesGetFeaturesResponse200.

        True if the full feature list is present, or false if it is filtered  # noqa: E501

        :param is_complete: The is_complete of this AssembliesGetFeaturesResponse200.  # noqa: E501
        :type: bool
        """

        self._is_complete = is_complete

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
        if not isinstance(other, AssembliesGetFeaturesResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
