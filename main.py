import subprocess

import pyaudio
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import random
import os
import struct
import ast
import Artemis.light_gestion as lights_master
import Artemis.database_handling as db
import Artemis.switches_gestion as sg
import Artemis.artemis_voice as av
import Artemis.file_gestion as fg
import Artemis.artemis_voice_mark2 as av2


def test_sources_micro():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


def startIA():
    filesize = os.path.getsize("pers_datas.txt")
    # checking if it's the first time i launch it
    pers_datas = ""
    if filesize != 0:
        # pers_datas = ast.literal_eval(file.read())
        pers_datas = fg.read_json()
        print(pers_datas)
        IAName = fg.read_spec_json('IA', 'IAName')

        currenthour = int(datetime.datetime.now().hour)
        # mnbacksentences = ['Nice to see you back sir', 'I am on fire, tell me if you need anything', 'Hello, hello ']
        mnbacksentencesfr = ['Heureux de vous revoir monsieur', 'Comment puis je vous aider ?',
                             IAName + ', pour vous servir']
        bs = random.choice(mnbacksentencesfr)
        print(bs)
        av.speak(bs)

    else:
        intro = "Bonjour, pardonnez moi mais qui suis-je ?"
        name = av.ask_for(intro)
        av.speak(name + ",heureux de vous rencontrer")
        fg.write_json("IA", "IAName", name)

    return pers_datas


def init_services():
    sg.store_switch_init()


if __name__ == '__main__':

    pa = None
    audio_stream = None

    try:
        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=av2.handle.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=av2.handle.frame_length)

        print('[Listening ...]')

        while True:
            pcm = audio_stream.read(av2.handle.frame_length)
            pcm = struct.unpack_from("h" * av2.handle.frame_length, pcm)
            av2.handle.process(pcm)
    except KeyboardInterrupt:
        print('Stopping ...')

        # pcm = av2.audio_stream.read(av2.handle.frame_length)
        # audio_frame = struct.unpack_from("h" * av2.handle.frame_length, pcm)
        # av2.handle.process(audio_frame)

    # lights_master.light_on(fg.ip_address("Lights", "chambre"))
    # init_services()
    # sg.find_switches()
    # sg.turn_off("fontaine")
    # init()
    # lights_master.identify_bulbs()
    # fg.write_json_details("Lights", "chambre", "ip", "192.168.0.17")

    # clear = lambda: os.system('cls')
    # pers_datas = {}
    # pers_datas = init()
    # lights_master.light_command("192.168.0.17")
    # Don't know yet if it's necessary to use a database or just a Json file.
    # default port is 27017
    # db.init_database(27017, pers_datas)
