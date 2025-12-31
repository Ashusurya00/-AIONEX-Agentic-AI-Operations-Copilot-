from crewai import LLM
from config.settings import GEMINI_API_KEY

gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=GEMINI_API_KEY
)
