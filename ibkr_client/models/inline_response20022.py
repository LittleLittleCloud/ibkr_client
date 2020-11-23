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


class InlineResponse20022(object):
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
        'conid': 'int',
        'company_header': 'str',
        'company_name': 'str',
        'symbol': 'str',
        'description': 'str',
        'restricted': 'str',
        'fop': 'str',
        'opt': 'str',
        'war': 'str',
        'sections': 'list[IserversecdefsearchSections]'
    }

    attribute_map = {
        'conid': 'conid',
        'company_header': 'companyHeader',
        'company_name': 'companyName',
        'symbol': 'symbol',
        'description': 'description',
        'restricted': 'restricted',
        'fop': 'fop',
        'opt': 'opt',
        'war': 'war',
        'sections': 'sections'
    }

    def __init__(self, conid=None, company_header=None, company_name=None, symbol=None, description=None, restricted=None, fop=None, opt=None, war=None, sections=None):  # noqa: E501
        """InlineResponse20022 - a model defined in Swagger"""  # noqa: E501

        self._conid = None
        self._company_header = None
        self._company_name = None
        self._symbol = None
        self._description = None
        self._restricted = None
        self._fop = None
        self._opt = None
        self._war = None
        self._sections = None
        self.discriminator = None

        if conid is not None:
            self.conid = conid
        if company_header is not None:
            self.company_header = company_header
        if company_name is not None:
            self.company_name = company_name
        if symbol is not None:
            self.symbol = symbol
        if description is not None:
            self.description = description
        if restricted is not None:
            self.restricted = restricted
        if fop is not None:
            self.fop = fop
        if opt is not None:
            self.opt = opt
        if war is not None:
            self.war = war
        if sections is not None:
            self.sections = sections

    @property
    def conid(self):
        """Gets the conid of this InlineResponse20022.  # noqa: E501

        Contract Identifier  # noqa: E501

        :return: The conid of this InlineResponse20022.  # noqa: E501
        :rtype: int
        """
        return self._conid

    @conid.setter
    def conid(self, conid):
        """Sets the conid of this InlineResponse20022.

        Contract Identifier  # noqa: E501

        :param conid: The conid of this InlineResponse20022.  # noqa: E501
        :type: int
        """

        self._conid = conid

    @property
    def company_header(self):
        """Gets the company_header of this InlineResponse20022.  # noqa: E501

        Company Name - Exchange  # noqa: E501

        :return: The company_header of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._company_header

    @company_header.setter
    def company_header(self, company_header):
        """Sets the company_header of this InlineResponse20022.

        Company Name - Exchange  # noqa: E501

        :param company_header: The company_header of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._company_header = company_header

    @property
    def company_name(self):
        """Gets the company_name of this InlineResponse20022.  # noqa: E501


        :return: The company_name of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this InlineResponse20022.


        :param company_name: The company_name of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def symbol(self):
        """Gets the symbol of this InlineResponse20022.  # noqa: E501


        :return: The symbol of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this InlineResponse20022.


        :param symbol: The symbol of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def description(self):
        """Gets the description of this InlineResponse20022.  # noqa: E501

        Exchange  # noqa: E501

        :return: The description of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20022.

        Exchange  # noqa: E501

        :param description: The description of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def restricted(self):
        """Gets the restricted of this InlineResponse20022.  # noqa: E501


        :return: The restricted of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """Sets the restricted of this InlineResponse20022.


        :param restricted: The restricted of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._restricted = restricted

    @property
    def fop(self):
        """Gets the fop of this InlineResponse20022.  # noqa: E501


        :return: The fop of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._fop

    @fop.setter
    def fop(self, fop):
        """Sets the fop of this InlineResponse20022.


        :param fop: The fop of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._fop = fop

    @property
    def opt(self):
        """Gets the opt of this InlineResponse20022.  # noqa: E501


        :return: The opt of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._opt

    @opt.setter
    def opt(self, opt):
        """Sets the opt of this InlineResponse20022.


        :param opt: The opt of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._opt = opt

    @property
    def war(self):
        """Gets the war of this InlineResponse20022.  # noqa: E501


        :return: The war of this InlineResponse20022.  # noqa: E501
        :rtype: str
        """
        return self._war

    @war.setter
    def war(self, war):
        """Sets the war of this InlineResponse20022.


        :param war: The war of this InlineResponse20022.  # noqa: E501
        :type: str
        """

        self._war = war

    @property
    def sections(self):
        """Gets the sections of this InlineResponse20022.  # noqa: E501


        :return: The sections of this InlineResponse20022.  # noqa: E501
        :rtype: list[IserversecdefsearchSections]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this InlineResponse20022.


        :param sections: The sections of this InlineResponse20022.  # noqa: E501
        :type: list[IserversecdefsearchSections]
        """

        self._sections = sections

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
        if issubclass(InlineResponse20022, dict):
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
        if not isinstance(other, InlineResponse20022):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other