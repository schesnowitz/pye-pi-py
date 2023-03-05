from fpdf import FPDF
import pandas as pd

# orientation="P" or L for landscape unit millimeters
pdf = FPDF(orientation="P", unit="mm", format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(r=254, g=0, b=0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # pdf.line(10, 20, 200, 20)
# pdf.ln adds break lines
#     set the footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(r=254, g=0, b=0)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)



    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # set footer
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(r=254, g=0, b=0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
pdf.output("topics.pdf")