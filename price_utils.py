# Buggy implementation (for agent to fix)
def apply_discount(price: float, discount_percent: float) -> float:
    return price * (1 - discount_percent / 100)
