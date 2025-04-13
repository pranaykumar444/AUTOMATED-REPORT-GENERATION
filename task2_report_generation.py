import pandas as pd
from fpdf import FPDF

try:
    df = pd.read_csv("student_scores.csv")
except FileNotFoundError:
    print("Error: student_scores.csv file not found.")
    exit()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Student Score Report", ln=True, align='C')

for i in range(len(df)):
    row = f"{df.iloc[i]['Name']} - Score: {df.iloc[i]['Score']}"
    pdf.cell(200, 10, txt=row, ln=True)

pdf.output("score_report.pdf")
print("PDF report generated: score_report.pdf")