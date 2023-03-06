from fpdf import FPDF
import glob
from pathlib import Path


# create a list of text filepaths
filepaths = glob.glob("files/*.txt")

# create one pdf
pdf = FPDF(orientation="P", unit="mm", format="A4")
# loop through each file
for filepath in filepaths:
    # add a page for each file
    pdf.add_page()

    # get the filename without the extension convert to title eg cat
    filename = Path(filepath).stem # .stem part of pathlib
    name = filename.title()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.cell(w=0, h=6, txt=name, align="L", ln=1)
    pdf.cell(w=0, h=15, txt="_________________________________________", align="C", ln=5)

    # get the text out of each file
    with open(filepath, 'r') as file:
        text = file.read()
        pdf.set_font(family="Times", style="", size=12)
        pdf.set_text_color(r=0, g=0, b=0)
        pdf.multi_cell(w=0, h=6, txt=text)


pdf.output("textfiles.pdf")

