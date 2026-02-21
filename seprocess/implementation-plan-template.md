# Implementation Plan - Sprint [XXX] - [Title]

## File Naming Convention
- Required filename pattern: `implementation-plan-sprint-XXX-[short-topic].md`
- Example: `implementation-plan-sprint-001-anti-dup-hardening.md`
- `XXX` must be sequential across project history.

## 1. Objective
- [Primary objective]
- [Secondary objective]

## 2. Non-Goals
- [Out of scope item]
- [Out of scope item]

## 3. Current State
- [Relevant baseline behavior]
- [Known risks/constraints]

## 3.1 Discovery Snapshot (Mandatory)
- Business objective (problem value):
  - [ ] [Objective and expected outcome]
- Constraints:
  - [ ] [Technical/business/compliance/time constraints]
- Source of truth:
  - [ ] [Systems/docs/owners considered authoritative]
- Non-goals:
  - [ ] [Explicitly not solving now]

## 3.2 Knowns / Unknowns
- Knowns (validated facts):
  - [ ] [Fact + evidence]
- Unknowns (must clarify):
  - [ ] [Open item + owner]

## 3.3 Assumptions and Validation Plan
- Assumption:
  - [ ] [Assumption]
  - Validation method: [Test/data review/spike/production metric]
  - Validation checkpoint: [Milestone/date]
  - Fallback if invalid: [Plan]

## 3.4 Critical Questions Before Coding
- [ ] [Question]
- [ ] [Question]
- [ ] [Question]
- [ ] [Question]
- [ ] [Question]
- [ ] [Question]
- [ ] [Question]
- [ ] [Question]
- [ ] [Question]
- [ ] [Question]

## 5. Public Contract Impact
- Affected public interfaces (API/events/schemas):
  - [List]
- Compatibility strategy:
  - [Preserve | Additive | Versioned break]
- Contract artifacts to update:
  - [OpenAPI/JSON Schema/tests/docs]

## 6. Observability Contract
- Critical paths covered:
  - [List]
- Required fields emitted:
  - [ ] `request_id`
  - [ ] `duration_ms`
  - [ ] structured logs
- Verification approach:
  - [Unit/integration/contract assertions]

## 7. Payload Limits & Validation
- Limits applied (or project equivalents):
  - `IMPORT_MAX_FILE_MB`: [value]
  - `IMPORT_MAX_ITEMS`: [value]
  - `PROMPT_MAX_BYTES`: [value]
- Validation behavior:
  - [Accepted/rejected boundaries + error model]
- Negative tests:
  - [List]

## 8. Acceptance Criteria
- [ ] [Measurable criterion]
- [ ] [Measurable criterion]
- [ ] Critical unknowns resolved or explicitly risk-accepted.
- [ ] High-impact assumptions validated or protected by monitoring/fallback.
- [ ] Discovery evidence captured in plan and PR.

## 9. Quality Gates
- [ ] Tests pass (project command and CI lane).
- [ ] No relevant duplication increase (baseline gate).
- [ ] Contract/API behavior preserved or intentionally versioned.
- [ ] Observability contract validated (`request_id`, `duration_ms`, structured logs).
- [ ] Payload limits and validation enforced for changed critical flows.
- [ ] Documentation updated (README and related docs).
- [ ] Discovery Gate passed (critical questions answered; residual risks explicit).
- [ ] Assumption traceability passed (owner + validation + fallback for each critical assumption).

## 10. Milestones and Readiness
- Milestone mapping:
  - M1: [Definition + exit criteria]
  - M2: [Definition + exit criteria]
  - M3: [Definition + exit criteria]
- Promotion rule:
  - [Which gate evidence is required to move milestones]

## 11. Work Plan (Phased)

### Phase 1 - Discovery and Framing
Goal: [Resolve critical unknowns and de-risk assumptions]

Checklist:
- [ ] Context map complete (objective, constraints, sources, non-goals)
- [ ] 10 critical questions answered or accepted as explicit risk
- [ ] Assumption register created with validation method/checkpoint

Done Criteria:
- [ ] Ready-to-Implement gate approved

### Phase 2 - [Name]
Goal: [Goal]

Checklist:
- [ ] [Task]
- [ ] [Task]

Done Criteria:
- [ ] [Outcome]

### Phase 3 - [Name]
Goal: [Goal]

Checklist:
- [ ] [Task]
- [ ] [Task]

Done Criteria:
- [ ] [Outcome]

## 12. Risks and Mitigations
- Risk: [Risk]
  - Mitigation: [Mitigation]
- Risk: [Risk]
  - Mitigation: [Mitigation]

## 13. Release Evidence
- Required evidence bundle:
  - [ ] Test results
  - [ ] Gate status summary
  - [ ] Contract diff/changelog
  - [ ] Operational docs updated
  - [ ] Discovery evidence summary (unknowns, assumptions, open risks)
- Release decision note:
  - [Go/No-Go + rationale]

## 14. Rollout / Recovery
- Rollout: [Strategy]
- Recovery: [Tag/commit fallback]

## 15. Progress Log
- [Date] [What was completed + validation evidence]
