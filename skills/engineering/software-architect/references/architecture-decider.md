# Architecture Decider

Receives the summary from `context-analyzer.md` and decides the minimum viable architecture.

## Decision Matrix

| Context | Recommended Architecture |
|---------|--------------------------|
| Idea / prototype, solo developer | Script or single-module app |
| MVP, uncertain domain | Simple monolith, minimal layers |
| Production, clear domain | Modular monolith (modules by domain) |
| Proven scale + independent teams | Extract services only where it hurts |

## Rules

1. **Never start with microservices.** They are extracted, not designed from scratch.
2. **Layers only if more than one consumer** of that logic exists.
3. **Database:** a relational one by default; specialized ones only with evidence.
4. **External abstractions** (queues, cache, events): add when the problem exists, not before.

## Output Format

```
Architecture: <decision>
Reason: <1-3 sentences tied to context>
What we WON'T do and why: <list>
Signals to evolve: <what pain would justify the next level>
```

Verify afterwards with `checklist-architecture-review.md` and document irreversible decisions as ADRs in the project repo.
