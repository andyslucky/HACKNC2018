import threading
import datetime

import speech_recognition as recognition
from speech_recognition import AudioFile

start_time = datetime.datetime.now()
start_time_arr = str(start_time).split(" ")
start_time_current = start_time_arr[1].split(":")
start_time_second = start_time_current[2]
print("Start: " + str(start_time))
print(recognition.__version__)

recognizer = recognition.Recognizer();

harvard: AudioFile = recognition.AudioFile("harvard.wav");

lock = threading.Lock()


def audio_helper(_audio, _lock):
    """
    This function is a helper function to parse the speech within a selected period.
    This function is also thread safe.
    :param _audio: audio file
    :param _lock: thread lock
    :return: raw string acquired from audio file
    """
    # Thread lock will stop the race condition from multiple thread trying to access one audio file.
    with _lock:
        audio_helper_speech = recognizer.recognize_sphinx(_audio)

    return audio_helper_speech


source: AudioFile
with harvard as source:
    print("file duration is:" + str(source.DURATION))
    audio = recognizer.record(source, duration=source.DURATION)
    speech = audio_helper(audio, lock)
    print(speech.split(" "))


end_time = datetime.datetime.now()
end_time_arr = str(end_time).split(" ")
end_time_current = end_time_arr[1].split(":")
end_time_second = end_time_current[2]
print("End: " + str(end_time))
print(float(end_time_second) - float(start_time_second))
