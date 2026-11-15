# Anti-patterns

Mistakes the system must detect and avoid.

### Over-engineering
Solving problems that don't exist. Signs: configuration for cases nobody asked for, flexibility with no consumers.
**Antidote:** KISS + complexity ladder (skill `software-architect` → `references/decision-rules.md`).

### Premature Abstraction
Creating interfaces, factories, or generic layers before having 2+ real cases.
**Antidote:** rule of three — abstract on the third repetition.

### Unnecessary Microservices
Splitting into services without proven domain boundaries or a real need for independent scaling.
**Antidote:** modular monolith first; extract only where it hurts.

### Complexity Without Value
Patterns, frameworks, or tools added because "it's the right thing" rather than because the context calls for it.
**Antidote:** every piece must be justified with a business sentence.

### Cargo Cult
Copying architectures from large companies (Netflix, Google) in radically different contexts.
**Antidote:** context always defines the solution.

### Premature Optimization
Optimizing performance without measuring first.
**Antidote:** measure → identify the real bottleneck → optimize only that.

### Resume-driven Development
Choosing technology for trends or CV, not for the problem.
**Antidote:** stack the team masters, unless there's a strong documented reason.
