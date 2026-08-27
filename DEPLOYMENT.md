# DEPLOYMENT — nepo.mee.cc

Reference for how this site builds, deploys, and authenticates mail.
Last verified 2026-08-27.

> **History:** this file was originally a go-live checklist for a multi-article
> blog deployed on Cloudflare Pages. Neither is true any more — the site is a
> single-screen splash page on GitHub Pages, and its DNS is on Route 53. The
> stale instructions were removed rather than left in place, because a wrong
> deployment doc is worse than none: it reads as authoritative and sends you to
> the wrong console.

## How it deploys

Push to `main` → GitHub Actions builds → GitHub Pages serves. There is nothing
to run by hand.

- Workflow: `.github/workflows/` (`Deploy to GitHub Pages`)
- Build: `npm run build` → `eleventy` → `_site/`
- Custom domain: `CNAME` file contains `nepo.mee.cc`
- Typical deploy: ~40 seconds

```bash
git push                       # that's the whole deploy
gh run list --limit 1          # check status
```

No Cloudflare Pages project, no `CLOUDFLARE_API_TOKEN` secret. Both were part of
the old setup and are gone.

## The site

One template — `index.njk`, rendered by Eleventy with `_includes/base.njk` —
paginated over `_data/locales.js` into three pages: `/` (English), `/pt/`
(Portuguese), `/ja/` (Japanese). Locale-independent configuration (address,
Formspree endpoint, year) lives in `_data/site.js`; every user-facing string
lives in `_data/i18n/{en,pt,ja}.json`, keyed identically across the three
files. There is no `articles/` directory and no `/design-system/` page.

The inquiry form posts to Formspree. Its endpoint is `site.formEndpoint`; while
that value is empty the page falls back to the plain email address.

### Internationalization (added 2026-08-25)

Three locales share the one template via Eleventy pagination — see
`_data/locales.js` (locale code, `<html lang>` value, and URL path) and
`_data/i18n/{en,pt,ja}.json` (every string on the page, keyed identically
across the three files). Add a fourth locale by adding one entry to each.

**Language switcher** — `EN · PT · 日本語` in the masthead, between the
name/role and the Mee mark. Clicking it writes the choice to
`localStorage['lang-pref']`.

**Auto-redirect** — only the English page (`_includes/base.njk`, guarded by
`{% if locale.code == "en" %}`) carries a synchronous script at the very top
of `<head>` that redirects to `/pt/` or `/ja/` based on
`navigator.languages`, unless `lang-pref` is already set — which only
happens via an explicit switcher click; the auto-redirect never sets it
itself. This is **browser language**, not IP geolocation: GitHub Pages has
no server/edge compute (see above — that infra was deliberately removed
once already), and a client-side geo-IP lookup would mean sending a
third-party service the visitor's IP before they've done anything. `/pt/`
and `/ja/` never redirect — landing there is treated as intentional.

**SEO** — each page has its own canonical URL, `hreflang` alternates for all
three plus `x-default` → `/`, and per-locale `<title>`/OG/JSON-LD sourced
from `i18n.<locale>.meta`.

**Translations** — drafted by Claude, reviewed by the user before each
commit. Japanese copy is intentionally different in substance, not just
translated: the three service panels pitch helping Japanese senior
leadership present to English-speaking/international audiences (an
interpreter-support note sits under Speaking & Training, JA only —
`services.speaking.note` in `ja.json`, rendered conditionally so EN/PT are
unaffected).

**CJK line-wrapping** — `ch`-based CSS widths (e.g. `.lede`'s
`max-width: 42ch`) are measured against the Latin "0" glyph, roughly half
the width of a full-width Japanese character — too narrow for the manual
`<br>` breaks in the Japanese copy, which will silently re-wrap mid-word
without it. `html[lang="ja"] .lede` overrides to `25em` for this reason.
The service panels have no such cap (their column isn't `ch`-based), so
their breaks were placed by measuring actual rendered character counts per
line via screenshot, not by formula — re-verify by screenshot if that copy
changes.

**Proof-row column alignment** — the two `.proof-row` lines (`proof.row1`/
`row2`) put a vertical rule between column a and column b via `border-left`
on the second `<span>`; for that rule to land at the same x in both rows,
`.proof-row span:first-child` needs a fixed `width` (currently `368px`) plus
`flex-shrink: 0`, not just a `min-width` — a `min-width` only holds alignment
by coincidence, for as long as every locale's column-a string renders
narrower than it, and silently breaks (rule drifts row-to-row) the moment one
doesn't. `368px` was picked by screenshot to be the narrowest width that
still keeps every current en/ja/pt column-a string on one line — re-verify
by screenshot (same headless-Chrome caveat above applies) if that copy
changes, since a longer string wraps inside the fixed column rather than
pushing the rule out of alignment.

**Testing note** — this machine's headless Chrome
(`/Applications/Google Chrome.app`) will not lay out below roughly 500px of
internal viewport width no matter what `--window-size` is passed; it
silently clamps, then crops the screenshot to the smaller canvas that was
actually requested. Confirm with an injected `window.innerWidth` check
before trusting a narrow screenshot — an element missing from the edge of
one may just be cropped, not actually broken. Real device testing is more
reliable than this workaround.

### Background plates

Three engravings from Diderot & d'Alembert's *Encyclopédie* (1751–1772), used as
CSS masks — the **alpha channel is the ink** and the colour comes from
`background-color`, so the RGB in those files is irrelevant.

| File | Position | Source | Licence |
|---|---|---|---|
| `plate-forme.webp` | left | *Imprimerie en Lettres, Pl. 1* (Musée Carnavalet) | CC0 |
| `plate-typecase.webp` | upper right | *Imprimerie, Casse* via Commons / Gallica (BnF) | **CC BY-SA 4.0** |
| `plate-amphitheatre.webp` | bottom right | *Encyclopédie* | public domain |

**`plate-typecase.webp` carries an attribution obligation.** The colophon credit
in `index.njk` naming Wikimedia Commons, Gallica and linking CC BY-SA 4.0 is a
licence condition, not decoration — removing it while that plate is in use puts
the site out of compliance. The 1751 engraving itself is public domain; the
claim is on the scan.

Processing note: `plate-typecase.webp` is Fig. 1 only, the case grid. The full
plate also carries Fig. 2, the case on its stand, but that sits in the
bottom-right corner the amphitheatre occupies. The full-plate crop and the patch
that covers a red library accession stamp are both recorded in the script — the
stamp falls below the current crop, so it needs no patch as things stand.

`tools-make-plate.py` regenerates both type plates: it thresholds luminance to
alpha and saves webp with `alpha_quality` near 60, which is what keeps the files
near 130 KB rather than 300 KB. The source scans are **not** in the repo —
download them next to the script first, under these exact names:

| Name | Where |
|---|---|
| `casse-cc0.jpg` | [Pl. 1, L'Opération de la casse](https://commons.wikimedia.org/wiki/File:Planche_de_l%E2%80%99Encyclop%C3%A9die_de_Diderot_et_d%E2%80%99Alembert._Pl._1._Imprimerie_en_Lettres,_L%E2%80%99Op%C3%A9ration_de_la_casse,_G.33153.jpg) |
| `casse-grid.jpg` | [Imprimerie, Casse](https://commons.wikimedia.org/wiki/File:Planche_encyclop%C3%A9die_imprimerie_3_Casse.jpg) |

Then `python3 tools-make-plate.py && cp plate-*.webp images/`.
`plate-amphitheatre.webp` predates the script and has no recipe here; it is in
git history if it ever needs recovering.

### Country flags

The countries claim used to carry six hand-drawn Irasutoya flags in
`images/flags/`, keyed off a `countries` list in `_data/site.js`. Both are gone
— the line is now plain text ("Flown in for events in 10+ countries"). The assets
and the recipe are in git history if the idea ever comes back; note that
Irasutoya's terms cap free commercial use at a limited number of illustrations
per work (20 at the time of writing), so check their current terms first.

### The form honeypot — do not remove `readonly`

`index.njk` carries a hidden `_gotcha` honeypot field. It **must** keep its
`readonly` attribute, and `_includes/base.njk` clears it before submitting.

Password managers ignore `autocomplete="off"` and will fill that field. When
they do, Formspree discards the submission as spam **while returning success to
the visitor** — so the sender sees "Thank you" and the message reaches nobody.
This happened in production on 2026-08-05. Both guards exist to prevent it;
removing either brings the bug back silently.

## DNS

`mee.cc` is hosted in **AWS Route 53**. The site record:

| Name | Type | Value |
|---|---|---|
| `nepo` | CNAME | `rafaelnepo.github.io` |

## Email Authentication for `mee.cc` (set up 2026-08-05)

DNS for `mee.cc` is hosted on **AWS Route 53**, not Cloudflare. Mail is Google
Workspace. Before this was set up, `contact@mee.cc` sent completely
unauthenticated mail — no SPF, no DKIM, no DMARC — which meant replies to
inquiries were a coin flip on reaching the inbox.

### The three records

All are TXT records in the `mee.cc` hosted zone. Route 53 requires values to be
wrapped in double quotes.

| Name | Value |
|---|---|
| `@` (apex) | `"v=spf1 include:_spf.google.com ~all"` |
| `google._domainkey` | the DKIM key, split — see below |
| `_dmarc` | `"v=DMARC1; p=none; rua=mailto:contact@mee.cc; fo=1"` |

The apex TXT record also holds the `google-site-verification=…` value on its own
line. **Do not remove it** — that is a separate value, not part of the SPF record.

### The DKIM splitting trap

A 2048-bit DKIM value is ~410 characters. Route 53 caps each quoted string at
255 **including the quotes**, so the key must be split into two quoted strings
separated by a space, **on one line**:

```
"v=DKIM1; k=rsa; p=FIRST-CHUNK" "SECOND-CHUNK"
```

Chunks of 205 characters work comfortably. Two traps here:

- Putting the chunks on **separate lines** creates two independent TXT records
  and DKIM fails with no useful error.
- Chunks of exactly 255 are rejected as "Value is too big" — the console counts
  the quotes.

To regenerate the key: Admin Console → Apps → Google Workspace → Gmail →
Authenticate email → 2048-bit, prefix `google`. Then click **START
AUTHENTICATION** — the DNS record alone does nothing until that switch is on.

### Verifying

Query AWS directly to bypass DNS caching:

```bash
NS=$(dig +short NS mee.cc | head -1)
dig +short TXT mee.cc @$NS              # SPF + site verification
dig +short TXT _dmarc.mee.cc @$NS       # DMARC
dig +short TXT google._domainkey.mee.cc @$NS   # DKIM
```

Then send a real message to Gmail and use **Show original**. All three should
say PASS — but check *which domain* DKIM signed with. If it reads
`…gappssmtp.com`, Google is still using its default key and the custom one is
not active yet. It must read `mee.cc`.

That distinction matters: a `gappssmtp.com` signature does not align with
`mee.cc`, so DMARC would be passing on SPF alone. **SPF breaks when mail is
forwarded; DKIM survives it.** Without aligned DKIM, any forwarded reply fails
DMARC.

### Tightening the policy — not before ~2026-09-02

`p=none` means "report, don't block." DMARC aggregate reports arrive at
`contact@mee.cc` as XML attachments listing every source sending as `mee.cc`.
After a few weeks of clean reports, tighten in order:

```
p=none  →  p=quarantine  →  p=reject
```

**Do not skip ahead.** If some forgotten service sends as `mee.cc` and is not in
the SPF record, `p=reject` makes that mail vanish silently. The reports exist to
find those senders first.

### Gmail filter

Formspree notifications land in spam by default. In Gmail: Settings → Filters
and Blocked Addresses → From `formspree.io` → **Never send it to Spam**. Without
this, inquiries are silently missed — the failure mode this whole page exists to
prevent.

## Troubleshooting

### Build failed

Check the run: `gh run view --log-failed`. Usually a Nunjucks syntax error in
`index.njk` or `_includes/base.njk`.

### Change not showing on the live site

Confirm the deploy finished (`gh run list --limit 1`), then hard-reload —
`Cmd+Shift+R`. GitHub Pages also caches at the edge for a few minutes.

### Form submissions not arriving

In order of likelihood: the Gmail filter above is missing and they are in spam;
the honeypot is being tripped (check the Formspree dashboard for
`_status error`); or the Formspree endpoint in `_data/site.js` is wrong.

### Images not showing

Use a leading slash — `/images/filename.jpg`. Files live in `images/`.

### Wrong language showing

A visitor stuck on the "wrong" language after switching is usually
`localStorage['lang-pref']` from earlier testing, not a bug — the
auto-redirect on `/` only respects a stored preference, it never guesses
based on anything else once one is set. Clear it (devtools → Application →
Local Storage) to see the browser-language auto-detect again.

## Rollback

The previous multi-article site is preserved:

- branch `archive/full-site`
- tag `v1-full-site`
- local copy `~/Desktop/nepo-blog-backup-2026-08-05/`
