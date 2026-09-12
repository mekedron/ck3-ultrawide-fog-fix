#!/usr/bin/env python3
"""Rebuilds thumbnail.png (Workshop preview) and tools/thumbnail-200px.png (a legibility
check at Steam's listing size, not uploaded). Layout lives in thumbnail_layout.py.

The crop window contains water spanning most of the frame width and no HUD element;
water is what makes the bug self-evident: the same bay is brown on the left and blue
on the right. Both screenshots are 5120x1440; CROP is in those coordinates."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from thumbnail_layout import make

OLD = "/home/nikita/Pictures/Screenshots/Screenshot_20260912_162527.png"  # vanilla
NEW = "/home/nikita/Pictures/Screenshots/Screenshot_20260912_163049.png"  # modded
CROP = (700, 320, 3000, 1255)   # 2300x935, 2.46:1, clear of every UI element
OUT = os.path.join(os.path.dirname(__file__), "..", "thumbnail.png")
make(OUT, "FOG TINT FIX", OLD, NEW, CROP, CROP, sub="ULTRAWIDE 32:9")
