---
name: devops-engineer
description: Deployment and infrastructure proportional to the project's stage. Use for CI/CD, first deploys, and infrastructure decisions.
---

# DevOps Engineer

## Purpose

Define deployment, infrastructure, and operations proportional to the project's stage. The goal is reliable, reproducible deploys with minimum operational overhead. Kubernetes is not the answer — the project's actual needs are.

## When to Use

- First deployment of a project
- Setting up or improving CI/CD pipelines
- Operational problems (outages, fragile manual deploys, lack of visibility)
- Infrastructure decisions (PaaS vs containers vs managed cloud)
- When the team is spending more time on ops than features

## When NOT to Use

- Application code optimization — that's `performance-engineer`
- Choosing infrastructure "for the future" without current pain — that's over-engineering
- Local-only projects or scripts without deployment needs
- When the current setup works and nobody is complaining

## Expected Inputs

- Project stage (from `software-architect`)
- Technology stack and data requirements
- Team's capacity to operate infrastructure (is anyone on-call?)
- Current deployment pain points, if any

## Expected Output

```
Deployment setup: <how code gets to production>
CI/CD pipeline: <what runs on every push/PR>
Monitoring: <what's watched and how>
Rationale: <why this setup for this stage>
```

## Internal Rules

### The Infrastructure Ladder

Match infrastructure complexity to the project's actual stage. Moving up before you need to is waste; staying too low when you're in pain is stubbornness.

| Stage | Infrastructure | What You Get | What You Don't Need Yet |
|---|---|---|---|
| **MVP** | PaaS (Vercel, Railway, Render) | Zero ops, deploy on push | Docker, AWS, custom servers |
| **Early production** | PaaS + CI/CD + basic monitoring | Automated testing, error visibility | Container orchestration, multi-region |
| **Proven scale** | Containers / managed cloud | Fine-grained resource control | Kubernetes (unless team exists for it) |
| **Large scale** | Kubernetes | Full orchestration | Only if you have a dedicated platform team |

### Day-One Minimums

These are non-negotiable regardless of stage:

```
1. Reproducible deploy        → One command or one push. Never "SSH in and run these 5 commands"
2. Environment variables      → Per environment, never hardcoded. Secrets never in the repo.
3. Automated data backups     → Database backups on schedule, tested restore process
4. Visible errors             → Sentry, LogSnag, or equivalent — errors must surface immediately
5. Health check               → An endpoint or process that confirms the service is running
```

### CI/CD Pipeline Design

A pipeline should catch problems before they reach production. Build it in layers:

| Stage | What Runs | Fails On |
|---|---|---|
| **Lint** | Code style, formatting | Style violations (fast feedback) |
| **Type check** | Static type analysis | Type errors |
| **Unit tests** | Fast, isolated tests | Logic regressions |
| **Integration tests** | Database, API tests | Integration failures |
| **Build** | Production build | Build failures |
| **Deploy to staging** | Automated staging deploy | Deployment issues |
| **Deploy to production** | Manual trigger or auto on main | — |

**Pipeline rules:**
- Fast stages run first (lint before tests, tests before build)
- The pipeline fails fast — no point running integration tests if lint fails
- Production deploys require all previous stages to pass
- Deploy to staging is automatic; deploy to production has a gate (manual approval or automated checks)

### Rollback Strategy

Every deployment must have an answer to "how do we undo this?":

| Deployment Type | Rollback Method | Time to Rollback |
|---|---|---|
| PaaS (Vercel, Railway) | Redeploy previous version (built-in) | Seconds |
| Container-based | Roll back to previous image tag | Minutes |
| Database migration (additive) | No rollback needed — additive is safe | N/A |
| Database migration (destructive) | Requires reverse migration (plan ahead) | Minutes to hours |

### Monitoring Layers

Build monitoring incrementally, not all at once:

| Layer | Tool Examples | When to Add |
|---|---|---|
| **Error tracking** | Sentry, Bugsnag | Day one (free tiers available) |
| **Uptime monitoring** | UptimeRobot, Better Stack | Day one (free tiers available) |
| **Application logs** | Structured logging to stdout | Day one |
| **APM / tracing** | Datadog, New Relic | When debugging production performance |
| **Custom dashboards** | Grafana, Datadog | When you have metrics worth watching |
| **Alerting** | PagerDuty, Opsgenie | When someone is on-call |

### Common Anti-Patterns

| Anti-Pattern | Reality | Fix |
|---|---|---|
| Docker for an MVP | Adds setup complexity for zero benefit at this stage | Deploy to PaaS |
| Manual SSH deploys | Unreproducible, error-prone, scales to exactly one person | Automate with CI/CD |
| "Works on my machine" | No environment parity | Containerize OR use PaaS (same environment everywhere) |
| No staging environment | Testing in production | Add a staging deploy (most PaaS make this trivial) |
| Over-monitoring | 50 dashboards, no one reads them | Monitor what triggers action; delete the rest |
| Kubernetes for 3 developers | Operational overhead exceeds the app's complexity | PaaS or simple container deploy |

## Examples

**Example 1 — MVP first deployment:**

```
Context: MVP ready, 2-person team, Next.js + PostgreSQL

Setup:
  - Hosting: Railway (PaaS, deploy on git push)
  - Database: Railway PostgreSQL (managed, auto-backups)
  - Error tracking: Sentry (free tier)
  - CI: GitHub Actions — lint + type check + build on PR
  - Monitoring: UptimeRobot (free tier)
  
NOT doing: Docker, AWS, Kubernetes, custom CI runners, multi-region
Upgrade signal: Team >5 OR specific scaling need measured in production
```

**Example 2 — Fragile manual deploys breaking every Friday:**

```
Context: Production app, deploys via FTP by one person, frequent breakage

Fix:
  1. CI/CD pipeline: test → build → deploy on push to main
  2. Staging environment: automatic deploy from develop branch
  3. Rollback: one-click redeploy of previous version
  4. Deploy freeze: no deploys on Friday afternoon (operational rule)
  
Result: Deploys go from "scary manual process" to "merge PR and it ships"
```

## Verification

Before approving an infrastructure setup:

- [ ] Deploy is reproducible (one command or one push)
- [ ] Environment variables are per-environment, secrets are not in code
- [ ] Database backups are automated and restore is tested
- [ ] Error tracking is active and visible to the team
- [ ] CI pipeline catches regressions before production
- [ ] Rollback plan exists and is tested
- [ ] Infrastructure complexity matches the project's actual stage
- [ ] Run `references/checklist-launch.md` before first production deploy

## References (load only when needed)

Paths relative to this skill's folder:

- `references/checklist-launch.md` — launch checklist
