# Python Fundamentals — 02. List

> **Vai trò:** Tài liệu kiến thức và code mẫu. Không tự động chứng minh người học đã làm xong bài thực hành.

## 1. Vấn đề thực tế

Một lần đọc file CSV có thể trả về nhiều mã đơn hoặc nhiều bản ghi. Cần một cấu trúc để giữ **một tập hợp có thứ tự** và thao tác trên từng phần tử.

## 2. List là gì?

\`list\` là một collection có thứ tự (ordered), có thể thay đổi (mutable), cho phép phần tử trùng lặp và có thể chứa nhiều kiểu dữ liệu.

\`\`\`python
order_ids = ["O001", "O002", "O003"]
print(order_ids[0])   # O001
print(order_ids[-1])  # O003
print(len(order_ids)) # 3
\`\`\`

- Index bắt đầu từ \`0\`, index âm đếm từ cuối.
- Truy cập vị trí không tồn tại gây \`IndexError\`.
- \`len(list)\` trả số phần tử, không phải tổng các giá trị số.

## 3. Các thao tác cơ bản

\`\`\`python
order_ids = ["O001", "O002"]
order_ids.append("O003")    # thêm một phần tử ở cuối
order_ids[1] = "O002-NEW"   # thay đổi phần tử thứ hai
first_two = order_ids[:2]  # tạo list mới từ lát cắt
assert len(order_ids) == 3
\`\`\`

| Thao tác | Ý nghĩa |
|---|---|
| \`items[i]\` | Lấy phần tử tại index \`i\` |
| \`items.append(x)\` | Thêm một phần tử vào cuối |
| \`items[i] = x\` | Thay thế phần tử ở index \`i\` |
| \`len(items)\` | Số lượng phần tử |
| \`x in items\` | Kiểm tra có giá trị \`x\` không |
| \`items[a:b]\` | Cắt đoạn từ index \`a\` đến trước \`b\` |

## 4. List có thể chứa Dictionary

\`\`\`python
orders = [
    {"order_id": "O001", "amount": 500000},
    {"order_id": "O002", "amount": 300000},
]

assert orders[0]["order_id"] == "O001"
assert orders[1]["amount"] == 300000
\`\`\`

Ở đây:
- \`orders\` là một List.
- \`orders[0]\` là Dictionary đầu tiên.
- \`orders[0]["amount"]\` là giá trị của key \`amount\` trong Dictionary đầu tiên.

## 5. Mutable và aliasing

\`\`\`python
a = ["O001"]
b = a
b.append("O002")
assert a == ["O001", "O002"]
\`\`\`

\`a\` và \`b\` cùng tham chiếu một List, nên sửa qua \`b\` sẽ thấy thay đổi qua \`a\`. Nếu cần một List mới ở mức nông, có thể dùng \`a.copy()\`; các đối tượng lồng nhau vẫn có thể được chia sẻ.

## 6. Lưu ý Data Engineering

List là cấu trúc thuận tiện cho dữ liệu nhỏ và bài tập. Giữ toàn bộ hàng triệu bản ghi trong một List có thể làm tốn RAM. Ở các bài nâng cao sẽ học cách đọc dữ liệu theo batch hoặc sử dụng hệ quản trị dữ liệu phù hợp. List cũng **không tự động xóa trùng**.

## 7. Lỗi thường gặp

- Tưởng phần tử đầu tiên là index \`1\`.
- Nhầm \`len(orders)\` với tổng \`amount\`.
- Nghĩ \`append\` tạo List mới (thực ra thay đổi List hiện tại và trả về \`None\`).
- Nhầm \`orders[0]\` với \`orders\` hoặc \`orders[0]["order_id"]\`.
- Thay đổi List qua một biến rồi bất ngờ thấy biến khác cũng đổi.

## 8. Tự kiểm tra kiến thức

1. Kết quả của \`["A", "B"][-1]\` là gì?
2. \`len(orders)\` có phải là tổng doanh thu không?
3. \`orders[0]\` là kiểu dữ liệu gì nếu \`orders\` là List chứa Dictionary?
4. Khi nào \`append\` phù hợp, khi nào không nên nạp mọi bản ghi vào RAM?

## 9. Tài liệu đi kèm

- [\`exercises.py\`](exercises.py): ví dụ minh họa có kiểm tra bằng \`assert\`.
- [Bài kế tiếp: Dictionary](../03-dictionaries/knowledge-summary.md).

**Ghi chú tiến độ:** Đây là tài liệu kiến thức; code mẫu không được ghi thành kết quả thực hành cá nhân chưa kiểm chứng.
