from pathlib import Path

VEYRA_ROOT = Path(__file__).resolve().parents[3]

PROJECT_FILE = VEYRA_ROOT / "projects" / "veyra-v0.1" / "PROJECT.md"
TASK_FILE = VEYRA_ROOT / 'tasks' / "TASKS.md"
WAITING_FILE = VEYRA_ROOT/ "tasks" / "WAITING.md"


def read_project():
    if not PROJECT_FILE.exists():
        print("ERROR: projects/veyra-v0.1/PROJECT.md was not found.")
        raise SystemExit(1)

    project_content = PROJECT_FILE.read_text(encoding="utf-8")
    return project_content


def parse_project(project_content):
    lines = project_content.splitlines()
    current_focus = None
    next_action = None
    current_section = None
    for line in lines:
      
        if line == "## Current Focus":
            current_section = "current_focus"
        elif line == "## Next Action":
            current_section = "next_action"
        elif current_section == "current_focus" and line.startswith("- "):
            current_focus = line.removeprefix("- ")
        elif current_section == "next_action" and line.startswith("- "):
            next_action = line.removeprefix("- ")
    return current_focus, next_action

def read_tasks():
    if not TASK_FILE.exists():
        print("ERROR: tasks/TASKS.md was not found.")
        raise SystemExit(1)

    task_content = TASK_FILE.read_text(encoding="utf-8")
    return task_content
def parse_tasks(task_content):
    lines = task_content.splitlines()
    tasks_by_section = {}
    current_section = None
    for line in lines:
        if line.startswith("## "):
            current_section = line.removeprefix("## ")
            tasks_by_section[current_section] = []
        elif line.startswith("- [ ] "):
            if current_section:
                tasks_by_section[current_section].append(line.removeprefix("- [ ] "))
    return tasks_by_section

def read_waiting():
    if not WAITING_FILE.exists():
        print("ERROR: tasks/WAITING.md was not found.")
        raise SystemExit(1)

    waiting_content = WAITING_FILE.read_text(encoding="utf-8")
    return waiting_content
def parse_waiting(waiting_content):
    lines = waiting_content.splitlines()
    waiting_by_section = {}
    current_section = None
    for line in lines:
        if line.startswith("## "):
            current_section = line.removeprefix("## ")
            waiting_by_section[current_section] = []
        elif line.startswith("- "):
            if current_section:
                waiting_by_section[current_section].append(line.removeprefix("- "))
    return waiting_by_section

def display_daily_view(current_focus, next_action, tasks_by_section, waiting_by_section):
    print("=== VEYRA  DAILY VIEW ===")
    print("\nCurrent Project")
    print(f"Current Focus: {current_focus}")
    print(f"Next Action: {next_action}")
    print("\nTasks:")
    for section, tasks in tasks_by_section.items():
        print(f"\n{section}")
        if tasks:
            for task in tasks:
                print(f"- {task}")
        else:
            print("None")
    print("\nWaiting:")
    for section, items in waiting_by_section.items():
        print(f"\n{section}")
        if items:
            for item in items:
                print(f"- {item}")
        else:
            print("None")

def main():
    project_content = read_project()
    current_focus, next_action = parse_project(project_content)
    task_content = read_tasks()
    tasks_by_section = parse_tasks(task_content)
    waiting_content = read_waiting()
    waiting_by_section = parse_waiting(waiting_content)
    display_daily_view(current_focus, next_action, tasks_by_section, waiting_by_section)

if __name__ == "__main__":
    main()