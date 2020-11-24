import json
import random as r

class Order:
    def __init__(self, price, quantity, ID):
        self.price = price
        self.quantity = quantity
        self.ID = ID

    def __repr__(self):
        return json.dumps(f'ID: {self.ID}, Цена: {self.price}, Количество: {self.quantity}', ensure_ascii=False)

class OrderBook:
    def __init__(self):
        self.asks = {}
        self.bids = {}

    def __repr__(self):

        list_of_asks = []
        for _, ask in self.asks.items():
            list_of_asks.append({'price': ask.price, 'quantity': ask.quantity})

        sorted(list_of_asks, key=lambda x : x['price'])

        list_of_bids = []
        for _, bid in self.bids.items():
            list_of_bids.append({'price': bid.price, 'quantity': bid.quantity})

        sorted(list_of_asks, key=lambda x : x['price'])

        asks_bids_dict = json.dumps({'asks': list_of_asks, 'bids': list_of_bids}, indent=2)
        return asks_bids_dict

    def create_ID(self):
        ID = r.randint(335, 523984723)
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

    def find_order(self, ID):
        if ID in self.asks:
            return self.asks[ID]
        elif ID in self.bids:
            return self.bids[ID]

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


order_dict = OrderBook()
order_dict.add_order_to_list(1, 4, 'bid')
order_dict.add_order_to_list(234, 23, 'bid')
order_dict.add_order_to_list(241634, 23, 'bid')
order_dict.add_order_to_list(26, 64, 'ask')
order_dict.add_order_to_list(767, 453, 'ask')
order_dict.add_order_to_list(122, 345, 'ask')

print(order_dict)


list_of_ID = order_dict.id_list_generate()
print(f'Список IDшников: {list_of_ID}')

random_id = list_of_ID[r.randint(1, 4)]
print(f'Рандомный ID: {random_id}')

print(f'Ставка: {order_dict.find_order(random_id)}')
order_dict.remove_order(random_id)

list_of_ID = order_dict.id_list_generate()
print(f'Список IDшников: {list_of_ID}')
