from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(text):
    file = "report.pdf"
    c = canvas.Canvas(file, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()
    return file