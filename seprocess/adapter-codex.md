# Adapter: Codex

Use this adapter when collaborating with Codex-style coding agents.

## Session Starter Prompt
Apply the Engineering Playbook Core. Before coding, run discovery-first: map objective, constraints, source-of-truth, non-goals, unknowns, and assumptions. Ask critical questions, challenge weak premises, and propose options with trade-offs. Only implement after Ready-to-Implement gate is satisfied. During implementation enforce tests, contract safety, observability, documentation updates, and quality gates.

## Required Artifacts Per Non-Trivial Task
- `seprocess/session-kickoff-template.md`
- `seprocess/discovery-checklist-template.md`
- `seprocess/implementation-plan-*.md`
- `seprocess/pr-checklist-template.md`

## Collaboration Rules
- Prefer short iterative slices with explicit checkpoints.
- Treat assumptions as testable hypotheses.
- Stop and escalate when critical unknowns remain unresolved.
