# Checklist: Launch

## Functional
- [ ] Main value flow tested end to end.
- [ ] Error and empty states handled in the UI.
- [ ] Tested on target audience devices/browsers.

## Operations
- [ ] Reproducible deploy and rollback tested.
- [ ] Automated backups active and restoration verified.
- [ ] Error monitoring active (Sentry or similar) with alerts.
- [ ] Logs accessible in production.

## Security
- [ ] Security checklist completed (skill `security-engineer` → `references/checklist-security-review.md`).
- [ ] Production environment variables reviewed (no dev values).

## Business
- [ ] Success metrics instrumented (minimum analytics).
- [ ] Terms / privacy published if user data is collected.
- [ ] Support/feedback channel defined.

## Post-launch
- [ ] On-call owner for the first 48h defined.
- [ ] Plan for the first iteration based on real feedback.
