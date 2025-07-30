# test_price_utils.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from price_utils import apply_discount

def test_apply_discount():
    price = 100
    discount = 0.2
    expected = 80
    result = apply_discount(price, discount)
    assert result == expected
