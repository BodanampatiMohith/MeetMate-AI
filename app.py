import streamlit as st
from transcribe import transcribe_audio
from summarize import generate_summary
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="🎙️ MeetMate AI", layout="wide")
st.title("🎙️ MeetMate AI – AI-Powered Meeting Minutes Generator")
st.markdown("Upload your meeting audio (.mp3 or .wav) and get instant transcript + summary.")

# Audio uploader
audio_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])

if audio_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=audio_file.name) as tmp_file:
        tmp_file.write(audio_file.read())
        tmp_path = tmp_file.name

    st.audio(tmp_path, format="audio/mp3")
    
    if st.button("🧠 Generate Transcript & Summary"):
        with st.spinner("Transcribing with Whisper..."):
            transcript = transcribe_audio(tmp_path)
            st.subheader("📝 Transcript")
            st.markdown(transcript)

        with st.spinner("Summarizing with Gemini..."):
            summary = generate_summary(transcript)
            st.subheader("📋 Summary & Action Items")
            st.markdown(summary)

        os.remove(tmp_path)
