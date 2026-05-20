# AGENTS.md — [PROJECT_NAME] Project Rules for AI Agents

This file serves as the operational guide for AI agents (DeepSeek, Claude, Gemini, Codex) when working with the [PROJECT_NAME] project.

---

## Core Principles

1. **SSOT (Single Source of Truth)** — Each entity (project, person, ticket, sprint, version, requirement, document) has **exactly one** `.md` file as its raw source of truth.
2. **No Duplication** — Do not store the same information in multiple places. Reference via ID or path instead.
3. **Markdown-first** — All management data is stored in Markdown format with YAML frontmatter.

---

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `rules/` | Detailed rules: project, workflow, validation, requirement, feedback |
| `projects/` | Project definitions |
| `people/` | Member profiles |
| `sprints/` | Sprint tracking files |
| `versions/` | Release version tracking |
| `tickets/` | Ticket data (source of truth for tasks) |
| `requirements/` | Requirements before being converted to tickets |
| `feedbacks/` | User feedback / reporting data |
| `docs/` | Technical documentation (solution, design, api, testcases) |

---

## Mandatory Operational Rules

### 1. Compliance with Rule Files
- **Always** read and adhere to the files in `rules/` before performing any operations:
  - `rules/project-rules.md` — General project rules
  - `rules/workflow-rules.md` — Ticket lifecycle & handoff flow
  - `rules/validation-rules.md` — Validation rules before writing files
  - `rules/requirement-rules.md` — Requirement management rules
  - `rules/feedback-rules.md` — Feedback management rules

### 2. Mandatory Metadata for Tickets
When creating/updating a ticket, the following metadata fields **must** be provided:
- `ticket_key`, `title`, `status`, `priority`
- `assignees` (BA, dev_app, dev_web, dev_backend, tester)
- `sprint_code`, `jira_url`, `document_links`
- `parent_key` / `sub_tasks` (if any)

### 3. Bidirectional Links
- A parent ticket must list `sub_tasks`, and a sub-ticket must have `parent_key`.
- A sprint file must list `ticket_keys`, and a ticket must have `sprint_code`.
- A requirement converted to a ticket must update `related_tickets`.

### 4. Git Synchronization
- **At the end of each session, you must commit and push** all changes to the remote repository.
- Commit messages must be clear and describe the changes made.
- **Before committing, update `README.md`** if there are changes in metrics (new ticket, status change, assignee, version). Scan all ticket/version/requirement files to get accurate numbers; do not use outdated numbers from memory.

### 5. Language
- Project documentation and metadata must be in **English**.
- Filenames, keys, and identifiers must remain in their original formats.

---

## Ticket Workflow

```
backlog → refined → analysis → ready_for_dev → in_progress → ready_for_test → testing → ready_for_release → released → done
                                                                                                      ↘ cancelled
```

### Key State Transition Conditions:
| Transition | Condition |
|------------|-----------|
| `analysis` → `ready_for_dev` | Must have `short_description`, `title`, `document_links` containing `solution`, BA assigned, and at least 1 component |
| `ready_for_dev` → `in_progress` | Must have an assignee for each component and a handoff plan |
| `in_progress` → `ready_for_test` | Code must be pushed/merged, testable build available |
| `testing` → `ready_for_release` | Must have a tester, test passed/approved, blockers resolved |
| `ready_for_release` → `released` | Must have `release_time` and `build_version` |

---

## Validation Before Writing Files

Before any write operation, the agent must verify:
1. **Jira URL** matches the format `https://jira.company.com/browse/[PREFIX]-XXX`
2. **Username** in `assignees` exists in `people/`
3. **Sprint** exists in `sprints/` and lists the ticket
4. **Version** exists in `versions/`
5. **Parent/Sub-ticket links** are bidirectional
6. **Document links** point to existing files, with valid types

---

## Quick Reference

- Ticket key format: `[PREFIX]-XXX` (e.g., `[PREFIX]-1005`)
- Jira URL format: `https://jira.company.com/browse/[PREFIX]-XXX`
- Requirement ID format: `REQ-YYYYMMDD-XXX`
- Feedback ID format: `FB-YYYYMMDD-XXX`
- Sprint code format: `[PREFIX] Sprint T{N} month {MM}`
