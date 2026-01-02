from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY
from config.settings import EVALUATOR_MODEL

evaluator_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=EVALUATOR_MODEL,
    temperature=0.2
)
