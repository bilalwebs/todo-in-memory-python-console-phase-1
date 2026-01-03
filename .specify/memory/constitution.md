<!--
  Sync Impact Report
  ==================
  Version change: N/A → 1.0.0 (initial constitution)

  Modified principles: N/A (all new)
  Added sections: 7 Core Principles, Quality Rules, Development Workflow
  Removed sections: None

  Templates status:
  - .specify/templates/plan-template.md ✅ no changes needed (generic structure)
  - .specify/templates/spec-template.md ✅ no changes needed (generic structure)
  - .specify/templates/tasks-template.md ✅ no changes needed (generic structure)
  - .specify/templates/commands/*.md ⚠️ no command files exist (pending)

  Follow-up TODOs: None
-->

# Phase-I CLI Todo App Constitution

## Core Principles

### I. In-Memory Storage Only
All application data MUST be stored exclusively in memory during runtime. No databases, file persistence, or external storage systems are permitted. This ensures simplicity and aligns with the CLI-focused nature of the application.

**Rationale**: Eliminates complexity of database setup, migration, and connection management. Data is ephemeral and resets on application restart.

### II. CLI-Only Interface
All user interactions MUST occur through the command-line interface. No web UI, GUI, or API endpoints are required or permitted. The application accepts input via stdin/args and produces output to stdout.

**Rationale**: Keeps the application lightweight and focused on its core purpose as a developer productivity tool.

### III. Task Data Structure
Every task MUST have the following attributes:
- `id`: Integer, auto-incrementing and unique
- `title`: String, required, non-empty
- `completed`: Boolean, defaults to false
- `description`: Optional string for additional context

**Rationale**: Simple, predictable structure that is easy to understand and validate. No optional nested objects or complex types.

### IV. Single Responsibility for Agents
Every agent MUST have a clearly defined, narrow scope. Agents MUST NOT handle concerns outside their explicit responsibilities. The Master agent coordinates sub-agents but MUST NOT contain direct task manipulation logic.

**Rationale**: Prevents spaghetti code where logic is scattered across multiple agents. Easier to test, debug, and extend.

### V. Atomic, Reusable Skills
Every skill MUST perform exactly one action and be independently testable. Skills MUST NOT have hidden dependencies or side effects beyond their documented purpose.

**Rationale**: Skills become building blocks that can be composed in different ways. Reduces bugs and improves maintainability.

### VI. No External Integrations
The application MUST NOT include web frameworks, authentication systems, or AI chatbot integrations. Third-party APIs, OAuth, and similar external services are explicitly out of scope.

**Rationale**: Strips away complexity not needed for a todo application. Reduces attack surface and dependency maintenance burden.

### VII. Readable Logic for Beginners
Code MUST be written with clarity and learnability as priorities. Complex patterns SHOULD be avoided when simpler alternatives exist. Comments SHOULD explain the "why" not the "what".

**Rationale**: This project serves as an educational example. Code should be approachable for developers learning agent-based architectures.

## Quality Rules

All implementations MUST comply with these quality standards:

1. **Input Validation**: Every user input MUST be validated before execution. Invalid input MUST produce a clear error message.

2. **Unique Sequential IDs**: Task IDs MUST be unique integers that increment sequentially. Deleted task IDs MUST NOT be reused.

3. **Destructive Action Confirmation**: Delete and similar destructive operations MUST prompt for user confirmation before execution.

4. **Consistent CLI Display**: Task output MUST be formatted consistently. Clear column headers and aligned columns required.

5. **Master Agent Coordination**: The Master agent delegates to sub-agents but contains no business logic itself.

## Development Workflow

### Phase Structure
1. **Spec Phase**: Define requirements and user stories
2. **Plan Phase**: Design architecture and interfaces
3. **Tasks Phase**: Break down work into testable tasks
4. **Red Phase**: Write failing tests first
5. **Green Phase**: Implement minimal code to pass tests
6. **Refactor Phase**: Improve code while maintaining passing tests

### Agent Responsibilities
- **TaskModelAgent**: Defines and manages the task data structure
- **TaskLogicAgent**: Implements CRUD operations and validation
- **CLIAgent**: Handles user interaction and output formatting

### Code Standards
- Follow single responsibility principle at function and module level
- Keep functions under 30 lines where practical
- Use meaningful variable and function names
- No magic numbers or hardcoded values (use constants)
- Validate all inputs at system boundaries

## Governance

This constitution is the authoritative source for all project decisions. It supersedes individual preferences and informal practices.

### Amendment Process
1. Proposed amendments MUST be documented with rationale
2. Changes MUST update the constitution version
3. Major changes require review and approval
4. Breaking changes MUST include migration guidance

### Versioning
- **MAJOR**: Incompatible principle changes or removals
- **MINOR**: New principles or significant expansions
- **PATCH**: Clarifications, wording fixes, non-semantic changes

### Compliance
All code contributions MUST be verified against this constitution. Reviews MUST check for:
- Principle violations
- Quality rule adherence
- Agent responsibility boundaries

**Version**: 1.0.0 | **Ratified**: 2026-01-03 | **Last Amended**: 2026-01-03
