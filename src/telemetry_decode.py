"""Frame decoder for the Tideglass Mk-II buoy telemetry stream."""

import struct

FRAME_MAGIC = b"TGB2"
HEADER = struct.Struct("<4sIHH")


def split_frames(stream: bytes):
    """Yield complete frames from a raw byte stream."""
    cursor = 0
    while cursor + HEADER.size <= len(stream):
        magic, seq, length, flags = HEADER.unpack_from(stream, cursor)
        if magic != FRAME_MAGIC:
            cursor += 1
            continue
        end = cursor + HEADER.size + length
        if end > len(stream):
            return
        yield seq, flags, stream[cursor + HEADER.size:end]
        cursor = end


def decode_pressure(payload: bytes):
    """Decode packed 24-bit pressure samples (0.1 hPa LSB)."""
    if len(payload) % 3:
        raise ValueError("pressure payload must be a multiple of 3 bytes")
    values = []
    for i in range(0, len(payload), 3):
        raw = payload[i] | (payload[i + 1] << 8) | (payload[i + 2] << 16)
        if raw & 0x800000:
            raw -= 1 << 24
        values.append(raw / 10.0)
    return values
