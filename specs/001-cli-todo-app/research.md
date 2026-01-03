# Research: CLI Todo App

**Feature**: CLI Todo App | **Date**: 2026-01-03

## Technical Decisions

### Language: Python 3.10+

**Decision**: Use Python 3.10+ for implementation.

**Rationale**:
- Beginner-friendly syntax (Principle VII)
- Excellent CLI support via standard library
- No external dependencies required (Principle VI)
- Cross-platform compatibility
- Clear, readable code patterns

**Alternatives Considered**:
- Node.js: Requires npm packages for CLI parsing
- Go: Single binary but more verbose syntax
- Rust: Steeper learning curve
- Bash: Limited for complex state management

### Testing: pytest

**Decision**: Use pytest for testing.

**Rationale**:
- Simple test discovery and execution
- Readable assertion syntax
- Widely used and well-documented
- Minimal boilerplate

### Storage: In-Memory Python List

**Decision**: Store tasks in a Python list with Task objects.

**Rationale**:
- Aligns with Principle I (In-Memory Storage Only)
- Simple to implement and understand
- No database setup required
- Sequential ID generation is straightforward

### CLI Interaction: Standard Input/Output

**Decision**: Use Python's built-in `input()` and `print()` functions.

**Rationale**:
- Principle II: CLI-Only Interface
- No external CLI libraries needed
- Works cross-platform
- Simple to test with mocked stdin/stdout

## Best Practices

### Agent Pattern

Following Single Responsibility Principle (Principle IV):
- Master agent delegates to specialized agents
- Each agent has exactly one responsibility
- Skills are atomic and reusable

### Error Handling

Per Quality Rules:
- All invalid operations show clear error messages
- Delete requires confirmation before execution
- Input validation before any operation

### Code Organization

Per Principle VII (Readable Logic):
- Functions under 30 lines where practical
- Meaningful names for all identifiers
- No magic numbers (use constants)

## Implementation Notes

### Sequential ID Generation

```python
# Simple counter approach (valid per constitution)
task_id_counter = 0

def generate_id():
    task_id_counter += 1
    return task_id_counter
```

### Task Storage

```python
# In-memory list (per Principle I)
tasks: List[Task] = []
```

### Menu Structure

```
=== Todo CLI ===
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit

Enter choice:
```

---

*Research complete - all decisions aligned with constitution principles.*
