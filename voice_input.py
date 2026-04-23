import speech_recognition as sr

def get_voice_text():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Adjusting for noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("🎤 Speak now...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        print("🔍 Recognizing...")
        text = recognizer.recognize_google(audio)
        print("✅ You said:", text)

        return text.lower()

    except sr.WaitTimeoutError:
        print("⏱️ No speech detected (timeout)")
        return ""

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""

    except sr.RequestError as e:
        print(f"🌐 API error: {e}")
        return ""

    except OSError as e:
        print(f"🎤 Microphone error: {e}")
        return ""