# Playbook: Build SaaS

## Skills Involved
`startup-advisor` → `product-manager` → `software-architect` → `database-architect` → `security-engineer` → `devops-engineer`

## Phases

### 1. Validation (startup-advisor + product-manager)
- Define the business hypothesis and the minimum MVP that validates it.
- Cut everything that doesn't validate the hypothesis.

### 2. Architecture (software-architect + database-architect)
- Default: simple monolith (Next.js / Rails / Laravel or similar) + PostgreSQL.
- Multi-tenancy: `tenant_id` column in a single DB; separate schemas or DBs only with evidence.

### 3. SaaS Essentials
- Auth (use a provider: Clerk, Auth0, Supabase — don't build).
- Subscriptions and payments (Stripe — don't build billing).
- Transactional emails (Resend, Postmark).
- Minimum onboarding that gets the user to value quickly.

### 4. Security (security-engineer)
- Tenant isolation on every query.
- Non-negotiable minimums from `skills/security-engineer/SKILL.md`.

### 5. Launch (devops-engineer)
- PaaS, CI/CD, backups, error monitoring.
- Pass the launch checklist (skill `devops-engineer` → `references/checklist-launch.md`).

## What NOT to Do at the Start
Microservices, Kubernetes, custom billing, complex feature flags, multi-region.
