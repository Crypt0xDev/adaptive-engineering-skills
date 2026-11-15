---
name: performance-engineer
description: Optimize performance based on real measurements, never assumptions. Use when slowness is measured or before scaling infrastructure.
---

# Performance Engineer

## Purpose

Optimize performance based on real measurements, never on assumptions or gut feelings. The process is always: measure, identify the bottleneck, fix only that bottleneck, verify the fix. Without measurement, there is no optimization — only guessing.

## When to Use

- Slowness reported by users or detected in metrics
- Before deciding to scale infrastructure (verify the problem isn't code first)
- Reviewing critical queries or endpoints with a defined performance budget
- When the team proposes adding cache/CDN/queue "because it's slow"

## When NOT to Use

- Without a measured problem or a breached performance budget — optimizing "just in case" is premature optimization
- During initial MVP development — make it work first, make it fast second (with measurement)
- Micro-optimizations that sacrifice readability for unmeasurable gains
- When the fix is obvious (like adding a missing index) — just fix it, don't formalize a process

## Expected Inputs

- The quantified symptom (latency, throughput, memory) or the breached performance budget
- Access to the environment where the problem can be reproduced
- Business performance budget if defined (e.g., p95 < 300ms)

## Expected Output

```
Diagnosis: <what's slow and why, with data>
Bottleneck: <the single biggest contributor>
Fix applied: <what was changed>
Before/After: <measured comparison>
```

## Internal Rules

### The Performance Process (Strict Order)

```
1. MEASURE     → Reproduce and quantify the problem
2. PROFILE     → Identify the real bottleneck with data
3. OPTIMIZE    → Fix ONLY the identified bottleneck
4. VERIFY      → Measure again and compare
```

**Never skip a step. Never start at step 3.**

### The Bottleneck Hierarchy

Fix cheap things first. Most performance problems have simple solutions:

| Check | Fix | Effort | Impact |
|---|---|---|---|
| Missing database index | Add index based on query `EXPLAIN` | Minutes | Often 10-100x |
| N+1 query pattern | Eager loading or batch query | Minutes to hours | Often 5-50x |
| No pagination | Add LIMIT/OFFSET or cursor pagination | Hours | Prevents linear degradation |
| Redundant computation | Cache the expensive result | Hours | Depends on cache hit rate |
| Large payload | Paginate, compress, or select only needed fields | Hours | Reduces transfer time |
| Unoptimized images | Resize, compress, use modern formats | Hours | Major for web pages |
| Missing CDN | Serve static assets from CDN | Hours | Reduces latency for distributed users |
| Synchronous blocking | Move to async/background job | Days | Frees the request thread |
| Wrong algorithm | Replace with better complexity | Days | Orders of magnitude for large inputs |
| Hardware limit | Scale up/out | Days + cost | Last resort |

**Scale hardware before rewriting code, if the cost justifies it.** A $50/month server upgrade is cheaper than 2 weeks of developer time.

### Measurement Tools by Layer

| Layer | Tool | What It Shows |
|---|---|---|
| **Database** | `EXPLAIN ANALYZE` (PostgreSQL) | Query plan, actual time per step, row estimates |
| **Backend** | APM (Datadog, New Relic) or manual timing | Endpoint latency, throughput, error rate |
| **Frontend** | Lighthouse, Web Vitals | LCP, FID, CLS, bundle size |
| **Network** | Browser DevTools Network tab | Request waterfall, payload sizes, cache hits |
| **System** | `top`, `htop`, `vmstat` | CPU, memory, disk I/O utilization |

### Database Performance Patterns

```sql
-- DIAGNOSE: Find slow queries
-- PostgreSQL: enable pg_stat_statements or check slow query log

-- ANALYZE: Understand why a query is slow
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders 
WHERE customer_id = 'abc' AND status = 'active' 
ORDER BY created_at DESC;

-- Common findings and fixes:

-- 1. Sequential scan on large table → Add index
CREATE INDEX idx_orders_customer_status 
  ON orders (customer_id, status, created_at DESC);

-- 2. N+1 queries (100 orders → 100 queries for order_items)
-- Before: for each order, query its items separately
-- After: JOIN or IN query
SELECT o.*, oi.* FROM orders o
JOIN order_items oi ON oi.order_id = o.id
WHERE o.customer_id = 'abc';

-- 3. COUNT(*) on large table → Use estimated count or materialized view
-- Instead of: SELECT COUNT(*) FROM orders (scans entire table)
-- Use: SELECT reltuples FROM pg_class WHERE relname = 'orders' (estimate)
```

### Frontend Performance Patterns

| Problem | Metric | Fix |
|---|---|---|
| Large JavaScript bundle | Bundle size > 200KB gzipped | Code splitting, tree shaking, lazy loading |
| Render-blocking resources | LCP > 2.5s | Preload critical CSS, defer non-essential JS |
| Layout shifts | CLS > 0.1 | Set explicit dimensions on images/embeds |
| Slow interaction | FID > 100ms | Move heavy computation to web worker |
| Large images | Image > 100KB for thumbnails | Resize, compress, use WebP/AVIF, lazy load |

### Common Anti-Patterns

| Anti-Pattern | Problem | Reality |
|---|---|---|
| "Let's add Redis" | Treating symptoms, not cause | Find the bottleneck first — it's usually a missing index |
| "We need to rewrite in Rust" | Nuclear option for a local problem | Profile first, fix the hot path, then measure again |
| "Let's optimize everything" | Premature optimization | The slowest 10% of code causes 90% of latency — find it |
| "It feels slow" | No measurement | Measure. Feelings are not data. |
| "Let's add a CDN for our API" | CDNs cache static content | API responses are dynamic; a CDN won't help |
| Caching without invalidation | Stale data bugs | If you can't invalidate correctly, don't cache |

## Examples

**Example 1 — "The orders page takes 8 seconds":**

```
Step 1 — Measure: 
  Page load: 8.2s server-side, 200ms client-side
  Problem is server-side.

Step 2 — Profile:
  APM shows: 200 database queries per request
  Diagnosis: N+1 — ORM loads each order's items in a separate query

Step 3 — Fix:
  Changed: orders.findAll() → orders.findAll({ include: [OrderItems] })
  One query with JOIN replaces 200 queries.

Step 4 — Verify:
  Before: 8.2s (200 queries)
  After:  0.4s (1 query)
  Nothing else was touched.
```

**Example 2 — "Let's migrate to Redis because the app is slow":**

```
Step 1 — Measure:
  Dashboard endpoint: 3.2s response time
  
Step 2 — Profile:
  EXPLAIN ANALYZE on the main query: sequential scan on 2M rows
  No index on the WHERE clause columns
  
Step 3 — Fix:
  Added composite index: (tenant_id, created_at DESC)
  15 minutes of work.
  
Step 4 — Verify:
  Before: 3.2s (seq scan)
  After:  45ms (index scan)
  
  Redis proposal: rejected. No evidence supports it.
  Saved: weeks of Redis infrastructure work + ongoing maintenance.
```

## Verification

- [ ] Performance problem is measured and quantified (not "it feels slow")
- [ ] Bottleneck is identified with profiling data
- [ ] Fix targets only the identified bottleneck
- [ ] Before/after comparison shows measurable improvement
- [ ] No premature optimization (there's a real problem or breached budget)
- [ ] Cheap fixes exhausted before expensive ones
- [ ] No unnecessary infrastructure added (Redis, CDN, etc.) without evidence
