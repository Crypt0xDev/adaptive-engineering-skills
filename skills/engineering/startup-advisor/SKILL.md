---
name: startup-advisor
description: Technical and product decisions for startups — speed and validation over perfection. Use for MVP planning, build vs buy, and acceptable tech debt.
---

# Startup Advisor

## Purpose

Guide technical and product decisions in a startup context where speed and validation matter more than perfection. The goal is to learn whether the business hypothesis is true before investing in engineering. Every decision is filtered through: "Does this help us validate faster?"

## When to Use

- Projects in idea/MVP stage with limited resources
- Build vs buy decisions
- Time-to-market pressure forcing trade-off choices
- Evaluating which technical debt is acceptable to take on
- When the team is over-engineering before product-market fit

## When NOT to Use

- Production systems at scale or enterprise contexts — those need rigor over speed
- To justify skipping the security minimums from `code-reviewer` — those are non-negotiable at every stage
- Irreversible decisions (database schema, public API contracts) — shortcuts don't apply there; use `software-architect`
- Post-product-market-fit: once you know what works, invest in doing it well

## Expected Inputs

- The business hypothesis to validate
- Available resources (time, money, team)
- Which parts are the core differentiator and which are commodity

## Expected Output

```
Recommendation: <minimum viable approach>
Acceptable shortcuts: <reversible trade-offs taken>
Documented debt: <what we're knowingly skipping>
Payoff signal: <measurable trigger to pay the debt>
```

## Internal Rules

### The Validation-First Framework

```
1. Identify the riskiest hypothesis     → "Will users pay for X?"
2. Find the cheapest way to test it     → Could be a landing page, not an app
3. Build only what the test requires    → Everything else is waste
4. Measure the result                   → Did the hypothesis hold?
5. Then decide what to build properly   → Now you know what matters
```

### Build vs Buy Decision Matrix

| Question | Build | Buy/Use SaaS |
|---|---|---|
| Is this your core differentiator? | Yes → build it | No → buy it |
| Does a good enough solution exist? | No → build it | Yes → use it |
| Can your team maintain it? | Yes and worth the cost | No → buy it |
| Time to market critical? | Only if faster to build | Almost always faster to buy |

**Default: buy everything that isn't your core business.** Stripe for payments, Auth0 for auth, SendGrid for email, Vercel for hosting. Build your differentiator, buy the plumbing.

### Acceptable vs Unacceptable Shortcuts

| Acceptable (Reversible) | Unacceptable (Non-Negotiable) |
|---|---|
| Manual processes instead of automation | Skipping input validation |
| Hardcoded config instead of admin panel | Storing passwords in plain text |
| Single-tenant architecture | No HTTPS |
| No CI/CD (deploy manually) | SQL injection vulnerabilities |
| Monolith instead of microservices | Secrets committed to the repo |
| No monitoring (check logs manually) | No backups of user data |
| Simple UI (functional, not polished) | Ignoring authentication on sensitive endpoints |

### Tech Debt Rules

1. **Conscious debt is acceptable; invisible debt is not.** Every shortcut is documented with its payoff signal.

   ```
   Debt: Using SQLite instead of PostgreSQL
   Why: Faster to set up for the prototype
   Payoff signal: >100 concurrent users OR need for concurrent writes
   Owner: @backend-lead
   ```

2. **Debt without a payoff signal is not debt — it's negligence.**

3. **Things that don't scale are fine until there's something to scale.** Doing things manually (sending emails, onboarding users) is a feature at the startup stage — it builds customer understanding.

4. **The best code is code you didn't write.** Every line of code is a liability. Fewer lines = less to maintain, less to break, less to understand.

### Common Startup Anti-Patterns

| Anti-Pattern | Reality Check |
|---|---|
| "Let's build microservices from day one" | You have 0 users. Ship a monolith this week. |
| "We need our own auth system" | No you don't. Use a provider. Build your product. |
| "Let's set up Kubernetes" | For what load? Railway/Vercel deploys in 5 minutes. |
| "We need 100% test coverage" | You need to know if anyone wants this. Test the critical path. |
| "Let's write our own framework" | Your framework is not your product. Use what exists. |
| "We should plan the architecture for 3 years" | You might pivot in 3 months. Plan for 3 months. |

## Examples

**Example 1 — Founder wants to build a subscription system:**

```
Question: Is subscription management your core differentiator?
Answer: No — the core is the content/service being sold.

Recommendation: Stripe Billing
Documented debt: "We depend on Stripe's pricing and API"
Payoff signal: When Stripe's commission exceeds the cost of building + maintaining in-house
               (typically >$500k/year in billing volume)
```

**Example 2 — Team wants microservices before having users:**

```
Context: Zero users, unvalidated hypothesis, 3-person team.

Recommendation: Monolith on PaaS, deployed this week.
  - Next.js + PostgreSQL on Railway
  - Manual deploys (git push)
  - Sentry for error tracking (free tier)
  - No CI/CD, no Docker, no Kubernetes
  
Documented debt: 
  - No automated testing → payoff signal: first paying customer
  - No CI/CD → payoff signal: team >3 or deploys >2/day
  - Manual email sending → payoff signal: >50 emails/week
```

**Example 3 — "Should we refactor before launching?":**

```
Question: Does the current code work? Can users complete the core flow?
Answer: Yes, but it's messy.

Recommendation: Launch now. Refactor after validation.
  - Messy code that validates a hypothesis > clean code that validates nothing
  - If users don't want this, the code gets deleted anyway
  - If users DO want this, you'll have revenue to fund the refactor
```

## Verification

- [ ] The riskiest business hypothesis is identified
- [ ] The build plan tests that hypothesis with minimum engineering
- [ ] Build vs buy decisions favor buying for non-core functionality
- [ ] Every shortcut is documented with a measurable payoff signal
- [ ] Security non-negotiables are respected regardless of stage
- [ ] Irreversible decisions received proper investment (no shortcuts)
- [ ] The team can ship within days/weeks, not months
