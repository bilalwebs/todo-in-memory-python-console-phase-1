"""
TaskManagerAgent.

Handles in-memory task operations (add, update, delete, toggle complete).
"""
from models.task_list import TaskList
from models.task import Task
from skills.add_task import add_task
from skills.toggle_task import toggle_task
from skills.update_task import update_task
from skills.delete_task import delete_task
from typing import Optional


class TaskManagerAgent:
    """
    Agent responsible for managing task data.

    Responsibilities:
        - Add new tasks
        - Update existing tasks
        - Delete tasks
        - Toggle completion status
    """

    def __init__(self) -> None:
        """Initialize with empty task list."""
        self.task_list = TaskList()

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with title and optional description.

        Args:
            title: Non-empty task title
            description: Optional task description

        Returns:
            Created Task object
        """
        return add_task(title, description, self.task_list)

    def update_task(self, task_id: int, title: Optional[str] = None,
                 description: Optional[str] = None) -> bool:
        """
        Update an existing task's title and/or description.

        Args:
            task_id: ID of task to update
            title: New title (None to keep current)
            description: New description (None to keep current)

        Returns:
            True if updated, False if ID not found
        """
        return update_task(self.task_list, task_id, title if title else None,
                        description if description else None)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id: ID of task to delete

        Returns:
            True if deleted, False if ID not found
        """
        return delete_task(task_id, self.task_list)

    def toggle_task(self, task_id: int) -> bool:
        """
        Toggle task completion status.

        Args:
            task_id: ID of task to toggle

        Returns:
            True if toggled, False if ID not found
        """
        return self.task_list.toggle(task_id)

    def get_all_tasks(self) -> list[Task]:
        """
        Get all tasks.

        Returns:
            List of all Task objects
        """
        return self.task_list.get_all()

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a single task by ID.

        Args:
            task_id: ID of task to get

        Returns:
            Task if found, None otherwise
        """
        return self.task_list.get(task_id)
