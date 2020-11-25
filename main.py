from dataclasses import dataclass
import uuid


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

        sorted(list_of_asks, key=lambda x: x['price'])

        list_of_bids = []
        for _, bid in self.bids.items():
            list_of_bids.append({'price': bid.price, 'quantity': bid.quantity})

        sorted(list_of_asks, key=lambda x: x['price'])

        asks_bids_dict = {'asks': list_of_asks, 'bids': list_of_bids}
        return asks_bids_dict

    def create_ID(self):
        ID = str(uuid.uuid4())
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
        else:
            return None
