"""Quality control for Fogbank Weather Mast string data."""

from __future__ import annotations


def flag_stuck_channels(readings, tolerance=0.02):
    """Return channel ids whose readings vary less than ``tolerance``."""
    stuck = []
    for channel, series in readings.items():
        if len(series) < 3:
            continue
        if max(series) - min(series) < tolerance:
            stuck.append(channel)
    return stuck
