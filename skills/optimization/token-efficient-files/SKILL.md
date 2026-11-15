---
name: token-efficient-files
description: "Mandatory token-saving strategy for reading or generating PDF, Word (.docx), Excel (.xlsx), and PowerPoint (.pptx) files. Use ALWAYS when the user uploads, mentions, or asks to analyze/summarize/read a pdf, word, excel, or ppt file — especially long, unstructured university papers. Also when generating or editing these formats. Applies BEFORE format-specific skills (docx/pdf/pptx/xlsx): defines HOW to read/edit them cheaply, not how to format them."
---

# Token-Efficient File Processing (PDF / Word / Excel / PPT)

## Purpose

Minimize token consumption when reading or generating document files without losing context. A long university PDF can contain 20-50k+ tokens of plain text; reading it entirely when only one section is needed wastes the context window. This skill enforces a two-step approach: cheap overview first, targeted deep-dive only where needed.

## When to Use

- Any time the user uploads, mentions, or asks to analyze/summarize/read a PDF, Word, Excel, or PowerPoint file
- Especially with long, unstructured documents (university papers, reports without clear headings)
- When generating or editing these formats across multiple iteration rounds
- Before invoking format-specific skills (`docx`, `pdf`, `pptx`, `xlsx`)

## When NOT to Use

- The file is short (2-3 pages, a single small sheet, a few slides) — overview and deep-dive collapse into one step
- The user explicitly asks to read the entire file and context window allows it
- Working with code files, markdown, or plain text — those are cheap to read directly

## The Process

### Step 1 — Cheap Overview (Mandatory, Always First)

Extract ONLY structural information — never the full text:

| File Type | What to Extract | What NOT to Do |
|-----------|----------------|----------------|
| **PDF** | Page count + first lines of each page/major block to detect section boundaries. Use text extraction for selectable PDFs; OCR only for scanned documents. | Don't dump all pages as plain text |
| **Word (.docx)** | List of headings/titles (if styled). Without structure: first line of each long paragraph to build an approximate map. | Don't convert the entire document to text |
| **Excel (.xlsx)** | Sheet names + dimensions (rows × columns) + headers + 2-3 sample rows per sheet. | Don't load all rows |
| **PowerPoint (.pptx)** | Slide title + first line of notes (if any). | Don't extract the full body of every slide |

With this structural overview, produce a brief summary (a few lines per page/section/sheet/slide) and present it.

### Step 2 — Targeted Deep-Dive (Only If Needed)

After the overview, determine which part needs full extraction:

| Scenario | Action |
|----------|--------|
| User's request is specific ("summarize the conclusion", "give me the Sales sheet") | Extract that section directly — skip the question |
| Request is broad ("what does this say?") | Ask which section to focus on, based on the overview |
| User says "the whole thing" | Extract in chunks, processing section by section — not all at once |

**Only extract full text/data from the specific section, sheet, or slides needed — not the entire file.**

### Exception: Short Files

If the file is short (few pages, one small sheet, few slides), the overview and deep-dive collapse into a single step. Don't add bureaucracy to a 2-page PDF.

## Generation and Editing Rules

For format and content, use the corresponding skills (`docx`, `pdf`, `pptx`, `xlsx`). This skill adds token discipline around them:

| Situation | Rule |
|-----------|------|
| Editing an already-generated file | Don't re-read it entirely to verify a small change. Use targeted search (grep / string replacement with bounded context), not full `view`. |
| Need to confirm structure before editing | Apply Step 1 (cheap overview) — what headings exist, what columns a sheet has |
| Iterating across multiple feedback rounds on a long document | Don't re-read the full document each round. Keep what's already extracted in context; request only the delta. |

## What NOT to Do

| Anti-Pattern | Why It's Wasteful |
|-------------|-------------------|
| `cat`/`view` without a range on a large file "to review everything" | Burns thousands of tokens on content you won't use |
| Converting the entire document to plain text for a targeted question | "What does page 5 say?" doesn't need pages 1-4 and 6-50 |
| Re-extracting a file already read in the same thread | The extracted content is already in context |
| Using OCR on PDFs that already have selectable text | OCR is slower, less accurate, and more expensive for text-native PDFs |

## Decision Flowchart

```
File received
    │
    ├─ Short file (< ~5 pages / 1 sheet / ~5 slides)?
    │   └─ YES → Read directly in one pass
    │   └─ NO ↓
    │
    ├─ Step 1: Cheap overview (structure only)
    │   └─ Present summary to user
    │
    ├─ Is the request already specific?
    │   └─ YES → Extract only that section
    │   └─ NO → Ask what to focus on
    │
    └─ Step 2: Targeted deep-dive on selected section(s)
```

## Examples

**Example 1 — 45-page university thesis PDF:**
User asks: "Summarize the methodology."
→ Step 1: Extract page count + first lines to find section boundaries. Identify that "Methodology" starts on page 12.
→ Step 2: Extract pages 12-18 only. Summarize that section.
→ Cost: ~3k tokens instead of ~40k for the full document.

**Example 2 — Excel workbook with 8 sheets:**
User asks: "What's in this Excel?"
→ Step 1: Sheet names + dimensions + headers + 2 sample rows each. Present the overview.
→ User says: "I need the Revenue sheet."
→ Step 2: Extract the Revenue sheet fully.

**Example 3 — 3-page PDF:**
User asks: "Read this PDF."
→ Short file → read directly in one pass. No two-step process needed.

## Related Skills

- **academic-writing** — when the file being read is a source for academic writing, this skill handles cheap reading; that skill defines how to cite it.
- **docx / pdf / pptx / xlsx** — for output formatting; this skill decides how much to read before invoking them.
