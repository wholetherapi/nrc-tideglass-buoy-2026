# Shelf Instruments Toolkit

Released reference implementations for the Shelf Observatory Campaign 2026
instrument fleet.  One repository carries the production code for the Tideglass
Buoy Mk-II telemetry stack, the Saltmarsh Sampler controller, the Dune Profile
Rover survey pipeline and the Fogbank Weather Mast quality-control chain.

## Release status

**Released - v2.3.0 (2026-04-18).**  This is the version that produced the
published campaign datasets.  Calibration tables and survey registries under
`data/` are the exact files shipped with the field units.

## Layout

- `src/telemetry_decode.py` - tideglass frame parser and QC rules
- `src/calibration.py` - tideglass pressure-stack calibration fit
- `src/sampler_control.py` - saltmarsh syringe rack sequencing
- `src/sample_log.py` - saltmarsh binary log reader
- `src/profile_extract.py` - rover scan-line segmentation
- `src/dem_fuse.py` - rover pass fusion
- `data/` - bench and survey tables
- `experiments/` - tank, intertidal and beach trial notes
