# Librería para interactuar con el modelo de lenguaje Gemini
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables del archivo .env (busca hacia arriba desde este script)
load_dotenv()

MODELO = "gemini-3.5-flash-lite"

# API KEY de Google Gemini
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Falta GEMINI_API_KEY. Defínela en el archivo .env")

# Cliente para conectarse a la API de Google
CLIENTE = genai.Client(api_key=API_KEY)


def preguntar(prompt, temperature=None, formato=None):

    configuracion = {
        "thinking_config": types.ThinkingConfig(
            thinking_level="minimal",
            include_thoughts=False
        )
    }

    # Configurar temperatura
    if temperature is not None:
        configuracion["temperature"] = temperature

    # Configurar formato de respuesta
    if formato is not None:
        configuracion["response_mime_type"] = "application/json"

        if isinstance(formato, dict):
            configuracion["response_schema"] = formato

    respuesta = CLIENTE.models.generate_content(
        model=MODELO,
        contents=prompt,
        config=types.GenerateContentConfig(**configuracion)
    )

    return (respuesta.text or "").strip()


if __name__ == "__main__":

    print(preguntar("¿Cuál es la capital de Perú?"))