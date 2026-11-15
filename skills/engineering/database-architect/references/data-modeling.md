# Data Modeling and Normalization

Best practices for schema design. Complements `skills/database-architect/`.

## Key Idea

Database design should be based on:

> **the problem domain + the system's future queries**

Not just storing data, but how it will be used, queried, and scaled.

## Good Design Process (in order)

1. **Understand system requirements**: what the business does, what information it needs, and how often.
2. **Clearly define domain entities**: business nouns with their own identity (Customer, Order, Product).
3. **Establish proper relationships**: only those the business requires, with correct cardinality (see Relationships section).
4. **Define correct and necessary attributes**: each column answers a real need; no "just in case" fields.
5. **Apply normalization** (3NF by default, see table below).
6. **Test and optimize based on real usage**: validate the model with the system's main queries and index based on measured access patterns.

## Common Mistakes to Avoid

- **Not identifying entities correctly** → tables that mix concepts or concepts spread across multiple tables without reason.
- **Unnecessary or redundant fields** → columns nobody queries or that duplicate derivable information.
- **Not defining primary keys** → every table has a PK, no exceptions.
- **Not applying normalization correctly** → repeating groups, partial or transitive dependencies (see normal forms).
- **Generating duplicate data** → the same fact stored in two places without someone responsible for syncing it.
- **Not thinking about future queries or usage patterns** → a "pretty" model that makes the daily queries the system needs impossible.

## Schema Design Rules

- **Model the business, not the UI**: tables reflect real domain entities, not screens.
- **Correct types**: money in integers (cents) or `DECIMAL` (never float), dates with timezone (`timestamptz`), real booleans (not `'Y'/'N'`).
- **Integrity in the DB**: primary keys always, foreign keys and constraints (`NOT NULL`, `UNIQUE`, `CHECK`) in the database, not just in the app.
- **Consistent naming**: one language and convention (`snake_case` plural for tables: `orders`, `order_items`).
- **No multi-value columns**: never store lists in a field (`"1,2,3"`); use a related table.
- **Versioned migrations** from day one; never alter the schema manually in production.

## Normalization

Normalize to **3NF by default**:

| Form | Practical Rule |
|------|----------------|
| 1NF | Each cell a single value; no repeating groups (`phone1`, `phone2` → `phones` table) |
| 2NF | Every attribute depends on the complete key (matters for composite keys) |
| 3NF | No attribute depends on another non-key attribute (city is not derived from zip code within the same table) |

### Denormalize Only When
- There's a measured slow query that normalization makes expensive, and
- The duplicated data is documented along with who keeps it in sync.

Valid example: price snapshot in `order_items` — this isn't incorrect denormalization, it's a **historical business fact** (the price at time of purchase).

## Relationships

- **1:N** — the most common: FK on the "many" side (`orders.customer_id`).
- **N:M** — intermediate table with a business name if it has one (`enrollments` better than `student_course`).
- **1:1** — suspicious: almost always the same table; separate only for security (sensitive data) or huge rarely-queried columns.
- Every relationship is justified by a real use case that traverses it (see skill `engineering-best-practices` → `references/oop-and-patterns.md`).

## Indexes

- Create based on real queries (frequent WHERE, JOIN, ORDER BY), not speculative.
- FKs almost always indexed.
- Every index costs on writes: measure before adding more.
