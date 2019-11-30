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


class BTMImport(object):
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
        'imported_external_document_id': 'str',
        'element_import': 'bool',
        'node_id': 'str',
        'namespace': 'str',
        'import_microversion': 'str',
        'path': 'str',
        'version': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'imported_external_document_id': 'importedExternalDocumentId',
        'element_import': 'elementImport',
        'node_id': 'nodeId',
        'namespace': 'namespace',
        'import_microversion': 'importMicroversion',
        'path': 'path',
        'version': 'version',
        'bt_type': 'btType'
    }

    def __init__(self, imported_external_document_id=None, element_import=None, node_id=None, namespace=None, import_microversion=None, path=None, version=None, bt_type=None):  # noqa: E501
        """BTMImport - a model defined in OpenAPI"""  # noqa: E501

        self._imported_external_document_id = None
        self._element_import = None
        self._node_id = None
        self._namespace = None
        self._import_microversion = None
        self._path = None
        self._version = None
        self._bt_type = None
        self.discriminator = None

        if imported_external_document_id is not None:
            self.imported_external_document_id = imported_external_document_id
        if element_import is not None:
            self.element_import = element_import
        if node_id is not None:
            self.node_id = node_id
        if namespace is not None:
            self.namespace = namespace
        if import_microversion is not None:
            self.import_microversion = import_microversion
        if path is not None:
            self.path = path
        if version is not None:
            self.version = version
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def imported_external_document_id(self):
        """Gets the imported_external_document_id of this BTMImport.  # noqa: E501


        :return: The imported_external_document_id of this BTMImport.  # noqa: E501
        :rtype: str
        """
        return self._imported_external_document_id

    @imported_external_document_id.setter
    def imported_external_document_id(self, imported_external_document_id):
        """Sets the imported_external_document_id of this BTMImport.


        :param imported_external_document_id: The imported_external_document_id of this BTMImport.  # noqa: E501
        :type: str
        """

        self._imported_external_document_id = imported_external_document_id

    @property
    def element_import(self):
        """Gets the element_import of this BTMImport.  # noqa: E501


        :return: The element_import of this BTMImport.  # noqa: E501
        :rtype: bool
        """
        return self._element_import

    @element_import.setter
    def element_import(self, element_import):
        """Sets the element_import of this BTMImport.


        :param element_import: The element_import of this BTMImport.  # noqa: E501
        :type: bool
        """

        self._element_import = element_import

    @property
    def node_id(self):
        """Gets the node_id of this BTMImport.  # noqa: E501


        :return: The node_id of this BTMImport.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTMImport.


        :param node_id: The node_id of this BTMImport.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def namespace(self):
        """Gets the namespace of this BTMImport.  # noqa: E501


        :return: The namespace of this BTMImport.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BTMImport.


        :param namespace: The namespace of this BTMImport.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def import_microversion(self):
        """Gets the import_microversion of this BTMImport.  # noqa: E501


        :return: The import_microversion of this BTMImport.  # noqa: E501
        :rtype: str
        """
        return self._import_microversion

    @import_microversion.setter
    def import_microversion(self, import_microversion):
        """Sets the import_microversion of this BTMImport.


        :param import_microversion: The import_microversion of this BTMImport.  # noqa: E501
        :type: str
        """

        self._import_microversion = import_microversion

    @property
    def path(self):
        """Gets the path of this BTMImport.  # noqa: E501


        :return: The path of this BTMImport.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BTMImport.


        :param path: The path of this BTMImport.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def version(self):
        """Gets the version of this BTMImport.  # noqa: E501


        :return: The version of this BTMImport.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BTMImport.


        :param version: The version of this BTMImport.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def bt_type(self):
        """Gets the bt_type of this BTMImport.  # noqa: E501


        :return: The bt_type of this BTMImport.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTMImport.


        :param bt_type: The bt_type of this BTMImport.  # noqa: E501
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
        if not isinstance(other, BTMImport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
