"""
TodoCLI_MasterAgent.

Coordinates all sub-agents, routes user input to appropriate handlers,
displays main menu loop.
"""
from agents.task_manager import TaskManagerAgent
from agents.display_agent import DisplayAgent
from agents.validation_agent import ValidationAgent
from models.task import Task


class TodoCLI_MasterAgent:
    """
    Main agent that coordinates all other agents.

    Responsibilities:
        - Coordinate TaskManagerAgent, DisplayAgent, ValidationAgent
        - Route user input to appropriate handlers
        - Display main menu loop
    """

    def __init__(self) -> None:
        """Initialize all sub-agents."""
        self.task_manager = TaskManagerAgent()
        self.display = DisplayAgent()
        self.validation = ValidationAgent()

    def run(self) -> None:
        """Main application loop."""
        while True:
            self.display.show_menu()
            choice = self.display.prompt_user_choice()

            if choice == "1":
                self._handle_add_task()
            elif choice == "2":
                self._handle_view_tasks()
            elif choice == "3":
                self._handle_update_task()
            elif choice == "4":
                self._handle_delete_task()
            elif choice == "5":
                self._handle_toggle_task()
            elif choice == "6":
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")

    def _handle_add_task(self) -> None:
        """Handle Add Task user story."""
        print("\n--- Add Task ---")
        title = input("Enter task title: ")
        validated_title = self.validation.validate_title(title)

        if not validated_title:
            print("Error: Title cannot be empty.")
            return

        description = input("Enter task description (optional): ")
        task = self.task_manager.add_task(validated_title, description)
        print(f"Task added successfully (ID: {task.id})")

    def _handle_view_tasks(self) -> None:
        """Handle View All Tasks user story."""
        print("\n--- View Tasks ---")
        tasks = self.task_manager.get_all_tasks()
        self.display.view_tasks(tasks)

    def _handle_update_task(self) -> None:
        """Handle Update Task user story."""
        print("\n--- Update Task ---")
        tasks = self.task_manager.get_all_tasks()
        if not tasks:
            print("No tasks to update.")
            return

        task_id_str = input("Enter task ID to update: ")
        task_id = self.validation.validate_id(task_id_str, tasks)

        if task_id is None:
            print("Task not found.")
            return

        new_title = input("Enter new title (leave empty to keep current): ")
        new_desc = input("Enter new description (leave empty to keep current): ")

        if new_title.strip():
            validated_title = self.validation.validate_title(new_title)
            if validated_title:
                success = self.task_manager.update_task(task_id, title=validated_title,
                                                description=new_desc if new_desc else None)
            else:
                print("Error: Title cannot be empty.")
                return
        else:
            success = self.task_manager.update_task(task_id, description=new_desc if new_desc else None)

        if success:
            print(f"Task {task_id} updated successfully")

    def _handle_delete_task(self) -> None:
        """Handle Delete Task user story."""
        print("\n--- Delete Task ---")
        tasks = self.task_manager.get_all_tasks()
        if not tasks:
            print("No tasks to delete.")
            return

        task_id_str = input("Enter task ID to delete: ")
        task_id = self.validation.validate_id(task_id_str, tasks)

        if task_id is None:
            print("Task not found.")
            return

        task = self.task_manager.get_task(task_id)
        print(f"Task: {task.title}")
        confirm = input("Are you sure you want to delete this task? (y/n): ").lower()

        if confirm in ["y", "yes"]:
            if self.task_manager.delete_task(task_id):
                print(f"Task {task_id} deleted successfully")
            else:
                print("Delete failed.")
        else:
            print("Delete cancelled.")

    def _handle_toggle_task(self) -> None:
        """Handle Toggle Task Completion user story."""
        print("\n--- Toggle Complete ---")
        tasks = self.task_manager.get_all_tasks()
        if not tasks:
            print("No tasks to toggle.")
            return

        task_id_str = input("Enter task ID to toggle: ")
        task_id = self.validation.validate_id(task_id_str, tasks)

        if task_id is None:
            print("Task not found.")
            return

        if self.task_manager.toggle_task(task_id):
            task = self.task_manager.get_task(task_id)
            status = "complete" if task.completed else "incomplete"
            print(f"Task {task_id} marked as {status}")
        else:
            print("Toggle failed.")
