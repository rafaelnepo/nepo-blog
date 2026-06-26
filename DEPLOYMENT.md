# DEPLOYMENT CHECKLIST — Go Live Today

## Step 1: Create GitHub Repository (5 min)

1. Go to https://github.com/new
2. Create a **private** repo called `nepo-blog`
3. Do NOT initialize with README (we have one)
4. Click "Create repository"

## Step 2: Push Code to GitHub (5 min)

In your terminal, from the `nepo-blog` directory:

```bash
git init
git add .
git commit -m "Initial commit: blog setup with design system"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/nepo-blog.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

## Step 3: Set Up Cloudflare Pages (10 min)

1. **Go to Cloudflare Dashboard** → Pages
2. Click **"Create a project"** → **"Connect to Git"**
3. Authorize GitHub if prompted
4. Select the `nepo-blog` repository
5. Click **"Begin setup"**

### Build Configuration:
- **Framework preset:** None (custom)
- **Build command:** `npm run build`
- **Build output directory:** `_site`
- **Environment variables:** (leave empty for now)

Click **"Save and Deploy"**

Cloudflare will build and deploy. This takes ~2-3 minutes. You'll get a temporary URL like `nepo-blog.pages.dev`.

## Step 4: Set Up Custom Domain (5 min)

### Option A: Domain is already on Cloudflare

If `mee.cc` is managed by Cloudflare:

1. **In Cloudflare Dashboard** → Websites → `mee.cc` → DNS
2. Click **"+ Add record"**
3. Fill in:
   - **Type:** CNAME
   - **Name:** nepo
   - **Target:** nepo-blog.pages.dev
   - **Proxy status:** Proxied (orange cloud)
4. Click **"Save"**

Wait 5–10 minutes for DNS to propagate. Then visit `https://nepo.mee.cc` ✓

### Option B: Domain is at another registrar (GoDaddy, Namecheap, etc.)

1. Point `mee.cc` nameservers to Cloudflare (Cloudflare will show you how)
2. OR create a CNAME record in your registrar:
   - **Name:** nepo
   - **Target:** nepo-blog.pages.dev

Then do Step 4A above.

## Step 5: Test Everything (5 min)

1. Visit `https://nepo.mee.cc` in your browser
2. Verify homepage loads with two sample articles
3. Click an article title → read full article
4. Check Design System page at `/design-system/`
5. Verify responsive on mobile (shrink browser window)

## Step 6: Configure GitHub Actions (Optional but Recommended)

So that future commits auto-deploy:

1. In GitHub repo settings → Secrets and variables → Actions
2. Click **"New repository secret"**
3. Add `CLOUDFLARE_API_TOKEN`:
   - Get from Cloudflare Dashboard → Account → API Tokens
   - Create new token with "Cloudflare Pages" permissions
   - Copy and paste into GitHub
4. Add `CLOUDFLARE_ACCOUNT_ID`:
   - Found in Cloudflare Dashboard → Account settings

Now every time you `git push`, the site rebuilds automatically. ✓

## Publishing Your First Real Article

1. **Write in IA Writer** (offline, as usual)
2. **Save to:** `articles/003-your-article-slug.md`
3. **Add YAML front matter** at top:
   ```yaml
   ---
   title: "Article Title"
   date: 2026-06-26
   author: Nepô
   tags: ["Tag1", "Tag2"]
   excerpt: "Brief summary for homepage"
   ---
   ```
4. **Write in markdown** below front matter
5. **Commit and push:**
   ```bash
   git add articles/003-your-article-slug.md
   git commit -m "Add article: Article Title"
   git push
   ```
6. **Wait ~2 minutes** → Site redeploys automatically
7. **Check nepo.mee.cc** → New article is live with "LATEST" label ✓

## Troubleshooting

### "Build failed" error in Cloudflare
- Check the build logs in Cloudflare Pages dashboard
- Usually it's a YAML syntax error in the article front matter
- Common issue: unquoted colons in titles (use `"Title: With Colon"`)

### Domain not resolving
- Wait 10-15 minutes (DNS propagation)
- Clear browser cache: Cmd+Shift+Delete (Chrome) or Cmd+Opt+E (Firefox)
- Check DNS records in Cloudflare are correct

### Images not showing
- Use `/images/filename.jpg` (leading slash required)
- Place actual image files in `images/` folder
- Commit images to GitHub: `git add images/`

## That's It!

Your blog is now:
- **Live at nepo.mee.cc**
- **Version controlled on GitHub**
- **Auto-deployed via Cloudflare Pages**
- **Ready for new articles**

From here, it's just:
1. Write in IA Writer
2. Save to `articles/`
3. Commit & push
4. Done.

No build commands, no complex deployment. Pure simplicity.

---

**Questions?** Check README.md for detailed documentation.  
**Ready?** Let's deploy. What's your GitHub username?
