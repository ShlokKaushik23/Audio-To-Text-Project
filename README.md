#  Multilingual Audio-to-Text Transcription using Whisper

A simple web app that converts `.mp3` audio files into accurate text transcriptions using OpenAI's Whisper model, all through a clean and responsive Streamlit interface.

---

##  Supported Languages

-  English  
-  Spanish  
-  German  and more

The app automatically detects the spoken language using Whisper’s multilingual capabilities.

---

##  Features

- Upload `.mp3` audio files
- Select Whisper model (`tiny`, `base`, `small`, `medium`, `large`)
- Automatic language detection
- Streamlit web interface
- Real-time transcription display
- Download transcription as `.txt` file

---

##  Installation Guide (No Prebuilt Virtual Env)

I can't upload the prebuilt `whisper-env` due to size limits (1,5GB) limit on Github : 100MB, follow these steps manually:

---

###  Step 1: Install Python 3.10, openai-whisper 

> Whisper and PyTorch don’t work properly on Python 3.12.

bash
pip install openai-whisper
pip install torch
pip install ffmpeg-python

- Download from: https://www.python.org/downloads/release/python-3100/
- During installation, check  “Add Python to PATH”

---

###  Step 2: Clone or Download This Project

```bash
git clone https://github.com/ShlokKaushik23/Audio-To-Text-Project
cd AudioToText
