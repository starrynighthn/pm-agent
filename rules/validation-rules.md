# Validation Rules - [PROJECT_NAME]

The agent must validate the following before writing any file:

1. **Jira Link**: `jira_url` must match `https://10.30.165.157/jira/browse/<ticket_key>`.
2. **People**: All usernames in `assignees` must exist in `people/` directory and their roles must match the assigned role.
3. **Sprint**: `sprint_code` must exist in `sprints/` and the sprint file must list the `ticket_key`.
4. **Version**: Referenced version codes must exist in `versions/`. `build_versions` must not be null if `release_time` is set for that platform.
5. **Parent/Sub-ticket**: Parent-child relationships must be bidirectional (parent lists sub-ticket, sub-ticket lists parent).
6. **Documents**: All paths in `document_links` must exist. Types must be one of: `solution`, `design`, `api`, `testcases`, `meeting_note`, `release_note`, `other`.
7. **Readiness Flags**: `has_solution_doc`, `has_design`, `has_api_backend`, etc., should be automatically inferred from existing documents and user confirmations.
8. **Feedback Rules**: For any feedback file under `feedbacks/`:
   - `fb_id` must match `FB-YYYYMMDD-XXX`.
   - `handler` must exist in `people/` directory (who received & handles the feedback).
   - Any username in `collaborators` must exist in `people/` directory.
   - Each update in `updates` must have a valid `author` (exists in `people/`), a `date` formatted as `YYYY-MM-DD HH:MM`, and a non-empty `content`.
   - `channel` must be one of: `whatsapp`, `vops`, `phone`, `email`, `direct`, `other`.
   - `fb_type` must be one of: `system_error`, `proposal`, `support`, `other`.
   - `fb_group` (chat group name) must not be empty or null.
   - If `progress` is `resolved` or `closed`, the `result` field must contain a non-empty string explaining the outcome.
9. **Requirement Rules**: For any requirement file under `requirements/`:
    - `req_id` must match `REQ-YYYYMMDD-XXX`.
    - `requester` must contain a non-empty `name` and `org`.
    - `status` must be one of: `draft`, `submitted`, `reviewing`, `accepted`, `rejected`, `converted`.
    - If `status` is `converted`, the `related_tickets` field must not be empty and must list at least one valid ticket key.
