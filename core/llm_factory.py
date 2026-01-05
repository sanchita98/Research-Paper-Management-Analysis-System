from langchain_groq import ChatGroq
from config.settings import settings

def get_llm(model="openai/gpt-oss-120b", temperature=0):
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=model,
        temperature=temperature
    )
