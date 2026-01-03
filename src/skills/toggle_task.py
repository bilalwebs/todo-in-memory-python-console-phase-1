"""
ToggleTaskComplete skill.

Flips task completion status between complete and incomplete.
"""
from models.task_list import TaskList


def toggle_task(task_id: int, task_list) -> bool:
    """
    Toggle a task's completion status.

    Args:
        task_id: ID of task to toggle
        task_list: TaskList object to update

    Returns:
        True if toggled, False if ID not found
    """
    return task_list.toggle(task_id)
