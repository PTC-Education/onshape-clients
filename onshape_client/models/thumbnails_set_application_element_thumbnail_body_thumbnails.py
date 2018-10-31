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


class ThumbnailsSetApplicationElementThumbnailBodyThumbnails(object):
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
        'base64_encoded_image': 'str',
        'description': 'str',
        'image_height': 'float',
        'unique_id': 'str',
        'image_width': 'float',
        'is_primary': 'bool'
    }

    attribute_map = {
        'base64_encoded_image': 'base64EncodedImage',
        'description': 'description',
        'image_height': 'imageHeight',
        'unique_id': 'uniqueId',
        'image_width': 'imageWidth',
        'is_primary': 'isPrimary'
    }

    def __init__(self, base64_encoded_image=None, description=None, image_height=None, unique_id=None, image_width=None, is_primary=None):  # noqa: E501
        """ThumbnailsSetApplicationElementThumbnailBodyThumbnails - a model defined in Swagger"""  # noqa: E501

        self._base64_encoded_image = None
        self._description = None
        self._image_height = None
        self._unique_id = None
        self._image_width = None
        self._is_primary = None
        self.discriminator = None

        if base64_encoded_image is not None:
            self.base64_encoded_image = base64_encoded_image
        if description is not None:
            self.description = description
        if image_height is not None:
            self.image_height = image_height
        if unique_id is not None:
            self.unique_id = unique_id
        if image_width is not None:
            self.image_width = image_width
        if is_primary is not None:
            self.is_primary = is_primary

    @property
    def base64_encoded_image(self):
        """Gets the base64_encoded_image of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501

        Base-64 encoded image string.  # noqa: E501

        :return: The base64_encoded_image of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :rtype: str
        """
        return self._base64_encoded_image

    @base64_encoded_image.setter
    def base64_encoded_image(self, base64_encoded_image):
        """Sets the base64_encoded_image of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.

        Base-64 encoded image string.  # noqa: E501

        :param base64_encoded_image: The base64_encoded_image of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :type: str
        """

        self._base64_encoded_image = base64_encoded_image

    @property
    def description(self):
        """Gets the description of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501

        An optional description of the image.  # noqa: E501

        :return: The description of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.

        An optional description of the image.  # noqa: E501

        :param description: The description of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image_height(self):
        """Gets the image_height of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501

        The height of the image being supplied. Suggested minimum is 600 pixels.  # noqa: E501

        :return: The image_height of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :rtype: float
        """
        return self._image_height

    @image_height.setter
    def image_height(self, image_height):
        """Sets the image_height of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.

        The height of the image being supplied. Suggested minimum is 600 pixels.  # noqa: E501

        :param image_height: The image_height of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :type: float
        """

        self._image_height = image_height

    @property
    def unique_id(self):
        """Gets the unique_id of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501

        A per element unique identifier, which is consistent across document versions and microversions.  # noqa: E501

        :return: The unique_id of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.

        A per element unique identifier, which is consistent across document versions and microversions.  # noqa: E501

        :param unique_id: The unique_id of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :type: str
        """

        self._unique_id = unique_id

    @property
    def image_width(self):
        """Gets the image_width of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501

        The width of the image being supplied. Suggested minimum is 600 pixels.  # noqa: E501

        :return: The image_width of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :rtype: float
        """
        return self._image_width

    @image_width.setter
    def image_width(self, image_width):
        """Sets the image_width of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.

        The width of the image being supplied. Suggested minimum is 600 pixels.  # noqa: E501

        :param image_width: The image_width of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :type: float
        """

        self._image_width = image_width

    @property
    def is_primary(self):
        """Gets the is_primary of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501

        If true, this image is used as the element image. Only one thumbnail can be designated as the primary thumbnail.  # noqa: E501

        :return: The is_primary of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """Sets the is_primary of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.

        If true, this image is used as the element image. Only one thumbnail can be designated as the primary thumbnail.  # noqa: E501

        :param is_primary: The is_primary of this ThumbnailsSetApplicationElementThumbnailBodyThumbnails.  # noqa: E501
        :type: bool
        """

        self._is_primary = is_primary

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
        if not isinstance(other, ThumbnailsSetApplicationElementThumbnailBodyThumbnails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
