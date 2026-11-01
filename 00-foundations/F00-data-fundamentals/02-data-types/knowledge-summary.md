# F0.2 — Structured Data Fundamentals

## 1. Structured Data

Structured Data là dữ liệu được tổ chức theo một cấu trúc xác định rõ ràng, thường biểu diễn dưới dạng bảng có hàng và cột.

### Thành phần

- **Row:** Một bản ghi dữ liệu.
- **Column:** Một thuộc tính của bản ghi.
- **Value:** Giá trị của một thuộc tính tại một bản ghi.
- **Schema:** Mô tả cấu trúc, kiểu dữ liệu và các quy tắc liên quan.
- **Data Grain:** Xác định mỗi dòng đại diện cho điều gì.

## 2. Data Types

| Type | Ý nghĩa | Ví dụ |
|---|---|---|
| INTEGER | Số nguyên | 100, 250 |
| DECIMAL | Số thập phân chính xác | 10.50 |
| TEXT | Chuỗi ký tự | "EMP001" |
| BOOLEAN | Giá trị đúng/sai | true, false |
| DATE | Ngày | 2026-11-01 |
| TIMESTAMP | Ngày và thời gian | 2026-11-01 10:30:00 |

## 3. NULL vs Zero

- `0` là giá trị số đã xác định.
- `NULL` biểu thị không có giá trị được xác định.
- Không tự động thay `NULL` bằng `0` nếu chưa có business rule.
- Cần xem xét tác động của giá trị thiếu đến kết quả phân tích.

## 4. Data Type Selection

Khi chọn kiểu dữ liệu cần cân nhắc:

1. Ý nghĩa nghiệp vụ của trường dữ liệu.
2. Phạm vi giá trị.
3. Độ chính xác cần thiết.
4. Cách dữ liệu được truy vấn và tính toán.
5. Quy tắc kiểm tra và ràng buộc dữ liệu.

Ví dụ: Số điện thoại nên lưu dạng chuỗi vì cần giữ số 0 đầu tiên và không được dùng cho phép tính số học.

## 5. Structured Data không đồng nghĩa với Clean Data

Dữ liệu có cấu trúc vẫn có thể chứa:

- Duplicate records.
- Missing values.
- Invalid values.
- Inconsistent values.
- Outdated records.

Do đó, cần kết hợp schema với data validation và data quality checks.

## 6. Nguyên tắc cần ghi nhớ

- Xác định Data Grain trước khi thiết kế hoặc phân tích bảng.
- Chọn kiểu dữ liệu theo ý nghĩa, không chỉ theo hình thức.
- Không nhầm lẫn `NULL` với `0`.
- Không dùng kiểu số cho mã định danh chỉ vì nó chứa chữ số.
- Không mặc định Structured Data là dữ liệu đáng tin cậy.