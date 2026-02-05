# import os
# from dotenv import load_dotenv

# load_dotenv()

# OLLAMA_URL = os.getenv("OLLAMA_URL")
# MODEL_NAME = os.getenv("MODEL_NAME")

# TEMPERATURE = float(os.getenv("TEMPERATURE", 0.2))
# TOP_P = float(os.getenv("TOP_P", 0.9))
# NUM_CTX = int(os.getenv("NUM_CTX", 512))
# NUM_PREDICT = int(os.getenv("NUM_PREDICT", 20000))


import os
from dotenv import load_dotenv

load_dotenv()


def get_int(name, default):
    try:
        return int(os.getenv(name, default))
    except (TypeError, ValueError):
        return default


def get_float(name, default):
    try:
        return float(str(os.getenv(name, default)).strip().rstrip(","))
    except (TypeError, ValueError):
        return default


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL_NAME = os.getenv("MODEL_NAME", "translategemma:latest")

NUM_CTX = get_int("NUM_CTX", 512)
NUM_PREDICT = get_int("NUM_PREDICT", 200000)
TEMPERATURE = get_float("TEMPERATURE", 0.2)
TOP_P = get_float("TOP_P", 0.9)
