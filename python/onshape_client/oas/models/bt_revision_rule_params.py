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


class BTRevisionRuleParams(object):
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
        'company_id': 'str',
        'revision_list': 'list[str]',
        'rule_type': 'int',
        'validation_regex': 'str',
        'script': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'company_id': 'companyId',
        'revision_list': 'revisionList',
        'rule_type': 'ruleType',
        'validation_regex': 'validationRegex',
        'script': 'script',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, company_id=None, revision_list=None, rule_type=None, validation_regex=None, script=None, description=None, name=None):  # noqa: E501
        """BTRevisionRuleParams - a model defined in OpenAPI"""  # noqa: E501

        self._company_id = None
        self._revision_list = None
        self._rule_type = None
        self._validation_regex = None
        self._script = None
        self._description = None
        self._name = None
        self.discriminator = None

        if company_id is not None:
            self.company_id = company_id
        if revision_list is not None:
            self.revision_list = revision_list
        if rule_type is not None:
            self.rule_type = rule_type
        if validation_regex is not None:
            self.validation_regex = validation_regex
        if script is not None:
            self.script = script
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def company_id(self):
        """Gets the company_id of this BTRevisionRuleParams.  # noqa: E501


        :return: The company_id of this BTRevisionRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTRevisionRuleParams.


        :param company_id: The company_id of this BTRevisionRuleParams.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def revision_list(self):
        """Gets the revision_list of this BTRevisionRuleParams.  # noqa: E501


        :return: The revision_list of this BTRevisionRuleParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._revision_list

    @revision_list.setter
    def revision_list(self, revision_list):
        """Sets the revision_list of this BTRevisionRuleParams.


        :param revision_list: The revision_list of this BTRevisionRuleParams.  # noqa: E501
        :type: list[str]
        """

        self._revision_list = revision_list

    @property
    def rule_type(self):
        """Gets the rule_type of this BTRevisionRuleParams.  # noqa: E501


        :return: The rule_type of this BTRevisionRuleParams.  # noqa: E501
        :rtype: int
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this BTRevisionRuleParams.


        :param rule_type: The rule_type of this BTRevisionRuleParams.  # noqa: E501
        :type: int
        """

        self._rule_type = rule_type

    @property
    def validation_regex(self):
        """Gets the validation_regex of this BTRevisionRuleParams.  # noqa: E501


        :return: The validation_regex of this BTRevisionRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._validation_regex

    @validation_regex.setter
    def validation_regex(self, validation_regex):
        """Sets the validation_regex of this BTRevisionRuleParams.


        :param validation_regex: The validation_regex of this BTRevisionRuleParams.  # noqa: E501
        :type: str
        """

        self._validation_regex = validation_regex

    @property
    def script(self):
        """Gets the script of this BTRevisionRuleParams.  # noqa: E501


        :return: The script of this BTRevisionRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this BTRevisionRuleParams.


        :param script: The script of this BTRevisionRuleParams.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def description(self):
        """Gets the description of this BTRevisionRuleParams.  # noqa: E501


        :return: The description of this BTRevisionRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTRevisionRuleParams.


        :param description: The description of this BTRevisionRuleParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this BTRevisionRuleParams.  # noqa: E501


        :return: The name of this BTRevisionRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTRevisionRuleParams.


        :param name: The name of this BTRevisionRuleParams.  # noqa: E501
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
        if not isinstance(other, BTRevisionRuleParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
