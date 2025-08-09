import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
import time

# Set page configuration
st.set_page_config(layout="centered")

# Set soft pink background and dark text
def set_bg_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffe6f0;
            color: #1a1a1a;
        }
        h1, h2, h3, h4 {
            color: #1a1a1a;
        }
        .stTextInput > div > div > input,
        .stTextArea > div > textarea,
        .stSelectbox > div > div {
            background-color: #fff5fa;
            color: #1a1a1a;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_color()
# Button and input styling
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #ff66a3;
        color: white;
        border: none;
        padding: 0.5em 1em;
        border-radius: 10px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #ff3385;
        color: white;
    }
    input {
        background-color: #fff5fa !important;
        color: #1a1a1a !important;
    }
    ::placeholder {
        color: #777 !important;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    /* Fix input text color */
    input, textarea {
        background-color: #fff0f5 !important;
        color: #222 !important;
    }

    /* Fix placeholder text */
    ::placeholder {
        color: #555 !important;
        opacity: 1 !important;
    }

    /* Dropdowns and selectboxes */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #fff0f5;
        color: #222;
    }

    /* General text color fix */
    * {
        color: #1f1f1f;
    }
    </style>
""", unsafe_allow_html=True)



st.title("🌸 Inside Out🌸")

# File paths
mood_file = "mood_log.csv"
journal_file = "journal_entries.csv"

# Mood options with emoji
mood_emoji = {
    "Happy": "😊",
    "Sad": "😢",
    "Angry": "😠",
    "Anxious": "😰",
    "Tired": "😴"
}

# Mood logging
st.header("📅 How are you feeling today?")
selected_mood = st.selectbox("Choose your mood", list(mood_emoji.keys()))

if st.button("Log Mood"):
    now = datetime.now()
    entry = {
        "date": now.strftime("%Y-%m-%d"),
        "mood": selected_mood,
        "emoji": mood_emoji[selected_mood]
    }
    if os.path.exists(mood_file):
        df = pd.read_csv(mood_file)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])
    df.to_csv(mood_file, index=False)
    st.success(f"Mood logged: {selected_mood} {mood_emoji[selected_mood]}")

# Mood tracker chart
if os.path.exists(mood_file):
    df = pd.read_csv(mood_file)
    df["date"] = pd.to_datetime(df["date"], errors='coerce')
    df = df.dropna(subset=["date", "mood"])
    st.subheader("📈 Mood Tracker Over Time")
    mood_counts = df.groupby(["date", "mood"]).size().unstack(fill_value=0)
    st.line_chart(mood_counts)

# Mood-based journaling
st.header("📓 Journal Your Thoughts")
if selected_mood:
    journal_input = st.text_area(f"What made you feel {selected_mood.lower()} today?")
    if st.button("Save Journal Entry"):
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "mood": selected_mood,
            "entry": journal_input
        }
        if os.path.exists(journal_file):
            journal_df = pd.read_csv(journal_file)
            journal_df = pd.concat([journal_df, pd.DataFrame([entry])], ignore_index=True)
        else:
            journal_df = pd.DataFrame([entry])
        journal_df.to_csv(journal_file, index=False)
        st.success("Journal entry saved!")

# Grounding techniques
st.header("🧘 Grounding Techniques")

with st.expander("🌬️ Breathing Exercise"):
    st.write("Follow the cycle below. One round includes inhale, hold, and exhale.")

    if st.button("Start Breathing Exercise"):
        st.write("Get ready...")
        time.sleep(1)
        phases = [("Inhale", 4), ("Hold", 4), ("Exhale", 4)]

        for i in range(2):  # Run 3 breathing rounds
            for phase, seconds in phases:
                with st.empty():
                    for t in range(seconds):
                        st.markdown(f"### {phase}... {seconds - t} sec")
                        time.sleep(1)
        st.success("Done! Great job.")


with st.expander("🖐️ 5-4-3-2-1 Grounding"):
    st.write("List the following to ground yourself:")
    st.text_input("🔍 5 things you can see")
    st.text_input("🖐️ 4 things you can feel")
    st.text_input("👂 3 things you can hear")
    st.text_input("👃 2 things you can smell")
    st.text_input("👅 1 thing you can taste")
