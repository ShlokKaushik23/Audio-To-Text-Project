import streamlit as st
import whisper
import os
import tempfile

# Sidebar for Model Selection
st.sidebar.title("Settings")
model_size = st.sidebar.selectbox(
    "Choose Whisper model:",
    options=["tiny", "base", "small", "medium", "large"],
    index=1  # default is "Base"
)

# It will load the model 
@st.cache_resource
def load_model(size):
    return whisper.load_model(size)

model = load_model(model_size)

st.title("Audio to Text Converter using Whisper")

uploaded_file = st.file_uploader("Upload an MP3 file", type=["mp3"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/mp3")

    if st.button("Transcribe"):
        with st.spinner(f"Transcribing using Whisper `{model_size}`..."):
            # Save uploaded file 
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
                temp_audio.write(uploaded_file.read())
                temp_audio_path = temp_audio.name

            
            result = model.transcribe(temp_audio_path)
            transcription = result["text"]

         
            st.subheader("📝 Transcription")
            st.write(transcription)

            # Download button for the Text File
            txt_filename = os.path.splitext(uploaded_file.name)[0] + f"_transcription_{model_size}.txt"
            st.download_button("💾 Download Transcription", transcription, file_name=txt_filename)

            os.remove(temp_audio_path)
