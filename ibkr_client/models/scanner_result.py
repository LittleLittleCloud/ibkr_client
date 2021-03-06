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


class ScannerResult(object):
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
        'total': 'int',
        'size': 'int',
        'offset': 'int',
        'scan_time': 'str',
        'id': 'float',
        'position': 'str',
        'contracts': 'ScannerresultContracts'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'offset': 'offset',
        'scan_time': 'scanTime',
        'id': 'id',
        'position': 'position',
        'contracts': 'Contracts'
    }

    def __init__(self, total=None, size=None, offset=None, scan_time=None, id=None, position=None, contracts=None):  # noqa: E501
        """ScannerResult - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._size = None
        self._offset = None
        self._scan_time = None
        self._id = None
        self._position = None
        self._contracts = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if offset is not None:
            self.offset = offset
        if scan_time is not None:
            self.scan_time = scan_time
        if id is not None:
            self.id = id
        if position is not None:
            self.position = position
        if contracts is not None:
            self.contracts = contracts

    @property
    def total(self):
        """Gets the total of this ScannerResult.  # noqa: E501


        :return: The total of this ScannerResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ScannerResult.


        :param total: The total of this ScannerResult.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def size(self):
        """Gets the size of this ScannerResult.  # noqa: E501


        :return: The size of this ScannerResult.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ScannerResult.


        :param size: The size of this ScannerResult.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def offset(self):
        """Gets the offset of this ScannerResult.  # noqa: E501


        :return: The offset of this ScannerResult.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ScannerResult.


        :param offset: The offset of this ScannerResult.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def scan_time(self):
        """Gets the scan_time of this ScannerResult.  # noqa: E501


        :return: The scan_time of this ScannerResult.  # noqa: E501
        :rtype: str
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        """Sets the scan_time of this ScannerResult.


        :param scan_time: The scan_time of this ScannerResult.  # noqa: E501
        :type: str
        """

        self._scan_time = scan_time

    @property
    def id(self):
        """Gets the id of this ScannerResult.  # noqa: E501


        :return: The id of this ScannerResult.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScannerResult.


        :param id: The id of this ScannerResult.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def position(self):
        """Gets the position of this ScannerResult.  # noqa: E501


        :return: The position of this ScannerResult.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ScannerResult.


        :param position: The position of this ScannerResult.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def contracts(self):
        """Gets the contracts of this ScannerResult.  # noqa: E501


        :return: The contracts of this ScannerResult.  # noqa: E501
        :rtype: ScannerresultContracts
        """
        return self._contracts

    @contracts.setter
    def contracts(self, contracts):
        """Sets the contracts of this ScannerResult.


        :param contracts: The contracts of this ScannerResult.  # noqa: E501
        :type: ScannerresultContracts
        """

        self._contracts = contracts

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
        if issubclass(ScannerResult, dict):
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
        if not isinstance(other, ScannerResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
