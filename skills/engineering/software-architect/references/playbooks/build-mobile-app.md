# Playbook: Build Mobile App

## Skills Involved
`product-manager` → `ux-designer` → `software-architect` → `devops-engineer`

## Phases

### 1. Platform Decision (software-architect)
| Context | Choice |
|---------|--------|
| MVP, web team | React Native / Expo or Flutter |
| Strong need for native APIs / performance | Native (Swift / Kotlin) |
| Just validating an idea | PWA first |

### 2. UX (ux-designer)
- Design for partial offline and slow connections.
- Loading/error states on every screen.
- Follow platform guidelines (HIG / Material).

### 3. Backend
- Reuse existing API or create a minimal one (see `build-api.md`).
- Auth with long-lived tokens + refresh.

### 4. Distribution (devops-engineer)
- Automated builds (EAS, Fastlane).
- Crash reporting from day one (Sentry, Crashlytics).
- Release plan: stores have review, there's no instant hotfix.

## What NOT to Do at the Start
Duplicate native apps with a small team, complex offline sync, push notifications before having users.
