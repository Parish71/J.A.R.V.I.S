# speech_handler.py
import sys
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')

def record_and_recognize_audio(testing=False):
    """
    Records audio from the microphone and recognizes the speech.
    If testing is True, it will return a test string instead.
    """
    if testing:
        # Return a predefined string for testing purposes
        return "Test input"

    # Initialize the recognizer and text-to-speech engine
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
        except sr.UnknownValueError:
            print("Unknown error occurred.")

    return ""

def speak_text(text):
    """
    Converts text to speech and speaks it out loud.
    """
    engine.say(text)
    engine.runAndWait()


