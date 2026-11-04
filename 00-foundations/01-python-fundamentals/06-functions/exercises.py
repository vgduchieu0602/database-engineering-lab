"""Lesson 10: Function — tính tổng đơn PAID theo business rule NovaCommerce.

Bài thực hành được người học tự viết và đã được đánh giá qua hội thoại.
Chạy: python exercises.py
Kết quả mong đợi: 1200000
"""

orders = [
    {"order_id": "O001", "amount": 500000, "status": "PAID"},
    {"order_id": "O002", "amount": 300000, "status": "FAILED"},
    {"order_id": "O003", "amount": 700000, "status": "PAID"},
    {"order_id": "O004", "amount": -100000, "status": "PAID"}
]


def calculate_paid_total(orders):
    total = 0

    for order in orders:
        if order["status"] == "PAID" and order["amount"] > 0:
            total += order["amount"]

    return total


result = calculate_paid_total(orders)
print(result)

# Đối chiếu với output kỳ vọng của bài thực hành.
assert result == 1200000, f"Expected 1200000, got {result}"

# Kiểm tra thêm tính tái sử dụng với dữ liệu rỗng.
assert calculate_paid_total([]) == 0