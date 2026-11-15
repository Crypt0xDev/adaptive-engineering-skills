---
name: test-engineer
description: Design test strategies proportional to the project's risk. Use when defining what to test, how to test it, and when to stop testing.
---

# Test Engineer

## Purpose

Design test strategies proportional to the project's risk and stage. Testing is not about 100% coverage — it's about catching the defects that matter before users find them. Every test must justify its existence by protecting against a real failure mode.

## When to Use

- Writing new code with business logic, calculations, permissions, or money/data handling
- Defining the test strategy for a project (which layers, which tools, what runs in CI)
- After a bug is fixed — the reproducing test comes FIRST, before the fix
- Before refactoring — ensuring the current behavior is covered
- When tests are slow, flaky, or failing intermittently

## When NOT to Use

- Prototypes or throwaway spikes (but if they're integrated, they get tests)
- Chasing a coverage percentage — coverage is an indicator, not a goal
- Trivial code with no logic (getters, wiring, declarative configuration)
- Reviewing general code quality (that's `code-reviewer`) or measuring performance (that's `performance-engineer`)

## Expected Inputs

- The code or feature to cover and what happens if it fails (real impact)
- Project stage (MVP, production, legacy with no tests)
- Stack and existing test tools — respect them before proposing others

## Expected Output

```
Test strategy:
  Critical paths: <what MUST be tested>
  Test types: <unit, integration, e2e — and WHY each>
  Not testing: <what's excluded and why>
```

## Internal Rules

### The Testing Pyramid (Proportional, Not Dogmatic)

```
        /  E2E  \        Few: critical user journeys only
       /----------\
      / Integration \    Some: component boundaries, API contracts
     /----------------\
    /    Unit Tests     \  Many: business logic, pure functions, edge cases
   /--------------------\
```

The pyramid is a guideline, not a rule. Some projects need more integration tests than unit tests. Match the strategy to where the risk is.

### What to Test (Risk-Based Prioritization)

| Priority | What to Test | Why | Test Type |
|---|---|---|---|
| **P0** | Money/data calculations | Errors cost real money | Unit |
| **P0** | Authentication/authorization | Security breach if wrong | Integration |
| **P0** | Data persistence (write paths) | Data loss is irreversible | Integration |
| **P1** | Critical user journeys | Revenue-impacting flows | E2E |
| **P1** | Edge cases in business logic | The bugs users actually hit | Unit |
| **P1** | API contracts | Breaking changes break clients | Integration/Contract |
| **P2** | Error handling paths | Graceful degradation | Unit/Integration |
| **P2** | Concurrent operations | Race conditions are hard to debug | Integration |
| **P3** | UI rendering | Visual regressions | Snapshot/Visual |

### What NOT to Test

| Skip This | Why | What to Do Instead |
|---|---|---|
| Framework behavior | Already tested by the framework | Trust it; test YOUR logic |
| Trivial code (getters, constructors) | No logic to break | Nothing |
| Private methods directly | Test through the public interface | Test behavior, not implementation |
| External services in unit tests | Unreliable, slow, costly | Mock at the boundary; integration test separately |
| Configuration/constants | No logic | Code review is enough |

### How to Write Tests

- **Behavior, not implementation:** the test doesn't break if you refactor without changing the result.
- **One failure reason per test**, with a name that describes the case (`rejects_order_when_out_of_stock`).
- **Deterministic:** no dependency on time, order, network, or shared state between tests.
- **Mocks only at boundaries** (network, clock, external services); never mock the code under test.
- **Fast:** the unit suite runs in seconds; slow tests go to a separate CI stage.

### Proportional to Stage

| Stage | Test Strategy |
|---|---|
| **MVP** | Tests for critical logic and the main flow. Nothing more. |
| **Production** | + regression tests for every bug, integration tests at critical points |
| **Legacy (no tests)** | Characterization tests on code you're about to touch. Don't try to cover everything. |

### Never

- Delete or disable a failing test to make CI pass without understanding why it fails.
- Write tests that only verify a mock was called, without verifying the result.
- Accept flaky tests — a test that passes 99% of the time trains the team to ignore failures.

## Examples

**Example 1 — Coupon discount function in an e-commerce:**

```
Context: Function that calculates coupon discounts. Risk: HIGH (money).

Tests (unit, no mocks needed):
  1. valid_coupon_applies_percentage_discount
  2. expired_coupon_returns_zero_discount
  3. minimum_amount_not_reached_rejects_coupon
  4. discount_greater_than_total_caps_at_total

Result: 4 fast tests covering the business rules.
NOT testing: UI rendering of the coupon field (separate concern).
```

**Example 2 — "Add tests to the whole project, it has 0% coverage":**

```
Approach: Do NOT try to cover everything.

Step 1: Identify the 2-3 modules with the most changes and bugs (git log + bug tracker)
Step 2: Write characterization tests for those modules (capture current behavior)
Step 3: Add the test job to CI (fail the build on test failures)
Step 4: From now on, every bug fix and new feature in those modules comes with tests

Result: Protection where it hurts, in hours instead of weeks.
Coverage target: none. Coverage will grow organically as the riskiest code gets tested.
```

## Verification

- [ ] Test strategy is proportional to risk (P0 paths tested first)
- [ ] Tests verify behavior and outcomes, not implementation details
- [ ] Each test is deterministic (no flaky tests accepted)
- [ ] Test names describe the scenario and expected result
- [ ] Mocks only at boundaries (network, external services), never on code under test
- [ ] No tests for trivial code, framework behavior, or third-party libraries
- [ ] Critical paths (money, auth, data) have explicit test coverage
