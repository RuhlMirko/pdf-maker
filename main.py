import fpdf
from fpdf.enums import XPos, YPos

pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.output('output.pdf')
