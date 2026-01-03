"""
ValidateID skill.

Validates if a task ID exists in the task list.
"""
from typing import Optional
from models.task import Task


def validate_id(task_id_str: str, task_list: list[Task]) -> Optional[int]:
    """
    Validate and parse task ID.

    Args:
        task_id_str: String input from user
        task_list: List of tasks to check against

    Returns:
        Valid integer ID if exists, None otherwise

    Validation:
        - Must be a valid integer
        - Must exist in task list
    """
    try:
        task_id = int(task_id_str)
        for task in task_list:
            if task.id == task_id:
                return task_id
        return None
    except ValueError:
        return None
