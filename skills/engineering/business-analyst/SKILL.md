---
name: business-analyst
description: Translate business needs into clear, verifiable requirements. Use when requirements are ambiguous, contradictory, or during initial discovery.
---

# Business Analyst

## Purpose

Translate business needs into clear, verifiable requirements. The goal is to close the gap between what stakeholders ask for (their assumed solution) and what they actually need (the underlying problem). Every requirement must be testable — if you can't verify it's done, it's not a requirement.

## When to Use

- Starting a project (requirements discovery and elicitation)
- Requirements are ambiguous, contradictory, or incomplete
- Scope changes are requested mid-project
- Validating that a deliverable meets what was actually asked for
- Stakeholders disagree on what the system should do

## When NOT to Use

- Prioritizing what to build first — that's `product-manager`
- Deciding how to implement — that's `software-architect`
- Personal projects or single-stakeholder prototypes where the requirement is obvious — formalizing would be bureaucracy
- The requirements are already clear, documented, and agreed upon — don't re-elicit

## Expected Inputs

- Access to stakeholders or their written requests
- Business context (current processes, existing systems, pain points)
- Constraints (regulatory, timeline, budget)

## Expected Output

```
Requirements: <prioritized list>
For each requirement:
  - User story: As <who> I want <what> so that <why>
  - Acceptance criteria: <measurable conditions>
  - Assumptions: <what we're taking for granted>
  - Risks: <what could go wrong>
```

## Internal Rules

### The Elicitation Process

```
1. Listen to the request     → what the stakeholder asks for (their solution)
2. Ask "why?" repeatedly     → dig to the root business problem
3. Separate need from want   → the NEED is the problem; the WANT is the assumed solution
4. Write verifiable stories  → "As X I want Y so that Z" with acceptance criteria
5. Detect gaps and conflicts → before building, not during
6. Get explicit sign-off     → ambiguity resolved, contradictions decided
```

### Core Principles

1. **Ask "why?" until you reach the business problem.** The first request is almost never the real requirement.

   | What they say | Why? | Real requirement |
   |---|---|---|
   | "Add an export to Excel button" | "Accounting re-creates the report manually each month" | Automated monthly report delivery |
   | "We need a mobile app" | "Field workers can't access the system" | Field-accessible interface (could be responsive web) |
   | "Make the dashboard real-time" | "We miss critical alerts" | Alert system with notifications (dashboard refresh rate is irrelevant) |

2. **A requirement without acceptance criteria is incomplete.** If you can't test it, you can't build it.

   ```
   BAD:  "The system should be fast"
   GOOD: "Search results load in under 500ms at p95 with 10k concurrent users"
   
   BAD:  "Easy to use"
   GOOD: "A new user completes their first order without help documentation in under 3 minutes"
   ```

3. **Detect contradictions BEFORE building.** When two stakeholders want conflicting things, escalate with the impact of each option — don't silently pick one.

4. **Distinguish business rules from implementation details.** "Discounts cannot exceed 50% of the order total" is a business rule (belongs in requirements). "Use a microservice for discounts" is an implementation detail (belongs in architecture).

5. **Document assumptions explicitly.** Every assumption is a risk. "We assume the payment provider's API has 99.9% uptime" — if wrong, the plan changes.

### Requirements Classification

| Type | Example | Who Owns It |
|------|---------|-------------|
| Functional | "Users can reset their password via email" | Business + UX |
| Non-functional | "Page load under 2s at p95" | Engineering + Business |
| Business rule | "Orders over $10k require manager approval" | Business |
| Constraint | "Must run on AWS due to existing contract" | Business + Ops |
| Assumption | "Users have stable internet" | Risk register |

### Common Failure Modes

| Failure | Consequence | Prevention |
|---------|------------|------------|
| Building the first request without asking why | Solving the wrong problem | Always dig to the root need |
| Vague acceptance criteria | "Is it done?" becomes a debate | Every criterion is measurable |
| Undocumented assumptions | Surprises during development | Write them down, review with stakeholders |
| Missing negative requirements | "What should it NOT do?" is undefined | Explicitly document out-of-scope items |
| Stakeholder says "you decide" | Blame when it's wrong | Get explicit sign-off on every decision |

## Examples

**Example 1 — The "Export to Excel" request:**

Stakeholder says: "We need an 'Export to Excel' button on the sales page."

```
Why? → "Accounting re-creates the sales report manually every month."
Why manually? → "They copy data from the screen into their spreadsheet template."
Real need → Automated monthly report in accounting's format.

Requirement: Automated monthly sales report
  Story: As accounting, I want the monthly sales report delivered automatically 
         so that I don't spend 4 hours recreating it manually.
  Acceptance criteria:
    - Report delivered by email on the 1st of each month by 8am
    - Format matches accounting's existing template
    - Includes all closed orders from the previous month
  Assumptions: Email delivery is acceptable (vs. direct ERP integration)
  Risk: If accounting's template changes, the report format needs updating
```

**Example 2 — Contradictory discount rules:**

Manager A: "All loyalty customers get 20% off."
Manager B: "No discounts on premium products."

```
Conflict: What happens when a loyalty customer buys a premium product?

Options documented with impact:
  A) Loyalty wins → 20% off premium products (margin impact: -$X/month)
  B) Premium wins → No discount on premium (customer satisfaction risk)
  C) Partial → 10% on premium for loyalty (compromise)

Action: Escalated to both managers with impact analysis.
Decision: Option B, documented with sign-off from both managers.
```

## Verification

Before marking requirements as complete:

- [ ] Every requirement has measurable acceptance criteria
- [ ] "Why?" has been asked until the root business problem is clear
- [ ] Contradictions between stakeholders are resolved and documented
- [ ] Assumptions are listed explicitly
- [ ] Out-of-scope items are documented (what the system will NOT do)
- [ ] Stakeholder sign-off is recorded
- [ ] Requirements are prioritized (by `product-manager` or jointly)
