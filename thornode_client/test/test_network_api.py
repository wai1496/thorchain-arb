# coding: utf-8

"""
    THORChain API

    This documentation outlines the API for THORChain.  NOTE: This document is a **work in progress**.  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import thornode_client
from thornode_client.api.network_api import NetworkApi  # noqa: E501
from thornode_client.rest import ApiException


class TestNetworkApi(unittest.TestCase):
    """NetworkApi unit test stubs"""

    def setUp(self):
        self.api = thornode_client.api.network_api.NetworkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_last_block_height(self):
        """Test case for get_all_last_block_height

        Get all last block height  # noqa: E501
        """
        pass

    def test_get_constant_values_from_thor_chain(self):
        """Test case for get_constant_values_from_thor_chain

        Get constant values from THORChain  # noqa: E501
        """
        pass

    def test_get_current_network_version(self):
        """Test case for get_current_network_version

        Get current network version  # noqa: E501
        """
        pass

    def test_get_inbound_addresses(self):
        """Test case for get_inbound_addresses

        Get inbound addresses  # noqa: E501
        """
        pass

    def test_get_last_block_height_per_chain(self):
        """Test case for get_last_block_height_per_chain

        Get last block height per chain  # noqa: E501
        """
        pass

    def test_get_network_data(self):
        """Test case for get_network_data

        Get network data  # noqa: E501
        """
        pass

    def test_get_ragnarok_status(self):
        """Test case for get_ragnarok_status

        Get Ragnarok status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
