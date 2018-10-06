import datetime
import speech_recognition as recognition

print(recognition.__version__)


def time_displayer(_string):
    current_time = datetime.datetime.now()
    print(_string + str(current_time))


def create_instance():
    recognizer = recognition.Recognizer();
    microphone = recognition.Microphone();
    with microphone as source:
        print("Say Something: ")
        audio: recognition.AudioData = recognizer.listen(source, phrase_time_limit=5)
        print(type(audio))
        parse_response = audio_recognizer(audio, recognizer)

    return parse_response


def audio_recognizer(_audio, _recognizer):
    """
    This function is a helper function to parse the speech within a selected period.
    This function is also thread safe.
    :param _recognizer: recognizer
    :param _audio: audio file
    :param _lock: thread lock
    :return: raw string acquired from audio file
    """
    if not isinstance(_audio, recognition.AudioData):
        raise TypeError("'_audio' must be 'AudioFile' instance")
    if not isinstance(_recognizer, recognition.Recognizer):
        raise TypeError("'_recognizer' must be 'recognition.Recognizer()' instance")

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = _recognizer.recognize_google(_audio)
    except recognition.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except recognition.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

