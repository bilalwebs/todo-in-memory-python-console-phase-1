"""
UpdateTask skill.

Modifies task title and/or description.
"""
from models.task import Task
from models.task_list import TaskList


def update_task(task_list: TaskList, task_id: int, title: str = None,
               description: str = None) -> bool:
    """
    Update an existing task's title and/or description.

    Args:
        task_list: TaskList to update
        task_id: ID of task to update
        title: New title (None to keep current)
        description: New description (None to keep current)

    Returns:
        True if updated, False if ID not found
    """
    task = task_list.get(task_id)
    if not task:
        return False

    if title is not None:
        task.title = title
    if description is not None:
        task.description = description

    return True
