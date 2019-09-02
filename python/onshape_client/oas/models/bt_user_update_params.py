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


class BTUserUpdateParams(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'default_company_name': 'str',
        'country_code': 'str',
        'old_password': 'str',
        'new_password': 'str',
        'phone_number': 'str',
        'forum_id': 'str',
        'description': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'default_company_name': 'defaultCompanyName',
        'country_code': 'countryCode',
        'old_password': 'oldPassword',
        'new_password': 'newPassword',
        'phone_number': 'phoneNumber',
        'forum_id': 'forumId',
        'description': 'description',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, first_name=None, last_name=None, default_company_name=None, country_code=None, old_password=None, new_password=None, phone_number=None, forum_id=None, description=None, name=None, id=None):  # noqa: E501
        """BTUserUpdateParams - a model defined in OpenAPI"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._default_company_name = None
        self._country_code = None
        self._old_password = None
        self._new_password = None
        self._phone_number = None
        self._forum_id = None
        self._description = None
        self._name = None
        self._id = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if default_company_name is not None:
            self.default_company_name = default_company_name
        if country_code is not None:
            self.country_code = country_code
        if old_password is not None:
            self.old_password = old_password
        if new_password is not None:
            self.new_password = new_password
        if phone_number is not None:
            self.phone_number = phone_number
        if forum_id is not None:
            self.forum_id = forum_id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def first_name(self):
        """Gets the first_name of this BTUserUpdateParams.  # noqa: E501


        :return: The first_name of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this BTUserUpdateParams.


        :param first_name: The first_name of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this BTUserUpdateParams.  # noqa: E501


        :return: The last_name of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this BTUserUpdateParams.


        :param last_name: The last_name of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def default_company_name(self):
        """Gets the default_company_name of this BTUserUpdateParams.  # noqa: E501


        :return: The default_company_name of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._default_company_name

    @default_company_name.setter
    def default_company_name(self, default_company_name):
        """Sets the default_company_name of this BTUserUpdateParams.


        :param default_company_name: The default_company_name of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._default_company_name = default_company_name

    @property
    def country_code(self):
        """Gets the country_code of this BTUserUpdateParams.  # noqa: E501


        :return: The country_code of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this BTUserUpdateParams.


        :param country_code: The country_code of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def old_password(self):
        """Gets the old_password of this BTUserUpdateParams.  # noqa: E501


        :return: The old_password of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this BTUserUpdateParams.


        :param old_password: The old_password of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._old_password = old_password

    @property
    def new_password(self):
        """Gets the new_password of this BTUserUpdateParams.  # noqa: E501


        :return: The new_password of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this BTUserUpdateParams.


        :param new_password: The new_password of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._new_password = new_password

    @property
    def phone_number(self):
        """Gets the phone_number of this BTUserUpdateParams.  # noqa: E501


        :return: The phone_number of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this BTUserUpdateParams.


        :param phone_number: The phone_number of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def forum_id(self):
        """Gets the forum_id of this BTUserUpdateParams.  # noqa: E501


        :return: The forum_id of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._forum_id

    @forum_id.setter
    def forum_id(self, forum_id):
        """Sets the forum_id of this BTUserUpdateParams.


        :param forum_id: The forum_id of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._forum_id = forum_id

    @property
    def description(self):
        """Gets the description of this BTUserUpdateParams.  # noqa: E501


        :return: The description of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTUserUpdateParams.


        :param description: The description of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this BTUserUpdateParams.  # noqa: E501


        :return: The name of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTUserUpdateParams.


        :param name: The name of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTUserUpdateParams.  # noqa: E501


        :return: The id of this BTUserUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTUserUpdateParams.


        :param id: The id of this BTUserUpdateParams.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, BTUserUpdateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
