import pytest
import json

class TestsForOrderBook:
    def test_is_order_exist_in_list(self, order_dict):
        print(json.dumps(order_dict.add_order(1, 4, 'bid')))
