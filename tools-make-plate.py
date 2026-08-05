"""Rebuild the background plate assets from their source scans.

The page uses these images as CSS masks: the alpha channel IS the ink, and
the colour comes from background-color. RGB is irrelevant; only alpha
matters, and it has to be clean — paper grain left in the alpha reads as
haze once the plate is tinted and scaled up.

Source scans are NOT in the repo. Download them next to this script first:

  casse-cc0.jpg   Pl. 1, Imprimerie en Lettres, L'Operation de la casse
                  Musee Carnavalet via Wikimedia Commons, CC0
  casse-grid.jpg  Imprimerie, Casse (the compositor's type case)
                  Commons / Gallica (BnF), CC BY-SA 4.0 - see DEPLOYMENT.md,
                  this one obliges the colophon credit

Then: python3 tools-make-plate.py && cp plate-*.webp images/
"""
from PIL import Image, ImageDraw


def make(src, out_name, box, width, paper, ink, gamma, quality, alpha_quality,
         patch=None):
    im = Image.open(src).convert('L')

    # Anything painted out has to go before thresholding — greyscale turns a
    # coloured library stamp into ink like any other mark.
    if patch:
        ImageDraw.Draw(im).rectangle(patch, fill=232)

    im = im.crop(box)

    # Normalise: at or above `paper` is fully transparent, at or below `ink`
    # fully opaque, linear between. gamma bends the midtones off the paper.
    lut = [0 if v >= paper else 255 if v <= ink else
           int(round((((paper - v) / (paper - ink)) ** gamma) * 255))
           for v in range(256)]
    alpha = im.point(lut)

    alpha = alpha.resize((width, round(alpha.height * (width / alpha.width))),
                         Image.LANCZOS)

    out = Image.new('RGBA', alpha.size, (255, 255, 255, 0))
    out.putalpha(alpha)
    # alpha_quality is what keeps these near 150 KB instead of 300 KB. Dense
    # engraved hatching is expensive to store losslessly and costs nothing
    # visible at background opacity.
    out.save(out_name, 'WEBP', quality=quality, alpha_quality=alpha_quality,
             method=6)
    print(f'{out_name:24} {alpha.size[0]}x{alpha.size[1]}')


# Left plate: Fig 4-6 — type sorts, composing stick, composed forme. Cropped
# inside the engraved border, which would otherwise fight the feather mask
# that dissolves each plate's edge.
make('casse-cc0.jpg', 'plate-forme.webp',
     box=(213, 1990, 3011, 4510), width=860,
     paper=210, ink=55, gamma=1.35, quality=60, alpha_quality=60)

# Right plate: the type case itself. `patch` covers a red accession stamp.
make('casse-grid.jpg', 'plate-typecase.webp',
     box=(48, 52, 722, 1108), width=780,
     paper=206, ink=60, gamma=1.3, quality=60, alpha_quality=58,
     patch=[57, 1027, 106, 1093])
