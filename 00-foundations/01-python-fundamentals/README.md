# Python Fundamentals

## 1. Tổng quan

Module [Foundations](../README.md) dành cho người bắt đầu học Python từ cơ bản, theo hướng ứng dụng vào Data Engineering và Data Analytics. Các bài được học từng concept nhỏ trước khi kết hợp thành bài toán ETL.

## 2. Tại sao cần học?

Một pipeline có thể đọc nhiều đơn hàng, nhưng nếu chưa hiểu biến, kiểu dữ liệu, danh sách và bản ghi, rất dễ xử lý sai. Python Fundamentals cung cấp ngôn ngữ để biểu diễn và biến đổi dữ liệu trước khi học xử lý file, SQL, data quality và batch processing.

## 3. Kiến thức và tài liệu

| Thứ tự | Concept | Trọng tâm | Tài liệu |
|---|---|---|---|
| 01 | Variables & Data Types | `str`, `int`, `float`, `bool`, `None`, gán và so sánh | [Knowledge summary](01-variables-and-types/knowledge-summary.md) · [Code mẫu](01-variables-and-types/exercises.py) |
| 02 | Python List | Index, slicing, `append`, `len`, mutable | [Knowledge summary](02-lists/knowledge-summary.md) · [Code mẫu](02-lists/exercises.py) |
| 03 | Python Dictionary | Key-value, `[]`, `get()`, key thiếu, cập nhật | [Knowledge summary](03-dictionaries/knowledge-summary.md) · [Code mẫu](03-dictionaries/exercises.py) |
| 04 | Python `for` Loop | Duyệt List chứa Dictionary, `if`, `and`, cộng dồn | [Knowledge summary](04-loops/knowledge-summary.md) · [Bài thực hành](04-loops/exercises.py) |
| 05 | Python `while` Loop | Điều kiện lặp, slicing theo batch, cập nhật trạng thái, tránh lặp vô hạn | [Knowledge summary](05-while-loop/knowledge-summary.md) · [Bài thực hành](05-while-loop/exercises.py) |
| 06 | Functions | Tham số, giá trị trả về, tái sử dụng logic | Sẽ tạo khi học |
| 07 | Error Handling | `try`/`except`, phân biệt lỗi dữ liệu và lỗi chương trình | Sẽ tạo khi học |
| 08 | File I/O & Modules | Đọc/ghi file, import, tổ chức code | Sẽ tạo khi học |

> Việc có tài liệu trên GitHub **không đồng nghĩa** đã hoàn thành bài thực hành độc lập. Các file trong 01–03 là code tham khảo để ôn tập; 04–05 có bài thực hành đã được trao đổi và đánh giá trong quá trình học.

## 4. Kiến thức cần có trước

Không bắt buộc biết Python từ trước. Có thể dùng Python 3 và terminal cơ bản để chạy ví dụ.

## 5. Công nghệ và công cụ

- Python 3: ngôn ngữ chính.
- Git/GitHub: lưu kiến thức và bằng chứng học tập.
- SQL/PostgreSQL: sẽ kết hợp trong các module sau.

## 6. Ứng dụng thực tế

Dùng mô hình đơn hàng NovaCommerce để biểu diễn record, xác định kiểu dữ liệu, lưu nhiều record trong List, đọc Dictionary, kiểm tra các trường và lọc đơn hàng theo business rule. Đây là ví dụ học thuật, chưa phải ETL production.

## 7. Kết quả mong đợi

Người học có thể giải thích lại từng concept bằng lời đơn giản, tự viết và chạy code cơ bản, xác định input/output, chỉ ra business rule, kiểm tra kết quả và lưu bằng chứng phù hợp. Mỗi concept được đánh giá trước khi đi tiếp.

## 8. Workflow học tập và lưu GitHub

1. Học một concept theo Problem → Concept → Tiny Example → Code → Explain Back → Why.
2. Tự trả lời, thực hành và được đánh giá. Chỉ chuyển tiếp khi đạt tối thiểu 8/10.
3. Đọc `knowledge-summary.md` để ôn kiến thức; code mẫu không thay thế phần thực hành của người học.
4. Khi có bài làm được kiểm tra, bổ sung bằng chứng code/test và commit lên GitHub.
5. Không đánh dấu module hay project hoàn thành chỉ vì đã tạo README.

## 9. Học tiếp nội dung nào?

Sau `while` Loop, học Functions, rồi Error Handling. Khi có nền tảng Python, tiếp tục [Python for Data](../02-python-for-data/README.md).
