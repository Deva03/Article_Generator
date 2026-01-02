from langchain_groq import ChatGroq
from config.settings import WRITER_MODEL
from config.settings import GROQ_API_KEY

def get_writer_llm(temperature: float):
    return ChatGroq(
        api_key=GROQ_API_KEY,
        model=WRITER_MODEL,
        temperature=temperature
    )
