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

from onshape_client.models.accounts_consume_purchase_response200_card import AccountsConsumePurchaseResponse200Card  # noqa: F401,E501


class AccountsConsumePurchaseResponse200(object):
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
        'plan_name': 'str',
        'canceled_at': 'str',
        'consumed_ids': 'list[str]',
        'group': 'str',
        'user_ids': 'list[str]',
        'plan_id': 'str',
        'amount_cents': 'float',
        'plan_type': 'float',
        'state': 'float',
        'seats': 'float',
        'subscription_end_at': 'str',
        'application_id': 'str',
        'id': 'str',
        'card': 'AccountsConsumePurchaseResponse200Card',
        'account_id': 'str'
    }

    attribute_map = {
        'plan_name': 'planName',
        'canceled_at': 'canceledAt',
        'consumed_ids': 'consumedIds',
        'group': 'group',
        'user_ids': 'userIds',
        'plan_id': 'planId',
        'amount_cents': 'amountCents',
        'plan_type': 'planType',
        'state': 'state',
        'seats': 'seats',
        'subscription_end_at': 'subscriptionEndAt',
        'application_id': 'applicationId',
        'id': 'id',
        'card': 'card',
        'account_id': 'accountId'
    }

    def __init__(self, plan_name=None, canceled_at=None, consumed_ids=None, group=None, user_ids=None, plan_id=None, amount_cents=None, plan_type=None, state=None, seats=None, subscription_end_at=None, application_id=None, id=None, card=None, account_id=None):  # noqa: E501
        """AccountsConsumePurchaseResponse200 - a model defined in Swagger"""  # noqa: E501

        self._plan_name = None
        self._canceled_at = None
        self._consumed_ids = None
        self._group = None
        self._user_ids = None
        self._plan_id = None
        self._amount_cents = None
        self._plan_type = None
        self._state = None
        self._seats = None
        self._subscription_end_at = None
        self._application_id = None
        self._id = None
        self._card = None
        self._account_id = None
        self.discriminator = None

        if plan_name is not None:
            self.plan_name = plan_name
        if canceled_at is not None:
            self.canceled_at = canceled_at
        if consumed_ids is not None:
            self.consumed_ids = consumed_ids
        if group is not None:
            self.group = group
        if user_ids is not None:
            self.user_ids = user_ids
        if plan_id is not None:
            self.plan_id = plan_id
        if amount_cents is not None:
            self.amount_cents = amount_cents
        if plan_type is not None:
            self.plan_type = plan_type
        if state is not None:
            self.state = state
        if seats is not None:
            self.seats = seats
        if subscription_end_at is not None:
            self.subscription_end_at = subscription_end_at
        if application_id is not None:
            self.application_id = application_id
        if id is not None:
            self.id = id
        if card is not None:
            self.card = card
        if account_id is not None:
            self.account_id = account_id

    @property
    def plan_name(self):
        """Gets the plan_name of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Plan name  # noqa: E501

        :return: The plan_name of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this AccountsConsumePurchaseResponse200.

        Plan name  # noqa: E501

        :param plan_name: The plan_name of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: str
        """

        self._plan_name = plan_name

    @property
    def canceled_at(self):
        """Gets the canceled_at of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Purchase canceled at  # noqa: E501

        :return: The canceled_at of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: str
        """
        return self._canceled_at

    @canceled_at.setter
    def canceled_at(self, canceled_at):
        """Sets the canceled_at of this AccountsConsumePurchaseResponse200.

        Purchase canceled at  # noqa: E501

        :param canceled_at: The canceled_at of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: str
        """

        self._canceled_at = canceled_at

    @property
    def consumed_ids(self):
        """Gets the consumed_ids of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Consumed Ids  # noqa: E501

        :return: The consumed_ids of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: list[str]
        """
        return self._consumed_ids

    @consumed_ids.setter
    def consumed_ids(self, consumed_ids):
        """Sets the consumed_ids of this AccountsConsumePurchaseResponse200.

        Consumed Ids  # noqa: E501

        :param consumed_ids: The consumed_ids of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: list[str]
        """

        self._consumed_ids = consumed_ids

    @property
    def group(self):
        """Gets the group of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Group  # noqa: E501

        :return: The group of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AccountsConsumePurchaseResponse200.

        Group  # noqa: E501

        :param group: The group of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def user_ids(self):
        """Gets the user_ids of this AccountsConsumePurchaseResponse200.  # noqa: E501

        User Ids  # noqa: E501

        :return: The user_ids of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this AccountsConsumePurchaseResponse200.

        User Ids  # noqa: E501

        :param user_ids: The user_ids of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: list[str]
        """

        self._user_ids = user_ids

    @property
    def plan_id(self):
        """Gets the plan_id of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Plan id  # noqa: E501

        :return: The plan_id of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this AccountsConsumePurchaseResponse200.

        Plan id  # noqa: E501

        :param plan_id: The plan_id of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def amount_cents(self):
        """Gets the amount_cents of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Amount cents  # noqa: E501

        :return: The amount_cents of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: float
        """
        return self._amount_cents

    @amount_cents.setter
    def amount_cents(self, amount_cents):
        """Sets the amount_cents of this AccountsConsumePurchaseResponse200.

        Amount cents  # noqa: E501

        :param amount_cents: The amount_cents of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: float
        """

        self._amount_cents = amount_cents

    @property
    def plan_type(self):
        """Gets the plan_type of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Plan type (0-RECURRING, 1-CONSUMABLE, 2-ONE_TIME)  # noqa: E501

        :return: The plan_type of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: float
        """
        return self._plan_type

    @plan_type.setter
    def plan_type(self, plan_type):
        """Sets the plan_type of this AccountsConsumePurchaseResponse200.

        Plan type (0-RECURRING, 1-CONSUMABLE, 2-ONE_TIME)  # noqa: E501

        :param plan_type: The plan_type of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: float
        """

        self._plan_type = plan_type

    @property
    def state(self):
        """Gets the state of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Purchase state (1-DELETED, 2-CANCELED, 3-UNPAID, 4-PAST_DUE, 5-TRIALING,             6-ACTIVE, 7-CONSUMED)  # noqa: E501

        :return: The state of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: float
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AccountsConsumePurchaseResponse200.

        Purchase state (1-DELETED, 2-CANCELED, 3-UNPAID, 4-PAST_DUE, 5-TRIALING,             6-ACTIVE, 7-CONSUMED)  # noqa: E501

        :param state: The state of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: float
        """

        self._state = state

    @property
    def seats(self):
        """Gets the seats of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Number of seats  # noqa: E501

        :return: The seats of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: float
        """
        return self._seats

    @seats.setter
    def seats(self, seats):
        """Sets the seats of this AccountsConsumePurchaseResponse200.

        Number of seats  # noqa: E501

        :param seats: The seats of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: float
        """

        self._seats = seats

    @property
    def subscription_end_at(self):
        """Gets the subscription_end_at of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Subscription end at  # noqa: E501

        :return: The subscription_end_at of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: str
        """
        return self._subscription_end_at

    @subscription_end_at.setter
    def subscription_end_at(self, subscription_end_at):
        """Sets the subscription_end_at of this AccountsConsumePurchaseResponse200.

        Subscription end at  # noqa: E501

        :param subscription_end_at: The subscription_end_at of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: str
        """

        self._subscription_end_at = subscription_end_at

    @property
    def application_id(self):
        """Gets the application_id of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Application Id  # noqa: E501

        :return: The application_id of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this AccountsConsumePurchaseResponse200.

        Application Id  # noqa: E501

        :param application_id: The application_id of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def id(self):
        """Gets the id of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Purchase Id  # noqa: E501

        :return: The id of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountsConsumePurchaseResponse200.

        Purchase Id  # noqa: E501

        :param id: The id of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def card(self):
        """Gets the card of this AccountsConsumePurchaseResponse200.  # noqa: E501


        :return: The card of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: AccountsConsumePurchaseResponse200Card
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this AccountsConsumePurchaseResponse200.


        :param card: The card of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: AccountsConsumePurchaseResponse200Card
        """

        self._card = card

    @property
    def account_id(self):
        """Gets the account_id of this AccountsConsumePurchaseResponse200.  # noqa: E501

        Account id  # noqa: E501

        :return: The account_id of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountsConsumePurchaseResponse200.

        Account id  # noqa: E501

        :param account_id: The account_id of this AccountsConsumePurchaseResponse200.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

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
        if not isinstance(other, AccountsConsumePurchaseResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
