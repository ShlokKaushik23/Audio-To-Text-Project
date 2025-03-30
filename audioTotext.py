import whisper
import os

def transcribe_audio(mp3_file_path):
    # Error handling case if file not found
    if not os.path.exists(mp3_file_path):
        raise FileNotFoundError(f"File not found: {mp3_file_path}")

    print("Loading Whisper model...")
    model = whisper.load_model("base") # I am using Best Model However we can use other models like tiny, small, base, medium and Large

    # Transcribe the audio
    print(f"Transcribing '{mp3_file_path}'...")
    result = model.transcribe(mp3_file_path)

    print("\n--- Transcription ---")
    print(result['text'])

    return result['text']


if __name__ == "__main__":
    audio_path = "german.mp3"  
    transcribe_audio(audio_path)
