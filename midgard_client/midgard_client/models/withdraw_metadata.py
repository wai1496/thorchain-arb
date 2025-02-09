# coding: utf-8

"""
    Midgard Public API

    The Midgard Public API queries THORChain and any chains linked via the Bifröst and prepares information about the network to be readily available for public users. The API parses transaction event data from THORChain and stores them in a time-series database to make time-dependent queries easy. Midgard does not hold critical information. To interact with BEPSwap and Asgardex, users should query THORChain directly.  # noqa: E501

    OpenAPI spec version: 2.1.0
    Contact: devs@thorchain.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WithdrawMetadata(object):
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
        'asymmetry': 'str',
        'basis_points': 'str',
        'liquidity_units': 'str',
        'network_fees': 'NetworkFees'
    }

    attribute_map = {
        'asymmetry': 'asymmetry',
        'basis_points': 'basisPoints',
        'liquidity_units': 'liquidityUnits',
        'network_fees': 'networkFees'
    }

    def __init__(self, asymmetry=None, basis_points=None, liquidity_units=None, network_fees=None):  # noqa: E501
        """WithdrawMetadata - a model defined in Swagger"""  # noqa: E501
        self._asymmetry = None
        self._basis_points = None
        self._liquidity_units = None
        self._network_fees = None
        self.discriminator = None
        self.asymmetry = asymmetry
        self.basis_points = basis_points
        self.liquidity_units = liquidity_units
        self.network_fees = network_fees

    @property
    def asymmetry(self):
        """Gets the asymmetry of this WithdrawMetadata.  # noqa: E501

        Decimal (-1.0 <=> 1.0), indicates how assymetrical the withdrawal was. 0 means totally symetrical  # noqa: E501

        :return: The asymmetry of this WithdrawMetadata.  # noqa: E501
        :rtype: str
        """
        return self._asymmetry

    @asymmetry.setter
    def asymmetry(self, asymmetry):
        """Sets the asymmetry of this WithdrawMetadata.

        Decimal (-1.0 <=> 1.0), indicates how assymetrical the withdrawal was. 0 means totally symetrical  # noqa: E501

        :param asymmetry: The asymmetry of this WithdrawMetadata.  # noqa: E501
        :type: str
        """
        if asymmetry is None:
            raise ValueError("Invalid value for `asymmetry`, must not be `None`")  # noqa: E501

        self._asymmetry = asymmetry

    @property
    def basis_points(self):
        """Gets the basis_points of this WithdrawMetadata.  # noqa: E501

        Int64 (Basis points, 0-10000, where 10000=100%), percentage of total pool ownership withdrawn  # noqa: E501

        :return: The basis_points of this WithdrawMetadata.  # noqa: E501
        :rtype: str
        """
        return self._basis_points

    @basis_points.setter
    def basis_points(self, basis_points):
        """Sets the basis_points of this WithdrawMetadata.

        Int64 (Basis points, 0-10000, where 10000=100%), percentage of total pool ownership withdrawn  # noqa: E501

        :param basis_points: The basis_points of this WithdrawMetadata.  # noqa: E501
        :type: str
        """
        if basis_points is None:
            raise ValueError("Invalid value for `basis_points`, must not be `None`")  # noqa: E501

        self._basis_points = basis_points

    @property
    def liquidity_units(self):
        """Gets the liquidity_units of this WithdrawMetadata.  # noqa: E501

        Int64, amount of liquidity units removed from the member as result of the withdrawal  # noqa: E501

        :return: The liquidity_units of this WithdrawMetadata.  # noqa: E501
        :rtype: str
        """
        return self._liquidity_units

    @liquidity_units.setter
    def liquidity_units(self, liquidity_units):
        """Sets the liquidity_units of this WithdrawMetadata.

        Int64, amount of liquidity units removed from the member as result of the withdrawal  # noqa: E501

        :param liquidity_units: The liquidity_units of this WithdrawMetadata.  # noqa: E501
        :type: str
        """
        if liquidity_units is None:
            raise ValueError("Invalid value for `liquidity_units`, must not be `None`")  # noqa: E501

        self._liquidity_units = liquidity_units

    @property
    def network_fees(self):
        """Gets the network_fees of this WithdrawMetadata.  # noqa: E501


        :return: The network_fees of this WithdrawMetadata.  # noqa: E501
        :rtype: NetworkFees
        """
        return self._network_fees

    @network_fees.setter
    def network_fees(self, network_fees):
        """Sets the network_fees of this WithdrawMetadata.


        :param network_fees: The network_fees of this WithdrawMetadata.  # noqa: E501
        :type: NetworkFees
        """
        if network_fees is None:
            raise ValueError("Invalid value for `network_fees`, must not be `None`")  # noqa: E501

        self._network_fees = network_fees

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
        if issubclass(WithdrawMetadata, dict):
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
        if not isinstance(other, WithdrawMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
