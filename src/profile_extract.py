"""Scan-line segmentation for foredune profiles."""

import math

MIN_POINTS = 40
MAX_GAP_M = 1.5


def segment_scanline(points):
    """Split a raw scanline into contiguous segments."""
    segments, current = [], []
    for point in points:
        if current and abs(point["x"] - current[-1]["x"]) > MAX_GAP_M:
            if len(current) >= MIN_POINTS:
                segments.append(current)
            current = []
        current.append(point)
    if len(current) >= MIN_POINTS:
        segments.append(current)
    return segments


def profile_length(segment):
    total = 0.0
    for left, right in zip(segment, segment[1:]):
        total += math.dist((left["x"], left["z"]), (right["x"], right["z"]))
    return round(total, 2)
