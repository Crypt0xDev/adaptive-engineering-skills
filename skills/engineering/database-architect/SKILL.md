---
name: database-architect
description: Design the data model and choose the right database engine. Use for schema design, normalization, entity relationships, and database decisions.
---

# Database Architect

## Purpose

Design the data model and choose the right database engine based on the domain and real access patterns. The schema should model the business, enforce its rules at the data layer, and support the queries the system actually needs.

## When to Use

- Starting a project (initial schema design)
- New data domains appearing in an existing system
- Measured query performance problems
- Evaluating a database engine migration or schema evolution
- When data integrity issues are reported (orphaned records, inconsistent state)

## When NOT to Use

- Day-to-day ad hoc queries — those don't need design decisions
- Performance optimization without prior measurement — that goes through `performance-engineer` first
- Choosing an ORM or data access library — that's `researcher`
- Adding a cache or queue "just in case" — only when measured need exists

## Expected Inputs

- Business entities and their real relationships (from `business-analyst` or domain knowledge)
- Volume and access patterns — real or honestly estimated (read-heavy vs write-heavy, growth rate)
- The primary queries the system will run
- Constraints (existing infrastructure, team expertise, compliance requirements)

## Expected Output

```
Schema: <entity-relationship description or DDL>
Engine: <chosen database> — <rationale tied to access patterns>
What we WON'T do: <over-engineering avoided>
Migration plan: <how to get from current state to proposed state>
```

## Internal Rules

### Engine Selection

Start with PostgreSQL. Move to something else only with evidence.

| Need | Engine | When to Consider |
|------|--------|-----------------|
| General-purpose, relational | PostgreSQL | Default choice — covers 90% of cases |
| Document-oriented, schema flexibility | MongoDB | Truly schema-less data that varies per record AND no relational queries needed |
| Full-text search | PostgreSQL `tsvector` or Elasticsearch | PostgreSQL first; Elasticsearch only at search-heavy scale |
| Key-value cache | Redis | Measured latency problem that caching solves |
| Time-series | TimescaleDB (on PostgreSQL) | High-volume time-series ingestion with time-based queries |
| Graph relationships | Neo4j | Core domain IS the graph (social networks, recommendation engines) |

**One database until it hurts.** Adding a second database doubles operational complexity. The pain must be measured and specific.

### Schema Design Rules

1. **Design from the domain, not the UI.** Tables model business entities and their real relationships. A form layout is not a schema.

2. **Normalize to 3NF by default.** Denormalize only with measured query performance data, and document who owns keeping the denormalized data in sync.

3. **Every table gets a primary key.** Prefer UUIDs for distributed systems, auto-increment integers for simpler setups.

4. **Foreign keys and constraints in the database**, not just in the application. The database is the last line of defense for data integrity.

   ```sql
   -- YES: constraint at the database level
   ALTER TABLE orders ADD CONSTRAINT fk_orders_customer
     FOREIGN KEY (customer_id) REFERENCES customers(id);
   
   -- NO: only validating in application code
   -- "We check customer_id exists before inserting" — until someone doesn't
   ```

5. **Indexes based on real queries, not speculation.** Add an index when you have the query that needs it. Review with `EXPLAIN ANALYZE`.

   ```sql
   -- Query: SELECT * FROM orders WHERE customer_id = ? AND status = 'active' ORDER BY created_at DESC
   -- Index that serves this query:
   CREATE INDEX idx_orders_customer_status_created 
     ON orders (customer_id, status, created_at DESC);
   ```

6. **Versioned migrations from day one.** Every schema change is a migration file, reviewed like code.

7. **Audit columns on every table** where the business cares about "who changed what when":
   ```sql
   created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
   updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
   ```

### Denormalization Decision Framework

| Question | If Yes |
|----------|--------|
| Is the query slow with measurement? | Consider denormalization |
| Can an index solve it? | Add the index instead |
| Can a materialized view solve it? | Use the view instead |
| Is the denormalized data a historical snapshot? | That's not denormalization — it's a business fact (e.g., price at time of order) |
| Who will keep the copies in sync? | If nobody is assigned, don't denormalize |

### Common Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Entity-Attribute-Value (EAV) | Impossible to query efficiently, no constraints | Model actual entities as tables |
| Storing JSON blobs for relational data | Loses referential integrity and query power | Use proper tables with FKs |
| Soft deletes everywhere | Complicates every query with `WHERE deleted_at IS NULL` | Use only where audit trail is legally required; otherwise hard delete |
| One table per tenant | Schema management nightmare at scale | Single schema with `tenant_id` column and row-level security |
| No timestamps | Can't debug, can't audit | Always add `created_at` and `updated_at` |

## Examples

**Example 1 — New e-commerce order schema:**

Entities: Customer, Product, Order, OrderItem.

```sql
CREATE TABLE customers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE products (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  price_cents INTEGER NOT NULL CHECK (price_cents >= 0),
  active BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  customer_id UUID NOT NULL REFERENCES customers(id),
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','paid','shipped','cancelled')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE order_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  product_id UUID NOT NULL REFERENCES products(id),
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  unit_price_cents INTEGER NOT NULL CHECK (unit_price_cents >= 0)
  -- unit_price_cents is a snapshot: the price at time of purchase (business fact, not denormalization)
);
```

**Example 2 — Slow dashboard aggregation:**

Symptom: Daily sales dashboard query takes 12 seconds, scanning 10M rows.

```
Step 1: EXPLAIN ANALYZE the query → sequential scan on orders, no index on date range
Step 2: Add composite index → CREATE INDEX idx_orders_date_status ON orders (created_at, status)
Step 3: Re-measure → 12s → 200ms
Step 4: Materialized view NOT needed — the index solved it
```

## Verification

- [ ] Schema models business entities and their real relationships
- [ ] Every table has a primary key
- [ ] Foreign keys enforce referential integrity at the database level
- [ ] Constraints validate business rules (CHECK, NOT NULL, UNIQUE where appropriate)
- [ ] Indexes match the actual queries the system runs
- [ ] No speculative denormalization — only where measured and documented
- [ ] Migrations are versioned and reviewable
- [ ] Run `references/checklist-database-review.md`

## References (load only when needed)

Paths relative to this skill's folder:

- `references/data-modeling.md` — modeling, normalization, and relationships
- `references/checklist-database-review.md` — final verification checklist
