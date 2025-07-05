import os
import tempfile
import whisper

def transcribe_audio(audio_path):
    """
    Transcribes audio from the given file path using OpenAI Whisper.
    """
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        return f"❌ Error during transcription: {e}"
