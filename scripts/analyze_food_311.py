# scripts/analyze_food_311.py
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CLEANED_FILE = Path("data/cleaned/food-inspections-with-311-by-zip-cleaned.csv")
RESULTS_DIR = Path("results")
PLOTS_DIR = RESULTS_DIR / "plots"


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(CLEANED_FILE, low_memory=False)
    print(f"Loaded cleaned dataset: {len(df)} rows")

    df["sr_count"] = pd.to_numeric(df["sr_count"], errors="coerce").fillna(0).astype(int)
    df["Zip"] = df["Zip"].astype(str).str.strip()

    df["Results_clean"] = df["Results"].astype(str).str.lower().str.strip()
    df["is_fail"] = df["Results_clean"].eq("fail")

    # 1. Basic distribution and ranking (zip by sr_count)

    zip_rank = (
        df.groupby("Zip", as_index=False)
          .agg(avg_sr_count=("sr_count", "mean"), total_inspections=("Inspection ID", "nunique"))
          .sort_values("avg_sr_count", ascending=False)
    )
    zip_rank_out = RESULTS_DIR / "zip_rank_by_sr_count.csv"
    zip_rank.to_csv(zip_rank_out, index=False)
    print(f"Saved zip ranking: {zip_rank_out}")

    # top 15 ZIPs by avg_sr_count visualization
    top_zip = zip_rank.head(15)
    plt.figure()
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


    # 2. sr_count and fail rate analysis

    fail_vs_sr = (
        df.groupby("Zip", as_index=False)
          .agg(avg_sr_count=("sr_count", "mean"), fail_rate=("is_fail", "mean"), inspections=("Inspection ID", "nunique"))
          .sort_values("avg_sr_count", ascending=False)
    )
    fail_vs_sr_out = RESULTS_DIR / "zip_fail_vs_sr.csv"
    fail_vs_sr.to_csv(fail_vs_sr_out, index=False)
    print(f"Saved fail vs sr_count summary: {fail_vs_sr_out}")

    corr = df[["sr_count", "is_fail"]].corr().iloc[0, 1]
    print(f"Correlation between sr_count and is_fail: {corr:.4f}")

    # Scatter plot: avg_sr_count vs fail_rate
    plt.figure()
    plt.scatter(fail_vs_sr["avg_sr_count"], fail_vs_sr["fail_rate"], alpha=0.6)
    plt.xlabel("Average sr_count (per ZIP)")
    plt.ylabel("Fail rate")
    plt.title("Fail Rate vs Sanitary 311 Requests (by ZIP)")
    plt.tight_layout()
    plot_fail_vs_sr = PLOTS_DIR / "fail_rate_vs_sr_count_scatter.png"
    plt.savefig(plot_fail_vs_sr)
    plt.close()
    print(f"Plot saved: {plot_fail_vs_sr}")


    # 3. sensitivity in facility type

    facility_df = df.copy()

    if not facility_df.empty:
        # Aggregate WITHOUT avg_sr_count (sr_count removed from output)
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
            facility_summary
            .sort_values("fail_rate", ascending=False)
            .head(10)
            .copy()
        )

        if not fac_plot.empty:
            plt.figure()
            plt.barh(fac_plot["Facility Type"], fac_plot["fail_rate"])
            plt.xlabel("Fail rate")
            plt.ylabel("Facility Type")
            plt.title("Top Facility Types by Fail Rate (all facility types)")
            plt.tight_layout()
            plot_facility = PLOTS_DIR / "facility_fail_rate_top.png"
            plt.savefig(plot_facility)
            plt.close()
            print(f"Plot saved: {plot_facility}")
        else:
            print("No facility types available for plotting")
    else:
        print("No facility type information; skipping facility-type summary")


    # 4. geographical summary by zip (for mapping)

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
