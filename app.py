# app.py
import os
import streamlit as st
from dotenv import load_dotenv
from crew import legal_assistant_crew
import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
from voice.speech_to_text import get_voice_input
from voice.text_to_speech import speak

load_dotenv()

st.set_page_config(page_title="AI Legal Assistant", page_icon="🧠", layout="wide")

st.title("⚖️ Personal AI Legal Assistant")
st.markdown(
    "Enter a legal problem in plain English. This assistant will help you:\n"
    "- Understand the legal issue\n"
    "- Find applicable IPC sections\n"
    "- Retrieve matching precedent cases\n"
    "- Generate a formal legal document"
)
with st.form("legal_form"):
    user_input = st.text_area(
    "📝 Describe your legal issue:",
    placeholder="✍️ Write your legal issue here... (e.g., Someone stole my phone and threatened me)",
    height=250
)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])

    with col1:
        submitted = st.form_submit_button("🔍 Run Legal Assistant")

    with col2:
        voice_btn = st.form_submit_button("🎤 Speak")
#Voicelogic 
if voice_btn:
    with st.spinner("🎤 Listening... Speak now"):
        user_input = get_voice_input()

    if user_input == "Could not understand audio":
        st.error("❌ Could not understand audio. Try again.")
        user_input = ""   
        voice_btn = False  

        # 👇 BONUS LINE HERE
        st.warning("🎤 Please try speaking again clearly.")

    else:
        st.success(f"🗣️ You said: {user_input}")
#RunAI
if submitted or voice_btn:
    if not user_input.strip():
        st.warning("Please enter a legal issue to analyze.")
    else:
        with st.spinner("🔎 Analyzing your case and preparing legal output..."):
            result = legal_assistant_crew.kickoff(inputs={"user_input": user_input})

        st.success("✅ Legal Assistant completed the workflow!")

        st.subheader("📄 Final Output")
        st.markdown(result if isinstance(result, str) else str(result))

        # Optional: Expand sections if intermediate steps are structured (later enhancement)
