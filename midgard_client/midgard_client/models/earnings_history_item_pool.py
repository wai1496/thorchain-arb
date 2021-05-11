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

class EarningsHistoryItemPool(object):
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
        'asset_liquidity_fees': 'str',
        'earnings': 'str',
        'pool': 'str',
        'rewards': 'str',
        'rune_liquidity_fees': 'str',
        'total_liquidity_fees_rune': 'str'
    }

    attribute_map = {
        'asset_liquidity_fees': 'assetLiquidityFees',
        'earnings': 'earnings',
        'pool': 'pool',
        'rewards': 'rewards',
        'rune_liquidity_fees': 'runeLiquidityFees',
        'total_liquidity_fees_rune': 'totalLiquidityFeesRune'
    }

    def __init__(self, asset_liquidity_fees=None, earnings=None, pool=None, rewards=None, rune_liquidity_fees=None, total_liquidity_fees_rune=None):  # noqa: E501
        """EarningsHistoryItemPool - a model defined in Swagger"""  # noqa: E501
        self._asset_liquidity_fees = None
        self._earnings = None
        self._pool = None
        self._rewards = None
        self._rune_liquidity_fees = None
        self._total_liquidity_fees_rune = None
        self.discriminator = None
        self.asset_liquidity_fees = asset_liquidity_fees
        self.earnings = earnings
        self.pool = pool
        self.rewards = rewards
        self.rune_liquidity_fees = rune_liquidity_fees
        self.total_liquidity_fees_rune = total_liquidity_fees_rune

    @property
    def asset_liquidity_fees(self):
        """Gets the asset_liquidity_fees of this EarningsHistoryItemPool.  # noqa: E501

        Int64(e8), liquidity fees collected in the pool's asset  # noqa: E501

        :return: The asset_liquidity_fees of this EarningsHistoryItemPool.  # noqa: E501
        :rtype: str
        """
        return self._asset_liquidity_fees

    @asset_liquidity_fees.setter
    def asset_liquidity_fees(self, asset_liquidity_fees):
        """Sets the asset_liquidity_fees of this EarningsHistoryItemPool.

        Int64(e8), liquidity fees collected in the pool's asset  # noqa: E501

        :param asset_liquidity_fees: The asset_liquidity_fees of this EarningsHistoryItemPool.  # noqa: E501
        :type: str
        """
        if asset_liquidity_fees is None:
            raise ValueError("Invalid value for `asset_liquidity_fees`, must not be `None`")  # noqa: E501

        self._asset_liquidity_fees = asset_liquidity_fees

    @property
    def earnings(self):
        """Gets the earnings of this EarningsHistoryItemPool.  # noqa: E501

        Int64(e8), total earnings in RUNE (totalLiquidityFees + rewards)  # noqa: E501

        :return: The earnings of this EarningsHistoryItemPool.  # noqa: E501
        :rtype: str
        """
        return self._earnings

    @earnings.setter
    def earnings(self, earnings):
        """Sets the earnings of this EarningsHistoryItemPool.

        Int64(e8), total earnings in RUNE (totalLiquidityFees + rewards)  # noqa: E501

        :param earnings: The earnings of this EarningsHistoryItemPool.  # noqa: E501
        :type: str
        """
        if earnings is None:
            raise ValueError("Invalid value for `earnings`, must not be `None`")  # noqa: E501

        self._earnings = earnings

    @property
    def pool(self):
        """Gets the pool of this EarningsHistoryItemPool.  # noqa: E501

        asset for the given pool  # noqa: E501

        :return: The pool of this EarningsHistoryItemPool.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this EarningsHistoryItemPool.

        asset for the given pool  # noqa: E501

        :param pool: The pool of this EarningsHistoryItemPool.  # noqa: E501
        :type: str
        """
        if pool is None:
            raise ValueError("Invalid value for `pool`, must not be `None`")  # noqa: E501

        self._pool = pool

    @property
    def rewards(self):
        """Gets the rewards of this EarningsHistoryItemPool.  # noqa: E501

        Int64(e8), RUNE amount sent to (positive) or taken from (negative) the pool as a result of balancing it's share of system income each block   # noqa: E501

        :return: The rewards of this EarningsHistoryItemPool.  # noqa: E501
        :rtype: str
        """
        return self._rewards

    @rewards.setter
    def rewards(self, rewards):
        """Sets the rewards of this EarningsHistoryItemPool.

        Int64(e8), RUNE amount sent to (positive) or taken from (negative) the pool as a result of balancing it's share of system income each block   # noqa: E501

        :param rewards: The rewards of this EarningsHistoryItemPool.  # noqa: E501
        :type: str
        """
        if rewards is None:
            raise ValueError("Invalid value for `rewards`, must not be `None`")  # noqa: E501

        self._rewards = rewards

    @property
    def rune_liquidity_fees(self):
        """Gets the rune_liquidity_fees of this EarningsHistoryItemPool.  # noqa: E501

        Int64(e8), liquidity fees collected in RUNE  # noqa: E501

        :return: The rune_liquidity_fees of this EarningsHistoryItemPool.  # noqa: E501
        :rtype: str
        """
        return self._rune_liquidity_fees

    @rune_liquidity_fees.setter
    def rune_liquidity_fees(self, rune_liquidity_fees):
        """Sets the rune_liquidity_fees of this EarningsHistoryItemPool.

        Int64(e8), liquidity fees collected in RUNE  # noqa: E501

        :param rune_liquidity_fees: The rune_liquidity_fees of this EarningsHistoryItemPool.  # noqa: E501
        :type: str
        """
        if rune_liquidity_fees is None:
            raise ValueError("Invalid value for `rune_liquidity_fees`, must not be `None`")  # noqa: E501

        self._rune_liquidity_fees = rune_liquidity_fees

    @property
    def total_liquidity_fees_rune(self):
        """Gets the total_liquidity_fees_rune of this EarningsHistoryItemPool.  # noqa: E501

        Int64(e8), total liquidity fees (assetFees + runeFees) collected, shown in RUNE  # noqa: E501

        :return: The total_liquidity_fees_rune of this EarningsHistoryItemPool.  # noqa: E501
        :rtype: str
        """
        return self._total_liquidity_fees_rune

    @total_liquidity_fees_rune.setter
    def total_liquidity_fees_rune(self, total_liquidity_fees_rune):
        """Sets the total_liquidity_fees_rune of this EarningsHistoryItemPool.

        Int64(e8), total liquidity fees (assetFees + runeFees) collected, shown in RUNE  # noqa: E501

        :param total_liquidity_fees_rune: The total_liquidity_fees_rune of this EarningsHistoryItemPool.  # noqa: E501
        :type: str
        """
        if total_liquidity_fees_rune is None:
            raise ValueError("Invalid value for `total_liquidity_fees_rune`, must not be `None`")  # noqa: E501

        self._total_liquidity_fees_rune = total_liquidity_fees_rune

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
        if issubclass(EarningsHistoryItemPool, dict):
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
        if not isinstance(other, EarningsHistoryItemPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
