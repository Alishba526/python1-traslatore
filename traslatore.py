import streamlit as st
from translate import Translator

# Custom CSS for glassmorphism effect and colorful design
st.markdown(
    """
    <style>
    /* Glassmorphism effect for the main container */
    .stApp {
        background-image: url('https://img.freepik.com/free-vector/realistic-glass-effect-background_52683-74487.jpg?ga=GA1.1.690664293.1741270361&semt=ais_hybrid');
        background-size: cover;
        background-position: center;
    }
    .main-container {
        background: rgba(21, 14, 14, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;t
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.8);
        color: #333;
        border-radius: 10px;
    }
    .stButton button {
        background-color: rgb(7, 80, 10);
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSelectbox div {
        background-color: rgba(255, 255, 255, 0.8);
        color: #333;
        border-radius: 10px;
    }
    .stSuccess {
        color: #28a745;
        font-size: 18px;
    }
    .stWarning {
        color: #ffc107;
        font-size: 18px;
    }
    .stError {
        color: rgb(173, 18, 34);
        font-size: 18px;
    }
    /* Highlight box for translated text */
    .translation-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main container with glassmorphism effect
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title of the app with an emoji
st.title("🌍 All-in-One Translator")

# Input text area with a placeholder
text = st.text_area("Enter text to translate:", "Hello, how are you?", height=130)

# Language selection with a colorful header
st.markdown("### 🎯 Select Target Language")
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Hindi": "hi",
    "Arabic": "ar",
    "Russian": "ru",
    "Urdu": "ur",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Pashto": "ps",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Odia": "or",
    "Assamese": "as",
    "Bhojpuri": "bh",
}
target_lang = st.selectbox("Choose a language:", list(languages.keys()))

# Translate button with a colorful design
if st.button("🚀 Translate"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text to translate.")
    else:
        try:
            translator = Translator(to_lang=languages[target_lang])
            translation = translator.translate(text)
            st.success("✅ Translation:")
            # Display translated text in a highlighted box
            st.markdown(
                f'<div class="translation-box"><strong>{translation}</strong></div>',
                unsafe_allow_html=True,
            )
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")

# Footer with a colorful note
st.markdown("---")
st.markdown("Made with ❤️ by Alishba Rehman")

# Close the main container
st.markdown('</div>', unsafe_allow_html=True)
