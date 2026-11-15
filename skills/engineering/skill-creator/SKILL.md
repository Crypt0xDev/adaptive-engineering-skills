---
name: skill-creator
description: Design and maintain the system's skills with a modular standard. Use when creating or modifying a skill.
---

# Skill Creator (Skill Development Expert)

## Purpose

Design and maintain the system's skills. This is the meta-skill — it defines the standard every skill must meet. Anyone developing skills works in this mode.

## When to Use

- Creating a new skill for the system
- Modifying or refactoring an existing skill
- Auditing skills for standard compliance
- Detecting and merging skills with duplicate logic

## When NOT to Use

- Solving the domain problem directly — the corresponding skill does that, not this one
- Creating a skill for a one-time occurrence — wait for the pattern to repeat (rule of three)
- General project documentation — that goes in README or in the relevant skill's `references/`

## Expected Inputs

- The recurring capability or problem the skill should cover
- The context where it will be used (project types, stages)
- Existing skills (to verify no overlap)

## Expected Output

A folder `skills/<category>/<kebab-case-name>/` with a `SKILL.md` that meets the mandatory structure (see template below). The frontmatter `name` matches the folder name, the `description` says what it does and when to use it (Claude decides activation based on this line), and the skill is added to the README table. CI verifies all three.

## Internal Rules

### When Creating Any Skill, ALWAYS:

1. **Single responsibility.** One skill = one capability. If describing it requires "and", it's two skills.

2. **Clear, descriptive names.** The name says what it does (`security-engineer`, not `helper`).

3. **No logic duplication.** If another skill already covers part of the functionality, reference it (`see skills/<category>/x/`), don't copy it.

4. **Low coupling.** A skill references others by name, never depends on their internal details.

5. **Small, specific sections.** Processes of 3-6 steps. If a process grows beyond that, the skill covers too much.

6. **Contextual design.** Every skill includes when NOT to use it — a skill without contraindications is poorly designed.

7. **Maintainability first.** A new reader should understand the skill in 5 minutes.

### When Creating Any Skill, NEVER:

- Apply extra patterns or structure without real need (no over-engineering)
- Create unnecessary dependencies between skills
- Leave the purpose ambiguous or overlapping with another skill
- Write sections with no concrete content (no filler)

### The Design Process

```
1. Analyze the goal       → What recurring capability does it cover? Does another skill already do this?
2. Understand the context → What project types and stages will it activate in?
3. Define responsibility  → One phrase, no "and"
4. Design clear structure → Complete the template with no empty or filler sections
5. Optimize for reuse     → Remove anything specific to a single project
```

### Quality Checklist for New Skills

| Check | Pass | Fail |
|---|---|---|
| Can you describe it in one sentence without "and"? | Single responsibility | Too broad — split it |
| Does it have "When NOT to Use"? | Well-designed | Missing contraindications |
| Does the name say what it does? | Self-documenting | Rename it |
| Does the description trigger Claude correctly? | Will activate when needed | Rewrite the description |
| Does it overlap with an existing skill? | Unique contribution | Merge or reference the other |
| Can a new reader understand it in 5 minutes? | Maintainable | Simplify it |

## Mandatory Template

```markdown
---
name: <kebab-case-name>
description: <What it does. Use when ...>
---

# <Skill Name>

## Purpose
<One sentence: what capability it covers and why>

## When to Use
<Concrete triggers>

## When NOT to Use
<Contraindications and limits — mandatory>

## Expected Inputs
<What context/information it needs to activate>

## Expected Output
<Concrete format of the result it produces>

## Internal Rules
<The rules the skill applies, aligned with system principles>

## Examples
<1-2 brief examples: situation → how the skill acts → result>
```

### Frontmatter Rules

- `name`: must match the folder name exactly, kebab-case
- `description`: one line that tells Claude when to activate this skill. This is the most important line — Claude reads it to decide whether to invoke the skill. Be specific about the trigger context.

## Examples

**Example 1 — Creating a new skill:**

Situation: The system needs to evaluate web accessibility as a recurring capability.

```
1. Check overlap → ux-designer covers usability but not WCAG compliance audits
2. Define responsibility → "Audit accessibility against WCAG standards"
3. Name → accessibility-auditor
4. Create skills/<category>/accessibility-auditor/SKILL.md using the template
5. Add to README table
6. "When NOT to Use": CLIs, APIs without UI, internal admin tools
```

Result: New skill with no overlap, clear contraindications, single responsibility.

**Example 2 — Rejecting an unnecessary skill:**

Situation: Someone proposes a "JSON validator" skill.

```
Analysis: JSON validation is a one-off task, not a recurring engineering capability.
Decision: Don't create it. Solve it with a standard function in the project that needs it.
Rule: The rule of three — wait for the pattern to repeat.
```

**Example 3 — Merging overlapping skills:**

Situation: Two skills share >50% of their rules.

```
Analysis: skill-A covers "API design" and skill-B covers "API review"
Overlap: both define the same API quality rules
Decision: Merge into one skill or have skill-B reference skill-A's rules
Rule: If two skills share more than half their rules, merge them
```

## Maintenance

- A skill unused for 3 months is deleted or merged — the system avoids over-engineering itself
- If two skills share more than half their rules, merge them
- Review skills after major system changes — some may be obsolete
