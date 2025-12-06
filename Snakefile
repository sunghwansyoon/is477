rule all:
    input:
        "results/zip_rank_by_sr_count.csv",
        "results/zip_fail_vs_sr.csv",
        "results/facility_type_summary.csv",
        "results/zip_summary_for_mapping.csv",
        "results/sensitive_zip_summary.csv",
        "results/plots/zip_rank_by_sr_count_top15.png",
        "results/plots/fail_rate_vs_sr_count_scatter.png",
        "results/plots/fail_rate_vs_sr_count_scatter_labeled.png",
        "results/plots/sensitive_zips_highlighted.png",

rule analyze:
    input:
        "data/cleaned/food-inspections-with-311-by-zip-cleaned.csv"
    output:
        "results/zip_rank_by_sr_count.csv",
        "results/zip_fail_vs_sr.csv",
        "results/facility_type_summary.csv",
        "results/zip_summary_for_mapping.csv",
        "results/sensitive_zip_summary.csv",
        "results/plots/zip_rank_by_sr_count_top15.png",
        "results/plots/fail_rate_vs_sr_count_scatter.png",
        "results/plots/fail_rate_vs_sr_count_scatter_labeled.png",
        "results/plots/sensitive_zips_highlighted.png",
    shell:
        "python3 scripts/analyze_food_311.py"