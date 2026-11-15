# Playbook: Build Dashboard

## Skills Involved
`business-analyst` → `ux-designer` → `database-architect` → `performance-engineer`

## Phases

### 1. Metrics First (business-analyst)
- Define what decisions the user will make with the dashboard.
- Every chart must answer a concrete business question; if not, remove it.

### 2. Build or Use BI?
- Internal use and data in SQL → consider Metabase / Grafana / Looker Studio before building.
- Build only if it's customer-facing or needs custom interaction.

### 3. UX (ux-designer)
- Most important content top-left.
- Few charts with meaning > many decorative charts.
- Empty states and sensible default date ranges.

### 4. Data (database-architect + performance-engineer)
- Direct queries with indexes while volume allows.
- Precalculated aggregations (materialized views) only when queries hurt.
- Result caching with short TTL before dedicated analytics infrastructure.

## What NOT to Do at the Start
Data warehouse, ETL pipelines, real-time via WebSockets — until volume or business demands it.
