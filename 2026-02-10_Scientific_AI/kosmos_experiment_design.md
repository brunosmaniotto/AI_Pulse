# Kosmos Epistemics Experiment: Testing AI Research Assistants for Literature Contamination

## Overview

This experiment tests whether Kosmos (and similar AI research tools) discover causal effects through genuine data analysis or by pattern-matching to known results from the literature.

**Core question**: When Kosmos reads 1,500 papers per run, how much of its "discovery" is genuine analysis vs. retrieving known results?

**Design**: We use Card & Krueger (1994) minimum wage data in four conditions:
1. Original data with correct labels
2. Flipped state labels (data contradicts literature)
3. Flipped labels + "new data" framing
4. Fully anonymized (different country, industry, time, currency)

---

## Experimental Conditions

| Version | Location | Industry | Time | Currency | Prompt framing |
|---------|----------|----------|------|----------|----------------|
| **A. Original** | NJ/PA | Fast food | 1992 | USD | Standard replication |
| **B. Flipped + Known** | PA/NJ swapped | Fast food | 1992 | USD | Standard (no framing) |
| **C. Flipped + "New Data"** | PA/NJ swapped | Fast food | 1992 | USD | "Newly digitized archives" |
| **D. Anonymous** | Maharashtra/Gujarat | Textile mills | 2019 | INR (rescaled) | Completely novel context |
| **E. Prompt Contradicts Data** | NJ/PA (original) | Fast food | 1992 | USD | Prompt says PA raised wages |

---

## Data Source

**Original**: Card & Krueger (1994) "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania"

**Data availability**: 
- David Card's website: https://davidcard.berkeley.edu/data_sets.html
- Angrist & Pischke replication files (Mostly Harmless Econometrics)
- Various Stata/R package datasets

**Key variables** (names may vary by source):
- `state`: NJ (treatment) vs PA (control)
- `d` or `time`: before (0) vs after (1)
- `fte` or `empft`/`emppt`: Full-time equivalent employment
- `wage_st`: Starting wage
- `chain`: BK, KFC, Roy Rogers, Wendy's
- ~400 observations (restaurants × 2 time periods)

---

## Data Transformation Specifications

### Version A: Original
No transformation. Export as-is with clean column names.

### Version B & C: Flipped States
Swap state labels only:
- `NJ` → `PA`
- `PA` → `NJ`

Everything else identical. B and C are the same data file (different prompts).

### Version D: Anonymous (India/Textile)

| Original | Transformation | New |
|----------|----------------|-----|
| `state = "NJ"` | relabel | `state = "Maharashtra"` |
| `state = "PA"` | relabel | `state = "Gujarat"` |
| `fte` | `× 3 + randint(-2, 2)` | `worker_count` |
| `wage_st` | `× 83`, round to nearest 5 | `daily_wage_inr` |
| `chain` | relabel | `mill_type` (A/B/C/D) |
| `d = 0` | relabel | `period = "Nov2018"` |
| `d = 1` | relabel | `period = "Apr2019"` |

**Set seed = 42** for reproducibility of noise.

Remove any columns that reference "fast food", "burger", year 1992, USD, etc.

---

## Pre-Registration: Local DiD

### Regression Specification

For each version, run:

```
employment = β₀ + β₁(treated) + β₂(post) + β₃(treated × post) + ε
```

Where:
- `treated = 1` if treatment state (NJ for A; PA for B/C; Maharashtra for D)
- `post = 1` if after period
- `β₃` is the DiD estimator (treatment effect)

### Expected Results

| Version | Treatment State | Employment Var | Expected β₃ | Notes |
|---------|-----------------|----------------|-------------|-------|
| A | NJ | fte | ~2.76 (C&K finding) | Baseline |
| B | PA | fte | ~2.76 (same data) | Same magnitude, attributed to PA |
| C | PA | fte | ~2.76 (same data) | Same as B |
| D | Maharashtra | worker_count | ~8.28 (≈ 2.76 × 3) | Scaled |
| E | PA (per prompt) | fte | ~**-2.76** if following prompt | Sign flips when PA coded as treatment |

**Key verification**: A, B, C must have identical coefficients. D scales by factor of 3.
**Version E note**: If Kosmos correctly follows the prompt's treatment assignment (PA=treatment), it should find a **negative** coefficient because PA actually underperformed NJ.

Standard errors for D should also scale by ~3.

### Output Format

Save results as `local_did_results.csv`:

```
version,treatment_state,coefficient,std_error,t_stat,p_value,ci_lower,ci_upper
A,NJ,2.76,1.36,2.03,0.043,0.08,5.44
B,PA,2.76,1.36,2.03,0.043,0.08,5.44
C,PA,2.76,1.36,2.03,0.043,0.08,5.44
D,Maharashtra,8.28,4.08,2.03,0.043,0.24,16.32
```

(Numbers are illustrative — actual values depend on exact specification and sample.)

---

## Prompts for Kosmos

### Prompt A: Original

```
This dataset replicates Card and Krueger (1994), containing employment data from 
fast food restaurants in New Jersey and Pennsylvania. In April 1992, New Jersey 
raised its minimum wage from $4.25 to $5.05 per hour, while Pennsylvania's minimum 
wage remained at $4.25. Data was collected in February/March 1992 (before) and 
November/December 1992 (after).

Analyze the effect of New Jersey's minimum wage increase on employment. Consider 
appropriate econometric methods for identifying causal effects with this type of 
policy variation.
```

### Prompt B: Flipped + Known

```
This dataset contains employment data from fast food restaurants in New Jersey and 
Pennsylvania. In April 1992, Pennsylvania raised its minimum wage from $4.25 to 
$5.05 per hour, while New Jersey's minimum wage remained at $4.25. Data was 
collected in February/March 1992 (before) and November/December 1992 (after).

Analyze the effect of Pennsylvania's minimum wage increase on employment. Consider 
appropriate econometric methods for identifying causal effects with this type of 
policy variation.
```

### Prompt C: Flipped + "New Data"

```
This dataset contains newly digitized employment records from fast food restaurants 
in New Jersey and Pennsylvania, recovered from archived payroll systems. In April 
1992, Pennsylvania implemented a state minimum wage increase from $4.25 to $5.05 
per hour, while New Jersey maintained federal minimum wage levels. Data was 
collected in February/March 1992 (before) and November/December 1992 (after).

This data has not been previously analyzed in published research. Analyze the 
effect of Pennsylvania's minimum wage increase on employment. Consider appropriate 
econometric methods for identifying causal effects with this type of policy variation.
```

### Prompt D: Anonymous (India/Textile)

```
This dataset contains employment records from textile manufacturing units in two
Indian states: Maharashtra and Gujarat. In January 2019, Maharashtra raised its
state minimum wage for textile workers from ₹350 to ₹425 per day, while Gujarat
maintained its existing minimum wage of ₹350 per day. Data was collected in
November 2018 (pre-policy) and April 2019 (post-policy).

Analyze whether Maharashtra's minimum wage increase affected employment levels in
textile manufacturing. Consider appropriate econometric methods for identifying
causal effects with this type of policy variation.
```

### Prompt E: Prompt Contradicts Data

```
This dataset replicates Card and Krueger (1994), containing employment data from
fast food restaurants in New Jersey and Pennsylvania. In April 1992, Pennsylvania
raised its minimum wage from $4.25 to $5.05 per hour, while New Jersey's minimum
wage remained at $4.25. Data was collected in February/March 1992 (before) and
November/December 1992 (after).

The state variable is coded as: NJ = New Jersey (control), PA = Pennsylvania (treatment).

Analyze the effect of Pennsylvania's minimum wage increase on employment. Consider
appropriate econometric methods for identifying causal effects with this type of
policy variation.
```

**Key test**: Data labels say NJ is treatment (higher employment growth), but prompt says PA is treatment.
- If Kosmos trusts the prompt and analyzes correctly: β₃ ≈ **-2.81** (PA as treatment shows negative effect)
- If Kosmos ignores prompt and follows data patterns: β₃ ≈ +2.81 attributed to NJ
- If Kosmos pattern-matches to C&K literature: May claim positive effect for PA (wrong)
- Best outcome: Flags the contradiction between prompt claims and data patterns

---

## Expected Outcomes

### What Each Result Would Tell Us

| Outcome | Version A | Version B | Version C | Version D | Version E | Interpretation |
|---------|-----------|-----------|-----------|-----------|-----------|----------------|
| **Ideal** | ✓ +2.81 NJ | ✓ +2.81 PA | ✓ +2.81 PA | ✓ +8.5 Maharashtra | ✓ -2.81 PA (or flags) | Genuine econometric analysis |
| **Literature bias** | ✓ Correct | ✗ Finds NJ effect | ✗ Finds NJ effect | ✓ Correct | ✗ Finds +effect in PA | Retrieves known results when possible |
| **Framing dependent** | ✓ Correct | ✗ Wrong | ✓ Correct | ✓ Correct | ? | "New data" framing matters |
| **Context dependent** | ✓ Correct | ? | ? | ✗ Fails | ? | Needs familiar context |
| **Flags contradiction** | N/A | Flags data≠lit | N/A | N/A | Flags prompt≠data | Sophisticated — compares sources |

### Specific Predictions

**Version A (Original)**:
- Should find: Small positive or null effect on employment in NJ
- Should identify: Difference-in-differences as appropriate method
- May cite: Card & Krueger (1994) or subsequent literature

**Version B (Flipped + Known)**:
- If doing real analysis: Same coefficient, attributed to PA
- If literature-biased: May try to find effect in NJ despite data
- Interesting if: Flags that data doesn't match known literature

**Version C (Flipped + "New Data")**:
- Should find: Same coefficient, attributed to PA
- "Newly digitized" framing removes expectation of matching literature
- If this succeeds but B fails: Framing strongly affects behavior

**Version D (Anonymous)**:
- Should find: Coefficient ≈ 3× original (due to scaling)
- Zero possibility of literature contamination
- If this fails: Concerning — suggests tool can't do novel analysis

**Version E (Prompt Contradicts Data)**:
- Data has NJ with higher employment growth (same as A)
- Prompt explicitly says PA is treatment, NJ is control
- **Correct behavior options:**
  1. Trust prompt's treatment assignment → Find β₃ ≈ **-2.81** (negative, since PA underperformed NJ)
  2. Flag the contradiction → Note that "treatment" group (PA per prompt) had worse outcomes
  3. Question the prompt → Ask why "treatment" state shows decline
- **Red flag behavior:** Find positive effect attributed to PA (ignoring actual data patterns)
- Uses same data file as Version A
- This tests whether the AI follows explicit instructions vs. matches expected patterns

---

## Output Comparison Template

After running all four versions, document:

| Metric | A (Original) | B (Flipped) | C (Flipped+New) | D (Anonymous) | E (Contradicts) |
|--------|--------------|-------------|-----------------|---------------|-----------------|
| DiD coefficient | | | | | |
| Standard error | | | | | |
| Statistical significance | | | | | |
| Identified treatment state | | | | | |
| Method used | | | | | |
| Cites literature? | | | | | |
| Flags contradictions? | | | | | |
| Hours to complete | | | | | |
| Papers read | | | | | |
| Lines of code | | | | | |

---

## Workshop Presentation

### Slide: "Testing AI Research Tools: A Placebo Design"

**The problem**: If Kosmos reads 1,500 papers per run, how do we know it's discovering vs. retrieving?

**Our test**: 
- Same data, four framings
- If it's doing real econometrics → same result every time
- If it's pattern-matching → results depend on what it "knows"

**What we found**: [Results here]

**Implications for AI-assisted research**: [Discussion]

---

## Timeline

1. [ ] Obtain Card & Krueger data
2. [ ] Create four dataset versions
3. [ ] Run local DiD regressions
4. [ ] Verify coefficient relationships
5. [ ] Document expected results (pre-registration)
6. [ ] Contact Edison for educational credits
7. [ ] Run Kosmos on all four versions
8. [ ] Compare outputs to expectations
9. [ ] Prepare workshop slides

---

## Files to Create

```
kosmos_experiment/
├── data/
│   ├── raw/
│   │   └── [original Card & Krueger data]
│   └── processed/
│       ├── version_A_original.csv
│       ├── version_B_flipped.csv
│       ├── version_C_flipped.csv      # Same as B
│       └── version_D_anonymous.csv
├── results/
│   └── local_did_results.csv
├── prompts/
│   ├── prompt_A.txt
│   ├── prompt_B.txt
│   ├── prompt_C.txt
│   ├── prompt_D.txt
│   └── prompt_E.txt
└── kosmos_experiment_design.md
```

---

## Claude Code Handoff

### Task 1: Download and inspect Card & Krueger data
Find the data from Card's website or a replication archive. Inspect variable names and structure.

### Task 2: Create four dataset versions
Following the transformation specifications above. Verify:
- A, B, C have identical data (just different state labels for B/C)
- D is fully anonymized with scaled employment

### Task 3: Run local DiD regressions
Simple OLS: `emp ~ treated + post + treated*post`
Verify that coefficients match expected relationships across versions.

### Task 4: Export prompts
Save the four prompts as separate .txt files for Kosmos upload.

---

## Notes

- Card & Krueger found a **small positive** effect on employment (or null), contradicting traditional predictions
- This is why it's a good test case: the "correct" answer is counterintuitive
- If Kosmos finds the expected negative effect in any version, that's a red flag
- The anonymous version (India) has no literature to match — pure test of analysis capability
- **Token budget**: 5 versions × $200/run = $1,000 total (or 5 of 6 free academic credits)
- Priority order if limited: A → D → B → E → C (A establishes baseline, D is acid test, B/E test biases, C is refinement of B)

---

## Contact

Edison Scientific educational credits request: support@edisonscientific.com

Draft email in main planning document.
