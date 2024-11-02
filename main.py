import fpdf
import pandas as pd

pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
df = pd.read_csv('topics.csv')

pdf.set_font('Times', 'B', 20)


pdf.add_page()
for index, row in df.iterrows():
    pdf.set_text_color(100, 100, 100)
    pdf.cell(h=10, text=row['Topic'], new_x="LMARGIN", new_y="NEXT")
    pdf.line(10, 20, 200, 20)
    # First

    for page in range(int(row['Pages'])):
        pdf.add_page()

pdf.output('output.pdf')
