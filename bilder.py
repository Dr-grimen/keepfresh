#!/usr/bin/env python3
"""Lagar produktbilete: fjernar tekstbanner, trimmar kantar, beskjer til kvadrat."""
from PIL import Image, ImageChops

def bakgrunnsfarge(im):
    k = [im.getpixel(p) for p in
         [(0,0),(im.width-1,0),(0,im.height-1),(im.width-1,im.height-1)]]
    return tuple(sum(c[i] for c in k)//4 for i in range(3))

def trim(im, toleranse=14):
    bg = Image.new("RGB", im.size, bakgrunnsfarge(im))
    diff = ImageChops.difference(im, bg).convert("L").point(lambda p: 255 if p > toleranse else 0)
    boks = diff.getbbox()
    return im.crop(boks) if boks else im

def lag(src, dst, kutt=None, storleik=1000, luft=0.05):
    im = Image.open(src).convert("RGB")
    if kutt:                                    # (topp, botn) i prosent — fjernar tekstbanner
        t, b = kutt
        im = im.crop((0, int(im.height*t), im.width, int(im.height*(1-b))))
    im = trim(im)
    bg = bakgrunnsfarge(im)
    # heile biletet blir med — vi fyller ut til kvadrat med bakgrunnsfargen frå
    # biletet sjølv, så det ikkje blir harde kvite stolpar og ikkje zoomar inn
    s = int(max(im.size) * (1 + 2*luft))
    lerret = Image.new("RGB", (s, s), bg)
    lerret.paste(im, ((s - im.width)//2, (s - im.height)//2))
    lerret.resize((storleik, storleik), Image.LANCZOS).save(dst, "WEBP", quality=90)

JOBBAR = [
    ("bilder-nye2/n-8.jpg",  "bilder/mini-1.webp",    None),
    ("bilder-nye2/n-6.jpg",  "bilder/mini-3.webp",    (0.20, 0)),
    ("bilder-nye2/n-4.jpg",  "bilder/mini-4.webp",    None),

    ("raa/classic/c-6.jpg",  "bilder/classic-1.webp", (0.24, 0)),
    ("raa/classic/c-1.jpg",  "bilder/classic-2.webp", None),
    ("raa/classic/c-3.jpg",  "bilder/classic-3.webp", (0.20, 0)),
    ("raa/classic/c-4.jpg",  "bilder/classic-4.webp", (0.26, 0)),

    ("raa/duck/d-6.jpg",     "bilder/duck-1.webp",    None),
    ("raa/duck/d-1.jpg",     "bilder/duck-2.webp",    (0.20, 0.38)),
    # duck-3 er eit utsnitt av d-3, sjå historikk
]

if __name__ == "__main__":
    for src, dst, kutt in JOBBAR:
        lag(src, dst, kutt)
        print(dst.split("/")[-1])
