# Checklist: Database Review

## Model (references/data-modeling.md)
- [ ] Do entities reflect the real business domain (well identified, no mixed concepts)?
- [ ] Is every attribute necessary? (no redundant or "just in case" fields)
- [ ] Are relationships justified by real use cases, with correct cardinality?
- [ ] Is the schema normalized (3NF), with denormalizations justified by metrics?
- [ ] No duplicate data without a sync owner?
- [ ] Does the model support the system's expected queries and usage patterns?
- [ ] Correct types (money in integers, dates with timezone, consistent IDs)?

## Integrity
- [ ] Does every table have a primary key?
- [ ] Foreign keys and constraints in the DB, not just in the app?
- [ ] NOT NULL fields where the business requires it?

## Performance
- [ ] Indexes based on real queries, not speculative?
- [ ] N+1 queries detected in main flows?
- [ ] Pagination on every collection read?

## Operations
- [ ] Versioned and reversible migrations?
- [ ] Automated backups verified (restoration tested)?
- [ ] Sensitive data encrypted at rest if risk requires it?
