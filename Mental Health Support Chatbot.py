import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()

# ----------------------------
# Initialize Groq Client
# ----------------------------
client = Groq(api_key=groq_api_key)

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Mental Health Support Chatbot", page_icon="🧠")

st.title("🧠 Mental Health Support Chatbot")
st.caption("Ask me anything about your mental health.")

# ----------------------------
# System Prompt
# ----------------------------
system_prompt = """
You are an expert in Mental Health Support.
Respond in 2-3 short supportive sentences.
Answer ONLY mental health related questions.
If the question is unrelated, politely refuse.
If user mentions self-harm or suicide, encourage seeking professional help.
"""

# ----------------------------
# Sidebar Settings
# ----------------------------
with st.sidebar:
    st.header("⚙ Settings")

    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.1
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ----------------------------
# Initialize Chat History
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Display Chat History
# ----------------------------
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)

# ----------------------------
# User Input
# ----------------------------
user_input = st.chat_input("Ask about stress, anxiety, burnout...")

if user_input:

    # Store user message
    st.session_state.messages.append(("user", user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    *[
                        {"role": role, "content": text}
                        for role, text in st.session_state.messages
                    ]
                ],
                temperature=temperature,
                stream=True
            )

            for chunk in response:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        except Exception as e:
            full_response = "⚠ API error or quota exceeded. Try again later."
            message_placeholder.markdown(full_response)

    # Store assistant response
    st.session_state.messages.append(("assistant", full_response))

# ----------------------------
# Footer
# ----------------------------
st.sidebar.markdown("---")
st.sidebar.write(f"Messages sent: {len(st.session_state.messages)//2}")
