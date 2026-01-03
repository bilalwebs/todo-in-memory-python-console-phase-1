"""
ViewTasks skill.

Displays task list in formatted table.
"""
from models.task import Task


def view_tasks(tasks: list[Task]) -> None:
    """
    Display all tasks in formatted table.

    Args:
        tasks: List of Task objects to display

    Shows:
        - ID, status, title, description columns
        - "No tasks yet" message if empty
    """
    if not tasks:
        print("\nNo tasks yet. Add a task to get started.")
        return

    print("\n=== Tasks ===")
    print("ID | Status | Title          | Description")
    print("--- | ------ | -------------- | ------------")

    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        # Truncate title if too long (up to 14 chars)
        title = task.title[:14] + ".." if len(task.title) > 14 else task.title.ljust(14)
        # Truncate description if too long (up to 12 chars)
        desc = task.description[:12] if task.description else ""
        if len(task.description) > 12:
            desc = task.description[:12] + ".."
        print(f"{task.id:<3} | {status:<6} | {title} | {desc}")

    print(f"\n({len(tasks)} task{'s' if len(tasks) != 1 else ''})")
