# DEPLOYMENT — nepo.mee.cc

Reference for how this site builds, deploys, and authenticates mail.
Last verified 2026-08-05.

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

One page — `index.njk`, rendered by Eleventy with `_includes/base.njk`. Content
and configuration live in `_data/site.js` (address, Formspree endpoint, year).
There is no `articles/` directory and no `/design-system/` page.

The inquiry form posts to Formspree. Its endpoint is `site.formEndpoint`; while
that value is empty the page falls back to the plain email address.

### Background plates

Three engravings from Diderot & d'Alembert's *Encyclopédie* (1751–1772), used as
CSS masks — the **alpha channel is the ink** and the colour comes from
`background-color`, so the RGB in those files is irrelevant.

| File | Position | Source | Licence |
|---|---|---|---|
| `plate-forme.webp` | left | *Imprimerie en Lettres, Pl. 1* (Musée Carnavalet) | CC0 |
| `plate-typecase.webp` | right | *Imprimerie, Casse* via Commons / Gallica (BnF) | **CC BY-SA 4.0** |
| `plate-arch.webp` | bottom right | *Encyclopédie* | public domain |

**`plate-typecase.webp` carries an attribution obligation.** The colophon credit
in `index.njk` naming Wikimedia Commons, Gallica and linking CC BY-SA 4.0 is a
licence condition, not decoration — removing it while that plate is in use puts
the site out of compliance. The 1751 engraving itself is public domain; the
claim is on the scan.

Processing note: the scan carries a red library accession stamp at roughly
(57, 1027)–(106, 1093) in the original. Greyscale reads it as ink, so it is
painted out before thresholding.

`tools-make-plate.py` regenerates the asset: it thresholds luminance to alpha
(paper 210, ink 55) and saves webp with `alpha_quality` near 60, which is what
keeps the file around 130 KB rather than 300 KB. It expects the source scan
alongside it as `casse-cc0.jpg` — that original is **not** in the repo, so
re-download it from Commons first:

```
https://commons.wikimedia.org/wiki/File:Planche_de_l’Encyclopédie_de_Diderot_et_d’Alembert._Pl._1._Imprimerie_en_Lettres,_L’Opération_de_la_casse,_G.33153.jpg
```

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

## Rollback

The previous multi-article site is preserved:

- branch `archive/full-site`
- tag `v1-full-site`
- local copy `~/Desktop/nepo-blog-backup-2026-08-05/`
