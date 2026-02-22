from gtts import gTTS
import os

def text_to_speech(script_text):
    """
    Converts script text into an MP3 audio file.
    Returns the audio file path.
    """

    output_path = "voice.mp3"

    tts = gTTS(text=script_text, lang="en")
    tts.save(output_path)

    return output_path