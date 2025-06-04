import threading
import speech_recognition as sr

class LiveRecognizer:
    def __init__(self, callback):
        self.callback = callback
        self.listening = False
        self.recognizer = sr.Recognizer()

    def start(self):
        self.listening = True
        threading.Thread(target=self._listen_loop, daemon=True).start()

    def stop(self):
        self.listening = False

    def _listen_loop(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                while self.listening:
                    try:
                        audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                        text = self.recognizer.recognize_google(audio).strip()
                        if text:
                            self.callback(text)
                    except sr.UnknownValueError:
                        self.callback("⚠️ Could not understand.")
                    except sr.RequestError as e:
                        self.callback(f"⚠️ API Error: {e}")
        except Exception as e:
            self.callback(f"⚠️ Microphone error: {e}")
