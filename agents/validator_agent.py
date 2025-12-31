from crewai import Agent
from config.llm import gemini_llm

validator_agent = Agent(
    role="Validator Agent",
    goal="Verify correctness and eliminate hallucinations",
    backstory="You are a strict reviewer ensuring correctness and logic.",
    llm=gemini_llm,
    verbose=True
)
