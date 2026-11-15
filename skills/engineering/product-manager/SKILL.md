---
name: product-manager
description: Define what to build and in what order to maximize business value per effort. Use for scoping, MVP definition, and backlog prioritization.
---

# Product Manager

## Purpose

Define what to build and in what order, maximizing business value per unit of effort. The goal is to ship the smallest thing that validates the riskiest assumption, learn from it, and iterate. Everything else waits.

## When to Use

- Defining the scope of a project or feature
- Prioritizing a backlog with competing items
- Deciding what goes into the MVP and what doesn't
- Resolving conflicts between features competing for resources
- When the team is building things nobody asked for

## When NOT to Use

- Technical implementation decisions — that's `software-architect`
- Detailed requirements elicitation — that's `business-analyst` (this skill prioritizes what they elicit)
- When scope is already signed off and no new information has emerged — don't reopen priorities without cause
- Personal projects with no stakeholders — just build what you want

## Expected Inputs

- The user's problem and the business objective
- List of candidate features or requirements
- Constraints: time, team size, budget
- Any existing data on user behavior or market validation

## Expected Output

```
MVP scope: <what's in and why>
Cut list: <what's out and why>
Success metrics: <how we'll know it worked>
Priority order: <sequence with rationale>
```

## Internal Rules

### The Prioritization Framework

Every feature must answer these questions before it earns a place in the build:

```
1. What problem does this solve?        → Must be specific and real
2. For whom?                             → Must be a defined user segment
3. How will we know it worked?           → Must have a measurable metric
4. What's the smallest version?          → Must be buildable in days, not months
5. What happens if we don't build it?    → If nothing, cut it
```

### Value/Effort Matrix

Prioritize systematically, not by who shouts loudest:

| | Low Effort | High Effort |
|---|---|---|
| **High Value** | **Do first** — quick wins | **Plan carefully** — worth it but invest wisely |
| **Low Value** | **Maybe later** — easy but not important | **Cut** — expensive and unimportant |

### MVP Definition Rules

1. **The MVP validates one hypothesis.** The riskiest assumption gets tested first.

   ```
   BAD MVP:  "Full app with chat, payments, gamification, and social features"
   GOOD MVP: "Can users complete a purchase?" → payment flow only
   ```

2. **"Nice to have" means "not in MVP."** If removing it doesn't invalidate the hypothesis, it's out.

3. **Success metrics are defined BEFORE building.** If you can't measure success, you can't validate the hypothesis.

   | Hypothesis | Metric | Target |
   |---|---|---|
   | "People will pay for X" | Conversion rate | >2% of visitors complete purchase |
   | "Teams need collaboration" | Weekly active users | >30% return in week 2 |
   | "Automation saves time" | Task completion time | 50% reduction vs manual |

4. **Scope creep is the default.** Actively resist it. Every addition must re-justify itself against the hypothesis.

### Saying No

The product manager's most important skill is saying no with a reason:

| Request | Response |
|---|---|
| "Can we also add X?" | "How does X validate our current hypothesis? If it doesn't, it goes to the backlog with a note." |
| "The competitor has Y" | "Do our users need Y? What data says so?" |
| "It would be cool to have Z" | "Cool doesn't ship. What problem does Z solve for which users?" |
| "The CEO wants it" | "Understood. What does it displace in the current priority? Let's make the trade-off explicit." |

### Backlog Hygiene

- Items without a clear problem statement get sent back for clarification
- Items older than 3 months without movement get reviewed: still relevant, or cut?
- No item enters the backlog without: problem, user, and rough value/effort estimate
- The backlog is a prioritized list, not a wish list — if everything is P1, nothing is

## Examples

**Example 1 — Client wants an app with everything:**

Request: App with chat, payments, gamification, social features, and analytics dashboard.

```
Hypothesis: "Users will pay for the core service."
MVP: Payment flow for the core service. Nothing else.
Cut list:
  - Chat → not needed to validate payment willingness
  - Gamification → engagement optimization, not validation
  - Social features → network effects come after core value is proven
  - Analytics dashboard → internal tool, build when there's data to analyze
Success metric: >2% of visitors complete a purchase in the first month
```

**Example 2 — Unordered backlog of 30 items:**

```
Step 1: Value/effort estimation with the team (2-hour session, not 2-week process)
Step 2: Place each item in the matrix

Result:
  Do first (5 items): High value, low effort — ship this sprint
  Plan carefully (4 items): High value, high effort — needs breakdown
  Maybe later (13 items): Low value, low effort — backlog with review date
  Cut (8 items): Low value, high effort — removed with documented reason
```

## Verification

Before committing to a scope:

- [ ] Every feature in scope answers "what problem, for whom, how do we measure"
- [ ] The MVP tests exactly one hypothesis — the riskiest one
- [ ] Success metrics are defined and measurable
- [ ] The cut list is explicit — stakeholders know what's out and why
- [ ] No feature was added because "it would be nice" without a problem statement
- [ ] Priority order reflects value/effort, not stakeholder volume
