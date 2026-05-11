"""
Sales discount calculator.

This module calculates the final price after applying a discount.
It contains a bug — find it with Copilot's help, then fix it.
"""


def calculate_discounted_price(unit_price: float, quantity: int, discount_pct: float) -> float:
    """Calculate the total price after applying a percentage discount.

    Args:
        unit_price: Price per unit (e.g., 199.99).
        quantity: Number of units ordered.
        discount_pct: Discount as a percentage (e.g., 10 means 10% off).

    Returns:
        Total price after discount.

    Example:
        >>> calculate_discounted_price(100.0, 3, 10)
        270.0   # 3 * 100 * (1 - 0.10) = 270.0
    """
    discount_multiplier = 1 - discount_pct  # BUG: discount_pct should be divided by 100
    return unit_price * quantity * discount_multiplier


def apply_bulk_discount(unit_price: float, quantity: int) -> float:
    """Apply an automatic bulk discount based on quantity.

    Discount tiers:
        - 0-4 units:   0% discount
        - 5-9 units:   5% discount
        - 10-19 units: 10% discount
        - 20+ units:   15% discount

    Args:
        unit_price: Price per unit.
        quantity: Number of units ordered.

    Returns:
        Total price after bulk discount.
    """
    if quantity >= 20:
        discount_pct = 15.0
    elif quantity >= 10:
        discount_pct = 10.0
    elif quantity >= 5:
        discount_pct = 5.0
    else:
        discount_pct = 0.0

    return calculate_discounted_price(unit_price, quantity, discount_pct)
