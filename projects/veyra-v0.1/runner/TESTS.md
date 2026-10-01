# Veyra V0.1 Runner Test Cases

## TC-001 — Display Daily operational View
Given the approved Veyra operational files exist, the runner should display a single terminal view containing Current Projects, Tasks, and Waiting sections.

## TC-002 — Read Approved Operational Sources
Given the approved Veyra files exist, the runner should read only the explicitly configured 'PROJECT.md', 'TASKS.md', and 'WAITING.md' files.

## TC-003 — Include Task State
Given 'tasks/TASKS.md' contains incomplete tasks, the runner should display those tasks in the Tasks section of the daily operational view.

## TC-004 — Include Waiting Times
Given 'tasks/WAITING.md' contains current waiting items, the runner should display those items in the Waiting section of the daily operational view.

## TC-005 — Include Current Projects Focus
Given 'projects/veyra-v0.1/PROJECT.md' contains a Current Focus and Next Action, the runner should display both vaules in the Current Projects section of the daily operational view.

## TC-006 — Handle Empty Operational Sections
Given an operational section contains no current items, the runner should display the section with 'NONE' as its value.

## TC-007 — Restrict File Access
The runner should access only the explicitly approved 'PROJECT.md', 'TASKS.md', and 'WAITING.md' paths and should not scan other Veyra directories or files. 

## TC-008 — PReserve Operational Files
Running the Veyra runner should not create, modify, rename, movem or delete 'PROJECT.md', 'TASKS.md', or 'WAITING.md'.

## TC-009 — Handle Missing Approved File 
Given an approved operational file cannot be found, the runner should display a clear error and exit without creating modifying any file. 