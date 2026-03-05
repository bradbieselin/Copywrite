# CopyDTC

**AI-powered copywriting agency for DTC (direct-to-consumer) brands.**

CopyDTC uses Claude and structured prompt templates to produce high-quality copy at agency speed. Emails, landing pages, ads, blog posts, social content, product descriptions, and more. Every deliverable is built from a client-specific Brand Voice Bible so the output sounds like the brand, not like a robot.

## How This Project Is Organized

| Folder | What It Does |
|--------|-------------|
| `/portal` | Password-protected client portal with admin panel |
| `/templates` | HTML templates for the landing page and web app |
| `/static` | Images and static assets |
| `/tests` | Test suite for the Flask app |
| `/agency/client-work` | Prompt templates, brand guides, and portfolio samples. The engine of the agency. |
| `/agency/operations` | Client onboarding, delivery workflows, reporting templates, SOPs, and business docs |
| `/agency/sales` | Outreach sequences, audit generators, proposals, and content marketing assets |
| `/agency/tools` | Standalone AI prompt tools (content generators, analyzers) |

## Tech Stack

- **Backend:** Python / Flask
- **Database:** SQLite (via db.py)
- **Email:** Resend HTTP API
- **Hosting:** Railway (production)
- **Security:** CSRF protection, session management, honeypot fields

## Key Files

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application |
| `db.py` | Database models and helpers |
| `landing.py` | Landing page routes |
| `intake.py` | Client intake form handler |
| `proposal.py` | Proposal generator |
| `dm.py` | Direct message helper |
| `instagram_dtc_scraper.py` | Instagram DTC brand scraper for prospecting |

## Getting Started

```bash
git clone https://github.com/bradbieselin/Copywrite.git
cd Copywrite
pip install -r requirements.txt
cp .env.example .env   # Fill in your keys
python app.py
```

## Deployment

See `DEPLOYMENT.md` for Railway production setup.
