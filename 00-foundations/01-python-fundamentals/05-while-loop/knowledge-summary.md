# Lesson 09 — Python `while` Loop

> **Phạm vi:** Kiến thức nền tảng và bài tập NovaCommerce. Đây là bản tổng hợp kiến thức dùng để ôn tập, không phải nhật ký lỗi hoặc đánh giá cá nhân.

## 1. Bài toán

NovaCommerce có danh sách đơn hàng và muốn chia thành các nhóm (batch), mỗi nhóm tối đa `batch_size` phần tử. Số lượng phần tử có thể không chia hết cho kích thước batch.

## 2. Khái niệm `while`

Vòng lặp `while` chạy phần thân **chừng nào điều kiện còn là `True`**. Điều kiện được kiểm tra trước mỗi lần lặp.

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

Kết quả: `1`, `2`, `3` (mỗi giá trị trên một dòng). Khi `count` thành `4`, điều kiện sai và vòng lặp kết thúc.

## 3. Các thành phần cần hiểu

- **Biến trạng thái:** `start` lưu index đầu tiên chưa được xử lý.
- **Điều kiện dừng:** `start < len(orders)` có nghĩa là vẫn còn phần tử ở vị trí `start`.
- **Slicing:** `orders[start:start + batch_size]` lấy phần tử từ `start` đến trước index `start + batch_size`.
- **Cập nhật trạng thái:** `start += batch_size` chuyển đến vị trí bắt đầu của batch kế tiếp.
- **Đánh số batch:** `batch_number += 1` cập nhật số thứ tự nhóm.

`len(orders)` trả về số phần tử của List, không phải tổng giá trị các đơn hàng.

## 4. Ví dụ batch processing

```python
orders = ["O001", "O002", "O003", "O004", "O005", "O006", "O007"]
batch_size = 3
start = 0
batch_number = 1

while start < len(orders):
    batch = orders[start:start + batch_size]
    print(f"Batch {batch_number}: {batch}")
    start += batch_size
    batch_number += 1
```

Kết quả mong đợi:

```text
Batch 1: ['O001', 'O002', 'O003']
Batch 2: ['O004', 'O005', 'O006']
Batch 3: ['O007']
```

Batch cuối chỉ có một phần tử: slicing trong Python tự lấy đến hết List nếu index kết thúc vượt độ dài.

## 5. Truy vết trạng thái

| Trước vòng lặp | Kiểm tra | Slicing | `start` sau khi cập nhật |
|---|---|---|---|
| `start = 0` | `0 < 7` → True | `orders[0:3]` | 3 |
| `start = 3` | `3 < 7` → True | `orders[3:6]` | 6 |
| `start = 6` | `6 < 7` → True | `orders[6:9]` | 9 |
| `start = 9` | `9 < 7` → False | Không chạy | Dừng |

## 6. `for` và `while`

- `for`: thích hợp khi muốn duyệt từng phần tử của iterable.
- `while`: thích hợp khi tiến trình cần tiếp tục dựa trên điều kiện trạng thái.
- Nhiều bài toán có thể giải bằng cả hai; lựa chọn phụ thuộc vào cách biểu diễn vòng lặp rõ ràng nhất.

## 7. Lỗi cần tránh

1. **Vòng lặp vô hạn:** quên cập nhật `start`, hoặc cập nhật không tiến tới điều kiện dừng.
2. **Batch rỗng/lặp sai:** không kiểm soát `batch_size`. Với thuật toán này, phải đảm bảo `batch_size > 0`.
3. **Lệch index:** dùng `<= len(orders)` thay cho `< len(orders)` có thể gây ra một batch rỗng.
4. **Nhầm slicing với đọc dữ liệu theo batch:** ví dụ chỉ chia List đã nằm trong RAM; không tự giảm RAM đã dùng để tải toàn bộ danh sách.
5. **Quên batch cuối:** tổng số phần tử không nhất thiết chia hết cho `batch_size`.

## 8. Kiểm tra thêm

- `orders = []`: không tạo batch nào.
- `len(orders) < batch_size`: có đúng một batch chứa toàn bộ orders.
- `len(orders) % batch_size == 0`: không sinh batch rỗng cuối.
- `batch_size <= 0`: cần được phát hiện và từ chối nếu xây dựng hàm dùng lại.

## 9. Ứng dụng Data Engineering

Trong pipeline thực tế, có thể sử dụng `while` để tiếp tục lấy API pagination khi còn `next_page`, hoặc để điều phối việc đọc từng nhóm từ nguồn. Tuy nhiên, thao tác slicing một List đã tải sẵn không thay thế cho ingestion theo batch từ file/database/API.

## 10. Tài liệu và điều kiện hoàn thành

- [`exercises.py`](exercises.py): bài làm chia 7 đơn hàng thành batch, với kết quả mong đợi.
- Có thể giải thích điều kiện dừng, slicing, thay đổi trạng thái và hành vi khi batch cuối ngắn.
- Bài thực hành đã được người học gửi và được đánh giá trong cuộc trao đổi; ví dụ không khẳng định đã có kiểm thử tự động toàn diện.

**Tiếp theo:** Python Functions — biến logic thành hàm có tham số và giá trị trả về.
