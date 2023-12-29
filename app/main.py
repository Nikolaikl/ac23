import os

import openai
import streamlit as st
from dotenv import load_dotenv

from app.utils.fetch_papers import fetch_papers

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")





st.title("LLama-2 Wissens-Chatbot")

user_input = st.text_input("Frage zum Llama-2:")

if st.button("Fragen"):
    if user_input:
        papers = fetch_papers()
        st.text("Einige Papiere zu Llama-2:")
        for paper in papers:
            st.text(paper)
