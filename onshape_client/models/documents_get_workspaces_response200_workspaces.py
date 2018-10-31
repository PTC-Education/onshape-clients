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

from onshape_client.models.documents_create_document_response200_default_workspace_creator import DocumentsCreateDocumentResponse200DefaultWorkspaceCreator  # noqa: F401,E501
from onshape_client.models.documents_create_document_response200_default_workspace_last_modifier import DocumentsCreateDocumentResponse200DefaultWorkspaceLastModifier  # noqa: F401,E501


class DocumentsGetWorkspacesResponse200Workspaces(object):
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
        'description': 'str',
        'parent': 'str',
        'creator': 'DocumentsCreateDocumentResponse200DefaultWorkspaceCreator',
        'is_read_only': 'bool',
        'can_delete': 'bool',
        'microversion': 'str',
        'name': 'str',
        'modified_at': 'datetime',
        'type': 'str',
        'id': 'str',
        'created_at': 'datetime',
        'last_modifier': 'DocumentsCreateDocumentResponse200DefaultWorkspaceLastModifier'
    }

    attribute_map = {
        'description': 'description',
        'parent': 'parent',
        'creator': 'creator',
        'is_read_only': 'isReadOnly',
        'can_delete': 'canDelete',
        'microversion': 'microversion',
        'name': 'name',
        'modified_at': 'modifiedAt',
        'type': 'type',
        'id': 'id',
        'created_at': 'createdAt',
        'last_modifier': 'lastModifier'
    }

    def __init__(self, description=None, parent=None, creator=None, is_read_only=None, can_delete=None, microversion=None, name=None, modified_at=None, type=None, id=None, created_at=None, last_modifier=None):  # noqa: E501
        """DocumentsGetWorkspacesResponse200Workspaces - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._parent = None
        self._creator = None
        self._is_read_only = None
        self._can_delete = None
        self._microversion = None
        self._name = None
        self._modified_at = None
        self._type = None
        self._id = None
        self._created_at = None
        self._last_modifier = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if parent is not None:
            self.parent = parent
        if creator is not None:
            self.creator = creator
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if can_delete is not None:
            self.can_delete = can_delete
        if microversion is not None:
            self.microversion = microversion
        if name is not None:
            self.name = name
        if modified_at is not None:
            self.modified_at = modified_at
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if last_modifier is not None:
            self.last_modifier = last_modifier

    @property
    def description(self):
        """Gets the description of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        User-provided description of workspace  # noqa: E501

        :return: The description of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentsGetWorkspacesResponse200Workspaces.

        User-provided description of workspace  # noqa: E501

        :param description: The description of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def parent(self):
        """Gets the parent of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        ID of workspace's parent version  # noqa: E501

        :return: The parent of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this DocumentsGetWorkspacesResponse200Workspaces.

        ID of workspace's parent version  # noqa: E501

        :param parent: The parent of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def creator(self):
        """Gets the creator of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501


        :return: The creator of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: DocumentsCreateDocumentResponse200DefaultWorkspaceCreator
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this DocumentsGetWorkspacesResponse200Workspaces.


        :param creator: The creator of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: DocumentsCreateDocumentResponse200DefaultWorkspaceCreator
        """

        self._creator = creator

    @property
    def is_read_only(self):
        """Gets the is_read_only of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        Whether workspace is read-only  # noqa: E501

        :return: The is_read_only of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this DocumentsGetWorkspacesResponse200Workspaces.

        Whether workspace is read-only  # noqa: E501

        :param is_read_only: The is_read_only of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: bool
        """

        self._is_read_only = is_read_only

    @property
    def can_delete(self):
        """Gets the can_delete of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        Whether workspace can be deleted  # noqa: E501

        :return: The can_delete of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this DocumentsGetWorkspacesResponse200Workspaces.

        Whether workspace can be deleted  # noqa: E501

        :param can_delete: The can_delete of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: bool
        """

        self._can_delete = can_delete

    @property
    def microversion(self):
        """Gets the microversion of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        Document microversion ID that is the root of the             workspace branch  # noqa: E501

        :return: The microversion of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: str
        """
        return self._microversion

    @microversion.setter
    def microversion(self, microversion):
        """Sets the microversion of this DocumentsGetWorkspacesResponse200Workspaces.

        Document microversion ID that is the root of the             workspace branch  # noqa: E501

        :param microversion: The microversion of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: str
        """

        self._microversion = microversion

    @property
    def name(self):
        """Gets the name of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        name of workspace  # noqa: E501

        :return: The name of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentsGetWorkspacesResponse200Workspaces.

        name of workspace  # noqa: E501

        :param name: The name of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def modified_at(self):
        """Gets the modified_at of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        Last modification date  # noqa: E501

        :return: The modified_at of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this DocumentsGetWorkspacesResponse200Workspaces.

        Last modification date  # noqa: E501

        :param modified_at: The modified_at of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def type(self):
        """Gets the type of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        Type of record  # noqa: E501

        :return: The type of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DocumentsGetWorkspacesResponse200Workspaces.

        Type of record  # noqa: E501

        :param type: The type of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        ID of workspace  # noqa: E501

        :return: The id of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsGetWorkspacesResponse200Workspaces.

        ID of workspace  # noqa: E501

        :param id: The id of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501

        Creation date  # noqa: E501

        :return: The created_at of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DocumentsGetWorkspacesResponse200Workspaces.

        Creation date  # noqa: E501

        :param created_at: The created_at of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def last_modifier(self):
        """Gets the last_modifier of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501


        :return: The last_modifier of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :rtype: DocumentsCreateDocumentResponse200DefaultWorkspaceLastModifier
        """
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, last_modifier):
        """Sets the last_modifier of this DocumentsGetWorkspacesResponse200Workspaces.


        :param last_modifier: The last_modifier of this DocumentsGetWorkspacesResponse200Workspaces.  # noqa: E501
        :type: DocumentsCreateDocumentResponse200DefaultWorkspaceLastModifier
        """

        self._last_modifier = last_modifier

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
        if not isinstance(other, DocumentsGetWorkspacesResponse200Workspaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
