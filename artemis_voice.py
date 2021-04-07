import pyttsx3
import speech_recognition as sr

# I am using Pyttsx3 for text to speech in Python
# sapi5 is Macrisoft speech application (0 or 1 in the voices table for male or female voice)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def ask_for(question):
    print(question)
    speak(question)
    tempvar = listen()
    return tempvar


def add_in_dict(data):
    pers_datas = open("pers_datas.txt", "w")
    pers_datas.write(str(data))
    pers_datas.close()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.adjust_for_ambient_noise(source)
        # r.pause_threshold = 2
        # r.listen(source, timeout=4)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='fr-fr')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"

    return query
