from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY
from config.settings import HTML_MODEL

html_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=HTML_MODEL,
    temperature=0.0
)
