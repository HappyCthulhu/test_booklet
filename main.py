import json
import random as r

class Order:
    def __init__(self, price, quantity, ID):
        self.price = price
        self.quantity = quantity
        self.ID = ID

class OrderBook:
    def __init__(self):
        self.asks = {}
        self.bids = {}

    def __repr__(self):

        list_of_asks = []
        for _, ask in self.asks.items():
            list_of_asks.append({'price': ask.price, 'quantity': ask.quantity})

        list_of_bids = []
        for _, bid in self.bids.items():
            list_of_bids.append({'price': bid.price, 'quantity': bid.quantity})

        dict_test_test = json.dumps({'asks': list_of_asks, 'bids': list_of_bids}, indent=2)
        return dict_test_test

    def create_ID(self):
        ID = r.randint(12412, 329173182)
        return ID

    def add_order_to_list(self, price, quantity, type):
        ID = self.create_ID()

        order = Order(price, quantity, ID)
        if type == 'ask':
            self.asks[ID] = order
        elif type == 'bid':
            self.bids[ID] = order
        else:
            print('Неправильный тип заявки')
        return self.asks, self.bids


order_dict = OrderBook()
order_dict.add_order_to_list(1, 4, 'bid')
order_dict.add_order_to_list(234, 23, 'bid')
order_dict.add_order_to_list(241634, 23, 'bid')
order_dict.add_order_to_list(26, 64, 'ask')
order_dict.add_order_to_list(767, 453, 'ask')
order_dict.add_order_to_list(122, 345, 'ask')

print(order_dict)