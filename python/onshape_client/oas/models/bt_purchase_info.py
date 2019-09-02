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


class BTPurchaseInfo(object):
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
        'group': 'str',
        'application': 'BTAPIApplicationSummaryInfo',
        'account_id': 'str',
        'plan_id': 'str',
        'plan': 'BTBillingPlanInfo',
        'seats': 'int',
        'subscription_begin_at': 'datetime',
        'subscription_end_at': 'datetime',
        'subscription_id': 'str',
        'client_id': 'str',
        'payment_type': 'int',
        'amount_cents': 'int',
        'next_charge': 'NextCharge',
        'plan_type': 'int',
        'card': 'BTCardInfo',
        'light_seats': 'int',
        'canceled_at': 'datetime',
        'subscribers': 'list[BTPlanSubscriberInfo]',
        'plan_name': 'str',
        'actual_amount_paid_cents': 'int',
        'trial_end': 'datetime',
        'coupon_percent_off': 'int',
        'reseller_name': 'str',
        'duration': 'int',
        'subscription_fields': 'Subscription',
        'purchase_date': 'datetime',
        'pending_cancelation': 'bool',
        'prorated_charges': 'list[ProratedCharges]',
        'prorated_total': 'int',
        'coupon_amount_off': 'int',
        'duration_months': 'int',
        'last_modified': 'datetime',
        'currency': 'str',
        'state': 'int',
        'href': 'str',
        'view_ref': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'group': 'group',
        'application': 'application',
        'account_id': 'accountId',
        'plan_id': 'planId',
        'plan': 'plan',
        'seats': 'seats',
        'subscription_begin_at': 'subscriptionBeginAt',
        'subscription_end_at': 'subscriptionEndAt',
        'subscription_id': 'subscriptionId',
        'client_id': 'clientId',
        'payment_type': 'paymentType',
        'amount_cents': 'amountCents',
        'next_charge': 'nextCharge',
        'plan_type': 'planType',
        'card': 'card',
        'light_seats': 'lightSeats',
        'canceled_at': 'canceledAt',
        'subscribers': 'subscribers',
        'plan_name': 'planName',
        'actual_amount_paid_cents': 'actualAmountPaidCents',
        'trial_end': 'trialEnd',
        'coupon_percent_off': 'couponPercentOff',
        'reseller_name': 'resellerName',
        'duration': 'duration',
        'subscription_fields': 'subscriptionFields',
        'purchase_date': 'purchaseDate',
        'pending_cancelation': 'pendingCancelation',
        'prorated_charges': 'proratedCharges',
        'prorated_total': 'proratedTotal',
        'coupon_amount_off': 'couponAmountOff',
        'duration_months': 'durationMonths',
        'last_modified': 'lastModified',
        'currency': 'currency',
        'state': 'state',
        'href': 'href',
        'view_ref': 'viewRef',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, group=None, application=None, account_id=None, plan_id=None, plan=None, seats=None, subscription_begin_at=None, subscription_end_at=None, subscription_id=None, client_id=None, payment_type=None, amount_cents=None, next_charge=None, plan_type=None, card=None, light_seats=None, canceled_at=None, subscribers=None, plan_name=None, actual_amount_paid_cents=None, trial_end=None, coupon_percent_off=None, reseller_name=None, duration=None, subscription_fields=None, purchase_date=None, pending_cancelation=None, prorated_charges=None, prorated_total=None, coupon_amount_off=None, duration_months=None, last_modified=None, currency=None, state=None, href=None, view_ref=None, id=None, name=None):  # noqa: E501
        """BTPurchaseInfo - a model defined in OpenAPI"""  # noqa: E501

        self._group = None
        self._application = None
        self._account_id = None
        self._plan_id = None
        self._plan = None
        self._seats = None
        self._subscription_begin_at = None
        self._subscription_end_at = None
        self._subscription_id = None
        self._client_id = None
        self._payment_type = None
        self._amount_cents = None
        self._next_charge = None
        self._plan_type = None
        self._card = None
        self._light_seats = None
        self._canceled_at = None
        self._subscribers = None
        self._plan_name = None
        self._actual_amount_paid_cents = None
        self._trial_end = None
        self._coupon_percent_off = None
        self._reseller_name = None
        self._duration = None
        self._subscription_fields = None
        self._purchase_date = None
        self._pending_cancelation = None
        self._prorated_charges = None
        self._prorated_total = None
        self._coupon_amount_off = None
        self._duration_months = None
        self._last_modified = None
        self._currency = None
        self._state = None
        self._href = None
        self._view_ref = None
        self._id = None
        self._name = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if application is not None:
            self.application = application
        if account_id is not None:
            self.account_id = account_id
        if plan_id is not None:
            self.plan_id = plan_id
        if plan is not None:
            self.plan = plan
        if seats is not None:
            self.seats = seats
        if subscription_begin_at is not None:
            self.subscription_begin_at = subscription_begin_at
        if subscription_end_at is not None:
            self.subscription_end_at = subscription_end_at
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if client_id is not None:
            self.client_id = client_id
        if payment_type is not None:
            self.payment_type = payment_type
        if amount_cents is not None:
            self.amount_cents = amount_cents
        if next_charge is not None:
            self.next_charge = next_charge
        if plan_type is not None:
            self.plan_type = plan_type
        if card is not None:
            self.card = card
        if light_seats is not None:
            self.light_seats = light_seats
        if canceled_at is not None:
            self.canceled_at = canceled_at
        if subscribers is not None:
            self.subscribers = subscribers
        if plan_name is not None:
            self.plan_name = plan_name
        if actual_amount_paid_cents is not None:
            self.actual_amount_paid_cents = actual_amount_paid_cents
        if trial_end is not None:
            self.trial_end = trial_end
        if coupon_percent_off is not None:
            self.coupon_percent_off = coupon_percent_off
        if reseller_name is not None:
            self.reseller_name = reseller_name
        if duration is not None:
            self.duration = duration
        if subscription_fields is not None:
            self.subscription_fields = subscription_fields
        if purchase_date is not None:
            self.purchase_date = purchase_date
        if pending_cancelation is not None:
            self.pending_cancelation = pending_cancelation
        if prorated_charges is not None:
            self.prorated_charges = prorated_charges
        if prorated_total is not None:
            self.prorated_total = prorated_total
        if coupon_amount_off is not None:
            self.coupon_amount_off = coupon_amount_off
        if duration_months is not None:
            self.duration_months = duration_months
        if last_modified is not None:
            self.last_modified = last_modified
        if currency is not None:
            self.currency = currency
        if state is not None:
            self.state = state
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def group(self):
        """Gets the group of this BTPurchaseInfo.  # noqa: E501


        :return: The group of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this BTPurchaseInfo.


        :param group: The group of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def application(self):
        """Gets the application of this BTPurchaseInfo.  # noqa: E501


        :return: The application of this BTPurchaseInfo.  # noqa: E501
        :rtype: BTAPIApplicationSummaryInfo
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this BTPurchaseInfo.


        :param application: The application of this BTPurchaseInfo.  # noqa: E501
        :type: BTAPIApplicationSummaryInfo
        """

        self._application = application

    @property
    def account_id(self):
        """Gets the account_id of this BTPurchaseInfo.  # noqa: E501


        :return: The account_id of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BTPurchaseInfo.


        :param account_id: The account_id of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def plan_id(self):
        """Gets the plan_id of this BTPurchaseInfo.  # noqa: E501


        :return: The plan_id of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this BTPurchaseInfo.


        :param plan_id: The plan_id of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def plan(self):
        """Gets the plan of this BTPurchaseInfo.  # noqa: E501


        :return: The plan of this BTPurchaseInfo.  # noqa: E501
        :rtype: BTBillingPlanInfo
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this BTPurchaseInfo.


        :param plan: The plan of this BTPurchaseInfo.  # noqa: E501
        :type: BTBillingPlanInfo
        """

        self._plan = plan

    @property
    def seats(self):
        """Gets the seats of this BTPurchaseInfo.  # noqa: E501


        :return: The seats of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._seats

    @seats.setter
    def seats(self, seats):
        """Sets the seats of this BTPurchaseInfo.


        :param seats: The seats of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._seats = seats

    @property
    def subscription_begin_at(self):
        """Gets the subscription_begin_at of this BTPurchaseInfo.  # noqa: E501


        :return: The subscription_begin_at of this BTPurchaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._subscription_begin_at

    @subscription_begin_at.setter
    def subscription_begin_at(self, subscription_begin_at):
        """Sets the subscription_begin_at of this BTPurchaseInfo.


        :param subscription_begin_at: The subscription_begin_at of this BTPurchaseInfo.  # noqa: E501
        :type: datetime
        """

        self._subscription_begin_at = subscription_begin_at

    @property
    def subscription_end_at(self):
        """Gets the subscription_end_at of this BTPurchaseInfo.  # noqa: E501


        :return: The subscription_end_at of this BTPurchaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._subscription_end_at

    @subscription_end_at.setter
    def subscription_end_at(self, subscription_end_at):
        """Sets the subscription_end_at of this BTPurchaseInfo.


        :param subscription_end_at: The subscription_end_at of this BTPurchaseInfo.  # noqa: E501
        :type: datetime
        """

        self._subscription_end_at = subscription_end_at

    @property
    def subscription_id(self):
        """Gets the subscription_id of this BTPurchaseInfo.  # noqa: E501


        :return: The subscription_id of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this BTPurchaseInfo.


        :param subscription_id: The subscription_id of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def client_id(self):
        """Gets the client_id of this BTPurchaseInfo.  # noqa: E501


        :return: The client_id of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this BTPurchaseInfo.


        :param client_id: The client_id of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def payment_type(self):
        """Gets the payment_type of this BTPurchaseInfo.  # noqa: E501


        :return: The payment_type of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this BTPurchaseInfo.


        :param payment_type: The payment_type of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._payment_type = payment_type

    @property
    def amount_cents(self):
        """Gets the amount_cents of this BTPurchaseInfo.  # noqa: E501


        :return: The amount_cents of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._amount_cents

    @amount_cents.setter
    def amount_cents(self, amount_cents):
        """Sets the amount_cents of this BTPurchaseInfo.


        :param amount_cents: The amount_cents of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._amount_cents = amount_cents

    @property
    def next_charge(self):
        """Gets the next_charge of this BTPurchaseInfo.  # noqa: E501


        :return: The next_charge of this BTPurchaseInfo.  # noqa: E501
        :rtype: NextCharge
        """
        return self._next_charge

    @next_charge.setter
    def next_charge(self, next_charge):
        """Sets the next_charge of this BTPurchaseInfo.


        :param next_charge: The next_charge of this BTPurchaseInfo.  # noqa: E501
        :type: NextCharge
        """

        self._next_charge = next_charge

    @property
    def plan_type(self):
        """Gets the plan_type of this BTPurchaseInfo.  # noqa: E501


        :return: The plan_type of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._plan_type

    @plan_type.setter
    def plan_type(self, plan_type):
        """Sets the plan_type of this BTPurchaseInfo.


        :param plan_type: The plan_type of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._plan_type = plan_type

    @property
    def card(self):
        """Gets the card of this BTPurchaseInfo.  # noqa: E501


        :return: The card of this BTPurchaseInfo.  # noqa: E501
        :rtype: BTCardInfo
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this BTPurchaseInfo.


        :param card: The card of this BTPurchaseInfo.  # noqa: E501
        :type: BTCardInfo
        """

        self._card = card

    @property
    def light_seats(self):
        """Gets the light_seats of this BTPurchaseInfo.  # noqa: E501


        :return: The light_seats of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._light_seats

    @light_seats.setter
    def light_seats(self, light_seats):
        """Sets the light_seats of this BTPurchaseInfo.


        :param light_seats: The light_seats of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._light_seats = light_seats

    @property
    def canceled_at(self):
        """Gets the canceled_at of this BTPurchaseInfo.  # noqa: E501


        :return: The canceled_at of this BTPurchaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._canceled_at

    @canceled_at.setter
    def canceled_at(self, canceled_at):
        """Sets the canceled_at of this BTPurchaseInfo.


        :param canceled_at: The canceled_at of this BTPurchaseInfo.  # noqa: E501
        :type: datetime
        """

        self._canceled_at = canceled_at

    @property
    def subscribers(self):
        """Gets the subscribers of this BTPurchaseInfo.  # noqa: E501


        :return: The subscribers of this BTPurchaseInfo.  # noqa: E501
        :rtype: list[BTPlanSubscriberInfo]
        """
        return self._subscribers

    @subscribers.setter
    def subscribers(self, subscribers):
        """Sets the subscribers of this BTPurchaseInfo.


        :param subscribers: The subscribers of this BTPurchaseInfo.  # noqa: E501
        :type: list[BTPlanSubscriberInfo]
        """

        self._subscribers = subscribers

    @property
    def plan_name(self):
        """Gets the plan_name of this BTPurchaseInfo.  # noqa: E501


        :return: The plan_name of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this BTPurchaseInfo.


        :param plan_name: The plan_name of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._plan_name = plan_name

    @property
    def actual_amount_paid_cents(self):
        """Gets the actual_amount_paid_cents of this BTPurchaseInfo.  # noqa: E501


        :return: The actual_amount_paid_cents of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._actual_amount_paid_cents

    @actual_amount_paid_cents.setter
    def actual_amount_paid_cents(self, actual_amount_paid_cents):
        """Sets the actual_amount_paid_cents of this BTPurchaseInfo.


        :param actual_amount_paid_cents: The actual_amount_paid_cents of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._actual_amount_paid_cents = actual_amount_paid_cents

    @property
    def trial_end(self):
        """Gets the trial_end of this BTPurchaseInfo.  # noqa: E501


        :return: The trial_end of this BTPurchaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._trial_end

    @trial_end.setter
    def trial_end(self, trial_end):
        """Sets the trial_end of this BTPurchaseInfo.


        :param trial_end: The trial_end of this BTPurchaseInfo.  # noqa: E501
        :type: datetime
        """

        self._trial_end = trial_end

    @property
    def coupon_percent_off(self):
        """Gets the coupon_percent_off of this BTPurchaseInfo.  # noqa: E501


        :return: The coupon_percent_off of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._coupon_percent_off

    @coupon_percent_off.setter
    def coupon_percent_off(self, coupon_percent_off):
        """Sets the coupon_percent_off of this BTPurchaseInfo.


        :param coupon_percent_off: The coupon_percent_off of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._coupon_percent_off = coupon_percent_off

    @property
    def reseller_name(self):
        """Gets the reseller_name of this BTPurchaseInfo.  # noqa: E501


        :return: The reseller_name of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._reseller_name

    @reseller_name.setter
    def reseller_name(self, reseller_name):
        """Sets the reseller_name of this BTPurchaseInfo.


        :param reseller_name: The reseller_name of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._reseller_name = reseller_name

    @property
    def duration(self):
        """Gets the duration of this BTPurchaseInfo.  # noqa: E501


        :return: The duration of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this BTPurchaseInfo.


        :param duration: The duration of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def subscription_fields(self):
        """Gets the subscription_fields of this BTPurchaseInfo.  # noqa: E501


        :return: The subscription_fields of this BTPurchaseInfo.  # noqa: E501
        :rtype: Subscription
        """
        return self._subscription_fields

    @subscription_fields.setter
    def subscription_fields(self, subscription_fields):
        """Sets the subscription_fields of this BTPurchaseInfo.


        :param subscription_fields: The subscription_fields of this BTPurchaseInfo.  # noqa: E501
        :type: Subscription
        """

        self._subscription_fields = subscription_fields

    @property
    def purchase_date(self):
        """Gets the purchase_date of this BTPurchaseInfo.  # noqa: E501


        :return: The purchase_date of this BTPurchaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, purchase_date):
        """Sets the purchase_date of this BTPurchaseInfo.


        :param purchase_date: The purchase_date of this BTPurchaseInfo.  # noqa: E501
        :type: datetime
        """

        self._purchase_date = purchase_date

    @property
    def pending_cancelation(self):
        """Gets the pending_cancelation of this BTPurchaseInfo.  # noqa: E501


        :return: The pending_cancelation of this BTPurchaseInfo.  # noqa: E501
        :rtype: bool
        """
        return self._pending_cancelation

    @pending_cancelation.setter
    def pending_cancelation(self, pending_cancelation):
        """Sets the pending_cancelation of this BTPurchaseInfo.


        :param pending_cancelation: The pending_cancelation of this BTPurchaseInfo.  # noqa: E501
        :type: bool
        """

        self._pending_cancelation = pending_cancelation

    @property
    def prorated_charges(self):
        """Gets the prorated_charges of this BTPurchaseInfo.  # noqa: E501


        :return: The prorated_charges of this BTPurchaseInfo.  # noqa: E501
        :rtype: list[ProratedCharges]
        """
        return self._prorated_charges

    @prorated_charges.setter
    def prorated_charges(self, prorated_charges):
        """Sets the prorated_charges of this BTPurchaseInfo.


        :param prorated_charges: The prorated_charges of this BTPurchaseInfo.  # noqa: E501
        :type: list[ProratedCharges]
        """

        self._prorated_charges = prorated_charges

    @property
    def prorated_total(self):
        """Gets the prorated_total of this BTPurchaseInfo.  # noqa: E501


        :return: The prorated_total of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._prorated_total

    @prorated_total.setter
    def prorated_total(self, prorated_total):
        """Sets the prorated_total of this BTPurchaseInfo.


        :param prorated_total: The prorated_total of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._prorated_total = prorated_total

    @property
    def coupon_amount_off(self):
        """Gets the coupon_amount_off of this BTPurchaseInfo.  # noqa: E501


        :return: The coupon_amount_off of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._coupon_amount_off

    @coupon_amount_off.setter
    def coupon_amount_off(self, coupon_amount_off):
        """Sets the coupon_amount_off of this BTPurchaseInfo.


        :param coupon_amount_off: The coupon_amount_off of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._coupon_amount_off = coupon_amount_off

    @property
    def duration_months(self):
        """Gets the duration_months of this BTPurchaseInfo.  # noqa: E501


        :return: The duration_months of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._duration_months

    @duration_months.setter
    def duration_months(self, duration_months):
        """Sets the duration_months of this BTPurchaseInfo.


        :param duration_months: The duration_months of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._duration_months = duration_months

    @property
    def last_modified(self):
        """Gets the last_modified of this BTPurchaseInfo.  # noqa: E501


        :return: The last_modified of this BTPurchaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this BTPurchaseInfo.


        :param last_modified: The last_modified of this BTPurchaseInfo.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def currency(self):
        """Gets the currency of this BTPurchaseInfo.  # noqa: E501


        :return: The currency of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this BTPurchaseInfo.


        :param currency: The currency of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def state(self):
        """Gets the state of this BTPurchaseInfo.  # noqa: E501


        :return: The state of this BTPurchaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTPurchaseInfo.


        :param state: The state of this BTPurchaseInfo.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def href(self):
        """Gets the href of this BTPurchaseInfo.  # noqa: E501


        :return: The href of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTPurchaseInfo.


        :param href: The href of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTPurchaseInfo.  # noqa: E501


        :return: The view_ref of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTPurchaseInfo.


        :param view_ref: The view_ref of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def id(self):
        """Gets the id of this BTPurchaseInfo.  # noqa: E501


        :return: The id of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTPurchaseInfo.


        :param id: The id of this BTPurchaseInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BTPurchaseInfo.  # noqa: E501


        :return: The name of this BTPurchaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTPurchaseInfo.


        :param name: The name of this BTPurchaseInfo.  # noqa: E501
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
        if not isinstance(other, BTPurchaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
