# Distributed Batch Processing

## 1. Project Overview

- **Cấp độ:** Middle
- **Mục tiêu:** Xử lý PySpark, partitioning, join strategy, shuffle và benchmark.
- **Công nghệ dự kiến:** Python, SQL, PostgreSQL và công cụ phù hợp; người học phải giải thích lựa chọn.

## 2. Business Context

NovaCommerce là doanh nghiệp thương mại điện tử giả lập cần dữ liệu đáng tin cậy để vận hành và ra quyết định.

## 3. Business Problem

Xử lý một máy không đáp ứng thời gian chạy và chi phí mục tiêu.

## 4. Stakeholders

Business owner dùng đầu ra; Data Engineer/Data Analyst chịu trách nhiệm dữ liệu; chủ nguồn xác nhận ngữ nghĩa và thay đổi schema.

## 5. Project Objectives

Cung cấp đầu ra đáp ứng business problem, có quy tắc dữ liệu rõ, khả năng kiểm tra và tài liệu hóa đánh đổi.

## 6. Scope

Xử lý PySpark, partitioning, join strategy, shuffle và benchmark.

## 7. Out of Scope

Không yêu cầu dữ liệu thật, ứng dụng khách hàng, SLA production hoặc phạm vi ngoài nghiệp vụ nêu trên.

## 8. Data Sources

Dữ liệu giao dịch lớn dạng Parquet. Người học phải mô tả schema đề xuất, business key, độ mới, volume và rủi ro chất lượng; không tạo dữ liệu mẫu trong roadmap.

## 9. Functional Requirements

- **FR-001:** Phải tiếp nhận và lưu vết nguồn: Dữ liệu giao dịch lớn dạng Parquet.
- **FR-002:** Phải áp dụng quy tắc: Partition key phải phù hợp truy vấn; benchmark dùng cùng dữ liệu; phải đo shuffle.
- **FR-003:** Phải tạo đầu ra trực tiếp giải quyết: Xử lý một máy không đáp ứng thời gian chạy và chi phí mục tiêu.
- **FR-004:** Phải đối chiếu count hoặc KPI nguồn–đích và báo cáo chênh lệch.
- **FR-005:** Phải cung cấp trạng thái chạy, lỗi và đường xử lý bản ghi bất thường.

## 10. Non-Functional Requirements

- Reliability: chạy lại không tạo sai lệch kết quả.
- Performance: đặt và đo **training target** phù hợp volume giả định.
- Security: không phơi lộ PII trong log/đầu ra không được cấp quyền.
- Maintainability: cấu hình và quy tắc có tài liệu.
- Observability: có log, metric hoặc trạng thái đủ điều tra lỗi.

## 11. Business Rules

Partition key phải phù hợp truy vấn; benchmark dùng cùng dữ liệu; phải đo shuffle Quy tắc phải có nguồn sở hữu và cách xử lý trường hợp vi phạm.

## 12. Expected Architecture

Dữ liệu giao dịch lớn dạng Parquet → lớp tiếp nhận/staging → kiểm tra và biến đổi → lớp dữ liệu phục vụ → đầu ra cho stakeholder. Thành phần cụ thể phụ thuộc vào quyết định có lý do của người học.

## 13. Expected Deliverables

Tài liệu kiến trúc, schema/contract, pipeline hoặc mô hình dữ liệu, bằng chứng chất lượng, đầu ra stakeholder và hướng dẫn vận hành ngắn.

## 14. Acceptance Criteria

- FR-001 đến FR-005 có bằng chứng kiểm tra được.
- Quy tắc tại Business Rules được áp dụng nhất quán.
- Có đối chiếu nguồn–đích và giải thích chênh lệch.
- Có bằng chứng xử lý lỗi hoặc chạy lại.
- Stakeholder giả lập có thể dùng đầu ra để trả lời business problem.

## 15. Testing Expectations

Xác minh đường đi dữ liệu, quy tắc nghiệp vụ, dữ liệu thiếu/trùng/muộn, chạy lại, đối chiếu KPI và khả năng quan sát; không yêu cầu test case chi tiết.

## 16. Prerequisites

Distributed Processing; Data Formats; Performance Optimization.

## 17. Difficulty & Learning Outcomes

Độ khó **Middle**. Project chứng minh năng lực biến yêu cầu nghiệp vụ thành tiêu chí kiểm chứng và quyết định kỹ thuật.

## 18. Optional Enhancements

Bổ sung data contract, cảnh báo, tối ưu chi phí, CI/CD hoặc khả năng self-service sau khi scope chính hoàn thành.

## 19. Definition of Done

Tất cả acceptance criteria có bằng chứng; testing expectations được đáp ứng; giới hạn còn lại được nêu rõ. Hoàn thành project không tự động đồng nghĩa đạt chức danh nghề nghiệp.
