# Deploying Copywrite to Railway

Railway is the recommended host — it runs Python/Flask apps directly from your
GitHub repo with zero infrastructure to manage.

---

## Prerequisites

- A [Railway](https://railway.app) account (free tier is fine to start)
- A [SendGrid](https://sendgrid.com) account for email (free tier: 100 emails/day)
- Your Anthropic API key

---

## Step 1 — Push to GitHub

Make sure your code is pushed to a GitHub repo.  The branch you're deploying
should be up to date.

---

## Step 2 — Create a Railway project

1. Log in to [railway.app](https://railway.app) and click **New Project**.
2. Choose **Deploy from GitHub repo** and select your repository.
3. Railway detects the `Procfile` and sets the start command automatically:
   ```
   web: gunicorn app:app
   ```

---

## Step 3 — Set environment variables

In Railway, open your service → **Variables** tab and add the following:

| Variable              | Required | Description |
|-----------------------|----------|-------------|
| `SECRET_KEY`          | **Yes**  | Random 32-byte hex string. Generate with: `python -c "import secrets; print(secrets.token_hex(32))"` |
| `ANTHROPIC_API_KEY`   | **Yes**  | Your Anthropic API key from [console.anthropic.com](https://console.anthropic.com) |
| `SENDGRID_API_KEY`    | Optional | SendGrid API key — enables email notifications |
| `SENDGRID_FROM_EMAIL` | Optional | Verified sender address in your SendGrid account |
| `ADMIN_EMAIL`         | Optional | Your email — receives admin notifications on new briefs |
| `APP_BASE_URL`        | Optional | Full URL of your deployed app, e.g. `https://your-app.up.railway.app` — used to build links in emails |

> **Tip:** Railway auto-injects `PORT`. Gunicorn binds to it automatically.

---

## Step 4 — Deploy

Railway deploys automatically on every push to your connected branch.  The
first deploy takes ~1-2 minutes.  After that, click **View Logs** to confirm
the app started cleanly.

---

## Step 5 — First login

1. Visit `https://your-app.up.railway.app/portal/login`
2. Log in with the default credentials:
   - **Email:** `admin@copywrite.io`
   - **Password:** `admin123`
3. **Immediately** go to **Settings** in the top navbar and change your password.

---

## Persistent storage note

Railway's filesystem is **ephemeral** — uploaded copy files are wiped on every
redeploy.  For production use, swap the local file storage for an S3-compatible
bucket (e.g. AWS S3, Cloudflare R2, or Railway's upcoming object storage).
The SQLite database is also local; for more than ~20 concurrent users, migrate
to a managed Postgres instance (Railway offers one as an add-on with one click).

---

## Custom domain

In Railway: **Settings → Networking → Custom Domain**.  Add your domain, then
update `APP_BASE_URL` to match (e.g. `https://copywrite.yourdomain.com`).

---

## Quick-start checklist

- [ ] Code pushed to GitHub
- [ ] Railway project created and linked to repo
- [ ] `SECRET_KEY` set (random, not the default)
- [ ] `ANTHROPIC_API_KEY` set
- [ ] First login → password changed immediately
- [ ] (Optional) SendGrid configured for email notifications
- [ ] (Optional) Custom domain configured and `APP_BASE_URL` updated
