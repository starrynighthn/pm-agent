# Project Rules - [PROJECT_NAME]

1. All project management data must be stored in markdown files.
2. Ticket file is the source of truth for task-level status and assignment.
3. Jira ticket key format must be [PREFIX]-999.
4. Jira URL format must be: https://10.30.165.157/jira/browse/<ticket_key>
5. Every ticket must belong to exactly one sprint at a time.
6. Every ticket may reference one or more markdown documents.
7. Every ticket may have one BA, one dev_app, one dev_web, one dev_backend, and one tester.
8. Every assigned role must have a handoff plan with planned dates and expected output.
9. Parent ticket cannot be marked done if any sub-ticket is still open.
10. Release fields are mandatory before status becomes released.
11. Usernames in assignees must exist in people directory.
12. Referenced sprint, version, and document files must exist.
13. Do not duplicate the same data across sprint, version, and ticket files.
14. Metadata is for machine-readability, body content is for human-readable context.
15. Every update session must conclude with a Git commit and push to ensure the remote repository is always synchronized with the local source of truth.
16. Tasks merged into a version build are considered completed (status: `done`).
