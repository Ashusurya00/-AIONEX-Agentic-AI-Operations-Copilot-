from crewai import Agent
from config.llm import gemini_llm

planner_agent = Agent(
    role="Planner Agent",
    goal="Break down the user's problem into clear, actionable steps",
    backstory=(
        "You are an expert AI planner who converts complex business problems "
        "into structured execution plans."
    ),
    llm=gemini_llm,   # ✅ IMPORTANT
    verbose=True,
    allow_delegation=True
)
