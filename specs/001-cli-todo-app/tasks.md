# Tasks: CLI Todo App

**Input**: Design documents from `/specs/001-cli-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/

**Tests**: The spec does not explicitly request tests. Tests are NOT included in this task breakdown.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create src/ directory structure with subfolders: agents/, skills/, models/, cli/, lib/
- [X] T002 Create tests/ directory structure with subfolders: contract/, integration/, unit/
- [X] T003 Create all __init__.py files in src/ subdirectories
- [X] T004 [P] Create main CLI entry point file at src/cli/main.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 [P] Create Task model class in src/models/task.py with id, title, description, completed attributes
- [X] T006 Create TaskList class in src/models/task_list.py with add, get, get_all, update, delete, toggle operations
- [X] T007 [P] Implement ValidateID skill in src/skills/validate_id.py to check if task ID exists
- [X] T008 [P] Implement ValidateTitle skill in src/skills/validate_title.py to ensure non-empty title
- [X] T009 [P] Create ValidationAgent in src/agents/validation_agent.py with ValidateID and ValidateTitle capabilities

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Users can create new tasks with title and optional description

**Independent Test**: Add a task by selecting "Add Task" from menu, entering title/description, and verify it appears in task list

### Implementation for User Story 1

- [X] T010 [P] Implement AddTask skill in src/skills/add_task.py that creates task with next sequential ID
- [X] T011 [US1] Implement TaskManagerAgent in src/agents/task_manager.py with add task capability
- [X] T012 [US1] Implement ShowMenu skill in src/skills/show_menu.py to display main menu options
- [X] T013 [US1] Implement PromptUserChoice skill in src/skills/prompt_user.py to capture user menu selection
- [X] T014 [P] [US1] Create DisplayAgent in src/agents/display_agent.py with ShowMenu and PromptUserChoice capabilities
- [X] T015 [US1] Implement ViewTasks skill in src/skills/view_tasks.py to display task list
- [X] T016 [US1] Create TodoCLI_MasterAgent in src/agents/master_agent.py to coordinate agents and run main menu loop

**Checkpoint**: At this point, User Story 1 (Add Task) should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can see all tasks with ID, title, description, and status

**Independent Test**: Add 2-3 tasks, select "View All Tasks", verify all tasks displayed correctly with status

### Implementation for User Story 2

- [X] T017 [US2] Update ViewTasks skill in src/skills/view_tasks.py to show formatted table with headers
- [X] T018 [US2] Add empty list handling to ViewTasks skill to show "No tasks yet" message
- [X] T019 [US2] Update DisplayAgent to properly route View menu option to ViewTasks skill

**Checkpoint**: At this point, User Stories 1 AND 2 (Add and View) should both work independently

---

## Phase 5: User Story 3 - Toggle Task Completion (Priority: P1)

**Goal**: Users can mark tasks as complete or incomplete

**Independent Test**: Add a task, toggle it to complete, verify status changes in task list

### Implementation for User Story 3

- [X] T020 [P] [US3] Implement ToggleTaskComplete skill in src/skills/toggle_task.py to flip completed status
- [X] T021 [US3] Add toggle capability to TaskManagerAgent in src/agents/task_manager.py
- [X] T022 [US3] Update TodoCLI_MasterAgent to route Toggle Complete menu option to correct agents

**Checkpoint**: At this point, User Stories 1, 2, AND 3 (Add, View, Toggle) should all work independently

---

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: Users can modify task title and description

**Independent Test**: Add a task, update its title and description, verify changes reflected

### Implementation for User Story 4

- [X] T023 [P] [US4] Implement UpdateTask skill in src/skills/update_task.py to modify task attributes
- [X] T024 [US4] Add update capability to TaskManagerAgent in src/agents/task_manager.py
- [X] T025 [US4] Update TodoCLI_MasterAgent to route Update menu option to correct agents

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P2)

**Goal**: Users can remove tasks after confirmation

**Independent Test**: Add tasks, delete one, confirm deletion, verify it no longer appears

### Implementation for User Story 5

- [X] T026 [P] Implement ConfirmAction skill in src/skills/confirm_action.py to prompt for y/n confirmation
- [X] T027 [P] [US5] Implement DeleteTask skill in src/skills/delete_task.py to remove task from TaskList
- [X] T028 [US5] Add delete capability to TaskManagerAgent in src/agents/task_manager.py
- [X] T029 [US5] Update DisplayAgent to route Delete menu option with confirmation
- [X] T030 [US5] Update TodoCLI_MasterAgent to route Delete menu option to correct agents

**Checkpoint**: At this point, all user stories (1-5) should be independently functional

---

## Phase 8: User Story 6 - Exit Application (Priority: P3)

**Goal**: Users can safely exit CLI application

**Independent Test**: Run CLI, select "Exit", verify application closes cleanly

### Implementation for User Story 6

- [X] T031 [US6] Update TodoCLI_MasterAgent to handle Exit menu option with graceful termination
- [X] T032 [US6] Add Ctrl+C signal handler to src/cli/main.py for clean exit

**Checkpoint**: All user stories should now be complete and functional

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T033 Update ViewTasks skill to handle description truncation for long descriptions
- [X] T034 Add consistent error message formatting across all skills
- [X] T035 [P] Add inline docstrings to all agent classes
- [X] T036 [P] Add inline docstrings to all skill functions
- [X] T037 Validate master agent properly routes all menu options to correct agents

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-8)**: All depend on Foundational phase completion
  - User stories can proceed in order: Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7 → Phase 8
  - Or partially in parallel: Phase 3 (P1 stories) first, then Phase 6-7 (P2 stories), then Phase 8 (P3 story)
- **Polish (Phase 9)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (Add Task) - P1**: Can start after Foundational (Phase 2)
- **User Story 2 (View Tasks) - P1**: Can start after Foundational (Phase 2), integrates with US1 for display
- **User Story 3 (Toggle) - P1**: Can start after Foundational (Phase 2), depends on TaskList from US1
- **User Story 4 (Update) - P2**: Can start after Foundational (Phase 2), depends on TaskList from US1
- **User Story 5 (Delete) - P2**: Can start after Foundational (Phase 2), depends on TaskList from US1 and Validation from Phase 2
- **User Story 6 (Exit) - P3**: Can start after Foundational (Phase 2), integrates with master agent

### Within Each User Story

- Skills before agents (skills define atomic operations)
- Agents consume skills (agents coordinate skills)
- Master agent coordinates all agents
- Display agent handles all user-facing output

### Parallel Opportunities

- **Setup (Phase 1)**: All tasks (T001-T004) can run in parallel
- **Foundational (Phase 2)**: All model and validation tasks (T005-T009) can run in parallel (within Phase 2)
- **User Story 1 (Phase 3)**: Skills (T010, T012, T013, T015) can run in parallel
- **User Story 4 (Phase 6)**: Skills (T026, T027) can run in parallel
- **Polish (Phase 9)**: Documentation tasks (T035, T036) can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all skills for User Story 1 together:
Task: "Implement AddTask skill in src/skills/add_task.py"
Task: "Implement ShowMenu skill in src/skills/show_menu.py"
Task: "Implement PromptUserChoice skill in src/skills/prompt_user.py"
Task: "Implement ViewTasks skill in src/skills/view_tasks.py"

# Then launch agents in parallel:
Task: "Implement TaskManagerAgent in src/agents/task_manager.py"
Task: "Create DisplayAgent in src/agents/display_agent.py"

# Finally, integrate with master agent
Task: "Create TodoCLI_MasterAgent in src/agents/master_agent.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1-3 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. Complete Phase 5: User Story 3 (Toggle)
6. **STOP and VALIDATE**: Test all P1 stories independently
7. Demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Demo (MVP!)
3. Add User Story 2 → Test independently → Demo
4. Add User Story 3 → Test independently → Demo
5. Add User Story 4 → Test independently → Demo
6. Add User Story 5 → Test independently → Demo
7. Add User Story 6 → Test independently → Demo
8. Each story adds value without breaking previous stories

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

**Task Summary**:
- Total tasks: 37
- Setup phase: 4 tasks
- Foundational phase: 5 tasks
- User Story 1: 7 tasks
- User Story 2: 3 tasks
- User Story 3: 3 tasks
- User Story 4: 3 tasks
- User Story 5: 5 tasks
- User Story 6: 2 tasks
- Polish phase: 5 tasks
