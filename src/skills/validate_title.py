"""
ValidateTitle skill.

Ensures task title is non-empty.
"""
from typing import Optional


def validate_title(title: str) -> Optional[str]:
    """
    Validate task title.

    Args:
        title: Title string to validate

    Returns:
        Valid title string if non-empty, None otherwise

    Validation:
        - Must be non-empty after stripping whitespace
    """
    title = title.strip()
    if title:
        return title
    return None
