import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

# Historial temporal
historial_chat = []


def preguntar_ia(contexto, pregunta):

    global historial_chat

    # Validar API KEY
    if not API_KEY:
        return "Error: No se encontró OPENROUTER_API_KEY en el archivo .env"

    # Limitar contexto PDF
    contexto = contexto[:5000]

    # Mensaje sistema
    system_prompt = f"""
Eres AulaIA, un asistente académico especializado EXCLUSIVAMENTE
en el contenido del documento proporcionado.

REGLAS OBLIGATORIAS:

1. Responde únicamente preguntas relacionadas con el contenido
   del documento.

2. Utiliza exclusivamente la información proporcionada en el
   CONTEXTO DEL DOCUMENTO.

3. No utilices conocimientos externos para responder.

4. No inventes información.

5. Si la pregunta no está relacionada con el documento,
   responde EXACTAMENTE:

"Lo siento, mi función es responder únicamente preguntas relacionadas
con el contenido del documento proporcionado."

6. Si la pregunta está relacionada con el documento pero la
   información necesaria no aparece en el contexto, responde:

"Lo siento, esa información no se encuentra en el documento
proporcionado."

7. No respondas preguntas sobre temas generales, programación,
   política, noticias, entretenimiento, matemáticas u otros temas
   si no están relacionados con el documento.

8. Mantén un tono académico, claro y profesional.

CONTEXTO DEL DOCUMENTO:
{contexto}
"""

    # Construir mensajes
    mensajes = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Agregar historial
    mensajes.extend(historial_chat)

    # Nueva pregunta
    mensajes.append({
        "role": "user",
        "content": pregunta
    })

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "AulaIA"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": mensajes,
        "temperature": 0.7,
        "max_tokens": 400
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=30
        )

        print("STATUS:", response.status_code)

        resultado = response.json()

        print("RESPUESTA API:")
        print(resultado)

        # Error HTTP
        if response.status_code != 200:
            return f"Error API ({response.status_code}): {resultado}"

        # Validar respuesta
        if "choices" not in resultado:
            return f"Respuesta inválida: {resultado}"

        respuesta_ia = resultado["choices"][0]["message"]["content"]

        # Guardar historial
        historial_chat.append({
            "role": "user",
            "content": pregunta
        })

        historial_chat.append({
            "role": "assistant",
            "content": respuesta_ia
        })

        # Limitar historial
        historial_chat = historial_chat[-10:]

        return respuesta_ia

    except requests.exceptions.Timeout:
        return "Error: Tiempo de espera agotado."

    except requests.exceptions.ConnectionError:
        return "Error: No se pudo conectar con la IA."

    except Exception as e:
        return f"Error inesperado: {str(e)}"