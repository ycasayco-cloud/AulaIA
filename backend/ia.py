import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

historial_chat = []


def preguntar_ia(contexto, pregunta):

    global historial_chat

    if not API_KEY:
        return "Error: No se encontró OPENROUTER_API_KEY."

    if not contexto:
        return "Lo siento, mi función es responder únicamente preguntas relacionadas con el contenido del documento proporcionado."

    contexto = contexto[:8000]

    system_prompt = f"""
Eres AulaIA, un asistente académico especializado en el documento
proporcionado por el docente.

Tu función principal es ayudar al estudiante a comprender,
explicar y analizar el contenido de ese documento.

REGLAS:

1. Responde únicamente utilizando la información contenida en el
   documento.

2. Puedes explicar, resumir, definir, comparar o desarrollar
   conceptos que estén presentes en el documento.

3. Si el estudiante pregunta de forma general sobre "el documento",
   "el contenido", "de qué trata", "qué puedes explicar",
   "explícame el documento" o expresiones similares, debes
   interpretar que se refiere al documento proporcionado y
   responder utilizando su contenido.

4. Si el estudiante saluda, puedes responder brevemente y recordar
   que puedes ayudarle con el documento.

5. Si la pregunta no tiene relación con el documento, responde
   exactamente:

"Lo siento, mi función es responder únicamente preguntas relacionadas
con el contenido del documento proporcionado."

6. Si la pregunta está relacionada con el documento pero la
   información solicitada no aparece en él, responde:

"Lo siento, esa información no se encuentra en el documento
proporcionado."

7. No utilices conocimientos externos para completar una respuesta.

8. No inventes información.

9. Mantén un tono académico, claro, amigable y profesional.

DOCUMENTO PROPORCIONADO:
{contexto}
"""

    mensajes = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    mensajes.extend(historial_chat)

    mensajes.append({
        "role": "user",
        "content": pregunta
    })

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://aulaia.onrender.com",
        "X-Title": "AulaIA"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": mensajes,
        "temperature": 0.3,
        "max_tokens": 500
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=30
        )

        resultado = response.json()

        print("STATUS:", response.status_code)
        print("RESPUESTA API:", resultado)

        if response.status_code != 200:
            return f"Error API ({response.status_code}): {resultado}"

        if "choices" not in resultado:
            return f"Respuesta inválida: {resultado}"

        respuesta_ia = resultado["choices"][0]["message"]["content"]

        historial_chat.append({
            "role": "user",
            "content": pregunta
        })

        historial_chat.append({
            "role": "assistant",
            "content": respuesta_ia
        })

        historial_chat = historial_chat[-10:]

        return respuesta_ia

    except requests.exceptions.Timeout:
        return "Error: Tiempo de espera agotado."

    except requests.exceptions.ConnectionError:
        return "Error: No se pudo conectar con la IA."

    except Exception as e:
        return f"Error inesperado: {str(e)}"