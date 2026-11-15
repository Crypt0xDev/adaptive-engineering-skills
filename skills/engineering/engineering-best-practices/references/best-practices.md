# Best Practices

## Code
- Names that explain intent; code is read more than it is written.
- Small functions with a single clear responsibility.
- Handle errors where you can act on them, not before.
- Tests for business-value behavior, not to hit metrics.

## Architecture
- Layers only if more than one consumer of that logic exists.
- A relational database by default; specialized ones only with evidence.
- Queues, cache, and events: add when the problem exists, not before.

## Process
- Start with the highest business-value flow.
- Small and frequent deliveries; early feedback.
- Stack the team already masters, unless there's a strong documented reason.

## Documentation
- Document decisions (the why), not the obvious (the what).
- A new dev should understand the project in less than a day.

## Minimum Security Always
- Secrets out of the code (environment variables).
- Validate inputs at the system boundary.
- HTTPS and password hashing are not optional at any stage.
