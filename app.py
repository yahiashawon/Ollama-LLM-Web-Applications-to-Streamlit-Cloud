import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Gemma 3 Vision Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🔬 Gemma 3 Vision Agent")

st.warning("⚠️ Make sure Ollama is running with: OLLAMA_ORIGINS=* ollama serve")

html_file_path = "gemma3_vision_agent.html"

if os.path.exists(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    components.html(html_content, height=1000, scrolling=True)
else:
    st.error(f"File not found: {html_file_path}")
