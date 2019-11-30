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


class BTMParameterDerived864(object):
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
        'module_id': 'BTPModuleId235',
        'namespace': 'str',
        'imports': 'list[BTMImport136]'
    }

    attribute_map = {
        'module_id': 'moduleId',
        'namespace': 'namespace',
        'imports': 'imports'
    }

    def __init__(self, module_id=None, namespace=None, imports=None):  # noqa: E501
        """BTMParameterDerived864 - a model defined in OpenAPI"""  # noqa: E501

        self._module_id = None
        self._namespace = None
        self._imports = None
        self.discriminator = None

        if module_id is not None:
            self.module_id = module_id
        if namespace is not None:
            self.namespace = namespace
        if imports is not None:
            self.imports = imports

    @property
    def module_id(self):
        """Gets the module_id of this BTMParameterDerived864.  # noqa: E501


        :return: The module_id of this BTMParameterDerived864.  # noqa: E501
        :rtype: BTPModuleId235
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this BTMParameterDerived864.


        :param module_id: The module_id of this BTMParameterDerived864.  # noqa: E501
        :type: BTPModuleId235
        """

        self._module_id = module_id

    @property
    def namespace(self):
        """Gets the namespace of this BTMParameterDerived864.  # noqa: E501


        :return: The namespace of this BTMParameterDerived864.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BTMParameterDerived864.


        :param namespace: The namespace of this BTMParameterDerived864.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def imports(self):
        """Gets the imports of this BTMParameterDerived864.  # noqa: E501


        :return: The imports of this BTMParameterDerived864.  # noqa: E501
        :rtype: list[BTMImport136]
        """
        return self._imports

    @imports.setter
    def imports(self, imports):
        """Sets the imports of this BTMParameterDerived864.


        :param imports: The imports of this BTMParameterDerived864.  # noqa: E501
        :type: list[BTMImport136]
        """

        self._imports = imports

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
        if not isinstance(other, BTMParameterDerived864):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
