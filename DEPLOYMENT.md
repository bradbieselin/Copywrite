# Deploying Copywrite to Railway (copydtc.com)

---

## What you need before starting

- A [Railway](https://railway.app) account on the **Hobby plan** ($5/month)
  — required for persistent Volumes (otherwise your database is wiped on every deploy)
- Your code pushed to a **GitHub repository**
- Your **Anthropic API key**
- (Optional) A [SendGrid](https://sendgrid.com) account for email notifications (free tier: 100 emails/day)

---

## Step 1 — Push to GitHub

Make sure your latest code is on GitHub. Railway deploys directly from a repo.

---

## Step 2 — Create a new Railway project

1. Log in at [railway.app](https://railway.app)
2. Click **New Project** → **Deploy from GitHub repo**
3. Select your repository and the branch you want to deploy (e.g. `main`)
4. Railway auto-detects the `Procfile` — the start command will be:
   ```
   web: gunicorn app:app
   ```
5. **Do not deploy yet.** Click through to the project dashboard first.

---

## Step 3 — Add a persistent Volume

This is the critical step. Without it, your database and uploaded files are deleted on every deploy.

1. In your Railway project, click **+ New** → **Volume**
2. Set the **Mount Path** to `/data`
3. Set the **Size** to at least `1 GB` (you can increase later at no extra charge until you hit it)
4. Attach it to your app service

---

## Step 4 — Set environment variables

In your Railway service, go to the **Variables** tab and add:

| Variable              | Value | Notes |
|-----------------------|-------|-------|
| `SECRET_KEY`          | (random string) | Generate: `python -c "import secrets; print(secrets.token_hex(32))"` |
| `ANTHROPIC_API_KEY`   | `sk-ant-...` | From [console.anthropic.com](https://console.anthropic.com) |
| `DB_PATH`             | `/data/copywrite.db` | Points to your persistent Volume |
| `UPLOAD_FOLDER`       | `/data/uploads` | Points to your persistent Volume |
| `APP_BASE_URL`        | `https://copydtc.com` | Update after first deploy with your real URL |
| `SENDGRID_API_KEY`    | `SG....` | Optional — enables email notifications |
| `SENDGRID_FROM_EMAIL` | `hello@copydtc.com` | Optional — must be verified in SendGrid |
| `ADMIN_EMAIL`         | `you@copydtc.com` | Optional — receives new brief notifications |

---

## Step 5 — Deploy

Click **Deploy** (or push a new commit to your connected branch — Railway redeploys automatically on every push).

Watch the **Logs** tab. On the very first deploy you should see:
```
[Portal] Default admin created — email: admin@copywrite.io  password: admin123
```
That confirms the database initialized correctly on the Volume.

---

## Step 6 — First login and password change

1. Visit `https://your-app.up.railway.app/portal/login`
2. Log in:
   - **Email:** `admin@copywrite.io`
   - **Password:** `admin123`
3. Immediately click **Settings** in the top navbar and change your password.

---

## Step 7 — Add copydtc.com as a custom domain

1. In Railway: go to your service → **Settings → Networking → Custom Domain**
2. Click **+ Custom Domain** and enter `copydtc.com`
3. Railway will show you a DNS record to add — typically a **CNAME** pointing to a Railway-provided hostname (e.g. `xxx.up.railway.app`)
4. Log in to your domain registrar where you bought **copydtc.com** and add that DNS record
5. Wait for DNS propagation (usually a few minutes, up to an hour)
6. Railway auto-provisions an SSL certificate via Let's Encrypt — HTTPS is handled automatically

> **Tip:** You can also add `www.copydtc.com` as a second custom domain if you want the `www` subdomain to work. Add a second DNS entry pointing `www` to the same Railway hostname.

---

## Step 8 — Update APP_BASE_URL

Once copydtc.com is resolving correctly, update the `APP_BASE_URL` environment variable in Railway to:

```
APP_BASE_URL=https://copydtc.com
```

This is used in email links sent to clients, so it must match your live domain.

---

## Environment variables — copy-paste ready

```
SECRET_KEY=<generate with: python -c "import secrets; print(secrets.token_hex(32))">
ANTHROPIC_API_KEY=sk-ant-...
DB_PATH=/data/copywrite.db
UPLOAD_FOLDER=/data/uploads
APP_BASE_URL=https://copydtc.com
SENDGRID_API_KEY=SG....
SENDGRID_FROM_EMAIL=hello@copydtc.com
ADMIN_EMAIL=you@copydtc.com
```

---

## Deployment checklist

- [ ] Code pushed to GitHub
- [ ] Railway Hobby plan active
- [ ] Railway project created and connected to repo
- [ ] Volume added and mounted at `/data`
- [ ] `SECRET_KEY` set (random, not the default)
- [ ] `ANTHROPIC_API_KEY` set
- [ ] `DB_PATH` set to `/data/copywrite.db`
- [ ] `UPLOAD_FOLDER` set to `/data/uploads`
- [ ] App deployed — Logs show database init message
- [ ] First login complete → password changed immediately
- [ ] Custom domain `copydtc.com` added in Railway → Settings → Networking
- [ ] DNS record added at your domain registrar pointing copydtc.com → Railway
- [ ] SSL certificate confirmed (HTTPS green lock in browser)
- [ ] `APP_BASE_URL` updated to `https://copydtc.com`
- [ ] (Optional) `www.copydtc.com` added as second custom domain
- [ ] (Optional) SendGrid configured with `hello@copydtc.com`
