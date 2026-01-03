# Quickstart: CLI Todo App

**Feature**: CLI Todo App | **Version**: 1.0.0 | **Date**: 2026-01-03

## Overview

A simple command-line todo application that helps you manage tasks. Add, view, update, delete, and mark tasks as complete - all from your terminal.

## Prerequisites

- Python 3.10 or higher
- No external dependencies required

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd BONSAI-TODO-APP
   ```

2. No installation steps needed - uses standard library only!

## Running the Application

### Start the CLI

```bash
python src/cli/main.py
```

Or run the entry point:

```bash
python -m src.cli.main
```

## Usage Guide

### Main Menu

When you start the app, you'll see:

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

### Add a Task

1. Select option `1` from menu
2. Enter task title (required)
3. Enter description (optional, press Enter to skip)

Example:
```
Enter choice: 1
Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, bread
Task added successfully (ID: 1)
```

### View All Tasks

1. Select option `2` from menu
2. See all tasks with their status

Example:
```
Enter choice: 2

=== Tasks ===
ID | Status | Title          | Description
--- | ------ | -------------- | ------------
1   | [ ]    | Buy groceries  | Milk, eggs

(1 task)
```

### Update a Task

1. Select option `3` from menu
2. Enter task ID to update
3. Enter new title (or leave empty to keep current)
4. Enter new description (or leave empty to keep current)

Example:
```
Enter choice: 3
Enter task ID to update: 1
Enter new title (leave empty to keep current): Buy almond milk
Enter new description (leave empty to keep current):
Task 1 updated successfully
```

### Delete a Task

1. Select option `4` from menu
2. Enter task ID to delete
3. Confirm deletion with `y` or cancel with `n`

Example:
```
Enter choice: 4
Enter task ID to delete: 1
Are you sure you want to delete task 1? (y/n): y
Task 1 deleted successfully
```

### Toggle Task Completion

1. Select option `5` from menu
2. Enter task ID to toggle

Example:
```
Enter choice: 5
Enter task ID to toggle: 1
Task 1 marked as complete
```

### Exit

1. Select option `6` from menu
2. Or press `Ctrl+C` at any time

## Task Status Legend

- `[ ]` = Incomplete
- `[X]` = Complete

## Tips

- Task IDs are sequential and never reused
- Empty descriptions are shown as blank
- Press Enter quickly to skip optional fields
- All data is lost when you exit (in-memory only)

## Troubleshooting

**Q: Application won't start**
- Check Python version: `python --version` (should be 3.10+)
- Ensure you're in the correct directory

**Q: "Task not found" error**
- View tasks first to see valid IDs
- Use the exact ID shown in the task list

**Q: Can't add empty title**
- Enter at least one character for the title

## Next Steps

- Run `/sp.tasks` to generate implementation tasks
- Follow Red-Green-Refactor workflow
- Test each user story independently

---

*Quickstart guide complete. Ready to start implementation.*
