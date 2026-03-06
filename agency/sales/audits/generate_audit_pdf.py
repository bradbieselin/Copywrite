#!/usr/bin/env python3
"""
CopyDTC Free Content Audit PDF Generator

Generates a branded, professional PDF audit report for DTC brand prospects.
This is the agency's primary lead magnet. A traditional agency charges $500-1000
for this. You produce it in 30 minutes with Claude and this script.

Usage:
    python generate_audit_pdf.py --brand "Brand Name" --url "https://example.com" --output audit.pdf

Or import and call generate_audit() directly from your Flask app.
"""

import argparse
import json
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.graphics import renderPDF


# Brand colors
NAVY = HexColor("#1a1a2e")
BLUE = HexColor("#2563eb")
LIGHT_BLUE = HexColor("#eff6ff")
DARK_GRAY = HexColor("#374151")
MEDIUM_GRAY = HexColor("#6b7280")
LIGHT_GRAY = HexColor("#f3f4f6")
GREEN = HexColor("#10b981")
RED = HexColor("#ef4444")
YELLOW = HexColor("#f59e0b")

def get_styles():
    """Create custom paragraph styles for the audit report."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="CoverTitle",
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=34,
        textColor=NAVY,
        alignment=TA_LEFT,
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="CoverSubtitle",
        fontName="Helvetica",
        fontSize=14,
        leading=20,
        textColor=MEDIUM_GRAY,
        alignment=TA_LEFT,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="SectionHead",
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=24,
        textColor=NAVY,
        spaceBefore=24,
        spaceAfter=12,
    ))
    styles.add(ParagraphStyle(
        name="SubHead",
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=18,
        textColor=DARK_GRAY,
        spaceBefore=16,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="BodyText2",
        fontName="Helvetica",
        fontSize=10.5,
        leading=16,
        textColor=DARK_GRAY,
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="FindingGood",
        fontName="Helvetica",
        fontSize=10.5,
        leading=16,
        textColor=DARK_GRAY,
        leftIndent=16,
        spaceAfter=4,
        bulletIndent=0,
    ))
    styles.add(ParagraphStyle(
        name="ScoreLabel",
        fontName="Helvetica-Bold",
        fontSize=36,
        leading=40,
        textColor=BLUE,
        alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        name="FooterText",
        fontName="Helvetica",
        fontSize=8,
        leading=10,
        textColor=MEDIUM_GRAY,
        alignment=TA_CENTER,
    ))
    return styles


def score_color(score):
    """Return color based on score: green (8-10), yellow (5-7), red (0-4)."""
    if score >= 8:
        return GREEN
    elif score >= 5:
        return YELLOW
    return RED


def score_label(score):
    if score >= 8:
        return "Strong"
    elif score >= 5:
        return "Needs Work"
    return "Critical"


def build_score_table(scores, styles):
    """Build the visual score summary table."""
    header = [
        Paragraph("<b>Category</b>", styles["BodyText2"]),
        Paragraph("<b>Score</b>", styles["BodyText2"]),
        Paragraph("<b>Rating</b>", styles["BodyText2"]),
    ]
    rows = [header]
    for cat, sc in scores.items():
        color = score_color(sc)
        rows.append([
            Paragraph(cat, styles["BodyText2"]),
            Paragraph(f"<b>{sc}/10</b>", styles["BodyText2"]),
            Paragraph(f'<font color="#{color.hexval()[2:]}">{score_label(sc)}</font>', styles["BodyText2"]),
        ])

    overall = round(sum(scores.values()) / len(scores), 1)
    rows.append([
        Paragraph("<b>Overall</b>", styles["BodyText2"]),
        Paragraph(f"<b>{overall}/10</b>", styles["BodyText2"]),
        Paragraph(f'<font color="#{score_color(round(overall)).hexval()[2:]}"><b>{score_label(round(overall))}</b></font>', styles["BodyText2"]),
    ])

    t = Table(rows, colWidths=[3*inch, 1.2*inch, 1.5*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("BACKGROUND", (0, -1), (-1, -1), LIGHT_BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [white, LIGHT_GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#e5e7eb")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return t


def build_findings_section(title, findings, styles):
    """Build a section with bullet-point findings."""
    elements = []
    elements.append(Paragraph(title, styles["SubHead"]))
    for f in findings:
        icon = "+" if f.get("type") == "good" else "-"
        prefix = '<font color="#10b981"><b>+</b></font>' if f.get("type") == "good" else '<font color="#ef4444"><b>-</b></font>'
        elements.append(Paragraph(
            f'{prefix}  {f["text"]}',
            styles["FindingGood"],
        ))
    return elements


def add_footer(canvas_obj, doc):
    """Add footer to each page."""
    canvas_obj.saveState()
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(MEDIUM_GRAY)
    canvas_obj.drawString(
        72, 30,
        f"CopyDTC Content Audit  |  copydtc.com  |  Confidential"
    )
    canvas_obj.drawRightString(
        letter[0] - 72, 30,
        f"Page {doc.page}"
    )
    # Top accent line
    canvas_obj.setStrokeColor(BLUE)
    canvas_obj.setLineWidth(3)
    canvas_obj.line(0, letter[1] - 10, letter[0], letter[1] - 10)
    canvas_obj.restoreState()


def generate_audit(data, output_path="audit-report.pdf"):
    """
    Generate a branded PDF audit report.

    Args:
        data: dict with keys:
            - brand_name: str
            - brand_url: str
            - audit_date: str (optional, defaults to today)
            - scores: dict mapping category names to scores (1-10)
            - sections: list of dicts with keys:
                - title: str
                - summary: str
                - findings: list of dicts with "text" and "type" ("good" or "bad")
                - recommendation: str
            - quick_wins: list of strings
            - revenue_impact: str (e.g. "15-25% increase in email revenue")
        output_path: str
    """
    brand = data["brand_name"]
    url = data.get("brand_url", "")
    audit_date = data.get("audit_date", datetime.now().strftime("%B %d, %Y"))
    scores = data["scores"]
    sections = data["sections"]
    quick_wins = data.get("quick_wins", [])
    revenue_impact = data.get("revenue_impact", "")

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        topMargin=0.8*inch,
        bottomMargin=0.8*inch,
        leftMargin=1*inch,
        rightMargin=1*inch,
    )

    styles = get_styles()
    story = []

    # === COVER PAGE ===
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("CONTENT AUDIT", styles["CoverSubtitle"]))
    story.append(Paragraph(brand, styles["CoverTitle"]))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=BLUE))
    story.append(Spacer(1, 16))
    story.append(Paragraph(f"Prepared for: <b>{brand}</b>", styles["BodyText2"]))
    if url:
        story.append(Paragraph(f"Website: {url}", styles["BodyText2"]))
    story.append(Paragraph(f"Date: {audit_date}", styles["BodyText2"]))
    story.append(Paragraph("Prepared by: CopyDTC", styles["BodyText2"]))
    story.append(Spacer(1, 1.5*inch))

    # Overall score highlight
    overall = round(sum(scores.values()) / len(scores), 1)
    story.append(Paragraph(f"{overall}/10", styles["ScoreLabel"]))
    story.append(Paragraph("Overall Content Score", ParagraphStyle(
        "centered", parent=styles["BodyText2"], alignment=TA_CENTER,
        textColor=MEDIUM_GRAY, fontSize=12,
    )))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(
        "This audit evaluates your brand's content across key channels and "
        "identifies specific opportunities to improve conversions, engagement, "
        "and revenue. Every recommendation is actionable and prioritized.",
        ParagraphStyle("centeredBody", parent=styles["BodyText2"], alignment=TA_CENTER)
    ))
    story.append(PageBreak())

    # === SCORE SUMMARY ===
    story.append(Paragraph("Score Summary", styles["SectionHead"]))
    story.append(Paragraph(
        "Each category is scored 1-10 based on best practices for DTC brands. "
        "Scores below 5 represent critical gaps that are likely costing you revenue.",
        styles["BodyText2"],
    ))
    story.append(Spacer(1, 8))
    story.append(build_score_table(scores, styles))
    story.append(Spacer(1, 16))

    # === DETAILED SECTIONS ===
    for section in sections:
        elements = []
        elements.append(Paragraph(section["title"], styles["SectionHead"]))
        elements.append(Paragraph(section["summary"], styles["BodyText2"]))
        elements.extend(build_findings_section("What We Found", section["findings"], styles))
        elements.append(Spacer(1, 8))
        # Recommendation box
        rec_table = Table(
            [[Paragraph(
                f'<b>Recommendation:</b> {section["recommendation"]}',
                ParagraphStyle("rec", parent=styles["BodyText2"], textColor=NAVY)
            )]],
            colWidths=[5.5*inch],
        )
        rec_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BLUE),
            ("BORDER_COLOR", (0, 0), (-1, -1), BLUE),
            ("BORDER_WIDTH", (0, 0), (-1, -1), 1),
            ("TOPPADDING", (0, 0), (-1, -1), 12),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ("LEFTPADDING", (0, 0), (-1, -1), 16),
            ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ]))
        elements.append(rec_table)
        story.extend(elements)

    story.append(PageBreak())

    # === QUICK WINS ===
    if quick_wins:
        story.append(Paragraph("Quick Wins (Do These This Week)", styles["SectionHead"]))
        story.append(Paragraph(
            "These are low-effort, high-impact changes you can make right now. "
            "No agency needed. Just do them.",
            styles["BodyText2"],
        ))
        for i, win in enumerate(quick_wins, 1):
            story.append(Paragraph(
                f"<b>{i}.</b>  {win}",
                ParagraphStyle("win", parent=styles["BodyText2"], leftIndent=16),
            ))
        story.append(Spacer(1, 16))

    # === REVENUE IMPACT ===
    if revenue_impact:
        story.append(Paragraph("Projected Revenue Impact", styles["SectionHead"]))
        impact_table = Table(
            [[Paragraph(
                f'<font size="14"><b>{revenue_impact}</b></font>',
                ParagraphStyle("impact", parent=styles["BodyText2"],
                               textColor=NAVY, alignment=TA_CENTER, fontSize=14)
            )]],
            colWidths=[5.5*inch],
        )
        impact_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BLUE),
            ("TOPPADDING", (0, 0), (-1, -1), 20),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 20),
        ]))
        story.append(impact_table)
        story.append(Spacer(1, 8))
        story.append(Paragraph(
            "This estimate is based on industry benchmarks for DTC brands that "
            "implement the changes recommended in this audit. Results vary by brand, "
            "but the directional impact is consistent.",
            styles["BodyText2"],
        ))

    story.append(Spacer(1, 24))

    # === CTA ===
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Ready to Fix This?", styles["SectionHead"]))
    story.append(Paragraph(
        "CopyDTC builds AI-powered content systems for DTC brands. We can implement "
        "every recommendation in this audit, usually within the first 30 days. "
        "No long contracts. Cancel anytime. First results in 7 days.",
        styles["BodyText2"],
    ))
    story.append(Spacer(1, 8))
    cta_table = Table(
        [[Paragraph(
            '<b>Book a free 15-minute call: brad@copydtc.com</b>',
            ParagraphStyle("cta", parent=styles["BodyText2"],
                           textColor=white, alignment=TA_CENTER, fontSize=12)
        )]],
        colWidths=[5.5*inch],
    )
    cta_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]))
    story.append(cta_table)

    # Build
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    return output_path


# === SAMPLE DATA (for testing and demo) ===
SAMPLE_AUDIT = {
    "brand_name": "Wild Bites Co.",
    "brand_url": "https://wildbites.co",
    "scores": {
        "Website Copy": 5,
        "Email Marketing": 3,
        "Product Descriptions": 6,
        "Ad Copy": 4,
        "Social Content": 7,
        "SEO / Blog Content": 2,
    },
    "sections": [
        {
            "title": "Website Copy",
            "summary": "Your homepage has a clear value proposition but loses momentum after the hero. The About page reads like a template, and your collection pages have almost no copy at all.",
            "findings": [
                {"text": "Hero headline is strong and benefit-focused", "type": "good"},
                {"text": "Trust badges and social proof visible above the fold", "type": "good"},
                {"text": "Below-the-fold copy is generic and doesn't reinforce your brand voice", "type": "bad"},
                {"text": "Collection pages have zero descriptive copy (missed SEO and conversion opportunity)", "type": "bad"},
                {"text": "About page reads like a corporate template, not a DTC brand story", "type": "bad"},
            ],
            "recommendation": "Rewrite your About page with your founder story and brand mission. Add 150-200 words of keyword-rich copy to each collection page. This alone could improve organic traffic by 20-30%.",
        },
        {
            "title": "Email Marketing",
            "summary": "You have a welcome flow and abandoned cart sequence, but both are underperforming. The welcome series has only 2 emails (should be 5-7), and your abandoned cart emails lack urgency and personalization.",
            "findings": [
                {"text": "Welcome flow exists and triggers correctly", "type": "good"},
                {"text": "Welcome series has only 2 emails (best practice is 5-7)", "type": "bad"},
                {"text": "No post-purchase flow (missing easy repeat revenue)", "type": "bad"},
                {"text": "Abandoned cart emails are generic with no brand voice", "type": "bad"},
                {"text": "No winback sequence for lapsed customers", "type": "bad"},
                {"text": "Subject lines average 3-4 words (too short, low open rates)", "type": "bad"},
            ],
            "recommendation": "Build a 5-email welcome sequence, 3-email abandoned cart flow with escalating urgency, and a post-purchase upsell sequence. Expected impact: 15-25% increase in email-attributed revenue within 60 days.",
        },
        {
            "title": "Product Descriptions",
            "summary": "Your product pages have the basics covered but don't sell. They list features without translating them into benefits. No social proof on product pages.",
            "findings": [
                {"text": "All products have descriptions (no blank pages)", "type": "good"},
                {"text": "High-quality product photography", "type": "good"},
                {"text": "Descriptions are feature-focused, not benefit-focused", "type": "bad"},
                {"text": "No reviews or UGC on product pages", "type": "bad"},
                {"text": "Missing sensory language that drives DTC purchases", "type": "bad"},
            ],
            "recommendation": "Rewrite product descriptions using the benefit-feature-proof framework. Lead with the customer benefit, support with the feature, close with social proof. Add a review integration.",
        },
        {
            "title": "Ad Copy (Meta / Google)",
            "summary": "Your ad library shows mostly image-based ads with minimal copy variation. You're running the same 2-3 headlines across all ad sets, which limits your ability to test and optimize.",
            "findings": [
                {"text": "Consistent visual brand identity across ads", "type": "good"},
                {"text": "Only 2-3 unique headline variations (should be 10+)", "type": "bad"},
                {"text": "No UGC-style ad copy (highest-performing format for DTC)", "type": "bad"},
                {"text": "Google Search ads have generic descriptions, low quality scores likely", "type": "bad"},
                {"text": "No clear testing framework for copy iterations", "type": "bad"},
            ],
            "recommendation": "Create 10 headline variations using different angles: social proof, urgency, benefit-first, problem-agitation, and curiosity. Add UGC-style copy to your creative mix. Expected impact: 20-40% improvement in CTR.",
        },
        {
            "title": "Social Content",
            "summary": "Your Instagram presence is solid with good visual consistency. However, captions are short and don't drive engagement or clicks. No TikTok presence yet.",
            "findings": [
                {"text": "Strong visual brand consistency on Instagram", "type": "good"},
                {"text": "Regular posting schedule (3-4x per week)", "type": "good"},
                {"text": "Good mix of product and lifestyle content", "type": "good"},
                {"text": "Captions average 15 words (should be 50-150 for engagement)", "type": "bad"},
                {"text": "No TikTok presence (massive missed opportunity for DTC)", "type": "bad"},
                {"text": "No clear CTA in posts", "type": "bad"},
            ],
            "recommendation": "Lengthen Instagram captions with storytelling, questions, and clear CTAs. Launch TikTok with behind-the-scenes content, founder stories, and product education. Expected engagement increase: 40-60%.",
        },
        {
            "title": "SEO / Blog Content",
            "summary": "Your blog has 3 posts from 6+ months ago. No keyword strategy is visible. You're leaving organic traffic on the table.",
            "findings": [
                {"text": "Blog exists and is technically functional", "type": "good"},
                {"text": "Only 3 blog posts total", "type": "bad"},
                {"text": "Posts are not optimized for any target keywords", "type": "bad"},
                {"text": "No internal linking strategy", "type": "bad"},
                {"text": "No content calendar or publishing cadence", "type": "bad"},
                {"text": "Missing category pages that could rank for commercial keywords", "type": "bad"},
            ],
            "recommendation": "Publish 2 SEO-optimized blog posts per week targeting long-tail keywords in your niche. Focus on 'best [product] for [use case]' and 'how to [problem your product solves]' formats. Expected impact: 5-10x organic traffic within 6 months.",
        },
    ],
    "quick_wins": [
        "Add 150+ words of copy to every collection page (improves SEO and conversions immediately)",
        "Extend your welcome email series from 2 to 5 emails (use your existing brand voice)",
        "Write 10 new ad headline variations and launch as a split test this week",
        "Add customer reviews to your top 5 product pages",
        "Write longer Instagram captions (50-150 words) with a question or CTA at the end",
    ],
    "revenue_impact": "Estimated 25-40% increase in content-attributed revenue within 90 days",
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a CopyDTC Content Audit PDF")
    parser.add_argument("--brand", help="Brand name")
    parser.add_argument("--url", help="Brand website URL")
    parser.add_argument("--data", help="Path to JSON data file (overrides --brand/--url)")
    parser.add_argument("--output", default="audit-report.pdf", help="Output PDF path")
    parser.add_argument("--sample", action="store_true", help="Generate sample audit (Wild Bites Co.)")
    args = parser.parse_args()

    if args.sample:
        print("Generating sample audit for Wild Bites Co...")
        path = generate_audit(SAMPLE_AUDIT, args.output)
        print(f"Done! Saved to: {path}")
    elif args.data:
        with open(args.data) as f:
            data = json.load(f)
        path = generate_audit(data, args.output)
        print(f"Done! Saved to: {path}")
    else:
        parser.print_help()
        print("\nTip: Run with --sample to generate a demo audit PDF.")

