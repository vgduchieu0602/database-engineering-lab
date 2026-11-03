"""Reference examples: Python List for NovaCommerce.

Run: python exercises.py
These examples are provided as study material, not learner completion proof.
"""

order_ids = ["O001", "O002"]
assert order_ids[0] == "O001"
assert order_ids[-1] == "O002"
assert len(order_ids) == 2

order_ids.append("O003")
assert order_ids == ["O001", "O002", "O003"]
assert order_ids[:2] == ["O001", "O002"]
assert "O003" in order_ids

orders = [
    {"order_id": "O001", "amount": 500000},
    {"order_id": "O002", "amount": 300000},
]
assert len(orders) == 2
assert orders[0]["amount"] == 500000
assert orders[1]["order_id"] == "O002"

alias = order_ids
alias.append("O004")
assert len(order_ids) == 4  # alias and order_ids refer to the same list.

print(f"order_ids={order_ids}")
print("All reference assertions passed.")

# Practice idea (not marked complete): add O005 without removing existing IDs.
