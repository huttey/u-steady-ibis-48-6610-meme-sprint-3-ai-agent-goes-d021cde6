#!/usr/bin/env python3
"""Meme Sprint 3 entry: writes the meme image to /output/entry.png."""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)

# Gate check: the output must be a whole PNG or JPEG, at most 1 MiB, 1024x1024.
from PIL import Image

im = Image.open(DST)
im.verify()
im = Image.open(DST)
assert im.format in ("PNG", "JPEG"), im.format
assert im.size == (1024, 1024), im.size
assert os.path.getsize(DST) <= 1048576, os.path.getsize(DST)
print("wrote", DST, os.path.getsize(DST), "bytes",
      "format=%s" % im.format, "size=%s" % (im.size,))
