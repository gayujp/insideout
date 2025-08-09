import streamlit as st
import json
from datetime import datetime
from responses import detect_emotion, get_response

MOOD_LOG = "mood_data.json"

# 🌸 BEAUTIFICATION CSS
import streamlit as st

# 💗 Pink background + heart tiles + font styling (Final fix)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand&display=swap');

    html, body, .css-18e3th9 {
        font-family: 'Quicksand', sans-serif;
        background: linear-gradient(to right, #ffccd5, #ffe6f0);
        background-image: url("https://em-content.zobj.net/source/telegram/358/sparkling-heart_1f496.png");
        background-repeat: repeat;
        background-size: 80px;
    }

    .css-1d391kg, .css-1dp5vir {  /* Force transparent containers */
        background-color: rgba(255,255,255,0.85) !important;
        border-radius: 20px;
        padding: 1rem;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }

    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 8px;
    }

    .stButton button {
        background-color: #ff80aa;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1.2rem;
        font-weight: bold;
        border: none;
    }

    </style>
""", unsafe_allow_html=True)


# 🌸 UI Start
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<div class="title">💗 MindMate – Your Mental Health Buddy</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">I’m here to check in with your feelings. Let’s talk 💬</div>', unsafe_allow_html=True)

# 🌸 Chat Input
user_input = st.text_input("Type how you're feeling today:")

if user_input:
    emotion = detect_emotion(user_input)
    bot_reply = get_response(emotion)
    st.markdown(f"🤖 **MindMate**: {bot_reply}")

# 🌸 Mood Logging
st.markdown("----")
st.subheader("📝 Mood Journal & Self-Care Tracker")

if st.checkbox("Log your mood today 💖"):
    mood_rating = st.slider("How would you rate your mood? (1 = Low, 10 = High)", 1, 10)
    journal_note = st.text_area("Jot down your thoughts here:", placeholder="Today, I feel...")
    if st.button("Save Entry", type="primary"):
        data = {"date": str(datetime.now()), "mood": mood_rating, "note": journal_note}
        try:
            with open(MOOD_LOG, "r") as f:
                logs = json.load(f)
        except FileNotFoundError:
            logs = []
        logs.append(data)
        with open(MOOD_LOG, "w") as f:
            json.dump(logs, f, indent=4)
        st.success("✨ Mood entry saved! You're doing great 🌈")

st.markdown("</div>", unsafe_allow_html=True)

# 🌸 Footer
st.markdown("---")
st.markdown("💡 _Note: This chatbot is for emotional support only. If you're in crisis, please contact a professional or helpline immediately._")
