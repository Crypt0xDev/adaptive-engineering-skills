---
name: graphql-evaluacion-implementacion
description: "Evaluates whether GraphQL is appropriate for a project (vs REST or alternatives) before implementing it, and if warranted, implements it with proper structure, security (input sanitization, query depth/complexity limits, per-resolver authorization), and clean code. Use ALWAYS when GraphQL is mentioned, a GraphQL API is requested, or GraphQL vs REST is being discussed, in any stack. Applies the criteria from decisiones-tecnicas-fundamentadas and the structure from buenas-practicas-ingenieria to the GraphQL case."
---

# GraphQL Evaluation and Implementation

## Purpose

Evaluate whether GraphQL is the right choice for a project before implementing it, and if it is, implement it with proper structure, security, and clean code. GraphQL is not a default — it's a tool for specific problems. This skill prevents cargo-cult adoption and ensures secure implementation when GraphQL is warranted.

## When to Use

- Any time GraphQL is mentioned or a GraphQL API is requested
- When discussing GraphQL vs REST (or other API styles)
- When evaluating whether to add GraphQL to an existing project
- When implementing a new GraphQL API
- Any stack — Node.js, Python, Go, Java, .NET, etc.

## When NOT to Use

- Building a straightforward REST API where GraphQL was never mentioned and there's no over/under-fetching problem
- The API style decision is already made and the user just wants implementation help — skip to Step 2

## The Process

### Step 1 — Evaluate Whether GraphQL Is Warranted (Always First)

Never implement GraphQL just because it was mentioned. Apply the same criteria as `decisiones-tecnicas-fundamentadas`:

#### 1.1 — Diagnose the Concrete Project

| Question | Why It Matters |
|----------|---------------|
| How many entities? How many clients consume the API? | Low complexity = REST is simpler |
| Is there real over-fetching/under-fetching? (`?include=`, `?fields=`, multiple chained calls to assemble a view) | This is GraphQL's core value proposition |
| What's the team's GraphQL experience? | Zero experience = significant maintenance cost |
| What stage? (prototype/MVP vs. long-term system) | MVP with uncertain domain = don't add complexity |
| What's the actual pain point? | "Should I use GraphQL?" is often a solution looking for a problem |

If any data point is in doubt, ask before assuming.

#### 1.2 — Decision Signals

**Signals FOR GraphQL:**

| Signal | Why |
|--------|-----|
| Client needs variable combinations of nested data | Different views request different subsets of the same resource |
| Real over/under-fetching with the current REST API | The problem GraphQL was designed to solve |
| Multiple clients (web, mobile, admin) with different data needs | One flexible API vs. multiple rigid endpoints |
| Long-term project with evolving data requirements | Investment in schema design pays off over time |

**Signals AGAINST (stay with REST or simplify):**

| Signal | Why |
|--------|-----|
| Simple CRUD, few entities, single client | REST covers everything with less complexity |
| Small project / MVP / proof of concept | REST is working fine; don't add complexity |
| Team has no GraphQL experience and no time to learn | Resolvers, N+1, different caching model = maintenance burden |
| REST is working well and migrating doesn't solve a concrete problem | Don't migrate for trends |

#### 1.3 — Confirm Before Implementing

- Summarize the diagnosis and conclusion in 3-5 lines, with project-specific reasoning
- If the decision is "yes", state it as a recommendation and wait for confirmation before writing code (unless the user already asked unambiguously)
- If any data couldn't be verified, say so

### Step 2 — Design With Proper Structure

Apply `buenas-practicas-ingenieria` (SOLID with judgment, no over-engineering). GraphQL-specific:

| Principle | Implementation |
|-----------|---------------|
| **Separate layers** | Schema/types, resolvers, and business logic (services) in separate files. Resolvers orchestrate — they don't contain business logic or direct SQL. |
| **Schema-first vs. code-first** | Follow what the stack already uses. For new projects, schema-first gives a clear contract between frontend and backend. |
| **Domain naming** | Name types and fields after the domain, not mirroring database tables. |
| **Pagination from the start** | Connection/cursor-based pagination is the GraphQL standard for lists. Prefer it over offset-based. |
| **Consistent errors** | Don't expose stack traces or raw DB error messages. Use structured error responses. |

```graphql
# GOOD: Domain-oriented schema with pagination
type Query {
  orders(first: Int!, after: String): OrderConnection!
  customer(id: ID!): Customer
}

type OrderConnection {
  edges: [OrderEdge!]!
  pageInfo: PageInfo!
}

# BAD: Database-mirroring schema without pagination
type Query {
  orders: [Order!]!      # Returns ALL orders — no pagination
  tbl_customers(pk: Int!): TblCustomer  # Exposes DB naming
}
```

### Step 3 — Security and Reliability

These are not optional. Each one prevents a specific, well-known attack vector:

| Protection | What It Does | Why It's Necessary |
|------------|-------------|-------------------|
| **Input sanitization** | Validate and sanitize all inputs in resolvers before passing to the data layer | GraphQL doesn't exempt you from input validation — same rules as REST |
| **Query depth limiting** | Reject operations BEFORE execution if nesting exceeds a threshold. Apply a stricter limit to nested lists (exponential growth). | Prevents deeply nested queries from consuming unbounded resources |
| **Query cost/complexity analysis** | Assign weights to types and fields; reject queries exceeding a maximum cost | Depth alone doesn't capture cost — a shallow query can still be expensive |
| **Rate limiting at the business logic layer** | Count operations per time window at the resolver/service level, not just HTTP level | The client chooses fields, so the server can't know request cost at the network layer |
| **Introspection in production** | Can disable for proprietary APIs, BUT the official graphql.org guide calls this "security by obscurity" — it's NOT sufficient alone. Combine with real authorization and hidden detailed error messages (attackers can infer schema from errors). | Introspection alone is a weak defense |
| **Per-resolver/per-field authorization** | Authorize at the resolver or field level, not just the single endpoint | One GraphQL endpoint exposes many sub-accesses — endpoint-level auth is insufficient |
| **Batch limiting** | Cap operations per batch AND aliases of the same field per operation (`friends1`, `friends2`… `friends100`) | Both are abuse vectors for resource exhaustion |
| **N+1 resolution** | Use data batching (DataLoader pattern) from the design, not as a patch | N+1 is the #1 GraphQL performance issue; it must be solved structurally |
| **Timeouts + HTTPS** | Request timeouts and encrypted transport | Standard baseline |
| **Explicit field exposure** | Every schema field is a deliberate decision about what to expose — not an automatic reflection of the data model | Prevents accidental exposure of sensitive data or relationships |

> When implementing, if there's any doubt about the exact syntax or guarantees of the GraphQL library for the stack (graphql-js, Strawberry, Apollo, Ariadne, gqlgen, etc.), verify against its official documentation before asserting. Official docs > blog posts.

### Step 4 — Clean Code

| Rule | Detail |
|------|--------|
| Consistency | Follow the project's existing naming, folder structure, and error handling conventions |
| Tests | At minimum, test resolvers that handle authentication, payments, and sensitive data |
| Schema documentation | Add descriptions to types and non-obvious fields |
| No dead schema | Remove fields and types that are no longer used |

```typescript
// GOOD: Resolver orchestrates, business logic is separate
const resolvers = {
  Query: {
    orders: (_, args, { dataSources }) =>
      dataSources.orderService.getOrders(args),
  },
};

// BAD: Business logic and SQL in the resolver
const resolvers = {
  Query: {
    orders: async (_, args) => {
      const result = await db.query(
        `SELECT * FROM orders WHERE user_id = ${args.userId}` // SQL injection + logic in resolver
      );
      return result.rows;
    },
  },
};
```

## Verification Checklist

- [ ] GraphQL was evaluated and justified as necessary (not "because it's cool")
- [ ] Resolvers are separated from business logic
- [ ] Depth limiting is active (with a stricter limit for nested lists)
- [ ] Cost/complexity analysis is active
- [ ] Introspection is treated as a weak layer, backed by real authorization and hidden error details
- [ ] Authorization is checked per resolver, not just per endpoint
- [ ] N+1 is resolved with batching/DataLoader where applicable
- [ ] Batch and alias limits are in place
- [ ] Inputs are sanitized just like in REST
- [ ] Pagination is implemented from the start for all list queries
- [ ] Schema uses domain naming, not database table names

## Related Skills

- **decisiones-tecnicas-fundamentadas** — Step 1 is a concrete application of that skill.
- **buenas-practicas-ingenieria** — Steps 2-4 inherit its structure, naming, and scaling rules.
