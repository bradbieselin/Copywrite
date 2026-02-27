# Deploying Copywrite to Railway

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
| `APP_BASE_URL`        | `https://your-app.up.railway.app` | Update after first deploy with your real URL |
| `SENDGRID_API_KEY`    | `SG....` | Optional — enables email notifications |
| `SENDGRID_FROM_EMAIL` | `you@yourdomain.com` | Optional — must be verified in SendGrid |
| `ADMIN_EMAIL`         | `you@youremail.com` | Optional — receives new brief notifications |

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

## Step 7 — Update APP_BASE_URL

After your first deploy, copy the generated Railway URL from **Settings → Domains**
and update the `APP_BASE_URL` variable to match (e.g. `https://copywrite-brad.up.railway.app`).
This is what gets used in the email links sent to clients.

---

## Step 8 — (Optional) Custom domain

1. In Railway: **Settings → Networking → Custom Domain**
2. Add your domain and follow the DNS instructions
3. Update `APP_BASE_URL` to your custom domain (e.g. `https://portal.yourdomain.com`)

---

## Environment variables — copy-paste ready

```
SECRET_KEY=<generate with: python -c "import secrets; print(secrets.token_hex(32))">
ANTHROPIC_API_KEY=sk-ant-...
DB_PATH=/data/copywrite.db
UPLOAD_FOLDER=/data/uploads
APP_BASE_URL=https://your-app.up.railway.app
SENDGRID_API_KEY=SG....
SENDGRID_FROM_EMAIL=you@yourdomain.com
ADMIN_EMAIL=you@youremail.com
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
- [ ] `APP_BASE_URL` updated to real Railway URL
- [ ] (Optional) SendGrid configured
- [ ] (Optional) Custom domain added
