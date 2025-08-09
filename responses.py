# responses.py

import random

def detect_emotion(user_input):
    text = user_input.lower()
    if any(word in text for word in ["sad", "lonely", "depressed", "upset"]):
        return "sad"
    elif any(word in text for word in ["angry", "annoyed", "frustrated"]):
        return "angry"
    elif any(word in text for word in ["happy", "great", "good", "excited"]):
        return "happy"
    elif any(word in text for word in ["anxious", "worried", "nervous", "panic"]):
        return "anxious"
    elif any(word in text for word in ["die", "suicide", "hurt myself", "worthless"]):
        return "crisis"
    else:
        return "neutral"

def get_response(emotion):
    responses = {
        "sad": [
            "I'm here for you. Do you want to talk about what's making you feel this way?",
            "Sometimes just letting it out helps. I'm listening."
        ],
        "angry": [
            "It's okay to feel angry. Want to try a short breathing exercise?",
            "Let’s talk it out—what made you feel this way?"
        ],
        "happy": [
            "Yay! I love hearing that. What made you feel good today?",
            "That’s amazing—keep riding that wave!"
        ],
        "anxious": [
            "Take a deep breath. You’re safe. Want to try a 4-7-8 breathing technique?",
            "Anxiety comes and goes. Want a grounding exercise?"
        ],
        "crisis": [
            "Please know you’re not alone. Talk to a trusted adult or call a helpline immediately.",
            "You are valuable and loved. If you're in danger, reach out to emergency support now."
        ],
        "neutral": [
            "Thanks for sharing. How about journaling a bit about your day?",
            "I'm always here to chat—how are you really feeling?"
        ]
    }
    return random.choice(responses.get(emotion, responses["neutral"]))
