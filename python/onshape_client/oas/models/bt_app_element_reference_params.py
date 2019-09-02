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


class BTAppElementReferenceParams(object):
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
        'part_number': 'str',
        'transaction_id': 'str',
        'parent_change_id': 'str',
        'sketch_ids': 'list[str]',
        'target_version_id': 'str',
        'pure_sketch': 'bool',
        'is_sketch_only': 'bool',
        'return_error': 'bool',
        'has_document_microversions': 'bool',
        'target_microversion_id': 'str',
        'id_tag_microversion_id': 'str',
        'id_tag': 'str',
        'track_new_versions': 'bool',
        'revision': 'str',
        'target_document_id': 'str',
        'target_element_id': 'str',
        'target_configuration': 'str',
        'update_sketch_info': 'bool'
    }

    attribute_map = {
        'part_number': 'partNumber',
        'transaction_id': 'transactionId',
        'parent_change_id': 'parentChangeId',
        'sketch_ids': 'sketchIds',
        'target_version_id': 'targetVersionId',
        'pure_sketch': 'pureSketch',
        'is_sketch_only': 'isSketchOnly',
        'return_error': 'returnError',
        'has_document_microversions': 'hasDocumentMicroversions',
        'target_microversion_id': 'targetMicroversionId',
        'id_tag_microversion_id': 'idTagMicroversionId',
        'id_tag': 'idTag',
        'track_new_versions': 'trackNewVersions',
        'revision': 'revision',
        'target_document_id': 'targetDocumentId',
        'target_element_id': 'targetElementId',
        'target_configuration': 'targetConfiguration',
        'update_sketch_info': 'updateSketchInfo'
    }

    def __init__(self, part_number=None, transaction_id=None, parent_change_id=None, sketch_ids=None, target_version_id=None, pure_sketch=None, is_sketch_only=None, return_error=None, has_document_microversions=None, target_microversion_id=None, id_tag_microversion_id=None, id_tag=None, track_new_versions=None, revision=None, target_document_id=None, target_element_id=None, target_configuration=None, update_sketch_info=None):  # noqa: E501
        """BTAppElementReferenceParams - a model defined in OpenAPI"""  # noqa: E501

        self._part_number = None
        self._transaction_id = None
        self._parent_change_id = None
        self._sketch_ids = None
        self._target_version_id = None
        self._pure_sketch = None
        self._is_sketch_only = None
        self._return_error = None
        self._has_document_microversions = None
        self._target_microversion_id = None
        self._id_tag_microversion_id = None
        self._id_tag = None
        self._track_new_versions = None
        self._revision = None
        self._target_document_id = None
        self._target_element_id = None
        self._target_configuration = None
        self._update_sketch_info = None
        self.discriminator = None

        if part_number is not None:
            self.part_number = part_number
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if parent_change_id is not None:
            self.parent_change_id = parent_change_id
        if sketch_ids is not None:
            self.sketch_ids = sketch_ids
        if target_version_id is not None:
            self.target_version_id = target_version_id
        if pure_sketch is not None:
            self.pure_sketch = pure_sketch
        if is_sketch_only is not None:
            self.is_sketch_only = is_sketch_only
        if return_error is not None:
            self.return_error = return_error
        if has_document_microversions is not None:
            self.has_document_microversions = has_document_microversions
        if target_microversion_id is not None:
            self.target_microversion_id = target_microversion_id
        if id_tag_microversion_id is not None:
            self.id_tag_microversion_id = id_tag_microversion_id
        if id_tag is not None:
            self.id_tag = id_tag
        if track_new_versions is not None:
            self.track_new_versions = track_new_versions
        if revision is not None:
            self.revision = revision
        if target_document_id is not None:
            self.target_document_id = target_document_id
        if target_element_id is not None:
            self.target_element_id = target_element_id
        if target_configuration is not None:
            self.target_configuration = target_configuration
        if update_sketch_info is not None:
            self.update_sketch_info = update_sketch_info

    @property
    def part_number(self):
        """Gets the part_number of this BTAppElementReferenceParams.  # noqa: E501


        :return: The part_number of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this BTAppElementReferenceParams.


        :param part_number: The part_number of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def transaction_id(self):
        """Gets the transaction_id of this BTAppElementReferenceParams.  # noqa: E501


        :return: The transaction_id of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this BTAppElementReferenceParams.


        :param transaction_id: The transaction_id of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def parent_change_id(self):
        """Gets the parent_change_id of this BTAppElementReferenceParams.  # noqa: E501


        :return: The parent_change_id of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._parent_change_id

    @parent_change_id.setter
    def parent_change_id(self, parent_change_id):
        """Sets the parent_change_id of this BTAppElementReferenceParams.


        :param parent_change_id: The parent_change_id of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._parent_change_id = parent_change_id

    @property
    def sketch_ids(self):
        """Gets the sketch_ids of this BTAppElementReferenceParams.  # noqa: E501


        :return: The sketch_ids of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._sketch_ids

    @sketch_ids.setter
    def sketch_ids(self, sketch_ids):
        """Sets the sketch_ids of this BTAppElementReferenceParams.


        :param sketch_ids: The sketch_ids of this BTAppElementReferenceParams.  # noqa: E501
        :type: list[str]
        """

        self._sketch_ids = sketch_ids

    @property
    def target_version_id(self):
        """Gets the target_version_id of this BTAppElementReferenceParams.  # noqa: E501


        :return: The target_version_id of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._target_version_id

    @target_version_id.setter
    def target_version_id(self, target_version_id):
        """Sets the target_version_id of this BTAppElementReferenceParams.


        :param target_version_id: The target_version_id of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._target_version_id = target_version_id

    @property
    def pure_sketch(self):
        """Gets the pure_sketch of this BTAppElementReferenceParams.  # noqa: E501


        :return: The pure_sketch of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: bool
        """
        return self._pure_sketch

    @pure_sketch.setter
    def pure_sketch(self, pure_sketch):
        """Sets the pure_sketch of this BTAppElementReferenceParams.


        :param pure_sketch: The pure_sketch of this BTAppElementReferenceParams.  # noqa: E501
        :type: bool
        """

        self._pure_sketch = pure_sketch

    @property
    def is_sketch_only(self):
        """Gets the is_sketch_only of this BTAppElementReferenceParams.  # noqa: E501


        :return: The is_sketch_only of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_sketch_only

    @is_sketch_only.setter
    def is_sketch_only(self, is_sketch_only):
        """Sets the is_sketch_only of this BTAppElementReferenceParams.


        :param is_sketch_only: The is_sketch_only of this BTAppElementReferenceParams.  # noqa: E501
        :type: bool
        """

        self._is_sketch_only = is_sketch_only

    @property
    def return_error(self):
        """Gets the return_error of this BTAppElementReferenceParams.  # noqa: E501


        :return: The return_error of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: bool
        """
        return self._return_error

    @return_error.setter
    def return_error(self, return_error):
        """Sets the return_error of this BTAppElementReferenceParams.


        :param return_error: The return_error of this BTAppElementReferenceParams.  # noqa: E501
        :type: bool
        """

        self._return_error = return_error

    @property
    def has_document_microversions(self):
        """Gets the has_document_microversions of this BTAppElementReferenceParams.  # noqa: E501


        :return: The has_document_microversions of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: bool
        """
        return self._has_document_microversions

    @has_document_microversions.setter
    def has_document_microversions(self, has_document_microversions):
        """Sets the has_document_microversions of this BTAppElementReferenceParams.


        :param has_document_microversions: The has_document_microversions of this BTAppElementReferenceParams.  # noqa: E501
        :type: bool
        """

        self._has_document_microversions = has_document_microversions

    @property
    def target_microversion_id(self):
        """Gets the target_microversion_id of this BTAppElementReferenceParams.  # noqa: E501


        :return: The target_microversion_id of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._target_microversion_id

    @target_microversion_id.setter
    def target_microversion_id(self, target_microversion_id):
        """Sets the target_microversion_id of this BTAppElementReferenceParams.


        :param target_microversion_id: The target_microversion_id of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._target_microversion_id = target_microversion_id

    @property
    def id_tag_microversion_id(self):
        """Gets the id_tag_microversion_id of this BTAppElementReferenceParams.  # noqa: E501


        :return: The id_tag_microversion_id of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._id_tag_microversion_id

    @id_tag_microversion_id.setter
    def id_tag_microversion_id(self, id_tag_microversion_id):
        """Sets the id_tag_microversion_id of this BTAppElementReferenceParams.


        :param id_tag_microversion_id: The id_tag_microversion_id of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._id_tag_microversion_id = id_tag_microversion_id

    @property
    def id_tag(self):
        """Gets the id_tag of this BTAppElementReferenceParams.  # noqa: E501


        :return: The id_tag of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._id_tag

    @id_tag.setter
    def id_tag(self, id_tag):
        """Sets the id_tag of this BTAppElementReferenceParams.


        :param id_tag: The id_tag of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._id_tag = id_tag

    @property
    def track_new_versions(self):
        """Gets the track_new_versions of this BTAppElementReferenceParams.  # noqa: E501


        :return: The track_new_versions of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: bool
        """
        return self._track_new_versions

    @track_new_versions.setter
    def track_new_versions(self, track_new_versions):
        """Sets the track_new_versions of this BTAppElementReferenceParams.


        :param track_new_versions: The track_new_versions of this BTAppElementReferenceParams.  # noqa: E501
        :type: bool
        """

        self._track_new_versions = track_new_versions

    @property
    def revision(self):
        """Gets the revision of this BTAppElementReferenceParams.  # noqa: E501


        :return: The revision of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this BTAppElementReferenceParams.


        :param revision: The revision of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def target_document_id(self):
        """Gets the target_document_id of this BTAppElementReferenceParams.  # noqa: E501


        :return: The target_document_id of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._target_document_id

    @target_document_id.setter
    def target_document_id(self, target_document_id):
        """Sets the target_document_id of this BTAppElementReferenceParams.


        :param target_document_id: The target_document_id of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._target_document_id = target_document_id

    @property
    def target_element_id(self):
        """Gets the target_element_id of this BTAppElementReferenceParams.  # noqa: E501


        :return: The target_element_id of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._target_element_id

    @target_element_id.setter
    def target_element_id(self, target_element_id):
        """Sets the target_element_id of this BTAppElementReferenceParams.


        :param target_element_id: The target_element_id of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._target_element_id = target_element_id

    @property
    def target_configuration(self):
        """Gets the target_configuration of this BTAppElementReferenceParams.  # noqa: E501


        :return: The target_configuration of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: str
        """
        return self._target_configuration

    @target_configuration.setter
    def target_configuration(self, target_configuration):
        """Sets the target_configuration of this BTAppElementReferenceParams.


        :param target_configuration: The target_configuration of this BTAppElementReferenceParams.  # noqa: E501
        :type: str
        """

        self._target_configuration = target_configuration

    @property
    def update_sketch_info(self):
        """Gets the update_sketch_info of this BTAppElementReferenceParams.  # noqa: E501


        :return: The update_sketch_info of this BTAppElementReferenceParams.  # noqa: E501
        :rtype: bool
        """
        return self._update_sketch_info

    @update_sketch_info.setter
    def update_sketch_info(self, update_sketch_info):
        """Sets the update_sketch_info of this BTAppElementReferenceParams.


        :param update_sketch_info: The update_sketch_info of this BTAppElementReferenceParams.  # noqa: E501
        :type: bool
        """

        self._update_sketch_info = update_sketch_info

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
        if not isinstance(other, BTAppElementReferenceParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
