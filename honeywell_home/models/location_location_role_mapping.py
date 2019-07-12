# coding: utf-8

"""
    Honeywell Home

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class LocationLocationRoleMapping(object):
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
        'location_id': 'int',
        'role': 'str',
        'location_name': 'str',
        'status': 'int'
    }

    attribute_map = {
        'location_id': 'locationID',
        'role': 'role',
        'location_name': 'locationName',
        'status': 'status'
    }

    def __init__(self, location_id=None, role=None, location_name=None, status=None):  # noqa: E501
        """LocationLocationRoleMapping - a model defined in OpenAPI"""  # noqa: E501

        self._location_id = None
        self._role = None
        self._location_name = None
        self._status = None
        self.discriminator = None

        if location_id is not None:
            self.location_id = location_id
        if role is not None:
            self.role = role
        if location_name is not None:
            self.location_name = location_name
        if status is not None:
            self.status = status

    @property
    def location_id(self):
        """Gets the location_id of this LocationLocationRoleMapping.  # noqa: E501


        :return: The location_id of this LocationLocationRoleMapping.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this LocationLocationRoleMapping.


        :param location_id: The location_id of this LocationLocationRoleMapping.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def role(self):
        """Gets the role of this LocationLocationRoleMapping.  # noqa: E501


        :return: The role of this LocationLocationRoleMapping.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this LocationLocationRoleMapping.


        :param role: The role of this LocationLocationRoleMapping.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def location_name(self):
        """Gets the location_name of this LocationLocationRoleMapping.  # noqa: E501


        :return: The location_name of this LocationLocationRoleMapping.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this LocationLocationRoleMapping.


        :param location_name: The location_name of this LocationLocationRoleMapping.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def status(self):
        """Gets the status of this LocationLocationRoleMapping.  # noqa: E501


        :return: The status of this LocationLocationRoleMapping.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LocationLocationRoleMapping.


        :param status: The status of this LocationLocationRoleMapping.  # noqa: E501
        :type: int
        """

        self._status = status

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
        if not isinstance(other, LocationLocationRoleMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
