# Quy tắc Quản lý Feedback - [PROJECT_NAME]

## 1. Định nghĩa
Feedback (Phản ánh) là các thông tin, lỗi phát sinh, yêu cầu hỗ trợ hoặc đề xuất cải tiến từ phía người dùng gửi về dự án [PROJECT_NAME] qua các kênh truyền thông khác nhau. Feedback cần được quản lý chặt chẽ để đảm bảo khả năng truy vết và xử lý triệt để.

## 2. Quy ước định danh và Lưu trữ
- Mã định danh tạm thời: `FB-YYYYMMDD-XXX` (Ví dụ: `FB-20260520-001`).
- Mỗi feedback được lưu dưới dạng một file Markdown (`.md`) riêng biệt trong thư mục `feedbacks/`.

## 3. Metadata chuẩn cho Feedback (Frontmatter)

Mọi file Feedback phải có đầy đủ YAML frontmatter sau:

```yaml
---
entity: feedback
fb_id: FB-YYYYMMDD-XXX
title: Tiêu đề tóm tắt phản ánh
reporter:
  name: Tên người phản ánh
  contact: Thông tin liên lạc (SĐT/Email/Username)
channel: whatsapp           # whatsapp | vops | phone | email | direct | other
fb_type: system_error       # system_error | proposal | support | other
fb_group: "Tên nhóm chat"   # Tên nhóm chat trên kênh truyền thông để truy vết sau này
handler: username           # Username của người tiếp nhận & xử lý chính (phải có trong people/)
collaborators: []           # Danh sách username phối hợp xử lý (phải có trong people/)
progress: open              # open | in_progress | resolved | closed
result: ""                  # Kết quả xử lý thực tế (bắt buộc khi trạng thái là resolved/closed)
updates:                    # Danh sách nhật ký tiến độ công việc kèm thời điểm cập nhật
  - date: "YYYY-MM-DD HH:MM" # Thời điểm cập nhật
    author: username        # Người cập nhật (phải có trong people/)
    content: "Mô tả tiến độ công việc"
created_date: 2026-05-20    # Ngày tiếp nhận
updated_date: 2026-05-20    # Ngày cập nhật gần nhất
related_tickets: []         # Danh sách các ticket [PREFIX]-XXX liên quan (nếu có)
---
```

## 4. Trạng thái và Luồng xử lý (Progress)

- `open`: Feedback mới tiếp nhận, đang chờ đánh giá và phân công người xử lý.
- `in_progress`: Đang trong quá trình xử lý hoặc đang phát triển các ticket liên quan.
- `resolved`: Đã xử lý xong kỹ thuật hoặc đã khắc phục lỗi, đang chờ xác nhận từ người phản ánh.
- `closed`: Đã phản hồi lại cho người gửi và đóng feedback thành công.

## 5. Quy tắc vận hành và Xác thực cho Agent

1. **Khả năng truy vết (Traceability):**
   - Trường `fb_group` là bắt buộc và phải điền chính xác tên nhóm chat nguồn (ví dụ: `"WhatsApp Group [PROJECT_NAME] Support"`) để phục vụ việc tra cứu lịch sử hội thoại sau này.
2. **Hợp lệ Nhân sự và Vai trò:**
   - **Người phản ánh (Reporter):** Thông tin người dùng/khách hàng gửi phản ánh (ghi nhận ở trường `reporter` dưới dạng text tự do, gồm Tên, SĐT, Email).
   - **Người tiếp nhận & xử lý chính (Handler):** Thành viên nội bộ [PROJECT_NAME] trực tiếp tiếp nhận thông tin từ kênh chat và chịu trách nhiệm xử lý chính (username trong `handler` phải tồn tại thực tế trong thư mục `people/`).
   - **Người phối hợp (Collaborators):** Các thành viên nội bộ [PROJECT_NAME] tham gia hỗ trợ giải quyết (các username trong danh sách `collaborators` phải tồn tại thực tế trong thư mục `people/`).
   - **Nhật ký tiến độ (Updates):** Mỗi bản ghi nhật ký tiến độ trong `updates` phải ghi nhận rõ thời điểm `date` (định dạng `YYYY-MM-DD HH:MM`), người cập nhật `author` (phải tồn tại thực tế trong thư mục `people/`), và nội dung tiến độ cụ thể `content`.
3. **Mối liên kết hai chiều:**
   - Nếu một feedback cần giải quyết bằng code/task kỹ thuật, Agent phải tạo ticket tương ứng (ví dụ: `[PREFIX]-1035`) và điền key vào danh sách `related_tickets` của feedback, đồng thời trong ticket đó phải liên kết ngược lại đường dẫn của file feedback ở phần `document_links`.
4. **Kết quả xử lý:**
   - Khi chuyển trạng thái `progress` sang `resolved` hoặc `closed`, Agent **bắt buộc** phải điền nội dung kết quả xử lý cụ thể vào trường `result` (không được để trống).
5. **Cập nhật Dashboard:**
   - Sau khi tạo mới hoặc cập nhật bất kỳ feedback nào, Agent phải chạy script quét và cập nhật lại bảng thống kê feedback trên `README.md`.
