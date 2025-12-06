# scripts/analyze_food_311.py
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

CLEANED_FILE = Path("data/cleaned/food-inspections-with-311-by-zip-cleaned.csv")
RESULTS_DIR = Path("results")
PLOTS_DIR = RESULTS_DIR / "plots"


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(CLEANED_FILE)
    print(f"Loaded cleaned dataset: {len(df)} rows")

    df["sr_count"] = pd.to_numeric(df["sr_count"], errors="coerce").fillna(0).astype(int)
    df["Zip"] = df["Zip"].astype(str).str.strip()

    df["Results_clean"] = df["Results"].astype(str).str.lower().str.strip()
    df["is_fail"] = df["Results_clean"].eq("fail")

    # Basic distribution and ranking (zip by sr_count)

    zip_rank = (
        df.groupby("Zip", as_index=False, dropna=False)
          .agg(avg_sr_count=("sr_count", "mean"), total_inspections=("Inspection ID", "nunique"))
          .sort_values("avg_sr_count", ascending=False)
    )
    zip_rank_out = RESULTS_DIR / "zip_rank_by_sr_count.csv"
    zip_rank.to_csv(zip_rank_out, index=False)
    print(f"Saved zip ranking: {zip_rank_out}")

    # top 15 ZIPs by avg_sr_count visualization
    top_zip = zip_rank.head(15)
    plt.figure(figsize=(10,8))
    plt.bar(top_zip["Zip"], top_zip["avg_sr_count"])
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Zip Code")
    plt.ylabel("Average Sanitary Complaint Count")
    plt.title("Top 15 ZIP Codes by Average Sanitary 311 Requests")
    plt.tight_layout()
    plot_zip_rank = PLOTS_DIR / "zip_rank_by_sr_count_top15.png"
    plt.savefig(plot_zip_rank)
    plt.close()
    print(f"Plot saved: {plot_zip_rank}")


    # RQ1 - sr_count and fail rate analysis

    fail_vs_sr = (
        df.groupby("Zip", as_index=False)
          .agg(avg_sr_count=("sr_count", "mean"), fail_rate=("is_fail", "mean"), inspections=("Inspection ID", "nunique"))
          .sort_values("avg_sr_count", ascending=False)
    )
    fail_vs_sr_out = RESULTS_DIR / "zip_fail_vs_sr.csv"
    fail_vs_sr.to_csv(fail_vs_sr_out, index=False)
    print(f"Saved fail vs sr_count summary: {fail_vs_sr_out}")

    corr_zip = fail_vs_sr[["avg_sr_count", "fail_rate"]].corr().iloc[0, 1]
    print(f"ZIP-level correlation between avg_sr_count and fail_rate: {corr_zip:.4f}")

    # ZIP-level Pearson correlation + p-value
    r, p = pearsonr(
        fail_vs_sr["avg_sr_count"],
        fail_vs_sr["fail_rate"]
    )

    print(f"ZIP-level Pearson correlation (r): {r:.4f}")
    print(f"P-value: {p:.4e}")

    corr_df = pd.DataFrame([{
        "level": "ZIP",
        "metric": "avg_sr_count vs fail_rate",
        "pearson_r": r,
        "p_value": p,
        "n_zips": len(fail_vs_sr)
    }])

    corr_out = RESULTS_DIR / "correlation_summary.csv"
    corr_df.to_csv(corr_out, index=False)

    print(f"Saved correlation summary: {corr_out}")

    # scatter plot: fail rate vs avg_sr_count
    plt.figure(figsize=(10,8)) 
    plt.scatter(fail_vs_sr["avg_sr_count"], fail_vs_sr["fail_rate"], alpha=0.6) 
    plt.xlabel("Average sr_count (per ZIP)") 
    plt.ylabel("Fail rate") 
    plt.title("Fail Rate vs Sanitary 311 Requests (by ZIP)") 
    plt.tight_layout() 
    plot_fail_vs_sr = PLOTS_DIR / "fail_rate_vs_sr_count_scatter.png" 
    plt.savefig(plot_fail_vs_sr) 
    plt.close() 
    print(f"Plot saved: {plot_fail_vs_sr}")

    # scatter plot with labeled top 10 ZIPs by fail rate
    label_zips = fail_vs_sr.head(10)

    plt.figure(figsize=(10,8))
    plt.scatter(
        fail_vs_sr["avg_sr_count"],
        fail_vs_sr["fail_rate"],
        alpha=0.5
    )

    for _, row in label_zips.iterrows():
        plt.text(
            row["avg_sr_count"],
            row["fail_rate"],
            row["Zip"],
            fontsize=7,
            alpha=0.8,
            ha="center",
            va="bottom",
        )

    plt.xlabel("Average sr_count (per ZIP)")
    plt.ylabel("Fail rate")
    plt.title("Fail Rate vs Sanitary 311 Requests (by ZIP) with Top ZIP Labels")
    plt.tight_layout()
    plot_fail_vs_sr = PLOTS_DIR / "fail_rate_vs_sr_count_scatter_labeled.png"
    plt.savefig(plot_fail_vs_sr)
    plt.close()
    print(f"Plot saved: {plot_fail_vs_sr}")


    # Sensitivity in facility type
    facility_df = df.copy()

    if not facility_df.empty:
        facility_summary = (
            facility_df.groupby("Facility Type", as_index=False)
                    .agg(
                        fail_rate=("is_fail", "mean"),
                        inspections=("Inspection ID", "nunique"),
                    )
                    .sort_values("inspections", ascending=False)
        )

        facility_out = RESULTS_DIR / "facility_type_summary.csv"
        facility_summary.to_csv(facility_out, index=False)
        print(f"Saved facility-type summary: {facility_out}")

        # Top 10 facility types by fail rate
        fac_plot = (
            facility_summary[facility_summary["inspections"] >= 50]
            .sort_values("fail_rate", ascending=False)
            .head(10)
            .copy()
        )

        if not fac_plot.empty:
            plt.figure(figsize=(10,8))
            plt.barh(fac_plot["Facility Type"], fac_plot["fail_rate"])
            plt.xlabel("Fail rate")
            plt.ylabel("Facility Type")
            plt.title("Top Facility Types by Fail Rate (>= 50 inspections)")
            plt.tight_layout()
            plot_facility = PLOTS_DIR / "facility_fail_rate_top.png"
            plt.savefig(plot_facility)
            plt.close()
            print(f"Plot saved: {plot_facility}")
        else:
            print("No facility types available for plotting (with >= 50 inspections)")
    else:
        print("No facility type information; skipping facility-type summary")


    # RQ2 - Scatter plot: facility type fail rate vs sr_count
    facility_zip = (
        df.groupby(["Facility Type", "Zip"], as_index=False)
          .agg(
              avg_sr_count=("sr_count", "mean"),
              fail_rate=("is_fail", "mean"),
              inspections=("Inspection ID", "nunique"),
          )
    )

    facility_zip_plot = facility_zip[(facility_zip["Facility Type"].notna()) & (facility_zip["Facility Type"].str.lower() != "nan")].copy()

    facility_counts = (
        df.groupby("Facility Type")["Inspection ID"].nunique().reset_index(name="inspection_count")
    )

    facility_zip_plot = facility_zip_plot.merge(facility_counts, on="Facility Type", how="left")
    facility_zip_plot = facility_zip_plot[facility_zip_plot["inspection_count"] >= 300]

    if not facility_zip_plot.empty:
        rows = []
        for ft, g in facility_zip.groupby("Facility Type"):
            if g["avg_sr_count"].nunique() < 2:
                continue
            corr_ft = g[["avg_sr_count", "fail_rate"]].corr().iloc[0, 1]
            rows.append({
                "Facility Type": ft,
                "corr_sr_fail": corr_ft,
                "zip_count": g["Zip"].nunique(),
                "total_inspections": g["inspections"].sum()
            })

        facility_sensitivity = (
            pd.DataFrame(rows)
            .sort_values("corr_sr_fail", ascending=False)
        )

        sens_out = RESULTS_DIR / "facility_sr_sensitivity.csv"
        facility_sensitivity.to_csv(sens_out, index=False)
        print(f"Saved facility-type sensitivity summary: {sens_out}")

        plt.figure(figsize=(10,8))
        top_types = (
            facility_zip_plot["Facility Type"]
            .value_counts()
            .nlargest(10)
            .index
        )

        plot_df = facility_zip_plot[
            facility_zip_plot["Facility Type"].isin(top_types)
        ]

        g = sns.FacetGrid(
            plot_df,
            col="Facility Type",
            col_wrap=4,
            height=3
        )

        g.map_dataframe(
            sns.scatterplot,
            x="avg_sr_count",
            y="fail_rate",
            alpha=0.6
        )

        g.set_axis_labels("Average sr_count (per ZIP)", "Fail rate")
        g.set_titles("{col_name}")
        g.fig.suptitle("Facility-Type Fail Rate vs Sanitary 311 Requests", y=1.03)

        fac_comp_plot = PLOTS_DIR / "facility_type_fail_vs_sr_comparison.png"
        plt.savefig(fac_comp_plot)
        plt.close()
        print(f"Plot saved: {fac_comp_plot}")

    # RQ3 - Identify sensitive ZIPs
    sr_thresh = fail_vs_sr["avg_sr_count"].quantile(0.75)
    fail_thresh = fail_vs_sr["fail_rate"].quantile(0.75)

    sensitive_zips = fail_vs_sr[(fail_vs_sr["avg_sr_count"] >= sr_thresh) & (fail_vs_sr["fail_rate"] >= fail_thresh)].copy()

    sensitive_out = RESULTS_DIR / "sensitive_zip_summary.csv"
    sensitive_zips.to_csv(sensitive_out, index=False)
    print(f"Saved sensitive ZIP summary: {sensitive_out}")

    if not sensitive_zips.empty:
        plt.figure(figsize=(10,8))
        # all ZIPs
        plt.scatter(
            fail_vs_sr["avg_sr_count"],
            fail_vs_sr["fail_rate"],
            alpha=0.3,
            label="Other ZIPs"
        )
        # sensitive ZIPs highlighted
        plt.scatter(
            sensitive_zips["avg_sr_count"],
            sensitive_zips["fail_rate"],
            color="red",
            alpha=0.8,
            label="Sensitive ZIPs (>= 75th percentile on both)"
        )

        plt.axvline(sr_thresh, linestyle="--", linewidth=0.8)
        plt.axhline(fail_thresh, linestyle="--", linewidth=0.8)

        for _, row in sensitive_zips.iterrows():
            plt.text(
                row["avg_sr_count"],
                row["fail_rate"],
                row["Zip"],
                fontsize=7,
                ha="center",
                va="bottom"
            )

        plt.xlabel("Average sr_count (per ZIP)")
        plt.ylabel("Fail rate")
        plt.title("Sensitive ZIPs by Fail Rate and Sanitary 311 Requests")
        plt.legend()
        plt.tight_layout()

        sens_plot = PLOTS_DIR / "sensitive_zips_highlighted.png"
        plt.savefig(sens_plot)
        plt.close()
        print(f"Plot saved: {sens_plot}")


    # Geographical summary by zip (for mapping)

    zip_summary = (
        df.groupby("Zip", as_index=False)
          .agg(
              total_inspections=("Inspection ID", "nunique"),
              fails=("is_fail", "sum"),
              fail_rate=("is_fail", "mean"),
              avg_sr_count=("sr_count", "mean"),
          )
    )
    zip_summary_out = RESULTS_DIR / "zip_summary_for_mapping.csv"
    zip_summary.to_csv(zip_summary_out, index=False)
    print(f"Saved geographic zip summary: {zip_summary_out}")


if __name__ == "__main__":
    main()
