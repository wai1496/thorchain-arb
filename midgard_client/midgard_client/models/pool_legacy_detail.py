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

class PoolLegacyDetail(object):
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
        'asset': 'str',
        'asset_depth': 'str',
        'asset_staked_total': 'str',
        'buy_asset_count': 'str',
        'buy_fee_average': 'str',
        'buy_fees_total': 'str',
        'buy_slip_average': 'str',
        'buy_tx_average': 'str',
        'buy_volume': 'str',
        'pool_apy': 'str',
        'pool_depth': 'str',
        'pool_fee_average': 'str',
        'pool_fees_total': 'str',
        'pool_slip_average': 'str',
        'pool_staked_total': 'str',
        'pool_tx_average': 'str',
        'pool_units': 'str',
        'pool_volume': 'str',
        'price': 'str',
        'rune_depth': 'str',
        'rune_staked_total': 'str',
        'sell_asset_count': 'str',
        'sell_fee_average': 'str',
        'sell_fees_total': 'str',
        'sell_slip_average': 'str',
        'sell_tx_average': 'str',
        'sell_volume': 'str',
        'stake_tx_count': 'str',
        'stakers_count': 'str',
        'staking_tx_count': 'str',
        'status': 'str',
        'swappers_count': 'str',
        'swapping_tx_count': 'str',
        'volume24h': 'str',
        'withdraw_tx_count': 'str'
    }

    attribute_map = {
        'asset': 'asset',
        'asset_depth': 'assetDepth',
        'asset_staked_total': 'assetStakedTotal',
        'buy_asset_count': 'buyAssetCount',
        'buy_fee_average': 'buyFeeAverage',
        'buy_fees_total': 'buyFeesTotal',
        'buy_slip_average': 'buySlipAverage',
        'buy_tx_average': 'buyTxAverage',
        'buy_volume': 'buyVolume',
        'pool_apy': 'poolAPY',
        'pool_depth': 'poolDepth',
        'pool_fee_average': 'poolFeeAverage',
        'pool_fees_total': 'poolFeesTotal',
        'pool_slip_average': 'poolSlipAverage',
        'pool_staked_total': 'poolStakedTotal',
        'pool_tx_average': 'poolTxAverage',
        'pool_units': 'poolUnits',
        'pool_volume': 'poolVolume',
        'price': 'price',
        'rune_depth': 'runeDepth',
        'rune_staked_total': 'runeStakedTotal',
        'sell_asset_count': 'sellAssetCount',
        'sell_fee_average': 'sellFeeAverage',
        'sell_fees_total': 'sellFeesTotal',
        'sell_slip_average': 'sellSlipAverage',
        'sell_tx_average': 'sellTxAverage',
        'sell_volume': 'sellVolume',
        'stake_tx_count': 'stakeTxCount',
        'stakers_count': 'stakersCount',
        'staking_tx_count': 'stakingTxCount',
        'status': 'status',
        'swappers_count': 'swappersCount',
        'swapping_tx_count': 'swappingTxCount',
        'volume24h': 'volume24h',
        'withdraw_tx_count': 'withdrawTxCount'
    }

    def __init__(self, asset=None, asset_depth=None, asset_staked_total=None, buy_asset_count=None, buy_fee_average=None, buy_fees_total=None, buy_slip_average=None, buy_tx_average=None, buy_volume=None, pool_apy=None, pool_depth=None, pool_fee_average=None, pool_fees_total=None, pool_slip_average=None, pool_staked_total=None, pool_tx_average=None, pool_units=None, pool_volume=None, price=None, rune_depth=None, rune_staked_total=None, sell_asset_count=None, sell_fee_average=None, sell_fees_total=None, sell_slip_average=None, sell_tx_average=None, sell_volume=None, stake_tx_count=None, stakers_count=None, staking_tx_count=None, status=None, swappers_count=None, swapping_tx_count=None, volume24h=None, withdraw_tx_count=None):  # noqa: E501
        """PoolLegacyDetail - a model defined in Swagger"""  # noqa: E501
        self._asset = None
        self._asset_depth = None
        self._asset_staked_total = None
        self._buy_asset_count = None
        self._buy_fee_average = None
        self._buy_fees_total = None
        self._buy_slip_average = None
        self._buy_tx_average = None
        self._buy_volume = None
        self._pool_apy = None
        self._pool_depth = None
        self._pool_fee_average = None
        self._pool_fees_total = None
        self._pool_slip_average = None
        self._pool_staked_total = None
        self._pool_tx_average = None
        self._pool_units = None
        self._pool_volume = None
        self._price = None
        self._rune_depth = None
        self._rune_staked_total = None
        self._sell_asset_count = None
        self._sell_fee_average = None
        self._sell_fees_total = None
        self._sell_slip_average = None
        self._sell_tx_average = None
        self._sell_volume = None
        self._stake_tx_count = None
        self._stakers_count = None
        self._staking_tx_count = None
        self._status = None
        self._swappers_count = None
        self._swapping_tx_count = None
        self._volume24h = None
        self._withdraw_tx_count = None
        self.discriminator = None
        self.asset = asset
        self.asset_depth = asset_depth
        self.asset_staked_total = asset_staked_total
        self.buy_asset_count = buy_asset_count
        self.buy_fee_average = buy_fee_average
        self.buy_fees_total = buy_fees_total
        self.buy_slip_average = buy_slip_average
        self.buy_tx_average = buy_tx_average
        self.buy_volume = buy_volume
        self.pool_apy = pool_apy
        self.pool_depth = pool_depth
        self.pool_fee_average = pool_fee_average
        self.pool_fees_total = pool_fees_total
        self.pool_slip_average = pool_slip_average
        self.pool_staked_total = pool_staked_total
        self.pool_tx_average = pool_tx_average
        self.pool_units = pool_units
        self.pool_volume = pool_volume
        self.price = price
        self.rune_depth = rune_depth
        self.rune_staked_total = rune_staked_total
        self.sell_asset_count = sell_asset_count
        self.sell_fee_average = sell_fee_average
        self.sell_fees_total = sell_fees_total
        self.sell_slip_average = sell_slip_average
        self.sell_tx_average = sell_tx_average
        self.sell_volume = sell_volume
        self.stake_tx_count = stake_tx_count
        self.stakers_count = stakers_count
        self.staking_tx_count = staking_tx_count
        self.status = status
        self.swappers_count = swappers_count
        self.swapping_tx_count = swapping_tx_count
        self.volume24h = volume24h
        self.withdraw_tx_count = withdraw_tx_count

    @property
    def asset(self):
        """Gets the asset of this PoolLegacyDetail.  # noqa: E501


        :return: The asset of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this PoolLegacyDetail.


        :param asset: The asset of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if asset is None:
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def asset_depth(self):
        """Gets the asset_depth of this PoolLegacyDetail.  # noqa: E501

        same as assetDepth from pool/stats  # noqa: E501

        :return: The asset_depth of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._asset_depth

    @asset_depth.setter
    def asset_depth(self, asset_depth):
        """Sets the asset_depth of this PoolLegacyDetail.

        same as assetDepth from pool/stats  # noqa: E501

        :param asset_depth: The asset_depth of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if asset_depth is None:
            raise ValueError("Invalid value for `asset_depth`, must not be `None`")  # noqa: E501

        self._asset_depth = asset_depth

    @property
    def asset_staked_total(self):
        """Gets the asset_staked_total of this PoolLegacyDetail.  # noqa: E501

        same as addAssetLiquidityVolume from pool/stats  # noqa: E501

        :return: The asset_staked_total of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._asset_staked_total

    @asset_staked_total.setter
    def asset_staked_total(self, asset_staked_total):
        """Sets the asset_staked_total of this PoolLegacyDetail.

        same as addAssetLiquidityVolume from pool/stats  # noqa: E501

        :param asset_staked_total: The asset_staked_total of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if asset_staked_total is None:
            raise ValueError("Invalid value for `asset_staked_total`, must not be `None`")  # noqa: E501

        self._asset_staked_total = asset_staked_total

    @property
    def buy_asset_count(self):
        """Gets the buy_asset_count of this PoolLegacyDetail.  # noqa: E501

        same as toAssetCount from pool/stats  # noqa: E501

        :return: The buy_asset_count of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._buy_asset_count

    @buy_asset_count.setter
    def buy_asset_count(self, buy_asset_count):
        """Sets the buy_asset_count of this PoolLegacyDetail.

        same as toAssetCount from pool/stats  # noqa: E501

        :param buy_asset_count: The buy_asset_count of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if buy_asset_count is None:
            raise ValueError("Invalid value for `buy_asset_count`, must not be `None`")  # noqa: E501

        self._buy_asset_count = buy_asset_count

    @property
    def buy_fee_average(self):
        """Gets the buy_fee_average of this PoolLegacyDetail.  # noqa: E501

        same as toAssetFees / toAssetCount from pool/stats  # noqa: E501

        :return: The buy_fee_average of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._buy_fee_average

    @buy_fee_average.setter
    def buy_fee_average(self, buy_fee_average):
        """Sets the buy_fee_average of this PoolLegacyDetail.

        same as toAssetFees / toAssetCount from pool/stats  # noqa: E501

        :param buy_fee_average: The buy_fee_average of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if buy_fee_average is None:
            raise ValueError("Invalid value for `buy_fee_average`, must not be `None`")  # noqa: E501

        self._buy_fee_average = buy_fee_average

    @property
    def buy_fees_total(self):
        """Gets the buy_fees_total of this PoolLegacyDetail.  # noqa: E501

        same as toAssetFees from pool/stats  # noqa: E501

        :return: The buy_fees_total of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._buy_fees_total

    @buy_fees_total.setter
    def buy_fees_total(self, buy_fees_total):
        """Sets the buy_fees_total of this PoolLegacyDetail.

        same as toAssetFees from pool/stats  # noqa: E501

        :param buy_fees_total: The buy_fees_total of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if buy_fees_total is None:
            raise ValueError("Invalid value for `buy_fees_total`, must not be `None`")  # noqa: E501

        self._buy_fees_total = buy_fees_total

    @property
    def buy_slip_average(self):
        """Gets the buy_slip_average of this PoolLegacyDetail.  # noqa: E501

        same as toAssetAverageSlip from pool/stats  # noqa: E501

        :return: The buy_slip_average of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._buy_slip_average

    @buy_slip_average.setter
    def buy_slip_average(self, buy_slip_average):
        """Sets the buy_slip_average of this PoolLegacyDetail.

        same as toAssetAverageSlip from pool/stats  # noqa: E501

        :param buy_slip_average: The buy_slip_average of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if buy_slip_average is None:
            raise ValueError("Invalid value for `buy_slip_average`, must not be `None`")  # noqa: E501

        self._buy_slip_average = buy_slip_average

    @property
    def buy_tx_average(self):
        """Gets the buy_tx_average of this PoolLegacyDetail.  # noqa: E501

        same as toAssetVolume / toAssetCount from pool/stats  # noqa: E501

        :return: The buy_tx_average of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._buy_tx_average

    @buy_tx_average.setter
    def buy_tx_average(self, buy_tx_average):
        """Sets the buy_tx_average of this PoolLegacyDetail.

        same as toAssetVolume / toAssetCount from pool/stats  # noqa: E501

        :param buy_tx_average: The buy_tx_average of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if buy_tx_average is None:
            raise ValueError("Invalid value for `buy_tx_average`, must not be `None`")  # noqa: E501

        self._buy_tx_average = buy_tx_average

    @property
    def buy_volume(self):
        """Gets the buy_volume of this PoolLegacyDetail.  # noqa: E501

        same as toAssetVolume from pool/stats  # noqa: E501

        :return: The buy_volume of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._buy_volume

    @buy_volume.setter
    def buy_volume(self, buy_volume):
        """Sets the buy_volume of this PoolLegacyDetail.

        same as toAssetVolume from pool/stats  # noqa: E501

        :param buy_volume: The buy_volume of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if buy_volume is None:
            raise ValueError("Invalid value for `buy_volume`, must not be `None`")  # noqa: E501

        self._buy_volume = buy_volume

    @property
    def pool_apy(self):
        """Gets the pool_apy of this PoolLegacyDetail.  # noqa: E501

        Float, Average Percentage Yield: annual return estimated using last weeks income, taking compound interest into account.  # noqa: E501

        :return: The pool_apy of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_apy

    @pool_apy.setter
    def pool_apy(self, pool_apy):
        """Sets the pool_apy of this PoolLegacyDetail.

        Float, Average Percentage Yield: annual return estimated using last weeks income, taking compound interest into account.  # noqa: E501

        :param pool_apy: The pool_apy of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if pool_apy is None:
            raise ValueError("Invalid value for `pool_apy`, must not be `None`")  # noqa: E501

        self._pool_apy = pool_apy

    @property
    def pool_depth(self):
        """Gets the pool_depth of this PoolLegacyDetail.  # noqa: E501

        same as 2*runeDepth from pool/stats  # noqa: E501

        :return: The pool_depth of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_depth

    @pool_depth.setter
    def pool_depth(self, pool_depth):
        """Sets the pool_depth of this PoolLegacyDetail.

        same as 2*runeDepth from pool/stats  # noqa: E501

        :param pool_depth: The pool_depth of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if pool_depth is None:
            raise ValueError("Invalid value for `pool_depth`, must not be `None`")  # noqa: E501

        self._pool_depth = pool_depth

    @property
    def pool_fee_average(self):
        """Gets the pool_fee_average of this PoolLegacyDetail.  # noqa: E501

        same as totalFees / swapCount from pool/stats  # noqa: E501

        :return: The pool_fee_average of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_fee_average

    @pool_fee_average.setter
    def pool_fee_average(self, pool_fee_average):
        """Sets the pool_fee_average of this PoolLegacyDetail.

        same as totalFees / swapCount from pool/stats  # noqa: E501

        :param pool_fee_average: The pool_fee_average of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if pool_fee_average is None:
            raise ValueError("Invalid value for `pool_fee_average`, must not be `None`")  # noqa: E501

        self._pool_fee_average = pool_fee_average

    @property
    def pool_fees_total(self):
        """Gets the pool_fees_total of this PoolLegacyDetail.  # noqa: E501

        same as totalFees from pool/stats  # noqa: E501

        :return: The pool_fees_total of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_fees_total

    @pool_fees_total.setter
    def pool_fees_total(self, pool_fees_total):
        """Sets the pool_fees_total of this PoolLegacyDetail.

        same as totalFees from pool/stats  # noqa: E501

        :param pool_fees_total: The pool_fees_total of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if pool_fees_total is None:
            raise ValueError("Invalid value for `pool_fees_total`, must not be `None`")  # noqa: E501

        self._pool_fees_total = pool_fees_total

    @property
    def pool_slip_average(self):
        """Gets the pool_slip_average of this PoolLegacyDetail.  # noqa: E501

        same as averageSlip from pool/stats  # noqa: E501

        :return: The pool_slip_average of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_slip_average

    @pool_slip_average.setter
    def pool_slip_average(self, pool_slip_average):
        """Sets the pool_slip_average of this PoolLegacyDetail.

        same as averageSlip from pool/stats  # noqa: E501

        :param pool_slip_average: The pool_slip_average of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if pool_slip_average is None:
            raise ValueError("Invalid value for `pool_slip_average`, must not be `None`")  # noqa: E501

        self._pool_slip_average = pool_slip_average

    @property
    def pool_staked_total(self):
        """Gets the pool_staked_total of this PoolLegacyDetail.  # noqa: E501

        same as addLiquidityVolume from pool/stats  # noqa: E501

        :return: The pool_staked_total of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_staked_total

    @pool_staked_total.setter
    def pool_staked_total(self, pool_staked_total):
        """Sets the pool_staked_total of this PoolLegacyDetail.

        same as addLiquidityVolume from pool/stats  # noqa: E501

        :param pool_staked_total: The pool_staked_total of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if pool_staked_total is None:
            raise ValueError("Invalid value for `pool_staked_total`, must not be `None`")  # noqa: E501

        self._pool_staked_total = pool_staked_total

    @property
    def pool_tx_average(self):
        """Gets the pool_tx_average of this PoolLegacyDetail.  # noqa: E501

        same as swapVolume / swapCount from pool/stats  # noqa: E501

        :return: The pool_tx_average of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_tx_average

    @pool_tx_average.setter
    def pool_tx_average(self, pool_tx_average):
        """Sets the pool_tx_average of this PoolLegacyDetail.

        same as swapVolume / swapCount from pool/stats  # noqa: E501

        :param pool_tx_average: The pool_tx_average of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if pool_tx_average is None:
            raise ValueError("Invalid value for `pool_tx_average`, must not be `None`")  # noqa: E501

        self._pool_tx_average = pool_tx_average

    @property
    def pool_units(self):
        """Gets the pool_units of this PoolLegacyDetail.  # noqa: E501

        same as units from pool/stats  # noqa: E501

        :return: The pool_units of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_units

    @pool_units.setter
    def pool_units(self, pool_units):
        """Sets the pool_units of this PoolLegacyDetail.

        same as units from pool/stats  # noqa: E501

        :param pool_units: The pool_units of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if pool_units is None:
            raise ValueError("Invalid value for `pool_units`, must not be `None`")  # noqa: E501

        self._pool_units = pool_units

    @property
    def pool_volume(self):
        """Gets the pool_volume of this PoolLegacyDetail.  # noqa: E501

        Int64(e8), same as buyVolume + sellVolume  # noqa: E501

        :return: The pool_volume of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._pool_volume

    @pool_volume.setter
    def pool_volume(self, pool_volume):
        """Sets the pool_volume of this PoolLegacyDetail.

        Int64(e8), same as buyVolume + sellVolume  # noqa: E501

        :param pool_volume: The pool_volume of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if pool_volume is None:
            raise ValueError("Invalid value for `pool_volume`, must not be `None`")  # noqa: E501

        self._pool_volume = pool_volume

    @property
    def price(self):
        """Gets the price of this PoolLegacyDetail.  # noqa: E501

        same as assetPrice from pool/stats  # noqa: E501

        :return: The price of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PoolLegacyDetail.

        same as assetPrice from pool/stats  # noqa: E501

        :param price: The price of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def rune_depth(self):
        """Gets the rune_depth of this PoolLegacyDetail.  # noqa: E501

        same as runeDepth from pool/stats  # noqa: E501

        :return: The rune_depth of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._rune_depth

    @rune_depth.setter
    def rune_depth(self, rune_depth):
        """Sets the rune_depth of this PoolLegacyDetail.

        same as runeDepth from pool/stats  # noqa: E501

        :param rune_depth: The rune_depth of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if rune_depth is None:
            raise ValueError("Invalid value for `rune_depth`, must not be `None`")  # noqa: E501

        self._rune_depth = rune_depth

    @property
    def rune_staked_total(self):
        """Gets the rune_staked_total of this PoolLegacyDetail.  # noqa: E501

        same as addRuneLiquidityVolume from pool/stats  # noqa: E501

        :return: The rune_staked_total of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._rune_staked_total

    @rune_staked_total.setter
    def rune_staked_total(self, rune_staked_total):
        """Sets the rune_staked_total of this PoolLegacyDetail.

        same as addRuneLiquidityVolume from pool/stats  # noqa: E501

        :param rune_staked_total: The rune_staked_total of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if rune_staked_total is None:
            raise ValueError("Invalid value for `rune_staked_total`, must not be `None`")  # noqa: E501

        self._rune_staked_total = rune_staked_total

    @property
    def sell_asset_count(self):
        """Gets the sell_asset_count of this PoolLegacyDetail.  # noqa: E501

        same as toRuneCount from pool/stats  # noqa: E501

        :return: The sell_asset_count of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._sell_asset_count

    @sell_asset_count.setter
    def sell_asset_count(self, sell_asset_count):
        """Sets the sell_asset_count of this PoolLegacyDetail.

        same as toRuneCount from pool/stats  # noqa: E501

        :param sell_asset_count: The sell_asset_count of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if sell_asset_count is None:
            raise ValueError("Invalid value for `sell_asset_count`, must not be `None`")  # noqa: E501

        self._sell_asset_count = sell_asset_count

    @property
    def sell_fee_average(self):
        """Gets the sell_fee_average of this PoolLegacyDetail.  # noqa: E501

        same as toRuneFees / toRuneCount from pool/stats  # noqa: E501

        :return: The sell_fee_average of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._sell_fee_average

    @sell_fee_average.setter
    def sell_fee_average(self, sell_fee_average):
        """Sets the sell_fee_average of this PoolLegacyDetail.

        same as toRuneFees / toRuneCount from pool/stats  # noqa: E501

        :param sell_fee_average: The sell_fee_average of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if sell_fee_average is None:
            raise ValueError("Invalid value for `sell_fee_average`, must not be `None`")  # noqa: E501

        self._sell_fee_average = sell_fee_average

    @property
    def sell_fees_total(self):
        """Gets the sell_fees_total of this PoolLegacyDetail.  # noqa: E501

        same as toRuneFees from pool/stats  # noqa: E501

        :return: The sell_fees_total of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._sell_fees_total

    @sell_fees_total.setter
    def sell_fees_total(self, sell_fees_total):
        """Sets the sell_fees_total of this PoolLegacyDetail.

        same as toRuneFees from pool/stats  # noqa: E501

        :param sell_fees_total: The sell_fees_total of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if sell_fees_total is None:
            raise ValueError("Invalid value for `sell_fees_total`, must not be `None`")  # noqa: E501

        self._sell_fees_total = sell_fees_total

    @property
    def sell_slip_average(self):
        """Gets the sell_slip_average of this PoolLegacyDetail.  # noqa: E501

        same as toRuneAverageSlip from pool/stats  # noqa: E501

        :return: The sell_slip_average of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._sell_slip_average

    @sell_slip_average.setter
    def sell_slip_average(self, sell_slip_average):
        """Sets the sell_slip_average of this PoolLegacyDetail.

        same as toRuneAverageSlip from pool/stats  # noqa: E501

        :param sell_slip_average: The sell_slip_average of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if sell_slip_average is None:
            raise ValueError("Invalid value for `sell_slip_average`, must not be `None`")  # noqa: E501

        self._sell_slip_average = sell_slip_average

    @property
    def sell_tx_average(self):
        """Gets the sell_tx_average of this PoolLegacyDetail.  # noqa: E501

        same as toRuneVolume / toRuneCount from pool/stats  # noqa: E501

        :return: The sell_tx_average of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._sell_tx_average

    @sell_tx_average.setter
    def sell_tx_average(self, sell_tx_average):
        """Sets the sell_tx_average of this PoolLegacyDetail.

        same as toRuneVolume / toRuneCount from pool/stats  # noqa: E501

        :param sell_tx_average: The sell_tx_average of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if sell_tx_average is None:
            raise ValueError("Invalid value for `sell_tx_average`, must not be `None`")  # noqa: E501

        self._sell_tx_average = sell_tx_average

    @property
    def sell_volume(self):
        """Gets the sell_volume of this PoolLegacyDetail.  # noqa: E501

        same as toRuneVolume from pool/stats  # noqa: E501

        :return: The sell_volume of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._sell_volume

    @sell_volume.setter
    def sell_volume(self, sell_volume):
        """Sets the sell_volume of this PoolLegacyDetail.

        same as toRuneVolume from pool/stats  # noqa: E501

        :param sell_volume: The sell_volume of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if sell_volume is None:
            raise ValueError("Invalid value for `sell_volume`, must not be `None`")  # noqa: E501

        self._sell_volume = sell_volume

    @property
    def stake_tx_count(self):
        """Gets the stake_tx_count of this PoolLegacyDetail.  # noqa: E501

        same as addLiquidityCount from pool/stats  # noqa: E501

        :return: The stake_tx_count of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._stake_tx_count

    @stake_tx_count.setter
    def stake_tx_count(self, stake_tx_count):
        """Sets the stake_tx_count of this PoolLegacyDetail.

        same as addLiquidityCount from pool/stats  # noqa: E501

        :param stake_tx_count: The stake_tx_count of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if stake_tx_count is None:
            raise ValueError("Invalid value for `stake_tx_count`, must not be `None`")  # noqa: E501

        self._stake_tx_count = stake_tx_count

    @property
    def stakers_count(self):
        """Gets the stakers_count of this PoolLegacyDetail.  # noqa: E501

        same as uniqueMemberCount from pool/stats  # noqa: E501

        :return: The stakers_count of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._stakers_count

    @stakers_count.setter
    def stakers_count(self, stakers_count):
        """Sets the stakers_count of this PoolLegacyDetail.

        same as uniqueMemberCount from pool/stats  # noqa: E501

        :param stakers_count: The stakers_count of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if stakers_count is None:
            raise ValueError("Invalid value for `stakers_count`, must not be `None`")  # noqa: E501

        self._stakers_count = stakers_count

    @property
    def staking_tx_count(self):
        """Gets the staking_tx_count of this PoolLegacyDetail.  # noqa: E501

        same as addLiquidityCount + withdrawCount from pool/stats  # noqa: E501

        :return: The staking_tx_count of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._staking_tx_count

    @staking_tx_count.setter
    def staking_tx_count(self, staking_tx_count):
        """Sets the staking_tx_count of this PoolLegacyDetail.

        same as addLiquidityCount + withdrawCount from pool/stats  # noqa: E501

        :param staking_tx_count: The staking_tx_count of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if staking_tx_count is None:
            raise ValueError("Invalid value for `staking_tx_count`, must not be `None`")  # noqa: E501

        self._staking_tx_count = staking_tx_count

    @property
    def status(self):
        """Gets the status of this PoolLegacyDetail.  # noqa: E501

        same as status from pool/stats  # noqa: E501

        :return: The status of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PoolLegacyDetail.

        same as status from pool/stats  # noqa: E501

        :param status: The status of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def swappers_count(self):
        """Gets the swappers_count of this PoolLegacyDetail.  # noqa: E501

        Int64, same as history/swaps:uniqueSwapperCount  # noqa: E501

        :return: The swappers_count of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._swappers_count

    @swappers_count.setter
    def swappers_count(self, swappers_count):
        """Sets the swappers_count of this PoolLegacyDetail.

        Int64, same as history/swaps:uniqueSwapperCount  # noqa: E501

        :param swappers_count: The swappers_count of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if swappers_count is None:
            raise ValueError("Invalid value for `swappers_count`, must not be `None`")  # noqa: E501

        self._swappers_count = swappers_count

    @property
    def swapping_tx_count(self):
        """Gets the swapping_tx_count of this PoolLegacyDetail.  # noqa: E501

        Int64, same as history/swaps:totalCount  # noqa: E501

        :return: The swapping_tx_count of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._swapping_tx_count

    @swapping_tx_count.setter
    def swapping_tx_count(self, swapping_tx_count):
        """Sets the swapping_tx_count of this PoolLegacyDetail.

        Int64, same as history/swaps:totalCount  # noqa: E501

        :param swapping_tx_count: The swapping_tx_count of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if swapping_tx_count is None:
            raise ValueError("Invalid value for `swapping_tx_count`, must not be `None`")  # noqa: E501

        self._swapping_tx_count = swapping_tx_count

    @property
    def volume24h(self):
        """Gets the volume24h of this PoolLegacyDetail.  # noqa: E501

        Int64(e8), same as swapVolume pool/stats?period=24h  # noqa: E501

        :return: The volume24h of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._volume24h

    @volume24h.setter
    def volume24h(self, volume24h):
        """Sets the volume24h of this PoolLegacyDetail.

        Int64(e8), same as swapVolume pool/stats?period=24h  # noqa: E501

        :param volume24h: The volume24h of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if volume24h is None:
            raise ValueError("Invalid value for `volume24h`, must not be `None`")  # noqa: E501

        self._volume24h = volume24h

    @property
    def withdraw_tx_count(self):
        """Gets the withdraw_tx_count of this PoolLegacyDetail.  # noqa: E501

        same as withdrawCount from pool/stats  # noqa: E501

        :return: The withdraw_tx_count of this PoolLegacyDetail.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_tx_count

    @withdraw_tx_count.setter
    def withdraw_tx_count(self, withdraw_tx_count):
        """Sets the withdraw_tx_count of this PoolLegacyDetail.

        same as withdrawCount from pool/stats  # noqa: E501

        :param withdraw_tx_count: The withdraw_tx_count of this PoolLegacyDetail.  # noqa: E501
        :type: str
        """
        if withdraw_tx_count is None:
            raise ValueError("Invalid value for `withdraw_tx_count`, must not be `None`")  # noqa: E501

        self._withdraw_tx_count = withdraw_tx_count

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
        if issubclass(PoolLegacyDetail, dict):
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
        if not isinstance(other, PoolLegacyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
