# Lesson 08 — Python `for` Loop

## Mục tiêu

Duyệt lần lượt các phần tử trong một `list`, truy cập dữ liệu `dict`, lọc theo điều kiện và cộng dồn kết quả. Áp dụng để xử lý đơn hàng trong pipeline dữ liệu cơ bản.

## 1. Vòng lặp `for`

```python
for item in items:
    print(item)
```

- `items` là đối tượng có thể lặp (iterable), ví dụ `list`.
- `item` là biến được gán lần lượt từng phần tử.
- Khối lệnh thụt lề bên dưới `for` được chạy cho từng phần tử.
- `for` không tự động chia dữ liệu thành batch hoặc giảm RAM nếu toàn bộ dữ liệu đã được nạp vào `list`.

## 2. List chứa Dictionary

```python
orders = [
    {"order_id": "O001", "amount": 500000, "status": "PAID"},
    {"order_id": "O002", "amount": 300000, "status": "FAILED"},
]

for order in orders:
    print(order["order_id"])
```

`orders` là `list`; mỗi `order` là một `dict`. Truy cập giá trị qua khóa, ví dụ `order["amount"]`.

## 3. Điều kiện bên trong vòng lặp

```python
if order["status"] == "PAID" and order["amount"] > 0:
    ...
```

- `==` so sánh bằng; `>` so sánh lớn hơn.
- `and` chỉ cho kết quả `True` khi cả hai điều kiện đều đúng.
- Indentation (thụt lề) quyết định khối lệnh thuộc `for` hoặc `if`; thường dùng 4 dấu cách mỗi cấp.

## 4. Cộng dồn (accumulator)

```python
total = 0
for order in orders:
    if order["status"] == "PAID" and order["amount"] > 0:
        total += order["amount"]
```

`total += value` tương đương `total = total + value`. Khởi tạo `total` trước vòng lặp, sau đó cập nhật ở mỗi bản ghi thỏa điều kiện.

## 5. Business rules và dữ liệu không hợp lệ

Trong bài thực hành, chỉ tính các đơn `PAID` có `amount > 0`. Bản ghi `PAID` với `amount = 0` hoặc âm không được cộng. Nếu bỏ kiểm tra số dương, giá trị âm có thể làm giảm tổng sai nghiệp vụ. Cần phân biệt **tổng giá trị đơn hàng PAID theo quy tắc bài tập** với **doanh thu được ghi nhận**: hai khái niệm không tự động tương đương.

Code bài học giả định mỗi bản ghi đều có khóa `status` và `amount`, và `amount` là số. Trong pipeline thực tế, cần kiểm tra schema, kiểu dữ liệu và quy tắc nghiệp vụ trước khi tính toán; không được coi bài này là một pipeline production hoàn chỉnh.

## 6. Lỗi thường gặp

- Không thụt lề sau `for` hoặc `if` → `IndentationError`.
- Dùng dấu nháy cong `“ ”` thay vì `' '` hoặc `" "` → lỗi cú pháp.
- Quên điều kiện nghiệp vụ → kết quả có thể đúng ngẫu nhiên trên dữ liệu mẫu nhưng sai với dữ liệu khác.
- Đặt `total = 0` bên trong vòng lặp → tổng bị khởi tạo lại mỗi lần.
- Nhầm `order` (một phần tử) với `orders` (toàn bộ danh sách).

## 7. Tự kiểm tra kiến thức

1. `order` khác `orders` thế nào trong `for order in orders`?
2. Vì sao `total = 0` cần nằm ngoài vòng lặp?
3. Vì sao cần cả `status == "PAID"` và `amount > 0`?
4. Vòng lặp `for` có đảm bảo xử lý 10 triệu bản ghi mà không tốn nhiều RAM không?

## 8. Liên hệ Data Engineering

Một vòng lặp có thể là bước nền tảng để duyệt, kiểm tra và biến đổi các bản ghi. Khi dữ liệu tăng lớn, cần cân nhắc đọc theo batch, streaming, hoặc đẩy phép tổng hợp xuống SQL/database tùy bài toán.

## 9. Điều kiện hoàn thành

- Giải thích được cách `for` duyệt `list` chứa `dict`.
- Viết đúng cú pháp, indentation, `if`/`and` và `+=`.
- Chạy được `exercises.py`, thu được tổng `1200000`.
- Giải thích được vì sao `FAILED`, số 0 và số âm không được tính.
