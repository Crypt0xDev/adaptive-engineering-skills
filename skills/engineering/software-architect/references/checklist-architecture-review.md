# Checklist: Architecture Review

## Context
- [ ] Does the architecture match the project's real stage (ladder from `references/decision-rules.md`)?
- [ ] Does every component have a one-sentence business justification?
- [ ] Is it documented what will NOT be done and why?

## Simplicity
- [ ] Can any layer or service be removed without losing functionality?
- [ ] Are there abstractions without a second consumer?
- [ ] Were microservices avoided without proven domain boundaries?

## Evolution
- [ ] Are irreversible decisions (DB, public API, contracts) documented as ADRs in the project repo?
- [ ] Are there defined signals that would indicate when to evolve to the next level?

## Risks
- [ ] Is the most likely single point of failure identified?
- [ ] Do external integrations have failure handling?
