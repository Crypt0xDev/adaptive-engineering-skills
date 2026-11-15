---
name: buenas-practicas-ingenieria
description: "Applies software engineering best practices (SOLID, maintainable folder structure, separation of concerns, scalability, naming, security) with judgment on any coding task in any language. Use ALWAYS when writing, reviewing, or structuring code, adding features, or discussing architecture and organization. Evaluates whether the project warrants a given structure before imposing it, respects existing conventions, and prioritizes long-term maintainability without over-engineering."
---

# Engineering Best Practices (With Judgment)

## Purpose

Apply software engineering best practices — SOLID principles, clean structure, separation of concerns, scalability, naming, and security — with judgment proportional to the project's size and stage. The goal is not pattern compliance; it's code that can be read, modified, and grown without breaking.

## When to Use

- Writing, reviewing, or structuring any new code
- Adding a feature to an existing project
- Discussing architecture, folder organization, or code conventions
- Any coding task in any language — backend, frontend, scripts, firmware

## When NOT to Use

- As a checklist to blindly impose SOLID on a 50-line script
- To override project conventions with personal preferences
- When the task is purely about choosing *which* technology (that's `decisiones-tecnicas-fundamentadas`); this skill covers *how* to implement it well

## The Process

### Step 0: Check Existing Conventions (Always First)

Before proposing structure or refactoring, examine how the project is already organized:

```
BEFORE ANY STRUCTURAL CHANGE, ANSWER:
→ What folder structure, layers, and naming does this project use?
→ Is there a linter/formatter configured (Prettier, Black, ESLint, Ruff)?
→ Is the existing pattern consistent?
→ Does changing it solve a real problem or just satisfy a preference?
```

If a consistent pattern exists, follow it. Flag an inconsistency only if it causes real maintainability issues, and as a suggestion — not an unsolicited rewrite.

### Step 1: Verify Before Asserting

Never fabricate APIs, method signatures, flags, or library versions. When in doubt about how a library or framework works:

| Action | Do | Don't |
|--------|----|-------|
| Check API compatibility | Read official docs | Trust blog posts or memory |
| Reference a library feature | Verify the version supports it | Assume the latest version |
| Suggest a pattern | Confirm the framework supports it | Invent a method name |
| Can't verify | Say so explicitly | Fill the gap with a confident guess |

**Official documentation > blog posts > memory > guessing.**

### Step 2: Decide the Right Level of Structure

Not every project needs layers, interfaces, or dependency injection. Match structure to the project's actual complexity:

**When to apply stricter SOLID / layered architecture:**

| Signal | Why |
|--------|-----|
| Backend with 3+ related entities | Domain boundaries start mattering |
| Code known to grow (new features, tenants, endpoints) | Investment in structure pays off |
| Business logic with changing rules (billing, promotions) | Isolate from HTTP/DB layers to test and modify independently |
| Multi-tenant or multi-client | Separation of concerns is mandatory, not optional |

**When to keep it simple (avoid over-engineering):**

| Signal | Why |
|--------|-----|
| One-off scripts, utilities, prototypes | Structure adds cost with no return |
| Small CRUD (1-2 entities, no real business logic yet) | A service layer for `create` and `list` is ceremony |
| Simple firmware/Arduino (loop + functions) | OOP adds complexity without benefit |
| No second use case in sight for an abstraction | YAGNI — abstract on the third repetition |

### Step 3: Apply Practical Rules

#### Naming and File Organization

| Rule | Example | Anti-pattern |
|------|---------|-------------|
| Names reflect the domain, not the implementation | `appointments/`, `promotions/` | Everything in `utils/` or `misc/` |
| One file, one clear responsibility | Split when mixing unrelated concerns | `helpers.js` that does 12 things |
| Predictable location | Where a reasonable dev would look for it | Custom folder hierarchy that ignores framework conventions |
| Consistent casing | Follow the project's style (kebab, camel, snake) | Mixing `UserProfile.ts` with `order_history.ts` |
| No generic names | `invoice-validator.ts`, `email-sender.py` | `data.py`, `temp.js`, `test2.ts` |

For small projects, the framework's default structure is enough. Don't create 8 folders for 3 files.

#### Code Quality Rules

1. **One function/class, one responsibility.** If the name needs "and", split it.
2. **Explicit dependencies, not hardcoded ones.** Inject what can change (DB clients, notification services) — without building a DI container unless justified.
3. **Don't repeat business logic** in two places. If a rule is used in two spots, extract it to a shared service/helper.
4. **Real error handling.** No empty `catch` blocks that swallow errors. Validate inputs at system boundaries (API entry, forms). Fail with clear messages without exposing internal details.
5. **No hardcoded secrets.** Keys, tokens, credentials, and DB URLs go in environment variables — never in code or the repository.
6. **Follow the project's linter/formatter** (Prettier, Black, ESLint, Ruff) over personal style.
7. **Comment the why, not the what.** Comments where intent isn't obvious; never narrate line by line.
8. **New changes follow the style of the file they touch.** Local consistency > theoretical purity.

#### Scalability: Design for Volume (100+ of Something)

When an entity can grow to 100, 1,000, or more records/users/items, design for it from the start without over-engineering:

**Backend / Data:**

| Practice | Why |
|----------|-----|
| Pagination from day one on any growable list | Never return all records without a limit |
| Indexes on frequently filtered/sorted/joined columns | Queries degrade silently without them |
| Avoid N+1 queries | Use eager loading / joins / dataloaders, not a query per item in a loop |
| Don't load entire collections into memory | Let the DB filter and count — that's what it's for |

**Frontend:**

| Practice | Why |
|----------|-----|
| Virtualization / lazy rendering for long lists | Don't mount 1,000 DOM nodes at once |
| Pagination or infinite scroll consuming backend pagination | Don't fetch everything and slice client-side |
| Loading / empty / error states | Not just the happy path with few records |

**Rule:** Don't optimize for millions when the real case is dozens, but leave the design ready to grow one order of magnitude without a rewrite.

## Security: Non-Negotiable Minimums (Every Stage, Even MVPs)

These always apply — they are the floor, not extra work. Additional security is proportional to risk (payment/personal data require more), but these are mandatory:

| Category | Requirement |
|----------|-------------|
| **SQL injection** | Parameterized queries / prepared statements / ORM. Never concatenate or interpolate user input into SQL. |
| **Input validation** | Validate and sanitize all input at system boundaries (type, format, length, range). Escape output by context (HTML, SQL, shell, URL) to prevent XSS and injection. |
| **Password storage** | Hash with bcrypt / argon2 / scrypt (automatic salt). Never plaintext, MD5, SHA1/SHA256 without key-stretching, or reversible encryption. Never log or return passwords. |
| **Authorization** | Per-resource authorization on every operation, not just "is logged in". Verify server-side that the resource belongs to the user (prevent IDOR). |
| **Sessions** | Tokens/cookies with expiration. Cookies: `HttpOnly`, `Secure`, `SameSite`. Regenerate session ID on login. Invalidate on logout and password change. |
| **Least privilege** | DB users, API keys, and admin routes with only necessary permissions. Admin routes restricted by role, not hidden by obscurity. |
| **Transport** | HTTPS everywhere. |
| **Dependencies** | Check for vulnerabilities when adding (`npm audit`, `pip-audit`). Prefer maintained packages. Pin versions in lockfile. |
| **Error messages** | Generic message to the user. Detail to the internal log (without passwords or tokens). Never expose stack traces, internal paths, versions, or SQL in production responses. |

## Proposing a Refactoring

Before proposing a refactoring, answer these questions:

```
REFACTORING CHECKLIST:
→ What concrete problem does this solve? (Not "this is more SOLID")
→ Is it scoped to the current task, or should it be a separate change?
→ Does the benefit justify the risk of touching working code?
→ Am I changing something that wasn't asked for?
```

- Explain in 1-2 lines what concrete problem the refactor solves.
- Large changes go as a separate suggestion, not mixed with the requested feature — one change does one thing.
- When in doubt about whether the refactor is worth it, ask before applying (except trivial corrections).
- Don't touch code unrelated to the request.

## Quick Checklist Before Writing New Code

- [ ] Does the project already have a convention for this? → Follow it
- [ ] Did I verify library APIs/versions instead of assuming them?
- [ ] Will this piece grow or repeat? → Minimal abstraction + scalable design (pagination/indexes/virtualization)
- [ ] Is this an isolated case or prototype? → Simple and direct, no extra layers
- [ ] Do files have clear names and are they where you'd look for them?
- [ ] Are security minimums met? (parameterized queries, password hashing, per-resource authorization, validated inputs, secrets out of code)
- [ ] Am I touching something that wasn't requested? → No, unless flagged as a separate suggestion

## Related Skills

- **decisiones-tecnicas-fundamentadas** — decides WHICH approach/technology to use; this skill guides HOW to implement it well.
- **graphql-evaluacion-implementacion** — inherits these structure and scale rules for the GraphQL case.

## References (load only when needed)

Paths relative to this skill's folder:

- `references/principles.md` — KISS, YAGNI, contextual SOLID.
- `references/best-practices.md` — general practices.
- `references/oop-and-patterns.md` — when to use OOP, polymorphism, and patterns.
- `references/anti-patterns.md` — errors to avoid.
