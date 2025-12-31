from crewai import Crew, Task
from agents.planner_agent import planner_agent
from agents.analyst_agent import analyst_agent
from agents.validator_agent import validator_agent
from agents.report_agent import report_agent


def run_crew(user_problem: str):

    plan_task = Task(
        description=f"Create a step-by-step plan to solve: {user_problem}",
        expected_output="A clear, ordered list of steps to solve the problem",
        agent=planner_agent
    )

    analysis_task = Task(
        description="Analyze the problem following the plan and extract insights",
        expected_output="Detailed analysis with insights, causes, and observations",
        agent=analyst_agent
    )

    validation_task = Task(
        description="Review the analysis for correctness, logic, and completeness",
        expected_output="Validated analysis with any corrections or confirmations",
        agent=validator_agent
    )

    report_task = Task(
        description="Create an executive-level summary with recommendations",
        expected_output="Professional executive report with actionable recommendations",
        agent=report_agent
    )

    crew = Crew(
        agents=[
            planner_agent,
            analyst_agent,
            validator_agent,
            report_agent
        ],
        tasks=[
            plan_task,
            analysis_task,
            validation_task,
            report_task
        ],
        verbose=True
    )

    return crew.kickoff()
