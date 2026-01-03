"""
DisplayAgent.

Handles CLI menu display, user prompts, and formatted task output.
"""
from models.task import Task
from skills.show_menu import show_menu
from skills.prompt_user import prompt_user_choice
from skills.view_tasks import view_tasks
from typing import List


class DisplayAgent:
    """
    Agent responsible for all user-facing display and input.

    Responsibilities:
        - Show main menu
        - Prompt user for choices
        - Display formatted task list
    """

    def show_menu(self) -> None:
        """Render main menu options."""
        show_menu()

    def prompt_user_choice(self) -> str:
        """Capture user menu selection."""
        return prompt_user_choice()

    def view_tasks(self, tasks: List[Task]) -> None:
        """Format and display task list."""
        view_tasks(tasks)
