# BONSAI TODO APP Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-01-03

## Active Technologies

- Python 3.10+ (001-cli-todo-app)

## Project Structure

```text
src/
├── agents/
│   ├── __init__.py
│   ├── master_agent.py      # TodoCLI_MasterAgent
│   ├── task_manager.py      # TaskManagerAgent
│   ├── display_agent.py     # DisplayAgent
│   └── validation_agent.py  # ValidationAgent
├── skills/
│   ├── __init__.py
│   ├── add_task.py
│   ├── update_task.py
│   ├── delete_task.py
│   ├── toggle_task.py
│   ├── show_menu.py
│   ├── prompt_user.py
│   ├── view_tasks.py
│   ├── validate_id.py
│   ├── validate_title.py
│   └── confirm_action.py
├── models/
│   ├── __init__.py
│   └── task.py              # Task class
├── cli/
│   ├── __init__.py
│   └── main.py              # Entry point
└── lib/
    └── __init__.py

tests/
├── contract/
├── integration/
└── unit/
```

## Commands

```bash
cd src; pytest; ruff check .
```

## Code Style

Python: Follow standard conventions - PEP 8 formatting, type hints, docstrings

## Recent Changes

- 001-cli-todo-app: Added Python 3.10+

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
