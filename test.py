import pytest
import json


class TestsForOrderBook:
    def test_is_order_exist_in_list(self, book):
        price = 1
        quantity = 4
        type = 'bid'
        order_ID = book.add_order(price, quantity, type)
        assert book.get_order(order_ID), 'There is no order with this ID in OrderBook'

    #TODO: если id некорректна, должен выдать 
    def test_if_order_is_not_exist(self, book):
        assert book.get_order(4545) == None, 'Existing order with incorrect ID'
    
    def test_ask_order_exist(self, book):
        price = 1
        quantity = 4
        type = 'ask'
        order_ID = book.add_order(price, quantity, type)
        assert book.get_order(order_ID), 'There is no ask-order'

    def test_bid_order_exist(self, book):
        price = 1
        quantity = 4
        type = 'bid'
        order_ID = book.add_order(price, quantity, type)
        assert book.get_order(order_ID), 'There is no bid-order'
        
    def test_wrong_type_order_exist(self, book):
        price = 1
        quantity = 4
        type = 'wrong type'
        try:
            order_ID = book.add_order(price, quantity, type)
            assert False, 'Order type is incorrect, but there is no Exception'
        except ValueError:
            return True
