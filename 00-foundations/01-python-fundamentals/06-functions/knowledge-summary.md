# Lesson 10 — Python Functions

> Tài liệu kiến thức để ôn tập. Ví dụ thực hành gắn với bài toán NovaCommerce, không phải báo cáo nhật ký học tập.

## 1. Vấn đề

Trong pipeline dữ liệu, cùng một quy tắc tính tổng các đơn hàng `PAID` có thể cần dùng ở nhiều nơi. Sao chép đoạn code xử lý khiến logic phân tán, dễ sai lệch khi cập nhật. Function đóng gói công việc thành một đơn vị có thể gọi lại.

## 2. Định nghĩa và gọi hàm

```python
def calculate_total(amount, shipping_fee):
    total = amount + shipping_fee
    return total

result = calculate_total(500000, 20000)
assert result == 520000
```

- `def`: định nghĩa hàm, chưa tự thực thi phần thân.
- `calculate_total`: tên hàm.
- `amount`, `shipping_fee`: **parameters** (tham số trong định nghĩa).
- `500000`, `20000`: **arguments** (giá trị truyền khi gọi).
- Phần thân hàm thụt vào, thông thường 4 dấu cách.
- `result` nhận giá trị được trả về từ lời gọi hàm.

## 3. `return` khác `print()`

```python
def display_amount():
    print(500000)

def get_amount():
    return 500000

a = display_amount()  # in ra 500000 nhưng a = None
b = get_amount()      # không tự in, b = 500000
```

- `print()` hiển thị, không thay thế giá trị trả về của hàm.
- Nếu thực thi đến cuối hàm mà không có `return`, Python mặc định trả về `None`.
- Khi gặp `return`, hàm kết thúc ngay và trả giá trị cho nơi gọi; code phía sau trong cùng lần gọi không tiếp tục chạy.
- Có thể `print()` một kết quả sau khi gọi hàm, nhưng logic xử lý nên `return` dữ liệu để bước khác sử dụng.

## 4. Function với List chứa Dictionary

```python
def calculate_paid_total(orders):
    total = 0

    for order in orders:
        if order["status"] == "PAID" and order["amount"] > 0:
            total += order["amount"]

    return total
```

Business rule cho bài học: chỉ tính `amount` dương khi `status == "PAID"`. Đơn `FAILED` hay số tiền âm không được cộng.

**Vì sao đặt `return total` ngoài vòng `for`?** Nếu đặt trong vòng lặp, hàm kết thúc ngay ở lần lặp đầu tiên đi tới `return`, khiến dữ liệu còn lại chưa được xử lý.

## 5. Tính tái sử dụng và scope cơ bản

```python
def calculate_double(amount):
    result = amount * 2
    return result

value = calculate_double(100)
```

`result` là biến cục bộ trong hàm. `value` nằm ở nơi gọi hàm và nhận kết quả `200`. Hàm nên nhận đầu vào rõ ràng thay vì dựa vào dữ liệu toàn cục khi có thể.

## 6. Những lỗi thường gặp

- `for order in order:` khi chưa có iterable tên `order`: dùng `for order in orders:`.
- `print result` là cú pháp Python 2; Python 3 dùng `print(result)`.
- Dấu `*` trong `*args` là cú pháp nhận positional arguments biến độ dài, không cần thiết khi tham số là một List `orders`.
- `return` quá sớm trong vòng lặp làm mất dữ liệu chưa duyệt.
- Nhầm `None` với `0` khi hàm quên `return`.
- Chỉ kiểm tra `status` mà bỏ qua quy tắc nghiệp vụ `amount > 0`.

## 7. Giới hạn và bước phát triển tiếp

Ví dụ giả định mọi Dictionary có đủ khóa và `amount` là số. Trong pipeline thực tế cần schema validation, xử lý bản ghi lỗi/quarantine, kiểm tra dữ liệu trùng và định nghĩa KPI rõ ràng. Tổng giá trị đơn `PAID` theo bài tập không mặc nhiên là doanh thu kế toán.

## 8. Tự kiểm tra

1. Phân biệt parameter và argument qua ví dụ.
2. `return` khác gì `print()`?
3. Tại sao `return` nên ở sau vòng lặp trong hàm tính tổng?
4. Nếu `orders` rỗng, hàm trả về bao nhiêu?
5. Vì sao function giúp giảm duplicate logic?

## 9. Bằng chứng học tập

- [`exercises.py`](exercises.py): bài thực hành NovaCommerce đã được người học viết và giải thích.
- Kiểm tra cú pháp và tổng kỳ vọng `1200000` bằng assertion.
- Bài học này là bước nền; không đại diện một ETL production hoàn chỉnh.

**Học tiếp:** Exception Handling (`try`, `except`) và xử lý lỗi dữ liệu.