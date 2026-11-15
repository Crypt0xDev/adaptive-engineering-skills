# Context Analyzer

Analyzes the real state of the project before any decision. This is the first step in the system flow.

## Inputs to Evaluate

### Business
- Product purpose and target users
- Stage: idea / MVP / production / legacy
- Time and budget constraints

### Technical
- Current stack and existing technical debt
- Real data volume and traffic (not projected)
- External integrations

### Team
- Size and seniority
- Domain knowledge
- Long-term maintenance capacity

## Output

A context summary with:

```
Stage: <idea|mvp|production|legacy>
Domain complexity: <low|medium|high>
Real load: <low|medium|high>
Team: <solo|small|medium|large>
Main risk: <description>
```

This summary feeds into `architecture-decider.md` and determines which other plugin skills to activate.
