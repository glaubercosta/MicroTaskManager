# Quality Gates Template (Project Binding for Engineering Playbook v2)

This file binds the portable gates from the playbook to repo-specific tools and thresholds.
Keep it explicit, enforceable, and CI-ready.

## Adoption Policy
This file is bound by the **Project Binding** defined in `seprocess/playbook.md`. 

- **Source of Truth**: `seprocess/playbook.md` (Project Name, Mode, Effective Date).
- **Merge Blocking Rule**: All gates below must align with the chosen mode (Forward-Only vs Full Enforcement).

## Lane Policy
- Production Lane: All gates below are mandatory in PR/CI.
- Spike Lane: Only Reproducibility Gate is mandatory; others optional unless promoting.

## Gates

### 1) Tests Gate
Goal: Automated tests pass (local + CI).
- Command(s):
  - `pytest`
- CI job(s):
  - `tests`

Policy:
- No merge if tests fail.
- New behavior must include tests (happy path + edge + failure) unless exception approved.

---

### 2) Lint / Typecheck Gate
Goal: Lint and type checks pass.
- Lint command:
  - `ruff check`
- Typecheck command:
  - `mypy .`

Policy:
- No merge if lint/typecheck fails.

---

### 3) Duplication Gate
Goal: No meaningful duplication increase beyond threshold.
- Tool:
  - `pylint --disable=all --enable=similarities .`
- Threshold:
  - No new clones >= configured threshold or no duplication trend increase.

Policy:
- Second occurrence: extract.
- Third occurrence: merge blocked unless justified.

---

### 4) Contract Gate
Goal: Protect API/event/schema contracts.
- Source of truth:
  - OpenAPI and/or JSON Schemas.
- Validation command:
  - `...`
- Contract test command:
  - `...`

Policy:
- No merge if contract validation/tests fail.
- Contract-breaking changes require explicit versioning + migration note.
- In this repo, pre-existing legacy drift is allowed only if unchanged by the PR.

---

### 5) Observability Contract Gate
Goal: Ensure minimum runtime traceability in critical paths.
- Required fields:
  - `request_id`
  - `duration_ms`
  - structured logs (JSON-lines/equivalent)
- Validation:
  - tests/assertions on changed critical endpoints/tools.

Policy:
- No merge if changed critical flows omit required telemetry fields.

---

### 6) Payload Safety Gate
Goal: Avoid unsafe/unbounded payload handling.
- Required limits (or project equivalents):
  - `IMPORT_MAX_FILE_MB`
  - `IMPORT_MAX_ITEMS`
  - `PROMPT_MAX_BYTES`
- Validation:
  - boundary tests for accepted/rejected sizes.

Policy:
- No merge if changed import/execute flows lack explicit limits and validation.

---

### 7) Complexity Gate (Recommended)
Goal: Prevent unbounded complexity growth in new/modified code.
- Tool:
  - `...`
- Threshold:
  - Example: Cyclomatic Complexity > 10 requires justification.

Policy:
- If threshold exceeded, add refactor task or justify with exception metadata.

---

### 8) Security Readiness Gate
Goal: Prevent high-severity exposure and support enterprise readiness.
- Dependency scan tool:
  - `...`
- SAST tool:
  - `...`
- DAST (when applicable):
  - `...`
- SBOM generation tool:
  - `...`

Policy:
- No new HIGH/CRITICAL findings unless exception approved.
- Secrets must never be committed.
- New endpoints must consider authn/authz + rate limiting.

---

### 9) Reproducibility Gate (Spike Lane Minimum)
Goal: Spikes must be reproducible and isolated.
- Required:
  - Document steps in spike header.
  - Keep spike code isolated (branch, /spikes, or feature flag off by default).

---

### 10) Discovery Gate
Goal: Ensure the team understands problem scope before implementation.
- Evidence required:
  - context map (objective, constraints, source of truth, non-goals),
  - knowns/unknowns list,
  - critical questions answered (minimum 10 for non-trivial work).
- Validation source:
  - implementation plan + PR checklist.

Policy:
- No merge for non-trivial scope without discovery evidence.

---

### 11) Assumption Traceability Gate
Goal: Make assumptions explicit, testable, and recoverable.
- Evidence required for each critical assumption:
  - owner,
  - validation method,
  - validation checkpoint,
  - fallback if invalid.
- Validation source:
  - implementation plan + tests/metrics/monitoring evidence.

Policy:
- No merge if critical assumptions are undocumented or have no validation/fallback path.

---

### 12) Evaluation Gate
Goal: Verify outcomes against realistic usage, not only happy-path correctness.
- Required:
  - minimum scenario set representing production-like queries/flows,
  - defined pass/fail thresholds,
  - post-change comparison to baseline.
- Validation source:
  - benchmark/evaluation artifact linked in PR.

Policy:
- No promotion of major feature work without evaluation evidence.

---

## Exceptions (Must Be Explicit)
If any gate is intentionally violated, PR must include:
- Why needed now
- Impact/risk
- Removal/review timeline
- Mitigation (tests/monitoring/rollback)
- Linked ticket and owner

## Notes
- Update this file whenever tools/commands or thresholds change.
- Keep commands copy-paste runnable.
- Track legacy gaps as backlog items; do not normalize regressions.
