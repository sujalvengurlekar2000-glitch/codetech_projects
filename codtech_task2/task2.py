import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

CSV_FILE = "data.csv"
PDF_OUTPUT = "analysis_report.pdf"

# Read data
df = pd.read_csv(CSV_FILE)
summary = df.describe()

# PDF Setup
styles = getSampleStyleSheet()
doc = SimpleDocTemplate(PDF_OUTPUT, pagesize=letter)
elements = []

# Title
elements.append(Paragraph("Automated Data Analysis Report", styles["Title"]))
elements.append(Spacer(1, 12))

# Subtitle
elements.append(Paragraph("Statistical Summary", styles["Heading2"]))
elements.append(Spacer(1, 12))

# Convert pandas summary to a table
table_data = [["Statistic"] + list(summary.columns)]

for stat in summary.index:
    row = [stat] + [round(summary[col][stat], 3) for col in summary.columns]
    table_data.append(row)

# Create the table
table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ("FONTNAME", (0,0), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,0), (-1,-1), 10),
    ("ALIGN", (1,1), (-1,-1), "RIGHT"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE")
]))

elements.append(table)

# Generate PDF
doc.build(elements)

print("PDF generated successfully!")