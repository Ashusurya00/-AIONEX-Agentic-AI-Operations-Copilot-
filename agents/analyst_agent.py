from crewai import Agent
from config.llm import gemini_llm
from tools.data_tools import CSVAnalysisTool

analyst_agent = Agent(
    role="Analyst Agent",
    goal="Analyze data, identify patterns, risks, and insights",
    backstory="You are a senior data analyst skilled in reasoning and analytics.",
    llm=gemini_llm,
    tools=[CSVAnalysisTool()],   # ✅ CORRECT
    verbose=True
)
