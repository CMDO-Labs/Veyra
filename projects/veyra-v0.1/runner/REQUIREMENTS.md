# Veyra V0.1 Runner Requirements

## Functional Requirements

### FR-001 — Display DAily Operational View
The Veyra runner must display a single terminal view summarizing approved operational information from Veyra

### FR-002 — Read Approved Operational Sources
The Veyra runner must read operational inforamation only from explicitly approved Veyra Markdown files.

### FR-003 — Include Task State
The Veyra runner must include the curent incomplete task state from ' tasks/TASKS.md' in the daily operational view.

### FR-004 — Include Waiting Items
The Veyra runner must include current items from 'tasks/WAITING.md' in the daily operational view.

### FR-005 — Include Current Projects Focus
The Veyra runner must include the current focus and next action from 'projects/veyrav0.1/PROJECT.md' in the daily operational view. 

### FR-006 — Handle Empty Operational Sections
If an operational section contains no current items, the Veyra runner must display the section with 'None" as its value.

## Security Requirements

### SR-001 — Approved File Access Only
The Veyra runner must access only explicitly approved files within the Veyra root directory.

### SR-002 — Read-Only Operation
The Veyra runner must not create, modify, rename, move, or delete operational data files.

### SR-003 — No Arbitrary Filesystem Access
The Veyra runner must not scan or access files outside the explicitly approved Veyra paths.

### SR-004 — Faily Safely on Missing Approved Files
If an approved operational file cannot be found, the Veyra runner must display a clear error and exit without creating or modifying any files.

