from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY

def get_llm(model_name: str, temperature: float = 0.7):
    return ChatGroq(
        model=model_name,
        temperature=temperature,
        groq_api_key=GROQ_API_KEY
    )
