import Input_io
import speech_recognition
import Langprocessor

commands = None
response = None
def record():
    microphone = speech_recognition.Microphone();
    recognizer = speech_recognition.Recognizer();
    input = Input_io.Input_io(recognizer,microphone)
    response = input.response();

    return response

def getReponse():
    return response
