# coding: utf-8

"""
    Client Portal Web API

    Production version of the Client Portal Web API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20027TradingTimes(object):
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
        'opening_time': 'int',
        'closing_time': 'int',
        'cancel_day_orders': 'str'
    }

    attribute_map = {
        'opening_time': 'openingTime',
        'closing_time': 'closingTime',
        'cancel_day_orders': 'cancelDayOrders'
    }

    def __init__(self, opening_time=None, closing_time=None, cancel_day_orders=None):  # noqa: E501
        """InlineResponse20027TradingTimes - a model defined in Swagger"""  # noqa: E501

        self._opening_time = None
        self._closing_time = None
        self._cancel_day_orders = None
        self.discriminator = None

        if opening_time is not None:
            self.opening_time = opening_time
        if closing_time is not None:
            self.closing_time = closing_time
        if cancel_day_orders is not None:
            self.cancel_day_orders = cancel_day_orders

    @property
    def opening_time(self):
        """Gets the opening_time of this InlineResponse20027TradingTimes.  # noqa: E501


        :return: The opening_time of this InlineResponse20027TradingTimes.  # noqa: E501
        :rtype: int
        """
        return self._opening_time

    @opening_time.setter
    def opening_time(self, opening_time):
        """Sets the opening_time of this InlineResponse20027TradingTimes.


        :param opening_time: The opening_time of this InlineResponse20027TradingTimes.  # noqa: E501
        :type: int
        """

        self._opening_time = opening_time

    @property
    def closing_time(self):
        """Gets the closing_time of this InlineResponse20027TradingTimes.  # noqa: E501


        :return: The closing_time of this InlineResponse20027TradingTimes.  # noqa: E501
        :rtype: int
        """
        return self._closing_time

    @closing_time.setter
    def closing_time(self, closing_time):
        """Sets the closing_time of this InlineResponse20027TradingTimes.


        :param closing_time: The closing_time of this InlineResponse20027TradingTimes.  # noqa: E501
        :type: int
        """

        self._closing_time = closing_time

    @property
    def cancel_day_orders(self):
        """Gets the cancel_day_orders of this InlineResponse20027TradingTimes.  # noqa: E501


        :return: The cancel_day_orders of this InlineResponse20027TradingTimes.  # noqa: E501
        :rtype: str
        """
        return self._cancel_day_orders

    @cancel_day_orders.setter
    def cancel_day_orders(self, cancel_day_orders):
        """Sets the cancel_day_orders of this InlineResponse20027TradingTimes.


        :param cancel_day_orders: The cancel_day_orders of this InlineResponse20027TradingTimes.  # noqa: E501
        :type: str
        """

        self._cancel_day_orders = cancel_day_orders

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
        if issubclass(InlineResponse20027TradingTimes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20027TradingTimes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
