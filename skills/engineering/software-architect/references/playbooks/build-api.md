# Playbook: Build API

## Skills Involved
`business-analyst` → `software-architect` → `database-architect` → `security-engineer` → `performance-engineer`

## Phases

### 1. Contract First
- Define resources, endpoints, and formats before coding.
- REST by default; GraphQL only if clients have highly variable query needs.
- Version from the start (`/v1/`).

### 2. Design
- Consistent conventions: plural names, correct status codes, errors with a unified format.
- Pagination on every collection from day one.
- Generated documentation (OpenAPI/Swagger).

### 3. Security (security-engineer)
- Auth per consumer: API keys (server-to-server) or OAuth2/JWT (users).
- Rate limiting if public.
- Strict input validation on every endpoint.

### 4. Operations
- Structured logs with request-id.
- Healthcheck endpoint.
- Contract tests for critical endpoints.

## What NOT to Do at the Start
Complex gateway, GraphQL "just in case", microservices per resource, distributed cache without measurement.
