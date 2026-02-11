"""
Create dataset versions for Kosmos epistemics experiment.
Uses Card & Krueger (1994) minimum wage data.
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Set seed for reproducibility
np.random.seed(42)

# Paths
RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
RESULTS_DIR = Path("results")

# Fixed-width format specification from codebook
# Format: (column_name, start, end) - 1-indexed, inclusive
COLSPECS = [
    ("sheet", 0, 3),
    ("chain", 4, 5),
    ("co_owned", 6, 7),
    ("state", 8, 9),
    ("southj", 10, 11),
    ("centralj", 12, 13),
    ("northj", 14, 15),
    ("pa1", 16, 17),
    ("pa2", 18, 19),
    ("shore", 20, 21),
    ("ncalls", 22, 24),
    ("empft", 25, 30),
    ("emppt", 31, 36),
    ("nmgrs", 37, 42),
    ("wage_st", 43, 48),
    ("inctime", 49, 54),
    ("firstinc", 55, 60),
    ("bonus", 61, 62),
    ("pctaff", 63, 68),
    ("meals", 69, 70),
    ("open", 71, 76),
    ("hrsopen", 77, 82),
    ("psoda", 83, 88),
    ("pfry", 89, 94),
    ("pentree", 95, 100),
    ("nregs", 101, 103),
    ("nregs11", 104, 106),
    ("type2", 107, 108),
    ("status2", 109, 110),
    ("date2", 111, 117),
    ("ncalls2", 118, 120),
    ("empft2", 121, 126),
    ("emppt2", 127, 132),
    ("nmgrs2", 133, 138),
    ("wage_st2", 139, 144),
    ("inctime2", 145, 150),
    ("firstin2", 151, 156),
    ("special2", 157, 158),
    ("meals2", 159, 160),
    ("open2r", 161, 166),
    ("hrsopen2", 167, 172),
    ("psoda2", 173, 178),
    ("pfry2", 179, 184),
    ("pentree2", 185, 190),
    ("nregs2", 191, 193),
    ("nregs112", 194, 196),
]


def load_raw_data():
    """Load the raw Card & Krueger data."""
    colspecs = [(start, end) for _, start, end in COLSPECS]
    names = [name for name, _, _ in COLSPECS]

    df = pd.read_fwf(
        RAW_DIR / "public.dat",
        colspecs=colspecs,
        names=names,
        na_values=["."]
    )
    return df


def compute_fte(df, suffix=""):
    """Compute full-time equivalent employment."""
    empft_col = f"empft{suffix}"
    emppt_col = f"emppt{suffix}"
    nmgrs_col = f"nmgrs{suffix}"

    # FTE = full-time + 0.5 * part-time + managers
    # Following Card & Krueger's methodology
    fte = df[empft_col] + 0.5 * df[emppt_col] + df[nmgrs_col]
    return fte


def create_panel_format(df):
    """
    Convert wide format to panel (long) format for DiD analysis.
    Each restaurant appears twice: before and after.
    """
    # Create before period
    before = pd.DataFrame({
        "restaurant_id": df["sheet"],
        "state": df["state"].map({1: "NJ", 0: "PA"}),
        "chain": df["chain"].map({1: "BK", 2: "KFC", 3: "Roys", 4: "Wendys"}),
        "period": "before",
        "post": 0,
        "fte": compute_fte(df, ""),
        "wage_st": df["wage_st"],
    })

    # Create after period (only for stores that completed 2nd interview)
    # status2 == 1 means answered 2nd interview
    df_after = df[df["status2"] == 1].copy()
    after = pd.DataFrame({
        "restaurant_id": df_after["sheet"],
        "state": df_after["state"].map({1: "NJ", 0: "PA"}),
        "chain": df_after["chain"].map({1: "BK", 2: "KFC", 3: "Roys", 4: "Wendys"}),
        "period": "after",
        "post": 1,
        "fte": compute_fte(df_after, "2"),
        "wage_st": df_after["wage_st2"],
    })

    # Combine
    panel = pd.concat([before, after], ignore_index=True)

    # Add treatment indicator (NJ = treatment in original)
    panel["treated"] = (panel["state"] == "NJ").astype(int)

    # Sort for nice output
    panel = panel.sort_values(["restaurant_id", "post"]).reset_index(drop=True)

    return panel


def create_version_a(panel):
    """Version A: Original data, no changes."""
    return panel.copy()


def create_version_b(panel):
    """Version B: Flip state labels (NJ <-> PA)."""
    df = panel.copy()
    df["state"] = df["state"].map({"NJ": "PA", "PA": "NJ"})
    # Recalculate treated (now PA is "treatment")
    df["treated"] = (df["state"] == "PA").astype(int)
    return df


def create_version_d(panel):
    """
    Version D: Anonymous (India/Textile).
    - Relabel states: NJ -> Maharashtra, PA -> Gujarat
    - Scale employment by 3 + noise
    - Convert wages to INR with additional noise to break clusters
    - Relabel chains to mill types
    - Change periods to Wave1/Wave2 (fictional)
    - Randomize unit IDs to prevent pattern matching
    """
    df = panel.copy()

    # Relabel states
    df["state"] = df["state"].map({"NJ": "Maharashtra", "PA": "Gujarat"})

    # Scale employment
    noise = np.random.randint(-2, 3, size=len(df))
    df["worker_count"] = (df["fte"] * 3 + noise).round(1)

    # Convert wages to INR with additional noise to break distinctive clusters
    # Base conversion: $4.25 * 83 ≈ 350, $5.05 * 83 ≈ 420
    # Add continuous noise (±15 INR) to obscure the bimodal pattern
    wage_noise = np.random.uniform(-15, 15, size=len(df))
    df["daily_wage_inr"] = (df["wage_st"] * 83 + wage_noise).round(0)

    # Relabel chains to mill types
    df["mill_type"] = df["chain"].map({
        "BK": "Type_A",
        "KFC": "Type_B",
        "Roys": "Type_C",
        "Wendys": "Type_D"
    })

    # Change periods to fictional labels (avoid real dates that could be searched)
    df["period"] = df["period"].map({"before": "Wave1", "after": "Wave2"})

    # Recalculate treated (Maharashtra is treatment)
    df["treated"] = (df["state"] == "Maharashtra").astype(int)

    # Select and rename columns for clean output
    df_out = df[["restaurant_id", "state", "mill_type", "period", "post",
                  "worker_count", "daily_wage_inr", "treated"]].copy()

    # Randomize unit IDs to prevent pattern matching with original C&K data
    n_units = df_out["restaurant_id"].nunique()
    id_mapping = dict(zip(
        df_out["restaurant_id"].unique(),
        np.random.permutation(range(1001, 1001 + n_units))
    ))
    df_out["unit_id"] = df_out["restaurant_id"].map(id_mapping)
    df_out = df_out.drop(columns=["restaurant_id"])

    # Reorder columns
    df_out = df_out[["unit_id", "state", "mill_type", "period", "post",
                      "worker_count", "daily_wage_inr", "treated"]]

    return df_out


def run_did_regression(df, emp_col="fte", treatment_state=None, cluster_col="restaurant_id"):
    """
    Run DiD regression: emp = b0 + b1*treated + b2*post + b3*treated*post + e
    Returns coefficient, std error, t-stat, p-value.
    Uses clustered standard errors at the restaurant level (following C&K methodology).
    """
    import statsmodels.api as sm

    # Drop missing values
    df_reg = df.dropna(subset=[emp_col, "treated", "post"])

    # Create interaction
    df_reg = df_reg.copy()
    df_reg["treated_post"] = df_reg["treated"] * df_reg["post"]

    # Prepare regression
    X = df_reg[["treated", "post", "treated_post"]]
    X = sm.add_constant(X)
    y = df_reg[emp_col]

    # Run OLS with clustered standard errors (following Card & Krueger methodology)
    # Cluster at restaurant level since we have panel data
    if cluster_col in df_reg.columns:
        model = sm.OLS(y, X).fit(cov_type='cluster',
                                  cov_kwds={'groups': df_reg[cluster_col]})
    else:
        # Fallback to robust SEs if cluster column not available
        model = sm.OLS(y, X).fit(cov_type='HC1')

    # Extract DiD coefficient (treated_post)
    coef = model.params["treated_post"]
    se = model.bse["treated_post"]
    tstat = model.tvalues["treated_post"]
    pval = model.pvalues["treated_post"]
    ci_lower, ci_upper = model.conf_int().loc["treated_post"]

    return {
        "coefficient": coef,
        "std_error": se,
        "t_stat": tstat,
        "p_value": pval,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
        "n_obs": len(df_reg),
    }


def main():
    print("Loading raw data...")
    df_raw = load_raw_data()
    print(f"  Loaded {len(df_raw)} observations (restaurants)")

    print("\nCreating panel format...")
    panel = create_panel_format(df_raw)
    print(f"  Panel has {len(panel)} rows ({len(panel)//2} restaurants × 2 periods)")

    # Create all versions
    print("\nCreating dataset versions...")

    version_a = create_version_a(panel)
    version_a.to_csv(PROCESSED_DIR / "version_A_original.csv", index=False)
    print("  Version A (original): saved")

    version_b = create_version_b(panel)
    version_b.to_csv(PROCESSED_DIR / "version_B_flipped.csv", index=False)
    # Version C uses same data file as B (different prompt only)
    version_b.to_csv(PROCESSED_DIR / "version_C_flipped.csv", index=False)
    print("  Version B & C (flipped): saved")

    version_d = create_version_d(panel)
    version_d.to_csv(PROCESSED_DIR / "version_D_anonymous.csv", index=False)
    print("  Version D (anonymous/India): saved")

    # Version E uses same data file as A (different prompt only)
    version_a.to_csv(PROCESSED_DIR / "version_E_contradicts.csv", index=False)
    print("  Version E (contradicts): saved (same data as A)")

    # Run DiD regressions for verification
    print("\n" + "="*60)
    print("LOCAL DiD VERIFICATION")
    print("="*60)

    results = []

    # Version A
    res_a = run_did_regression(version_a, "fte")
    res_a["version"] = "A"
    res_a["treatment_state"] = "NJ"
    results.append(res_a)
    print(f"\nVersion A (Original, NJ=treatment):")
    print(f"  DiD coefficient: {res_a['coefficient']:.3f}")
    print(f"  Std error: {res_a['std_error']:.3f}")
    print(f"  t-stat: {res_a['t_stat']:.3f}, p-value: {res_a['p_value']:.3f}")

    # Version B (same coefficient, different attribution)
    res_b = run_did_regression(version_b, "fte")
    res_b["version"] = "B"
    res_b["treatment_state"] = "PA"
    results.append(res_b)
    print(f"\nVersion B (Flipped, PA=treatment):")
    print(f"  DiD coefficient: {res_b['coefficient']:.3f}")
    print(f"  Std error: {res_b['std_error']:.3f}")
    print(f"  t-stat: {res_b['t_stat']:.3f}, p-value: {res_b['p_value']:.3f}")

    # Version C (same as B)
    res_c = res_b.copy()
    res_c["version"] = "C"
    results.append(res_c)
    print(f"\nVersion C (same as B)")

    # Version D (scaled) - use unit_id for clustering since we renamed it
    res_d = run_did_regression(version_d, "worker_count", cluster_col="unit_id")
    res_d["version"] = "D"
    res_d["treatment_state"] = "Maharashtra"
    results.append(res_d)
    print(f"\nVersion D (Anonymous, Maharashtra=treatment):")
    print(f"  DiD coefficient: {res_d['coefficient']:.3f}")
    print(f"  Std error: {res_d['std_error']:.3f}")
    print(f"  t-stat: {res_d['t_stat']:.3f}, p-value: {res_d['p_value']:.3f}")
    print(f"  (Expected: ~{res_a['coefficient']*3:.3f} due to 3x scaling)")

    # Version E (same as A, data wins over prompt)
    res_e = res_a.copy()
    res_e["version"] = "E"
    res_e["treatment_state"] = "NJ (data) vs PA (prompt)"
    results.append(res_e)
    print(f"\nVersion E (Contradicts, same data as A)")
    print(f"  Data shows treatment effect in: NJ")
    print(f"  Prompt claims treatment is: PA")

    # Save results
    results_df = pd.DataFrame(results)
    results_df = results_df[["version", "treatment_state", "coefficient", "std_error",
                             "t_stat", "p_value", "ci_lower", "ci_upper", "n_obs"]]
    results_df.to_csv(RESULTS_DIR / "local_did_results.csv", index=False)
    print(f"\n\nResults saved to {RESULTS_DIR / 'local_did_results.csv'}")

    # Verification checks
    print("\n" + "="*60)
    print("VERIFICATION CHECKS")
    print("="*60)
    print(f"\n1. A and B have identical coefficients: {np.isclose(res_a['coefficient'], res_b['coefficient'])}")
    print(f"2. D coefficient ≈ 3 × A coefficient: {res_d['coefficient']:.3f} vs {res_a['coefficient']*3:.3f}")
    print(f"   Ratio: {res_d['coefficient'] / res_a['coefficient']:.2f}x (expected: ~3x)")


if __name__ == "__main__":
    main()
