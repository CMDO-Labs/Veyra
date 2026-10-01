# Veyra V0.1 Design
## Task reader

The Veyra task reader will use a small pipeline:

1. Locate the approved task file.
2. Read the task file.
3. Parse the Markdown into task sections.
4. Identify each task's completion state.
5. Filter completed tasks from the actionable summary.
6. Display the remaining tasks grouped by section.

## Planned Functions

### read_tasks()
Reads the approved `tasks/TASKS.md` file and returns its contents as text.
### parse_tasks ()
Receives the Markdown text and converts recognized task sections and task entries into structured data.

### display_tasks()
Receives the structured task data and displays incomplete tasks grouped by section.

### main()
Controls the program flow by calling the other functions in the required order.

## Task Data Structure
Parsed incomplete tasks are grouped by section.

Each section is stored as a key with a list of incomplete task descriptions.

Conceptual example:

Active
- Finish remaining local Terraform fundamentals.

Next
- Build the first Python automation for Veyra.

Scheduled
- None

  ## Approved Paths

  The task reader will operate from the Veyra root directory.

  Approved input:

  - 'tasks/TASKS.md'

  The program will construct the task-file path relative to the Veyra root rather than hard-coding an absolute Windows path.