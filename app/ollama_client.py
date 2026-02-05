import requests
import json
from config import (
    OLLAMA_URL,
    MODEL_NAME,
    NUM_CTX,
    NUM_PREDICT,
    TEMPERATURE,
    TOP_P,
)


def warm_model():
    try:
        requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": "Translate to Telugu: Hello",
                "stream": False,
                "options": {"num_ctx": 128},
            },
            timeout=5,
        )
    except:
        pass


def translate_stream(text):
    prompt = f"""Translate the following text into Telugu.
Return only the Telugu translation.
Do not explain or add extra text.

Text:
{text}
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": True,
        "options": {
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "num_ctx": NUM_CTX,
            "num_predict": NUM_PREDICT,
        },
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=True,
        timeout=60,
    )
    response.raise_for_status()

    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue

        data = json.loads(line)

        if data.get("done"):
            break

        yield data.get("response", "")
