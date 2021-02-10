import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import random
import os

# I am using Pyttsx3 for text to speech in Python
# sapi5 is Macrisoft speech application (0 or 1 in the voices table for male or female voice)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def init(pers_datas):
    filesize = os.path.getsize("pers_datas.txt")
    # checking if it's the first time i launch it
    if filesize != 0:
        with open("pers_datas.txt") as file:
            for line in file:
                (key, val) = line.split()
                pers_datas[int(key)] = val

        currenthour = int(datetime.datetime.now().hour)
        mnbacksentences = ['Nice to see you back sir', 'I am on fire, tell me if you need anything', 'Hello, hello '
                                                                                                   'handsome man']
        bs = random.choice(mnbacksentences)
        print(bs)
        speak(bs)

    else:
        pers_datas = open("pers_datas.txt", "w")
        intro = "Nice to meet you Sir, I am a bit confused. Who am I ?"
        print(intro)
        speak(intro)
        # please only say the name :
        name = listen()
        speak(name + "glad to be introduced")
        dict = {'IAName': name}
        pers_datas.write(dict)
        pers_datas.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    pers_datas = {}
    init(pers_datas)
