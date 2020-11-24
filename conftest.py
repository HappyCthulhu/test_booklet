import pytest
from main import OrderBook, Order

@pytest.fixture(scope="function")
def order_dict():
    order_dict = OrderBook()
