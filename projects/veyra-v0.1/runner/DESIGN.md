# Veyra V0.1 Runner Design

## Data Flow

The Veyra runner uses the following processing flow:

1. Read approved operational files.
2. Parse relevant information from each file.
3. Organzie parsed information into the daily operational heirarchy.
4. Display the faily operational view the terminal.

## Daily View Heirarchy

1. Current Project
2. Tasks
3. Waiting

## Components

### read_project()
Reads the approved 'Project.md' file.

### parse_project()
Extracts the current focus and next action from the project content. 

### read_tasks()
Reads the approved 'TASKS.md' file.

### parse_tasks()
Extracts incomplete tasks grouped by task section

### read_waiting()
Reads the approved 'WAITING.md" file.
 
### parse_waiting()
Extracts current waiting items.

### display_daily_view()
Displays the organized Current Projects, Tasks, and Waiting information in the terminal.

### main()
Controls the runner workflow and calls the required functions in the correct order.

