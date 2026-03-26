"""
filter_aromatic_pha.py

Filters bioplastic replacement candidates to remove copolymers/blends
where any PHA monomer contains aromatic atoms. Aromatic PHA monomers
are harder to produce biologically and harder to biodegrade, making
them less viable for real-world bioplastic applications.

Usage:
    python filter_aromatic_pha.py

Input:  export/candidates.csv
Output: export/candidates_no_aromatic.csv
"""

import sys
from pathlib import Path

import pandas as pd

# Add bioplastic_design/ to the Python path so we can import utils
BIOPLASTIC_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BIOPLASTIC_DIR))

from utils.chemistry import pha_monomers_have_aromatic

EXPORT_DIR = BIOPLASTIC_DIR / "export"
INPUT_CSV = EXPORT_DIR / "candidates.csv"
OUTPUT_CSV = EXPORT_DIR / "candidates_no_aromatic.csv"


def main():
    df = pd.read_csv(INPUT_CSV)
    print(f"Loaded {len(df)} candidates from {INPUT_CSV.name}")

    # Flag rows where any PHA monomer contains aromatic atoms
    df["pha_aromatic"] = df.apply(
        lambda row: pha_monomers_have_aromatic(row["smiles"], row["names"]),
        axis=1,
    )

    # Report
    n_aromatic = df["pha_aromatic"].sum()
    n_clean = (~df["pha_aromatic"]).sum()
    print(f"  Aromatic PHA monomers: {n_aromatic}")
    print(f"  Aliphatic PHA monomers: {n_clean}")
    print()
    print("Breakdown by polymer:")
    breakdown = df.groupby("abb")["pha_aromatic"].value_counts().unstack(fill_value=0)
    breakdown.columns = ["aliphatic", "aromatic"]
    print(breakdown.to_string())

    # Filter and save
    df_clean = df[~df["pha_aromatic"]].drop(columns="pha_aromatic")
    df_clean.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSaved {len(df_clean)} candidates to {OUTPUT_CSV.name}")


if __name__ == "__main__":
    main()