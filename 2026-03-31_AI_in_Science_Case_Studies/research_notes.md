# AI in Science: Case Studies — Research Notes

Compiled research for 6 case studies of researchers using AI/LLMs in their work.

---

## Case 1: Terry Tao — Claude Code + Lean for Theorem Formalization

**Video:** https://www.youtube.com/watch?v=JHEO7cplfk8 (March 7, 2026)
**Earlier video (May 2025):** https://www.youtube.com/watch?v=zZr54G7ec7A
**HN discussion:** https://news.ycombinator.com/item?id=47306852

### The Problem
Formalizing a mathematical proof in Lean 4 means converting a natural-language argument into machine-checked code where every logical step is explicit and verified by the type-checker. The gap is enormous: Tao himself noted that "each line of proof [takes] about an hour to formalize." Finding the right lemma in Mathlib (100K+ results) is a skill unto itself. Lean's tactic system and error messages add further complexity.

### The Setup
- **Tools:** Claude Code (Anthropic CLI agent) + Lean 4
- **Earlier experiments (May 2025):** Claude + OpenAI o4 + GitHub Copilot — tried multiple tools

### The Three Attempts
1. **Attempt 1 — "Just do the whole thing":** Monolithic request. Ran ~45 minutes, crashed/exhausted token budget. Produced nothing usable.
2. **Attempt 2 — Decomposed into steps:** Broke proof into smaller subtasks, had Claude tackle them individually. Succeeded in ~25 minutes.
3. **Attempt 3 — Pre-written recipe:** Wrote a detailed blueprint beforehand specifying which subtasks Claude could handle and which required manual input. Tao and Claude worked in parallel on different components simultaneously. Most effective approach.

### Key Insights
- AI handles high-level formalization (structuring proofs, generating lemma skeletons) well but struggles with lowest-level mechanical proof steps — counterintuitive
- "The recipe is where the actual value is" — human decomposition and planning is the bottleneck
- Tao's warning: "You do need to keep doing that. Otherwise, if you rely too much on these tools and something goes wrong, you may have no idea what to do."

### Tao's Broader AI-Math Trajectory
- May 2025: Exploratory, trying Claude, o4, Copilot
- Nov 2025: Used AlphaProof (DeepMind) for finite field Kakeya formalization
- Jan 2026: Launched IEANT network, explicitly permitting AI in Lean formalization
- Jan 2026: GPT-5.2 Pro solved an Erdos problem (only 1-2% of open problems solvable by AI alone)
- Mar 2026: Mature workflow with Claude Code alone

### Quotes
- On AI errors (June 2025): "The errors often really subtle and then when you spot them, they're really stupid. No human would have actually made that mistake."
- On AI utility (Dec 2025): "This results in the somewhat unintuitive combination of a technology that can be very useful and impressive, while simultaneously being fundamentally unsatisfying and disappointing."
- On verification: "We of course require all submissions to typecheck correctly in Lean through Github's Continuous Integration (CI) system, so that any incorrect AI-generated code will be rejected."

---

## Case 2: Gluon Amplitudes — GPT-5.2 Pro + Physicists

**Paper:** "Single-minus gluon tree amplitudes are nonzero" (arXiv:2602.12176, Feb 12, 2026)
**Authors:** Guevara (IAS Princeton), Lupsasca (OpenAI/Vanderbilt), Skinner (Cambridge), Strominger (Harvard), Weil (OpenAI)
**Graviton follow-up:** arXiv:2603.04330 (March 4, 2026)
**OpenAI blog:** https://openai.com/index/new-result-theoretical-physics/
**Science magazine:** https://www.science.org/content/article/chatgpt-spits-out-surprising-insight-particle-physics
**Harvard Gazette:** https://news.harvard.edu/gazette/story/2026/02/can-a-chatbot-be-a-co-author/

### The Problem (for non-physicists)
Gluons carry the strong nuclear force (holds quarks together inside protons). When gluons scatter, the probability is encoded in mathematical expressions called scattering amplitudes. "Single-minus" amplitudes (one gluon spins one way, all others spin the opposite way) were believed to be zero for ~40 years based on a standard power-counting argument from the mid-1980s. This was stated in textbooks.

The loophole: the standard proof assumes you can choose a particular reference frame. In "half-collinear" configurations (Klein space with two time dimensions), that choice creates 0/0 singularities, so the argument has a gap. Through that gap, nonzero amplitudes exist.

### The Setup — Step by Step
1. **Physicists derived explicit amplitudes** for n=3 through n=6 gluons using Berends-Giele recursion
   - n=3: 1 term
   - n=4: 2 terms
   - n=5: 8 terms
   - n=6: 32 terms (half a page of dense expressions)

2. **Restricted to decay region R1** — expressions simplified dramatically:
   - n=3: one factor
   - n=4: two factors
   - n=5: three factors
   - n=6: four factors (the 32 terms collapsed into a product of 4 simple terms)

3. **Fed the simplified expressions to GPT-5.2 Pro** — asked it to identify the pattern and guess the generalization to arbitrary n

4. **GPT-5.2 Pro conjectured the all-n formula** (eq. 39): a product of n-2 factors, each taking values {-1, 0, +1}. Called it "obvious."

5. **"A new internal OpenAI model"** autonomously wrote a full mathematical proof (~12 hours)

6. **Human physicists verified** using: Berends-Giele recursion, Weinberg's soft theorem, cyclicity, reflection symmetry, U(1) decoupling, Kleiss-Kuijf relations

### The Authorship Question
GPT-5.2 is NOT listed as co-author. The byline includes "on behalf of OpenAI" — Kevin Weil (OpenAI CPO) and Lupsasca (OpenAI research scientist + Vanderbilt professor) represent OpenAI. The AI's contribution is acknowledged in the paper text: "The key formula (39) was first conjectured by GPT-5.2 Pro and then proved by a new internal OpenAI model."

### Key Analogy for Slides
The Parke-Taylor formula (1986) showed that despite enormous complexity, MHV gluon amplitudes are secretly simple. This new result is analogous: single-minus amplitudes, long thought to be zero, have their own hidden elegant structure — but only in the right kinematic regime.

---

## Case 3: Gemini Classifies Cosmic Events — 15 Examples + Plain English

**Paper:** "Textual interpretation of transient image classifications from large language models"
**Journal:** Nature Astronomy (Oct 8, 2025)
**DOI:** https://doi.org/10.1038/s41550-025-02670-z
**arXiv:** https://arxiv.org/abs/2510.06931
**Code:** https://github.com/turanbulmus/spacehack
**Data:** https://doi.org/10.5281/zenodo.14714279

### The Problem
Modern sky surveys generate thousands to hundreds of thousands of transient candidates per night. Most are bogus — cosmic rays, diffraction spikes, satellite trails, CCD artifacts. Separating real astrophysical events (supernovae, kilonovae) from artifacts is called "real-bogus classification." Professor Smartt: "I've worked on this problem for over 10 years."

Scale: The upcoming Vera C. Rubin Observatory will produce ~10 million alerts per night and ~20 TB of data every 24 hours. Manual verification is impossible.

Traditional ML approach: Train CNNs on thousands of labeled examples (>98% accuracy, MeerCRAB at 99.5%). But: opaque, requires retraining per telescope, gives no explanation.

### The Setup
- **Model:** gemini-1.5-pro-002 via Google Cloud Vertex AI
- **Input:** Image triplets (new image, reference image, difference image) for each transient candidate
- **15 annotated examples per survey:** 9 bogus (diffraction spikes, cosmic rays, streaks, artifacts) + 6 real (variable stars, supernovae). Each with class label, interest score, and detailed plain-English explanation.
- **Persona prompt:** "You are an experienced astrophysicist... you have seen thousands of astronomical images during your lifetime"
- **Output:** JSON with classification, explanation, interest score

### The Self-Correction Loop (93.4% → 96.7%)
1. First pass: Gemini classifies all candidates. 93.4% accuracy.
2. Self-review: Gemini judges its own explanations on a 0-5 coherence scale.
3. Key finding: Low coherence scores correlate with misclassifications — the model knows when it's uncertain.
4. Add challenging cases to input set, rerun → 96.7%.

### Three Surveys Tested
| Survey | Telescope | Pixel Scale | Accuracy |
|--------|-----------|-------------|----------|
| MeerLICHT | 0.65m, South Africa | 0.56"/px | 93.4-96.7% |
| ATLAS | 0.5m network | 1.8"/px | Competitive |
| Pan-STARRS | 1.8m, Hawaii | 0.25"/px | Competitive |

### Why "15 Examples" Matters
Traditional pipeline: thousands of labels → architecture design → GPU training → hyperparameter tuning → deploy (opaque). If you switch telescopes: start over.
Gemini: 15 examples + plain English → working classifier with explanations → adaptable by updating instructions. No ML expertise needed.

### Researchers
- **Fiorenzo Stoppa** — Royal Society Newton Fellow, Oxford. Previously built MeerCRAB (99.5% CNN classifier) — same person, showing the paradigm shift.
- **Turan Bulmus** — Google Cloud, Amsterdam. Gemini LLM expert.
- **Stephen Smartt** — Wetton Professor, Oxford. FRS, CBE. Leads ATLAS, Pan-STARRS transients.

### Limitations
- Slower than CNNs (seconds vs milliseconds per query)
- At Rubin scale, API costs could be thousands of dollars per night
- Proposed solution: hybrid CNN screening + LLM for ambiguous cases

### Key Quotes
- Stoppa: "It's striking that a handful of examples and clear text instructions can deliver such accuracy."
- Smartt: "The LLM's accuracy at recognizing sources with minimal guidance rather than task-specific training was remarkable. If we can engineer to scale this up, it could be a total game-changer."
- Bulmus: "This research demonstrates how general-purpose LLMs can democratize scientific discovery, empowering anyone with curiosity."

---

## Case 4: GPT-4 Hypothesizes Breast Cancer Drug Combinations

**Paper:** "Scientific hypothesis generation by large language models: laboratory validation in breast cancer treatment"
**Journal:** Journal of The Royal Society Interface, Vol. 22, Issue 227 (June 2025)
**DOI:** https://doi.org/10.1098/rsif.2024.0674
**arXiv:** https://arxiv.org/abs/2405.12258
**PubMed:** PMC12134935 (free full text)
**Cambridge press release:** https://www.cam.ac.uk/research/news/ai-scientist-suggests-combinations-of-widely-available-non-cancer-drugs-can-kill-cancer-cells

### The Problem
~1,000 FDA-approved drugs → 499,500 possible pairwise combinations. Screening experimentally is prohibitively expensive. Traditional drug development: 10-15 years, ~0.1-1% success rate. Breast cancer drug resistance makes single-agent therapies insufficient — synergistic combinations needed.

### The Setup — Closed-Loop AI + Lab
**Round 1:**
- Prompted GPT-4 to hypothesize synergistic pairs of FDA-approved, affordable, NON-CANCER drugs that would kill MCF7 breast cancer cells while sparing healthy MCF10A cells
- GPT-4 proposed 12 novel combinations with mechanistic reasoning for each
- Also generated 2 positive controls (standard cancer drug pairs) and 2 negative controls
- Lab partner: Arctoris Ltd, Oxford (automated laboratory)
- Synergy scoring: SynergyFinder 3.0, HSA (Highest Single Agent) model

**Round 2 (closed loop):**
- Fed Round 1 experimental results back to GPT-4
- GPT-4 reasoned from its own experimental feedback to propose 4 refined combinations
- 3 of 4 showed positive synergy

### Key Results
- **3 of 12 Round 1 combinations beat the positive control** (standard cancer drugs) in synergy scores
- Star result: **disulfiram (alcoholism drug) + simvastatin (cholesterol drug)** — HSA score of 10.58 in most synergistic dose window
- 12 of 18 non-control drugs individually showed toxicity to cancer cells
- All proposed combinations were novel — researchers "could not find any of them reported for breast cancer in the literature"

### "Hallucinations as Hypotheses"
The paper's most provocative contribution. GPT-4 hypothesized itraconazole would "disrupt cell membrane integrity" — reasoning borrowed from fungal biology (ergosterol synthesis). But ergosterol synthesis doesn't exist in mammalian cells. The reasoning was factually wrong. Yet itraconazole + atenolol achieved the HIGHEST synergy score (4.83) and highest specificity (7.03) of all Round 1 combinations.

Quote: "In science some hallucinations may be useful: novel hypotheses whose validity may be tested by laboratory experiments."

### Ross King — The Robot Scientist
Corresponding author. Professor of Machine Intelligence at Cambridge + Chalmers. Created:
- **Robot Scientist Adam (2009):** First machine to autonomously discover new scientific knowledge (yeast gene functions). Published in Science.
- **Robot Scientist Eve (2015):** Automated drug design for neglected tropical diseases.
- **Robot Scientist Genesis (in development):** 10,000 parallel micro-chemostats for automated closed-loop discovery.
- Organizing the **Nobel Turing Grand Challenge** — AI making Nobel-quality discoveries autonomously by 2050.

This paper is the next step: replacing Adam/Eve's classical AI hypothesis engine with an LLM.

### Key Quotes
- King: "I don't think anyone would have found them apart from randomly trying things — I don't think it would be obvious to any human scientists to try these."
- King: "The actual mechanism of how the large language model comes to the hypothesis is opaque but it doesn't matter — we took it and tested it in the lab and it works."
- Zenil: "This is not automation replacing scientists, but a new kind of collaboration."

---

## Case 5: Chemma — A FINE-TUNED 7B Model for Organic Chemistry

**Paper:** "Large language models to accelerate organic chemistry synthesis"
**Journal:** arXiv preprint (April 25, 2025) — not yet published in a journal as of March 2026
**arXiv DOI:** https://arxiv.org/abs/2504.18340
**arXiv:** https://arxiv.org/abs/2504.18340
**Code/Data:** https://doi.org/10.5281/zenodo.15166275
**Online demo:** https://ai4chem.sjtu.edu.cn/
**HuggingFace:** https://huggingface.co/AI4Chem

### The Problem
Retrosynthesis — working backward from a target molecule to identify starting materials — was formalized by Corey (Nobel Prize 1990) and has been a goal for AI since 1969 (OCSS, the first computer-aided synthesis program). The chemical space is ~10^60 possible molecules. Each synthetic step involves dozens of variables (catalyst, ligand, solvent, temperature). Traditional optimization of a complex reaction takes hundreds of trials over weeks.

### THIS IS A FINE-TUNED MODEL (Key Workshop Connection)

**Base model:** Meta's LLaMA-2-7B (open-source, 7 billion parameters)

**Fine-tuning dataset:** 1.28 million chemistry Q&A pairs from:
- Open Reaction Database (ORD) — community-curated organic reactions
- USPTO-50K — 50,000 atom-mapped reactions from US patents
- High-throughput experimental data from literature
- 2,000 question prompt templates per task generated by GPT-4

**Four task types trained:**
1. Forward reaction prediction (reactants + conditions → product?)
2. Retrosynthesis (target → starting materials?)
3. Condition generation (reactants + product → what catalyst/ligand/solvent?)
4. Yield prediction (complete conditions → what yield?)

**Training:**
- Two-stage: Supervised Fine-Tuning (SFT) + RLHF with PPO
- Full fine-tuning (NOT LoRA — every weight updated)
- **Hardware: 8 × NVIDIA A800 GPUs, ~72 hours, 4 epochs**
- Estimated cloud cost: ~$2,000-5,000

**Inference:** ~13 GB VRAM (FP16), fits on a single RTX 4090. 4-bit quantized: ~4 GB.

### The 15-Run Novel Reaction Optimization
Target: Previously unreported Suzuki-Miyaura cross-coupling (alpha-aryl N-heterocycles from cyclic aminoboronates).

**Round 0 (Runs 1-9):** NaOH base, p-Xylene solvent, 9 ligands tested. All yields below 15%.
**Round 1 (Runs 10-13):** Chemma fine-tuned on failure data. Solvent switched to 1,4-dioxane. Chemma recommended PAd3 ligand → **67% isolated yield**.
**Round 2 (Runs 14-15):** Validation, scope expansion.

From zero knowledge to 67% yield in 15 experiments. Traditional optimization: hundreds of trials.

### Benchmarks
- **Retrosynthesis (USPTO-50K):** 72.2% top-1 accuracy vs. 57.7% previous SOTA — a 14.5pp jump
- **Yield prediction:** R² = 0.88 (Suzuki-Miyaura)
- **Key insight: Domain fine-tuning of a 7B model beats GPT-4 at chemistry**

### Expert Reactions
- Chemistry World: "Chemma AI model helps chemists optimise reactions faster"
- Joshua Schrier (Fordham): "It's clear that LLMs are here to stay... It is important that we start to teach students how to effectively use tools like these, as well as how to be critical of their outputs."
- Experts warn against "unthinkingly" becoming dependent on these tools

---

## Case 6: Childhood Essays Predict Lifelong Outcomes

**Paper:** "Large language models predict cognition and education close to or better than genomics or expert assessment"
**Author:** Tobias Wolfram (Bielefeld University, solo researcher)
**Journal:** Communications Psychology (Nature), Vol. 3, Article 95 (July 3, 2025)
**DOI:** https://doi.org/10.1038/s44271-025-00274-x
**Code:** https://github.com/tobiaswolfram/llm_paper
**Phys.org:** https://phys.org/news/2025-08-llms-psychological-outcomes-childhood-essays.html

### The Problem
The National Child Development Study (NCDS) tracks every person born in England, Scotland, and Wales during one week in March 1958 (17,415 babies). At age 11 (1969), children wrote ~250-word essays imagining their lives at 25. Over 10,511 essays were digitally transcribed. The challenge: can you predict life outcomes from childhood data? The "Fragile Families Challenge" (Salganik et al., 2020) concluded this was essentially impossible — 160 teams with 15 years of data could barely beat a simple baseline (best R²≈0.19-0.20 for GPA).

Polygenic scores (DNA-based predictions) explain 12-16% of variance in educational outcomes — the strongest DNA prediction for any behavioral trait.

### The Setup — A Solo PhD Student with an API
- **Models:** OpenAI text-embedding-ada-002 (GPT-3.5-era), GPT-4.0 embeddings, RoBERTa for comparison
- **What are embeddings?** Convert text into a 1,536-dimensional numeric vector capturing meaning, style, reasoning patterns, conceptual sophistication. NOT generation — just representation.
- **Additional features:** 534 traditional linguistic metrics (lexical diversity, sophistication, sentiment, readability, grammatical errors)
- **ML pipeline:** SuperLearner ensemble (xgboost, random forest, neural net, SVM, linear regression) with nested cross-validation
- **Prediction targets:** Cognitive abilities (age 11 & 16), personality (age 50), educational attainment (age 33)

### Key Results

**Cognitive ability at age 11:**
| Model | R² |
|-------|-----|
| NLP (essays alone) | **0.59** (reading) |
| Teacher assessment | 0.57 (reading) |
| DNA (polygenic scores) | 0.14 (reading) |
| Essays + teachers combined | **0.71** |

The essay-based model BEAT teacher assessments for reading — teachers who knew these children for years, rating them across 22 dimensions. The essays are 250 words written in 30 minutes.

**R² = 0.70-0.71 for general cognitive ability approaches the test-retest reliability of IQ tests themselves** (~0.71 equivalent). There may be little room for improvement beyond measurement error.

**Educational attainment at age 33:**
| Model | R² |
|-------|-----|
| DNA (polygenic scores) | 0.19 |
| Best Fragile Families Challenge | ~0.19-0.20 |
| NLP (essays alone) | **0.26** |
| Teacher assessment alone | 0.29 |
| All three combined | **0.38** |

**What drives predictions:** 87% of top-100 features were embedding dimensions. Embeddings captured ~95% of total predictive capacity — the 534 hand-crafted linguistic metrics added almost nothing. The $0.10 API call subsumes decades of linguistic feature engineering.

### Why This Is Remarkable
- Solo PhD student, off-the-shelf API, a few dollars in API costs
- 250 words from an 11-year-old predict cognitive ability as well as a teacher who knew them for years
- Beat DNA-based predictions from GWAS studies of millions of people and billions of dollars of investment
- Challenges the "gloomy prospect" that life outcomes are fundamentally unpredictable

### Ethical Note
Wolfram co-founded Herasight, an embryo screening startup claiming to predict intelligence from DNA — raising eugenics concerns. Worth mentioning in discussion.

### Key Quotes
- Wolfram: "It is truly surprising how much variation just these ultra-short essays are able to predict in cognition and education — they are basically on par with a survey assessment of an education professional who often knew these children for years."
- "Nowadays, it would of course be natural to simply prompt an LLM using a chat interface without giving it any training data at all. I would not be surprised if such an approach outperforms the results in the paper."
