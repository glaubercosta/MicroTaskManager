# Session Kickoff: Project Initialization (MicroTaskManager)

## 1. Objective
- Formalize the project scope, constraints, and architecture for the `MicroTaskManager` pilot.
- Achieve the "Ready-to-Implement" gate for Sprint 1.

## 2. Context Map
- **Business objective**: Create a simple, robust micro task manager as a pilot for the `SEprocess`.
- **Constraints (time, tech, compliance, dependencies)**:
  - Language: Python.
  - Quality Gates: PRD-ready (TDD, Lint, Typecheck, Duplication).
  - Scope: "Simple as possible".
- **Source-of-truth systems/docs**:
  - `seprocess/playbook.md`
  - `seprocess/adapter-codex.md`
  - `seprocess/quality-gates-template.md` (Targeting Python)
- **Non-goals**: Multi-user support, complex UI (initially), third-party integrations.

## 3. Knowns vs Unknowns
- **Knowns (validated)**:
  - Tech stack: Python with pytest/ruff/mypy/pylint.
  - Process: Engineering Playbook v2.
  - Goal: Task management.
- **Unknowns (must clarify)**:
  - Storage method (SQLite, JSON, Memory?).
  - UI Type (CLI, Web, or API first?).
  - Core Task schema (status list, priority level, tags?).
  - Deployment/Packaging requirements.

## 4. Critical Questions (Before Coding)
- [x] 1. Should we use a database (SQLite) or simple file persistence (JSON/YAML) to minimize dependencies? **(Answer: SQLite)**
- [x] 2. What is the minimum Task entity? **(Answer: ID, Title, Status [todo, doing, done, Deprecated], CreatedAt, CompletedAt)**
- [x] 3. How will the user interact with it? **(Answer: REST API using FastAPI)**
- [x] 4. Does "simple as possible" include task categories or just a flat list? **(Answer: Simple flat list)**
- [x] 5. How do we handle "soft" tasks (reminders) vs "hard" tasks (with deadlines)? **(Answer: Unified approach with optional `due_at`)**
- [x] 6. Will the tool be used as a library (SDK) or a standalone executable? **(Answer: Standalone API)**
- [x] 7. How should we handle errors (TaskNotFound, InvalidStatusChange)? **(Answer: Fail Fast)**
- [x] 8. Do we need search or filtering capabilities in Sprint 1? **(Answer: Yes, by status and title)**
- [x] 9. What is the specific 'WOW' factor for this simple pilot project? **(Answer: Swagger excellence + Speed via Discovery-First)**
- [x] 10. How will we measure the success of the `SEprocess` adoption during this project? **(Answer: Gate compliance, minimal rework, docs accuracy, and TOKEN CONSUMPTION)**

## 5. Assumptions Register
- **Assumption**: A CLI-first approach is sufficient for the pilot.
  - Owner: User/Agent
  - Validation method: Review against business objective.
  - Validation checkpoint: Session Kickoff closure.
  - Fallback if invalid: Pivot to FastAPI-based web app.

- **Assumption**: SQLite is acceptable as a "zero-setup" database.
  - Owner: Agent
  - Validation method: Tech review.
  - Validation checkpoint: Discovery phase.
  - Fallback if invalid: Local JSON file.

## 6. Options and Trade-offs
- **Option A: Pure CLI**
  - Benefits: Fast to develop, easy to test, low friction.
  - Risks: Limited usability for non-technical users.
  - Why/when choose: Best for a "simple as possible" engineering pilot.
- **Option B: FastAPI (API First)**
  - Benefits: Easier to extend with a UI later, standard modern Python.
  - Risks: More boilerplate, requires server process.
  - Why/when choose: If we anticipate needing a web/mobile UI quickly.

## 7. Ready-to-Implement Gate
- [ ] Critical unknowns resolved or risk-accepted
- [ ] High-impact assumptions have validation and fallback
- [ ] Acceptance criteria are measurable
- [ ] Quality gates for this scope are identified

## 8. Execution Plan (Short)
1. Categorize and answer critical questions.
2. Define Task model and persistence layer.
3. Setup TDD boilerplate matching quality gates.

## 9. Validation Plan
- Tests: Pytest suite with 100% coverage on core logic.
- Metrics: Quality gates compliance (Ruff/Mypy/Pylint).
- Rollback signal: Architecture becomes too complex for a "micro" tool.
