# Checklist: Security Review

## Non-negotiable Minimums
- [ ] Secrets out of the code (environment variables / vault).
- [ ] HTTPS on all public environments.
- [ ] Passwords with strong hashing (bcrypt / argon2).
- [ ] Parameterized queries on all data access.
- [ ] Input validation at the system boundary.

## Authentication and Authorization
- [ ] Tokens with expiration and secure renewal.
- [ ] Authorization verified per resource (not just "is logged in").
- [ ] No predictable IDs that allow access to others' data (IDOR).

## Data
- [ ] Sensitive data identified and encrypted at rest if applicable.
- [ ] No sensitive data in logs.
- [ ] Applicable compliance reviewed (GDPR / PCI / sector).

## Surface
- [ ] Dependencies without known vulnerabilities (npm audit / equivalent).
- [ ] Rate limiting on public and login endpoints.
- [ ] Security headers configured (CSP, HSTS, etc.).
