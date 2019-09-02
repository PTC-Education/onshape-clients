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


class GBTMAssemblyFeature(object):
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
        'node_id': 'str',
        'namespace': 'str',
        'import_microversion': 'str',
        'name': 'str',
        'suppressed': 'bool',
        'parameters': 'list[BTMParameter]',
        'feature_type': 'str',
        'feature_id': 'str',
        'sub_features': 'list[BTMFeature]',
        'return_after_subfeatures': 'bool',
        'version': 'int'
    }

    attribute_map = {
        'node_id': 'nodeId',
        'namespace': 'namespace',
        'import_microversion': 'importMicroversion',
        'name': 'name',
        'suppressed': 'suppressed',
        'parameters': 'parameters',
        'feature_type': 'featureType',
        'feature_id': 'featureId',
        'sub_features': 'subFeatures',
        'return_after_subfeatures': 'returnAfterSubfeatures',
        'version': 'version'
    }

    def __init__(self, node_id=None, namespace=None, import_microversion=None, name=None, suppressed=None, parameters=None, feature_type=None, feature_id=None, sub_features=None, return_after_subfeatures=None, version=None):  # noqa: E501
        """GBTMAssemblyFeature - a model defined in OpenAPI"""  # noqa: E501

        self._node_id = None
        self._namespace = None
        self._import_microversion = None
        self._name = None
        self._suppressed = None
        self._parameters = None
        self._feature_type = None
        self._feature_id = None
        self._sub_features = None
        self._return_after_subfeatures = None
        self._version = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if namespace is not None:
            self.namespace = namespace
        if import_microversion is not None:
            self.import_microversion = import_microversion
        if name is not None:
            self.name = name
        if suppressed is not None:
            self.suppressed = suppressed
        if parameters is not None:
            self.parameters = parameters
        if feature_type is not None:
            self.feature_type = feature_type
        if feature_id is not None:
            self.feature_id = feature_id
        if sub_features is not None:
            self.sub_features = sub_features
        if return_after_subfeatures is not None:
            self.return_after_subfeatures = return_after_subfeatures
        if version is not None:
            self.version = version

    @property
    def node_id(self):
        """Gets the node_id of this GBTMAssemblyFeature.  # noqa: E501


        :return: The node_id of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this GBTMAssemblyFeature.


        :param node_id: The node_id of this GBTMAssemblyFeature.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def namespace(self):
        """Gets the namespace of this GBTMAssemblyFeature.  # noqa: E501


        :return: The namespace of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this GBTMAssemblyFeature.


        :param namespace: The namespace of this GBTMAssemblyFeature.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def import_microversion(self):
        """Gets the import_microversion of this GBTMAssemblyFeature.  # noqa: E501


        :return: The import_microversion of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: str
        """
        return self._import_microversion

    @import_microversion.setter
    def import_microversion(self, import_microversion):
        """Sets the import_microversion of this GBTMAssemblyFeature.


        :param import_microversion: The import_microversion of this GBTMAssemblyFeature.  # noqa: E501
        :type: str
        """

        self._import_microversion = import_microversion

    @property
    def name(self):
        """Gets the name of this GBTMAssemblyFeature.  # noqa: E501


        :return: The name of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GBTMAssemblyFeature.


        :param name: The name of this GBTMAssemblyFeature.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def suppressed(self):
        """Gets the suppressed of this GBTMAssemblyFeature.  # noqa: E501


        :return: The suppressed of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: bool
        """
        return self._suppressed

    @suppressed.setter
    def suppressed(self, suppressed):
        """Sets the suppressed of this GBTMAssemblyFeature.


        :param suppressed: The suppressed of this GBTMAssemblyFeature.  # noqa: E501
        :type: bool
        """

        self._suppressed = suppressed

    @property
    def parameters(self):
        """Gets the parameters of this GBTMAssemblyFeature.  # noqa: E501


        :return: The parameters of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: list[BTMParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this GBTMAssemblyFeature.


        :param parameters: The parameters of this GBTMAssemblyFeature.  # noqa: E501
        :type: list[BTMParameter]
        """

        self._parameters = parameters

    @property
    def feature_type(self):
        """Gets the feature_type of this GBTMAssemblyFeature.  # noqa: E501


        :return: The feature_type of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: str
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """Sets the feature_type of this GBTMAssemblyFeature.


        :param feature_type: The feature_type of this GBTMAssemblyFeature.  # noqa: E501
        :type: str
        """

        self._feature_type = feature_type

    @property
    def feature_id(self):
        """Gets the feature_id of this GBTMAssemblyFeature.  # noqa: E501


        :return: The feature_id of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this GBTMAssemblyFeature.


        :param feature_id: The feature_id of this GBTMAssemblyFeature.  # noqa: E501
        :type: str
        """

        self._feature_id = feature_id

    @property
    def sub_features(self):
        """Gets the sub_features of this GBTMAssemblyFeature.  # noqa: E501


        :return: The sub_features of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: list[BTMFeature]
        """
        return self._sub_features

    @sub_features.setter
    def sub_features(self, sub_features):
        """Sets the sub_features of this GBTMAssemblyFeature.


        :param sub_features: The sub_features of this GBTMAssemblyFeature.  # noqa: E501
        :type: list[BTMFeature]
        """

        self._sub_features = sub_features

    @property
    def return_after_subfeatures(self):
        """Gets the return_after_subfeatures of this GBTMAssemblyFeature.  # noqa: E501


        :return: The return_after_subfeatures of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: bool
        """
        return self._return_after_subfeatures

    @return_after_subfeatures.setter
    def return_after_subfeatures(self, return_after_subfeatures):
        """Sets the return_after_subfeatures of this GBTMAssemblyFeature.


        :param return_after_subfeatures: The return_after_subfeatures of this GBTMAssemblyFeature.  # noqa: E501
        :type: bool
        """

        self._return_after_subfeatures = return_after_subfeatures

    @property
    def version(self):
        """Gets the version of this GBTMAssemblyFeature.  # noqa: E501


        :return: The version of this GBTMAssemblyFeature.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GBTMAssemblyFeature.


        :param version: The version of this GBTMAssemblyFeature.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if not isinstance(other, GBTMAssemblyFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
