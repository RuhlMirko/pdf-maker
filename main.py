import fpdf
import pandas as pd

pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv('topics.csv')

pdf.set_font('Times', 'B', 20)

pdf.add_page()
for index, row in df.iterrows():
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Times', 'B', 20)
    pdf.cell(h=10, text=row['Topic'], new_x="LMARGIN", new_y="NEXT")

    for page in range(row['Pages']):
        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)
        pdf.set_y(-10)
        # Setting font: helvetica italic 8
        pdf.set_font("helvetica", "I", 8)
        # Changing text color:
        pdf.set_text_color(100, 100, 100)
        # Printing page number:
        pdf.cell(0, 10, f"{pdf.page_no()}/{{nb}} - {row['Topic']}", align="R")
        pdf.add_page()

pdf.output('output.pdf')
