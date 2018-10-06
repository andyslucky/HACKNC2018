import Input_io
import speech_recognition
import Langprocessor

def record():
    microphone = speech_recognition.Microphone();
    recognizer = speech_recognition.Recognizer();
    input = Input_io.Input_io(recognizer,microphone)
    response = input.response();

    if "on" in response['transcription']:
        return True
    else:
        return False
    #return response

def parseResponse(response):
    output = response['transcription']
    return output






