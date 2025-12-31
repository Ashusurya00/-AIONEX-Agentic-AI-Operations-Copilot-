🤖 AIONEX – Agentic AI Operations Copilot

AIONEX is an enterprise-style Agentic AI system that uses multiple autonomous AI agents to analyze real business data, reason step-by-step, validate insights, and generate executive-ready reports.

Unlike traditional chatbots or single-prompt GenAI apps, AIONEX demonstrates true agentic behavior — planning, tool usage, verification, and decision-oriented reporting.

🚀 Key Highlights

✅ True Agentic AI architecture (not just a chatbot)

🧠 Multi-agent collaboration using CrewAI

🔍 Tool-enabled agents for real data analysis

⚙️ Gemini AI for advanced reasoning & long context

📊 Works with real CSV business data

🎨 Professional Streamlit SaaS-style UI

🧪 Built with production-grade structure & best practices

🧠 What is Agentic AI?

Agentic AI systems are capable of:

Planning their own actions

Using tools to interact with data

Validating outputs to reduce hallucinations

Collaborating across specialized agents

AIONEX simulates an AI analyst team, where each agent has a clear role and responsibility.

🧩 System Architecture
🔹 Agents Used
Agent	Responsibility
Planner Agent	Breaks down the business problem into actionable steps
Analyst Agent	Analyzes structured data using Pandas tools
Validator Agent	Verifies insights for correctness and logic
Report Agent	Generates executive-level summaries and recommendations

Each agent is powered by Gemini AI and orchestrated using CrewAI.

🛠️ Tech Stack

LLM: Gemini AI

Agent Framework: CrewAI

Backend: Python

Data Tools: Pandas

UI: Streamlit (custom CSS + animations)

Architecture: Agentic AI (multi-agent orchestration)

📂 Project Structure
agentic_ai_copilot/
│
├── app.py                  # Streamlit UI
├── assets/
│   └── AI_FIN.jpg           # Background image
│
├── agents/
│   ├── planner_agent.py
│   ├── analyst_agent.py
│   ├── validator_agent.py
│   └── report_agent.py
│
├── crew/
│   └── crew_setup.py
│
├── tools/
│   └── data_tools.py        # CSV analysis tool (BaseTool)
│
├── config/
│   ├── settings.py          # Environment config
│   └── llm.py               # Gemini LLM setup
│
├── data/
│   └── sales_performance_data.csv
│
├── test_run.py              # Terminal test runner
├── requirements.txt
└── README.md

📊 Example Use Case

Scenario:
A business uploads sales performance data and asks:

“Analyze the uploaded sales data to identify reasons for the sales decline and provide actionable recommendations.”

🔍 AIONEX Automatically:

Detects declining trends

Identifies regional underperformance

Analyzes marketing spend vs outcomes

Correlates customer complaints with revenue drop

Produces an executive-ready report

🖥️ UI Preview

The Streamlit interface provides:

CSV upload

Business problem input

Real-time agent execution

Clean, executive-style output

Glassmorphism design with background visuals

⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/ashusurya00/aionex-agentic-ai.git
cd aionex-agentic-ai

2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here

▶️ Run the Application
🖥️ Streamlit UI
streamlit run app.py

🧪 Terminal Test (Explains agent flow)
python test_run.py

🧪 Sample Prompts to Try
Analyze the uploaded sales data to identify key reasons for the sales decline.
Highlight regional issues, marketing inefficiencies, and customer behavior patterns.

Perform a root cause analysis on the sales performance data and generate
executive-level recommendations.

Act as a business intelligence system and detect risks and warning signals
in the sales data.

🧠 What This Project Demonstrates

Deep understanding of Agentic AI systems

Multi-agent orchestration & task delegation

Tool calling and data reasoning

LLM hallucination control via validation

End-to-end AI product development

Professional UI & system design

🚀 Future Enhancements

🔄 Live agent-by-agent execution streaming

🧭 Timeline visualization (Planner → Analyst → Validator)

📄 PDF report export

☁️ Deployment on Streamlit Cloud / AWS

🌙 Dark / Light mode toggle


If you’d like to discuss Agentic AI, GenAI systems, or collaboration opportunities, feel free to connect.

⭐ If you like this project, don’t forget to star the repo!
