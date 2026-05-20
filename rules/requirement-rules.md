# Requirement Rules - [PROJECT_NAME]

## 1. Definition
A Requirement is a proposal for a feature, change, or bug fix from a customer or internal team before it is converted into an official ticket.

## 2. Naming Convention
- The temporary requirement ID format is: `REQ-YYYYMMDD-XXX` (e.g., `REQ-20260506-001`).
- Each requirement is saved as an individual file under the `requirements/` directory.

## 3. Standard Metadata for Requirements (Frontmatter)

```yaml
---
entity: requirement
req_id: REQ-20260506-001
title: Title of the requirement
requester:
  name: Name of the requester
  org: Organization / Department
request_date: 2026-05-06
priority: medium             # low | medium | high | critical
status: draft                # draft | submitted | reviewing | accepted | rejected | converted
tags: []
related_tickets: []
---
```

## 4. Requirement Status Lifecycle
- `draft`: Newly created or in development.
- `submitted`: Requirement has been officially submitted.
- `reviewing`: Currently under review and evaluation.
- `accepted`: Approved and ready to be converted into tickets.
- `rejected`: Rejected or declined.
- `converted`: Converted into one or more tickets (must have `related_tickets`).

## 5. Operational Rules
- Every requirement must have valid `requester` details.
- When transitioning the status to `converted`, the agent must update the `related_tickets` list.
- Requirement files must not be deleted after conversion to preserve history.
