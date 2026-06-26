# Nepô's Blog

A minimal, handcrafted blog built with **11ty** and vanilla CSS. Designed for longevity, not speed. Inspired by Monocle's design language and the old internet's editorial sensibility.

## Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Run Locally
```bash
npm run serve
```
Visit `http://localhost:8080` in your browser.

### 3. Build for Production
```bash
npm run build
```
Output goes to `_site/` directory.

## Project Structure

```
nepo-blog/
├── articles/                 # Markdown files for blog posts
│   ├── 001-wonder-threshold.md
│   └── 002-irasutoya.md
├── css/
│   └── style.css            # All design tokens, typography, colors
├── _includes/
│   ├── base.njk             # Main layout template
│   ├── article.njk          # Article page template
│   └── partials/            # Reusable template components
├── _data/
│   └── site.js              # Site configuration (title, author, etc.)
├── design-system/
│   └── index.md             # Design documentation (typography, colors, spacing)
├── images/                  # Static images (use in articles with `/images/filename.jpg`)
├── index.njk                # Homepage template
├── .eleventy.js             # 11ty configuration
├── package.json             # Dependencies
└── .gitignore              # Git exclusions
```

## Writing & Publishing Articles

### Create a New Article

1. **Create a markdown file** in `articles/`:
   ```
   articles/003-your-article-slug.md
   ```

2. **Add YAML front matter** at the top:
   ```yaml
   ---
   title: "Your Article Title"
   date: 2026-06-26
   author: Nepô
   tags: ["Design", "Philosophy"]
   excerpt: "A brief summary of the article for the homepage."
   ---
   ```

3. **Write in markdown**:
   ```markdown
   # Your Section

   Regular paragraph text.

   > A blockquote for emphasis

   - List items
   - Work naturally
   ```

4. **Add images** (optional):
   ```markdown
   ![Alt text describing the image](/images/your-image.jpg)
   ```

### Markdown Features Supported

- **Headings:** `# H1`, `## H2`, `### H3`, etc.
- **Emphasis:** `**bold**`, `*italic*`, `***bold italic***`
- **Links:** `[text](url)`
- **Lists:** `- item` (unordered), `1. item` (ordered)
- **Blockquotes:** `> quote text`
- **Code:** `` `inline code` ``, or triple backticks for blocks
- **Highlights:** `<mark>highlighted text</mark>` renders with yellow background
- **Images:** `![alt](/images/filename.jpg)`

### Publishing Workflow

1. **Write offline** in IA Writer (`.md` format)
2. **Save to** `articles/` folder
3. **Commit to GitHub:**
   ```bash
   git add articles/003-your-article.md
   git commit -m "Add article: Your Article Title"
   git push
   ```
4. **GitHub Actions** (or manual deploy) builds and pushes to Cloudflare Pages
5. **Go live** at `nepo.mee.cc`

## Design System

All design decisions are documented in `/design-system/index.md`.

### Key Design Tokens

**Colors:**
- `--color-text: #1a1a1a` — Primary text
- `--color-accent: #FFDC1E` — Yellow highlight
- `--color-bg: #ffffff` — Background

**Typography:**
- `--font-serif: Georgia, Garamond` — Headlines
- `--font-sans: System fonts` — Body text

**Spacing:**
- `--space-md: 24px` — Default margin
- `--space-lg: 32px` — Section gap
- `--space-xl: 48px` — Large separation

### Customization

Edit `css/style.css` to modify any design token. All values are at the top in the `:root` selector for easy tweaking.

## Homepage Logic

- **Latest article** gets prominent display with a "LATEST" label
- Newest article has more visual focus (larger title, featured)
- Once a new article is published, the previous "latest" moves to the "Exploration" section
- **Exploration section** lists all older articles chronologically (newest first)
- Tags display inline with each article for quick reference

## Deployment to Cloudflare Pages

1. **Create a GitHub repo** (private or public)
2. **Push your local project:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/nepo-blog.git
   git push -u origin main
   ```

3. **Connect to Cloudflare Pages:**
   - Go to Cloudflare dashboard → Pages
   - Click "Create a project" → Connect to Git
   - Select your `nepo-blog` repo
   - Build command: `npm run build`
   - Build output directory: `_site`
   - Click "Deploy"

4. **Set custom domain:**
   - In Cloudflare Pages settings → Custom domains
   - Add `nepo.mee.cc` (requires DNS setup in Cloudflare)

## DNS Setup (for `nepo.mee.cc`)

If your main domain (`mee.cc`) is on Cloudflare:

1. In Cloudflare dashboard, go to DNS records for `mee.cc`
2. Create a CNAME record:
   - **Name:** `nepo`
   - **Target:** `nepo-blog.pages.dev` (Cloudflare Pages URL)
   - **Proxy status:** Proxied

3. It may take 5–15 minutes to propagate

## Inline Image Handling

Articles support images placed inline:

```markdown
# My Article

Some text.

![A description of the image](/images/example.jpg)

More text continues here.
```

Images are:
- Responsive (scale to fit the article width)
- Vertically centered with generous spacing
- Max-width of the article container (600px)
- Rounded corners (2px)

## Search & Filtering (Future)

Currently, the site is simple and navigational. Future additions:
- Full-text search
- Tag-based filtering
- Category pages
- Related articles widget

These can be added without breaking the existing structure.

## SEO Basics

- Each article has proper meta tags (title, description, og:image)
- Clean URLs based on file structure
- Sitemaps can be generated with an 11ty plugin
- Social sharing uses Open Graph & Twitter Card tags

## Performance Notes

- **No JavaScript** in the base template (except optional analytics)
- **Static HTML output** — serves instantly
- **CSS is inline-critical** — all styles in one file, loaded once
- **Images are optimized** — use `.jpg` for photos, `.png` for graphics

## Troubleshooting

### Site doesn't rebuild locally
```bash
rm -rf node_modules _site
npm install
npm run serve
```

### Images not showing
Check the path: `/images/filename.jpg` (leading slash is required)

### Tags aren't displaying
Tags are automatically extracted from the YAML front matter. Remove `"articles"` from the tags array—it's auto-added by 11ty and filtered out in templates.

## License

MIT. This project is yours to own and modify.

---

**Built with:** 11ty, vanilla CSS, and intention.  
**Inspired by:** Monocle, Arthur Mee, the old internet.  
**Philosophy:** Constraint breeds clarity. Handcraft outlasts trends.
