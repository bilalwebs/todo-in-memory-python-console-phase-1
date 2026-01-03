# Data Model: CLI Todo App

**Feature**: CLI Todo App | **Date**: 2026-01-03

## Entity: Task

Represents a single todo item stored in memory.

### Attributes

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `id` | Integer | Yes | Auto-increment | Unique sequential identifier |
| `title` | String | Yes | N/A | Task title (non-empty) |
| `description` | String | No | "" | Optional task details |
| `completed` | Boolean | No | False | Completion status |

### Validation Rules

- `id`: Must be unique, positive integer, never reused
- `title`: Must be non-empty string after strip()
- `description`: Optional, empty string stored as ""
- `completed`: Boolean (True/False)

### State Transitions

```
Incomplete -> Toggle -> Complete
Complete -> Toggle -> Incomplete
(No other state changes)
```

### Python Representation

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
```

## Storage: TaskList

In-memory collection of Task objects.

### Structure

```python
from typing import List

class TaskList:
    tasks: List[Task]
    next_id: int  # Counter for generating new IDs
```

### Operations

| Operation | Description |
|-----------|-------------|
| `add(task: Task)` | Append task with new ID |
| `get(id: int) -> Optional[Task]` | Find task by ID |
| `get_all() -> List[Task]` | Return all tasks |
| `update(id: int, task: Task)` | Replace task at ID |
| `delete(id: int)` | Remove task by ID |
| `toggle(id: int)` | Flip completed status |

### Constraints

- Maximum tasks: System memory limited
- ID range: Python int (practically unlimited)
- Concurrency: Single-user only (no locks needed)

## Relationships

```
TaskList (1) ----> (0..n) Task
```

- One TaskList contains zero or more Tasks
- Each Task belongs to exactly one TaskList
- No cross-references between Tasks

## Example Data

```python
tasks = TaskList()
tasks.add(Task(id=1, title="Buy groceries", description="Milk, eggs, bread"))
tasks.add(Task(id=2, title="Finish report", completed=False))
```

---

*Data model aligned with Constitution Principle III (Task Data Structure)*
