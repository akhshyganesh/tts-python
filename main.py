# tts_utils.py

from TTS.api import TTS
import os

import sounddevice as sd


class TextToSpeech:
    def __init__(self, model_name: str = "tts_models/en/ljspeech/tacotron2-DDC"):
        """
        Initializes the TTS engine with a given model.
        Default model is Tacotron2-DDC on LJSpeech (English).
        """
        self.tts = TTS(model_name)
        
    def speak(self, text: str):
        print(f"[TTS] Speaking: {text}")
        # Generate audio as numpy array
        wav = self.tts.tts(text)
        # Play audio directly
        sd.play(wav, samplerate=22050)  # Adjust samplerate if needed
        sd.wait()

    # def speak(self, text: str):
    #     """
    #     Speak the given text through the default audio output.
    #     """
    #     print(f"[TTS] Speaking: {text}")
    #     self.tts.tts_to_file(text=text, file_path="output.wav")
    #     os.system("play output.wav" if os.name != "nt" else "start output.wav")

    def save(self, text: str, path: str = "output.wav"):
        """
        Save the spoken version of the text to a file.
        """
        print(f"[TTS] Saving audio to: {path}")
        self.tts.tts_to_file(text=text, file_path=path)

# Example usage
if __name__ == "__main__":
    tts = TextToSpeech()
    tts.speak("Great news! Today was a wonderful day and I received a surprise gift from my friend.")
    tts.speak("However, I have some sad news too. I checked my lottery ticket and unfortunately, I did not win this time.")

