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
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    print(f"wrote {dest} ({dest.stat().st_size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
