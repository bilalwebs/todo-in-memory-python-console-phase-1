"""
DeleteTask skill.

Removes task from TaskList.
"""
from models.task_list import TaskList


def delete_task(task_id: int, task_list: TaskList) -> bool:
    """
    Delete a task by ID.

    Args:
        task_id: ID of task to delete
        task_list: TaskList to remove from

    Returns:
        True if deleted, False if ID not found
    """
    return task_list.delete(task_id)
