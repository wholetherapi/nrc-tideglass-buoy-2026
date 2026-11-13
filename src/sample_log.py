"""Reader for the sampler binary log format (SLG1)."""

import struct

RECORD = struct.Struct("<4sHHff")


def read_records(blob):
    records = []
    for offset in range(0, len(blob) - RECORD.size + 1, RECORD.size):
        magic, position, flags, pore_pressure, salinity = RECORD.unpack_from(blob, offset)
        if magic != b"SLG1":
            continue
        records.append(
            {
                "position": position,
                "flags": flags,
                "pore_pressure_kpa": round(pore_pressure, 3),
                "salinity_psu": round(salinity, 2),
            }
        )
    return records
