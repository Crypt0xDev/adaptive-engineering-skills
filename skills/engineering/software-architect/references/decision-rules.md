# Decision Framework

## Step 1 — Context First
Before proposing any solution, answer:
1. What business problem does it solve?
2. How many users / what real load (not projected)?
3. What size and experience does the team have?
4. What is the project's expected lifespan?
5. Stage: idea, MVP, production, or legacy?

## Step 2 — Complexity Ladder
Always start at the lowest level that works:

| Level | When |
|-------|------|
| Script / function | One-off task, no state |
| Simple monolith | MVP, small team, uncertain domain |
| Modular monolith | Clear domain, growing team |
| Separate services | Proven domain boundaries + real need for independent scaling |

Move up only with evidence (real pain, not anticipated).

## Step 3 — Patterns on Demand
A pattern is applied only if:
- The problem it solves already exists in the project, and
- The cost of not applying it is greater than the cost of applying it.

## Step 4 — Reversible vs Irreversible
- **Reversible** (names, internal structure): decide quickly.
- **Irreversible** (database, public API, contracts): analyze more and document as ADR in the project repo.

## Step 5 — Format for Every Decision

```
Decision: <what was chosen>
Reason: <1-3 sentences tied to context>
What we WON'T do and why: <list>
Signals to evolve: <what pain would justify the next level>
```
