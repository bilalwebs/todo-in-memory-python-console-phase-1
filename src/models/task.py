"""
Task data model.

Represents a single todo item with id, title, description, and completion status.
"""
from dataclasses import dataclass


@dataclass
class Task:
    """
    A task in the todo application.

    Attributes:
        id: Integer, auto-incrementing, unique
        title: String, required, non-empty
        description: String, optional, defaults to empty
        completed: Boolean, defaults to False
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
