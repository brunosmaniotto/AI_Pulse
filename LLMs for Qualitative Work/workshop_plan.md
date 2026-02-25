# LLMs for Qualitative Work — Workshop Plan

## Overview

**Series**: D-Lab AI Pulse, Spring 2026
**Session**: 4 (March 10, 2026)
**Duration**: ~50 minutes (30 min demo + 20 min discussion)
**Audience**: UC Berkeley students, staff, and faculty doing qualitative research

---

## The Hook

Qualitative researchers face a tension: AI promises to speed up tedious tasks like transcription and initial coding, but qualitative work is fundamentally about human interpretation — meaning, context, nuance. This session explores where LLMs genuinely help, where they fall short, and how to use them without compromising research quality.

---

## Session Outline (~50 min)

### Part 1: The Landscape (5 min)

Where AI meets qualitative research today:
- Transcription and interview processing
- Initial coding and theme suggestion
- Literature synthesis and memo drafting
- Pattern identification across large datasets

Key finding from 2025 research: LLMs perform well at deductive analysis (applying pre-defined codes) but struggle with inductive analysis (discovering new themes from data). They're analytical scaffolding, not analysts.

The COREQ+LLM reporting standard (in development) — what journals will expect you to document about AI use.

### Part 2: Live Demos (20–25 min)

#### Demo 1: Transcription to Themes (8 min)
**Tool**: ChatGPT or Claude
- Upload a sample interview transcript
- Prompt: "Read this interview transcript. Identify the 5 most prominent themes, with a supporting quote for each."
- Show how different prompts yield different results (prompt sensitivity)
- Then: "Now code every paragraph according to these themes"
- Discuss: What did it get right? What did it miss?

#### Demo 2: Deductive Coding at Scale (7 min)
**Tool**: Claude
- Pre-define a codebook (e.g., 8 codes with definitions)
- Upload 3–4 interview excerpts
- Prompt: "Apply this codebook to the following excerpts. For each excerpt, assign all relevant codes and explain your reasoning."
- Compare AI coding to "ground truth" human coding
- Key point: Deductive coding is where LLMs shine — they apply existing frameworks consistently

#### Demo 3: ATLAS.ti AI Features (5 min)
**Tool**: ATLAS.ti (web version)
- Show the AI-assisted coding workflow in a dedicated QDA platform
- AI code suggestions, conversational inquiry feature
- Compare to the "raw LLM" approach in Demos 1–2
- When does a dedicated platform add value vs. just using ChatGPT?

#### Demo 4: The Hallucination Problem (5 min)
**Tool**: ChatGPT or Claude
- Ask the LLM to generate quotes supporting a theme
- Cross-check against the original transcript
- Show a fabricated quote that sounds plausible but doesn't exist in the data
- Key takeaway: Always verify AI-generated quotes against raw data

### Part 3: Best Practices (5 min)

When to use LLMs in qualitative work:
- Transcription and cleanup
- First-pass deductive coding with a pre-defined codebook
- Generating memo drafts and summaries
- Exploring patterns across large datasets
- Literature synthesis

When NOT to use LLMs:
- As your only coder (always validate)
- For inductive theme discovery without human refinement
- With sensitive/identifiable data on commercial platforms (use local models — see Session 6)
- As a shortcut to avoid engaging deeply with your data

Documentation checklist:
- Which model and version you used
- At what stage of analysis
- What prompts you gave
- How you validated the output
- What you changed after human review

### Discussion (15–20 min)

Suggested prompts:
1. Does AI-assisted coding change what qualitative research IS? If a machine helps identify your themes, is it still YOUR interpretation?
2. Data privacy: Would you upload interview transcripts with identifiable information to ChatGPT? Where's the line?
3. The speed trap: AI makes first-pass coding 80% faster. Is that a good thing, or does slowness serve a purpose in qualitative work?
4. Graduate students: If your advisor says "just run it through ChatGPT first," what do you do?
5. IRB implications: Should informed consent forms mention AI-assisted analysis?

---

## Tools Mentioned

| Tool | What it does | Pricing |
|------|-------------|---------|
| ChatGPT | General-purpose LLM, qualitative coding, theme generation | Free tier available |
| Claude | Lower hallucination rates, good for dense documents | Free tier (limited) |
| ATLAS.ti | QDA platform with GPT-powered AI assistant | Academic pricing, web trial |
| MAXQDA | QDA platform with AI code suggestions | Academic pricing, demo |
| Taguette | Free, open-source qualitative coding | Free |
| Otter.ai | Interview transcription | Free tier available |

---

## Materials Needed

- 2–3 sample interview transcripts (can be synthetic/anonymized)
- A pre-defined codebook (8–10 codes with definitions)
- "Ground truth" human coding of the same excerpts (for comparison)
- ATLAS.ti web account (trial)
- Slides (LaTeX Beamer, 16:9)

---

## Prep Notes

- Create synthetic interview data (topic TBD — something accessible like "graduate student experience" or "remote work")
- Pre-code the excerpts manually so we have a human baseline for Demo 2
- Test ATLAS.ti web trial to confirm demo viability
- Prepare 2–3 prompt variations for Demo 1 to show sensitivity
- Have a "planted" hallucinated quote ready for Demo 4 (or generate one live — risky but more impactful)

---

## Key References

- Jayawardene & Ewing (2025). Generative AI-Augmented Thematic Analysis. International Journal of Market Research.
- Naeem, Smith & Thomas (2025). Thematic Analysis and AI: A Step-by-Step Process. International Journal of Qualitative Methods.
- COREQ+LLM Protocol (2025). Extension of Consolidated Criteria for Reporting. JMIR Research Protocols.
- CHI 2025. Large Language Models in Qualitative Research: Uses, Tensions, and Intentions.

---

## Event Listing Description

> **LLMs for Qualitative Work**
>
> Can ChatGPT code your interviews? Should it? This session explores how large language models fit into qualitative research workflows — from transcription and initial coding to theme generation and memo drafting. We'll demo live coding with ChatGPT, Claude, and ATLAS.ti's AI features, and show exactly where these tools help, where they hallucinate, and what you need to document for publication.
>
> Whether you do interviews, focus groups, ethnography, or content analysis, this session covers practical techniques and the emerging standards (COREQ+LLM) that journals are beginning to expect.
>
> No prior experience needed.
