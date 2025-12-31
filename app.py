import streamlit as st
import tempfile
import os
import base64

from crew.crew_setup import run_crew


# ------------------ UTILS ------------------
def get_base64_bg(image_path: str) -> str:
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# ------------------ LOAD BACKGROUND IMAGE ------------------
BG_IMAGE_PATH = "assets/AI_FIN.jpg"
bg_image = get_base64_bg(BG_IMAGE_PATH)


# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Autonomous Multi-Agent Reasoning Engine",
    page_icon="🤖",
    layout="wide"
)


# ------------------ CUSTOM CSS ------------------
st.markdown(
    f"""
    <style>

    /* App background */
    .stApp {{
        background: linear-gradient(
            rgba(0, 0, 0, 0.65),
            rgba(0, 0, 0, 0.65)
        ),
        url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Fade animation */
    @keyframes fadeUp {{
        from {{ opacity: 0; transform: translateY(15px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    .fade {{
        animation: fadeUp 0.7s ease-in-out;
    }}

    /* Glassmorphism card */
    .glass {{
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-radius: 16px;
        padding: 1.6rem;
        border: 1px solid rgba(255,255,255,0.25);
        color: white;
        margin-bottom: 1.5rem;
    }}

    /* Buttons */
    div.stButton > button {{
        background: linear-gradient(135deg, #7f5af0, #5a7cff);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.6rem;
        font-size: 16px;
        transition: all 0.3s ease;
    }}

    div.stButton > button:hover {{
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background: rgba(20, 20, 30, 0.85);
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ------------------ HEADER ------------------
st.markdown(
    """
    <div class="glass fade">
        <h1>🤖 Agentic AI Operations Copilot</h1>
        <p style="font-size:18px; opacity:0.9;">
            Autonomous multi-agent intelligence powered by <b>Gemini AI</b> & <b>CrewAI</b>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ------------------ SIDEBAR ------------------
st.sidebar.header("📂 Data Input")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

st.sidebar.markdown("---")
st.sidebar.write(
    "This system uses multiple AI agents to autonomously plan, analyze, "
    "validate, and generate executive-level insights."
)


# ------------------ MAIN CONTENT ------------------
left, right = st.columns([1, 1.3], gap="large")


# ------------------ LEFT CARD ------------------
with left:
    st.markdown('<div class="glass fade">', unsafe_allow_html=True)

    st.subheader("📝 Business Problem")

    user_problem = st.text_area(
        "Describe the problem",
        placeholder="Analyze sales decline and recommend corrective actions",
        height=130
    )

    run_button = st.button("🚀 Run Agentic Analysis")

    st.markdown('</div>', unsafe_allow_html=True)


# ------------------ RIGHT CARD ------------------
with right:
    st.markdown('<div class="glass fade">', unsafe_allow_html=True)

    st.subheader("🧠 Agent Output")

    if run_button:

        if not uploaded_file or not user_problem:
            st.warning("Please upload a CSV file and enter a problem.")
        else:
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
                tmp.write(uploaded_file.read())
                csv_path = tmp.name

            with st.spinner("Agents are reasoning and collaborating..."):
                result = run_crew(
                    f"{user_problem}. Use data from file: {csv_path}"
                )

            st.markdown("### 📊 Executive Report")
            st.markdown(result)

            os.remove(csv_path)
            st.success("Analysis completed")

    else:
        st.info("Run an analysis to see agent output here.")

    st.markdown('</div>', unsafe_allow_html=True)


# ------------------ FOOTER ------------------
st.markdown(
    """
    <p style="text-align:center; color:#c7c7c7; margin-top:2rem;">
        Built with ❤️ using Agentic AI • Gemini • CrewAI
    </p>
    """,
    unsafe_allow_html=True
)
