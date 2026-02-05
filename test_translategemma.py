# import streamlit as st
# import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "translategemma:latest"

# st.set_page_config(page_title="English to Telugu Translator", page_icon="🌏")

# st.title("🌏 English → Telugu Translator")

# # Initialize history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # User input
# prompt = st.chat_input("Type text to translate into Telugu...")

# if prompt:
#     # Show user message
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # 🔹 Translation prompt
#     translation_prompt = f"""
# Translate the following text into Telugu.
# Only return the translated Telugu text.

# Text:
# {prompt}
# """

#     payload = {
#         "model": MODEL_NAME,
#         "prompt": translation_prompt,
#         "stream": False,
#         "options": {
#             "temperature": 0.2,
#             "top_p": 0.9,
#             "num_ctx": 512,
#             "num_predict": 200,
#         },
#     }

#     with st.chat_message("assistant"):
#         with st.spinner("Translating..."):
#             response = requests.post(OLLAMA_URL, json=payload)
#             response.raise_for_status()
#             answer = response.json()["response"]

#             st.markdown(answer)

#     st.session_state.messages.append({"role": "assistant", "content": answer})


import streamlit as st
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "translategemma:latest"

st.set_page_config(
    page_title="English → Telugu Translator", page_icon="🌏", layout="centered"
)

st.title("🌏 English → Telugu Translator")
# st.caption("Powered by Ollama • Optimized for speed")


# 🔥 Warm-up model to avoid cold start latency
@st.cache_resource
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


warm_model()

# User input
text = st.chat_input("Enter English text to translate into Telugu...")

if text:
    with st.chat_message("user"):
        st.markdown(text)

    # ⚡ Minimal, strict translation prompt
    translation_prompt = f"""Translate the following text into Telugu.
Return only the Telugu translation.
Do not explain or add extra text.

Text:
{text}
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": translation_prompt,
        "stream": True,
        "options": {
            "temperature": 0.2,
            "top_p": 0.9,
            "num_ctx": 512,
            "num_predict": 2000,
        },
    }

    with st.chat_message("assistant"):
        placeholder = st.empty()
        translated_text = ""

        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=60)
        response.raise_for_status()

        for line in response.iter_lines(decode_unicode=True):
            if not line:
                continue

            data = json.loads(line)

            if data.get("done"):
                break

            token = data.get("response", "")
            translated_text += token
            placeholder.markdown(translated_text)
