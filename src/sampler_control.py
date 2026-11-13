"""Syringe-rack sequencer for the Saltmarsh Sampler Mk-I."""

import time

RACK_SIZE = 12
DWELL_SECONDS = 42


def plan_sequence(plots, replicates=3):
    """Build a flat sampling plan for a list of plot ids."""
    plan = []
    for plot in plots:
        for rep in range(replicates):
            plan.append({"plot": plot, "replicate": rep + 1})
    if len(plan) > RACK_SIZE:
        raise ValueError("plan exceeds the 12-position rack")
    return plan


def run_sequence(plan, advance=None):
    """Execute the plan, waiting DWELL_SECONDS between positions."""
    advance = advance or (lambda: time.sleep(DWELL_SECONDS))
    log = []
    for position, step in enumerate(plan, start=1):
        advance()
        log.append({"position": position, **step})
    return log
