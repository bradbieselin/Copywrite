# Invoice Template

> **Purpose:** Standard invoice template for monthly client billing. Clean, professional format that can be adapted for Stripe, QuickBooks, or manual invoicing.
> **Status:** Scaffold — full content to be built in subsequent prompts
> **Used by:** Brad for monthly client billing

## Contents

### Invoice Fields
- Invoice number (format: CDTC-[YEAR]-[SEQUENTIAL])
- Invoice date
- Due date (Net 15 from invoice date)
- CopyDTC business details (name, address, email, tax ID if applicable)
- Client business details (name, address, billing contact)

### Line Items
- Service tier name and description
- Monthly retainer amount
- Any additional services (one-off projects, extra deliverables)
- Subtotal
- Tax (if applicable)
- Total due

### Payment Details
- Accepted payment methods: Stripe, bank transfer, check
- Payment link (Stripe invoice URL)
- Bank details for wire transfer (if applicable)
- Late payment policy: 1.5% per month after 15 days

### Notes Section
- Brief summary of deliverables produced this period
- Next invoice date reminder
- Thank you message

### Automation
- Stripe recurring invoice setup instructions
- QuickBooks integration notes
- Auto-reminder schedule: 3 days before due, day of, 3 days after, 7 days after
