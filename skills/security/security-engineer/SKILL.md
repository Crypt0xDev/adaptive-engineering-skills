---
name: security-engineer
description: Mandatory and risk-proportional security for all code. Use when code handles authentication, sensitive data, public APIs, or before launching.
---

# Security Engineer

## Purpose

Guarantee mandatory security minimums in all code and risk-proportional security based on the project's context. Security is not a feature you add later — it's a constraint that applies from line one. The minimums are non-negotiable; everything else scales with the risk.

## When to Use

- All code that touches authentication, authorization, or sensitive data
- Before every launch (with `references/checklist-security-review.md`)
- Designing public APIs or third-party integrations
- Handling payments or personal data
- After a security incident or vulnerability report

## When NOT to Use

- To block an MVP with banking-grade security requirements — security is proportional to risk (minimums always; the rest depends on context)
- Formal compliance audits (SOC2, ISO 27001) — those require certified human specialists; this skill prepares for them, it doesn't certify
- Penetration testing — this skill guides secure development; pentesting is a separate activity

## Expected Inputs

- The code or design to evaluate
- Type of data the system handles (public, personal, financial, health)
- Exposed surface (public API, multi-tenant, internal only)
- Current stage (MVP, production, enterprise)

## Expected Output

```
Risk assessment:
  [CRITICAL] <finding> — <mitigation>
  [HIGH]     <finding> — <mitigation>
  [MEDIUM]   <finding> — <mitigation>
  
Mandatory minimums: <checklist status>
Risk-proportional recommendations: <based on data type and surface>
```

## Internal Rules

### Non-Negotiable Minimums (Every Stage, Every Project)

These apply regardless of context. No exceptions. No "we'll add it later."

| Rule | Why | Bad Example |
|---|---|---|
| **Secrets in environment variables**, never in code | Leaked repos expose all credentials | `const API_KEY = "sk-live-..."` in source |
| **HTTPS everywhere** | Plaintext HTTP exposes all traffic | HTTP endpoint serving login form |
| **Passwords hashed with bcrypt/argon2** | Weak hashes are trivially broken | MD5, SHA1, or plaintext passwords |
| **Input validation at system boundaries** | Untrusted input is the #1 attack vector | Accepting any string as an email |
| **Output escaped by context** | Prevents XSS and injection | Rendering user input as raw HTML |
| **Parameterized queries** | Prevents SQL injection | `"SELECT * FROM users WHERE id = " + userId` |
| **Session management** | Prevents session hijacking | No expiration, no regeneration on login |
| **Least privilege** | Limits blast radius | Admin API keys for read-only operations |
| **Errors without sensitive info** | Prevents information leakage | Stack traces shown to users |

### Session Management Checklist

```
- [ ] Sessions expire after inactivity (30 min default, configurable)
- [ ] Session ID regenerated on login (prevents session fixation)
- [ ] Session invalidated on logout (server-side, not just cookie deletion)
- [ ] Cookies: HttpOnly + Secure + SameSite=Lax (or Strict)
- [ ] No session data in URLs
- [ ] Concurrent session limit (if business requires)
```

### Risk-Proportional Security

Beyond the minimums, security requirements scale with what's at stake:

| Context | Additional Requirements |
|---|---|
| **Personal data (PII)** | Encryption at rest, audit logging, data retention policy, GDPR/CCPA compliance |
| **Financial data / payments** | PCI DSS compliance, tokenized card data (never store raw), transaction audit trail |
| **Public API** | Rate limiting, API key rotation, OAuth2/JWT with short expiration, request signing |
| **Multi-tenant** | Row-level authorization on EVERY operation, tenant isolation in queries, no data leakage between tenants |
| **Health data** | HIPAA compliance, encryption at rest and in transit, access logging, minimum necessary access |

### OWASP Top 10 Quick Reference

| Vulnerability | Check | Mitigation |
|---|---|---|
| **Injection** (SQL, NoSQL, OS) | User input reaches a query or command | Parameterized queries, never concatenate |
| **Broken Authentication** | Weak passwords allowed, no brute-force protection | Strong password policy, rate limiting, MFA |
| **Sensitive Data Exposure** | Sensitive data in logs, URLs, or plaintext | Encrypt at rest, mask in logs, HTTPS only |
| **Broken Access Control (IDOR)** | User A can access User B's data | Authorize by resource on every operation |
| **Security Misconfiguration** | Default credentials, verbose errors, open admin | Harden defaults, strip debug info in production |
| **XSS** | User input rendered as HTML | Context-aware output encoding |
| **CSRF** | State-changing requests without token | CSRF tokens or SameSite cookies |
| **Insecure Deserialization** | Untrusted data deserialized | Validate and sanitize before deserializing |
| **Known Vulnerabilities** | Outdated dependencies with CVEs | Regular dependency updates, automated scanning |
| **Insufficient Logging** | No record of security events | Log auth events, access to sensitive data, failures |

### Authorization Patterns

```typescript
// WRONG: Only checks "is logged in"
app.get('/invoices/:id', requireAuth, async (req, res) => {
  const invoice = await db.invoices.findById(req.params.id);
  res.json(invoice); // Any logged-in user sees any invoice!
});

// RIGHT: Checks "owns this resource"
app.get('/invoices/:id', requireAuth, async (req, res) => {
  const invoice = await db.invoices.findById(req.params.id);
  if (!invoice) return res.status(404).json({ error: 'Not found' });
  if (invoice.userId !== req.user.id) return res.status(403).json({ error: 'Forbidden' });
  res.json(invoice);
});
```

```sql
-- WRONG: Trusts the application to filter
SELECT * FROM invoices WHERE id = $1;

-- RIGHT: Enforces at the query level
SELECT * FROM invoices WHERE id = $1 AND user_id = $2;
```

## Examples

**Example 1 — IDOR in multi-tenant endpoint:**

```
Endpoint: GET /invoices/:id
Risk: CRITICAL — any logged-in user can read any other user's invoices

Finding: The endpoint checks authentication but not authorization. 
         It verifies the user is logged in but not that the invoice belongs to them.

Mitigation: Add resource-level authorization:
  WHERE invoice.user_id = session.user_id (in the query)
  OR middleware that verifies ownership before returning data
  
Verification: Test with User A's session requesting User B's invoice → must return 403
```

**Example 2 — MVP security assessment:**

```
Context: Internal tool, no sensitive data, 5 users, behind VPN

Assessment:
  Mandatory minimums: ALL APPLY (secrets, HTTPS, validation, parameterized queries)
  Risk-proportional: LOW
    - No PCI/GDPR requirements (no sensitive data)
    - No public API (behind VPN)
    - No multi-tenancy (5 known users)
  
Recommendation: Apply all non-negotiable minimums. Skip formal pentest until 
                the tool becomes externally accessible or handles sensitive data.
```

**Example 3 — API key in source code found during review:**

```
Finding: [CRITICAL] API key for payment provider hardcoded in config.ts line 14
  const STRIPE_KEY = "sk_live_abc123..."

Immediate actions:
  1. Rotate the key immediately (it's compromised once committed)
  2. Move to environment variable
  3. Check git history — the key exists in all previous commits
  4. Add .env to .gitignore
  5. Consider git-secrets or similar pre-commit hook

Note: Even after removing from code, the key exists in git history. 
      The key MUST be rotated, not just removed from the current commit.
```

## Verification

- [ ] All non-negotiable minimums are met (see checklist above)
- [ ] No secrets in source code or git history
- [ ] Authorization checks are per-resource, not just per-session
- [ ] Input validation at every system boundary
- [ ] Output escaped appropriately for context (HTML, SQL, URL, etc.)
- [ ] Dependencies scanned for known vulnerabilities
- [ ] Error messages don't leak sensitive information
- [ ] Risk-proportional requirements addressed for the data type
- [ ] Run `references/checklist-security-review.md` before launch

## References (load only when needed)

Paths relative to this skill's folder:

- `references/checklist-security-review.md` — pre-launch security checklist
