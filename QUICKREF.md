# NEPO BLOG — QUICK REFERENCE

## What You Have

✅ **Static site generator (11ty)** — converts markdown to HTML  
✅ **Monocle-inspired design** — serif headlines, generous whitespace, #FFDC1E accent  
✅ **Design system documentation** — `/design-system/` page with all tokens  
✅ **Two sample articles** — showing different writing styles  
✅ **Homepage logic** — latest article featured, older articles in "Exploration" section  
✅ **Mobile responsive** — works on all devices  
✅ **No JavaScript** — pure HTML + CSS, fast and clean  
✅ **SEO-ready** — meta tags, open graph, clean URLs  
✅ **Git workflow ready** — private GitHub repo + auto-deploy to Cloudflare  

---

## Essential Commands

```bash
# Install dependencies (first time only)
npm install

# Run locally for testing
npm run serve
# Visit http://localhost:8080

# Build for production
npm run build
# Output: _site/ directory

# Commit new article to GitHub
git add articles/003-new-article.md
git commit -m "Add article: Title"
git push
# (Auto-deploys to nepo.mee.cc in ~2 minutes)
```

---

## File Structure at a Glance

```
articles/              ← Write .md files here
css/style.css          ← All design tokens (colors, fonts, spacing)
_includes/*.njk        ← HTML templates (don't touch unless customizing)
index.njk              ← Homepage layout
design-system/         ← Design documentation page
images/                ← Put images here, reference as /images/filename.jpg
README.md              ← Full documentation
DEPLOYMENT.md          ← Setup & deployment guide
```

---

## Writing an Article (IA Writer Workflow)

1. **Write in IA Writer** (offline, .md format)
2. **Save to folder:** `articles/003-your-slug.md`
3. **Add YAML header:**
```yaml
---
title: "Your Article Title"
date: 2026-06-26
author: Nepô
tags: ["Design", "Philosophy"]
excerpt: "One-sentence summary for homepage."
---
```
4. **Write markdown below header**
5. **Commit & push:**
```bash
git add articles/003-your-slug.md
git commit -m "Add article: Your Title"
git push
```
6. **Wait 2 minutes** → Site updates automatically

---

## Design System at a Glance

| Token | Value | Usage |
|-------|-------|-------|
| **Accent** | #FFDC1E | Tags, highlights, hover states |
| **Text** | #1a1a1a | Primary text, dark gray |
| **Light Text** | #666 | Secondary, metadata, dates |
| **Headlines** | Georgia, Garamond | Serif, confident, old-internet |
| **Body** | System fonts | Clean, accessible, fast |
| **Line Height** | 1.7 | Comfortable reading |
| **Article Width** | 600px | Optimal reading column |
| **Spacing** | 8px grid | Consistent, intentional |

---

## Homepage Logic

- **Latest Article** — featured at top with "LATEST" label, larger title
- **Once new article posts** — previous latest moves to "Exploration" section
- **Exploration** — chronological list of all older articles (newest first)
- **Tags** — displayed inline with each article, no filtering yet
- **No algorithm** — pure reverse-chronological display

---

## Markdown Features You Can Use

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text** or __bold__
*Italic text* or _italic_
***Bold italic***

<mark>Highlighted text (yellow background)</mark>

[Link text](https://example.com)

> Blockquote — italicized with yellow left border

- Bullet list
  - Nested item
  - Another nested

1. Numbered list
2. Second item

![Alt text](/images/filename.jpg)

`inline code`

\`\`\`
Code block
With multiple lines
\`\`\`

---  (horizontal rule)
```

---

## Markdown + YAML Front Matter Format

```markdown
---
title: "Your Article Title Here"
date: 2026-06-26
author: Nepô
tags: ["Tag1", "Tag2", "Tag3"]
excerpt: "One-sentence summary that appears on homepage. Keep under 150 chars."
---

# Your article starts here

Regular paragraph text.

> "A blockquote or important quote."

More paragraphs. Links are [like this](https://example.com).

![Optional image](/images/filename.jpg)

## Sections

Use headers to structure your thinking.

---

(horizontal rule for visual break)
```

---

## Design Customization (CSS)

All design tokens are in `css/style.css` at the top:

```css
:root {
  --color-accent: #FFDC1E;      /* Change yellow here */
  --text-base: 18px;            /* Change base font size */
  --font-serif: 'Georgia', ...   /* Change headline font */
  --line-height-normal: 1.7;     /* Change line spacing */
  /* etc. */
}
```

Edit the values, commit, and deploy. No build step required—CSS loads instantly.

---

## Deployment Checklist

- [ ] Create private GitHub repo: `nepo-blog`
- [ ] Push code: `git push -u origin main`
- [ ] Connect to Cloudflare Pages
- [ ] Set build command: `npm run build`
- [ ] Set output directory: `_site`
- [ ] Add CNAME DNS record (or nameserver) for `nepo.mee.cc`
- [ ] Wait for DNS propagation (~5-10 min)
- [ ] Visit `https://nepo.mee.cc` ✓
- [ ] Test homepage, article pages, design system
- [ ] (Optional) Set up GitHub Actions for auto-deploy

---

## Next Steps After Launch

### Tier 2 (when ready):
- Newsletter signup flow
- Share buttons (copy link, email, Twitter)
- Tag filter pages
- Search functionality

### Tier 3 (future):
- Comments (Disqus or GitHub Discussions)
- Author bio refinement
- Related articles sidebar
- Analytics (privacy-preserving)

---

## URLs & Links

- **Live site:** https://nepo.mee.cc
- **GitHub repo:** https://github.com/YOUR-USERNAME/nepo-blog (private)
- **Cloudflare Pages dashboard:** https://dash.cloudflare.com → Pages → nepo-blog
- **Design System page:** https://nepo.mee.cc/design-system/

---

## Philosophy

- **Constraint = Clarity** — No algorithm, no distraction. Just good writing & design.
- **Handcrafted** — Every decision is visible, intentional, documented.
- **Ownership** — You control the code, the content, the domain.
- **Longevity** — This will still work 10 years from now.
- **Old Internet Energy** — Personal blogs mattered. Let's build that back.

---

**You're all set. Let's deploy today.**

What's your GitHub username? I'll create a final checklist.
