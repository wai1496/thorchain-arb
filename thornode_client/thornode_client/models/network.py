# coding: utf-8

"""
    THORChain API

    This documentation outlines the API for THORChain.  NOTE: This document is a **work in progress**.  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from thornode_client.configuration import Configuration


class Network(object):
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
        'bond_reward_rune': 'str',
        'total_bond_units': 'str',
        'total_reserve': 'str',
        'burned_bep_2_rune': 'str',
        'burned_erc_20_rune': 'str'
    }

    attribute_map = {
        'bond_reward_rune': 'bond_reward_rune',
        'total_bond_units': 'total_bond_units',
        'total_reserve': 'total_reserve',
        'burned_bep_2_rune': 'burned_bep_2_rune',
        'burned_erc_20_rune': 'burned_erc_20_rune'
    }

    def __init__(self, bond_reward_rune=None, total_bond_units=None, total_reserve=None, burned_bep_2_rune=None, burned_erc_20_rune=None, _configuration=None):  # noqa: E501
        """Network - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bond_reward_rune = None
        self._total_bond_units = None
        self._total_reserve = None
        self._burned_bep_2_rune = None
        self._burned_erc_20_rune = None
        self.discriminator = None

        if bond_reward_rune is not None:
            self.bond_reward_rune = bond_reward_rune
        if total_bond_units is not None:
            self.total_bond_units = total_bond_units
        if total_reserve is not None:
            self.total_reserve = total_reserve
        if burned_bep_2_rune is not None:
            self.burned_bep_2_rune = burned_bep_2_rune
        if burned_erc_20_rune is not None:
            self.burned_erc_20_rune = burned_erc_20_rune

    @property
    def bond_reward_rune(self):
        """Gets the bond_reward_rune of this Network.  # noqa: E501

        total amount of awarded rune for node operators  # noqa: E501

        :return: The bond_reward_rune of this Network.  # noqa: E501
        :rtype: str
        """
        return self._bond_reward_rune

    @bond_reward_rune.setter
    def bond_reward_rune(self, bond_reward_rune):
        """Sets the bond_reward_rune of this Network.

        total amount of awarded rune for node operators  # noqa: E501

        :param bond_reward_rune: The bond_reward_rune of this Network.  # noqa: E501
        :type: str
        """

        self._bond_reward_rune = bond_reward_rune

    @property
    def total_bond_units(self):
        """Gets the total_bond_units of this Network.  # noqa: E501

        total amount of bond units  # noqa: E501

        :return: The total_bond_units of this Network.  # noqa: E501
        :rtype: str
        """
        return self._total_bond_units

    @total_bond_units.setter
    def total_bond_units(self, total_bond_units):
        """Sets the total_bond_units of this Network.

        total amount of bond units  # noqa: E501

        :param total_bond_units: The total_bond_units of this Network.  # noqa: E501
        :type: str
        """

        self._total_bond_units = total_bond_units

    @property
    def total_reserve(self):
        """Gets the total_reserve of this Network.  # noqa: E501

        total amount of reserve in rune  # noqa: E501

        :return: The total_reserve of this Network.  # noqa: E501
        :rtype: str
        """
        return self._total_reserve

    @total_reserve.setter
    def total_reserve(self, total_reserve):
        """Sets the total_reserve of this Network.

        total amount of reserve in rune  # noqa: E501

        :param total_reserve: The total_reserve of this Network.  # noqa: E501
        :type: str
        """

        self._total_reserve = total_reserve

    @property
    def burned_bep_2_rune(self):
        """Gets the burned_bep_2_rune of this Network.  # noqa: E501

        total amount of burned BEP2 rune to native rune  # noqa: E501

        :return: The burned_bep_2_rune of this Network.  # noqa: E501
        :rtype: str
        """
        return self._burned_bep_2_rune

    @burned_bep_2_rune.setter
    def burned_bep_2_rune(self, burned_bep_2_rune):
        """Sets the burned_bep_2_rune of this Network.

        total amount of burned BEP2 rune to native rune  # noqa: E501

        :param burned_bep_2_rune: The burned_bep_2_rune of this Network.  # noqa: E501
        :type: str
        """

        self._burned_bep_2_rune = burned_bep_2_rune

    @property
    def burned_erc_20_rune(self):
        """Gets the burned_erc_20_rune of this Network.  # noqa: E501

        total amount of burned ERC20 rune to native rune  # noqa: E501

        :return: The burned_erc_20_rune of this Network.  # noqa: E501
        :rtype: str
        """
        return self._burned_erc_20_rune

    @burned_erc_20_rune.setter
    def burned_erc_20_rune(self, burned_erc_20_rune):
        """Sets the burned_erc_20_rune of this Network.

        total amount of burned ERC20 rune to native rune  # noqa: E501

        :param burned_erc_20_rune: The burned_erc_20_rune of this Network.  # noqa: E501
        :type: str
        """

        self._burned_erc_20_rune = burned_erc_20_rune

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
        if issubclass(Network, dict):
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
        if not isinstance(other, Network):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Network):
            return True

        return self.to_dict() != other.to_dict()
