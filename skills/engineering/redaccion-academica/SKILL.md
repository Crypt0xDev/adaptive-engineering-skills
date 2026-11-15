---
name: redaccion-academica
description: "Writes, improves, and structures academic documents — reports, theses, monographs, theoretical frameworks, essays, and technical papers — with natural academic language, correctly placed citations, verified real sources, and recent relevant bibliography. Supports APA, IEEE, Vancouver, ISO 690, and other standards. Use ALWAYS when asked to write, expand, correct, or improve academic text that requires citations and references."
---

# Academic Writing

## Purpose

Write, improve, and structure academic documents with natural academic language, correctly placed citations from verified real sources, and recent relevant bibliography. Every claim that needs backing must be traceable to a real, pertinent source — or explicitly flagged as needing one.

## When to Use

- Writing or expanding academic texts: reports, theses, monographs, essays, literature reviews, theoretical frameworks
- Improving or correcting existing academic writing
- Adding citations and references to a document
- Any task where the user needs text with proper academic sourcing

## When NOT to Use

- Blog posts, marketing copy, or informal writing — those don't need academic rigor
- Technical documentation for software (that's `documentation-and-adrs`)
- When the user explicitly says they don't need citations

## The Process

### Step 1 — Declare the Framework Before Writing

Before starting any academic writing, establish and briefly state:

| Parameter | Action |
|-----------|--------|
| **Citation standard** | Use the one the user specifies. If not specified, ask which their course or institution requires. Don't default to APA. |
| **Text language** | Use the language the user requests |
| **Source language** | Note whether only sources in one language or also sources in English/other languages will be used |
| **Source origin** | Note whether working with user-provided sources or sources found and verified through external search |

After this declaration, proceed with writing.

### Step 2 — Write With Real, Verified Sources

#### The Absolute Rule: Never Fabricate Bibliographic Information

It is strictly prohibited to fabricate:

- Authors, titles, publication years, publishers, journals
- Volumes, issue numbers, pages, DOIs, URLs
- Institutions, statistics, research results
- Direct quotes, bibliographic references

**A reference may only be included if:**
1. It was provided by the user, OR
2. It was found through a real search and can be verified

Do not create references just because they "look academic."

If a claim needs backing and no verified source exists, search for an appropriate source first. If none is found, rephrase the claim or explicitly note it needs an additional source.

#### Source Verification Checklist

When sources are found externally, verify each one:

- [ ] The source actually exists
- [ ] The author or responsible institution is confirmed
- [ ] The publication year is confirmed
- [ ] The title is confirmed
- [ ] The content actually supports the claim being made
- [ ] DOI or URL has been verified (don't guess them)
- [ ] The source isn't cited just because it contains similar keywords
- [ ] The source isn't used to support a claim it doesn't actually demonstrate

**A source's existence doesn't make it adequate. Content relevance is mandatory.**

#### Source Recency

| Rule | Detail |
|------|--------|
| Default | Sources from the **last 5 years** relative to the current year |
| User override | If the user specifies a different period, respect it |
| Exceptions | Foundational, normative, classic, historical, or theoretical sources — and sources indispensable to explain a concept's origin |

When using an older source for one of these reasons, briefly note why. Don't use old sources simply because they're easy to find.

#### Source Priority (Descending)

1. Peer-reviewed scientific articles
2. Official institutional documents
3. Technical standards and normative documents
4. Academic books
5. Theses and reliable university repositories
6. International organization publications
7. Official technical documentation

Avoid blogs, commercial pages, content without authorship, and low-quality sites when a better academic or institutional source exists.

### Step 3 — Place Citations Correctly

#### Citation Relevance

Each citation must specifically justify the claim it accompanies. Do not add citations:

- As filler
- Just to increase the reference count
- Because a source "seems related"
- At the end of a full paragraph when the source only supports one sentence
- To appear more academically rigorous

If a paragraph contains ideas from different sources, distribute citations accordingly:

```
CORRECT:
Cloud computing enables on-demand access to computing resources (Author, 2024).
Additionally, its adoption can reduce certain costs associated with physical
infrastructure (Author, 2023).

INCORRECT:
Cloud computing enables on-demand access to computing resources. Additionally,
its adoption can reduce costs (Author, 2024; Author, 2023).
← Both references dumped at the end when each supports a different claim
```

#### Citation Forms

| Type | When | Example |
|------|------|---------|
| **Narrative** | The author is part of the sentence | According to García (2023), technology adoption modifies organizational processes. |
| **Parenthetical** | Emphasis is on the information | Technology adoption can modify organizational processes (García, 2023). |

#### Author Count (APA 7 — adjust for the requested standard)

| Authors | Form |
|---------|------|
| One | Name in every citation: (García, 2023) |
| Two | Both always. Parenthetical with "&": (García & López, 2023). Narrative with "and"/"y": García and López (2023) |
| Three or more | First author + "et al." **from the first citation**: (García et al., 2023) |
| No author | Abbreviated title in author position |
| No date | "n.d." (English) or "s.f." (Spanish) |

#### Direct Quotes

| Type | Rule (APA 7) |
|------|-------------|
| Short quote (<40 words) | In quotation marks, within the paragraph, with page number |
| Block quote (≥40 words) | Separate paragraph, indented, no quotation marks. Prefer paraphrasing unless the exact wording is essential |

**Never present as a direct quote a phrase that hasn't been verified directly in the source. Never fabricate page numbers.**

> The above follows APA 7. Exact placement, punctuation, brackets, and numbering must be adjusted to the requested standard (IEEE uses bracketed numbers, Vancouver uses numbered references, ISO 690 its own format). When unsure about a specific standard, verify its official format before applying it.

### Step 4 — Maintain Quality Throughout

#### Natural Academic Language

The text should read like a university paper written by a person — maintaining academic formality without artificial or overly ornamental expressions.

Avoid repetitive expressions characteristic of AI-generated text:

| Avoid | Instead |
|-------|---------|
| "in today's rapidly evolving world" | State the specific context |
| "it is worth noting that" | Just state the point |
| "plays a fundamental/crucial role" | Describe the specific impact |
| "without a doubt" | Let the evidence speak |
| "in conclusion, we can affirm that" | Write a substantive conclusion |
| "in this context, it is essential to" | Get to the point |

Don't replace these with artificial synonyms. The priority is writing naturally.

#### Avoid Generic Content

Every paragraph must contribute information directly related to the topic. Do not include:

- Unnecessary definitions
- Background that doesn't contribute to the topic
- Obvious statements or repetitions
- Conclusions that merely restate what came before
- Information unrelated to the work's objective

Length should depend on the amount of necessary information, not an arbitrary word count.

#### Coherence and Uniformity

Maintain throughout the document:

- The same terminology (don't use different terms for the same concept just to avoid repetition)
- The same level of formality
- The same grammatical person
- Logical structure with natural transitions
- Consistency in citations and references

#### No Shallow Paraphrasing

When an idea comes from a source, don't just change a few words from the original. Understand the information and express it in your own structure while maintaining the original meaning and correctly citing the source. Don't present a source's specific idea as your own knowledge.

#### Citation Count

There is no artificial citation count to meet. The quantity depends on:

- Topic complexity
- Number of claims requiring backing
- Availability of relevant sources
- Type of work requested

Fewer but directly relevant sources are better than a document padded with irrelevant references. Where possible, combine different quality academic sources to support the main arguments.

## Verification Checklist

Before delivering the work:

- [ ] Citation standard was declared
- [ ] Text and source languages were indicated
- [ ] Source origin was indicated
- [ ] No fabricated authors or references exist
- [ ] All references used actually exist
- [ ] Sources were verified for existence AND relevance
- [ ] Bibliography meets the requested recency threshold
- [ ] Older source exceptions are justified
- [ ] Each citation directly supports its corresponding claim
- [ ] Citations are correctly placed (not dumped at paragraph end)
- [ ] No filler citations exist
- [ ] No fabricated pages, DOIs, or URLs
- [ ] No shallow paraphrasing of sources
- [ ] Text avoids generic content
- [ ] Language is natural and academic
- [ ] Terminological and structural coherence throughout
- [ ] References match exactly the sources cited in the text
- [ ] No unused references in the bibliography
- [ ] No repetitive AI-characteristic expressions

## Fundamental Principle

**The priority is not producing many pages or many citations. The priority is producing a solid, specific, coherent, natural, and verifiable academic text where every important claim can be traced to a real, pertinent source.**

## Related Skills

- **ahorro-tokens-archivos** — when sources or assignments come in PDF/Word, that skill handles cheap reading before writing.
