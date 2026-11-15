# OOP, Polymorphism and Patterns: When to Apply Them

> OOP and patterns (like Singleton) are applied only when the context justifies it, not as a fixed rule.

## Object-Oriented Programming

### When to Apply OOP
- The domain has **entities with their own state and behavior** (Order, Account, Reservation) whose rules should be encapsulated together.
- There are **invariants to protect** (e.g. "an order cannot be confirmed without items") — the class guarantees it never exists in an invalid state.
- There are **real behavior variants** that benefit from a common interface.

### When NOT to
- Pure data transformation logic (input → output): simple functions are clearer and more testable.
- Classes with only getters/setters and no behavior (anemic model): it's a struct in disguise, use a simple data object.
- Creating inheritance hierarchies "to reuse code": prefer composition; inheritance only for true "is-a" relationships with polymorphic behavior.

## Polymorphism

### When to Use
- There are **2+ real implementations today** of the same contract (e.g. `PaymentGateway` → Stripe, PayPal) and the client code shouldn't know which one it uses.
- `if/switch` on the same "type" repeats in multiple places: replacing them with polymorphism eliminates the duplication.

### When NOT to
- A single implementation "just in case" another comes (YAGNI — premature abstraction).
- A single `switch` in one place: it's simpler and more readable than a class hierarchy.

## Entity Relationships

### Necessary
- The relationship exists in the **real business** and the code queries or validates it (Order → Customer, Invoice → Order).
- The cardinality reflects the business rule (an order belongs to ONE customer).

### Unnecessary (avoid)
- Bidirectional relationships "for convenience" when only one direction is navigated — they create coupling and cycles.
- Speculative relationships for queries nobody makes.
- Intermediate entities with no business meaning.

**Rule:** every relationship must be justified by a real use case that traverses it. If nobody queries it, it doesn't exist.

## Singleton Pattern

### Correct Use (rare)
Only when **conceptually there must be ONE instance in the entire system** and creating more would be an error:
- DB connection pool, configuration loaded once, logger.
- Even in these cases, prefer **creating a single instance and injecting it** (dependency injection) over a Singleton with static global access.

### Incorrect Use (the usual)
- As a disguised global variable to "access something from anywhere" → hidden coupling, impossible to test.
- For services with shared mutable state → concurrency bugs.
- By default/habit, without asking if uniqueness is a domain requirement.

**Rule:** if you can pass the dependency through the constructor, do it. Singleton is the last option, depending on the project context and architecture, not the first.

## Key Idea

Architecture (microservices, OOP, patterns like Singleton) should be applied **only when the context justifies it**, not as a fixed rule. See skill `software-architect` → `references/decision-rules.md` (Step 3 — patterns on demand).
