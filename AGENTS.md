# AGENTS.md — [PROJECT_NAME] Project Rules for AI Agents

File này là hướng dẫn vận hành cho AI agent (DeepSeek, Claude, Gemini, Codex) khi làm việc với dự án [PROJECT_NAME].

---

## Nguyên tắc cốt lõi

1. **SSOT (Single Source of Truth)** — Mỗi entity (project, person, ticket, sprint, version, requirement, document) có **đúng một** file `.md` là nguồn dữ liệu gốc.
2. **Không trùng lặp** — Không lưu cùng một thông tin ở nhiều nơi. Dùng ID hoặc đường dẫn để tham chiếu.
3. **Markdown-first** — Toàn bộ dữ liệu quản lý ở định dạng Markdown với YAML frontmatter.

---

## Cấu trúc thư mục

| Thư mục | Mục đích |
|---------|----------|
| `rules/` | Quy tắc chi tiết: project, workflow, validation, requirement |
| `projects/` | Định nghĩa dự án |
| `people/` | Hồ sơ thành viên |
| `sprints/` | File theo dõi sprint |
| `versions/` | Theo dõi phiên bản release |
| `tickets/` | Dữ liệu ticket (nguồn gốc cho task) |
| `requirements/` | Yêu cầu trước khi chuyển thành ticket |
| `feedbacks/` | Dữ liệu feedback/phản ánh từ người dùng |
| `docs/` | Tài liệu kỹ thuật (solution, design, api, testcases) |

---

## Quy tắc vận hành bắt buộc

### 1. Tuân thủ rule file
- **Luôn** đọc và tuân theo các file trong `rules/` trước khi thao tác:
  - `rules/project-rules.md` — Quy tắc chung dự án
  - `rules/workflow-rules.md` — Vòng đời ticket & luồng handoff
  - `rules/validation-rules.md` — Quy tắc validate trước khi ghi file
  - `rules/requirement-rules.md` — Quy tắc quản lý yêu cầu
  - `rules/feedback-rules.md` — Quy tắc quản lý feedback/phản ánh

### 2. Metadata bắt buộc cho ticket
Khi tạo/cập nhật ticket, **phải có đủ** các trường metadata:
- `ticket_key`, `title`, `status`, `priority`
- `assignees` (BA, dev_app, dev_web, dev_backend, tester)
- `sprint_code`, `jira_url`, `document_links`
- `parent_key` / `sub_tasks` (nếu có)

### 3. Liên kết hai chiều (Bidirectional links)
- Parent ticket phải liệt kê `sub_tasks`, sub-ticket phải có `parent_key`.
- Sprint file phải liệt kê `ticket_keys`, ticket phải có `sprint_code`.
- Requirement khi chuyển thành ticket phải cập nhật `related_tickets`.

### 4. Git synchronization
- **Cuối mỗi session, phải commit và push** mọi thay đổi lên remote repository.
- Commit message rõ ràng, mô tả thay đổi đã thực hiện.
- **Trước khi commit, cập nhật `README.md`** nếu có thay đổi về số liệu (ticket mới, đổi status, assignee, version). Quét lại toàn bộ ticket/version/requirement file để lấy số liệu chính xác, không dùng số cũ từ memory.

### 5. Ngôn ngữ
- Tài liệu dự án và metadata dùng **tiếng Việt**.
- Tên file, key, mã định danh giữ nguyên dạng gốc.

---

## Quy trình ticket

```
backlog → refined → analysis → ready_for_dev → in_progress → ready_for_test → testing → ready_for_release → released → done
                                                                                                      ↘ cancelled
```

### Điều kiện chuyển trạng thái chính:
| Chuyển trạng thái | Điều kiện |
|-------------------|-----------|
| `analysis` → `ready_for_dev` | Có `short_description`, `title`, `document_links` chứa `solution`, BA được gán, ít nhất 1 component |
| `ready_for_dev` → `in_progress` | Có assignee cho mỗi component và handoff plan |
| `in_progress` → `ready_for_test` | Code đã push/merge, build testable sẵn sàng |
| `testing` → `ready_for_release` | Có tester, test pass/approved, blocker đã resolved |
| `ready_for_release` → `released` | Có `release_time` và `build_version` |

---

## Validate trước khi ghi file

Trước mọi thao tác ghi, agent phải kiểm tra:
1. **Jira URL** đúng format `https://10.30.165.157/jira/browse/[PREFIX]-XXX`
2. **Username** trong `assignees` tồn tại trong `people/`
3. **Sprint** tồn tại trong `sprints/` và có liệt kê ticket
4. **Version** tồn tại trong `versions/`
5. **Parent/Sub liên kết hai chiều**
6. **Document links** trỏ đến file tồn tại, type hợp lệ

---

## Tham chiếu nhanh

- Ticket key format: `[PREFIX]-XXX` (VD: `[PREFIX]-1005`)
- Jira URL format: `https://10.30.165.157/jira/browse/[PREFIX]-XXX`
- Requirement ID format: `REQ-YYYYMMDD-XXX`
- Feedback ID format: `FB-YYYYMMDD-XXX`
- Sprint code format: `[PREFIX] Sprint T{N} tháng {MM}`
