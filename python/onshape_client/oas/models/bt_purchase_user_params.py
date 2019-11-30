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


class BTPurchaseUserParams(object):
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
        'user_id': 'str',
        'consumed_quantity': 'int',
        'purchase_id': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'consumed_quantity': 'consumedQuantity',
        'purchase_id': 'purchaseId'
    }

    def __init__(self, user_id=None, consumed_quantity=None, purchase_id=None):  # noqa: E501
        """BTPurchaseUserParams - a model defined in OpenAPI"""  # noqa: E501

        self._user_id = None
        self._consumed_quantity = None
        self._purchase_id = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if consumed_quantity is not None:
            self.consumed_quantity = consumed_quantity
        if purchase_id is not None:
            self.purchase_id = purchase_id

    @property
    def user_id(self):
        """Gets the user_id of this BTPurchaseUserParams.  # noqa: E501


        :return: The user_id of this BTPurchaseUserParams.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BTPurchaseUserParams.


        :param user_id: The user_id of this BTPurchaseUserParams.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def consumed_quantity(self):
        """Gets the consumed_quantity of this BTPurchaseUserParams.  # noqa: E501


        :return: The consumed_quantity of this BTPurchaseUserParams.  # noqa: E501
        :rtype: int
        """
        return self._consumed_quantity

    @consumed_quantity.setter
    def consumed_quantity(self, consumed_quantity):
        """Sets the consumed_quantity of this BTPurchaseUserParams.


        :param consumed_quantity: The consumed_quantity of this BTPurchaseUserParams.  # noqa: E501
        :type: int
        """

        self._consumed_quantity = consumed_quantity

    @property
    def purchase_id(self):
        """Gets the purchase_id of this BTPurchaseUserParams.  # noqa: E501


        :return: The purchase_id of this BTPurchaseUserParams.  # noqa: E501
        :rtype: str
        """
        return self._purchase_id

    @purchase_id.setter
    def purchase_id(self, purchase_id):
        """Sets the purchase_id of this BTPurchaseUserParams.


        :param purchase_id: The purchase_id of this BTPurchaseUserParams.  # noqa: E501
        :type: str
        """

        self._purchase_id = purchase_id

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
        if not isinstance(other, BTPurchaseUserParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
