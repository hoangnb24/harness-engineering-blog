# Deploying Harness Engineering Blog to Cloudflare Pages

This project is an Astro static site. Cloudflare Pages should build the site with `npm run build` and serve the generated `dist/` directory.

## Repository

GitHub repository:

```text
https://github.com/hoangnb24/harness-engineering-blog
```

## Option A — Recommended: Cloudflare Pages Git integration

Use this when you want every push to `main` to deploy automatically.

1. Open Cloudflare Dashboard.
2. Go to **Workers & Pages**.
3. Select **Create application**.
4. Choose **Pages**.
5. Choose **Connect to Git**.
6. Select the GitHub repository:

   ```text
   hoangnb24/harness-engineering-blog
   ```

7. Configure the project:

   | Setting | Value |
   | --- | --- |
   | Project name | `harness-engineering-blog` |
   | Production branch | `main` |
   | Framework preset | `Astro` |
   | Build command | `npm run build` |
   | Build output directory | `dist` |
   | Root directory | `/` |
   | Node.js version | `22` or newer |

8. Click **Save and Deploy**.
9. After the first deploy, Cloudflare will provide a URL like:

   ```text
   https://harness-engineering-blog.pages.dev
   ```

10. Update these files with the production URL if it differs:

   - `astro.config.mjs` → `site`
   - `public/robots.txt` → `Sitemap`
   - GitHub repo homepage URL

## Option B — Direct upload with Wrangler

Use this for a one-off deploy from the local machine.

### 1. Authenticate

```bash
npx wrangler login
```

Or use an API token with Cloudflare Pages permissions:

```bash
export CLOUDFLARE_API_TOKEN="..."
```

The token needs at least:

- Account read
- Cloudflare Pages edit/write

### 2. Build locally

```bash
npm install
npm run build
```

### 3. Deploy

```bash
npx wrangler pages deploy dist --project-name harness-engineering-blog --branch main
```

The project also includes `wrangler.toml`:

```toml
name = "harness-engineering-blog"
pages_build_output_dir = "./dist"
compatibility_date = "2026-05-23"
```

So after authentication, this shorter command should also work:

```bash
npx wrangler pages deploy
```

## Local verification before deploy

Run:

```bash
npm audit --audit-level=moderate
npm run build
```

Expected result:

- `npm audit` reports zero moderate-or-higher vulnerabilities
- Astro builds the static site into `dist/`

## Post-deploy checklist

After Cloudflare creates the Pages project:

1. Visit the canonical production URL:

   ```text
   https://harness-engineering-blog.pages.dev
   ```

   Wrangler may also print a deployment-specific preview URL like:

   ```text
   https://<deployment-hash>.harness-engineering-blog.pages.dev
   ```

   Prefer the canonical project URL for sharing unless you specifically need to inspect one immutable preview deploy.

2. Confirm these routes work:

   ```text
   /
   /agent-ready-repository/
   /agents-md-template/
   /projects/harness-experimental/
   /blog/
   ```

3. Update `astro.config.mjs` with the final production URL.
4. Update `public/robots.txt` sitemap URL with the final production URL.
5. Set the GitHub repository homepage to the production URL:

   ```bash
   gh repo edit hoangnb24/harness-engineering-blog --homepage https://harness-engineering-blog.pages.dev
   ```

6. Later, after a custom domain is chosen, update Cloudflare Pages custom domains and replace the `.pages.dev` URL in config/docs.

## Troubleshooting first deploy access

If the deployment-specific preview URL does not load immediately, try the canonical project URL first:

```text
https://harness-engineering-blog.pages.dev
```

For a brand-new Pages project, DNS/TLS propagation can briefly lag right after Wrangler prints the deployment URL. Re-check after a minute and test with:

```bash
curl -I -L https://harness-engineering-blog.pages.dev
curl -I -L https://<deployment-hash>.harness-engineering-blog.pages.dev
```

A successful response should be `HTTP/2 200`.

## Notes

- The current production placeholder in `astro.config.mjs` is:

  ```text
  https://harness-engineering-blog.pages.dev
  ```

- If Cloudflare gives a different generated URL, prefer that exact URL until a custom domain is configured.
- Search Console and analytics setup require account-sensitive approval and should be handled after the first successful deploy.
