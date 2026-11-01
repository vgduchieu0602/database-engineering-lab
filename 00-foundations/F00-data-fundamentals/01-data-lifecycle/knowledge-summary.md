## Duplicate Events, Deduplication & Idempotency

### 1. Duplicate Event

Duplicate Event xảy ra khi cùng một sự kiện logic được ghi nhận hoặc chuyển đến nhiều lần.

Ví dụ: Hệ thống thanh toán gửi lại sự kiện `E101` do không nhận được xác nhận từ hệ thống tiếp nhận.

### 2. Deduplication

Deduplication là quá trình nhận diện và xử lý các bản ghi trùng theo một quy tắc xác định.

Để nhận diện duplicate cần:

1. Xác định Data Grain: Mỗi dòng đại diện cho điều gì?
2. Xác định khóa định danh sự kiện.
3. Kiểm tra các bản ghi trùng và tính nhất quán của dữ liệu.
4. Áp dụng quy tắc xử lý phù hợp.

**Lưu ý:** Hai sự kiện có cùng `order_id` chưa chắc là duplicate. Một đơn hàng có thể có nhiều sự kiện hợp lệ.

### 3. Idempotency

Idempotency là tính chất của một thao tác mà khi thực hiện lặp lại với cùng đầu vào, trạng thái kết quả vẫn giống như thực hiện một lần.

Ví dụ: Xử lý lại cùng một sự kiện thanh toán không được ghi nhận doanh thu hai lần.

### 4. Persistent State

Dữ liệu chỉ lưu trong bộ nhớ chương trình thường bị mất khi tiến trình kết thúc.

Đối với pipeline cần khôi phục sau sự cố, thông tin về các sự kiện đã xử lý có thể cần được lưu bền vững, chẳng hạn trong database.

### 5. Các nguyên tắc cần nhớ

- Không xóa dữ liệu chỉ vì trùng `order_id`.
- Phải hiểu Data Grain trước khi deduplicate.
- Duplicate delivery có thể xảy ra khi hệ thống retry.
- Deduplication trong bộ nhớ không đủ để bảo đảm xử lý an toàn qua các lần khởi động.
- Có thể sử dụng database transaction và unique constraint để xây dựng cơ chế xử lý idempotent.