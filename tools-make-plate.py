"""Turn an Encyclopedie scan into an alpha-only plate asset.

The page uses these images as CSS masks: the alpha channel IS the ink, and
the colour comes from background-color. So RGB is irrelevant; only the
alpha matters, and it has to be clean — paper grain left in the alpha
reads as haze once the plate is tinted and scaled up.
"""
from PIL import Image, ImageOps
import sys

SRC = 'casse-cc0.jpg'


def make(name, box, width, paper=210, ink=55, gamma=1.35, quality=72):
    im = Image.open(SRC).convert('L')
    if box:
        im = im.crop(box)

    # Normalise: everything at or above `paper` becomes fully transparent,
    # everything at or below `ink` fully opaque, linear in between.
    lut = []
    for v in range(256):
        if v >= paper:
            a = 0.0
        elif v <= ink:
            a = 1.0
        else:
            a = (paper - v) / (paper - ink)
        lut.append(int(round((a ** gamma) * 255)))
    alpha = im.point(lut)

    h = int(round(alpha.height * (width / alpha.width)))
    alpha = alpha.resize((width, h), Image.LANCZOS)

    out = Image.new('RGBA', alpha.size, (255, 255, 255, 0))
    out.putalpha(alpha)
    path = f'plate-{name}.webp'
    out.save(path, 'WEBP', quality=quality, method=6)

    px = alpha.load()
    lit = sum(1 for y in range(0, h, 7) for x in range(0, width, 7) if px[x, y] > 30)
    total = len(range(0, h, 7)) * len(range(0, width, 7))
    print(f'{path:28} {width}x{h}  ink {lit/total:5.1%}')
    return path


# Coordinates measured on the 900x1400 render, scaled by 3.543 to the original.
# All crops sit INSIDE the engraved border; a hard rectangle would fight the
# feather mask that dissolves each plate's edge.
make('sorts',   (319, 2002, 2976, 2640), 1200)   # Fig 4  - the individual type sorts
make('forme',   (390, 3330, 2834, 4510), 1200)   # Fig 6  - the composed forme
make('figures', (213, 1990, 3011, 4510), 1000)   # Fig 4-6 stacked
