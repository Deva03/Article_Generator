from dotenv import load_dotenv
import os

load_dotenv()

# Groq Models
WRITER_MODEL = "openai/gpt-oss-20b"
EVALUATOR_MODEL = "openai/gpt-oss-20b"
REFINER_MODEL = "llama-3.3-70b-versatile"
HTML_MODEL = "llama-3.3-70b-versatile"


EVALUATION_THRESHOLD = 7.5
MAX_RETRIES = 3

GROQ_API_KEY = "API_Key"

# Search (Serper)
SERPER_API_KEY = "SERPER_KEY"
SEARCH_RESULTS_LIMIT = 3

