from pathlib import Path
VEYRA_ROOT = Path(__file__).resolve().parents[2]
TASK_FILE = VEYRA_ROOT / "tasks" / "TASKS.md"

if not TASK_FILE.exists():
    print("ERROR: tasks/TASKS.md was not found.")
    raise SystemExit(1)

def read_tasks():
    task_content = TASK_FILE.read_text(encoding="utf-8")
    return task_content
def parse_tasks(task_content):
    lines = task_content.splitlines()
    tasks_by_section ={}
    current_section = None
    
    for line in lines:
        if line.startswith("##"):
            current_section = line.removeprefix("## ")
            tasks_by_section[current_section] = []
        elif line.startswith("- [ ] "):
            task_text = line.removeprefix("- [ ] ")
            tasks_by_section[current_section].append(task_text)

    return tasks_by_section


def display_tasks(tasks_by_section):
    for section, tasks in tasks_by_section.items():
        print(f"\n{section}")
        if tasks:
            for task in tasks:
                print(f"- {task}")
        else:
            print("None")

def main():
    tasks_content = read_tasks()
    tasks_by_section = parse_tasks(tasks_content)
    display_tasks(tasks_by_section)

if __name__ == "__main__":
    main()