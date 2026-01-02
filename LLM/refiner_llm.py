from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY
from config.settings import REFINER_MODEL

refiner_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model= REFINER_MODEL,
    temperature=0.2
)
