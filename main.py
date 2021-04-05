import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import random
import os
import ast
import Artemis.light_gestion as lights_master
import Artemis.database_handling as db
import Artemis.file_gestion as fg

# I am using Pyttsx3 for text to speech in Python
# sapi5 is Macrisoft speech application (0 or 1 in the voices table for male or female voice)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def test_sources_micro():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


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


def init():
    filesize = os.path.getsize("pers_datas.txt")
    # checking if it's the first time i launch it
    if filesize != 0:
        # pers_datas = ast.literal_eval(file.read())
        pers_datas = fg.read_json()
        print(pers_datas)
        IAName = fg.read_spec_json('IA','IAName')

        currenthour = int(datetime.datetime.now().hour)
        # mnbacksentences = ['Nice to see you back sir', 'I am on fire, tell me if you need anything', 'Hello, hello ']
        mnbacksentencesfr = ['Heureux de vous revoir monsieur', 'Comment puis je vous aider ?',
                             IAName + ', pour vous servir']
        bs = random.choice(mnbacksentencesfr)
        print(bs)
        speak(bs)

    else:
        intro = "Bonjour, pardonnez moi mais qui suis-je ?"
        name = ask_for(intro, "IAName")
        speak(name + ",heureux de vous rencontrer")
        fg.write_json("IA", "IAName", name)

    return pers_datas


def ask_for(question, info):
    print(question)
    speak(question)
    tempvar = listen()
    dict = {info: tempvar}
    add_in_dict(dict)
    return tempvar


def add_in_dict(data):
    pers_datas = open("pers_datas.txt", "w")
    pers_datas.write(str(data))
    pers_datas.close()


if __name__ == '__main__':
    # clear = lambda: os.system('cls')
    pers_datas = {}
    pers_datas = init()
    # lights_master.light_command("192.168.0.17")

    # Don't know yet if it's necessary to use a database or just a Json file.
    # default port is 27017
    # db.init_database(27017, pers_datas)
