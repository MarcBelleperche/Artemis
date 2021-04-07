import pyaudio
from picovoice import Picovoice
import speech_recognition as sr
import struct
import pvporcupine
import os

# Now using a specific file for the voice. Better structure to don't get confused.
# Looking foward to use picovoice to train model to have a clear understanding model and actions.
# Did't got all the subtilities of it but soon enough

abs_path = os.path.abspath('src')
keyword_path = abs_path + "/keyword/artemis_windows_2021-05-07-utc_v1_9_0.ppn"
model_path = abs_path + "/keyword/porcupine_params_fr.pv"


def wake_word_callback():
    print("GOT THE NAME")


context_path = abs_path + "/context/Lights_fr_windows_2021-05-07-utc_v1_6_0.rhn"
context_model_path = abs_path + "/context/rhino_params_fr.pv"


def inference_callback(inference):
    print("GOT inference")
    print(inference.is_understood)
    if inference.is_understood:
        control = inference.intent
        print(control)
        if control == "power":
            for state, location in inference.slots.items():
                # print(control[location] + ":"+control[state])
                print("    %s : '%s'" % (state, location))


handle = Picovoice(
    keyword_path=keyword_path,
    porcupine_model_path=model_path,
    porcupine_sensitivity=0.5,
    wake_word_callback=wake_word_callback,
    context_path=context_path,
    rhino_sensitivity=0.5,
    rhino_model_path=context_model_path,
    inference_callback=inference_callback)


def get_next_audio_frame():
    pass
