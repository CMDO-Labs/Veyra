# Veyra V0.1 Test Cases

## TC-001 — Read Valid Task File

Given `tasks/TASKS.md` exists and contains valid task data, the program should read the file without modifying it.

## TC-002 — Identify Task Sections

Given tasks exist under `Active`, `Next`, `Scheduled`, and `Someday`, the program should assign each task to the correct section.

## TC-003 — Distinguish Completion State

Given both `- [ ]` and `- [x]` tasks, the program should identify incomplete and completed tasks correctly.

## TC-004 — Display Incomplete Tasks

The terminal summary should display incomplete tasks and exclude completed tasks.

## TC-005 — Handle Empty Section

If a section contains no incomplete tasks, the terminal summary should display `None` for that section.

## TC-006 — Handle Missing Task File

If `tasks/TASKS.md` cannot be found, the program should display a clear error and exit without creating or modifying files.

## Test Results
| Test Case | Result |
| --- | --- |
| TC-001 | PASS |
| TC-002 | PASS |
| TC-003 | PASS |
| TC-004 | PASS |
| TC-005 | PASS |
| TC-006 | PASS |