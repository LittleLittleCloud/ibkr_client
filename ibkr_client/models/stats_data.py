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


class StatsData(object):
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
        'conid': 'float',
        'exchange': 'str',
        'v': 'float',
        't': 'float',
        'tt': 'float',
        'p': 'str'
    }

    attribute_map = {
        'conid': 'Conid',
        'exchange': 'Exchange',
        'v': 'V',
        't': 'T',
        'tt': 'TT',
        'p': 'P'
    }

    def __init__(self, conid=None, exchange=None, v=None, t=None, tt=None, p=None):  # noqa: E501
        """StatsData - a model defined in Swagger"""  # noqa: E501

        self._conid = None
        self._exchange = None
        self._v = None
        self._t = None
        self._tt = None
        self._p = None
        self.discriminator = None

        if conid is not None:
            self.conid = conid
        if exchange is not None:
            self.exchange = exchange
        if v is not None:
            self.v = v
        if t is not None:
            self.t = t
        if tt is not None:
            self.tt = tt
        if p is not None:
            self.p = p

    @property
    def conid(self):
        """Gets the conid of this StatsData.  # noqa: E501


        :return: The conid of this StatsData.  # noqa: E501
        :rtype: float
        """
        return self._conid

    @conid.setter
    def conid(self, conid):
        """Sets the conid of this StatsData.


        :param conid: The conid of this StatsData.  # noqa: E501
        :type: float
        """

        self._conid = conid

    @property
    def exchange(self):
        """Gets the exchange of this StatsData.  # noqa: E501


        :return: The exchange of this StatsData.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this StatsData.


        :param exchange: The exchange of this StatsData.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def v(self):
        """Gets the v of this StatsData.  # noqa: E501


        :return: The v of this StatsData.  # noqa: E501
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this StatsData.


        :param v: The v of this StatsData.  # noqa: E501
        :type: float
        """

        self._v = v

    @property
    def t(self):
        """Gets the t of this StatsData.  # noqa: E501


        :return: The t of this StatsData.  # noqa: E501
        :rtype: float
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this StatsData.


        :param t: The t of this StatsData.  # noqa: E501
        :type: float
        """

        self._t = t

    @property
    def tt(self):
        """Gets the tt of this StatsData.  # noqa: E501


        :return: The tt of this StatsData.  # noqa: E501
        :rtype: float
        """
        return self._tt

    @tt.setter
    def tt(self, tt):
        """Sets the tt of this StatsData.


        :param tt: The tt of this StatsData.  # noqa: E501
        :type: float
        """

        self._tt = tt

    @property
    def p(self):
        """Gets the p of this StatsData.  # noqa: E501

        Object, payload depends on event type. See confluence page for IGEvntUpd.  # noqa: E501

        :return: The p of this StatsData.  # noqa: E501
        :rtype: str
        """
        return self._p

    @p.setter
    def p(self, p):
        """Sets the p of this StatsData.

        Object, payload depends on event type. See confluence page for IGEvntUpd.  # noqa: E501

        :param p: The p of this StatsData.  # noqa: E501
        :type: str
        """

        self._p = p

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
        if issubclass(StatsData, dict):
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
        if not isinstance(other, StatsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
