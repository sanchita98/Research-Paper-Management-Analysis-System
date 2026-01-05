"""
settings.py
-----------
Central configuration loader.

Supports:
- Local development via .env
- Streamlit Cloud via st.secrets
"""

import os
from dotenv import load_dotenv

load_dotenv()

def get_groq_api_key():
    """
    Fetch GROQ API key from:
    1. Streamlit secrets (cloud)
    2. Environment variables (local)
    """
    try:
        import streamlit as st
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    return os.getenv("GROQ_API_KEY")


class Settings:
    GROQ_API_KEY = get_groq_api_key()

    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY not found. "
            "Add it to Streamlit Secrets or .env file."
        )


settings = Settings()
