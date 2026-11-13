# Tideglass Buoy Mk-II

Firmware, telemetry decoding and the tank-calibration pipeline for the Mk-II
wave-energy buoy used by the Northwind shelf array.

## Release status

**Released - v1.4.0 (2026-01-22).**  The decoder in `src/` is the version that
produced the published campaign dataset, and `data/tank_baseline.csv` is the
exact calibration table shipped with units TB-011 through TB-016.

## Layout

- `src/telemetry_decode.py` - frame parser and QC rules
- `src/calibration.py` - pressure-stack calibration fit
- `data/tank_baseline.csv` - bench calibration table
- `experiments/tank_trials.md` - tank trial log and acceptance numbers
