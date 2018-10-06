<<<<<<< HEAD
import Input_io
import speech_recognition
import Langprocessor

commands = None

def record():
    microphone = speech_recognition.Microphone();
    recognizer = speech_recognition.Recognizer();
    input = Input_io.Input_io(recognizer,microphone)
    response = input.response();

    return response


record()
=======
import Input_io

def record():
    response = Input_io.create_instance()
>>>>>>> 3d30c23bc4cf08e7682e8cc1a396ae10ca3281b5
