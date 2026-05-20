# Feedback Management Rules - [PROJECT_NAME]

## 1. Definition
Feedback refers to user reports, system errors, support requests, or improvement suggestions sent by users to the [PROJECT_NAME] project through various communication channels. Feedback must be managed carefully to ensure full traceability and complete resolution.

## 2. Naming and Storage Conventions
- Temporary feedback identifier format: `FB-YYYYMMDD-XXX` (e.g., `FB-20260520-001`).
- Each feedback is saved as an individual Markdown (`.md`) file in the `feedbacks/` directory.

## 3. Standard Metadata for Feedback (Frontmatter)

Every feedback file must contain the following YAML frontmatter:

```yaml
---
entity: feedback
fb_id: FB-20260520-001
title: Summary title of the feedback
reporter:
  name: Reporter's name
  contact: Contact information (Phone/Email/Username)
channel: whatsapp           # whatsapp | vops | phone | email | direct | other
fb_type: system_error       # system_error | proposal | support | other
fb_group: "Chat Group Name" # Name of the chat group or channel for traceability
handler: username           # Primary handler's username (must exist in people/)
collaborators: []           # List of collaborating usernames (must exist in people/)
progress: open              # open | in_progress | resolved | closed
result: ""                  # Actual outcome/result (mandatory when status is resolved/closed)
updates:                    # List of progress updates with timestamps
  - date: "YYYY-MM-DD HH:MM" # Timestamp of the update
    author: username        # Author of the update (must exist in people/)
    content: "Description of progress made"
created_date: 2026-05-20    # Received date
updated_date: 2026-05-20    # Last updated date
related_tickets: []         # List of related [PREFIX]-XXX tickets (if any)
---
```

## 4. Status and Handoff Flow (Progress)

- `open`: Newly received feedback, waiting for evaluation and assignment.
- `in_progress`: Under resolution or when related tickets are in development.
- `resolved`: Technical resolution or fix completed, waiting for verification from the reporter.
- `closed`: Successfully resolved, feedback provided to the reporter, and ticket closed.

## 5. Operational and Validation Rules for Agents

1. **Traceability:**
   - The `fb_group` field is mandatory and must accurately capture the source chat group name (e.g., `"WhatsApp Group [PROJECT_NAME] Support"`) to assist in conversational tracking.
2. **Personnel & Roles Validation:**
   - **Reporter:** Customer/user who submitted the feedback (recorded in the `reporter` field as free-form text containing Name, Phone, and/or Email).
   - **Handler:** Internal [PROJECT_NAME] team member who received and takes primary responsibility for the feedback (the username in `handler` must exist under the `people/` directory).
   - **Collaborators:** Internal [PROJECT_NAME] team members assisting in the resolution (usernames in `collaborators` must exist under the `people/` directory).
   - **Updates Log:** Every log entry in `updates` must record a valid `date` (format: `YYYY-MM-DD HH:MM`), a valid `author` (must exist under the `people/` directory), and a non-empty `content` describing progress.
3. **Bidirectional Linking:**
   - If a feedback requires technical implementation, the Agent must create a corresponding ticket (e.g., `[PREFIX]-1035`) and link it under `related_tickets`. The created ticket must in turn link to the feedback markdown file inside its `document_links`.
4. **Resolution Result:**
   - When transitioning the `progress` status to `resolved` or `closed`, the Agent **must** provide a detailed outcome description in the `result` field. Leaving it empty is not allowed.
5. **Dashboard Updates:**
   - After creating or updating any feedback file, the Agent must run the system scanning script to update the feedback statistics on the `README.md` dashboard.
