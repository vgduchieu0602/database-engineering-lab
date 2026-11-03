"""Reference examples: Python Dictionary for NovaCommerce.

Run: python exercises.py
These examples are reference material, not learner completion evidence.
"""

order = {"order_id": "O001", "amount": 500000, "status": "PAID"}
assert order["order_id"] == "O001"
assert order["amount"] == 500000

order["source"] = "api"
assert order["source"] == "api"

assert "coupon_code" not in order
assert order.get("coupon_code") is None

order["refund_amount"] = None
assert "refund_amount" in order
assert order.get("refund_amount") is None

orders = [
    {"order_id": "O001", "status": "PAID", "amount": 500000},
    {"order_id": "O002", "status": "FAILED", "amount": 300000},
]
assert orders[0]["status"] == "PAID"
assert orders[1]["amount"] == 300000

print(f"first_order={orders[0]['order_id']}")
print("All reference assertions passed.")

# Practice idea (not marked complete): add validated_at to a record.
