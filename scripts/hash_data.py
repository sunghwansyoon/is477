from pathlib import Path
import hashlib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUT_FILE = BASE_DIR / "results" / "data_hash_manifest.csv"

def sha256_file(path, chunk_size=8192):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    rows = []

    for file_path in DATA_DIR.rglob("*"):
        if file_path.is_file():
            rows.append({
                "file": str(file_path.relative_to(BASE_DIR)),
                "sha256": sha256_file(file_path),
                "size_bytes": file_path.stat().st_size,
            })

    df = pd.DataFrame(rows).sort_values("file")

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_FILE, index=False)

    print(f"Saved data hash manifest: {OUT_FILE}")

if __name__ == "__main__":
    main()
