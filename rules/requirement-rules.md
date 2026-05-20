# Requirement Rules - [PROJECT_NAME]

## 1. Định nghĩa
Yêu cầu (Requirement) là các đề xuất tính năng, thay đổi hoặc fix bug từ phía khách hàng hoặc nội bộ trước khi được chuyển thành ticket chính thức.

## 2. Quy ước định danh
- Mã yêu cầu tạm thời có dạng: `REQ-YYYYMMDD-XXX` (Ví dụ: `REQ-20260506-001`).
- Mỗi yêu cầu được lưu trong một file riêng tại thư mục `requirements/`.

## 3. Metadata chuẩn cho Requirement

```yaml
---
entity: requirement
req_id: REQ-20260506-001
title: Tiêu đề yêu cầu
requester:
  name: Tên người yêu cầu
  org: Đơn vị/Phòng ban
request_date: 2026-05-06
priority: medium
status: draft
tags: []
related_tickets: []
---
```

## 4. Trạng thái của Requirement
- `draft`: Đang khởi tạo.
- `submitted`: Đã gửi yêu cầu.
- `reviewing`: Đang xem xét/đánh giá.
- `accepted`: Đã chấp thuận (sẵn sàng chuyển thành ticket).
- `rejected`: Đã từ chối.
- `converted`: Đã chuyển thành ticket (phải có `related_tickets`).

## 5. Quy tắc vận hành
- Mọi yêu cầu phải có thông tin `requester`.
- Khi chuyển trạng thái sang `converted`, agent phải cập nhật danh sách `related_tickets`.
- File yêu cầu không được xóa sau khi convert để giữ lịch sử.
