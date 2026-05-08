from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

from rag import buscar_contexto, guardar_documento
from ia import preguntar_ia
from loaders.pdf_loader import leer_pdf

import shutil

app = FastAPI()

class Pregunta(BaseModel):
    pregunta: str

@app.get("/")
def inicio():
    return {"mensaje": "AulaIA funcionando correctamente 🚀"}

@app.post("/preguntar")
def preguntar(data: Pregunta):

    contexto = buscar_contexto(data.pregunta)

    respuesta = preguntar_ia(
        contexto,
        data.pregunta
    )

    return {
        "respuesta": respuesta
    }

@app.post("/subir-pdf")
def subir_pdf(file: UploadFile):

    ruta = f"uploads/{file.filename}"

    with open(ruta, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    texto = leer_pdf(ruta)

    guardar_documento(texto, file.filename)

    return {
        "mensaje": "PDF procesado correctamente"
    }