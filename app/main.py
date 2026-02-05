import streamlit as st
from ollama_client import translate_stream, warm_model

st.set_page_config(
    page_title="English → Telugu Translator",
    page_icon="🌏",
    layout="centered",
)

st.title("🌏 English → Telugu Translator")


# Warm up model once
@st.cache_resource
def init():
    warm_model()


init()

text = st.chat_input("Enter English text to translate into Telugu...")

if text:
    with st.chat_message("user"):
        st.markdown(text)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        translated_text = ""

        for token in translate_stream(text):
            translated_text += token
            placeholder.markdown(translated_text)
