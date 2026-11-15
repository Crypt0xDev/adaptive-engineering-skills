---
name: ux-designer
description: Design simple user experiences centered on the value flow. Use before building any UI or when users report friction in existing flows.
---

# UX Designer

## Purpose

Design simple user experiences centered on the user's value flow — the shortest path from intent to outcome. The goal is usability, not aesthetics. Every screen and interaction must earn its place by helping the user complete their task faster.

## When to Use

- Designing new screens or user flows
- Users report friction in existing flows (high abandonment, confusion, support tickets)
- Before building any UI — design precedes code
- Evaluating whether a UI change improves or harms usability

## When NOT to Use

- Products without a user interface (APIs, CLIs, background jobs) — except for DX of their messages and docs
- Deep branding or visual identity decisions — that's a different discipline; this skill covers usability
- Aesthetic redesigns without a detected usability problem — don't redesign for taste
- When the UI is already validated and working well — don't change what works

## Expected Inputs

- The primary task the user wants to complete
- User profile and usage context (device, urgency, frequency, technical skill level)
- Technical constraints of the project
- Any existing data: analytics, support tickets, user feedback

## Expected Output

```
User flow: <step-by-step path from intent to outcome>
Screen descriptions: <what each screen shows and why>
States: <empty, loading, error, success for each screen>
Rationale: <why this design over alternatives>
```

## Internal Rules

### Core Principles

1. **The primary flow completes in the minimum number of steps.** Every additional step is friction. Every field, button, and screen must justify its existence.

2. **Familiar conventions over originality.** The user should never have to learn your interface. Use patterns they already know.

   | Instead of... | Use... | Why |
   |---|---|---|
   | Custom navigation | Standard sidebar/tabs | Users don't read instructions |
   | Clever icon-only buttons | Labeled buttons | Icons are ambiguous without text |
   | Novel form patterns | Standard form layouts | Muscle memory speeds completion |
   | Hidden gestures | Visible controls | Discoverability over cleverness |

3. **Every screen has four mandatory states.** Design all four — not just the happy path:

   | State | What it shows | Design requirement |
   |---|---|---|
   | **Empty** | No data yet | Clear call-to-action to start |
   | **Loading** | Data is being fetched | Skeleton or spinner, never a blank screen |
   | **Error** | Something went wrong | What happened + what the user can do about it |
   | **Success** | Task completed | Confirmation + clear next step |

4. **Accessibility is not optional.** These are minimums, not extras:
   - Color contrast ratio ≥ 4.5:1 for text (WCAG AA)
   - Visible focus indicators for keyboard navigation
   - Labels on all form inputs (not just placeholders)
   - Touch targets ≥ 44x44px on mobile
   - Screen reader compatibility (semantic HTML, ARIA where needed)

5. **Mobile-first when context indicates.** If users will use it on phones, design for phones first and scale up.

### The Design Process

```
1. Identify the primary task    → What is the ONE thing the user came here to do?
2. Map the shortest flow        → Minimum steps from intent to outcome
3. Design the minimum UI        → Only what the user needs at each step
4. Add all four states          → Empty, loading, error, success
5. Test with real context       → Device, environment, user skill level
6. Iterate with feedback        → Real user behavior, not assumptions
```

### Information Hierarchy

On every screen, answer: "What does the user need FIRST?"

```
1. Primary action / critical information   → Most prominent, top-left or center
2. Supporting context                      → Visible but secondary
3. Secondary actions                       → Available but not competing
4. Metadata and admin info                 → Bottom, collapsed, or separate screen
```

### Form Design Rules

| Rule | Example |
|---|---|
| Ask only what you need right now | Registration: email + password only; ask for name later |
| Group related fields | Shipping address fields together, billing together |
| Use appropriate input types | Date picker for dates, dropdown for <7 options, autocomplete for >7 |
| Show validation inline, in real time | "Password must be 8+ characters" as the user types |
| Pre-fill when possible | Default country from locale, repeat last-used address |
| One primary action per form | One "Submit" button, not three competing CTAs |

### Common UX Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Confirmation dialogs for reversible actions | "Are you sure?" fatigue | Let users undo instead of asking permission |
| Modal on top of modal | Cognitive overload | Redesign the flow to avoid stacking |
| Required fields not marked | User submits, gets errors, loses trust | Mark required fields from the start |
| Disabled buttons without explanation | User doesn't know why they can't proceed | Show a tooltip or inline hint explaining what's missing |
| Infinite scroll for important lists | User can't find items, can't bookmark position | Add pagination or search/filter |
| Success without confirmation | User wonders "did it work?" | Always confirm the action succeeded |

## Examples

**Example 1 — Registration form with 12 fields and 40% abandonment:**

```
Analysis: Only email and password are needed to start. The other 10 fields 
          can be collected progressively when the product needs them.

Before: 12-field form → 40% abandonment
After:  2-field form (email + password) → progressive profiling

Flow:
  1. User enters email + password → account created
  2. First use: "What's your name?" (one field, skippable)
  3. First purchase: "Shipping address?" (collected in context)
  
Result: Reduced form to 2 fields. Remaining data collected when the user 
        understands WHY it's needed (in context, not upfront).
```

**Example 2 — Dashboard for factory operators:**

```
Context: Tablets, gloves, variable lighting, high-urgency decisions.

Design decisions:
  - Touch targets: 64x64px minimum (operators wear gloves)
  - Contrast: WCAG AAA (variable factory lighting)
  - Critical metric: top-left, largest element on screen
  - No hover states (touch only)
  - Alarm state: full-screen red with large "Acknowledge" button
  - Font size: minimum 18px (readability at arm's length)
  
States:
  - Empty: "No active alerts — system normal" with green indicator
  - Loading: Skeleton with last-known values (never blank)
  - Error: "Connection lost — showing data from [time]" with retry button
  - Alarm: Full-screen alert with one-tap acknowledgment
```

## Verification

Before approving a design:

- [ ] Primary flow completes in minimum steps — no unnecessary screens or fields
- [ ] All four states designed: empty, loading, error, success
- [ ] Familiar conventions used — no novel patterns without strong justification
- [ ] Accessibility minimums met: contrast, focus, labels, touch targets
- [ ] Mobile-first if context requires it
- [ ] Information hierarchy is clear: primary action/info is the most prominent
- [ ] Forms follow progressive disclosure: only what's needed now
- [ ] Error states tell the user what happened AND what to do
