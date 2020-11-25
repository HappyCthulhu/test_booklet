import json
import random as r
from dataclasses import dataclass

# TODO: сделать уникальные IDшники класса

@dataclass
class Order:
    price: int
    quantity: int
    ID: int
    type: str

class OrderBook:
    def __init__(self):
        self.asks = {}
        self.bids = {}

    def get_info(self):
        list_of_asks = []
        for _, ask in self.asks.items():
            list_of_asks.append({'price': ask.price, 'quantity': ask.quantity})

        sorted(list_of_asks, key=lambda x : x['price'])

        list_of_bids = []
        for _, bid in self.bids.items():
            list_of_bids.append({'price': bid.price, 'quantity': bid.quantity})

        sorted(list_of_asks, key=lambda x : x['price'])

        asks_bids_dict = {'asks': list_of_asks, 'bids': list_of_bids}
        return asks_bids_dict

    def create_ID(self):
        ID = r.randint(335, 523984723)
        return ID

    def add_order(self, price, quantity, type):
        ID = self.create_ID()

        order = Order(price, quantity, ID, type)
        if type == 'ask':
            self.asks[ID] = order
        elif type == 'bid':
            self.bids[ID] = order
        else:
            raise ValueError('Wrong order type')

        return order.ID

    def get_order(self, ID):
        if ID in self.asks:
            return self.asks[ID]
        elif ID in self.bids:
            return self.bids[ID]
        else:
            return None

    def id_list_generate(self):
        list_of_ID = []

        for elem in list(self.asks.keys()):
            list_of_ID.append(elem)
        for elem in list(self.bids.keys()):
            list_of_ID.append(elem)

        return list_of_ID

    def remove_order(self, ID):
        if ID in self.asks:
            del self.asks[ID]
        elif ID in self.bids:
            del self.bids[ID]


book = OrderBook()
print(book.add_order(1, 4, 'bid'))
# book.add_order(234, 23, 'bid')
# book.add_order(241634, 23, 'bid')
# book.add_order(26, 64, 'ask')
# book.add_order(767, 453, 'ask')
# book.add_order(122, 345, 'ask')
#
# print(json.dumps(book.get_info(), indent=2))
#
#
# list_of_ID = book.id_list_generate()
# print(f'Список IDшников: {list_of_ID}')
#
# random_id = list_of_ID[r.randint(1, 4)]
# print(f'Рандомный ID: {random_id}')
#
# print(f'Ставка: {book.get_order(random_id)}')
# book.remove_order(random_id)
#
# list_of_ID = book.id_list_generate()
# print(f'Список IDшников: {list_of_ID}')
