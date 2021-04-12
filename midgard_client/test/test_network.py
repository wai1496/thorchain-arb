# coding: utf-8

"""
    Midgard Public API

    The Midgard Public API queries THORChain and any chains linked via the Bifröst and prepares information about the network to be readily available for public users. The API parses transaction event data from THORChain and stores them in a time-series database to make time-dependent queries easy. Midgard does not hold critical information. To interact with BEPSwap and Asgardex, users should query THORChain directly.  # noqa: E501

    OpenAPI spec version: 2.0.0-alpha.3
    Contact: devs@thorchain.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import midgard_client
from midgard_client.models.network import Network  # noqa: E501
from midgard_client.rest import ApiException


class TestNetwork(unittest.TestCase):
    """Network unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNetwork(self):
        """Test Network"""
        # FIXME: construct object with mandatory attributes with example values
        # model = midgard_client.models.network.Network()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
