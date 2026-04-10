from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(value, status, fert):
    doc = SimpleDocTemplate("logs/report.pdf")
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Gas Detection Report", styles['Title']))
    content.append(Paragraph(f"Gas Value: {value}", styles['Normal']))
    content.append(Paragraph(f"Fertilizer: {fert}", styles['Normal']))
    content.append(Paragraph(f"Status: {status}", styles['Normal']))

    if status == "SAFE":
        content.append(Paragraph("Condition is safe.", styles['Normal']))
    elif status == "WARNING":
        content.append(Paragraph("Moderate risk detected.", styles['Normal']))
    else:
        content.append(Paragraph("Dangerous condition!", styles['Normal']))

    doc.build(content)
