# PR Checklist (Engineering Playbook v2)

> Use this checklist for every PR. Delete items that do not apply only when clearly irrelevant.

## Meta
- [ ] Lane selected: **Spike** | **Production**
- [ ] AI-assisted: **Yes** | **No**
  - If Yes: scope disclosed (files/sections) + what was manually verified

## Discovery & Collaboration
- [ ] Context map captured (objective, constraints, source of truth, non-goals)
- [ ] Critical questions answered before implementation (or risk-accepted explicitly)
- [ ] Assumptions documented with owner + validation + fallback
- [ ] Alternatives and trade-offs were considered and recorded

## Scope & Plan
- [ ] Scope is clear and minimal (no unrelated refactors)
- [ ] Implementation plan linked (required for non-trivial work)
- [ ] Acceptance criteria defined and met
- [ ] If architecture/security/dependency decisions: ADR linked (if applicable)

## Tests (TDD / Coverage)
- [ ] Tests added/updated for changed behavior
- [ ] Includes: happy path + edge case + failure case (Production Lane)
- [ ] Refactors with behavior risk have characterization tests first
- [ ] All tests pass locally and in CI

## Quality Gates
- [ ] Lint/static checks pass
- [ ] Duplication gate satisfied (no new meaningful clones beyond threshold)
- [ ] Complexity gate satisfied or justified (if configured)
- [ ] Security baseline satisfied (dependency scan / SAST where configured)
- [ ] Discovery, assumption traceability, and evaluation gates satisfied (if applicable)

## Security & Privacy Minimums (Production Lane)
- [ ] No secrets/tokens committed
- [ ] Logs reviewed: no PII/secrets leakage
- [ ] Input validation at boundaries (API/UI/CLI) considered/implemented
- [ ] New endpoints reviewed for authn/authz + abuse controls (rate limiting, CORS)

## Documentation
- [ ] README updated if behavior/config/workflow changed
- [ ] Docs include verify + rollback steps (where relevant)
- [ ] Examples are runnable and current

## Release Hygiene / Return Points
- [ ] Commits are focused and reversible
- [ ] Checkpoint tag created for non-trivial milestones (if applicable)
- [ ] Rollback path is explicit (tag/commit reference)

## Exceptions (If Any)
- [ ] Exception declared with: why now, impact/risk, timeline, mitigation
