import os
import requests

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

def preguntar_ia(contexto, pregunta):

    prompt = f"""
    Responde como un asistente académico.

    CONTEXTO:
    {contexto}

    PREGUNTA:
    {pregunta}
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        URL,
        headers=headers,
        json=data
    )

    resultado = response.json()

    print(resultado)

    return resultado["choices"][0]["message"]["content"]