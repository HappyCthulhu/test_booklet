import pytest
import json


class TestsForOrderBook:
    def test_is_order_exist_in_list(self, book):
        price = 1
        quantity = 4
        type = 'bid'
        order_ID = book.add_order(price, quantity, type)
        assert book.get_order(order_ID), 'There is no order with this ID in OrderBook'

