# Playbook: Build E-commerce

## Skills Involved
`business-analyst` → `product-manager` → `software-architect` → `security-engineer` → `performance-engineer`

## Phase 0 — Build or Use a Platform?
- Standard catalog → **Shopify / WooCommerce**. Don't build.
- Build only if the sales model is genuinely atypical or e-commerce is the core business differentiator.

## If Building

### 1. Minimum Domain
Catalog → cart → checkout → order → payment. Nothing else in v1.

### 2. Payments (security-engineer)
- Stripe / local provider. **Never touch card data** (PCI via provider).
- Idempotency on order creation and payment webhooks.

### 3. Data (database-architect)
- PostgreSQL; prices in integers (cents); immutable orders (price snapshots).
- Inventory with concurrency control (don't sell what you don't have).

### 4. Performance (performance-engineer)
- The catalog is read-intensive: cache product pages when there's real traffic.
- Optimized images via CDN.

## What NOT to Do at the Start
Recommendation engine, multi-currency, multi-warehouse, marketplace — until the business asks for it.
