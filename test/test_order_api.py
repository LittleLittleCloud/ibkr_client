# coding: utf-8

"""
    Client Portal Web API

    Production version of the Client Portal Web API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ibkr_client
from ibkr_client.api.order_api import OrderApi  # noqa: E501
from ibkr_client.rest import ApiException


class TestOrderApi(unittest.TestCase):
    """OrderApi unit test stubs"""

    def setUp(self):
        self.api = ibkr_client.api.order_api.OrderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_iserver_account_account_id_order_order_id_delete(self):
        """Test case for iserver_account_account_id_order_order_id_delete

        Cancel Order  # noqa: E501
        """
        pass

    def test_iserver_account_account_id_order_order_id_post(self):
        """Test case for iserver_account_account_id_order_order_id_post

        Modify Order  # noqa: E501
        """
        pass

    def test_iserver_account_account_id_order_post(self):
        """Test case for iserver_account_account_id_order_post

        Place Order  # noqa: E501
        """
        pass

    def test_iserver_account_account_id_order_whatif_post(self):
        """Test case for iserver_account_account_id_order_whatif_post

        Preview Order  # noqa: E501
        """
        pass

    def test_iserver_account_account_id_orders_post(self):
        """Test case for iserver_account_account_id_orders_post

        Place Orders (Support bracket orders)  # noqa: E501
        """
        pass

    def test_iserver_account_orders_fa_group_post(self):
        """Test case for iserver_account_orders_fa_group_post

        Place Orders for Financial Advisor Groups  # noqa: E501
        """
        pass

    def test_iserver_account_orders_get(self):
        """Test case for iserver_account_orders_get

        Live Orders  # noqa: E501
        """
        pass

    def test_iserver_reply_replyid_post(self):
        """Test case for iserver_reply_replyid_post

        Place Order Reply  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
