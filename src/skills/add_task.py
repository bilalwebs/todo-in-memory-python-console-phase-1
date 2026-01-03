"""
AddTask skill.

Creates a new task with next sequential ID.
"""
from models.task import Task
from models.task_list import TaskList


def add_task(title: str, description: str, task_list: TaskList) -> Task:
    """
    Create a new task with title and optional description.

    Args:
        title: Non-empty task title
        description: Optional task description
        task_list: TaskList to add to

    Returns:
        Created Task object with assigned ID
    """
    task = Task(id=0, title=title, description=description)
    return task_list.add(task)
