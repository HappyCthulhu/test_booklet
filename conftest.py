import pytest
import json
from main import OrderBook, Order

@pytest.fixture(scope="function")
def book():
    book = OrderBook()
    return book

