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


class ThermostatSensorAccessoryValue(object):
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
        'cool_setpoint': 'float',
        'heat_setpoint': 'float',
        'indoor_humidity': 'float',
        'indoor_temperature': 'float',
        'motion_det': 'bool',
        'occupancy_det': 'bool',
        'exclude_temp': 'bool',
        'exclude_motion': 'bool',
        'pressure': 'float',
        'occupancy_sensitivity': 'str',
        'occupancy_timeout': 'int',
        'status': 'str',
        'battery_status': 'str',
        'rssi_average': 'float'
    }

    attribute_map = {
        'cool_setpoint': 'coolSetpoint',
        'heat_setpoint': 'heatSetpoint',
        'indoor_humidity': 'indoorHumidity',
        'indoor_temperature': 'indoorTemperature',
        'motion_det': 'motionDet',
        'occupancy_det': 'occupancyDet',
        'exclude_temp': 'excludeTemp',
        'exclude_motion': 'excludeMotion',
        'pressure': 'pressure',
        'occupancy_sensitivity': 'occupancySensitivity',
        'occupancy_timeout': 'occupancyTimeout',
        'status': 'status',
        'battery_status': 'batteryStatus',
        'rssi_average': 'rssiAverage'
    }

    def __init__(self, cool_setpoint=None, heat_setpoint=None, indoor_humidity=None, indoor_temperature=None, motion_det=None, occupancy_det=None, exclude_temp=None, exclude_motion=None, pressure=None, occupancy_sensitivity=None, occupancy_timeout=None, status=None, battery_status=None, rssi_average=None):  # noqa: E501
        """ThermostatSensorAccessoryValue - a model defined in OpenAPI"""  # noqa: E501

        self._cool_setpoint = None
        self._heat_setpoint = None
        self._indoor_humidity = None
        self._indoor_temperature = None
        self._motion_det = None
        self._occupancy_det = None
        self._exclude_temp = None
        self._exclude_motion = None
        self._pressure = None
        self._occupancy_sensitivity = None
        self._occupancy_timeout = None
        self._status = None
        self._battery_status = None
        self._rssi_average = None
        self.discriminator = None

        if cool_setpoint is not None:
            self.cool_setpoint = cool_setpoint
        if heat_setpoint is not None:
            self.heat_setpoint = heat_setpoint
        if indoor_humidity is not None:
            self.indoor_humidity = indoor_humidity
        if indoor_temperature is not None:
            self.indoor_temperature = indoor_temperature
        if motion_det is not None:
            self.motion_det = motion_det
        if occupancy_det is not None:
            self.occupancy_det = occupancy_det
        if exclude_temp is not None:
            self.exclude_temp = exclude_temp
        if exclude_motion is not None:
            self.exclude_motion = exclude_motion
        if pressure is not None:
            self.pressure = pressure
        if occupancy_sensitivity is not None:
            self.occupancy_sensitivity = occupancy_sensitivity
        if occupancy_timeout is not None:
            self.occupancy_timeout = occupancy_timeout
        if status is not None:
            self.status = status
        if battery_status is not None:
            self.battery_status = battery_status
        if rssi_average is not None:
            self.rssi_average = rssi_average

    @property
    def cool_setpoint(self):
        """Gets the cool_setpoint of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The cool_setpoint of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: float
        """
        return self._cool_setpoint

    @cool_setpoint.setter
    def cool_setpoint(self, cool_setpoint):
        """Sets the cool_setpoint of this ThermostatSensorAccessoryValue.


        :param cool_setpoint: The cool_setpoint of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: float
        """

        self._cool_setpoint = cool_setpoint

    @property
    def heat_setpoint(self):
        """Gets the heat_setpoint of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The heat_setpoint of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: float
        """
        return self._heat_setpoint

    @heat_setpoint.setter
    def heat_setpoint(self, heat_setpoint):
        """Sets the heat_setpoint of this ThermostatSensorAccessoryValue.


        :param heat_setpoint: The heat_setpoint of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: float
        """

        self._heat_setpoint = heat_setpoint

    @property
    def indoor_humidity(self):
        """Gets the indoor_humidity of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The indoor_humidity of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: float
        """
        return self._indoor_humidity

    @indoor_humidity.setter
    def indoor_humidity(self, indoor_humidity):
        """Sets the indoor_humidity of this ThermostatSensorAccessoryValue.


        :param indoor_humidity: The indoor_humidity of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: float
        """

        self._indoor_humidity = indoor_humidity

    @property
    def indoor_temperature(self):
        """Gets the indoor_temperature of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The indoor_temperature of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: float
        """
        return self._indoor_temperature

    @indoor_temperature.setter
    def indoor_temperature(self, indoor_temperature):
        """Sets the indoor_temperature of this ThermostatSensorAccessoryValue.


        :param indoor_temperature: The indoor_temperature of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: float
        """

        self._indoor_temperature = indoor_temperature

    @property
    def motion_det(self):
        """Gets the motion_det of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The motion_det of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: bool
        """
        return self._motion_det

    @motion_det.setter
    def motion_det(self, motion_det):
        """Sets the motion_det of this ThermostatSensorAccessoryValue.


        :param motion_det: The motion_det of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: bool
        """

        self._motion_det = motion_det

    @property
    def occupancy_det(self):
        """Gets the occupancy_det of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The occupancy_det of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: bool
        """
        return self._occupancy_det

    @occupancy_det.setter
    def occupancy_det(self, occupancy_det):
        """Sets the occupancy_det of this ThermostatSensorAccessoryValue.


        :param occupancy_det: The occupancy_det of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: bool
        """

        self._occupancy_det = occupancy_det

    @property
    def exclude_temp(self):
        """Gets the exclude_temp of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The exclude_temp of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_temp

    @exclude_temp.setter
    def exclude_temp(self, exclude_temp):
        """Sets the exclude_temp of this ThermostatSensorAccessoryValue.


        :param exclude_temp: The exclude_temp of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: bool
        """

        self._exclude_temp = exclude_temp

    @property
    def exclude_motion(self):
        """Gets the exclude_motion of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The exclude_motion of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_motion

    @exclude_motion.setter
    def exclude_motion(self, exclude_motion):
        """Sets the exclude_motion of this ThermostatSensorAccessoryValue.


        :param exclude_motion: The exclude_motion of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: bool
        """

        self._exclude_motion = exclude_motion

    @property
    def pressure(self):
        """Gets the pressure of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The pressure of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: float
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this ThermostatSensorAccessoryValue.


        :param pressure: The pressure of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: float
        """

        self._pressure = pressure

    @property
    def occupancy_sensitivity(self):
        """Gets the occupancy_sensitivity of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The occupancy_sensitivity of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: str
        """
        return self._occupancy_sensitivity

    @occupancy_sensitivity.setter
    def occupancy_sensitivity(self, occupancy_sensitivity):
        """Sets the occupancy_sensitivity of this ThermostatSensorAccessoryValue.


        :param occupancy_sensitivity: The occupancy_sensitivity of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: str
        """

        self._occupancy_sensitivity = occupancy_sensitivity

    @property
    def occupancy_timeout(self):
        """Gets the occupancy_timeout of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The occupancy_timeout of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: int
        """
        return self._occupancy_timeout

    @occupancy_timeout.setter
    def occupancy_timeout(self, occupancy_timeout):
        """Sets the occupancy_timeout of this ThermostatSensorAccessoryValue.


        :param occupancy_timeout: The occupancy_timeout of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: int
        """

        self._occupancy_timeout = occupancy_timeout

    @property
    def status(self):
        """Gets the status of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The status of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ThermostatSensorAccessoryValue.


        :param status: The status of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def battery_status(self):
        """Gets the battery_status of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The battery_status of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: str
        """
        return self._battery_status

    @battery_status.setter
    def battery_status(self, battery_status):
        """Sets the battery_status of this ThermostatSensorAccessoryValue.


        :param battery_status: The battery_status of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: str
        """

        self._battery_status = battery_status

    @property
    def rssi_average(self):
        """Gets the rssi_average of this ThermostatSensorAccessoryValue.  # noqa: E501


        :return: The rssi_average of this ThermostatSensorAccessoryValue.  # noqa: E501
        :rtype: float
        """
        return self._rssi_average

    @rssi_average.setter
    def rssi_average(self, rssi_average):
        """Sets the rssi_average of this ThermostatSensorAccessoryValue.


        :param rssi_average: The rssi_average of this ThermostatSensorAccessoryValue.  # noqa: E501
        :type: float
        """

        self._rssi_average = rssi_average

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
        if not isinstance(other, ThermostatSensorAccessoryValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other