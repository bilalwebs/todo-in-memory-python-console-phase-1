"""
TaskList storage class.

Manages in-memory collection of Task objects.
"""
from typing import List, Optional
from .task import Task


class TaskList:
    """
    In-memory collection of Task objects.

    Attributes:
        tasks: List[Task] - List of all tasks
        next_id: int - Counter for generating new sequential IDs
    """

    def __init__(self) -> None:
        """Initialize empty task list with counter starting at 1."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add(self, task: Task) -> Task:
        """
        Add a task with a new sequential ID.

        Args:
            task: Task object to add (should have id=0, will be assigned)

        Returns:
            Task with assigned ID
        """
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        return task

    def get(self, task_id: int) -> Optional[Task]:
        """
        Find task by ID.

        Args:
            task_id: ID of task to find

        Returns:
            Task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all(self) -> List[Task]:
        """
        Get all tasks.

        Returns:
            List of all Task objects
        """
        return self.tasks.copy()

    def update(self, task_id: int, task: Task) -> bool:
        """
        Replace task at ID with new task data.

        Args:
            task_id: ID of task to update
            task: New task data (id will not be changed)

        Returns:
            True if updated, False if ID not found
        """
        for i, existing in enumerate(self.tasks):
            if existing.id == task_id:
                self.tasks[i] = task
                self.tasks[i].id = task_id  # Preserve original ID
                return True
        return False

    def delete(self, task_id: int) -> bool:
        """
        Remove task by ID.

        Args:
            task_id: ID of task to delete

        Returns:
            True if deleted, False if ID not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def toggle(self, task_id: int) -> bool:
        """
        Flip task completion status.

        Args:
            task_id: ID of task to toggle

        Returns:
            True if toggled, False if ID not found
        """
        task = self.get(task_id)
        if task:
            task.completed = not task.completed
            return True
        return False
