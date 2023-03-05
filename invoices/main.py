import pandas as pd
import openpyxl
import glob
from fpdf import FPDF
from pathlib import Path



sheets = glob.glob('sheets/*.xlsx')
print(sheets)

for sheet in sheets:
    df = pd.read_excel(sheet, sheet_name='Sheet 1')
    print(df)
    filename = Path(sheet).stem

    invoice_nr = filename.split("-")[0] 
    print(invoice_nr)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()
    pdf.set_font(family="Courier", style="", size=12)
    pdf.set_text_color(32, 31, 33)

    pdf.cell(w=50, h=8, txt=f"invoice_nr.{invoice_nr}", align="L", ln=1)
    pdf.output(f"pdf/{filename}.pdf")