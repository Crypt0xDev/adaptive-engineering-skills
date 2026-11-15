---
name: code-reviewer
description: Systematic code review focused on correctness, security, and maintainability. Use when reviewing PRs, auditing code quality, or before merging.
---

# Code Reviewer

## Purpose

Review code systematically for correctness, security, and maintainability — in that order. A code review is not about style preferences; it's about catching defects before they reach production and ensuring the code is understandable by the next person who reads it.

## When to Use

- Reviewing pull requests before merge
- Auditing existing code for quality issues
- After a bug is found — reviewing the surrounding code for similar patterns
- Self-verifying all generated code before delivering it

## When NOT to Use

- Reviewing generated code that will be regenerated (migrations output, protobuf, lock files)
- Style-only nitpicks when a linter/formatter already enforces style
- Blocking a PR over subjective preferences — review for defects, not taste
- Architecture decisions — that's `software-architect`; review the implementation, not the design (unless the design is clearly wrong)

## Expected Inputs

- The code to review (diff, PR, or file)
- Context: what the change is supposed to do
- The project's conventions (if known)

## Expected Output

```
[CRITICAL] <file:line> — <defect description>
[WARNING]  <file:line> — <potential issue>
[SUGGESTION] <file:line> — <improvement opportunity>

Summary: <overall assessment and recommendation>
Verdict: APPROVE | REQUEST_CHANGES | DISCUSS
```

## Internal Rules

### Review Priority Order

Always review in this order. Stop at the first category with findings before moving to the next:

```
1. CORRECTNESS  → Does it do what it's supposed to do? Are there bugs?
2. SECURITY     → Does it introduce vulnerabilities? (see security-engineer)
3. DATA         → Can it corrupt or lose data? Are migrations safe?
4. PERFORMANCE  → Will it degrade under load? (only when measurable)
5. MAINTAINABILITY → Can the next person understand and modify it?
```

### The Review Checklist

| Category | Check | Red Flag |
|---|---|---|
| **Correctness** | Edge cases handled? | Happy path only, no nil/empty/boundary checks |
| **Correctness** | Error paths correct? | Errors swallowed, wrong error type, missing cleanup |
| **Correctness** | Concurrency safe? | Shared mutable state without synchronization |
| **Correctness** | Off-by-one errors? | `<` vs `<=`, array bounds, pagination boundaries |
| **Security** | Input validated? | User input reaches DB/shell/HTML unvalidated |
| **Security** | Authorization checked? | Checks authentication but not authorization (IDOR) |
| **Security** | Secrets exposed? | API keys, passwords, tokens in code or logs |
| **Data** | Migration reversible? | Destructive migration with no rollback path |
| **Data** | Race conditions? | Read-then-write without transactions or locks |
| **Data** | Null handling? | Nullable field accessed without null check |
| **Performance** | N+1 queries? | Loop with a query inside (ORM or raw SQL) |
| **Performance** | Unbounded results? | Query without LIMIT on a growing table |
| **Maintainability** | Single responsibility? | Function does multiple unrelated things |
| **Maintainability** | Naming clear? | Abbreviations, misleading names, generic `data`/`info` |
| **Maintainability** | Tests cover the change? | New logic without corresponding tests |

### What NOT to Comment On

These are NOT review findings — they waste everyone's time:

| Not a Finding | Why | What to Do Instead |
|---|---|---|
| Style preferences | Linters enforce style | Configure a linter |
| "I would have done it differently" | Not a defect | Let it go unless it's clearly worse |
| Trivial naming suggestions | Subjective | Only flag if genuinely misleading |
| Missing features not in scope | Scope creep | File a separate issue |
| "Add more comments" | Comments rot | Only if the code is genuinely incomprehensible |

### How to Write Review Comments

**Bad comments** (vague, unhelpful):
```
"This could be improved"
"Not sure about this"
"Consider refactoring"
```

**Good comments** (specific, actionable):
```
"[CRITICAL] This query is vulnerable to SQL injection. 
 Line 42: userId comes from req.params and is concatenated into the query.
 Fix: Use parameterized query: db.query('SELECT * FROM users WHERE id = $1', [userId])"

"[WARNING] This will throw on null — user.address is nullable in the schema
 but accessed without a null check on line 67.
 Fix: Add optional chaining: user.address?.city"
```

### Severity Levels

| Level | Meaning | Action |
|---|---|---|
| **CRITICAL** | Bug, security vulnerability, data loss risk | Must fix before merge |
| **WARNING** | Likely to cause issues in specific conditions | Should fix, discuss if disagreement |
| **SUGGESTION** | Improvement opportunity, not a defect | Optional, author decides |

## Examples

**Example 1 — Reviewing an API endpoint:**

```
[CRITICAL] auth_middleware.js:34 — Authorization bypass
  The middleware checks req.user exists (authentication) but the endpoint 
  at routes/invoices.js:12 doesn't verify the invoice belongs to req.user.
  Any authenticated user can read any invoice.
  Fix: Add WHERE user_id = req.user.id to the query.

[WARNING] routes/invoices.js:28 — Unbounded query
  GET /invoices returns all invoices with no pagination.
  Will degrade as data grows.
  Fix: Add LIMIT/OFFSET or cursor pagination.

[SUGGESTION] routes/invoices.js:15 — Consider extracting validation
  The validation logic (lines 15-28) could move to a middleware for reuse.

Summary: Critical authorization bug must be fixed. Otherwise clean implementation.
Verdict: REQUEST_CHANGES
```

**Example 2 — Reviewing a database migration:**

```
[CRITICAL] migration_042.sql:8 — Destructive column removal
  DROP COLUMN email_verified removes data with no rollback path.
  If any downstream service reads this column, it will break silently.
  Fix: 1) Verify no code reads this column, 2) Add a reverse migration,
       3) Consider a two-phase approach: deprecate first, remove next release.

[WARNING] migration_042.sql:3 — NOT NULL on existing column without default
  ALTER TABLE users ADD COLUMN role VARCHAR NOT NULL will fail if the table 
  has existing rows (no default value provided).
  Fix: Add DEFAULT 'user' or backfill in the same migration.

Summary: Migration has a destructive operation and will fail on existing data.
Verdict: REQUEST_CHANGES
```

## Verification

After completing a review:

- [ ] All findings have a severity level (CRITICAL/WARNING/SUGGESTION)
- [ ] All findings reference specific file and line
- [ ] All findings include a concrete fix suggestion
- [ ] No style-only nitpicks (unless genuinely harmful)
- [ ] Review covers correctness and security before maintainability
- [ ] Verdict is clear: APPROVE, REQUEST_CHANGES, or DISCUSS

## References (load only when needed)

Paths relative to this skill's folder:

- `references/code-quality.md` — mandatory quality and security rules
- `references/checklist-code-review.md` — review checklist
