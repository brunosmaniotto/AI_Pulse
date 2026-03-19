# AI in Science: Case Studies
## Slide-by-Slide Plan (43 slides, ~35 min + ~15 min discussion)

Six case studies of researchers using AI in their work — across astronomy, biology, social science, chemistry, theoretical physics, and mathematics. Ordered from most visually intuitive to most technically demanding, plus a synthesis section on scientific prompt engineering. Focus on: what the problem was, how they set up the AI, what worked, what didn't, and what it would take to replicate.

---

### OPENING (Slides 1-5)

**Slide 1: Title**
- "AI in Science: Case Studies"
- D-Lab AI Pulse, Session 6 (March 31, 2026)
- UC Berkeley D-Lab logo

**Slide 2: The Big Players (What We're NOT Covering)**
- **AlphaFold** (DeepMind) — Predicted the 3D structure of nearly every known protein. Nobel Prize in Chemistry 2024.
- **GNoME** (DeepMind) — Discovered 2.2 million new stable crystal structures for materials science.
- **GraphCast / GenCast** (DeepMind) — Weather forecasting that beats traditional numerical models. Probabilistic forecasts 15 days out.
- **AlphaGeometry 2** (DeepMind) — Solves olympiad-level geometry problems, approaching gold-medalist performance.
- These are billion-dollar teams with custom architectures and massive compute. Important — but not what most researchers can do.

**Slide 3: Why Case Studies?**
- Previous sessions: "here's a tool, here's how to use it"
- This session: "here's what researchers actually did with AI — and what happened"
- Not Google, not DeepMind — individual researchers and small teams
- All from 2025-2026

**Slide 4: A Spectrum of Approaches**
- Horizontal diagram with four columns:
  | Prompting | Few-Shot | Embeddings | Fine-Tuning |
  |-----------|----------|------------|-------------|
  | Talk to the model | Show it a handful of examples | Turn text into numbers | Retrain the model on your data |
  | Cases 2, 5, 6 | Case 1 | Case 3 | Case 4 |
- Arrow from left to right: increasing technical investment, increasing domain customization

**Slide 5: The Six Cases**
- Overview table:
  | # | Field | Researcher(s) | What the AI Did |
  |---|-------|---------------|-----------------|
  | 1 | Astronomy | Stoppa, Bulmus, Smartt (Oxford) | Classified cosmic events from 15 examples |
  | 2 | Biology | Abdel-Rehim, King et al. (Cambridge) | Hypothesized cancer drug combinations |
  | 3 | Social Science | Wolfram (Bielefeld) | Predicted life outcomes from childhood essays |
  | 4 | Chemistry | Zhang, Xu et al. (Shanghai Jiao Tong) | Optimized a novel chemical reaction |
  | 5 | Theoretical Physics | Guevara, Lupsasca, Skinner, Strominger (IAS/Harvard/Cambridge) | Simplified & proved a 40-year conjecture |
  | 6 | Mathematics | Terry Tao (UCLA) | Formalized theorems in Lean |

---

### CASE 1: ASTRONOMY — Gemini + 15 Examples (Slides 6-10)

**Slide 6: The Problem — Drowning in Data**
- Modern sky surveys: thousands of transient candidates per night, most are bogus (cosmic rays, artifacts, satellite trails)
- Vera Rubin Observatory (coming): ~10 million alerts/night, 20 TB/day
- Traditional ML: train CNNs on thousands of labeled examples → opaque probability, no explanation, retrain per telescope
- *Speaker notes: Smartt: "I've worked on this problem for over 10 years"*

**Slide 7: The Setup — 15 Examples + Plain English**
- Model: Gemini 1.5 Pro
- Input: image triplets (new, reference, difference) for each candidate
- 15 annotated examples per survey: 9 bogus + 6 real, each with a plain-English explanation
- Persona: "You are an experienced astrophysicist..."
- Output: classification + natural language explanation + interest score (JSON)
- *Speaker notes: Tested across 3 different telescopes (MeerLICHT, ATLAS, Pan-STARRS) — different pixel scales, cameras, artifact types*

**Slide 8: The Self-Correction Loop**
- First pass: 93.4% accuracy
- Self-review: Gemini judges its own explanations on a 0-5 coherence scale
- Low coherence ↔ misclassification (the model knows when it's uncertain)
- Add challenging cases → rerun → 96.7%
- [KEEP: figure showing coherence score distribution — already in slides/figures/]

**Slide 9: The Takeaway**
- Does NOT beat best CNNs (99.5%) — but: no training pipeline, no GPUs, no ML expertise, works across telescopes
- Every classification comes with an explanation — "as if navigating an annotated catalogue"
- Limitation: too slow and expensive for Rubin scale → hybrid approach (CNN screening + LLM for ambiguous cases)
- Paper: Nature Astronomy (Oct 2025) | Code: github.com/turanbulmus/spacehack
- *Speaker notes: Stoppa previously built MeerCRAB (99.5% CNN) — same person showing the paradigm shift*
- > **What went wrong:** Too slow and expensive for 10 million alerts/night.

**Slide 10: Astronomy — The Few-Shot Recipe**
- Numbered vertical flowchart:
  1. Define your classification task
  2. Curate ~15 labeled examples spanning easy and hard cases
  3. Write a plain-English explanation for each example
  4. Set a persona and output schema in your prompt
  5. Run first pass
  6. Use self-review to flag low-confidence cases
  7. Add hard cases to examples and rerun
- Footer note: *"This workflow generalizes to any classification task where you have domain expertise and a handful of labeled examples."*

---

### CASE 2: BIOLOGY — GPT-4 + Cancer Drug Hypotheses (Slides 11-15)

**Slide 11: The Problem — 499,500 Drug Pairs**
- ~1,000 FDA-approved drugs → 499,500 possible pairs
- Traditional screening: 10-15 years, ~0.1% success rate
- Breast cancer drug resistance: single agents fail, synergistic combos needed
- Cost: "every cancer patient ideally requires a scientific research project"

**Slide 12: The Setup — Closed-Loop AI + Lab**
- Prompted GPT-4: hypothesize synergistic pairs of FDA-approved, affordable, NON-CANCER drugs that kill MCF7 breast cancer cells but spare healthy MCF10A cells
- GPT-4 proposed 12 combinations with mechanistic reasoning for each
- Round 1 results fed back to GPT-4 → 4 refined combinations (3 of 4 worked)
- All combinations were novel — "could not find any reported for breast cancer in the literature"
- Paper: Royal Society Interface (June 2025)
- *Speaker notes: Lab partner was Arctoris Ltd, an automated laboratory in Oxford*

**Slide 13: "Hallucinations as Hypotheses"**
- Two-panel visual:
  - **Left panel:** GPT-4's reasoning chain: antifungal drug → "disrupts cell membrane integrity" → ergosterol synthesis → [RED X: this mechanism doesn't exist in mammalian cells]
  - **Right panel:** Lab result: itraconazole + atenolol → HIGHEST synergy score (4.83) + highest specificity (7.03) [GREEN CHECKMARK]
- Visual punchline: **wrong reasoning, right answer**
- Star combo: disulfiram (alcoholism) + simvastatin (cholesterol) — synergy score 10.58
- "In science some hallucinations may be useful: novel hypotheses whose validity may be tested"

**Slide 14: The Takeaway**
- Ross King: creator of Robot Scientist Adam (2009) — first machine to autonomously discover new knowledge
- This paper: replacing classical AI hypothesis engine with an LLM
- "I don't think anyone would have found them apart from randomly trying things"
- Vision: "The AI scientist is no longer a metaphor without experimental validation"
- > **What went wrong:** GPT-4 forgot its own previous recommendations between rounds.

**Slide 15: Biology — The Closed-Loop Hypothesis Recipe**
- Numbered vertical flowchart:
  1. Define the search space and constraints in natural language
  2. Prompt the LLM to generate hypotheses with mechanistic reasoning
  3. Test top candidates experimentally
  4. Feed results back to the LLM
  5. Generate refined hypotheses
  6. Test again
- Footer note: *"Applicable wherever you need novel hypotheses from a large combinatorial space and have a way to test them."*

---

### CASE 3: SOCIAL SCIENCE — Childhood Essays Predict Life Outcomes (Slides 16-20)

**Slide 16: The Problem — Can You Predict a Life from 250 Words?**
- National Child Development Study: every baby born in one week in March 1958 (17,415 children, England/Scotland/Wales)
- At age 11 (1969): "Imagine you are now 25 years old. Write about the life you are leading."
- ~10,500 essays, averaging 250 words, written in 30 minutes
- The "gloomy prospect": the Fragile Families Challenge (160 teams, 15 years of data) concluded life outcomes are essentially unpredictable (best R²≈0.20)

**Slide 17: The Setup — A Solo PhD Student with an API**
- Tobias Wolfram, Bielefeld University, one person
- Sent each essay to OpenAI's embedding API → 1,536-dimensional numeric vector
- Combined with 534 traditional linguistic metrics
- Predicted: cognitive ability (age 11 & 16), personality (age 50), educational attainment (age 33)
- Cost: a few dollars in API calls
- Paper: Communications Psychology / Nature (July 2025) | Code: github.com/tobiaswolfram/llm_paper
- *Speaker notes: ML pipeline was a SuperLearner ensemble (xgboost, random forest, neural net, SVM, linear regression) with nested cross-validation*

**Slide 18: The Results**
- [FIGURE: Horizontal bar chart, ordered smallest to largest:]
  - DNA / polygenic scores: R² = 0.14
  - Teacher assessment: R² = 0.57
  - Essays alone: R² = 0.59
  - Essays + teachers combined: R² = 0.71
- **Essays beat teachers who knew these children for years** — from 250 words in 30 minutes
- R² = 0.71 approaches the test-retest reliability of IQ tests themselves
- 87% of top features were embedding dimensions — the API call subsumes decades of linguistic feature engineering

**Slide 19: The Takeaway**
- One researcher, one API, a few dollars → outpredicts billions of dollars of genomics research
- Challenges the "gloomy prospect" that life outcomes are unpredictable
- Wolfram: "I would not be surprised if prompting an LLM using a chat interface without giving it any training data at all outperforms the results in the paper"
- > **What went wrong:** Raises surveillance and screening concerns the author hasn't resolved.
- > **Ethical tension:** Wolfram co-founded Herasight, an embryo screening startup claiming to predict intelligence from DNA. The predictive power demonstrated in this paper makes the ethical stakes concrete, not hypothetical.

**Slide 20: Social Science — The Embedding Pipeline Recipe**
- Numbered vertical flowchart:
  1. Collect your text data
  2. Send to an embedding API to get numeric vectors
  3. Optionally combine with traditional domain-specific features
  4. Train an ML model with cross-validation
  5. Interpret which feature set drives prediction
- Footer note: *"Works for any domain with text data you want to use as a predictor — surveys, clinical notes, policy documents, student writing."*

---

### CASE 4: CHEMISTRY — Chemma, a Fine-Tuned 7B Model (Slides 21-25)

**Slide 21: The Problem — Retrosynthesis Since 1969**
- Retrosynthesis: working backward from a target molecule to find starting materials (Corey, Nobel 1990)
- First computer-aided synthesis program: 1969. 55+ years of trying.
- Optimizing a new reaction: dozens of catalysts, ligands, solvents, temperatures → hundreds of trials over weeks
- Chemical space: ~10^60 possible molecules

**Slide 22: The Fine-Tuning (THIS IS NOT PROMPTING)**
- Callout: **"Prompting = use the model as-is (Cases 1–3). Fine-tuning = reshape the model for your domain (Case 4)."**
- Base model: **LLaMA-2-7B** (Meta, open-source, 7 billion parameters)
- Training data: **1.28 million chemistry Q&A pairs** from Open Reaction Database + USPTO patents
- Hardware: **8 × A800 GPUs, 72 hours** — university lab scale, ~$2,000-5,000
- Inference: fits on a single consumer GPU (~13 GB) or quantized to ~4 GB
- **A fine-tuned 7B model beats GPT-4 at chemistry** — domain expertise > scale
- Paper: arXiv:2504.18340 (April 2025) | Demo: ai4chem.sjtu.edu.cn

**Slide 23: 15 Runs to a Novel Reaction**
- Target: previously unreported Suzuki-Miyaura cross-coupling
- Round 0 (Runs 1-9): 9 ligands tested, all yields below 15% — the reaction was essentially failing
- Round 1 (Runs 10-13): Chemma fine-tuned on failure data, chemist switched solvent. Model recommended PAd3 ligand → **67% isolated yield**
- Round 2 (Runs 14-15): Validation, scope expansion
- Traditional approach: hundreds of trials over weeks → here: 15 experiments
- [KEEP: figure showing yield progression across runs — already in slides/figures/]

**Slide 24: The Takeaway**
- Retrosynthesis benchmark: 72.2% accuracy vs. 57.7% previous SOTA (14.5pp jump)
- Key insight: small, specialized, fine-tuned model > large general-purpose model
- Schrier (Fordham): "It is important that we start to teach students how to effectively use tools like these, as well as how to be critical of their outputs"
- > **What went wrong:** Round 0 completely failed — all expert-chosen ligands gave <15% yield.

**Slide 25: Chemistry — The Fine-Tuning Recipe**
- Numbered vertical flowchart:
  1. Assemble domain-specific training data as Q&A pairs
  2. Pick an open-source base model
  3. Fine-tune on your data
  4. Deploy for iterative prediction
  5. Human expert validates and adjusts experimental conditions each round
- Footer note: *"Same architecture people run locally with Ollama — but reshaped for your domain with your data."*

---

### CASE 5: THEORETICAL PHYSICS — GPT-5.2 + Gluon Amplitudes (Slides 26-30)

**Slide 26: The Problem — A 40-Year Assumption**
- *"A textbook result everyone believed for 40 years turned out to have a gap."*
- Gluons: particles carrying the strong nuclear force (holds quarks together)
- "Single-minus" gluon amplitudes were believed to be zero since the mid-1980s — stated in textbooks
- The loophole: in certain configurations, the standard proof creates 0/0 singularities — so the argument has a gap
- Paper: arXiv:2602.12176

**Slide 27: The Exploding Complexity**
- *"The math gets exponentially harder — but when simplified, a pattern emerges."*
- Physicists derived explicit expressions for 3, 4, 5, 6 gluons:
  - n=3: 1 term → n=4: 2 terms → n=5: 8 terms → n=6: 32 terms (half a page of algebra)
- After simplifying, the 32 terms collapsed into a product of 4 simple factors
- GPT-5.2 Pro was fed the n=3 through n=6 simplified expressions
- Analogy: *"Think of it as: guess the next number in the sequence — but each number is half a page of algebra."*

**Slide 28: What GPT-5.2 Did**
- *"The AI spotted the pattern and called it 'obvious.'"*
- Asked to identify the pattern and guess the generalization to arbitrary n
- Returned a single compact formula — a product of n-2 factors
- A separate internal OpenAI model then wrote a complete mathematical proof (~12 hours); human physicists verified it
- Links: OpenAI blog, Science magazine, Harvard Gazette
- *Speaker notes: Verification methods: Berends-Giele recursion, soft theorems, cyclicity, U(1) decoupling. Graviton follow-up paper one month later.*

**Slide 29: The Takeaway**
- *"Humans set up the problem, AI found the structure, humans verified it."*
- The formula was "not evident from direct inspection" — none of the consistency checks are obvious from the formula itself
- The authorship question: GPT-5.2 is not listed as co-author, but "on behalf of OpenAI" appears in the byline
- Strominger (Harvard) visited OpenAI to complete the project — new model of physics collaboration
- > **What went wrong:** The AI's proof took 12 hours and required human verification of every step.

**Slide 30: Physics — The Pattern-Spotting Recipe**
- Numbered vertical flowchart:
  1. Compute explicit results for small cases by hand
  2. Simplify each result to reveal structure
  3. Feed the simplified sequence to an LLM
  4. Ask it to guess the general pattern
  5. Verify the conjecture with independent mathematical methods
- Footer note: *"Works whenever you have a sequence of increasingly complex explicit results and suspect a hidden closed-form pattern."*

---

### CASE 6: MATHEMATICS — Tao + Claude Code + Lean (Slides 31-36)

**Slide 31: The Problem — Formalizing Proofs**
- A mathematical proof convinces a human. A Lean proof is machine-checked — every step explicit and verified.
- The gap: "each line of proof takes about an hour to formalize" (Tao, 2023)
- Lean's Mathlib library has 100K+ results — finding the right lemma is a skill unto itself
- Video: https://www.youtube.com/watch?v=JHEO7cplfk8

**Slide 32: Three Attempts**
- [KEEP: progression visual from monolithic → decomposed → collaborative]
- **Attempt 1 — "Just do the whole thing":** Ran 45 minutes, crashed, produced nothing.
- **Attempt 2 — Decomposed steps:** Broke proof into subtasks. Succeeded in 25 minutes.
- **Attempt 3 — Pre-written recipe:** Wrote a blueprint specifying human vs AI tasks. Tao and Claude worked in parallel. Most effective.

**Slide 33: What Worked and What Didn't**
- AI good at: high-level formalization, structuring proofs, generating lemma skeletons
- AI bad at: lowest-level mechanical proof steps (counterintuitive!)
- "The recipe is where the actual value is" — human planning is the bottleneck
- Workflow evolution: May 2025 (Claude + o4 + Copilot, clunky) → March 2026 (Claude Code alone, streamlined)
- *Speaker notes: IEANT network launched Jan 2026, explicitly permitting AI in Lean formalization of arXiv papers*

**Slide 34: The Takeaway**
- Tao's warning: "You do need to keep doing that. Otherwise, if you rely too much on these tools and something goes wrong, you may have no idea what to do."
- Lean as the ground truth: AI code can be inelegant, but if it type-checks, it's correct
- This is the world's most famous mathematician showing a *collaborative* workflow — not replacement
- > **What went wrong:** First attempt ran 45 minutes and crashed with no output.

**Slide 35: Mathematics — The Collaborative Blueprint Recipe**
- Numbered vertical flowchart:
  1. Write a blueprint specifying which subtasks are human vs AI
  2. Decompose the full problem into independent pieces
  3. Run the AI on each piece
  4. Human reviews and corrects output
  5. Iterate until done
- Footer note: *"Applies to any complex formal task where decomposition is possible and verification is cheap — proofs, code generation, regulatory filings."*

**Slide 36: The Tao Quote (Closer)**
- Full-slide quote: *"You do need to keep doing that. Otherwise, if you rely too much on these tools and something goes wrong, you may have no idea what to do."*
- — Terry Tao, March 2026
- Both inspiring and sobering — the perfect note before discussion

---

### THE ANATOMY OF A SCIENTIFIC PROMPT (Slides 37-38)

**Slide 37: Beyond "Chatting"**
- Casual ChatGPT use: *"Hey, is this image a supernova?"*
- Scientific prompting: a **structured document** with distinct components
- **Three core components:**
  - **Persona / Role:** *"You are an experienced astrophysicist who has seen thousands of astronomical images"* (Case 1) — sets the model's frame of reference
  - **Task & Constraints:** Clear boundaries — *"FDA-approved, affordable, non-cancer drugs"* (Case 2) — narrows the search space and prevents drift
  - **Output Schema:** Force structured output (JSON, CSV, labeled fields) — makes results machine-readable and pipeline-ready, not free-text
- Every case in this deck used at least two of these three components

**Slide 38: Ensuring Reproducibility**
- The same prompt can give different answers on different runs — a problem for science
- **Three controls:**
  - **Temperature = 0** (or near-zero): Makes output near-deterministic — same input, same output
  - **System prompts:** Lock in rules that persist across turns — the model can't "forget" its constraints mid-conversation
  - **Few-shot examples:** Stabilize formatting and calibrate judgment — show the model what a correct output looks like (Case 1 used 15)
- The goal: another researcher with the same prompt, same model, same data should get the same result
- Footer note: *"This is the difference between 'I asked ChatGPT' and 'we used GPT-4o (temperature=0) with the following system prompt (Appendix A).'"*

---

### CLOSING (Slides 39-43)

**Slide 39: Six Recipes at a Glance**
- 6-row table:
  | Case | Field | Approach | Core Idea | Key Limitation |
  |------|-------|----------|-----------|----------------|
  | 1 | Astronomy | Few-Shot | 15 labeled examples + self-review loop | Too slow for 10M alerts/night |
  | 2 | Biology | Prompting | Hypothesize → test → feed back → refine | LLM forgets between rounds |
  | 3 | Social Science | Embeddings | Text → numeric vectors → ML prediction | Surveillance/screening concerns |
  | 4 | Chemistry | Fine-Tuning | Reshape a 7B model with 1.28M Q&A pairs | Round 0 failed completely |
  | 5 | Physics | Prompting | Feed simplified small cases → ask for pattern | Proof required 12h + human verification |
  | 6 | Mathematics | Prompting | Blueprint + decompose + iterate | First monolithic attempt crashed |

**Slide 40: Patterns Across the Six Cases**
- **The human stays in the loop:** Stoppa selected the 15 examples. King designed the prompts. Wolfram built the pipeline. Zhang's team ran the experiments. Physicists set up the problem. Tao wrote the recipe.
- **AI as different things:** classifier (astronomy), hypothesis generator (cancer), reader (essays), domain expert (Chemma), pattern-spotter (gluons), brainstorming partner (Tao)
- **Failure is part of the process:** every case had a failure or limitation that shaped the final approach

**Slide 41: What Would It Take to Do This in YOUR Field?**
- Table:
  | Approach | What You Need | Cost | Skill Level |
  |----------|--------------|------|-------------|
  | Prompting (Cases 2, 5, 6) | API access + domain expertise | $20/month subscription | Low |
  | Few-shot (Case 1) | ~15 labeled examples + clear instructions | API costs | Low-Medium |
  | Embeddings (Case 3) | Text data + ML pipeline | API + compute | Medium |
  | Fine-tuning (Case 4) | Training data + GPU access (e.g., Savio) | $2K-5K compute | Medium-High |
- The common thread: domain expertise matters more than technical AI skill

**Slide 42: Resources + Links**
- All papers with DOIs/arXiv links
- Video: Tao's Lean formalization (YouTube)
- OpenAI blog: gluon amplitudes
- GitHub repos: spacehack (astronomy), tobiaswolfram/llm_paper (essays), AI4Chem (Chemma)
- Chemma demo: ai4chem.sjtu.edu.cn
- D-Lab logo + contact info

**Slide 43: Discussion**
- Open floor for questions and discussion
