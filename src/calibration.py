"""Pressure-stack calibration for the Tideglass buoy."""

import csv

DEFAULT_TABLE = "data/tank_baseline.csv"


def load_baseline(path=DEFAULT_TABLE):
    rows = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows.append(
                {
                    "depth_m": float(row["depth_m"]),
                    "raw_hpa": float(row["raw_hpa"]),
                    "reference_hpa": float(row["reference_hpa"]),
                }
            )
    return rows


def fit_offset(rows):
    """Least-squares offset between raw and reference pressure."""
    diffs = [r["raw_hpa"] - r["reference_hpa"] for r in rows]
    return sum(diffs) / len(diffs)
