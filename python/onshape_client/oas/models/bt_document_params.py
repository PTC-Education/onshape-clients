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


class BTDocumentParams(object):
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
        'owner_id': 'str',
        'project_id': 'str',
        'parent_id': 'str',
        'is_public': 'bool',
        'beta_capability_ids': 'list[str]',
        'is_empty_content': 'bool',
        'generate_unknown_messages': 'bool',
        'not_revision_managed': 'bool',
        'owner_email': 'str',
        'owner_type': 'int',
        'description': 'str',
        'tags': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'owner_id': 'ownerId',
        'project_id': 'projectId',
        'parent_id': 'parentId',
        'is_public': 'isPublic',
        'beta_capability_ids': 'betaCapabilityIds',
        'is_empty_content': 'isEmptyContent',
        'generate_unknown_messages': 'generateUnknownMessages',
        'not_revision_managed': 'notRevisionManaged',
        'owner_email': 'ownerEmail',
        'owner_type': 'ownerType',
        'description': 'description',
        'tags': 'tags',
        'name': 'name'
    }

    def __init__(self, owner_id=None, project_id=None, parent_id=None, is_public=None, beta_capability_ids=None, is_empty_content=None, generate_unknown_messages=None, not_revision_managed=None, owner_email=None, owner_type=None, description=None, tags=None, name=None):  # noqa: E501
        """BTDocumentParams - a model defined in OpenAPI"""  # noqa: E501

        self._owner_id = None
        self._project_id = None
        self._parent_id = None
        self._is_public = None
        self._beta_capability_ids = None
        self._is_empty_content = None
        self._generate_unknown_messages = None
        self._not_revision_managed = None
        self._owner_email = None
        self._owner_type = None
        self._description = None
        self._tags = None
        self._name = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id
        if project_id is not None:
            self.project_id = project_id
        if parent_id is not None:
            self.parent_id = parent_id
        if is_public is not None:
            self.is_public = is_public
        if beta_capability_ids is not None:
            self.beta_capability_ids = beta_capability_ids
        if is_empty_content is not None:
            self.is_empty_content = is_empty_content
        if generate_unknown_messages is not None:
            self.generate_unknown_messages = generate_unknown_messages
        if not_revision_managed is not None:
            self.not_revision_managed = not_revision_managed
        if owner_email is not None:
            self.owner_email = owner_email
        if owner_type is not None:
            self.owner_type = owner_type
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if name is not None:
            self.name = name

    @property
    def owner_id(self):
        """Gets the owner_id of this BTDocumentParams.  # noqa: E501


        :return: The owner_id of this BTDocumentParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this BTDocumentParams.


        :param owner_id: The owner_id of this BTDocumentParams.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def project_id(self):
        """Gets the project_id of this BTDocumentParams.  # noqa: E501


        :return: The project_id of this BTDocumentParams.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BTDocumentParams.


        :param project_id: The project_id of this BTDocumentParams.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BTDocumentParams.  # noqa: E501


        :return: The parent_id of this BTDocumentParams.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BTDocumentParams.


        :param parent_id: The parent_id of this BTDocumentParams.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def is_public(self):
        """Gets the is_public of this BTDocumentParams.  # noqa: E501


        :return: The is_public of this BTDocumentParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this BTDocumentParams.


        :param is_public: The is_public of this BTDocumentParams.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def beta_capability_ids(self):
        """Gets the beta_capability_ids of this BTDocumentParams.  # noqa: E501


        :return: The beta_capability_ids of this BTDocumentParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._beta_capability_ids

    @beta_capability_ids.setter
    def beta_capability_ids(self, beta_capability_ids):
        """Sets the beta_capability_ids of this BTDocumentParams.


        :param beta_capability_ids: The beta_capability_ids of this BTDocumentParams.  # noqa: E501
        :type: list[str]
        """

        self._beta_capability_ids = beta_capability_ids

    @property
    def is_empty_content(self):
        """Gets the is_empty_content of this BTDocumentParams.  # noqa: E501


        :return: The is_empty_content of this BTDocumentParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_empty_content

    @is_empty_content.setter
    def is_empty_content(self, is_empty_content):
        """Sets the is_empty_content of this BTDocumentParams.


        :param is_empty_content: The is_empty_content of this BTDocumentParams.  # noqa: E501
        :type: bool
        """

        self._is_empty_content = is_empty_content

    @property
    def generate_unknown_messages(self):
        """Gets the generate_unknown_messages of this BTDocumentParams.  # noqa: E501


        :return: The generate_unknown_messages of this BTDocumentParams.  # noqa: E501
        :rtype: bool
        """
        return self._generate_unknown_messages

    @generate_unknown_messages.setter
    def generate_unknown_messages(self, generate_unknown_messages):
        """Sets the generate_unknown_messages of this BTDocumentParams.


        :param generate_unknown_messages: The generate_unknown_messages of this BTDocumentParams.  # noqa: E501
        :type: bool
        """

        self._generate_unknown_messages = generate_unknown_messages

    @property
    def not_revision_managed(self):
        """Gets the not_revision_managed of this BTDocumentParams.  # noqa: E501


        :return: The not_revision_managed of this BTDocumentParams.  # noqa: E501
        :rtype: bool
        """
        return self._not_revision_managed

    @not_revision_managed.setter
    def not_revision_managed(self, not_revision_managed):
        """Sets the not_revision_managed of this BTDocumentParams.


        :param not_revision_managed: The not_revision_managed of this BTDocumentParams.  # noqa: E501
        :type: bool
        """

        self._not_revision_managed = not_revision_managed

    @property
    def owner_email(self):
        """Gets the owner_email of this BTDocumentParams.  # noqa: E501


        :return: The owner_email of this BTDocumentParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_email

    @owner_email.setter
    def owner_email(self, owner_email):
        """Sets the owner_email of this BTDocumentParams.


        :param owner_email: The owner_email of this BTDocumentParams.  # noqa: E501
        :type: str
        """

        self._owner_email = owner_email

    @property
    def owner_type(self):
        """Gets the owner_type of this BTDocumentParams.  # noqa: E501


        :return: The owner_type of this BTDocumentParams.  # noqa: E501
        :rtype: int
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this BTDocumentParams.


        :param owner_type: The owner_type of this BTDocumentParams.  # noqa: E501
        :type: int
        """

        self._owner_type = owner_type

    @property
    def description(self):
        """Gets the description of this BTDocumentParams.  # noqa: E501


        :return: The description of this BTDocumentParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTDocumentParams.


        :param description: The description of this BTDocumentParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this BTDocumentParams.  # noqa: E501


        :return: The tags of this BTDocumentParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BTDocumentParams.


        :param tags: The tags of this BTDocumentParams.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def name(self):
        """Gets the name of this BTDocumentParams.  # noqa: E501


        :return: The name of this BTDocumentParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTDocumentParams.


        :param name: The name of this BTDocumentParams.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, BTDocumentParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
