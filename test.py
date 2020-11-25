import pytest
import json


class TestsForOrderBook:
    def test_order_bid_exist(self, book):
        price = 1
        quantity = 4
        type = 'bid'
        order_ID = book.add_order(price, quantity, type)
        assert book.get_order(order_ID), 'There is no order bid with this ID in OrderBook'

    def test_order_ask_exist(self, book):
        price = 1
        quantity = 4
        type = 'ask'
        order_ID = book.add_order(price, quantity, type)
        assert book.get_order(order_ID), 'There is no order ask with this ID in OrderBook'

    def test_order_is_not_exist(self, book):
        assert book.get_order(4545) == None, 'Existing order with incorrect ID'
        
    def test_remove_order_ask(self, book):
        price = 1
        quantity = 4
        type = 'ask'
        order_ID = book.add_order(price, quantity, type)
        book.remove_order(order_ID)
        assert not book.get_order(order_ID)

    def test_remove_order_bid(self, book):
        price = 1
        quantity = 4
        type = 'bid'
        order_ID = book.add_order(price, quantity, type)
        book.remove_order(order_ID)
        assert not book.get_order(order_ID)

    def test_wrong_type_order_exist(self, book):
        price = 1
        quantity = 4
        type = 'wrong type'
        try:
            order_ID = book.add_order(price, quantity, type)
            assert False, 'Order type is incorrect, but there is no Exception'
        except ValueError:
            return True

    def test_correct_order_book_with_ask_order(self, book):
        price = 1
        quantity = 4
        type = 'ask'
        order_ID = book.add_order(price, quantity, type)
        order_book = book.get_info()
        assert order_book['asks'][0]['price'] == price and order_book['asks'][0][
            'quantity'] == quantity, 'order_book ask value isnt correct'

    def test_correct_order_book_with_bid_order(self, book):
        price = 1
        quantity = 4
        type = 'bid'
        order_ID = book.add_order(price, quantity, type)
        order_book = book.get_info()
        assert order_book['bids'][0]['price'] == price and order_book['bids'][0][
            'quantity'] == 234532, 'order_book bid value isnt correct'
