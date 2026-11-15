# Microservices: When and When Not

> Architecture should be applied only when the context justifies it, not as a fixed rule.

## When NOT to Use Microservices

- Project in idea / MVP stage (the domain still changes too much).
- Small team (< 2-3 independent teams): a single team maintains a monolith better.
- Domain boundaries not yet proven in production.
- "Because Netflix/Google uses them" (cargo cult — see anti-patterns in skill `engineering-best-practices`).
- To fix messy code: a messy monolith becomes messy microservices + network.

## When Separating into Two or More Services IS Justified

A service is separated when **several** of these conditions are met at once (not just one):

1. **Proven domain boundary**: the module has its own language, data, and rules, with little communication with the rest (real bounded context).
2. **Independent scaling**: one part needs 10x more resources than the rest (e.g. image processing vs CRUD), and scaling the full monolith is costly.
3. **Independent teams**: there's a team that can own the complete service (code, deploy, on-call). Conway's Law: architecture follows organization.
4. **Conflicting deployment cycles**: one part changes daily and another is stable, and deploys block each other.
5. **Incompatible technical requirements**: different language/runtime justified (e.g. ML in Python within a Java system), or compliance requirements that demand isolation (e.g. PCI for payments).

## Rules When Separating

- **Extract, don't design from scratch**: the first microservice is extracted from a modular monolith where the boundary was already tested.
- **One service = its database**: no sharing tables between services; communication only via API or events.
- **Start from the edge**: extract modules with few dependencies first (e.g. notifications, report generation), not the domain core.
- **Versioned contracts** between services; one service doesn't break another on deploy.
- **Cost assumed consciously**: each service adds network, latency, observability, deploys, and distributed failure modes. If that cost doesn't buy anything, don't separate.

## Signals to Evolve (from modular monolith to services)

- Monolith builds/deploys block multiple teams daily.
- A specific module consumes disproportionate, measured resources.
- Constant merge conflicts between teams in the same modules.

Document the extraction decision as ADR in the project repo (it's irreversible in practice).
