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

from onshape_client.models.documents_get_documents_response200_created_by import DocumentsGetDocumentsResponse200CreatedBy  # noqa: F401,E501
from onshape_client.models.documents_get_documents_response200_default_workspace import DocumentsGetDocumentsResponse200DefaultWorkspace  # noqa: F401,E501
from onshape_client.models.documents_get_documents_response200_modified_by import DocumentsGetDocumentsResponse200ModifiedBy  # noqa: F401,E501
from onshape_client.models.documents_get_documents_response200_owner import DocumentsGetDocumentsResponse200Owner  # noqa: F401,E501
from onshape_client.models.documents_get_documents_response200_thumbnail import DocumentsGetDocumentsResponse200Thumbnail  # noqa: F401,E501


class DocumentsGetDocumentsResponse200Items(object):
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
        'size_bytes': 'float',
        'trashed_at': 'datetime',
        'total_workspaces_scheduled_for_update': 'float',
        'name': 'str',
        'can_unshare': 'bool',
        'permission': 'str',
        'href': 'str',
        'id': 'str',
        'default_workspace': 'DocumentsGetDocumentsResponse200DefaultWorkspace',
        'thumbnail': 'DocumentsGetDocumentsResponse200Thumbnail',
        'active': 'bool',
        'tags': 'list[str]',
        'modified_at': 'datetime',
        'created_by': 'DocumentsGetDocumentsResponse200CreatedBy',
        'total_workspaces_updating': 'float',
        'owner': 'DocumentsGetDocumentsResponse200Owner',
        'modified_by': 'DocumentsGetDocumentsResponse200ModifiedBy',
        'starred': 'str',
        'trash': 'bool',
        'public': 'bool',
        'created_at': 'datetime'
    }

    attribute_map = {
        'size_bytes': 'sizeBytes',
        'trashed_at': 'trashedAt',
        'total_workspaces_scheduled_for_update': 'totalWorkspacesScheduledForUpdate',
        'name': 'name',
        'can_unshare': 'canUnshare',
        'permission': 'permission',
        'href': 'href',
        'id': 'id',
        'default_workspace': 'defaultWorkspace',
        'thumbnail': 'thumbnail',
        'active': 'active',
        'tags': 'tags',
        'modified_at': 'modifiedAt',
        'created_by': 'createdBy',
        'total_workspaces_updating': 'totalWorkspacesUpdating',
        'owner': 'owner',
        'modified_by': 'modifiedBy',
        'starred': 'starred',
        'trash': 'trash',
        'public': 'public',
        'created_at': 'createdAt'
    }

    def __init__(self, size_bytes=None, trashed_at=None, total_workspaces_scheduled_for_update=None, name=None, can_unshare=None, permission=None, href=None, id=None, default_workspace=None, thumbnail=None, active=None, tags=None, modified_at=None, created_by=None, total_workspaces_updating=None, owner=None, modified_by=None, starred=None, trash=None, public=None, created_at=None):  # noqa: E501
        """DocumentsGetDocumentsResponse200Items - a model defined in Swagger"""  # noqa: E501

        self._size_bytes = None
        self._trashed_at = None
        self._total_workspaces_scheduled_for_update = None
        self._name = None
        self._can_unshare = None
        self._permission = None
        self._href = None
        self._id = None
        self._default_workspace = None
        self._thumbnail = None
        self._active = None
        self._tags = None
        self._modified_at = None
        self._created_by = None
        self._total_workspaces_updating = None
        self._owner = None
        self._modified_by = None
        self._starred = None
        self._trash = None
        self._public = None
        self._created_at = None
        self.discriminator = None

        if size_bytes is not None:
            self.size_bytes = size_bytes
        if trashed_at is not None:
            self.trashed_at = trashed_at
        if total_workspaces_scheduled_for_update is not None:
            self.total_workspaces_scheduled_for_update = total_workspaces_scheduled_for_update
        if name is not None:
            self.name = name
        if can_unshare is not None:
            self.can_unshare = can_unshare
        if permission is not None:
            self.permission = permission
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if default_workspace is not None:
            self.default_workspace = default_workspace
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if active is not None:
            self.active = active
        if tags is not None:
            self.tags = tags
        if modified_at is not None:
            self.modified_at = modified_at
        if created_by is not None:
            self.created_by = created_by
        if total_workspaces_updating is not None:
            self.total_workspaces_updating = total_workspaces_updating
        if owner is not None:
            self.owner = owner
        if modified_by is not None:
            self.modified_by = modified_by
        if starred is not None:
            self.starred = starred
        if trash is not None:
            self.trash = trash
        if public is not None:
            self.public = public
        if created_at is not None:
            self.created_at = created_at

    @property
    def size_bytes(self):
        """Gets the size_bytes of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Size of document in bytes  # noqa: E501

        :return: The size_bytes of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: float
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this DocumentsGetDocumentsResponse200Items.

        Size of document in bytes  # noqa: E501

        :param size_bytes: The size_bytes of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: float
        """

        self._size_bytes = size_bytes

    @property
    def trashed_at(self):
        """Gets the trashed_at of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        When document has been trashed  # noqa: E501

        :return: The trashed_at of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: datetime
        """
        return self._trashed_at

    @trashed_at.setter
    def trashed_at(self, trashed_at):
        """Sets the trashed_at of this DocumentsGetDocumentsResponse200Items.

        When document has been trashed  # noqa: E501

        :param trashed_at: The trashed_at of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: datetime
        """

        self._trashed_at = trashed_at

    @property
    def total_workspaces_scheduled_for_update(self):
        """Gets the total_workspaces_scheduled_for_update of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Number of workspaces that are scheduled             for updating  # noqa: E501

        :return: The total_workspaces_scheduled_for_update of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: float
        """
        return self._total_workspaces_scheduled_for_update

    @total_workspaces_scheduled_for_update.setter
    def total_workspaces_scheduled_for_update(self, total_workspaces_scheduled_for_update):
        """Sets the total_workspaces_scheduled_for_update of this DocumentsGetDocumentsResponse200Items.

        Number of workspaces that are scheduled             for updating  # noqa: E501

        :param total_workspaces_scheduled_for_update: The total_workspaces_scheduled_for_update of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: float
        """

        self._total_workspaces_scheduled_for_update = total_workspaces_scheduled_for_update

    @property
    def name(self):
        """Gets the name of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Name of document  # noqa: E501

        :return: The name of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentsGetDocumentsResponse200Items.

        Name of document  # noqa: E501

        :param name: The name of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def can_unshare(self):
        """Gets the can_unshare of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Whether document can be unshared  # noqa: E501

        :return: The can_unshare of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: bool
        """
        return self._can_unshare

    @can_unshare.setter
    def can_unshare(self, can_unshare):
        """Sets the can_unshare of this DocumentsGetDocumentsResponse200Items.

        Whether document can be unshared  # noqa: E501

        :param can_unshare: The can_unshare of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: bool
        """

        self._can_unshare = can_unshare

    @property
    def permission(self):
        """Gets the permission of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The permission of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this DocumentsGetDocumentsResponse200Items.

        Onshape internal use  # noqa: E501

        :param permission: The permission of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: str
        """

        self._permission = permission

    @property
    def href(self):
        """Gets the href of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Document URL  # noqa: E501

        :return: The href of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this DocumentsGetDocumentsResponse200Items.

        Document URL  # noqa: E501

        :param href: The href of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Document ID  # noqa: E501

        :return: The id of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsGetDocumentsResponse200Items.

        Document ID  # noqa: E501

        :param id: The id of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def default_workspace(self):
        """Gets the default_workspace of this DocumentsGetDocumentsResponse200Items.  # noqa: E501


        :return: The default_workspace of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: DocumentsGetDocumentsResponse200DefaultWorkspace
        """
        return self._default_workspace

    @default_workspace.setter
    def default_workspace(self, default_workspace):
        """Sets the default_workspace of this DocumentsGetDocumentsResponse200Items.


        :param default_workspace: The default_workspace of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: DocumentsGetDocumentsResponse200DefaultWorkspace
        """

        self._default_workspace = default_workspace

    @property
    def thumbnail(self):
        """Gets the thumbnail of this DocumentsGetDocumentsResponse200Items.  # noqa: E501


        :return: The thumbnail of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: DocumentsGetDocumentsResponse200Thumbnail
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this DocumentsGetDocumentsResponse200Items.


        :param thumbnail: The thumbnail of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: DocumentsGetDocumentsResponse200Thumbnail
        """

        self._thumbnail = thumbnail

    @property
    def active(self):
        """Gets the active of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Whether a shared document is active  # noqa: E501

        :return: The active of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this DocumentsGetDocumentsResponse200Items.

        Whether a shared document is active  # noqa: E501

        :param active: The active of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def tags(self):
        """Gets the tags of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Reserved for future use  # noqa: E501

        :return: The tags of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DocumentsGetDocumentsResponse200Items.

        Reserved for future use  # noqa: E501

        :param tags: The tags of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def modified_at(self):
        """Gets the modified_at of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Date of last modification  # noqa: E501

        :return: The modified_at of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this DocumentsGetDocumentsResponse200Items.

        Date of last modification  # noqa: E501

        :param modified_at: The modified_at of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def created_by(self):
        """Gets the created_by of this DocumentsGetDocumentsResponse200Items.  # noqa: E501


        :return: The created_by of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: DocumentsGetDocumentsResponse200CreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DocumentsGetDocumentsResponse200Items.


        :param created_by: The created_by of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: DocumentsGetDocumentsResponse200CreatedBy
        """

        self._created_by = created_by

    @property
    def total_workspaces_updating(self):
        """Gets the total_workspaces_updating of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Number of workspaces that are updating  # noqa: E501

        :return: The total_workspaces_updating of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: float
        """
        return self._total_workspaces_updating

    @total_workspaces_updating.setter
    def total_workspaces_updating(self, total_workspaces_updating):
        """Sets the total_workspaces_updating of this DocumentsGetDocumentsResponse200Items.

        Number of workspaces that are updating  # noqa: E501

        :param total_workspaces_updating: The total_workspaces_updating of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: float
        """

        self._total_workspaces_updating = total_workspaces_updating

    @property
    def owner(self):
        """Gets the owner of this DocumentsGetDocumentsResponse200Items.  # noqa: E501


        :return: The owner of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: DocumentsGetDocumentsResponse200Owner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DocumentsGetDocumentsResponse200Items.


        :param owner: The owner of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: DocumentsGetDocumentsResponse200Owner
        """

        self._owner = owner

    @property
    def modified_by(self):
        """Gets the modified_by of this DocumentsGetDocumentsResponse200Items.  # noqa: E501


        :return: The modified_by of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: DocumentsGetDocumentsResponse200ModifiedBy
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this DocumentsGetDocumentsResponse200Items.


        :param modified_by: The modified_by of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: DocumentsGetDocumentsResponse200ModifiedBy
        """

        self._modified_by = modified_by

    @property
    def starred(self):
        """Gets the starred of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Whether document has been starred  # noqa: E501

        :return: The starred of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: str
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Sets the starred of this DocumentsGetDocumentsResponse200Items.

        Whether document has been starred  # noqa: E501

        :param starred: The starred of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: str
        """

        self._starred = starred

    @property
    def trash(self):
        """Gets the trash of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Whether document has been trashed  # noqa: E501

        :return: The trash of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: bool
        """
        return self._trash

    @trash.setter
    def trash(self, trash):
        """Sets the trash of this DocumentsGetDocumentsResponse200Items.

        Whether document has been trashed  # noqa: E501

        :param trash: The trash of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: bool
        """

        self._trash = trash

    @property
    def public(self):
        """Gets the public of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Whether document is public  # noqa: E501

        :return: The public of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this DocumentsGetDocumentsResponse200Items.

        Whether document is public  # noqa: E501

        :param public: The public of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def created_at(self):
        """Gets the created_at of this DocumentsGetDocumentsResponse200Items.  # noqa: E501

        Creation date  # noqa: E501

        :return: The created_at of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DocumentsGetDocumentsResponse200Items.

        Creation date  # noqa: E501

        :param created_at: The created_at of this DocumentsGetDocumentsResponse200Items.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, DocumentsGetDocumentsResponse200Items):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
