#!/usr/bin/env python3
"""Byggjer FreshSeal-butikken: framside + éi side per produkt.

Køyr:  python3 bygg.py
Alt innhald ligg i PRODUKT under. Endrar du pris eller tekst, endrar du her
og køyrer skriptet på nytt — då blir alle sidene oppdaterte likt.
"""

V = "3"  # versjonsnummer på css/bilete, auk denne når du endrar bilete

PRODUKT = [
    {
        "slug": "mini-sealer",
        "namn": "FreshSeal Mini Sealer",
        "kort": "Mini Sealer",
        "teaser": "Oppladbar, med kutter og magnet. Flaggskipet.",
        "pris": "$24.99",
        "bilete": [
            ("mini-1", "FreshSeal Mini Sealer in white"),
            ("mini-2", "Mini Sealer with USB-C charging cable"),
            ("mini-3", "Sealer, cutter, magnetic base and charging port"),
            ("mini-4", "Mini Sealer held on a fridge door by its magnet"),
            ("mini-5", "Sealing a coffee bag"),
        ],
        "bundlar": [
            ("1", "$24.99", None, None, "1 Sealer"),
            ("2", "$39.99", "$49.98", "Most popular", "2 Sealers"),
            ("3", "$54.99", "$74.97", "Best value", "3 Sealers"),
        ],
        "intro": "Not sure a mini sealer will actually earn a spot in your kitchen? We get it. "
                 "That's why your purchase is backed by our hassle-free return policy — if it "
                 "doesn't work for you, send it back, no hard feelings.",
        "punkt": [
            "Seals any plastic bag airtight in one pass — chips, coffee, pasta, frozen food",
            "Built-in cutter opens the bag again cleanly, so it does both jobs",
            "USB-C rechargeable — no batteries to buy, and no cable left plugged in",
            "Magnetic base: it lives on the fridge door instead of lost in a drawer",
            "Lit power switch so you can see when it is on",
        ],
        "utro": "For $24.99, the only real risk is leaving food to go stale without one.",
        "stell": [
            "Wipe the sealing strip clean when it is cool — never rinse the unit",
            "Charge with the supplied USB-C cable; a full charge lasts weeks of normal use",
            "Store in a cool, dry place away from direct sunlight",
        ],
        "kjelde": "4.9 out of 5 from 653 reviews",
        "omtalar": [
            ("Very practical, with an illuminated on/off switch for safety. It has a small blade to "
             "open packages by turning it, or to cut excess material when sealing in the normal "
             "position.", "E***r · verified purchase · 8 January 2026"),
            ("The truth is that it works quite well, and the fact that it is rechargeable and has a "
             "magnetic base lets you keep it in your kitchen without any problem.",
             "Verified purchase · 6 December 2025"),
            ("Better than the cheaper versions. It seals well and heats up immediately after turning "
             "on, which makes securing the packaging easier and more efficient.",
             "I***k · verified purchase · 1 November 2025"),
        ],
    },
    {
        "slug": "classic",
        "namn": "FreshSeal Classic",
        "kort": "Classic",
        "teaser": "Den enkle. Over 100 000 selde.",
        "pris": "$24.99",
        "bilete": [
            ("classic-1", "FreshSeal Classic in white"),
            ("classic-2", "Classic sealing a bag by hand"),
            ("classic-3", "Sealing a freezer bag"),
            ("classic-4", "Classic slipped into a coat pocket"),
            ("classic-5", "Four examples of bags being sealed"),
        ],
        "bundlar": [("1", "$24.99", None, None, "1 Sealer")],
        "intro": "The plain one. No charging, no extra functions — you press it along the bag and it "
                 "closes airtight. Over 100,000 people have bought this exact model, and it is the "
                 "most proven sealer we sell.",
        "punkt": [
            "One squeeze and a slide, and the bag is sealed shut",
            "Runs on 2 AA batteries — ready the second it arrives (batteries not included)",
            "Small enough for a coat pocket or a drawer",
            "Nothing to charge, nothing to break",
        ],
        "utro": "The same price as the rest of the range, and the one most people start with.",
        "stell": [
            "Wipe the sealing strip clean when it is cool — never rinse the unit",
            "Take the batteries out if you are storing it for a long time",
            "Store in a cool, dry place away from direct sunlight",
        ],
        "kjelde": "4.9 out of 5 from 29,765 reviews",
        "omtalar": [
            ("Love the size, works great. Awesome product at a very affordable price. Light weight. "
             "Perfect for what I need it for.", "Verified purchase · 3 October 2025"),
            ("The sealer arrived well packaged and in perfect condition. No need to wait for it to "
             "heat up — I put the batteries in and used it right away. Very useful for frozen bags. "
             "I will surely buy some more.", "E***r · verified purchase · 13 November 2025"),
        ],
    },
    {
        "slug": "duck",
        "namn": "FreshSeal Duck",
        "kort": "Duck",
        "teaser": "Same jobb, men den sit på kjøleskapet og ser deg i auga.",
        "pris": "$24.99",
        "bilete": [
            ("duck-1", "FreshSeal Duck, a duck-shaped bag sealer"),
            ("duck-2", "The Duck sealing a snack bag"),
            ("duck-3", "Four things the Duck can seal"),
            ("duck-4", "The Duck, open and closed"),
            ("duck-5", "How to use the Duck, step by step"),
        ],
        "bundlar": [("1", "$24.99", None, None, "1 Duck")],
        "intro": "It is a duck. It is also a perfectly good bag sealer with a cutter, a magnet and "
                 "USB charging. Both things are true at once, and that is the point.",
        "punkt": [
            "Seals and cuts, exactly like the Mini Sealer does",
            "USB rechargeable, with a magnet so it hangs on the fridge",
            "A safety button so it does not heat up in a drawer by accident",
            "The one kitchen gadget people actually comment on",
        ],
        "utro": "Buy it for the joke, keep it because it works.",
        "stell": [
            "Wipe the sealing strip clean when it is cool — never rinse the unit",
            "Charge over USB; a full charge lasts weeks of normal use",
            "Store in a cool, dry place away from direct sunlight",
        ],
        "kjelde": "4.9 out of 5 from 138 reviews",
        "omtalar": [
            ("That's so cute — a real eye-catcher in the kitchen. Very practical with the magnet for "
             "hanging and USB charging. Works very well, and the cutting function is there too. "
             "Absolutely recommended.", "C***g · verified purchase · 13 September 2025"),
            ("I bought it without much expectation, but when I used it I was much more satisfied "
             "than expected. I was worried about how it would look in reality since I chose it from "
             "photos only — the quality was outstanding.", "Verified purchase · 2025"),
        ],
    },
]


def hovud(tittel, skildring, aktiv=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tittel}</title>
<meta name="description" content="{skildring}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={V}">
</head>
<body>

<div class="announce">Free shipping on all orders</div>

<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html">FreshSeal<span>.</span></a>
    <nav class="nav">
      <a href="index.html">Shop</a>
      <a href="faq.html">FAQ</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
</header>
"""


BUNN = """
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="index.html">FreshSeal<span>.</span></a>
        <p>Bag sealers that keep your food fresh, cut waste, and save you money — free shipping,
           30-day returns.</p>
      </div>
      <div>
        <h4>Shop</h4>
        <ul>
          <li><a href="mini-sealer.html">Mini Sealer</a></li>
          <li><a href="classic.html">Classic</a></li>
          <li><a href="duck.html">Duck</a></li>
        </ul>
      </div>
      <div>
        <h4>Help</h4>
        <ul>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="shipping.html">Shipping &amp; Returns</a></li>
          <li><a href="contact.html">Contact Us</a></li>
          <li><a href="about.html">About</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">&copy; 2026 FreshSeal. All rights reserved.</div>
  </div>
</footer>

</body>
</html>
"""


def produktside(p):
    hero, hero_alt = p["bilete"][0]
    AKTIV = ' aria-current="true"'
    thumbs = "\n".join(
        '        <button%s><img src="bilder/%s.webp?v=%s" alt="%s"></button>'
        % (AKTIV if i == 0 else "", f, V, alt)
        for i, (f, alt) in enumerate(p["bilete"]))

    bundlar = ""
    for pack, pris, fyr, merke, namn in p["bundlar"]:
        tag = f'\n          <span class="b-tag">{merke}</span>' if merke else ""
        s = f' <s>{fyr}</s>' if fyr else ""
        akt = ' aria-current="true"' if pack == "1" else ""
        bundlar += (f'        <button class="bundle" data-pack="{pack}" data-price="{pris}"{akt}>\n'
                    f'          <span class="b-name">{namn}</span>\n'
                    f'          <span class="b-price">{pris}{s}</span>{tag}\n'
                    f'        </button>\n')

    punkt = "\n".join(f"            <li>{x}</li>" for x in p["punkt"])
    stell = "\n".join(f"            <li>{x}</li>" for x in p["stell"])
    omt = "\n".join(
        f'      <article class="review">\n'
        f'        <div class="stars">★★★★★</div>\n'
        f'        <p>"{tekst}"</p>\n'
        f'        <div class="who">{kven}</div>\n'
        f'      </article>\n' for tekst, kven in p["omtalar"])

    lenker = ",\n    ".join(
        f'{pack}: "https://buy.stripe.com/{p["slug"].upper()}-{pack}-STK"'
        for pack, *_ in p["bundlar"])

    return hovud(f'{p["namn"]} | FreshSeal', p["teaser"]) + f"""
<div class="crumb">
  <div class="wrap"><a href="index.html">Shop</a><span>&rsaquo;</span>{p["kort"]}</div>
</div>

<main class="wrap">
  <div class="product">

    <div>
      <div class="gallery-main">
        <img id="mainImage" src="bilder/{hero}.webp?v={V}" alt="{hero_alt}">
      </div>
      <div class="thumbs" id="thumbs">
{thumbs}
      </div>
    </div>

    <div>
      <h1>{p["namn"]}</h1>
      <div class="price" id="price">{p["pris"]}</div>

      <div class="bundles" id="bundles">
{bundlar}      </div>

      <!-- STRIPE: lim inn Payment Link-ane dine i STRIPE-objektet nedst på sida. -->
      <a class="btn-buy" id="buyButton" href="#">Pay Now</a>

      <div class="assurance">
        <div><span class="ico">🚚</span>Free Shipping</div>
        <div><span class="ico">↩︎</span>30-Day Returns</div>
        <div><span class="ico">🔒</span>Secure Checkout</div>
      </div>

      <details class="panel" open>
        <summary>Description</summary>
        <div class="body">
          <p>{p["intro"]}</p>
          <p><strong>Here's what you're getting:</strong></p>
          <ul>
{punkt}
          </ul>
          <p>{p["utro"]}</p>
        </div>
      </details>

      <details class="panel">
        <summary>Shipping &amp; Returns</summary>
        <div class="body">
          <ul>
            <li>Free shipping on every order</li>
            <li>Delivery in 8&ndash;14 days with tracking</li>
            <li>Free returns within 30 days of delivery</li>
            <li>If we cannot deliver to your address, you get a full refund</li>
          </ul>
        </div>
      </details>

      <details class="panel">
        <summary>Care Instructions</summary>
        <div class="body">
          <ul>
{stell}
          </ul>
        </div>
      </details>
    </div>

  </div>
</main>

<section class="promise">
  <div class="wrap">
    <h2>Our promise</h2>
    <div class="promise-grid">
      <div>
        <h3>Try it for 30 days</h3>
        <p>Use it, test it on your own bags. If it is not for you, send it back within 30 days and
           we refund you in full.</p>
      </div>
      <div>
        <h3>It arrives, or you don't pay</h3>
        <p>Every order ships with tracking. If your parcel is lost, damaged, or we cannot deliver
           to your address, you get your money back — no argument.</p>
      </div>
      <div>
        <h3>A person answers</h3>
        <p>Write to us and a human reads it, usually the same day. No ticket numbers, no chatbot
           sending you in circles.</p>
      </div>
    </div>

    <div class="reviews-src">
      <h3>What buyers say about this sealer</h3>
      <p class="src-note">Reviews of this exact model from verified purchases on our supplier's
         AliExpress listing — {p["kjelde"]}. They are not FreshSeal customers, because FreshSeal is
         new. We show them so you can judge the product itself.</p>

{omt}    </div>

    <div class="reviews-empty">
      <p>No FreshSeal reviews yet. Yours would be the first, and it will appear here exactly as
         you write it.</p>
    </div>
  </div>
</section>
{BUNN.replace('</body>', '''<script>
  var STRIPE = {
    ''' + lenker + '''
  };

  var bundles = document.getElementById('bundles');
  var buy = document.getElementById('buyButton');
  var priceEl = document.getElementById('price');
  buy.href = STRIPE[1];
  bundles.addEventListener('click', function (e) {
    var btn = e.target.closest('.bundle');
    if (!btn) return;
    Array.prototype.forEach.call(bundles.children, function (b) {
      b.setAttribute('aria-current', b === btn ? 'true' : 'false');
    });
    priceEl.textContent = btn.dataset.price;
    buy.href = STRIPE[btn.dataset.pack];
  });

  var thumbs = document.getElementById('thumbs');
  var main = document.getElementById('mainImage');
  thumbs.addEventListener('click', function (e) {
    var btn = e.target.closest('button');
    if (!btn) return;
    main.src = btn.querySelector('img').src;
    Array.prototype.forEach.call(thumbs.children, function (b) {
      b.setAttribute('aria-current', b === btn ? 'true' : 'false');
    });
  });
</script>

</body>''')}"""


def framside():
    flagg = PRODUKT[0]
    kort = ""
    for p in PRODUKT:
        f, alt = p["bilete"][0]
        kort += f"""      <a class="card" href="{p["slug"]}.html">
        <div class="card-img"><img src="bilder/{f}.webp?v={V}" alt="{alt}"></div>
        <h3>{p["kort"]}</h3>
        <p>{p["teaser"]}</p>
        <div class="card-price">{p["pris"]}</div>
      </a>
"""
    hf, hero_alt = flagg["bilete"][0]
    return hovud("FreshSeal | Bag sealers that keep food fresh",
                 "Bag sealers that close a bag airtight in one pass. Free shipping, 30-day returns.") + f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-img"><img src="bilder/{hf}.webp?v={V}" alt="{hero_alt}"></div>
    <div class="hero-text">
      <p class="eyebrow">The flagship</p>
      <h1>Stop throwing away half a bag</h1>
      <p class="lead">The FreshSeal Mini Sealer closes any plastic bag airtight in one pass —
         chips, coffee, pasta, frozen food. It recharges over USB-C, cuts the bag open again, and
         hangs on your fridge door so you never lose it in a drawer.</p>
      <div class="hero-cta">
        <a class="btn-buy" href="mini-sealer.html">Shop the Mini Sealer — $24.99</a>
        <p class="hero-note">Free shipping · 30-day returns · Delivery in 8&ndash;14 days</p>
      </div>
    </div>
  </div>
</section>

<section class="range">
  <div class="wrap">
    <h2>The FreshSeal range</h2>
    <p class="range-note">Three sealers, one job. Pick the one that fits your kitchen.</p>
    <div class="cards">
{kort}    </div>
  </div>
</section>

<section class="promise">
  <div class="wrap">
    <h2>Our promise</h2>
    <div class="promise-grid">
      <div>
        <h3>Try it for 30 days</h3>
        <p>Use it, test it on your own bags. If it is not for you, send it back within 30 days and
           we refund you in full.</p>
      </div>
      <div>
        <h3>It arrives, or you don't pay</h3>
        <p>Every order ships with tracking. If your parcel is lost, damaged, or we cannot deliver
           to your address, you get your money back — no argument.</p>
      </div>
      <div>
        <h3>A person answers</h3>
        <p>Write to us and a human reads it, usually the same day. No ticket numbers, no chatbot
           sending you in circles.</p>
      </div>
    </div>
  </div>
</section>
{BUNN}"""


if __name__ == "__main__":
    open("index.html", "w", encoding="utf-8").write(framside())
    print("index.html")
    for p in PRODUKT:
        open(f'{p["slug"]}.html', "w", encoding="utf-8").write(produktside(p))
        print(f'{p["slug"]}.html')
