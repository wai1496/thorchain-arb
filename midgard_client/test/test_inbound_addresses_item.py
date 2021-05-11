# coding: utf-8

"""
    Midgard Public API

    The Midgard Public API queries THORChain and any chains linked via the Bifröst and prepares information about the network to be readily available for public users. The API parses transaction event data from THORChain and stores them in a time-series database to make time-dependent queries easy. Midgard does not hold critical information. To interact with BEPSwap and Asgardex, users should query THORChain directly.  # noqa: E501

    OpenAPI spec version: 2.1.0
    Contact: devs@thorchain.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import midgard_client
from midgard_client.models.inbound_addresses_item import InboundAddressesItem  # noqa: E501
from midgard_client.rest import ApiException


class TestInboundAddressesItem(unittest.TestCase):
    """InboundAddressesItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInboundAddressesItem(self):
        """Test InboundAddressesItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = midgard_client.models.inbound_addresses_item.InboundAddressesItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
