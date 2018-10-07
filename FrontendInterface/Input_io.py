import datetime
import speech_recognition as recognition

class Input_io:
    def __init__(self, recognizer, microphone):
        self.recognizer = recognizer
        self.microphone = microphone
        self.audio = None;


    def time_displayer(_string):
        current_time = datetime.datetime.now()
        print(_string + str(current_time))

    def audio_recognizer(self):
        """
        This function is a helper function to parse the speech within a selected period.
        This function is also thread safe.
        :param _recognizer: recognizer
        :param _audio: audio file
        :param _lock: thread lock
        :return: raw string acquired from audio file
        """
        if not isinstance(self.audio, recognition.AudioData):
            raise TypeError("'_audio' must be 'AudioFile' instance")
        if not isinstance(self.recognizer, recognition.Recognizer):
            raise TypeError("'_recognizer' must be 'recognition.Recognizer()' instance")

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }
        try:
            response["transcription"] = self.recognizer.recognize_google(self.audio)
        except recognition.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except recognition.UnknownValueError:
            response["error"] = "Unable to recognize speech"

        return response

    def response(self):
        preparedResponse = {}
        buffer = ""
        while True:
            with self.microphone as source:
                print("Say Something: ")
                self.audio = self.recognizer.listen(source,phrase_time_limit=2)
                print("Waiting...")
                preparedResponse = self.audio_recognizer()
                if "transcription" in preparedResponse and preparedResponse['transcription'] is not None:
                    buffer +=(" "+ preparedResponse['transcription'])
                    if "on" in buffer.lower() or "off" in buffer.lower():
                        break
        preparedResponse['transcription'] = buffer
        print(buffer)
        return preparedResponse

