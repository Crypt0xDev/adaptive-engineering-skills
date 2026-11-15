# Code Quality & Security Rules

Mandatory rules when writing or modifying code. Unlike architecture patterns (which depend on context), these rules apply **always**, at any project stage.

---

## What Code Must NEVER Have

### Duplicated Code
- Before writing, check if the logic already exists in the project and reuse it.
- If logic repeats 3 times, extract it (rule of three, skill `engineering-best-practices` → `references/principles.md`).
- Don't copy-paste blocks: extract a shared function or module.

### Non-descriptive Names
- Forbidden: `data`, `temp`, `x`, `aux`, `doStuff`, cryptic abbreviations.
- Variables and functions named by business intent: `calculateTotalWithTaxes()`, not `calc()`.
- Booleans as questions: `isActive`, `hasPermission`.

### Overly Large Functions
- One function = one responsibility. If it needs "and" to describe itself, split it.
- Guideline: if it doesn't fit on one screen (~30-40 lines) or has more than 3 nesting levels, refactor.
- Maximum 3-4 parameters; more than that, group into an object.

### Excessive Coupling
- Modules communicate through clear interfaces/contracts, not by touching each other's internals.
- No shared mutable global variables.
- Dependencies in one direction only; no cycles between modules.

### Lack of Comments and Documentation
- Comment the **why** (decisions, constraints, trade-offs), clean code already says the what.
- Every public/exported function with a brief docstring: what it does, parameters, return.
- Project README updated: how to install, configure, and run.

---

## What Code Must ALWAYS Maintain

### Maintainability
- Clean code consistent with the project's style.
- A new dev should understand any module in minutes.

### User Validation Security
- Validate identity on the server, never trust the client alone.
- Authorization verified per resource on every operation (not just "is logged in").

### Secure Passwords
- Require minimum policy (length ≥ 8-12, no common passwords).
- Never log passwords or return them in responses.

### Parameterized Queries
- Every query with placeholders/prepared statements or ORM.
- **Forbidden** to concatenate or interpolate user input in SQL.

### Data Escaping and Sanitization
- Validate and sanitize all input at the system boundary (type, format, length, range).
- Escape output per context (HTML, SQL, shell, URL) to prevent XSS and injections.

### Proper Session Management
- Tokens/cookies with expiration; cookies `HttpOnly`, `Secure`, `SameSite`.
- Regenerate session ID on login; invalidate on logout and password change.

### Secure Password Storage
- Hashing with bcrypt / argon2 / scrypt (with automatic salt).
- **Forbidden**: plaintext, MD5, SHA1/SHA256 without key-stretching, reversible encryption.

### Least Privilege
- DB users, API keys, and roles with only the permissions they need.
- Endpoints and admin routes restricted by role, not hidden by obscurity.

### Updated Dependencies
- Check vulnerabilities when adding dependencies (`npm audit`, `pip-audit` or equivalent).
- Prefer maintained and popular dependencies; avoid abandoned packages.
- Versions pinned in lockfile.

### Error Handling Without Exposing Sensitive Information
- To the user: generic message ("An error occurred, please try again").
- To internal logs: full detail (stack trace, context) — without passwords or tokens.
- Never expose stack traces, internal paths, versions, or SQL in production responses.

---

## Good Programming Practices

| Correct | Incorrect |
|---------|-----------|
| One function does one thing | Functions that do too many things |
| Clear, short, descriptive names | Confusing or overly long names |
| Useful and necessary parameters | Unnecessary or "just in case" parameters |
| Easy-to-test code (injected dependencies, no hidden state) | Hard-to-test code (globals, Singletons, hidden effects) |
| Context-based architecture | Applying patterns without real need |

## Architecture and Patterns by Context

> Architecture (microservices, OOP, patterns like Singleton) is applied **only when the context justifies it**, not as a fixed rule.

Detailed criteria in other plugin skills:

- **Microservices** → skill `software-architect` → `references/microservices.md`: when to separate into two or more services (proven domain boundary + independent scaling + independent teams), and when not (MVP, small team, cargo cult).
- **OOP, polymorphism and entity relationships** → skill `engineering-best-practices` → `references/oop-and-patterns.md`: OOP when there are entities with state and invariants; polymorphism with 2+ real implementations; every relationship justified by a real use case.
- **Singleton** → same file: only when the system genuinely requires a single instance (connection pool, config, logger), and even then prefer dependency injection over global access.
- **DB modeling and normalization** → skill `database-architect` → `references/data-modeling.md`: 3NF by default, integrity in the DB, denormalize only with measurement and documentation.

---

## How It's Applied

1. **When writing code**: these rules are met from the first draft, not "later".
2. **When reviewing**: skill `code-reviewer` and `references/checklist-code-review.md` verify each point.
3. **As the project advances**: architecture scales by context (skill `software-architect`), but these rules are constant at every stage.
