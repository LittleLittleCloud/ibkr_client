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


class Transactions(object):
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
        'id': 'str',
        'currency': 'str',
        'includes_real_time': 'bool',
        '_from': 'float',
        'to': 'float',
        'transactions': 'list[TransactionsTransactions]'
    }

    attribute_map = {
        'id': 'id',
        'currency': 'currency',
        'includes_real_time': 'includesRealTime',
        '_from': 'from',
        'to': 'to',
        'transactions': 'transactions'
    }

    def __init__(self, id=None, currency=None, includes_real_time=None, _from=None, to=None, transactions=None):  # noqa: E501
        """Transactions - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._currency = None
        self._includes_real_time = None
        self.__from = None
        self._to = None
        self._transactions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if currency is not None:
            self.currency = currency
        if includes_real_time is not None:
            self.includes_real_time = includes_real_time
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if transactions is not None:
            self.transactions = transactions

    @property
    def id(self):
        """Gets the id of this Transactions.  # noqa: E501

        will always be getTransactions  # noqa: E501

        :return: The id of this Transactions.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transactions.

        will always be getTransactions  # noqa: E501

        :param id: The id of this Transactions.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def currency(self):
        """Gets the currency of this Transactions.  # noqa: E501

        same as request  # noqa: E501

        :return: The currency of this Transactions.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Transactions.

        same as request  # noqa: E501

        :param currency: The currency of this Transactions.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def includes_real_time(self):
        """Gets the includes_real_time of this Transactions.  # noqa: E501

        Indicates whether current day and realtime data is included in the result  # noqa: E501

        :return: The includes_real_time of this Transactions.  # noqa: E501
        :rtype: bool
        """
        return self._includes_real_time

    @includes_real_time.setter
    def includes_real_time(self, includes_real_time):
        """Sets the includes_real_time of this Transactions.

        Indicates whether current day and realtime data is included in the result  # noqa: E501

        :param includes_real_time: The includes_real_time of this Transactions.  # noqa: E501
        :type: bool
        """

        self._includes_real_time = includes_real_time

    @property
    def _from(self):
        """Gets the _from of this Transactions.  # noqa: E501

        Period start date. Epoch time, GMT  # noqa: E501

        :return: The _from of this Transactions.  # noqa: E501
        :rtype: float
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Transactions.

        Period start date. Epoch time, GMT  # noqa: E501

        :param _from: The _from of this Transactions.  # noqa: E501
        :type: float
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this Transactions.  # noqa: E501

        Period end date. Epoch time, GMT  # noqa: E501

        :return: The to of this Transactions.  # noqa: E501
        :rtype: float
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Transactions.

        Period end date. Epoch time, GMT  # noqa: E501

        :param to: The to of this Transactions.  # noqa: E501
        :type: float
        """

        self._to = to

    @property
    def transactions(self):
        """Gets the transactions of this Transactions.  # noqa: E501

        Sorted by date descending  # noqa: E501

        :return: The transactions of this Transactions.  # noqa: E501
        :rtype: list[TransactionsTransactions]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this Transactions.

        Sorted by date descending  # noqa: E501

        :param transactions: The transactions of this Transactions.  # noqa: E501
        :type: list[TransactionsTransactions]
        """

        self._transactions = transactions

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
        if issubclass(Transactions, dict):
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
        if not isinstance(other, Transactions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other