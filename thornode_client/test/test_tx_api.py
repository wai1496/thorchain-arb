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
from thornode_client.api.tx_api import TxApi  # noqa: E501
from thornode_client.rest import ApiException


class TestTxApi(unittest.TestCase):
    """TxApi unit test stubs"""

    def setUp(self):
        self.api = thornode_client.api.tx_api.TxApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_a_tx_with_given_hash(self):
        """Test case for get_a_tx_with_given_hash

        Get a tx with given hash  # noqa: E501
        """
        pass

    def test_get_tx_signers(self):
        """Test case for get_tx_signers

        Get tx signers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
