import Input_io
import speech_recognition
import threading
import Langprocessor

def record(callback,ui):
    microphone = speech_recognition.Microphone();
    recognizer = speech_recognition.Recognizer();
    input = Input_io.Input_io(recognizer,microphone)
    response = input.response();
    try:
        if "on" in response['transcription']:
            callback(True)
        else:
            callback(False)
    except Exception as e:
        print(e)
    ui.listeningThread = None
    #return response

def parseResponse(response):
    output = response['transcription']
    return output






