# 📝 Phase I - In-Memory Python Console App

A **Python CLI TODO application** with agent-based architecture that manages tasks in memory. Users can add, view, update, delete, and toggle task completion using a console menu.

---

## 🚀 Project Overview

This project demonstrates **Spec-Driven Development (SDD)** methodology and agent-based software architecture. All tasks are stored **in memory**, so data is lost when the program exits.

Built for the **Hackathon GIAIC** competition.

---

## ✨ Features

- **Add new tasks** - Create tasks with title and optional description
- **View all tasks** - Display tasks in formatted table with ID, status, title, and description
- **Update existing tasks** - Modify task title and/or description
- **Delete tasks** - Remove tasks with confirmation prompt
- **Toggle completion** - Mark tasks as complete or incomplete

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Agent-based architecture** - 4 coordinating agents
- **Atomic skills** - 10 reusable skill modules
- **Console / CLI based**

---

## 📁 Project Structure

```
Phase I - In-Memory Python Console App/
├── src/
│   ├── agents/          # Coordinating agents
│   │   ├── master_agent.py      # Main application loop & routing
│   │   ├── task_manager.py      # Task data management
│   │   ├── display_agent.py     # CLI menu & output
│   │   └── validation_agent.py  # Input validation
│   ├── skills/          # Atomic operations
│   │   ├── add_task.py
│   │   ├── update_task.py
│   │   ├── delete_task.py
│   │   ├── toggle_task.py
│   │   ├── show_menu.py
│   │   ├── prompt_user.py
│   │   ├── view_tasks.py
│   │   ├── validate_id.py
│   │   └── validate_title.py
│   ├── models/          # Data models
│   │   ├── task.py              # Task dataclass
│   │   └── task_list.py        # In-memory task storage
│   ├── cli/
│   │   └── main.py              # Entry point
│   ├── skills/          # [Empty] - for future use
│   └── lib/             # [Empty] - for future use
├── tests/               # Test directories (not implemented yet)
│   ├── contract/
│   ├── integration/
│   └── unit/
├── specs/              # SDD specification documents
│   └── 001-cli-todo-app/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
├── history/            # Prompt History Records (PHRs)
├── CLAUDE.md           # Development guidelines
└── README.md
```

---

## ▶️ How to Run

```bash
cd "D:\Hackthon_GIAIC\BONSAI TODO APP"
python src/cli/main.py
```

Or from any directory:
```bash
python /path/to/Phase\ I - In-Memory\ Python\ Console\ App/src/cli/main.py
```

---

## 📋 Usage

Once running, you'll see the main menu:

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

### Adding a Task
```
Enter choice: 1

--- Add Task ---
Enter task title: Learn Python
Enter task description (optional): Complete online course
Task added successfully (ID: 1)
```

### Viewing Tasks
```
Enter choice: 2

--- View Tasks ---

=== Tasks ===
ID | Status | Title          | Description
--- | ------ | -------------- | ------------
1   | [ ]    | Learn Python    | Complete onl..
2   | [X]    | Write Code     | Build app...

(2 tasks)
```

### Updating a Task
```
Enter choice: 3

--- Update Task ---
Enter task ID to update: 1
Enter new title (leave empty to keep current): Master Python
Enter new description (leave empty to keep current): Build CLI apps
Task 1 updated successfully
```

### Deleting a Task
```
Enter choice: 4

--- Delete Task ---
Enter task ID to delete: 2
Task: Write Code
Are you sure you want to delete this task? (y/n): y
Task 2 deleted successfully
```

### Toggling Task Completion
```
Enter choice: 5

--- Toggle Complete ---
Enter task ID to toggle: 1
Task 1 marked as complete
```

---

## 🏗️ Architecture

This application uses **agent-based architecture** with clear separation of concerns:

### Agents (4 total)
- **TodoCLI_MasterAgent**: Coordinates all agents, routes user input, runs main loop
- **TaskManagerAgent**: Manages task data operations (CRUD)
- **DisplayAgent**: Handles all CLI output and menu display
- **ValidationAgent**: Validates user input (IDs, titles)

### Skills (10 total)
Each skill is a single atomic operation:
- **AddTask**: Create task with sequential ID
- **UpdateTask**: Modify task attributes
- **DeleteTask**: Remove task from list
- **ToggleTask**: Flip completion status
- **ViewTasks**: Format and display task table
- **ShowMenu**: Display main menu options
- **PromptUser**: Capture user menu selection
- **ValidateID**: Check if task ID exists
- **ValidateTitle**: Ensure non-empty title

### Design Principles (SDD Constitution)
1. ✅ **Single Responsibility** - Each agent/skill has one job
2. ✅ **Agent-Based** - Coordinating agents manage operations
3. ✅ **Atomic Skills** - Skills do one thing well
4. ✅ **Dependency Inversion** - Skills depend on abstractions, not implementations
5. ✅ **No Frameworks** - Pure Python, no external dependencies
6. ✅ **In-Memory Storage** - TaskList stores data in memory
7. ✅ **Type Hints** - Full type annotations throughout

---

## 🔧 Development

### Run Code Quality Checks
```bash
cd src
pytest          # Run tests (when implemented)
ruff check .     # Lint code
```

### Specification Documents
- **spec.md**: Feature specification with user stories
- **plan.md**: Implementation plan with phase breakdown
- **tasks.md**: Detailed task list (37 tasks across 9 phases)

---

## 📊 Implementation Status

| Phase | Tasks | Status |
|-------|--------|--------|
| Phase 1: Setup | T001-T004 | ✅ Complete |
| Phase 2: Foundational | T005-T009 | ✅ Complete |
| Phase 3: Add Task (US1) | T010-T016 | ✅ Complete |
| Phase 4: View Tasks (US2) | T017-T019 | ✅ Complete |
| Phase 5: Toggle Task (US3) | T020-T022 | ✅ Complete |
| Phase 6: Update Task (US4) | T023-T025 | ✅ Complete |
| Phase 7: Delete Task (US5) | T026-T030 | ✅ Complete |
| Phase 8: Exit (US6) | T031-T032 | ✅ Complete |
| Phase 9: Polish | T033-T037 | ✅ Complete |

**Total: 37/37 tasks completed** ✅

---

## 🎯 Future Enhancements

- [ ] Add persistent storage (JSON file, database)
- [ ] Add task priorities
- [ ] Add due dates
- [ ] Add task search/filter
- [ ] Add unit tests
- [ ] Add integration tests
- [ ] Add color formatting to CLI
- [ ] Add task categories/tags

---

## 📄 License

Built for Hackathon GIAIC.

---

## 👤 Credits

Built using **Spec-Driven Development (SDD)** methodology with Claude Code.
