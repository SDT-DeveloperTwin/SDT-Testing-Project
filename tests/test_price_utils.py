# test_price_utils.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from price_utils import apply_discount

def test_apply_discount():
    price = 100
    discount = 20
    expected = 80.00
    result = apply_discount(price, discount)
    assert result == expected, f"Expected {expected}, but got {result}"
