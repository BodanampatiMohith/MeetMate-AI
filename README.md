🎙️ MeetMate AI

MeetMate AI is an AI-powered Streamlit web application that lets users upload MP3 audio files (like meeting recordings, podcasts, lectures, etc.) and get instant transcription and smart summaries using Whisper and Gemini (Google Generative AI).

🧠 What It Does
📤 Upload an .mp3 file

🎧 Uses Whisper to transcribe the audio into text

🧾 Uses Gemini (via LangChain) to generate a human-like summary of the content

💬 Displays both the transcript and the summary in a user-friendly interface

🔍 Tech Stack
Tool	Purpose
Streamlit	Web UI
Whisper (OpenAI)	Audio Transcription
Google Gemini (via LangChain)	Text Summarization
Python	Core language
FFmpeg	Audio processing dependency
dotenv	Environment variable management

📂 Folder Structure
bash
Copy
Edit
meetmate1ai/
│
├── app.py                # Streamlit frontend
├── transcribe.py         # Handles Whisper transcription
├── summarize.py          # Summarizes using Gemini API
├── requirements.txt      # All dependencies
├── .env                  # Contains your API key (not committed)
⚙️ Installation & Run Locally
🔹 Requirements: Python 3.8+, FFmpeg installed, valid Gemini API key

1. Clone the Repo
bash
Copy
Edit
git
cd meetmate-ai
3. Create Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # for Windows
4. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
5. Add Google Gemini API Key
Create a .env file and add:

env
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
5. Run the App
bash
Copy
Edit
streamlit run app.py
Then open the URL shown in the terminal (usually http://localhost:8501)

📦 requirements.txt
txt
Copy
Edit
streamlit
openai-whisper
ffmpeg-python
python-dotenv
langchain
langchain-google-genai
📝 Example Use Case
Upload an .mp3 of a Zoom meeting.

Automatically get a full transcript and a bullet-point summary.

Perfect for students, professionals, researchers, and creators.

🛡️ Disclaimer
This project uses the Gemini API from Google and Whisper from OpenAI. Ensure you comply with the Google Generative AI usage policy and OpenAI usage policy.

👨‍💻 Author
Bodanampati Mohith
CSE (AIML)
Reg No: 23BAI0131
GitHub


![{4D972019-6062-434B-96EC-EE08FB95AC6D}](https://github.com/user-attachments/assets/c86209ec-0bf4-414a-ad03-4e4a61b97bb4)
![{8E6C5058-2042-4EFF-8DA8-3FF5C583D8BC}](https://github.com/user-attachments/assets/beb76c69-278e-4a8e-bb16-a6016c1db7fa)
