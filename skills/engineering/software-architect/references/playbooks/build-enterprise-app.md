# Playbook: Build Enterprise App

## Skills Involved
`business-analyst` → `software-architect` → `database-architect` → `security-engineer` → `devops-engineer` → `code-reviewer`

## Context Differences
Here the context does justify more structure: multiple stakeholders, compliance, legacy integrations, long lifespan.

## Phases

### 1. Requirements (business-analyst)
- Map stakeholders, current processes, and existing integrations (ERP, AD/SSO, legacy systems).
- Requirements with signed acceptance criteria.

### 2. Architecture (software-architect)
- Modular monolith with clear domain boundaries — prepared to extract, not extracted.
- Explicit contracts with external systems; anti-corruption layer at legacy boundaries.

### 3. Security and Compliance (security-engineer)
- Corporate SSO (SAML / OIDC), RBAC per resource.
- Audit trail for sensitive actions from day one.
- Applicable compliance (GDPR, SOC2, sector regulations).

### 4. Quality and Operations
- CI/CD with environments (dev / staging / prod), mandatory code review.
- Data migrations rehearsed; rollback plan.
- Decision documentation as ADRs in the project repo.

## What NOT to Do
Big-bang rewrite of legacy systems; microservices without teams to own them; custom internal frameworks.
