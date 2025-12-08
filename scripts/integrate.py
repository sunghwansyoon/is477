from pathlib import Path
import pandas as pd

BASE_DIR = Path.cwd().parent

RAW_DIR = BASE_DIR / "data" / "raw"
OUT_DIR = BASE_DIR / "data" / "integrated"

OUT_DIR.mkdir(parents=True, exist_ok=True)

food_path = RAW_DIR / "Food_Inspections_raw.csv"
sr_path   = RAW_DIR / "311_Service_Requests_sanitary_raw.csv"

food_usecols = [
    "Inspection ID", "DBA Name", "AKA Name", "License #", "Facility Type",
    "Risk", "Address", "City", "State", "Zip", "Inspection Date",
    "Inspection Type", "Results", "Violations", "Latitude", "Longitude"
]

food = pd.read_csv(
    food_path,
    usecols=lambda c: True if c in food_usecols else False,
    dtype={"Zip": "string"},
    low_memory=False,
)

food = food[food["Zip"].notna()].copy()

print("Food rows after filtering:", len(food))

sr_usecols = ["SR_NUMBER", "SR_TYPE", "ZIP_CODE", "CREATED_DATE", "LATITUDE", "LONGITUDE"]

sr = pd.read_csv(
    sr_path,
    usecols=lambda c: True if c in sr_usecols else False,
    dtype={"ZIP_CODE": "string"},
    low_memory=False,
)

sr = sr[sr["ZIP_CODE"].notna()].copy()

print("311 rows after filtering:", len(sr))

sr_counts = (
    sr.groupby("ZIP_CODE", as_index=False)
      .agg(sr_count=("SR_NUMBER", "nunique"))
)

sr_by_type = (
    sr.pivot_table(
        index="ZIP_CODE",
        columns="SR_TYPE",
        values="SR_NUMBER",
        aggfunc="nunique",
        fill_value=0,
    )
    .reset_index()
)

sr_counts_full = sr_counts.merge(sr_by_type, on="ZIP_CODE", how="left")

merged = food.merge(
    sr_counts,
    left_on="Zip",
    right_on="ZIP_CODE",
    how="left",
)

if "sr_count" in merged.columns:
    merged["sr_count"] = merged["sr_count"].fillna(0).astype("int64")

merged.drop(columns=["ZIP_CODE"], inplace=True)

print("Merged rows:", len(merged))

row_level_out = OUT_DIR / "food_inspections_with_311_by_zip.csv"
merged.to_csv(row_level_out, index=False)

print(f"Row-level merged file created at: {row_level_out}")