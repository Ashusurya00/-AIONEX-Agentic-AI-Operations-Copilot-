from crewai import Agent
from config.llm import gemini_llm

report_agent = Agent(
    role="Report Agent",
    goal="Generate professional executive-level reports",
    backstory="You create concise, business-ready reports.",
    llm=gemini_llm,
    verbose=True
)
