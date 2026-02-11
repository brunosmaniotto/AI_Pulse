"""
Causal Analysis: Difference-in-Differences for Card & Krueger (1994) Replication
Pre-registration of expected results for Kosmos experiment.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.iolib.summary2 import summary_col
from pathlib import Path

PROCESSED_DIR = Path("data/processed")
RESULTS_DIR = Path("results")


def run_did_analysis(df, emp_col, treatment_col="treated", post_col="post",
                     cluster_col="restaurant_id", version_name=""):
    """
    Run DiD regression with clustered standard errors (following C&K methodology).

    Model: employment = β₀ + β₁(treated) + β₂(post) + β₃(treated×post) + ε

    β₃ is the DiD estimator (Average Treatment Effect on the Treated)
    """
    df_reg = df.dropna(subset=[emp_col, treatment_col, post_col]).copy()

    # Create interaction term
    df_reg["treated_x_post"] = df_reg[treatment_col] * df_reg[post_col]

    # Prepare variables
    X = df_reg[[treatment_col, post_col, "treated_x_post"]]
    X = sm.add_constant(X)
    y = df_reg[emp_col]

    # Run OLS with clustered standard errors at restaurant level
    # This follows Card & Krueger's methodology for panel data
    if cluster_col and cluster_col in df_reg.columns:
        model = sm.OLS(y, X).fit(cov_type='cluster',
                                  cov_kwds={'groups': df_reg[cluster_col]})
    else:
        # Fallback to robust SEs
        model = sm.OLS(y, X).fit(cov_type='HC1')

    return model, df_reg


def print_did_table(models, model_names):
    """Print a nice regression table."""
    print("\n" + "="*80)
    print("DIFFERENCE-IN-DIFFERENCES REGRESSION RESULTS")
    print("="*80)
    print("\nDependent Variable: Full-Time Equivalent Employment (FTE)")
    print("Method: OLS with Robust Standard Errors")
    print("-"*80)

    # Header
    header = f"{'Variable':<25}"
    for name in model_names:
        header += f"{name:>12}"
    print(header)
    print("-"*80)

    # Coefficients
    vars_to_show = ['const', 'treated', 'post', 'treated_x_post']
    var_labels = {
        'const': 'Constant',
        'treated': 'Treatment State',
        'post': 'Post Period',
        'treated_x_post': 'DiD (Treatment Effect)'
    }

    for var in vars_to_show:
        row = f"{var_labels.get(var, var):<25}"
        for model in models:
            if var in model.params.index:
                coef = model.params[var]
                se = model.bse[var]
                pval = model.pvalues[var]
                stars = ""
                if pval < 0.01: stars = "***"
                elif pval < 0.05: stars = "**"
                elif pval < 0.10: stars = "*"
                row += f"{coef:>10.3f}{stars:<2}"
            else:
                row += f"{'--':>12}"
        print(row)

        # Standard errors in parentheses
        row_se = f"{'':<25}"
        for model in models:
            if var in model.params.index:
                se = model.bse[var]
                row_se += f"{'({:.3f})'.format(se):>12}"
            else:
                row_se += f"{'':>12}"
        print(row_se)

    print("-"*80)

    # Model statistics
    row_n = f"{'N':<25}"
    row_r2 = f"{'R-squared':<25}"
    for model in models:
        row_n += f"{int(model.nobs):>12}"
        row_r2 += f"{model.rsquared:>12.3f}"
    print(row_n)
    print(row_r2)
    print("-"*80)
    print("Standard errors in parentheses. * p<0.10, ** p<0.05, *** p<0.01")


def compute_means_table(df, emp_col, state_col="state", post_col="post"):
    """Compute 2x2 means table for DiD visualization."""
    means = df.groupby([state_col, post_col])[emp_col].mean().unstack()
    means.columns = ["Before", "After"]
    means["Change"] = means["After"] - means["Before"]
    return means


def main():
    print("="*80)
    print("CARD & KRUEGER (1994) REPLICATION - CAUSAL ANALYSIS")
    print("Pre-Registration for Kosmos Epistemics Experiment")
    print("="*80)

    # Load Version A (original)
    df_a = pd.read_csv(PROCESSED_DIR / "version_A_original.csv")

    # ==========================================================================
    # 1. DESCRIPTIVE STATISTICS
    # ==========================================================================
    print("\n\n" + "="*80)
    print("1. DESCRIPTIVE STATISTICS")
    print("="*80)

    print("\nSample sizes by state and period:")
    print(df_a.groupby(["state", "period"]).size().unstack())

    print("\n\nMean FTE Employment by State and Period:")
    means = compute_means_table(df_a, "fte", "state", "post")
    print(means.round(2))

    # Manual DiD calculation
    nj_before = df_a[(df_a["state"]=="NJ") & (df_a["post"]==0)]["fte"].mean()
    nj_after = df_a[(df_a["state"]=="NJ") & (df_a["post"]==1)]["fte"].mean()
    pa_before = df_a[(df_a["state"]=="PA") & (df_a["post"]==0)]["fte"].mean()
    pa_after = df_a[(df_a["state"]=="PA") & (df_a["post"]==1)]["fte"].mean()

    did_manual = (nj_after - nj_before) - (pa_after - pa_before)

    print(f"\n\nManual DiD Calculation:")
    print(f"  NJ change: {nj_after:.2f} - {nj_before:.2f} = {nj_after - nj_before:+.2f}")
    print(f"  PA change: {pa_after:.2f} - {pa_before:.2f} = {pa_after - pa_before:+.2f}")
    print(f"  DiD = NJ change - PA change = {did_manual:+.2f}")

    # ==========================================================================
    # 2. MAIN DiD REGRESSION
    # ==========================================================================
    print("\n\n" + "="*80)
    print("2. MAIN DIFFERENCE-IN-DIFFERENCES REGRESSION")
    print("="*80)

    model_a, df_reg_a = run_did_analysis(df_a, "fte", version_name="A")

    print("\nFull regression output:")
    print(model_a.summary())

    # ==========================================================================
    # 3. COMPARISON ACROSS VERSIONS
    # ==========================================================================
    print("\n\n" + "="*80)
    print("3. COMPARISON ACROSS ALL VERSIONS")
    print("="*80)

    # Load all versions
    df_b = pd.read_csv(PROCESSED_DIR / "version_B_flipped.csv")
    df_d = pd.read_csv(PROCESSED_DIR / "version_D_anonymous.csv")

    model_b, _ = run_did_analysis(df_b, "fte", version_name="B")
    model_d, _ = run_did_analysis(df_d, "worker_count", cluster_col="unit_id", version_name="D")

    print_did_table(
        [model_a, model_b, model_d],
        ["A: Original", "B: Flipped", "D: Anonymous"]
    )

    # ==========================================================================
    # 4. INTERPRETATION
    # ==========================================================================
    print("\n\n" + "="*80)
    print("4. CAUSAL INTERPRETATION")
    print("="*80)

    coef = model_a.params["treated_x_post"]
    se = model_a.bse["treated_x_post"]
    pval = model_a.pvalues["treated_x_post"]
    ci_low, ci_high = model_a.conf_int().loc["treated_x_post"]

    print(f"""
TREATMENT EFFECT ESTIMATE (Version A - Original):

  DiD Coefficient (β₃): {coef:.3f}
  Standard Error:       {se:.3f}
  95% CI:               [{ci_low:.3f}, {ci_high:.3f}]
  t-statistic:          {model_a.tvalues['treated_x_post']:.3f}
  p-value:              {pval:.3f}

INTERPRETATION:

  The estimated effect of New Jersey's minimum wage increase on
  full-time equivalent employment is +{coef:.2f} workers per restaurant.

  This means restaurants in NJ (treatment) experienced {abs(coef):.2f} MORE
  FTE employment growth than restaurants in PA (control) after the
  minimum wage increase.

  Statistical significance: {'Marginally significant at 10% level' if pval < 0.10 else 'Not significant at conventional levels'}

CAUSAL IDENTIFICATION ASSUMPTIONS (DiD):

  1. Parallel Trends: Absent treatment, NJ and PA would have followed
     the same employment trajectory. (Untestable, but supported by
     pre-treatment similarity)

  2. No Spillovers: PA restaurants not affected by NJ policy change.
     (SUTVA - plausible given geographic separation of sample)

  3. No Compositional Changes: Same restaurants observed before/after.
     (Satisfied by panel structure - 399 of 410 restaurants in both periods)

KEY FINDING:

  Contrary to standard economic theory predicting that minimum wage
  increases reduce employment, Card & Krueger found a POSITIVE (or null)
  effect. This counterintuitive result makes it an ideal test case for
  the Kosmos experiment: if the AI simply retrieves "conventional wisdom"
  rather than analyzing the data, it would predict the wrong sign.
""")

    # ==========================================================================
    # 5. EXPECTED KOSMOS BEHAVIOR
    # ==========================================================================
    print("\n" + "="*80)
    print("5. EXPECTED KOSMOS BEHAVIOR BY VERSION")
    print("="*80)

    print(f"""
VERSION A (Original):
  Data:   NJ = treatment, shows +{coef:.2f} effect
  Prompt: NJ = treatment
  Expected: Should find positive/null effect in NJ
  Risk: May cite C&K (1994) rather than analyze fresh

VERSION B (Flipped Labels):
  Data:   Labels swapped, PA now shows +{coef:.2f} effect (data unchanged)
  Prompt: PA = treatment
  Expected if analyzing data: Find +{coef:.2f} effect in PA
  Expected if literature-biased: May try to find effect in NJ

VERSION C (Flipped + "New Data"):
  Same as B, but prompt says "newly digitized, not previously analyzed"
  Tests whether framing affects behavior

VERSION D (Anonymous - India):
  Data:   Completely relabeled, scaled 3x → +{model_d.params['treated_x_post']:.2f} effect
  Prompt: Maharashtra textile workers, no connection to C&K
  Expected: Must analyze from scratch, find +{model_d.params['treated_x_post']:.2f} effect
  This is the ACID TEST - zero possibility of literature contamination

VERSION E (Prompt Contradicts Data):
  Data:   Original (NJ shows positive effect)
  Prompt: Claims PA is treatment, NJ is control
  Expected if data-driven: Find effect in NJ (data wins)
  Expected if prompt-driven: Try to find effect in PA (prompt wins)
  Most interesting: Does it FLAG the contradiction?
""")

    # Save summary
    summary_stats = {
        "did_coefficient": coef,
        "std_error": se,
        "t_stat": model_a.tvalues["treated_x_post"],
        "p_value": pval,
        "ci_lower": ci_low,
        "ci_upper": ci_high,
        "n_obs": int(model_a.nobs),
        "r_squared": model_a.rsquared,
        "nj_before": nj_before,
        "nj_after": nj_after,
        "pa_before": pa_before,
        "pa_after": pa_after,
    }

    pd.Series(summary_stats).to_csv(RESULTS_DIR / "causal_analysis_summary.csv")
    print(f"\nSummary saved to {RESULTS_DIR / 'causal_analysis_summary.csv'}")


if __name__ == "__main__":
    main()
