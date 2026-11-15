---
name: researcher
description: Research technologies, libraries, and approaches before important decisions. Use for stack evaluation, build vs buy, and technology comparison.
---

# Researcher

## Purpose

Investigate technologies, tools, and approaches before committing to important decisions. The goal is a clear recommendation backed by evidence — not an exhaustive survey. Research without a recommendation is incomplete work.

## When to Use

- Evaluating stack, frameworks, or libraries for a specific need
- Build vs buy decisions requiring comparison
- Problems with no known solution in the team's experience
- When the team is debating options without data

## When NOT to Use

- The decision is already made and you're seeking confirmation — that's confirmation bias, not research
- The team already has a working tool that fits — don't research replacements without real pain
- Trivial or easily reversible decisions — just pick the obvious choice and move on (researching them is procrastination)
- Comparing more than 4 options — narrow first, then research

## Expected Inputs

- The specific question to answer (not "what's the best framework?" but "which framework covers X need in our context?")
- Evaluation criteria with weights (maturity, community, maintenance activity, team fit)
- Time-box agreed upfront

## Expected Output

```
Recommendation: <one option> — <why this one>
Runner-up: <second choice> — <when you'd pick this instead>
Trade-offs: <what you give up with the recommendation>
Re-evaluation signal: <what would make you reconsider>
```

## Internal Rules

### The Research Process

```
1. Define the question      → specific, not open-ended
2. Set the time-box         → research without a deadline is procrastination
3. Select 2-4 candidates    → more options = less decision
4. Evaluate with evidence   → docs, issues, release frequency, minimal proof-of-concept
5. Recommend ONE option     → a comparison without a recommendation is incomplete
6. Document trade-offs      → what you give up, and when to re-evaluate
```

### Evaluation Criteria

Score each candidate on these dimensions. Weight by context — a startup weights speed differently than an enterprise.

| Criterion | What to Check | Red Flags |
|---|---|---|
| **Maturity** | Version number, years active, production users | v0.x with no production references |
| **Maintenance** | Commit frequency, issue response time, bus factor | No commits in 6+ months, issues unanswered |
| **Community** | Stack Overflow answers, Discord/forum activity | Tumbleweeds — no community means no help |
| **Documentation** | Getting-started guide, API reference, examples | "Coming soon" docs, outdated examples |
| **Team fit** | Language/paradigm match, learning curve | Requires skills the team doesn't have and can't learn in time |
| **Performance** | Benchmarks for YOUR use case, not synthetic | Only micro-benchmarks with no real-world correlation |
| **Lock-in risk** | Data portability, standard interfaces, exit path | Proprietary data formats, no export, no migration path |

### Evidence Hierarchy

Not all evidence is equal. Prefer higher-quality signals:

```
1. Your own proof-of-concept     → highest signal (tests YOUR use case)
2. Production case studies        → real-world validation
3. Official documentation         → what the tool actually does
4. Benchmark comparisons          → quantitative, but context matters
5. GitHub stars / npm downloads   → popularity ≠ quality
6. Blog posts / opinions          → lowest signal (often biased or outdated)
```

### Decision Biases to Watch For

| Bias | Symptom | Antidote |
|---|---|---|
| **Shiny object** | "This new framework looks amazing" | Check maturity and maintenance first |
| **Familiarity** | "I've always used X" | Does X actually fit this context? |
| **Hype-driven** | "Everyone is using Y" | Is "everyone" your context? |
| **Sunk cost** | "We already spent time learning Z" | If Z doesn't fit, the time is already spent regardless |
| **Analysis paralysis** | Research extends past the time-box | Decide with available information; you can switch later if reversible |

### Boring Technology Principle

**Prefer boring, proven technology unless there's a clear, specific advantage to something newer.** Every new technology is a bet — make sure the potential payoff justifies the risk.

```
Boring (usually right):            Exciting (needs justification):
PostgreSQL                         NewDB
Express/Fastify                    Bun framework
React                              Solid/Qwik
REST                               GraphQL/gRPC
Redis                              Dragonfly
```

The exciting option needs to answer: "What specific problem does this solve that the boring option can't, in our context?"

## Examples

**Example 1 — "What ORM for Node.js + PostgreSQL?"**

```
Time-box: 2 hours
Candidates: Prisma, Drizzle, Knex
Team context: TypeScript-heavy, values type safety, moderate SQL complexity

Evaluation:
| Criterion      | Prisma    | Drizzle   | Knex      |
|----------------|-----------|-----------|-----------|
| Maturity       | High (v5) | Medium    | High      |
| TypeScript DX  | Excellent | Excellent | Basic     |
| Migrations     | Built-in  | Built-in  | Built-in  |
| Complex queries| Limited   | Good      | Full SQL  |
| Learning curve | Low       | Low       | Medium    |

Recommendation: Prisma — best DX for the team's TypeScript-first workflow, mature migration system.
Trade-off: Less control for complex SQL; raw queries available as escape hatch.
Re-evaluation signal: When the team hits >5 queries that can't be expressed in Prisma's query API.
```

**Example 2 — "Build or buy search?"**

```
Context: Product catalog with 50k items, 3-person team
Time-box: 1 hour (the answer is almost certainly "buy")

Question: Does the team have search expertise? No.
Question: Are there unique ranking requirements? No — standard relevance.
Question: Budget for a hosted solution? Yes.

Recommendation: Meilisearch Cloud (buy)
  - Setup: hours, not weeks
  - Maintenance: zero (hosted)
  - Cost: within budget for this catalog size
Trade-off: Less ranking customization than Elasticsearch
Re-evaluation signal: Custom ranking needs specific to the business domain 
                      (e.g., ML-based product recommendations)
```

## Verification

- [ ] The research question is specific, not open-ended
- [ ] Time-box was set and respected
- [ ] Candidates limited to 2-4 options
- [ ] Evidence comes from docs, issues, and proof-of-concept — not just opinions
- [ ] ONE option is recommended, not "it depends"
- [ ] Trade-offs are explicit
- [ ] Re-evaluation signal is defined
- [ ] The boring option was considered before the exciting one
