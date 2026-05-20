# Workflow Rules - [PROJECT_NAME]

## 1. Ticket Lifecycle
The standard statuses for a ticket are:
- `backlog`: newly created
- `refined`: basic scope defined
- `analysis`: BA is analyzing
- `ready_for_dev`: ready for development
- `in_progress`: being implemented
- `ready_for_test`: dev finished, waiting for test
- `testing`: tester is testing
- `blocked`: blocked by something
- `ready_for_release`: test passed, waiting for release
- `released`: included in a release
- `done`: completed
- `cancelled`: cancelled

## 2. Transition Rules
- **analysis -> ready_for_dev**: Must have `short_description`, `title`, `document_links` containing `solution`, an assigned BA, and at least one component.
- **ready_for_dev -> in_progress**: Must have an assignee for each component and a handoff plan.
- **in_progress -> ready_for_test**: Backend code must be pushed (if backend), app must be merged or testable build available (if app), web must be merged (if web), and API must be ready (if API).
- **testing -> ready_for_release**: Must have a tester, test result must be pass or conditionally approved, and blocker defects must be resolved/waived.
- **ready_for_release -> released**: Must have `release_time` and a corresponding `build_version` or release tag.
- **Any status -> done**: Automatically applied once the ticket is merged into a version build.
- **released -> done**: Release completed, no open sub-tickets, no open blockers.

## 3. Handoff Flow
- BA -> Dev (Backend, App, Web)
- Backend -> App, Tester (API, Docs)
- App/Web -> Tester (Build, Merge)
- Tester -> PM (Test Report)
