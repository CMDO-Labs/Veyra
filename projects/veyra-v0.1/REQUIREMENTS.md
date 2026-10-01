# Veyra V0.1 Requirements
## Functional Requirements
### FR-001 — Read Veyra Task State
Veyra must be able to read task information from the approved Markdown file `tasks/TASKS.md` without modifying the file
### FR-002 — Identify Task Sections
Veyra must identify tasks under the `Active`, `Next`, `Scheduled`, and `Someday` sections of `tasks/TASKS.md`.
### FR-003 — Idnetify Task Completion State
Veyra must distinguish between incomplete tasks marked `- [ ]` and completed tasks marked `- [x]`.
### FR-004 — Display Task Summary
Veyra must display a terminal summary of incomplete tasks grouped by their task section.
### FR-005 — Handle Missing Task File
If `tasks/TASKS.md` cannot be found, Veyra must display a clear error message and exit without creating or modifying any files.
###FR-006 — Handle Empty Task Sections
If a task section contains no incomplete tasks, Veyra must display the section with `None` as its value.


## Security Requirements

### SR-001 — Approved File Access Only
Veyra must access only explicitly approved files within the Veyra root directory.
### SR-002 — Read-Only Operation
The V0.1 task reader must not create, modify, rename, move, or delete any files.
### SR-003 — No Arbitrary Filesystem Access
The V0.1 task reader must not scan or access files outside the approved Veyra path