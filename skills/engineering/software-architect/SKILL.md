---
name: software-architect
description: Decide the minimum viable architecture for the real context. Use when starting projects, facing structural changes, or evaluating monolith vs microservices.
---

# Software Architect

## Purpose

Decide the minimum viable architecture based on the project's real context — stage, domain, load, and team. The goal is the simplest structure that solves today's problems without creating tomorrow's bottlenecks. Architecture is a tool, not a destination.

## When to Use

- Starting a new project (choosing the initial structure)
- Facing significant structural changes (new domains, major integrations, new teams)
- Choosing between two architectural approaches with unclear trade-offs
- Evaluating whether to evolve the current architecture (e.g., monolith to services)
- When the team is blocked by the current structure (deploy conflicts, coupling pain)

## When NOT to Use

- Local changes within a single module — those don't need architectural decisions
- Choosing specific libraries or tools — that's `researcher`
- When the architecture is already decided and only needs implementation — don't reopen decisions without new pain
- Premature scaling: don't design for 10M users when you have 100

## Expected Inputs

- Context summary from `references/context-analyzer.md` (stage, domain, real load, team size and skills)
- Known constraints (budget, deadlines, team's technology stack)
- The specific architectural question to resolve

## Expected Output

```
Architecture: <decision>
Rationale: <1-3 sentences tied to context>
What we WON'T do and why: <list>
Evolution signals: <what pain would justify the next level>
```

## Internal Rules

### The Complexity Ladder

Every project sits on this ladder. Move up only when measured pain forces it — never preemptively.

| Context | Architecture | Rationale |
|---------|-------------|-----------|
| Idea / prototype | Single script or single-module app | Validate the idea, nothing else matters |
| MVP, uncertain domain | Simple monolith | One deployable, one database, minimal ceremony |
| Production, clear domain | Modular monolith | Clear module boundaries, shared deploy, enforced interfaces |
| Proven scale + independent teams | Extract services where it hurts | Service boundary follows team boundary and measured bottleneck |

### Core Principles

1. **Never start with microservices.** Services are extracted from a working monolith when there's measured pain — they're never designed from scratch. See criteria in `references/microservices.md`.

2. **Layers only when justified.** Add a layer only when more than one consumer needs that logic. A single-consumer abstraction layer is indirection without value.

3. **Locate the project on the complexity ladder** using `references/decision-rules.md` before making any recommendation.

4. **Document irreversible decisions** as ADRs in the project repo (e.g., `docs/adr/`). Reversible decisions don't need documentation — just make them and move on.

5. **Separate reversible from irreversible.** Database schema, public API contracts, and data model choices are hard to reverse — invest time there. Framework choice, folder structure, and internal module boundaries are easy to reverse — decide quickly.

### Decision Process

```
1. Gather context    → stage, domain, load, team (references/context-analyzer.md)
2. Locate on ladder  → where does this project sit today? (references/decision-rules.md)
3. Identify pain     → what specific problem needs an architectural answer?
4. Propose minimum   → simplest structure that solves the pain
5. Define boundaries → what we WON'T do and why
6. Set evolution signals → what measurable pain would trigger the next level
```

### Anti-Patterns to Catch

| Anti-Pattern | Signal | Correction |
|---|---|---|
| Resume-driven architecture | "Let's use Kubernetes" with no scale requirements | Match infra to actual stage |
| Premature abstraction | Interfaces with a single implementation | Remove until second consumer exists |
| Invisible coupling | Module A imports Module B's internals | Define explicit interfaces between modules |
| Architecture astronaut | Weeks of design, zero lines of code | Time-box architecture decisions; build and learn |
| Cargo cult | "Netflix does it this way" | Netflix has 10,000 engineers; what does YOUR context need? |

## Examples

**Example 1 — Startup asking for "SaaS architecture":**

Context: 2-person team, MVP stage, uncertain domain, zero users.

Decision:
```
Architecture: Simple monolith (Next.js + PostgreSQL on Railway)
Rationale: MVP with uncertain domain — minimize moving parts, maximize iteration speed.
What we WON'T do: microservices, message queues, Kubernetes, separate frontend/backend repos.
Evolution signals: deploy conflicts between team members, or a single module consuming >70% of resources with a clear domain boundary.
```

**Example 2 — Monolith with a measured bottleneck:**

Context: Production app, modular monolith, reporting module consuming 80% of CPU (measured over 2 weeks).

Decision:
```
Architecture: Extract reporting as a standalone service.
Rationale: Clear domain boundary, measured resource contention, independent scaling need.
What we WON'T do: extract any other module — no pain, no extraction.
Evolution signals: if another module shows similar contention patterns with clear boundaries.
```

**Example 3 — Team wants to "modernize" a working monolith:**

Context: Monolith serving 50k users, 5-person team, no measured pain, deploys take 10 minutes.

Decision:
```
Architecture: Keep the monolith. Invest in modular boundaries instead.
Rationale: No measured pain. 10-minute deploys are fine for this team size. Microservices would triple operational complexity without solving a real problem.
What we WON'T do: break into services without evidence of pain.
Evolution signals: deploy frequency blocked by team growth, or module-level scaling needs proven by metrics.
```

## Verification

Before finalizing an architecture decision:

- [ ] The project's position on the complexity ladder is identified with evidence
- [ ] The decision solves a real, current problem — not a hypothetical future one
- [ ] The "What we WON'T do" list is explicit and justified
- [ ] Evolution signals are measurable, not vague ("when we need to scale")
- [ ] Irreversible decisions are documented as ADRs
- [ ] The team can operate this architecture with their current skills
- [ ] Run the checklist in `references/checklist-architecture-review.md`

## References (load only when needed)

Paths relative to this skill's folder:

- `references/context-analyzer.md` — how to gather context (stage, domain, load, team)
- `references/decision-rules.md` — complexity ladder and decision format
- `references/architecture-decider.md` — from context to minimum viable architecture
- `references/microservices.md` — when to extract services and when not to
- `references/checklist-architecture-review.md` — final verification checklist
- `references/playbooks/` — guides by project type: `build-saas.md`, `build-api.md`, `build-dashboard.md`, `build-ecommerce.md`, `build-mobile-app.md`, `build-enterprise-app.md`
