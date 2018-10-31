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


class AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances(object):
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
        'name': 'str',
        'part_id': 'str',
        'document_microversion': 'str',
        'type': 'str',
        'document_version': 'str',
        'element_id': 'str',
        'configuration': 'str',
        'suppressed': 'bool',
        'id': 'str',
        'document_id': 'str',
        'is_standard_content': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'part_id': 'partId',
        'document_microversion': 'documentMicroversion',
        'type': 'type',
        'document_version': 'documentVersion',
        'element_id': 'elementId',
        'configuration': 'configuration',
        'suppressed': 'suppressed',
        'id': 'id',
        'document_id': 'documentId',
        'is_standard_content': 'isStandardContent'
    }

    def __init__(self, name=None, part_id=None, document_microversion=None, type=None, document_version=None, element_id=None, configuration=None, suppressed=None, id=None, document_id=None, is_standard_content=None):  # noqa: E501
        """AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._part_id = None
        self._document_microversion = None
        self._type = None
        self._document_version = None
        self._element_id = None
        self._configuration = None
        self._suppressed = None
        self._id = None
        self._document_id = None
        self._is_standard_content = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if part_id is not None:
            self.part_id = part_id
        if document_microversion is not None:
            self.document_microversion = document_microversion
        if type is not None:
            self.type = type
        if document_version is not None:
            self.document_version = document_version
        if element_id is not None:
            self.element_id = element_id
        if configuration is not None:
            self.configuration = configuration
        if suppressed is not None:
            self.suppressed = suppressed
        if id is not None:
            self.id = id
        if document_id is not None:
            self.document_id = document_id
        if is_standard_content is not None:
            self.is_standard_content = is_standard_content

    @property
    def name(self):
        """Gets the name of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Part/feature/assembly name  # noqa: E501

        :return: The name of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Part/feature/assembly name  # noqa: E501

        :param name: The name of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def part_id(self):
        """Gets the part_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Deterministic part ID if type is Part. If the             part cannot be resolved, the value will be the empty string. This can happen if a change in the             source part studio causes the part that was originally referenced to be missing.  # noqa: E501

        :return: The part_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Deterministic part ID if type is Part. If the             part cannot be resolved, the value will be the empty string. This can happen if a change in the             source part studio causes the part that was originally referenced to be missing.  # noqa: E501

        :param part_id: The part_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def document_microversion(self):
        """Gets the document_microversion of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Microversion ID of document             containing the included instance  # noqa: E501

        :return: The document_microversion of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: str
        """
        return self._document_microversion

    @document_microversion.setter
    def document_microversion(self, document_microversion):
        """Sets the document_microversion of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Microversion ID of document             containing the included instance  # noqa: E501

        :param document_microversion: The document_microversion of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: str
        """

        self._document_microversion = document_microversion

    @property
    def type(self):
        """Gets the type of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Instance type. Current valid values are Part,             Assembly, Feature. Other values may be added in the future. Note that \"Part\" may mean a reference to             a surface or a solid and that \"Feature\" currently means a reference to a Sketch, but support for             other feature types may be added in the future. For Part, a specific bodyType is included in the             parts information and for Feature, a specific featureType is included in the partStudioFeatures             information.  # noqa: E501

        :return: The type of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Instance type. Current valid values are Part,             Assembly, Feature. Other values may be added in the future. Note that \"Part\" may mean a reference to             a surface or a solid and that \"Feature\" currently means a reference to a Sketch, but support for             other feature types may be added in the future. For Part, a specific bodyType is included in the             parts information and for Feature, a specific featureType is included in the partStudioFeatures             information.  # noqa: E501

        :param type: The type of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def document_version(self):
        """Gets the document_version of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Version ID of document containing the             included instance, if reached through one or more version references  # noqa: E501

        :return: The document_version of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: str
        """
        return self._document_version

    @document_version.setter
    def document_version(self, document_version):
        """Sets the document_version of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Version ID of document containing the             included instance, if reached through one or more version references  # noqa: E501

        :param document_version: The document_version of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: str
        """

        self._document_version = document_version

    @property
    def element_id(self):
        """Gets the element_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Element ID of the part/assembly instance  # noqa: E501

        :return: The element_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Element ID of the part/assembly instance  # noqa: E501

        :param element_id: The element_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def configuration(self):
        """Gets the configuration of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Configuration of the Part studio element                    if the instance references a Part studio.  # noqa: E501

        :return: The configuration of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Configuration of the Part studio element                    if the instance references a Part studio.  # noqa: E501

        :param configuration: The configuration of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def suppressed(self):
        """Gets the suppressed of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Instance suppressed or not  # noqa: E501

        :return: The suppressed of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: bool
        """
        return self._suppressed

    @suppressed.setter
    def suppressed(self, suppressed):
        """Sets the suppressed of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Instance suppressed or not  # noqa: E501

        :param suppressed: The suppressed of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: bool
        """

        self._suppressed = suppressed

    @property
    def id(self):
        """Gets the id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Instance ID  # noqa: E501

        :return: The id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Instance ID  # noqa: E501

        :param id: The id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def document_id(self):
        """Gets the document_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        Document ID for the document containing the             included instance  # noqa: E501

        :return: The document_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        Document ID for the document containing the             included instance  # noqa: E501

        :param document_id: The document_id of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def is_standard_content(self):
        """Gets the is_standard_content of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501

        If type is Part this field             indicates whether the part is Standard Content.  # noqa: E501

        :return: The is_standard_content of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :rtype: bool
        """
        return self._is_standard_content

    @is_standard_content.setter
    def is_standard_content(self, is_standard_content):
        """Sets the is_standard_content of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.

        If type is Part this field             indicates whether the part is Standard Content.  # noqa: E501

        :param is_standard_content: The is_standard_content of this AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances.  # noqa: E501
        :type: bool
        """

        self._is_standard_content = is_standard_content

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
        if not isinstance(other, AssembliesGetAssemblyDefinitionResponse200RootAssemblyInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
