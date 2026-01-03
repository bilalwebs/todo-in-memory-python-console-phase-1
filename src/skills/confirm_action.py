"""
ConfirmAction skill.

Prompts for y/n confirmation before destructive action.
"""


def confirm_action(action: str, task_title: str) -> bool:
    """
    Prompt user for y/n confirmation.

    Args:
        action: Description of action (e.g., "delete task")
        task_title: Title of task being acted on

    Returns:
        True if confirmed (y/yes), False otherwise
    """
    print(f"Task: {task_title}")
    confirm = input(f"Are you sure you want to {action}? (y/n): ").lower()
    return confirm in ["y", "yes"]
