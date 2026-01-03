"""
ValidationAgent.

Validates user input and enforces spec rules.
"""
from typing import Optional, List
from models.task import Task
from skills.validate_id import validate_id
from skills.validate_title import validate_title


class ValidationAgent:
    """
    Agent responsible for validating user input.

    Capabilities:
        - ValidateID: Check if task ID exists
        - ValidateTitle: Ensure title is non-empty
    """

    def validate_id(self, task_id_str: str, task_list: List[Task]) -> Optional[int]:
        """
        Validate that task ID exists.

        Args:
            task_id_str: String input from user
            task_list: List of tasks to check

        Returns:
            Valid integer ID, or None if invalid/not found
        """
        return validate_id(task_id_str, task_list)

    def validate_title(self, title: str) -> Optional[str]:
        """
        Validate that title is non-empty.

        Args:
            title: Title string to validate

        Returns:
            Valid title string, or None if invalid
        """
        return validate_title(title)
