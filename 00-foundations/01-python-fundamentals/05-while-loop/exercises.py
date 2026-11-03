"""Lesson 09 — while loop: NovaCommerce batch processing.

Bài thực hành đã được người học gửi và đánh giá trong cuộc trao đổi.
Chạy: python exercises.py

Kết quả mong đợi:
Batch 1: ['O001', 'O002', 'O003']
Batch 2: ['O004', 'O005', 'O006']
Batch 3: ['O007']
"""

orders = [
    "O001", "O002", "O003",
    "O004", "O005", "O006", "O007"
]

batch_size = 3
start = 0
batch_number = 1

while start < len(orders):
    batch = orders[start:start + batch_size]
    print(f"Batch {batch_number}: {batch}")

    start += batch_size
    batch_number += 1
