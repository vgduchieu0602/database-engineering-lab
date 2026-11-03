# Python Fundamentals — 01. Variables & Data Types

> **Vai trò:** Tài liệu kiến thức để tham khảo và ôn tập. Không phải nhật ký học tập hay chứng nhận đã hoàn thành project.

## 1. Vấn đề thực tế

Một nguồn dữ liệu đơn hàng của NovaCommerce có các thuộc tính như mã đơn, số tiền, trạng thái và lý do lỗi. Nếu nhầm kiểu dữ liệu, pipeline có thể tính sai hoặc không phân biệt được dữ liệu thiếu với giá trị thực tế.

## 2. Biến (variable) là gì?

Biến là tên được gắn với một giá trị/đối tượng. Trong Python, dùng phép gán `=` để đặt tên và có thể gán lại.

```python
order_id = "O001"
amount_vnd = 500000
status = "PAID"
amount_vnd = 600000  # gán lại tên biến
```

- `=` dùng để gán, `==` dùng để so sánh bằng.
- Tên biến nên diễn tả ý nghĩa nghiệp vụ: `amount_vnd` dễ hiểu hơn `a`.
- Python xác định kiểu tại lúc chạy (dynamic typing), nhưng không có nghĩa là mọi kiểu đều có thể cộng/trừ với nhau.

## 3. Các kiểu dữ liệu nền tảng

| Kiểu | Ví dụ | Ứng dụng |
|---|---|---|
| `str` | `"O001"`, `"PAID"` | ID, trạng thái; không dùng làm số tiền |
| `int` | `500000` | Tiền VND nguyên, số lượng |
| `float` | `0.15` | Số thực; không mặc nhiên phù hợp cho phép tính tiền cần độ chính xác tuyệt đối |
| `bool` | `True`, `False` | Cờ hợp lệ, cờ đã hoàn tiền |
| `NoneType` | `None` | Biểu diễn chưa có giá trị trong Python |

```python
order_id = "O001"
amount_vnd = 500000
is_paid = True
refund_amount = None

print(type(order_id))      # <class 'str'>
print(type(amount_vnd))    # <class 'int'>
print(type(is_paid))       # <class 'bool'>
print(type(refund_amount)) # <class 'NoneType'>
```

`None` không đồng nghĩa với `0`: `None` nghĩa là không có giá trị, còn `0` là số không đã biết. Cần xác định ngữ nghĩa nguồn dữ liệu trước khi gán giá trị mặc định.

## 4. Kiểm tra kiểu, phép tính và so sánh

```python
amount_vnd = 500000
fee_vnd = 20000
total_vnd = amount_vnd + fee_vnd

assert isinstance(amount_vnd, int)
assert total_vnd == 520000
assert amount_vnd > 0
```

- `type(x)` cho biết kiểu cụ thể; `isinstance(x, int)` kiểm tra quan hệ kiểu.
- Lưu ý `bool` là kiểu con của `int` trong Python: `isinstance(True, int)` là `True`. Khi kiểm tra số tiền nghiêm ngặt, phải cân nhắc từ chối boolean.
- Không cộng trực tiếp `"500000" + 20000`: chuỗi và số là hai kiểu khác nhau.
- Khi cần chuyển kiểu: `int("500000")` thành công, còn `int("abc")` gây `ValueError`.

## 5. Quy tắc nghiệp vụ cần tách khỏi kiểu dữ liệu

Có kiểu `int` chưa chứng minh `amount_vnd` hợp lệ: `-100000` vẫn là `int`. Việc `amount_vnd > 0` là **business rule** cho bài thực hành, không phải điều kiện chung cho mọi giao dịch. Refund có thể được mô hình hóa bằng loại giao dịch và amount riêng, tùy data contract.

## 6. Những lỗi thường gặp

- Nhầm `None` với `0`.
- Tin rằng dữ liệu từ API/CSV luôn đúng kiểu.
- Dùng `float` để tính tiền mà không xem xét độ chính xác.
- Nhầm gán `=` với so sánh `==`.
- Chỉ kiểm tra kiểu, không kiểm tra business rule.

## 7. Tự kiểm tra kiến thức

1. `order_id = "001"` thuộc kiểu gì, vì sao không nên chuyển mã đơn thành số?
2. `None` và `0` khác nhau thế nào trong dữ liệu hoàn tiền?
3. Tại sao `amount_vnd = -100000` vẫn có kiểu hợp lệ nhưng có thể vi phạm yêu cầu?
4. Vì sao cần kiểm tra dữ liệu nhận từ API/CSV trước khi tính toán?

## 8. Liên hệ với Data Engineering

Variable và data type là nền tảng cho schema, data validation, transform và kiểm tra chất lượng dữ liệu. Sau này, các quy tắc sẽ được thực thi rõ ràng hơn bằng Python, SQL và công cụ validation.

## 9. Tài liệu đi kèm

- [`exercises.py`](exercises.py): các ví dụ chạy được và `assert` minh họa.
- [Bài kế tiếp: List](../02-lists/knowledge-summary.md).

**Ghi chú tiến độ:** Tài liệu được bổ sung từ nội dung lý thuyết đã học; file ví dụ là lời giải tham khảo, chưa khẳng định người học tự hoàn thành bài tập code.
