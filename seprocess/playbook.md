# Engineering Playbook v2 (Portable Project Standard)

## Purpose
Define a reusable engineering workflow for new and existing projects with explicit standards for discovery-first planning, TDD, implementation plans, anti-duplication, contract governance, observability, documentation quality, and release hygiene.

## Scope
- Applies to all code changes.
- Covers discovery, implementation, tests, review, documentation, and CI.
- Technology-agnostic by design.

## Policy Mode (Project Binding)
When adopting this playbook in a project, define one mode explicitly:

- `Forward-Only + Frozen Baseline`:
  - legacy behavior before adoption is non-blocking by default,
  - new/modified scope must comply,
  - merges are blocked for regressions and new non-compliance.
- `Full Immediate Enforcement`:
  - all active scope must comply immediately,
  - merges are blocked for any non-compliance.

Project binding block (fill in target project):
- Project: [name]
- Mode: [Forward-Only + Frozen Baseline | Full Immediate Enforcement]
- Effective date: [YYYY-MM-DD]
- Legacy handling rule: [explicit rule]

## Working Mode (Always-On)
For every session, follow this sequence:
1. Context scan (current behavior, risks, constraints).
2. Discovery-first protocol (unknowns, assumptions, critical questions).
3. Baseline (tests + git status + quality gates state).
4. Plan (use implementation plan template for non-trivial work).
5. Build incrementally (small reversible changes).
6. Validate (tests + gates).
7. Update docs + plan status.
8. Commit/tag with recovery point when milestone is reached.

## Discovery-First Protocol (Mandatory Before Coding)
Before implementation, produce and validate:
- Problem map:
  - business objective,
  - constraints,
  - source-of-truth systems,
  - non-goals.
- Knowns vs Unknowns:
  - what is validated,
  - what is still assumption,
  - what can break in production.
- Critical questions list:
  - include "questions we are not asking yet" (minimum 10 for non-trivial work).
- Assumption register:
  - each assumption has owner, validation method, and due checkpoint.

Implementation must not start until "Ready to Implement" is met:
- critical unknowns are resolved or explicitly risk-accepted,
- high-impact assumptions have validation plan,
- acceptance criteria and gates are measurable.

## TDD Standard (Operational)
1. Red: write or adjust a failing test first.
2. Green: implement minimum code to pass.
3. Refactor: improve design with tests still green.

Rules:
- Refactors with behavior risk require characterization tests first.
- No feature is complete without automated test coverage for the changed behavior.

## Contract-First Delivery
- Public contract changes (API/request/response/schema/events) must be explicit in planning.
- Contract compatibility strategy must be declared: preserved, additive, or versioned break.
- JSON/OpenAPI schema updates must be synchronized with tests and documentation.
- In this repo, legacy contract drift is tracked and prioritized, but only new regressions block merges.

## Operational Telemetry Minimum
For critical execution paths, the response and logs must support traceability:
- `request_id` for correlation.
- `duration_ms` for latency tracking.
- Structured logs (JSON-lines or equivalent) with contextual fields.

Telemetry rules:
- New endpoints/features must include telemetry fields from day one.
- Existing legacy endpoints may be remediated incrementally, but new regressions are blocked.

## Semantic Catalog Operations Standard
For metadata-heavy environments, apply this operating profile:
- Refresh cadence target: 24h (`CATALOG_SNAPSHOT_STALE_AFTER_SECONDS=86400`).
- Prefer async refresh with progress/status payload for large catalogs.
- Discovery flow:
  - semantic-first (`search_semantic_catalog`),
  - structural validation (`list_database_structure`),
  - join validation (`inspect_join_paths`),
  - final execution (`query_database`).
- Freshness/state checks must use live tools (`query_database`, `list_empty_tables`, `get_table_stats`).

Troubleshooting minimum runbook:
1. Confirm active scope (`get_active_context`).
2. Validate runtime adapter (`get_connection_capabilities`).
3. Inspect refresh status payload (`status`, `processed_tables`, `total_tables`, `result`/`error`).
4. If metadata-catalog access alert appears, treat as partial refresh:
   - vector index may be updated,
   - snapshot persistence may have failed,
   - fix metadata catalog access and refresh again.
5. Export scoped snapshot (`export_catalog_snapshot_json`) for verification/audit.

## Sprint Documentation Triad
Every sprint must keep these artifacts synchronized:
- Project knowledge base (context, backlog, decisions snapshot).
- Operational README (setup, env vars, run/verify/rollback).
- ADR index (decision records and status).

Rule:
- Sprint closure is incomplete if triad updates are missing for changed behavior/process.

## Milestone Mapping Standard
Implementation plans must map delivery to milestones (`M1..Mn`) with explicit readiness criteria.
- Each milestone needs measurable exit criteria.
- Promotion between milestones requires quality gate evidence.

## Implementation Plan Standard
Mandatory when work is non-trivial (multi-file change, architecture, reliability, performance, security):
- Define scope and non-goals.
- Define acceptance criteria and quality gates.
- Break into phases with checklist.
- Update checklist status after each validated phase.

Naming and lifecycle rules:
- Every planning effort must generate its own implementation plan instance.
- Plan file name must include the sprint number in sequential order.
- Recommended pattern: `implementation-plan-sprint-XXX-[short-topic].md`.
- Sprint numbering must be monotonic and never reused.

Use templates from the `seprocess/` directory:
- `seprocess/implementation-plan-template.md`
- `seprocess/pr-checklist-template.md`
- `seprocess/session-kickoff-template.md`
- `seprocess/discovery-checklist-template.md`
- `seprocess/adr-template.md`
- `seprocess/spike-header-template.md`

## Anti-Duplication Standard
1. Single Source of Truth:
- Shared logic must live in one reusable function/helper/module.

2. Extraction Trigger:
- Second occurrence: extract.
- Third occurrence: merge blocked unless justified.

3. Consistency:
- Repeated output/error formatting must use centralized formatters.
- Repeated execution flows must be helperized.
- Repeated test setup must move to fixtures/factories.

## README and Documentation Standard
README must be updated whenever behavior/config/workflow changes:
- Features and behavior changes.
- Environment variables and defaults.
- Usage and operational flow.
- Testing/CI gates.

Documentation quality criteria:
- Accurate, current, and runnable examples.
- Explicit assumptions and constraints.
- Operational guidance (how to verify and rollback).

## Quality Gates (Default)
- Automated tests pass.
- No increase in relevant code duplication (baseline trend gate).
- Lint/static checks pass as configured.
- Contract/API behavior preserved or explicitly versioned.
- Telemetry minimum present in critical execution paths.
- Discovery and assumption traceability evidence is present for non-trivial work.

## PR Review Protocol
Reject PR if any:
- New meaningful duplication without rationale.
- Missing tests for changed behavior.
- Docs/README not updated when required.
- Plan/checklist not updated for planned work.
- CI/gates failing.
- New contract drift or missing telemetry on new/modified critical paths.
- Critical assumptions are undocumented or unvalidated.

## Exception Protocol
Allowed only with explicit note in PR:
- Performance-critical measured path.
- Temporary migration bridge with follow-up removal ticket.
- Minimal duplication for test readability.

Required metadata for exceptions:
- Why needed now.
- Impact/risk.
- Removal or review timeline.
- Linked ticket/owner.

## Release Hygiene
- Commit in focused units.
- Tag stable milestones.
- Keep rollback path explicit (tag/commit reference).

## Return Points (Checkpoint Policy)
Return points are mandatory for non-trivial work.

When to create a checkpoint:
- After each completed task in the active implementation plan.
- At the end of each delivery slice.
- Before risky refactors or contract changes.

Checkpoint minimum requirements:
- Tests and quality gates are green.
- Plan status is updated with evidence.
- Commit is focused and reversible.
- Annotated tag is created with clear stage naming.

Recommended tag patterns:
- Task checkpoint: `sprint-XXX-task-YY-checkpoint`
- Slice checkpoint: `sprint-XXX-slice-N-checkpoint`
- Stable milestone: `sprint-XXX-milestone-[name]`

Checkpoint workflow:
1. Validate (tests + duplication gate + configured CI-equivalent checks).
2. Commit focused changes.
3. Create annotated tag.
4. Optionally push commit/tag immediately for remote recovery.

## Session Definition of Done (DoD)
A session is considered done when:
- Tests and quality gates pass.
- No new relevant duplication is introduced.
- Active implementation plan is updated with validated progress.
- README/docs are updated when behavior/config/workflow changes.
- Contract and telemetry requirements are met for changed critical paths.
- Discovery and assumption evidence are captured for non-trivial scope.
- Commit/tag strategy is applied for milestone-level changes.

## Session Starter Prompt (Recommended)
"Apply Engineering Playbook v2. Before implementing, run discovery-first: list assumptions, identify unknowns, ask critical questions, challenge weak premises, and propose options with trade-offs. Then execute with contract-first delivery, telemetry minimum, implementation plan discipline, anti-duplication, documentation-first updates, and quality gates."
