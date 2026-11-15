---
name: grounded-technical-decisions
description: "Makes grounded technical decisions based on the project's real context — not assumptions. Use ALWAYS when choosing between technical options (architecture, library, framework, database, pattern, implementation approach, refactoring strategy) or when the user asks 'which should I use' / 'what's best for this' / 'is this the right choice'. Gathers context first, analyzes the concrete case, then delivers a reasoned recommendation with explicit trade-offs."
---

# Context-Grounded Technical Decisions

## Purpose

Make technical decisions grounded in the project's real context. Before recommending anything, understand the actual project: its size, stage, stack, constraints, and who maintains it. A recommendation based on an imagined project is worse than none — it sounds convincing but doesn't apply.

## When to Use

- Choosing between technical approaches (architecture, patterns, implementation strategies)
- Recommending a technology, library, framework, or database
- Answering "which should I use?", "what's best for this?", "is this the right approach?"
- Any decision where context changes the answer
- Evaluating whether to migrate, refactor, or keep the current approach

## When NOT to Use

- The decision is purely cosmetic (naming style, formatting) — follow the project's existing convention
- The user already made the decision and just wants implementation help — use `engineering-best-practices` instead
- You're choosing between equivalent options where context doesn't matter (both are fine)

## The Golden Rule: Don't Fabricate, Verify

| Principle | What It Means |
|-----------|---------------|
| **Don't fabricate context** | If a fact needed for the decision isn't confirmed, ask or explicitly mark it as an assumption — never assume the best case and proceed as if it were true |
| **Verify with real tools** | If the decision depends on external facts (does a library exist? what does the official docs say? is there an existing solution?), check before asserting |
| **If you can't verify, say so** | Don't fill a gap with a confident-sounding statement |
| **Official docs > blogs > memory** | Always prefer authoritative sources |

## The Process

### Step 1 — Gather Real Context (Before Forming an Opinion)

Find out what's missing from this list (ask only what isn't already known from the conversation or visible code):

```
CONTEXT CHECKLIST:
→ Stage and objective: Prototype/MVP to validate, or system to maintain and grow?
→ Actual size: How many entities, expected users, data volume, how many devs?
→ Existing stack and constraints: What does the project already use? What does the team know? Hosting/budget limits?
→ The actual problem: What pain point triggers this decision?
```

Many "decisions" (`Should I use GraphQL?`, `Do I need Redis?`) are solutions looking for a problem. Confirm the real pain point first.

If the available code/context is sufficient, don't over-ask. If a decisive factor is in doubt, ask before deciding.

### Step 2 — Analyze the Concrete Case (Not the Generic One)

Compare real options against the gathered context, not against abstract "best practices":

| Do | Don't |
|----|-------|
| Name trade-offs specific to THIS project | Say "X is more scalable" without qualification |
| Consider "do nothing / keep what you have" as a valid option | Assume change is always better |
| Verify claims about tools before recommending | Recommend based on general reputation |
| Weigh the team's existing expertise | Ignore learning curve and maintenance cost |

#### The Complexity Ladder (Start at the Lowest Level That Works)

Place the project on the minimum viable step. Move up only with evidence of real pain — not anticipated pain:

| Level | When | Example |
|-------|------|---------|
| Script / function | One-off task, no state | Data migration, cron job, build script |
| Simple monolith | MVP, small team, uncertain domain | Next.js + PostgreSQL, Django + SQLite |
| Modular monolith | Clear domain, growing team | Bounded contexts within one deployable |
| Separate services | Proven domain boundaries + real need for independent scaling | Extract the one module that actually needs it |

**Never start with microservices.** They are extracted where it hurts, not designed from scratch.

#### Reversible vs. Irreversible Decisions

| Type | Approach | Examples |
|------|----------|---------|
| **Reversible** | Decide quickly, don't over-analyze | Names, internal structure, a scoped pattern, a library for a small feature |
| **Irreversible** | Analyze carefully, document the reasoning | Database engine, public API contract, data schema, authentication provider |

Irreversible decisions deserve an ADR (Architecture Decision Record) in the project's `docs/adr/` folder.

### Step 3 — Deliver the Grounded Decision

A good technical recommendation has these properties:

1. **Clear recommendation** — not "it depends" without a conclusion
2. **Reason anchored to real context** — not generic advantages
3. **Explicit trade-offs** — what you're accepting and what you're giving up
4. **Confidence markers** — distinguish fact / estimate / recommendation / opinion
5. **Flagged unknowns** — if any part depends on unconfirmed data, say so

For significant decisions (architecture, stack, irreversible choices), close with this format:

```
Decision: <what was chosen>
Reason: <1-3 sentences tied to the project's context>
What we WON'T do and why: <list>
Signals to evolve: <what pain would justify the next level>
```

If context isn't sufficient for a confident recommendation, say so and ask for the missing data point — don't force an answer.

## Anti-Patterns to Detect and Stop

When a proposal (yours or the user's) falls into one of these, name it and offer the antidote:

| Anti-Pattern | Signal | Antidote |
|-------------|--------|----------|
| **Over-engineering** | Solving problems that don't exist (config/flexibility with no consumers) | KISS + complexity ladder |
| **Premature abstraction** | Interfaces/factories/generic layers before 2+ real use cases | Rule of three: abstract on the third repetition |
| **Unnecessary microservices** | Splitting without proven domain boundaries | Modular monolith first |
| **Cargo cult** | Copying Netflix/Google architecture in a different context | The context defines the solution, not the company that built it |
| **Resume-driven development** | Choosing technology for trendiness or CV | Stack the team knows, unless there's a strong documented reason |
| **Premature optimization** | Optimizing without measuring | Measure → find the real bottleneck → optimize only that |

## What NOT to Do

- Don't recommend the trendy technology by default without justifying it against the real case
- Don't assume future scale/growth not mentioned to justify complexity today (YAGNI)
- Don't give a long, confident answer about a project you know little about — that's the "imagined context" to avoid
- Don't re-ask what was already answered in the conversation or visible in the code

## Verification Checklist

Before closing a decision:

- [ ] Did I understand the real problem, or am I solving the one I assumed?
- [ ] Is the recommendation based on real project data, not a generic case?
- [ ] Did I verify external facts instead of assuming them?
- [ ] Did I mark what is assumption vs. confirmed, and what is fact / estimate / recommendation / opinion?
- [ ] Did I consider "change nothing" as an option?
- [ ] For irreversible decisions: is the reasoning documented (or suggested to be documented)?

## Related Skills

- **engineering-best-practices** — once the approach is decided, that skill guides how to implement it well.
- **graphql-evaluation** — a concrete application of this skill to the "should we use GraphQL?" case.
