# Python Fundamentals — 03. Dictionary

> **Vai trò:** Tài liệu ôn tập và code mẫu, không phải bằng chứng đã hoàn thành toàn bộ bài thực hành.

## 1. Vấn đề thực tế

Một đơn hàng có nhiều thuộc tính: mã đơn, số tiền, trạng thái. Lưu dữ liệu theo vị trí dễ gây nhầm lẫn; Dictionary cho phép đặt **tên khóa có ý nghĩa**.

## 2. Dictionary là gì?

\`dict\` lưu các cặp \`key: value\`. Mỗi key duy nhất trong một Dictionary; value có thể là nhiều kiểu dữ liệu.

\`\`\`python
order = {
    "order_id": "O001",
    "amount": 500000,
    "status": "PAID",
}
print(order["order_id"])  # O001
\`\`\`

- \`order\` là Dictionary; \`"status"\` là key; \`"PAID"\` là value.
- Key phải hashable (ví dụ \`str\`, \`int\`, tuple chỉ gồm phần tử hashable); List không dùng làm key.
- Python Dictionary giữ thứ tự chèn key, nhưng trong xử lý dữ liệu cần truy cập theo tên key, không dựa vào vị trí.

## 3. Truy cập, thêm và cập nhật

\`\`\`python
order = {"order_id": "O001", "amount": 500000}
assert order["amount"] == 500000
order["status"] = "PAID"  # thêm key
order["amount"] = 550000 # cập nhật value
assert order["amount"] == 550000
\`\`\`

Nếu key không tồn tại:
- \`order["coupon_code"]\` gây \`KeyError\`.
- \`order.get("coupon_code")\` trả \`None\` nếu không có key.
- \`"coupon_code" in order\` kiểm tra key tồn tại.

Cẩn thận: \`get()\` trả \`None\` khi key thiếu **và** khi key có sẵn nhưng value là \`None\`. Muốn phân biệt, hãy dùng \`in\`.

## 4. List chứa Dictionary

\`\`\`python
orders = [
    {"order_id": "O001", "status": "PAID", "amount": 500000},
    {"order_id": "O002", "status": "FAILED", "amount": 300000},
]
assert orders[0]["status"] == "PAID"
\`\`\`

- \`orders\`: List gồm nhiều đơn hàng.
- \`orders[0]\`: Dictionary của đơn đầu tiên.
- \`orders[0]["status"]\`: String \`"PAID"\`.

Đây là cấu trúc phổ biến khi biểu diễn các bản ghi trả về từ API sau khi chuyển đổi JSON, nhưng vẫn cần schema validation.

## 5. Thiếu key, NULL và business rule

\`\`\`python
order = {"order_id": "O003", "refund_amount": None}
assert "refund_amount" in order
assert order["refund_amount"] is None
assert "status" not in order
\`\`\`

Ba trạng thái cần phân biệt trong pipeline:
1. **Key không có**: nguồn không gửi thuộc tính.
2. **Key có, value = \`None\`**: nguồn gửi thuộc tính nhưng chưa có giá trị (tùy contract).
3. **Key có, value = \`0\`**: một giá trị số đã biết.

Không tự động đổi mọi key thiếu hay \`None\` thành \`0\` vì có thể làm sai KPI.

## 6. Mutable và sao chép

Dictionary là mutable. \`copy()\` tạo bản sao nông (shallow copy): các value lồng nhau như List/Dictionary vẫn có thể được chia sẻ.

## 7. Lỗi thường gặp

- Truy cập key không tồn tại bằng \`[]\` → \`KeyError\`.
- Nhầm \`order\` là List hoặc \`orders\` là một Dictionary.
- Tưởng \`get()\` luôn phân biệt key thiếu với value \`None\`.
- Dùng tên key sai kiểu hoặc sai chữ hoa/thường.
- Tin rằng một Dictionary có đúng schema chỉ vì được viết ở dạng \`{ ... }\`.

## 8. Tự kiểm tra kiến thức

1. Trong \`{"amount": 500000}\`, phần nào là key và phần nào là value?
2. \`order["status"]\` khác gì \`order.get("status")\` khi key không tồn tại?
3. \`orders[1]["amount"]\` truy cập theo những bước nào?
4. Vì sao key bị thiếu không đồng nghĩa với amount bằng \`0\`?

## 9. Liên hệ Data Engineering

Dictionary thường đại diện cho một record đã parse. Ta dùng key để truy cập trường dữ liệu, kiểm tra sự tồn tại của field, chuẩn hóa và áp dụng schema/business validation. Các bước đó là nền cho \`for\` Loop và ETL.

## 10. Tài liệu đi kèm

- [\`exercises.py\`](exercises.py): ví dụ và assertions.
- [Bài kế tiếp: \`for\` Loop](../04-loops/knowledge-summary.md).

**Ghi chú tiến độ:** Tài liệu được bổ sung từ kiến thức đã thảo luận; ví dụ là tài liệu tham khảo, không khẳng định đã làm bài thực hành độc lập.
