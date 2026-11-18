#!/usr/bin/env python3
"""Deterministically write the bundled entry image to an output directory.

Usage:
    python3 main.py                 # writes to /output/entry.png
    python3 main.py /tmp/out1       # writes to /tmp/out1/entry.png

No network access at runtime. The bundled image (entry.png, next to this
file) is copied byte-for-byte, so repeated runs produce identical output.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEFAULT_OUTPUT_DIR = Path("/output")


def main(argv: list[str]) -> int:
    output_dir = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    data = dest.read_bytes()
    if len(data) > 1048576:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > 1024 or height > 1024:
        raise SystemExit(f"entry.png is {width}x{height}, over the 1024x1024 limit")
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {dest} ({len(data)} bytes, {width}x{height}, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
