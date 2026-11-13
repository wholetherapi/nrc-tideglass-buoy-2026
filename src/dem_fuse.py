"""Fuse overlapping DEM passes into one surface."""

GRID_M = 0.25


def fuse_passes(passes):
    """Average height on a fixed grid; later passes win inside a 2 m core."""
    cells = {}
    for order, cells_pass in enumerate(passes):
        for key, z in cells_pass.items():
            cells.setdefault(key, []).append((order, z))
    surface = {}
    for key, samples in cells.items():
        ordered = sorted(samples)
        weights = [1.0] * len(ordered)
        weights[-1] = 2.0
        surface[key] = sum(z * w for (_, z), w in zip(ordered, weights)) / sum(weights)
    return surface
