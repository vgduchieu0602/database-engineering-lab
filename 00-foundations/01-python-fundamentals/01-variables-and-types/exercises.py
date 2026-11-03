"""Reference examples: variables and data types for NovaCommerce.

Run: python exercises.py
These are runnable reference examples, not evidence of learner-authored exercises.
"""

order_id = "O001"
amount_vnd = 500000
status = "PAID"
is_refunded = False
refund_amount_vnd = None

assert isinstance(order_id, str)
assert isinstance(amount_vnd, int)
assert isinstance(status, str)
assert isinstance(is_refunded, bool)
assert refund_amount_vnd is None

shipping_fee_vnd = 20000
total_vnd = amount_vnd + shipping_fee_vnd
assert total_vnd == 520000

# A missing value is different from a known zero.
assert refund_amount_vnd is not 0
refund_amount_vnd = 0
assert refund_amount_vnd == 0

# Type checking alone cannot enforce business rules.
invalid_amount_vnd = -100000
assert isinstance(invalid_amount_vnd, int)
assert invalid_amount_vnd <= 0

print(f"order_id={order_id}; total_vnd={total_vnd}")
print("All reference assertions passed.")

# Practice idea (not marked complete): explain why int("abc") fails.
