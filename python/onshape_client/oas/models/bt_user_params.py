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


class BTUserParams(object):
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
        'email': 'str',
        'default_company_name': 'str',
        'plan_id': 'str',
        'seats': 'int',
        'recaptcha': 'str',
        'invite_friend_request': 'bool',
        'approve_user': 'bool',
        'cad_system_at_signup': 'str',
        'eula_accepted': 'bool',
        'country_code': 'str',
        'company_plan': 'bool',
        'phone_number': 'str',
        'forum_id': 'str',
        'role': 'int',
        'upgrade_to_education_plan': 'bool',
        'source': 'int',
        'password': 'str',
        'token': 'str',
        'description': 'str',
        'name': 'str',
        'message': 'str',
        'id': 'str',
        'state': 'int'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'default_company_name': 'defaultCompanyName',
        'plan_id': 'planId',
        'seats': 'seats',
        'recaptcha': 'recaptcha',
        'invite_friend_request': 'inviteFriendRequest',
        'approve_user': 'approveUser',
        'cad_system_at_signup': 'cadSystemAtSignup',
        'eula_accepted': 'eulaAccepted',
        'country_code': 'countryCode',
        'company_plan': 'companyPlan',
        'phone_number': 'phoneNumber',
        'forum_id': 'forumId',
        'role': 'role',
        'upgrade_to_education_plan': 'upgradeToEducationPlan',
        'source': 'source',
        'password': 'password',
        'token': 'token',
        'description': 'description',
        'name': 'name',
        'message': 'message',
        'id': 'id',
        'state': 'state'
    }

    def __init__(self, first_name=None, last_name=None, email=None, default_company_name=None, plan_id=None, seats=None, recaptcha=None, invite_friend_request=None, approve_user=None, cad_system_at_signup=None, eula_accepted=None, country_code=None, company_plan=None, phone_number=None, forum_id=None, role=None, upgrade_to_education_plan=None, source=None, password=None, token=None, description=None, name=None, message=None, id=None, state=None):  # noqa: E501
        """BTUserParams - a model defined in OpenAPI"""  # noqa: E501

        self._first_name = None
        self._last_name = None
        self._email = None
        self._default_company_name = None
        self._plan_id = None
        self._seats = None
        self._recaptcha = None
        self._invite_friend_request = None
        self._approve_user = None
        self._cad_system_at_signup = None
        self._eula_accepted = None
        self._country_code = None
        self._company_plan = None
        self._phone_number = None
        self._forum_id = None
        self._role = None
        self._upgrade_to_education_plan = None
        self._source = None
        self._password = None
        self._token = None
        self._description = None
        self._name = None
        self._message = None
        self._id = None
        self._state = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if default_company_name is not None:
            self.default_company_name = default_company_name
        if plan_id is not None:
            self.plan_id = plan_id
        if seats is not None:
            self.seats = seats
        if recaptcha is not None:
            self.recaptcha = recaptcha
        if invite_friend_request is not None:
            self.invite_friend_request = invite_friend_request
        if approve_user is not None:
            self.approve_user = approve_user
        if cad_system_at_signup is not None:
            self.cad_system_at_signup = cad_system_at_signup
        if eula_accepted is not None:
            self.eula_accepted = eula_accepted
        if country_code is not None:
            self.country_code = country_code
        if company_plan is not None:
            self.company_plan = company_plan
        if phone_number is not None:
            self.phone_number = phone_number
        if forum_id is not None:
            self.forum_id = forum_id
        if role is not None:
            self.role = role
        if upgrade_to_education_plan is not None:
            self.upgrade_to_education_plan = upgrade_to_education_plan
        if source is not None:
            self.source = source
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if message is not None:
            self.message = message
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state

    @property
    def first_name(self):
        """Gets the first_name of this BTUserParams.  # noqa: E501


        :return: The first_name of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this BTUserParams.


        :param first_name: The first_name of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this BTUserParams.  # noqa: E501


        :return: The last_name of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this BTUserParams.


        :param last_name: The last_name of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this BTUserParams.  # noqa: E501


        :return: The email of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTUserParams.


        :param email: The email of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def default_company_name(self):
        """Gets the default_company_name of this BTUserParams.  # noqa: E501


        :return: The default_company_name of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._default_company_name

    @default_company_name.setter
    def default_company_name(self, default_company_name):
        """Sets the default_company_name of this BTUserParams.


        :param default_company_name: The default_company_name of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._default_company_name = default_company_name

    @property
    def plan_id(self):
        """Gets the plan_id of this BTUserParams.  # noqa: E501


        :return: The plan_id of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this BTUserParams.


        :param plan_id: The plan_id of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def seats(self):
        """Gets the seats of this BTUserParams.  # noqa: E501


        :return: The seats of this BTUserParams.  # noqa: E501
        :rtype: int
        """
        return self._seats

    @seats.setter
    def seats(self, seats):
        """Sets the seats of this BTUserParams.


        :param seats: The seats of this BTUserParams.  # noqa: E501
        :type: int
        """

        self._seats = seats

    @property
    def recaptcha(self):
        """Gets the recaptcha of this BTUserParams.  # noqa: E501


        :return: The recaptcha of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._recaptcha

    @recaptcha.setter
    def recaptcha(self, recaptcha):
        """Sets the recaptcha of this BTUserParams.


        :param recaptcha: The recaptcha of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._recaptcha = recaptcha

    @property
    def invite_friend_request(self):
        """Gets the invite_friend_request of this BTUserParams.  # noqa: E501


        :return: The invite_friend_request of this BTUserParams.  # noqa: E501
        :rtype: bool
        """
        return self._invite_friend_request

    @invite_friend_request.setter
    def invite_friend_request(self, invite_friend_request):
        """Sets the invite_friend_request of this BTUserParams.


        :param invite_friend_request: The invite_friend_request of this BTUserParams.  # noqa: E501
        :type: bool
        """

        self._invite_friend_request = invite_friend_request

    @property
    def approve_user(self):
        """Gets the approve_user of this BTUserParams.  # noqa: E501


        :return: The approve_user of this BTUserParams.  # noqa: E501
        :rtype: bool
        """
        return self._approve_user

    @approve_user.setter
    def approve_user(self, approve_user):
        """Sets the approve_user of this BTUserParams.


        :param approve_user: The approve_user of this BTUserParams.  # noqa: E501
        :type: bool
        """

        self._approve_user = approve_user

    @property
    def cad_system_at_signup(self):
        """Gets the cad_system_at_signup of this BTUserParams.  # noqa: E501


        :return: The cad_system_at_signup of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._cad_system_at_signup

    @cad_system_at_signup.setter
    def cad_system_at_signup(self, cad_system_at_signup):
        """Sets the cad_system_at_signup of this BTUserParams.


        :param cad_system_at_signup: The cad_system_at_signup of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._cad_system_at_signup = cad_system_at_signup

    @property
    def eula_accepted(self):
        """Gets the eula_accepted of this BTUserParams.  # noqa: E501


        :return: The eula_accepted of this BTUserParams.  # noqa: E501
        :rtype: bool
        """
        return self._eula_accepted

    @eula_accepted.setter
    def eula_accepted(self, eula_accepted):
        """Sets the eula_accepted of this BTUserParams.


        :param eula_accepted: The eula_accepted of this BTUserParams.  # noqa: E501
        :type: bool
        """

        self._eula_accepted = eula_accepted

    @property
    def country_code(self):
        """Gets the country_code of this BTUserParams.  # noqa: E501


        :return: The country_code of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this BTUserParams.


        :param country_code: The country_code of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def company_plan(self):
        """Gets the company_plan of this BTUserParams.  # noqa: E501


        :return: The company_plan of this BTUserParams.  # noqa: E501
        :rtype: bool
        """
        return self._company_plan

    @company_plan.setter
    def company_plan(self, company_plan):
        """Sets the company_plan of this BTUserParams.


        :param company_plan: The company_plan of this BTUserParams.  # noqa: E501
        :type: bool
        """

        self._company_plan = company_plan

    @property
    def phone_number(self):
        """Gets the phone_number of this BTUserParams.  # noqa: E501


        :return: The phone_number of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this BTUserParams.


        :param phone_number: The phone_number of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def forum_id(self):
        """Gets the forum_id of this BTUserParams.  # noqa: E501


        :return: The forum_id of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._forum_id

    @forum_id.setter
    def forum_id(self, forum_id):
        """Sets the forum_id of this BTUserParams.


        :param forum_id: The forum_id of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._forum_id = forum_id

    @property
    def role(self):
        """Gets the role of this BTUserParams.  # noqa: E501


        :return: The role of this BTUserParams.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this BTUserParams.


        :param role: The role of this BTUserParams.  # noqa: E501
        :type: int
        """

        self._role = role

    @property
    def upgrade_to_education_plan(self):
        """Gets the upgrade_to_education_plan of this BTUserParams.  # noqa: E501


        :return: The upgrade_to_education_plan of this BTUserParams.  # noqa: E501
        :rtype: bool
        """
        return self._upgrade_to_education_plan

    @upgrade_to_education_plan.setter
    def upgrade_to_education_plan(self, upgrade_to_education_plan):
        """Sets the upgrade_to_education_plan of this BTUserParams.


        :param upgrade_to_education_plan: The upgrade_to_education_plan of this BTUserParams.  # noqa: E501
        :type: bool
        """

        self._upgrade_to_education_plan = upgrade_to_education_plan

    @property
    def source(self):
        """Gets the source of this BTUserParams.  # noqa: E501


        :return: The source of this BTUserParams.  # noqa: E501
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BTUserParams.


        :param source: The source of this BTUserParams.  # noqa: E501
        :type: int
        """

        self._source = source

    @property
    def password(self):
        """Gets the password of this BTUserParams.  # noqa: E501


        :return: The password of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this BTUserParams.


        :param password: The password of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def token(self):
        """Gets the token of this BTUserParams.  # noqa: E501


        :return: The token of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this BTUserParams.


        :param token: The token of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def description(self):
        """Gets the description of this BTUserParams.  # noqa: E501


        :return: The description of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTUserParams.


        :param description: The description of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this BTUserParams.  # noqa: E501


        :return: The name of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTUserParams.


        :param name: The name of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def message(self):
        """Gets the message of this BTUserParams.  # noqa: E501


        :return: The message of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BTUserParams.


        :param message: The message of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def id(self):
        """Gets the id of this BTUserParams.  # noqa: E501


        :return: The id of this BTUserParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTUserParams.


        :param id: The id of this BTUserParams.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this BTUserParams.  # noqa: E501


        :return: The state of this BTUserParams.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTUserParams.


        :param state: The state of this BTUserParams.  # noqa: E501
        :type: int
        """

        self._state = state

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
        if not isinstance(other, BTUserParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
