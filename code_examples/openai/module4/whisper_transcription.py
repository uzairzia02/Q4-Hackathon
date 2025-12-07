import openai
import os

# Ensure you have your OpenAI API key set as an environment variable
# export OPENAI_API_KEY='YOUR_API_KEY'

def transcribe_audio_file(audio_file_path):
    """
    Transcribes an audio file using OpenAI's Whisper API.

    Args:
        audio_file_path (str): The path to the audio file (e.g., .mp3, .wav).

    Returns:
        str: The transcribed text.
    """
    if not os.path.exists(audio_file_path):
        print(f"Error: Audio file not found at {audio_file_path}")
        return None

    try:
        with open(audio_file_path, "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcript.text
    except openai.APIError as e:
        print(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Create a dummy audio file for demonstration purposes
    # In a real scenario, this would be an actual recording
    dummy_audio_file = "dummy_command.mp3"
    try:
        # Requires pydub and ffmpeg for actual dummy audio generation
        # For simplicity, we'll just create an empty file or assume it exists
        if not os.path.exists(dummy_audio_file):
            with open(dummy_audio_file, "w") as f:
                f.write("") # Placeholder for actual audio content

        print(f"Transcribing {dummy_audio_file}...")
        # Note: A real audio file is needed for successful transcription.
        # This example will likely fail if dummy_command.mp3 is truly empty or not a valid audio format.
        transcribed_text = transcribe_audio_file(dummy_audio_file)
        if transcribed_text:
            print(f"Transcribed Text: '{transcribed_text}'")
        else:
            print("Transcription failed or returned empty.")
    finally:
        # Clean up dummy file if created
        if os.path.exists(dummy_audio_file):
             os.remove(dummy_audio_file)
             print(f"Cleaned up {dummy_audio_file}")
