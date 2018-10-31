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

from onshape_client.models.assemblies_get_named_views_response200_named_views_key import AssembliesGetNamedViewsResponse200NamedViewsKey  # noqa: F401,E501
from onshape_client.models.assemblies_get_named_views_response200_named_views_view_name import AssembliesGetNamedViewsResponse200NamedViewsViewName  # noqa: F401,E501


class AssembliesGetNamedViewsResponse200NamedViews(object):
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
        'view_name': 'AssembliesGetNamedViewsResponse200NamedViewsViewName',
        'key': 'AssembliesGetNamedViewsResponse200NamedViewsKey'
    }

    attribute_map = {
        'view_name': 'viewName',
        'key': 'key'
    }

    def __init__(self, view_name=None, key=None):  # noqa: E501
        """AssembliesGetNamedViewsResponse200NamedViews - a model defined in Swagger"""  # noqa: E501

        self._view_name = None
        self._key = None
        self.discriminator = None

        if view_name is not None:
            self.view_name = view_name
        if key is not None:
            self.key = key

    @property
    def view_name(self):
        """Gets the view_name of this AssembliesGetNamedViewsResponse200NamedViews.  # noqa: E501


        :return: The view_name of this AssembliesGetNamedViewsResponse200NamedViews.  # noqa: E501
        :rtype: AssembliesGetNamedViewsResponse200NamedViewsViewName
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """Sets the view_name of this AssembliesGetNamedViewsResponse200NamedViews.


        :param view_name: The view_name of this AssembliesGetNamedViewsResponse200NamedViews.  # noqa: E501
        :type: AssembliesGetNamedViewsResponse200NamedViewsViewName
        """

        self._view_name = view_name

    @property
    def key(self):
        """Gets the key of this AssembliesGetNamedViewsResponse200NamedViews.  # noqa: E501


        :return: The key of this AssembliesGetNamedViewsResponse200NamedViews.  # noqa: E501
        :rtype: AssembliesGetNamedViewsResponse200NamedViewsKey
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AssembliesGetNamedViewsResponse200NamedViews.


        :param key: The key of this AssembliesGetNamedViewsResponse200NamedViews.  # noqa: E501
        :type: AssembliesGetNamedViewsResponse200NamedViewsKey
        """

        self._key = key

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
        if not isinstance(other, AssembliesGetNamedViewsResponse200NamedViews):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
