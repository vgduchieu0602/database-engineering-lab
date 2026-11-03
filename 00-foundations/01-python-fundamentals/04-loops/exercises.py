"""Lesson 08: for loop — NovaCommerce paid order total.

Chạy: python exercises.py
Kết quả mong đợi: 1200000
"""

orders = [
    {"order_id": "O001", "amount": 500000, "status": "PAID"},
    {"order_id": "O002", "amount": 300000, "status": "FAILED"},
    {"order_id": "O003", "amount": 700000, "status": "PAID"},
    {"order_id": "O004", "amount": 0, "status": "PAID"},
]

total = 0

for order in orders:
    if order["status"] == "PAID" and order["amount"] > 0:
        total += order["amount"]

print(total)

# Kiểm chứng kết quả bài tập.
assert total == 1200000, f"Expected 1200000, got {total}"

# Thử thay amount của O004 thành -100000: tổng vẫn phải là 1200000.
