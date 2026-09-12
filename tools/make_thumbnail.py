#!/usr/bin/env python3
"""Build thumbnail.png from a vanilla screenshot and a modded one.

The crop window is chosen so that no HUD element is inside it - no pause label,
resource bar, portrait, minimap or right-hand icon column - and so that it contains
water spanning most of the frame width. Water is what makes the bug self-evident:
the same bay is brown on the left and blue on the right.

Both screenshots must be 5120x1440; CROP is in those coordinates.
"""
from PIL import Image, ImageDraw, ImageFont

OLD = "/home/nikita/Pictures/Screenshots/Screenshot_20260912_162527.png"  # vanilla
NEW = "/home/nikita/Pictures/Screenshots/Screenshot_20260912_163049.png"  # modded
OUT = "/home/nikita/Projects/ck3-ultrawide-fog-fix/thumbnail.png"

S = 1280
H = S // 2
CROP = (700, 250, 3000, 1400)   # 2300x1150, 2:1, clear of every UI element

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def half(path):
    return Image.open(path).convert("RGB").crop(CROP).resize((S, H), Image.LANCZOS)


canvas = Image.new("RGB", (S, S))
canvas.paste(half(OLD), (0, 0))
canvas.paste(half(NEW), (0, H))

d = ImageDraw.Draw(canvas, "RGBA")
big = ImageFont.truetype(FB, 62)
small = ImageFont.truetype(FR, 28)


def badge(y_top, title, sub):
    pad_x, pad_y = 26, 18
    w = int(max(d.textlength(title, font=big), d.textlength(sub, font=small))) + pad_x * 2
    h = pad_y * 2 + 62 + 10 + 32
    d.rectangle([28, y_top, 28 + w, y_top + h], fill=(12, 10, 8, 205))
    d.text((28 + pad_x, y_top + pad_y), title, font=big, fill=(245, 238, 225, 255))
    d.text((28 + pad_x, y_top + pad_y + 70), sub, font=small, fill=(198, 176, 132, 255))


badge(30, "BEFORE", "vanilla: one bay, brown on the left")
badge(H + 30, "AFTER", "the same water all the way across")

d.rectangle([0, H - 3, S, H + 2], fill=(196, 168, 116, 255))

# rebuild from raw pixels so no source metadata survives, then quantise to stay
# under Steam's 1 MB preview limit at full 1280x1280
clean = Image.new("RGB", canvas.size)
clean.putdata(list(canvas.getdata()))
clean = clean.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG)
clean.save(OUT, "PNG", optimize=True)

import os
print("saved", OUT, clean.size, os.path.getsize(OUT), "bytes")
