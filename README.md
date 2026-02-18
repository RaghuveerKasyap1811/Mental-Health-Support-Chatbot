# 🧠 Mental Health Support Chatbot

AI-powered supportive chatbot built with Streamlit and Groq API.

# 📌 Overview

This project is a lightweight conversational AI application designed to provide short, supportive responses to mental health–related queries such as stress, anxiety, burnout, and emotional regulation.

The chatbot enforces strict scope boundaries and includes basic crisis-aware behavior through controlled system prompting.

⚠ This is an educational AI project and not a replacement for professional therapy.

# 🚀 Features

Real-time streaming responses

Adjustable response creativity (temperature control)

Session-based chat memory

Mental health–only response enforcement

Basic crisis-response guardrails

Clean and minimal Streamlit UI

# 🛠 Tech Stack

Python

Streamlit

Groq API (LLaMA models)

python-dotenv

### 📂 Project Structure
```
├── app.py
├── .env
├── requirements.txt
└── README.md
```
# ⚙ Installation
1️⃣ Clone the Repository
```
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
```
2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

Or manually:

pip install streamlit groq python-dotenv

3️⃣ Add API Key

Create a .env file:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the Groq console.

4️⃣ Run the Application
```
streamlit run app.py
```
# 🧠 How It Works

User inputs a mental health–related question.

The system prompt enforces:

Scope restriction (mental health only)

Short supportive responses

No medical diagnosis

Crisis escalation messaging

Chat history is maintained using Streamlit session state.

Groq LLaMA model generates responses.

Streaming output updates in real-time.

# 🔐 Safety & Guardrails

The chatbot:

Refuses non–mental health questions

Avoids medical diagnosis or prescriptions

Encourages professional help if self-harm or suicidal intent is detected

Maintains short, supportive tone

# ⚠ Limitations

Not clinically validated

No real crisis hotline integration

No persistent database logging

No advanced moderation filtering

Depends on external API availability

# 📈 Future Improvements

Add self-harm keyword detection layer

Integrate crisis hotline auto-display

Add user authentication

Add conversation export feature

Deploy using Streamlit Cloud / Docker

Add moderation filtering pipeline

# 🎯 Purpose

This project demonstrates:

LLM API integration

Prompt engineering with safety boundaries

Conversational UI development

Responsible AI system design

# 📜 License

This project is for educational and portfolio purposes.

## Author

C Raghuveer Kasyap  
AI & ML Enthusiast | LLM Application Developer
