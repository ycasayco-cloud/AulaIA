from pypdf import PdfReader

def leer_pdf(ruta):
    reader = PdfReader(ruta)
    texto = ""

    for page in reader.pages:
        texto += page.extract_text()

    return texto