# test_price_utils.py
from price_utils import apply_discount

def test_apply_discount():
    price = 100
    discount = 0.2
    expected = 80
    result = apply_discount(price, discount)
    assert result == expected
