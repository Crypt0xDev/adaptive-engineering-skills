# Checklist: Code Review

## Simplicity
- [ ] Is there a simpler solution that does the same thing?
- [ ] Are there abstractions with a single unjustified implementation?
- [ ] Is there code for hypothetical futures? (YAGNI)

## Correctness
- [ ] Are edge cases in the main flow covered?
- [ ] Are errors handled where they can be acted upon?
- [ ] Tests for value behavior (not implementation)?

## Maintainability (references/code-quality.md)
- [ ] No duplicated code? (reuse existing; extract on the third repetition)
- [ ] Descriptive names by business intent? (no `data`, `temp`, `doStuff`)
- [ ] Small functions with a single responsibility? (~30-40 lines, ≤3 nesting levels)
- [ ] Low coupling? (communication via contracts, no mutable globals, no cycles)
- [ ] Documented? (comments on the why, docstrings on public functions)
- [ ] Can a new dev understand it in 10 minutes?
- [ ] Consistent with surrounding code style?

## Security (references/code-quality.md)
- [ ] Server-side user validation and per-resource authorization?
- [ ] Passwords with minimum policy and hashed with bcrypt/argon2?
- [ ] Parameterized queries on all data access?
- [ ] Inputs validated/sanitized and outputs escaped per context?
- [ ] Sessions with expiration, HttpOnly/Secure/SameSite cookies, invalidation on logout?
- [ ] Least privilege on DB, API keys, and admin routes?
- [ ] Dependencies audited and pinned in lockfile?
- [ ] Errors without exposing stack traces, internal paths, or SQL to the user?
- [ ] Secrets out of the code (environment variables)?

## Verdict
Classify each finding as **Blocker** / **Important** / **Suggestion**, always proposing the alternative.
