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


class ThermostatSettingsSpecialMode(object):
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
        'auto_changeover_active': 'bool',
        'emergency_heat_active': 'bool'
    }

    attribute_map = {
        'auto_changeover_active': 'autoChangeoverActive',
        'emergency_heat_active': 'emergencyHeatActive'
    }

    def __init__(self, auto_changeover_active=None, emergency_heat_active=None):  # noqa: E501
        """ThermostatSettingsSpecialMode - a model defined in OpenAPI"""  # noqa: E501

        self._auto_changeover_active = None
        self._emergency_heat_active = None
        self.discriminator = None

        if auto_changeover_active is not None:
            self.auto_changeover_active = auto_changeover_active
        if emergency_heat_active is not None:
            self.emergency_heat_active = emergency_heat_active

    @property
    def auto_changeover_active(self):
        """Gets the auto_changeover_active of this ThermostatSettingsSpecialMode.  # noqa: E501


        :return: The auto_changeover_active of this ThermostatSettingsSpecialMode.  # noqa: E501
        :rtype: bool
        """
        return self._auto_changeover_active

    @auto_changeover_active.setter
    def auto_changeover_active(self, auto_changeover_active):
        """Sets the auto_changeover_active of this ThermostatSettingsSpecialMode.


        :param auto_changeover_active: The auto_changeover_active of this ThermostatSettingsSpecialMode.  # noqa: E501
        :type: bool
        """

        self._auto_changeover_active = auto_changeover_active

    @property
    def emergency_heat_active(self):
        """Gets the emergency_heat_active of this ThermostatSettingsSpecialMode.  # noqa: E501


        :return: The emergency_heat_active of this ThermostatSettingsSpecialMode.  # noqa: E501
        :rtype: bool
        """
        return self._emergency_heat_active

    @emergency_heat_active.setter
    def emergency_heat_active(self, emergency_heat_active):
        """Sets the emergency_heat_active of this ThermostatSettingsSpecialMode.


        :param emergency_heat_active: The emergency_heat_active of this ThermostatSettingsSpecialMode.  # noqa: E501
        :type: bool
        """

        self._emergency_heat_active = emergency_heat_active

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
        if not isinstance(other, ThermostatSettingsSpecialMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other